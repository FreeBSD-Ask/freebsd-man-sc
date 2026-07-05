# crypto_driver.9

`crypto_driver` — 对称密码学驱动程序接口

## 名称

`crypto_driver`

## 概要

```c
#include <opencrypto/cryptodev.h>

void
crypto_copyback(struct cryptop *crp, int off, int size, const void *src)

void
crypto_copydata(struct cryptop *crp, int off, int size, void *dst)

void
crypto_done(struct cryptop *crp)

int32_t
crypto_get_driverid(device_t dev, size_t session_size, int flags)

void *
crypto_get_driver_session(crypto_session_t crypto_session)

void
crypto_read_iv(struct cryptop *crp, void *iv)

int
crypto_unblock(uint32_t driverid, int what)

int
crypto_unregister_all(uint32_t driverid)

int
CRYPTODEV_FREESESSION(device_t dev, crypto_session_t crypto_session)

int
CRYPTODEV_NEWSESSION(device_t dev, crypto_session_t crypto_session,
    const struct crypto_session_params *csp)

int
CRYPTODEV_PROBESESSION(device_t dev,
    const struct crypto_session_params *csp)

int
CRYPTODEV_PROCESS(device_t dev, struct cryptop *crp, int flags)

void
hmac_init_ipad(struct auth_hash *axf, const char *key, int klen,
    void *auth_ctx)

void
hmac_init_opad(struct auth_hash *axf, const char *key, int klen,
    void *auth_ctx)
```

## 描述

对称密码学驱动程序处理由消费者提交到与该驱动程序关联的会话的密码学请求。

密码学驱动程序调用 `crypto_get_driverid` 向密码学框架注册。`dev` 是用于服务请求的设备。`CRYPTODEV` 方法定义在附加到 `dev` 的设备驱动程序的方法表中。`session_size` 指定由密码学框架分配的特定于驱动程序的每会话结构的大小。`flags` 是关于驱动程序属性的位掩码。必须指定 `CRYPTOCAP_F_SOFTWARE` 或 `CRYPTOCAP_F_HARDWARE` 中的恰好一个。`CRYPTOCAP_F_SOFTWARE` 应用于使用主机 CPU 处理请求的驱动程序。`CRYPTOCAP_F_HARDWARE` 应用于在独立的协处理器上处理请求的驱动程序。对于在 `CRYPTODEV_PROCESS` 中同步处理请求的驱动程序，应设置 `CRYPTOCAP_F_SYNC`。对于使用加速 CPU 指令的软件驱动程序，应设置 `CRYPTOCAP_F_ACCEL_SOFTWARE`。`crypto_get_driverid` 返回一个不透明的驱动程序标识。

`crypto_unregister_all` 从密码学框架中注销驱动程序。如果有任何待处理操作或打开的会话，此函数将休眠。`driverid` 是先前调用 `crypto_get_driverid` 返回的值。

当通过 `crypto_newsession` 创建新会话时，密码学框架会在每个活动驱动程序上调用 `CRYPTODEV_PROBESESSION` 以确定用于该会话的最佳驱动程序。此方法应检查 `csp` 中的会话参数。如果驱动程序不支持 `csp` 所描述的请求，此方法应返回一个错误值。如果驱动程序确实支持 `csp` 所描述的请求，它应返回一个负值。框架优先选择具有最大负值的驱动程序，类似于 [DEVICE_PROBE(9)](device_probe.9.md)。此方法为非错误返回值定义了以下值：

**`CRYPTODEV_PROBE_HARDWARE`** 驱动程序通过协处理器处理请求。

**`CRYPTODEV_PROBE_ACCEL_SOFTWARE`** 驱动程序使用优化指令（如 AES-NI）在主机 CPU 上处理请求。

**`CRYPTODEV_PROBE_SOFTWARE`** 驱动程序在主机 CPU 上处理请求。

此方法不应休眠。

一旦框架为会话选择了驱动程序，框架就会调用 `CRYPTODEV_NEWSESSION` 方法来初始化特定于驱动程序的会话状态。在调用此方法之前，框架会分配一个每会话的特定于驱动程序的数据结构。此结构以零初始化，其大小由传递给 `crypto_get_driverid` 的 `session_size` 设置。此方法可通过将 `crypto_session` 传递给 `crypto_get_driver_session` 来检索指向此数据结构的指针。会话参数在 `csp` 中描述。

此方法不应休眠。

`CRYPTODEV_FREESESSION` 在会话销毁时被调用，以释放任何特定于驱动程序的状态。在此方法返回后，每会话的特定于驱动程序的数据结构会被框架显式清零并释放。如果驱动程序不需要额外的拆除步骤，它可以保留此方法为未定义。

此方法不应休眠。

`CRYPTODEV_PROCESS` 为提交到活动会话的每个请求调用。此方法可以同步完成请求，也可以调度为异步完成，但绝不能休眠。

如果此方法由于资源不足（例如命令队列已满）而无法完成请求，它可以通过返回 `ERESTART` 来延迟该请求。该请求将由框架排队，并在驱动程序通过 `crypto_unblock` 释放待处理请求后重试。提交到属于该驱动程序的会话的任何请求也将被排队，直到调用 `crypto_unblock` 为止。

如果驱动程序在处理请求时遇到错误，应通过 `crp` 的 `crp_etype` 字段报告，而不是直接返回错误。

如果该驱动程序还有额外的请求排队，`flags` 可设置为 `CRYPTO_HINT_MORE`。驱动程序可以将其作为批量完成中断的提示。注意，这些额外的请求可能来自不同的会话。

`crypto_get_driver_session` 返回会话 `crypto_session` 的特定于驱动程序的每会话数据结构的指针。此函数可在 `CRYPTODEV_NEWSESSION`、`CRYPTODEV_PROCESS` 和 `CRYPTODEV_FREESESSION` 回调中使用。

`crypto_copydata` 将 `crp` 输入缓冲区中的 `size` 字节复制到 `dst` 所指向的本地缓冲区中。字节从请求输入缓冲区中偏移量 `off` 字节处开始读取。

`crypto_copyback` 将 `src` 所指向的本地缓冲区中的 `size` 字节复制到 `crp` 的输出缓冲区中。字节写入到请求输出缓冲区中偏移量 `off` 字节处开始。

`crypto_read_iv` 将 `crp` 的 IV 或 nonce 复制到 `iv` 所指向的本地缓冲区中。

驱动程序调用 `crypto_done` 将请求 `crp` 标记为已完成。在调用此函数之前，应在 `crp_etype` 中设置任何错误。

如果驱动程序通过从 `CRYPTO_PROCESS` 返回 `ERESTART` 来延迟请求，框架将排队该驱动程序的所有请求，直到驱动程序调用 `crypto_unblock` 指示临时资源短缺已得到缓解。例如，如果驱动程序由于命令环已满而返回 `ERESTART`，它将在使命令环条目可用的命令完成中断中调用 `crypto_unblock`。`driverid` 是 `crypto_get_driverid` 返回的值。`what` 指示驱动程序再次能够处理的请求类型：

**`CRYPTO_SYMQ`** 指示驱动程序能够处理传递给 `CRYPTODEV_PROCESS` 的对称请求。

`hmac_init_ipad` 准备一个认证上下文以生成 HMAC 的内部哈希。`axf` 是认证算法的软件实现，例如 `crypto_auth_hash` 返回的值。`key` 是指向 `klen` 字节 HMAC 密钥的指针。`auth_ctx` 指向所需算法的有效认证上下文。此函数使用提供的密钥初始化上下文。

`hmac_init_opad` 类似于 `hmac_init_ipad`，不同之处在于它准备认证上下文以生成 HMAC 的外部哈希。

## 返回值

`crypto_apply` 返回调用者提供的回调函数的返回值。

`crypto_contiguous_subsegment` 返回指向连续段的指针或 `NULL`。

`crypto_get_driverid` 成功时返回驱动程序标识，出错时返回 -1。

`crypto_unblock`、`crypto_unregister_all`、`CRYPTODEV_FREESESSION`、`CRYPTODEV_NEWSESSION` 和 `CRYPTODEV_PROCESS` 成功时返回零，失败时返回错误。

`CRYPTODEV_PROBESESSION` 成功时返回负值，失败时返回错误。

## 参见

[crypto(7)](../man7/crypto.7.md), [crypto(9)](crypto.9.md), [crypto_buffer(9)](crypto_buffer.9.md), [crypto_request(9)](crypto_request.9.md), [crypto_session(9)](crypto_session.9.md)
