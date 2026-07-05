# crypto_request.9

`crypto_request` — 对称密码学操作

## 名称

`crypto_request`

## 概要

```c
#include <opencrypto/cryptodev.h>

struct cryptop *
crypto_clonereq(crypto_session_t cses, struct cryptop *crp, int how)

int
crypto_dispatch(struct cryptop *crp)

int
crypto_dispatch_async(struct cryptop *crp, int flags)

void
crypto_dispatch_batch(struct cryptopq *crpq, int flags)

void
crypto_destroyreq(struct cryptop *crp)

void
crypto_freereq(struct cryptop *crp)

struct cryptop *
crypto_getreq(crypto_session_t cses, int how)

void
crypto_initreq(struct cryptop *crp, crypto_session_t cses)

void
crypto_use_buf(struct cryptop *crp, void *buf, int len)

void
crypto_use_mbuf(struct cryptop *crp, struct mbuf *m)

void
crypto_use_uio(struct cryptop *crp, struct uio *uio)

void
crypto_use_vmpage(struct cryptop *crp, vm_page_t *pages, int len,
    int offset)

void
crypto_use_output_buf(struct cryptop *crp, void *buf, int len)

void
crypto_use_output_mbuf(struct cryptop *crp, struct mbuf *m)

void
crypto_use_output_uio(struct cryptop *crp, struct uio *uio)

void
crypto_use_output_vmpage(struct cryptop *crp, vm_page_t *pages,
    int len, int offset)
```

## 描述

内核中的每个对称密码学操作由 `struct cryptop` 的实例描述，并与一个活动会话关联。

请求可以动态分配，也可以使用调用者提供的存储。动态分配的请求应通过 `crypto_getreq` 或 `crypto_clonereq` 分配，并在请求完成后通过 `crypto_freereq` 释放。使用调用者提供存储的请求，应在每次操作开始时通过 `crypto_initreq` 初始化，并在请求完成后通过 `crypto_destroyreq` 销毁。

对于 `crypto_clonereq`、`crypto_getreq` 和 `crypto_initreq`，`cses` 是对活动会话的引用。对于 `crypto_clonereq` 和 `crypto_getreq`，`how` 被传递给 [malloc(9)](malloc.9.md)，应设置为 `M_NOWAIT` 或 `M_WAITOK`。

`crypto_clonereq` 分配一个新请求，该请求继承原始 `crp` 请求的请求输入（例如请求缓冲区）。但是，新请求与 `cses` 会话关联，而不是从 `crp` 继承会话。`crp` 不能是已完成的请求。

请求初始化后，调用者应设置结构中的字段以描述请求特定的参数。未使用的字段应保持原样。

`crypto_dispatch`、`crypto_dispatch_async` 和 `crypto_dispatch_batch` 函数将一个或多个密码学请求传递给附加到该请求会话的驱动程序。如果请求字段中有错误，这些函数可向调用者返回错误。如果在服务请求时遇到错误，则会改为通过 `crp_etype` 报告给请求的回调函数（`crp_callback`）。

注意，请求的回调函数可能在 `crypto_dispatch` 返回之前被调用。

请求一旦通过回调函数发出完成信号，就应通过 `crypto_destroyreq` 或 `crypto_freereq` 释放。

密码学操作包含若干字段来描述请求。

### 请求缓冲区

请求可以指定单个原地修改的数据缓冲区（`crp_buf`），也可以指定独立的输入（`crp_buf`）和输出（`crp_obuf`）缓冲区。注意，压缩模式请求不支持独立的输入和输出缓冲区。

所有请求必须具有由以下函数之一初始化的有效 `crp_buf`：

`crypto_use_buf` 使用 `buf` 所指向的 `len` 字节数组作为数据缓冲区。

`crypto_use_mbuf` 使用网络内存缓冲区 `m` 作为数据缓冲区。

`crypto_use_uio` 使用分散/聚集列表 `uio` 作为数据缓冲区。

`crypto_use_vmpage` 使用 `vm_page_t` 结构数组作为数据缓冲区。

对于使用独立输入和输出缓冲区的请求，应使用以下函数之一初始化 `crp_obuf`：

`crypto_use_output_buf` 使用 `buf` 所指向的 `len` 字节数组作为输出缓冲区。

`crypto_use_output_mbuf` 使用网络内存缓冲区 `m` 作为输出缓冲区。

`crypto_use_output_uio` 使用分散/聚集列表 `uio` 作为输出缓冲区。

`crypto_use_output_vmpage` 使用 `vm_page_t` 结构数组作为输出缓冲区。

### 请求区域

每个请求在数据缓冲区中描述一个或多个区域。每个区域由相对于数据缓冲区起始处的偏移量和长度描述。某些区域的长度对于属于一个会话的所有请求都是相同的。这些长度在关联会话的会话参数中设置。所有请求都必须定义一个有效载荷区域。其他区域仅在特定会话模式下才需要。

对于使用独立输入和输出数据缓冲区的请求，AAD、IV 和有效载荷区域始终定义为输入缓冲区中的区域。此外，还需定义一个独立的有效载荷输出区域，用于在输出缓冲区中保存加密或解密的输出。摘要区域对于验证现有摘要的请求，描述输入数据缓冲区中的一个区域。对于计算摘要的请求，摘要区域描述输出数据缓冲区中的一个区域。注意，写入输出缓冲区的唯一数据是加密或解密结果和任何计算出的摘要。AAD 和 IV 区域不会从输入缓冲区复制到输出缓冲区，而仅用作输入。

定义了以下区域：

嵌入的附加认证数据

嵌入的 IV 或 nonce

要加密、解密、压缩或解压缩的数据

加密或解密后的数据

认证摘要、哈希或标签

| **区域** | **缓冲区** | **描述** |
| -------- | ---------- | -------- |
| AAD | 输入 | |
| IV | 输入 | |
| 有效载荷 | 输入 | |
| 有效载荷输出 | 输出 | |
| 摘要 | 输入/输出 | |

| **区域** | **起始** | **长度** |
| -------- | -------- | -------- |
| AAD | `crp_aad_start` | `crp_aad_length` |
| IV | `crp_iv_start` | `csp_ivlen` |
| 有效载荷 | `crp_payload_start` | `crp_payload_length` |
| 有效载荷输出 | `crp_payload_output_start` | `crp_payload_length` |
| 摘要 | `crp_digest_start` | `csp_auth_mlen` |

允许请求仅操作数据缓冲区的一个子集。例如，来自 IPsec 的请求所操作的网络数据包包含既不用作附加认证数据（AAD）也不用作有效载荷数据的头部。

### 请求操作

所有请求必须在 `crp_op` 中指定要执行的操作类型。可用操作取决于会话的模式。

压缩请求支持以下操作：

**`CRYPTO_OP_COMPRESS`** 压缩数据缓冲区中有效载荷区域的数据。

**`CRYPTO_OP_DECOMPRESS`** 解压缩数据缓冲区中有效载荷区域的数据。

密码请求支持以下操作：

**`CRYPTO_OP_ENCRYPT`** 加密数据缓冲区中有效载荷区域的数据。

**`CRYPTO_OP_DECRYPT`** 解密数据缓冲区中有效载荷区域的数据。

摘要请求支持以下操作：

**`CRYPTO_OP_COMPUTE_DIGEST`** 对数据缓冲区中的有效载荷区域计算摘要，并将结果存储到摘要区域。

**`CRYPTO_OP_VERIFY_DIGEST`** 对数据缓冲区中的有效载荷区域计算摘要。将计算出的摘要与摘要区域中的现有摘要进行比较。如果摘要匹配，则成功完成请求。如果摘要不匹配，则请求以 `EBADMSG` 失败。

AEAD 和"先加密后认证"请求支持以下操作：

**`CRYPTO_OP_ENCRYPT |`** `CRYPTO_OP_COMPUTE_DIGEST` 加密数据缓冲区中有效载荷区域的数据。对 AAD 和有效载荷区域计算摘要，并将结果存储到数据缓冲区。

**`CRYPTO_OP_DECRYPT |`** `CRYPTO_OP_VERIFY_DIGEST` 对数据缓冲区中的 AAD 和有效载荷区域计算摘要。将计算出的摘要与摘要区域中的现有摘要进行比较。如果摘要匹配，则解密有效载荷区域。如果摘要不匹配，则以 `EBADMSG` 失败该请求。

### 请求 AAD

AEAD 和"先加密后认证"请求可选择性地包含附加认证数据。AAD 可以在输入缓冲区的 AAD 区域中提供，也可以作为由 `crp_aad` 指向的单个缓冲区提供。无论哪种情况，`crp_aad_length` 始终指示 AAD 的字节量。

### 请求 ESN

IPsec 请求可选择性地包含扩展序列号（ESN）。ESN 可以在 `crp_esn` 中提供，也可以作为 `crp_aad` 所指向的 AAD 的一部分提供。

如果 ESN 存储在 `crp_esn` 中，应在 `csp_flags` 中设置 `CSP_F_ESN`。此用例专用于"加密并认证"模式，因为序列号的高 32 位被附加到 Next Header 之后（RFC 4303）。

AEAD 模式在独立的 AAD 缓冲区中提供 ESN（参见例如 RFC 4106，第 5 章 AAD 构造）。

### 请求 IV 和/或 Nonce

某些密码学操作需要 IV 或 nonce 作为输入。IV 可以存储在数据缓冲区的 IV 区域中，也可以存储在 `crp_iv` 中。默认情况下，假定 IV 存储在 IV 区域中。如果 IV 存储在 `crp_iv` 中，应在 `crp_flags` 中设置 `CRYPTO_F_IV_SEPARATE`，并将 `crp_iv_start` 保持为零。

如果请求将部分（而非全部）IV 存储在数据缓冲区中，应将部分 IV 存储在数据缓冲区中，并通过 `crp_iv` 单独传递完整 IV。

### 请求和回调调度

密码学框架提供了多种方法来调度向驱动程序分发请求以及处理驱动程序回调。`crypto_dispatch`、`crypto_dispatch_async` 和 `crypto_dispatch_batch` 函数可用于请求不同的分发调度策略。

`crypto_dispatch` 同步地将请求传递给驱动程序。驱动程序本身可以同步或异步处理请求，具体取决于驱动程序是由软件还是硬件实现。

`crypto_dispatch_async` 异步地分发请求。如果驱动程序本身是同步的，请求会被排队到由工作线程池支持的任务队列。这种方式允许来自单个生产者的请求并行处理，从而提高吞吐量。默认情况下，该池为每个 CPU 分配一个线程。工作线程将请求出队并异步地传递给驱动程序。`crypto_dispatch_async` 额外接受一个 `flags` 参数。`CRYPTO_ASYNC_ORDERED` 标志指示请求的完成回调必须按请求分发的相同顺序调用。如果驱动程序是异步的，`crypto_dispatch_async` 的行为与 `crypto_dispatch` 相同。

`crypto_dispatch_batch` 允许调用者收集一批请求并同时提交给驱动程序。这允许硬件驱动程序优化请求处理调度和批量完成中断。批量提交通过在每个请求上调用驱动程序的 process 方法来实现，对除最后一个请求外的每个请求指定 `CRYPTO_HINT_MORE`。`crypto_dispatch_batch` 的 `flags` 参数目前被忽略。

回调函数调度比请求调度更简单。回调可以由 `crypto_done` 同步调用，也可以排队到工作线程池。该工作线程池默认也为每个 CPU 分配一个工作线程。注意，由 `crypto_done` 同步调用的回调函数必须遵循与线程化中断处理程序相同的限制。

默认情况下，回调由工作线程异步调用。如果设置了 `CRYPTO_F_CBIMM`，回调始终由 `crypto_done` 同步调用。如果设置了 `CRYPTO_F_CBIFSYNC`，回调在请求由软件驱动程序处理时同步调用，在请求由硬件驱动程序处理时异步调用。

如果请求以 `CRYPTO_ASYNC_ORDERED` 调度到任务队列，回调将始终异步调用，忽略 `CRYPTO_F_CBIMM` 和 `CRYPTO_F_CBIFSYNC`。IPsec 使用此标志，以确保解密后的网络数据包按大致接收时的顺序向上传递到网络栈。

### 其他请求字段

除了上面枚举的字段和标志外，`struct cryptop` 还包括以下字段：

**`crp_session`** 对活动会话的引用。这在由 `crypto_getreq` 创建请求时设置，不应修改。驱动程序可使用它获取特定于驱动程序的会话状态或会话参数。

**`crp_etype`** 错误状态。成功时为零，请求失败时为错误。由驱动程序在通过 `crypto_done` 完成请求之前设置。

**`crp_flags`** 标志的位掩码。

**`crp_cipher_key`** 指向请求特定加密密钥的指针。如果未设置此值，请求使用会话加密密钥。

**`crp_auth_key`** 指向请求特定认证密钥的指针。如果未设置此值，请求使用会话认证密钥。

**`crp_opaque`** 不透明指针。此指针允许密码学框架的用户存储有关请求的信息，以便在回调中使用。

**`crp_callback`** 回调函数。这必须指向类型为 `void (*)(struct cryptop *)` 的回调函数。回调函数应检查 `crp_etype` 以确定已完成操作的状态。它还应安排通过 `crypto_freereq` 释放请求。

**`crp_olen`** 用于压缩和解压缩请求，描述数据缓冲区中有效载荷区域的更新长度。如果压缩请求增加了有效载荷的大小，则数据缓冲区不修改，请求成功完成，并将 `crp_olen` 设置为压缩数据本应使用的大小。调用者可将其与有效载荷区域长度进行比较，以确定压缩数据是否被丢弃。

## 返回值

`crypto_dispatch` 在请求包含无效字段时返回错误，请求有效时返回零。`crypto_getreq` 成功时返回指向新请求结构的指针，失败时返回 `NULL`。仅当 `how` 中传入 `M_NOWAIT` 时才可能返回 `NULL`。

## 参见

[ipsec(4)](../man4/ipsec.4.md), [crypto(7)](../man7/crypto.7.md), [crypto(9)](crypto.9.md), [crypto_session(9)](crypto_session.9.md), [mbuf(9)](mbuf.9.md), [uio(9)](uio.9.md)

## 缺陷

并非所有驱动程序都能正确处理在单个会话中混合使用会话密钥和每请求密钥。消费者应要么在会话参数中为会话指定单个密钥，要么始终使用每请求密钥。
