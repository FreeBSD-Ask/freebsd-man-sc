# aout(4)

`aout` — 内核对执行传统 a.out 格式二进制文件的支持

## 名称

`aout`

## 概要

```sh
kldload a.out
```

## 描述

[a.out(5)](../man5/a.out.5.md) 可执行格式在 FreeBSD 3.0 发布之前使用。由于当时 i386 是唯一受支持的架构，[a.out(5)](../man5/a.out.5.md) 可执行文件只能在支持执行 i386 代码的平台上激活，例如 i386 和 amd64。

要为旧系统调用和旧系统调用调用方法添加内核支持，请将以下选项放入内核配置文件中：

> `options COMPAT_43`
> br
> `options COMPAT_FREEBSD32`

`COMPAT_FREEBSD32` 选项仅在 64 位 CPU 架构上需要。

需要使用 [kldload(8)](../man8/kldload.8.md) 工具加载 `aout.ko` 模块，以支持 [a.out(5)](../man5/a.out.5.md) 映像激活器：

> `kldload aout`

或者，要在引导时加载该模块，请在 loader.conf(5) 中加入以下行：

```sh
aout_load="YES"
```

[a.out(5)](../man5/a.out.5.md) 格式在很久以前是主流格式。现代操作系统的合理默认设置和安全要求与当时的默认环境相矛盾，需要调整系统以模拟旧二进制文件的自然环境。

以下 [sysctl(8)](../man8/sysctl.8.md) 可调参数对此有用：

**Xo** `security.bsd.map_at_zero` Xc 设为 1 以允许在地址 0 处映射进程页面。某些非常古老的 `ZMAGIC` 可执行映像需要在地址 0 处进行文本映射。

**Xo** `kern.pid_max` Xc 旧版 FreeBSD 使用有符号 16 位类型作为 `pid_t`。当前内核使用 32 位类型作为 `pid_t`，并允许进程 ID 最大到 99999。这些值无法用旧的 `pid_t` 表示，主要对使用 wait(2) 系统调用的进程（例如 shell）造成问题。将 sysctl 设为 30000 可解决此问题。

**Xo** `kern.elf32.read_exec` Xc 设为 1 以强制 32 位进程执行的任何可访问内存映射都允许执行，参见 mmap(2)。旧版 i386 CPU 的 PTE 中没有禁止从页面执行的位，因此许多旧程序即使对于可执行代码的映射也未指定 `PROT_EXEC`。如果映射已允许任何访问，此 sysctl 会强制 `PROT_EXEC`。仅当主机架构允许不可执行映射时才需要此设置。

## 参见

execve(2), [a.out(5)](../man5/a.out.5.md), [elf(5)](../man5/elf.5.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

[a.out(5)](../man5/a.out.5.md) 可执行格式用于古老的 AT&T UNIX，并从最初开始直到 FreeBSD 2.2.9 一直是 FreeBSD 的主要可执行格式。在 FreeBSD 3.0 中它被 [elf(5)](../man5/elf.5.md) 取代。

## 作者

`aout` 手册页由 Konstantin Belousov <kib@FreeBSD.org> 编写。

## 缺陷

在 64 位架构上，并非所有旧系统调用的包装器都已实现。
