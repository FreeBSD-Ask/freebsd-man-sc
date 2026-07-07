# ecn(9)

`ecn` — 用于隧道封装/解封装的 IP ECN 接口

## 名称

`ecn`, `ip_ecn_ingress`, `ip_ecn_egress`, `ip6_ecn_ingress`, `ip6_ecn_egress`

## 概要

```c
#include <sys/netinet/ip_ecn.h>
#include <sys/netinet6/ip6_ecn.h>
```

### 常量

```c
ECN_COMPLETE ECN_ALLOWED ECN_FORBIDDEN ECN_NOCARE
```

### ECN 操作函数

```c
void
ip_ecn_ingress(int mode, uint8_t *outer, const uint8_t *inner)

void
ip6_ecn_ingress(int mode, uint32_t *outer, const uint32_t *inner)

int
ip_ecn_egress(int mode, uint8_t *outer, const uint8_t *inner)

int
ip6_ecn_egress(int mode, uint32_t *outer, const uint32_t *inner)
```

## 描述

`ip_ecn_ingress` 和 `ip_ecn_egress` 接口为隧道封装（ingress）和解封装（egress）实现显式拥塞通知（ECN）处理。它们操作 IP Type of Service (TOS) 或 IPv6 Traffic Class (TCLASS) 头字段中的 ECN 位。这些函数在 `ip_ecn_egress` 的 `ECN_ALLOWED` 模式下实现了 RFC6040 的标准规范，并在 `ip_ecn_ingress` 中额外提供了 `ECN_FORBIDDEN` 模式作为兼容模式。

### 接口

操作 `ip_tos` 和 `ipv6_flow` 的函数如下：

`ip_ecn_ingress` `ip6_ecn_ingress` 在封装时（ingress）根据 `struct ip` 中 `ip_tos` 字段或 `struct ip6_hdr` 中 `ip6_flow` 字段的 ECN 位进行 ECN 处理，从 `inner` 到 `outer`。它还会将 DSCP 值从 `inner` 复制到 `outer`。

`ip_ecn_egress` `ip6_ecn_egress` 在解封装时（egress）根据 `outer` 到 `inner` 的 ECN 位进行 ECN 处理。`ECN_ALLOWED` 模式可能修改 `inner` 的 ECN 位，或通过返回 `ECN_WARN` 或 `ECN_ALARM` 值指示调用者丢弃或记录。

`ip_ecn_egress` 的返回码如下：

**`ECN_DROP`** (0) 调用者必须丢弃该数据包。

**`ECN_SUCCESS`** (1) 处理成功；inner ECN 位可能已被更新。

**`ECN_WARN`** (2) 处理成功；调用者可对异常 ECN 组合记录警告。

**`ECN_ALARM`** (3) 处理成功；调用者应记录，并可对严重 ECN 异常发出告警。

函数处理以下模式：

**`ECN_COMPLETE`** RFC6040 中定义的常规模式。ECN 位在封装过程中保留；解封装遵循 RFC6040 规则，并在检测到潜在危险数据包时返回 `ECN_WARN` 或 `ECN_ALARM` 值。

**`ECN_ALLOWED`** RFC6040 中定义的常规模式，不带安全检查。ECN 位在封装过程中保留；解封装遵循 RFC6040 规则。

**`ECN_FORBIDDEN`** 兼容模式。封装时剥离 ECN，解封装时将丢弃外层头部携带 CE 的数据包。此模式不应在 `ip_ecn_egress` 或 `ip6_ecn_egress` 中使用，因为 `ECN_ALLOWED` 模式已涵盖 RFC6040 中规定的所有可能场景。

**`ECN_NOCARE`** 保留 ECN 位不变并忽略。

### IPV6 处理

IPv6 接口 `ip6_ecn_ingress` 和 `ip6_ecn_egress` 从 32 位 `ip6_flow` 中提取 8 位 DSCP 和 ECN 值，并将其插入到 IPv4 等效接口中。

## 参见

[ip(4)](../man4/ip.4.md), [ip6(4)](../man4/ip6.4.md), [ipsec(4)](../man4/ipsec.4.md)

## 历史

历史上 `ip_ecn_egress` 使用布尔风格的返回值。当前 API 保留了丢弃（ECN_DROP == 0）和成功（ECN_SUCCESS == 1）的数值映射，但定义了额外的非零状态码（ECN_WARN、ECN_ALARM）。仅测试非零成功的调用者将继续把 WARN/ALARM 视为成功。

## 作者

Pouria Mousavizadeh Tehrani <pouria@FreeBSD.org>
