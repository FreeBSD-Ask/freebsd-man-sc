# ieee80211_proto.9

`ieee80211_proto` — 802.11 状态机支持

## 名称

`ieee80211_proto`

## 概要

```c
#include <net80211/ieee80211_var.h>
```

```c
void
ieee80211_start_all(struct ieee80211com *)

void
ieee80211_stop_all(struct ieee80211com *)

void
ieee80211_suspend_all(struct ieee80211com *)

void
ieee80211_resume_all(struct ieee80211com *)
```

```c
enum ieee80211_state;

int
ieee80211_new_state(struct ieee80211vap *, enum ieee80211_state, int)
```

```c
void
ieee80211_wait_for_parent(struct ieee80211com *)
```

## 描述

支持 802.11 设备驱动程序的 `net80211` 层使用状态机控制 vap 的操作。这些状态机根据 vap 操作模式而变化。站模式状态机遵循协议规范中的 802.11 MLME 状态。其他状态机更简单，反映操作工作如扫描 BSS 或自动选择操作信道。当多个 vap 运行时，状态机用于协调操作如选择信道。状态机机制还用于将 `net80211` 层绑定到驱动程序；这在下面有更多描述。

为状态机定义了以下状态：

**`IEEE80211_S_INIT`** 默认/初始状态。处于此状态的 vap 不应持有任何动态状态（例如节点表中关联站的条目）。驱动程序必须使硬件静默；例如，不应有中断触发。

**`IEEE80211_S_SCAN`** 扫描 BSS 或选择操作信道。注意，扫描也可以在其他状态下进行（例如当后台扫描活动时）；此状态在最初将 vap 带到操作状态或事件（如站模式下的信标丢失）之后进入。

**`IEEE80211_S_AUTH`** （在站模式下）向接入点认证。此状态通常在选择 BSS 后从 `IEEE80211_S_SCAN` 到达，但如果认证握手失败，也可能从 `IEEE80211_S_ASSOC` 或 `IEEE80211_S_RUN` 到达。

**`IEEE80211_S_ASSOC`** （在站模式下）关联到接入点。此状态在成功认证后从 `IEEE80211_S_AUTH` 到达，或如果收到 DisAssoc 帧则从 `IEEE80211_S_RUN` 到达。

**`IEEE80211_S_CAC`** 正在进行信道可用性检查（CAC）。此状态仅在启用 DFS 且选择用于操作的信道需要 CAC 时进入。

**`IEEE80211_S_RUN`** 操作状态。在此状态下，vap 可以传输数据帧、接受站关联请求等。注意，数据流量还受关联"端口"是否授权的限制。当 WPA/802.11i/802.1x 运行时，授权可能单独发生；例如在站模式下，wpa_supplicant(8) 必须完成握手并配置必要的密钥，端口才会被授权。在此状态下，BSS 可操作，关联状态有效且可使用；例如，`ic_bss` 和 `ic_bsschan` 保证可用。

**`IEEE80211_S_CSA`** 信道切换通告（CSA）待处理。此状态仅在从 `IEEE80211_S_RUN` 收到接入点的 CSA（在站模式下）或本地站准备更改信道时到达。在此状态下，流量可能会根据 CSA 中的静默设置而被静默。

**`IEEE80211_S_SLEEP`** （在站模式下）休眠以节省功耗。此状态仅在启用省电操作且本地站被认为足够空闲以进入低功耗模式时从 `IEEE80211_S_RUN` 到达。

注意，状态是有序的（如上所示）；例如，vap 必须处于 `IEEE80211_S_RUN` 或"更高"状态才能传输帧。某些 `net80211` 数据仅在特定状态下有效；例如，指定操作 BSS 信道的 `iv_bsschan` 除了在 `IEEE80211_S_RUN` 或更高状态外，永远不应使用。

## 状态变化

状态机变化通常在 `net80211` 层内部处理，以响应 ioctl(2) 请求、接收到的帧或外部事件（如信标丢失）。`ieee80211_new_state` 函数用于在 vap 上启动状态机变化。提供新状态和可选参数。请求最初被处理以处理多个 vap 的协调。例如，一次只能有一个 vap 进行扫描，如果多个 vap 请求更改为 `IEEE80211_S_SCAN`，第一个将被允许运行，其他将被*推迟*直到扫描操作完成，届时将采用所选信道。同样，`net80211` 处理 vap 组合的协调，例如 AP 和站 vap，其中站可能需要漫游以跟随其关联的 AP（将 AP vap 拖到新信道）。另一个重要的协调是 `IEEE80211_S_CAC` 和 `IEEE80211_S_CSA` 的处理。一次最多只能有一个 vap 主动更改状态。实际上，`net80211` 在专用的 [taskqueue(9)](taskqueue.9.md) 线程中单线程化状态机逻辑，该线程还用于同步扫描和信标丢失处理等工作。

完成多 vap 调度/协调后，调用每 vap 的 `iv_newstate` 方法执行状态变化工作。驱动程序使用此入口设置私有状态，然后使用先前定义的方法指针将调用调度到 `net80211` 层（用 OOP 术语来说，它们调用"超级方法"）。

`net80211` 特殊处理两个状态变化。转换到 `IEEE80211_S_RUN` 时，vap 传输队列上的 `IFF_DRV_OACTIVE` 位被清除，以便流量可以流动。转换到 `IEEE80211_S_INIT` 时，刷新与 vap 关联的扫描缓存中的任何状态，并刷新传输队列上待处理的任何帧。

## 驱动程序集成

驱动程序应覆盖 `iv_newstate` 方法以插入自己的代码并处理状态变化所需的设置工作。否则，驱动程序必须调用 `ieee80211_start_all` 以响应通过 `SIOCSIFFLAGS` ioctl 请求标记为 up，并且应使用 `ieee80211_suspend_all` 和 `ieee80211_resume_all` 实现挂起/恢复支持。

还有一个 `ieee80211_stop_all` 调用强制所有 vap 到 `IEEE80211_S_INIT` 状态，但驱动程序不需要此调用；控制通常由 `net80211` 处理，或者在卡弹出或 vap 销毁的情况下，工作将在驱动程序外部启动。

## 参见

ioctl(2), wpa_supplicant(8), [ieee80211(9)](ieee80211.9.md), [ifnet(9)](ifnet.9.md), [taskqueue(9)](taskqueue.9.md)

## 历史

状态机概念是最初出现于 NetBSD 1.5 的原始 `ieee80211` 代码库的一部分。
