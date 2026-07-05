# hash.9

`hash` — 通用内核哈希函数

## 名称

`hash`, `hash32`, `hash32_buf`, `hash32_str`, `hash32_strn`, `hash32_stre`, `hash32_strne`, `jenkins_hash`, `jenkins_hash32`, `murmur3_32_hash`, `murmur3_32_hash32`

## 概要

```c
#include <sys/hash.h>
```

```c
uint32_t
hash32_buf(const void *buf, size_t len, uint32_t hash)
uint32_t
hash32_str(const void *buf, uint32_t hash)
uint32_t
hash32_strn(const void *buf, size_t len, uint32_t hash)
uint32_t
hash32_stre(const void *buf, int end, const char **ep, uint32_t hash)
uint32_t
hash32_strne(const void *buf, size_t len, int end, const char **ep,
    uint32_t hash)
uint32_t
jenkins_hash(const void *buf, size_t len, uint32_t hash)
uint32_t
jenkins_hash32(const uint32_t *buf, size_t count, uint32_t hash)
uint32_t
murmur3_32_hash(const void *buf, size_t len, uint32_t hash)
uint32_t
murmur3_32_hash32(const uint32_t *buf, size_t count, uint32_t hash)
```

## 描述

`hash32` 函数用于为内核中的良好哈希算法提供一致且通用的接口。这些函数可用于哈希 ASCII `NUL` 终止字符串以及内存块。

`len` 参数是缓冲区的字节长度。`count` 参数是缓冲区的 32 位字长度。

`hash32_buf` 函数用作通用缓冲区哈希函数。`buf` 参数用于传递位置，`len` 是缓冲区的字节长度。`hash` 参数用于扩展现有哈希，或传递初始值 `HASHINIT` 来启动新哈希。

`hash32_str` 函数用于哈希 `buf` 中传递的 `NUL` 终止字符串，初始哈希值由 `hash` 给出。

`hash32_strn` 函数类似于 `hash32_str` 函数，区别在于它还接受 `len` 参数，这是预期字符串的最大长度。

`hash32_stre` 和 `hash32_strne` 函数是内核用于哈希路径名组件的辅助函数。这些函数有额外的终止条件，即在要哈希的字符串中找到由 `end` 给定的字符时终止。如果参数 `ep` 不为 `NULL`，它被设置为缓冲区中哈希函数终止哈希的位置。

`jenkins_hash` 函数与 `hash32_buf` 语义相同，但提供具有更好分布的更高级哈希算法。

`jenkins_hash32` 使用与 `jenkins_hash` 函数相同的哈希算法，但仅适用于 `uint32_t` 大小的数组，因此更简单且更快。它接受 `uint32_t` 值数组作为第一个参数，该数组的大小作为第二个参数。

`murmur3_32_hash` 和 `murmur3_32_hash32` 函数类似于 `jenkins_hash` 和 `jenkins_hash32`，但实现 MurmurHash3 的 32 位版本。

## 返回值

`hash32` 函数返回缓冲区或字符串的 32 位哈希值。

## 实例

```c
LIST_HEAD(head, cache) *hashtbl = NULL;
u_long mask = 0;
void
sample_init(void)
{
        hashtbl = hashinit(numwanted, type, flags, &mask);
}
void
sample_use(char *str, int len)
{
        uint32_t hash;
        hash = hash32_str(str, HASHINIT);
        hash = hash32_buf(&len, sizeof(len), hash);
        hashtbl[hash & mask] = len;
}
```

## 参见

`free(9)`, [hashinit(9)](hashinit.9.md), [malloc(9)](malloc.9.md)

## 限制

`hash32` 函数仅为 32 位函数。它们在 64 位性能上表现较差，尤其是高 32 位。目前这不被视为很大的限制，因为这些哈希值通常用于索引数组。如果这些哈希值用于其他目的，应重新审视此限制。

## 历史

`murmur3_32_hash32` 函数首次出现于 NetBSD 1.6。`hash32` 函数的当前实现首次提交到 OpenBSD 3.2，后来导入 FreeBSD 6.1。`jenkins_hash` 函数添加于 FreeBSD 10.0。`murmur3_32_hash` 函数添加于 FreeBSD 10.1。

## 作者

`hash32` 函数由 Tobias Weingartner 编写。`jenkins_hash` 函数由 Bob Jenkins 编写。`murmur3_32_hash` 函数由 Dag-Erling Smørgrav <des@FreeBSD.org> 编写。
