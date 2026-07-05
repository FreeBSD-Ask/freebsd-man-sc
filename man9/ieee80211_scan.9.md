# ieee80211_scan.9

`ieee80211_scan` — 802.11 扫描支持

## 名称

`ieee80211_scan`

## 概要

```c
#include <net80211/ieee80211_var.h>
```

```c
int
ieee80211_start_scan(struct ieee80211vap *, int flags,
    u_int duration, u_int mindwell, u_int maxdwell,
    u_int nssid, const struct ieee80211_scan_ssid ssids[])

int
ieee80211_check_scan(struct ieee80211vap *, int flags,
    u_int duration, u_int mindwell, u_int maxdwell,
    u_int nssid, const struct ieee80211_scan_ssid ssids[])

int
ieee80211_check_scan_current(struct ieee80211vap *)

int
ieee80211_bg_scan(struct ieee80211vap *, int)

int
ieee80211_cancel_scan(struct ieee80211vap *)

int
ieee80211_cancel_scan_any(struct ieee80211vap *)

int
ieee80211_scan_next(struct ieee80211vap *)

int
ieee80211_scan_done(struct ieee80211vap *)

int
ieee80211_probe_curchan(struct ieee80211vap *, int)

void
ieee80211_add_scan(struct ieee80211vap *,
    const struct ieee80211_scanparams *,
    const struct ieee80211_frame *, int subtype,
    int rssi, int noise)

void
ieee80211_scan_timeout(struct ieee80211com *)

void
ieee80211_scan_assoc_fail(struct ieee80211vap *,
    const uint8_t mac[IEEE80211_ADDR_LEN], int reason)

void
ieee80211_scan_flush(struct ieee80211vap *)

void
ieee80211_scan_iterate(struct ieee80211vap *,
    ieee80211_scan_iter_func, void *)

void
ieee80211_scan_dump_channels(const struct ieee80211_scan_state *)

void
ieee80211_scanner_register(enum ieee80211_opmode,
    const struct ieee80211_scanner *)

void
ieee80211_scanner_unregister(enum ieee80211_opmode,
    const struct ieee80211_scanner *)

void
ieee80211_scanner_unregister_all(const struct ieee80211_scanner *)

const struct ieee80211_scanner *
ieee80211_scanner_get(enum ieee80211_opmode)
```

## 描述

`net80211` 软件层为扫描提供了一个可扩展的框架。扫描是站点定位要加入的 BSS（在 infrastructure 和 IBSS 模式下）或要使用的信道（当作为 AP 或 IBSS 主节点工作时）的过程。扫描分为“主动”扫描和“被动”扫描。主动扫描会在访问每个信道时发送一个或多个 ProbeRequest 帧。被动扫描会访问扫描集合中的每个信道但不发送任何帧；站点只监听流量。注意，根据监管限制，主动扫描在发送 ProbeRequest 帧之前可能仍需先监听流量。

扫描操作涉及构造一组要检查的信道（扫描集合）、访问每个信道并收集信息（例如存在哪些 BSS），然后分析结果以做出决策（例如加入哪个 BSS）。此过程需要尽可能快，因此 `net80211` 会智能地构造扫描集合，并且只在信道上停留必要的时间。扫描结果会被缓存，扫描缓存用于在可能时避免扫描，并在 infrastructure 模式下工作时启用接入点之间的漫游。

扫描由实现各操作模式 *策略* 的可插拔模块处理。核心扫描支持提供了支持这些模块的基础设施，并向 `net80211` 层的其余部分导出通用 API。策略模块决定访问哪些信道、记录哪些状态以做出决策，并选择作为扫描结果返回的最终站点/信道。

在最初将 vap 带到工作状态时同步执行扫描，并可选地在后台进行以维护扫描缓存，用于漫游和非法 AP 监测。扫描与控制 vap 的 `net80211` 状态机无关，但与 `IEEE80211_S_SCAN` 状态相关联。同一时间只能有一个 vap 进行扫描；此调度策略在 `ieee80211_new_state` 中处理，对扫描代码是透明的。

扫描由一组参数控制，这些参数（潜在地）约束信道集合以及任何所需的 SSID 和 BSSID。`net80211` 附带一个标准扫描器模块，可与所有可用的操作模式配合工作，并支持“后台扫描”和“漫游”操作。

## 扫描器模块

扫描模块使用注册机制挂接到 `net80211` 层。使用 `ieee80211_scanner_register` 为特定操作模式注册扫描模块，使用 `ieee80211_scanner_unregister` 或 `ieee80211_scanner_unregister_all` 清除条目（通常在模块卸载时）。同一时间每个操作模式只能注册一个扫描器模块。

## 驱动程序支持

扫描操作通常由 `net80211` 层管理。驱动程序必须提供 `ic_scan_start` 和 `ic_scan_stop` 方法，分别在扫描开始和工作完成时调用；这些方法应处理诸如启用接收 Beacon 和 ProbeResponse 帧以及禁用任何 BSSID 匹配等工作。`ic_set_channel` 方法用于在扫描时改变信道。`net80211` 会生成 ProbeRequest 帧并使用 `ic_raw_xmit` 方法发送它们。扫描时收到的帧通过正常的接收路径分派给 `net80211`。将扫描工作卸载到固件的设备最易于与 `net80211` 配合的方式是按一次一个信道操作，因为这样将控制权交给 `net80211` 的扫描机调度器。但是如果驱动程序使用 `ieee80211_add_scan` 例程手动分派结果以将结果输入扫描缓存，则支持多信道扫描。

## 扫描请求

扫描请求通过 `IEEE80211_SCAN_REQUEST` ioctl 发出，或通过 vap 状态机中需要扫描的变更发出。在这两种情况下，都可以先检查扫描缓存，如果认为它足够“热”，则在不离开当前信道的情况下使用其内容。要在不检查缓存的情况下启动扫描，可以调用 `ieee80211_start_scan`；否则可以使用 `ieee80211_check_scan` 先检查扫描缓存，如果缓存内容过期则启动扫描。还有 `ieee80211_check_scan_current`，它是使用先前设置的扫描参数检查扫描缓存然后再扫描的简写形式。

后台扫描以协程方式使用 `ieee80211_bg_scan` 完成。对此例程的首次调用将启动一个后台扫描，运行一段有限的时间后返回到 BSS 信道。后续调用将遍历扫描集合直到访问完所有信道。通常这些后续调用会被定时，以允许接收接入点为站点缓存的帧。

如果扫描操作由指定的 vap 启动，可以使用 `ieee80211_cancel_scan` 取消；或使用 `ieee80211_cancel_scan_any` 强制终止，无论哪个 vap 启动了它。这些请求主要由 `net80211` 在发送路径中使用，以在要发送帧时取消后台扫描。驱动程序不应需要使用这些调用（或本页描述的大多数调用）。

`ieee80211_scan_next` 和 `ieee80211_scan_done` 例程对扫描集合进行显式迭代，通常不应被驱动程序使用。`ieee80211_probe_curchan` 处理在主动扫描期间访问信道时发送 ProbeRequest 帧的工作。当信道属性标记为 `IEEE80211_CHAN_PASSIVE` 时，此函数会安排在发送任何帧之前先接收 802.11 流量（以遵守监管限制）。

最小/最大驻留时间参数用于约束访问信道所花费的时间。最大驻留时间约束监听流量所花费的时间。最小驻留时间用于减少此时间——当达到该时间并且已收到一个或多个帧时，将立即进行信道切换。驱动程序可以通过 `iv_scan_mindwell` 方法覆盖此行为。

## 扫描缓存管理

扫描缓存内容由扫描策略模块管理，在该模块之外是不透明的。`net80211` 扫描框架定义了用于交互的 API。扫描缓存内容的有效性由 `iv_scanvalid` 控制，并通过 `IEEE80211_SCAN_VALID` 请求导出到用户空间。

可以使用 `ieee80211_scan_flush` 显式刷新缓存内容，或在启动扫描操作时设置 `IEEE80211_SCAN_FLUSH` 标志。

扫描缓存条目由 `ieee80211_add_scan` 例程创建；通常在收到 Beacon 或 ProbeResponse 帧时。现有条目通常会根据最新信息进行更新，但某些信息（如 RSSI 和噪声底值读数）可能会合并以呈现平均值。

缓存内容通过 `ieee80211_scan_timeout` 调用进行老化。通常这些调用与其他站点表活动一起发生；每 `IEEE80211_INACT_WAIT` 秒（默认 15 秒）一次。

单个缓存条目由 `ieee80211_scan_assoc_success` 标记为可用，由 `ieee80211_scan_assoc_fail` 标记为有故障，后者接受一个参数用于标识是对 Authentication/Association 请求无响应还是收到了否定响应（这可能加速缓存驱逐或将该条目列入黑名单）。

可以使用 `ieee80211_scan_iterate` 调用查看缓存内容。缓存条目以公共格式导出，并通过 `IEEE80211_SCAN_RESULTS` 请求导出给用户应用程序。

## 参见

ioctl(2), [ieee80211(9)](ieee80211.9.md), [ieee80211_proto(9)](ieee80211_proto.9.md)
