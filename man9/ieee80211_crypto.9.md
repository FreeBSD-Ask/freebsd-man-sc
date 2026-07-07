# ieee80211_crypto(9)

`ieee80211_crypto` — 802.11 加密支持

## 名称

`ieee80211_crypto`

## 概要

```c
#include <net80211/ieee80211_var.h>
```

```c
void
ieee80211_crypto_register(const struct ieee80211_cipher *)

void
ieee80211_crypto_unregister(const struct ieee80211_cipher *)

int
ieee80211_crypto_available(int cipher)
```

```c
void
ieee80211_notify_replay_failure(struct ieee80211vap *,
    const struct ieee80211_frame *, const struct ieee80211_key *,
    uint64_t rsc, int tid)

void
ieee80211_notify_michael_failure(struct ieee80211vap *,
    const struct ieee80211_frame *, u_int keyix)

int
ieee80211_crypto_newkey(struct ieee80211vap *, int cipher, int flags,
    struct ieee80211_key *)

int
ieee80211_crypto_setkey(struct ieee80211vap *, struct ieee80211_key *)

int
ieee80211_crypto_delkey(struct ieee80211vap *, struct ieee80211_key *)

void
ieee80211_key_update_begin(struct ieee80211vap *)

void
ieee80211_key_update_end(struct ieee80211vap *)

void
ieee80211_crypto_delglobalkeys(struct ieee80211vap *)

void
ieee80211_crypto_reload_keys(struct ieee80211com *)
```

```c
struct ieee80211_key *
ieee80211_crypto_encap(struct ieee80211_node *, struct mbuf *)

struct ieee80211_key *
ieee80211_crypto_decap(struct ieee80211_node *, struct mbuf *, int flags)

int
ieee80211_crypto_demic(struct ieee80211vap *, struct ieee80211_key *,
    struct mbuf *, int force)

int
ieee80211_crypto_enmic(struct ieee80211vap *, struct ieee80211_key *,
    struct mbuf *, int force)
```

## 描述

`net80211` 层包括对 802.11 协议的全面加密支持。提供了 WPA 和 802.11i 所需密码的软件实现，以及 802.11 帧的封装/解封处理。软件密码编写为内核模块，并向核心加密支持注册。加密框架支持驱动程序对密码的硬件加速，在驱动程序无法提供必要的硬件服务时自动回退到软件实现。

## 加密密码模块

`net80211` 密码模块使用 `ieee80211_crypto_register` 注册其服务，并提供描述其操作的模板。此 `ieee80211_cipher` 结构定义了与协议相关的状态，例如在封装/解封期间保留/移除的 802.11 头中的空间字节数，以及设置密钥和执行加密操作的入口点。

密码模块可以通过 `wk_private` 结构成员将私有状态关联到每个密钥。如果状态由模块设置，则在密钥销毁之前会调用它以回收资源。

加密模块可以通知系统两种事件。当识别到数据包重放事件时，可以使用 `ieee80211_notify_replay_failure` 发出信号。当检测到 `TKIP` Michael 失败时，可以调用 `ieee80211_notify_michael_failure`。驱动程序也可以使用这些例程发出硬件检测到的事件信号。

## 加密密钥管理

`net80211` 层为 WPA、802.1x 和 802.11i 等协议实现了每 vap 4 元素"全局密钥表"和每站"单播密钥"。全局密钥表设计用于支持传统 WEP 操作和多播/组密钥，但某些应用程序也使用它在站模式下实现 WPA。全局表中的密钥由 0-3 范围内的密钥索引标识。每站密钥由站的 MAC 地址标识，通常用于单播 PTK 绑定。

`net80211` 提供用于管理全局和每站密钥的 ioctl(2) 操作。驱动程序通常不参与软件密钥管理；它们仅在提供加密操作的硬件加速时才参与。

`ieee80211_crypto_newkey` 用于分配新的 `net80211` 密钥或重新配置现有密钥。必须指定密码以及任何固定的密钥索引。`net80211` 层将处理分配密码和驱动程序资源以支持密钥。

一旦分配了密钥，可以使用 `ieee80211_crypto_setkey` 设置其内容，并使用 `ieee80211_crypto_delkey` 删除（回收任何密码和驱动程序资源）。

`ieee80211_crypto_delglobalkeys` 用于回收 vap 全局密钥表中的所有密钥；通常仅在 `net80211` 层内部使用。

`ieee80211_crypto_reload_keys` 处理从软件密钥状态重新加载硬件密钥状态，例如在挂起/恢复周期之后所需。

## 驱动程序加密支持

驱动程序通过 `ieee80211com` 结构的 `ic_cryptocaps` 字段标识其具有硬件支持的密码。如果硬件支持可用，驱动程序还应填写为设备使用而创建的每个 `ieee80211vap` 的 `iv_key_alloc`、`iv_key_set` 和 `iv_key_delete` 方法。此外，可以设置 `iv_key_update_begin` 和 `iv_key_update_end` 方法来处理更新硬件密钥状态的同步要求。

当 `net80211` 分配软件密钥且驱动程序可以加速密码操作时，将调用 `iv_key_alloc` 方法。驱动程序可以返回与出站流量关联的令牌（用于加密帧）。否则（例如硬件资源不可用），驱动程序将不返回令牌，`net80211` 将安排在软件中完成工作，并将已准备好传输的帧传递给驱动程序。

对于接收，驱动程序用 `M_WEP` mbuf 标志标记帧，以指示硬件已解密有效载荷。如果帧的 802.11 头中标记了 `IEEE80211_FC1_PROTECTED` 位且未标记 `M_WEP`，则在软件中完成解密。对于更复杂的场景，将查阅软件密钥状态；例如，决定在硬件处理 TKIP 解密后是否需要在软件中完成 Michael 验证。

管理复杂密钥数据结构（例如将软件密钥故障转入硬件密钥缓存）的驱动程序可以通过调用 `ieee80211_key_update_begin` 和 `ieee80211_key_update_end` 包围其工作来安全地操作软件密钥状态。当接收流量处于活动状态时，这些调用还同步硬件密钥状态更新。

## 参见

ioctl(2), [wlan_ccmp(4)](../man4/wlan_ccmp.4.md), [wlan_tkip(4)](../man4/wlan_tkip.4.md), [wlan_wep(4)](../man4/wlan_wep.4.md), [ieee80211(9)](ieee80211.9.md)
