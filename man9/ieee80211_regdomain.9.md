# ieee80211_regdomain.9

`ieee80211_regdomain` — 802.11 监管支持

## 名称

`ieee80211_regdomain`

## 概要

```c
#include <net80211/ieee80211_var.h>
#include <net80211/ieee80211_regdomain.h>
```

```c
int
ieee80211_init_channels(struct ieee80211com *,
    const struct ieee80211_regdomain *,
    const uint8_t bands[])

void
ieee80211_sort_channels(struct ieee80211_channel *, int nchans)

struct ieee80211_appie *
ieee80211_alloc_countryie(struct ieee80211com *)
```

## 描述

`net80211` 软件层为驱动程序提供了一套支持框架，其中包括完备的监管支持。`net80211` 提供了由特权用户应用程序强制执行 *监管策略* 的机制。

驱动程序定义设备的能力，并可以拦截和控制通过 `net80211` 请求的监管变更。初始的监管状态（包括信道列表）必须由驱动程序在调用 `ieee80211_ifattach` 之前填入。信道列表应当反映设备 *校准* 可用的信道集合。该列表也可以稍后通过 `ieee80211com` 结构中的 `ic_getradiocaps` 方法来请求。`ieee80211_init_channels` 函数为那些未（或无法）填入合适信道列表的驱动程序提供基本的回退支持。系统会提供默认的监管状态，例如监管 SKU、ISO 国家代码、位置（例如室内、室外），以及设备能够工作的一组频段。`net80211` 用一组默认的信道和能力填充 `ic_channels` 中的信道表。注意此机制应谨慎使用，因为所创建的信道列表与设备能力之间的任何不匹配都可能导致运行时错误（例如请求在设备不支持的信道上工作）。SKU 和国家信息用于生成 802.11h 协议元素及相关操作（例如用于 802.11d）；驱动程序的错误设置并不致命，只是可能引起混淆。

没有固定/默认监管状态的设备可以将监管 SKU 设置为 `SKU_DEBUG`，国家代码设置为 `CTRY_DEFAULT`，将正确的设置留给用户应用程序。如果已知默认设置，可以安装它们，并且/或者使用 `ieee80211_notify_country` 向用户空间派发事件，以便 devd(8) 在系统引导时（或设备插入时）完成相应的设置工作。

使用 `ieee80211_sort_channels` 例程对信道表进行排序以优化查找。每当信道表内容被修改时都应执行此操作。

`ieee80211_alloc_countryie` 函数分配由 802.11h 规定的信息元素。由于生成代价较高，它被缓存在 `ic_countryie` 中，并且仅在监管状态变更时才生成。直接调用 `ieee80211_alloc_countryie` 的驱动程序不应协助进行此缓存工作；这样做可能会使 `net80211` 层产生混淆。

## 驱动程序监管控制

驱动程序可以通过重写 `ic_setregdomain` 方法（该方法检查变更请求）来控制监管变更请求。虽然驱动程序可以拒绝任何不符合其要求的请求，但建议在接受时宽容一些，并且只要可能，与其拒绝请求，不如将其修改为正确的。例如，如果某个信道的发射功率上限过高，驱动程序可以拒绝该请求，或者（更好的做法是）降低上限以使其符合要求。包含不可接受信道的请求应当被拒绝，否则可能在应用程序状态和 `net80211` 管理的状态之间产生不匹配。具体的操作规则仍在制定中。

## 参见

[regdomain(5)](../man5/regdomain.5.md), [ifconfig(8)](../man8/ifconfig.8.md), [ieee80211(9)](ieee80211.9.md)
