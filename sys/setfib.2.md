# setfib(2)

`setfib` — 为调用进程设置默认 FIB（路由表）

## 名称

`setfib`

## 库

Lb libc

## 概要

```c
#include <sys/socket.h>

int
setfib(int fib);
```

## 描述

`setfib()` 系统调用将调用之后打开的所有套接字的关联 FIB（路由表）设置为参数 `fib` 所指定的值。`fib` 参数必须大于或等于 0，且小于当前系统最大值，该最大值可通过 `net.fibs` sysctl 检索。系统最大值在内核配置文件中通过

> `options ROUTETABLES=`*N*

设置，或者在 **/boot/loader.conf** 或 **/etc/sysctl.conf** 中通过

```sh
net.fibs="N"
```

设置，其中 *N* 是小于 65536 的整数。注意，FIB 的数量可以在引导后增加，但不能减少。

65536 这一最大值是由于实现中将 FIB 编号存储在 [mbuf(9)](../man9/mbuf.9.md) 包头的一个 16 位字段中，但不建议使用如此大的数量，因为无论是否使用，每个 FIB 都会分配内存，且在某些地方会遍历所有 FIB。

进程的默认 FIB 将应用于所有支持多 FIB 的协议族，并被不支持的协议族所忽略。进程的默认 FIB 可以通过 `SO_SETFIB` 套接字选项针对单个套接字进行覆盖。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

如果 `fib` 参数大于当前系统最大值，`setfib()` 系统调用将失败，不执行任何操作并返回 `EINVAL`。

## 参见

[setfib(1)](../man1/setfib.1.md), [setsockopt(2)](setsockopt.2.md)

## 标准

`setfib()` 系统调用是 FreeBSD 的扩展，但类似的扩展已被添加到许多其他 UNIX 风格的内核中。

## 历史

`setfib()` 函数出现于 FreeBSD 7.1。
