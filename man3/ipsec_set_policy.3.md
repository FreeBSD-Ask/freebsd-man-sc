# ipsec_set_policy(3)

`ipsec_set_policy` — 从人类可读字符串创建 IPsec 策略结构

## 名称

`ipsec_set_policy`, `ipsec_get_policylen`, `ipsec_dump_policy`

## 库

libipsec

## 概要

`#include <netipsec/ipsec.h>`

```c
char *
ipsec_set_policy(const char *policy, int len);

int
ipsec_get_policylen(const char *buf);

char *
ipsec_dump_policy(c_caddr_t *buf, const char *delim);
```

## 描述

`ipsec_set_policy()` 函数从人类可读的策略规范生成 IPsec 策略规范结构 `struct sadb_x_policy` 和/或 `struct sadb_x_ipsecrequest`。策略规范必须作为 C 字符串给出，通过 `policy` 参数传递，字符串长度通过 `len` 给出。`ipsec_set_policy()` 函数返回指向包含正确格式的 IPsec 策略规范结构的缓冲区的指针。该缓冲区是动态分配的，必须使用 free(3) 库函数释放。

`ipsec_get_policylen()` 函数返回将规范结构传递给 setsockopt(2) 系统调用时所需的缓冲区长度。

`ipsec_dump_policy()` 函数将 IPsec 策略结构转换为人类可读的形式。`buf` 参数指向 IPsec 策略结构 `struct sadb_x_policy`。`delim` 是分隔符字符串，通常是空白字符。如果将 `delim` 设置为 `NULL`，则假定为单个空格。`ipsec_dump_policy()` 函数返回指向动态分配字符串的指针。调用者有责任使用 free(3) 库调用释放返回的指针。

`policy` 按以下方式给出：

`protocol` `/` `mode` `/` `src` `-` `dst` [`/level`] `protocol` 为以下之一：`ah`、`esp` 或 `ipcomp`，分别表示使用认证头（Authentication Header）、封装安全协议（Encapsulating Security Protocol）或 IP 压缩协议。`mode` 为 `transport` 或 `tunnel`，两种模式的含义在 [ipsec(4)](../man4/ipsec.4.md) 中描述。`src` 和 `dst` 指定源系统和目标系统的 IP 地址（v4 或 v6）。`src` 始终代表“发送节点”，`dst` 始终代表“接收节点”。当 `direction` 为 `in` 时，`dst` 是本节点，`src` 是远程节点或对等方。如果 `mode` 为 `transport`，`src` 和 `dst` 都可以省略。`level` 必须设置为以下之一：`default`、`use`、`require` 或 `unique`。`default` 表示内核应查阅由一组 [sysctl(8)](../man8/sysctl.8.md) 变量定义的默认安全策略。相关的 [sysctl(8)](../man8/sysctl.8.md) 变量在 [ipsec(4)](../man4/ipsec.4.md) 中描述。选择 `use` 时，可以使用相关的安全关联（SA）（如果可用），但不是必需的。如果 SA 可用，则数据包将由 IPsec 处理，即加密和/或认证，但如果 SA 不可用，则数据包将以明文传输。不建议使用 `use` 选项，因为它允许加密或认证链路变为未加密或未认证的意外错误配置，建议尽可能使用 `require` 关键字代替 `use`。使用 `require` 关键字意味着需要相关的 SA，内核必须对所有匹配的数据包执行 IPsec 处理。`unique` 关键字与 `require` 具有相同的效果，但增加了出站流量的 SA 仅用于此策略的限制。使用 setkey(8) 通过手动密钥定义 SA 时，可能需要标识符来关联策略和 SA。以这种方式在 `unique` 关键字后放置十进制数字作为标识符：`unique:number`，其中 `number` 必须在 1 到 32767 之间。如果 `request` 字符串保持无歧义，可以省略 `level` 及其前面的斜杠，但鼓励显式指定以避免意外行为。如果省略 `level`，将被解释为 `default`。

**`direction`** `discard` `direction` 必须为 `in` 或 `out`，指定策略应用于入站还是出站数据包。选择 `discard` 策略时，匹配策略的数据包将被丢弃。

**`direction`** `entrust` `entrust` 表示查阅内核中的安全策略数据库（SPD），由 setkey(8) 控制。

**`direction`** `bypass` `bypass` 方向表示不应进行 IPsec 处理，数据包将以明文传输。bypass 选项仅适用于特权套接字。

`direction` `ipsec` `request ...` `ipsec` 方向表示匹配的数据包由 IPsec 处理。`ipsec` 后可跟一个或多个 `request` 字符串，格式为：

注意，此处允许的规范与 setkey(8) 中有所不同。使用 setkey(8) 指定安全策略时，既不使用 entrust 也不使用 bypass。详情参见 setkey(8)。

## 返回值

`ipsec_set_policy()` 函数成功时返回指向包含策略规范的已分配缓冲区的指针；否则返回 NULL 指针。

`ipsec_get_policylen()` 函数成功时返回正值，指示缓冲区大小，出错时返回负值。

`ipsec_dump_policy()` 函数成功时返回指向动态分配区域（包含人类可读的安全策略）的指针，出错时返回 `NULL`。

## 实例

设置丢弃所有入站数据包的策略。

```sh
in discard
```

所有出站数据包要求由 IPsec 处理并使用 ESP 传输。

```sh
out ipsec esp/transport//require
```

所有入站数据包要求使用 AH 协议进行认证。

```sh
in ipsec ah/transport//require
```

通过 10.1.1.2 和 10.1.1.1 处的端点进行出站隧道数据包。

```sh
out ipsec esp/tunnel/10.1.1.2-10.1.1.1/require
```

## 参见

ipsec_strerror(3), [ipsec(4)](../man4/ipsec.4.md), setkey(8)

## 历史

这些函数首次出现在 WIDE/KAME IPv6 协议栈工具包中。

基于 KAME 项目（http://www.kame.net/）协议栈的 IPv6 和 IPsec 支持最初集成到 FreeBSD 4.0 中。
