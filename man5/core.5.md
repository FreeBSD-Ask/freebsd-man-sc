# core(5)

`core` — 内存映像文件格式

## 名称

`core`

## 概要

`#include <sys/param.h>`

## 描述

少数导致进程异常终止的信号也会使进程的内存状态记录写入磁盘，以便日后由可用的调试器检查。（见 sigaction(2)）此内存映像默认写入到工作目录中名为 `programname.core` 的文件中；前提是已终止的进程在该目录中有写权限，且异常未导致系统崩溃。（在此情况下，是否保存 core 文件是任意的，见 savecore(8)）

文件名通过 [sysctl(8)](../man8/sysctl.8.md) 变量 `kern.corefile` 控制。此变量的内容描述了用于存储 core 映像的文件名。此文件名可以是绝对路径，也可以是相对路径（将解析为生成该文件的程序的当前工作目录）。

可在 `kern.corefile` sysctl 中使用以下格式说明符，将额外信息插入到生成的 core 文件名中：

***%H*** 机器主机名。

***%I*** 从零开始的索引，直到达到 sysctl *debug.ncores* 的值。这对于限制特定进程生成的 core 文件数量很有用。

***%N*** 进程名。

***%P*** 进程 PID。

***%S*** 生成 core 时的信号。

***%U*** 进程 UID。

默认名称为 *%N.core*，产生传统的 FreeBSD 行为。

core 文件的最大大小受 `RLIMIT_CORE` setrlimit(2) 限制。超过此限制的文件不会被创建。

如果限制值很大，映射了非常大且可能稀疏填充的虚拟内存区域的进程可能需要很长时间来创建 core 转储。系统会忽略发送给正在写入 core 文件的进程的所有信号，但 `SIGKILL` 例外，它会终止写入并使进程立即退出。可以通过将可调 [sysctl(8)](../man8/sysctl.8.md) 变量 `kern.core_dump_can_intr` 设置为零来禁用 `SIGKILL` 的这种行为。

默认情况下，更改了用户或组凭据（无论是真实还是有效）的进程不会创建 core 文件。可以通过将 [sysctl(8)](../man8/sysctl.8.md) 变量 `kern.sugid_coredump` 设置为 1 来更改此行为以生成 core 转储。

如果内核配置文件中包含以下项目之一，core 文件可由内核压缩：

**options** GZIO

**options** ZSTDIO

以下 sysctl 控制 core 文件压缩：

***kern.compress_user_cores*** 启用用户 core 文件的压缩。值为 1 配置 [gzip(1)](../man1/gzip.1.md) 压缩，值为 2 配置 zstd(1) 压缩。根据所选格式，压缩的 core 文件名后会附加 `.gz` 或 `.zst` 后缀。

***kern.compress_user_cores_level*** 压缩级别。默认为 6。

## 注释

core 文件在写入时会将打开的文件描述符信息作为 ELF 注释包含在内。默认情况下，文件路径会被打包以仅使用所需的空间。但是，文件路径可能随时更改，包括在 core 转储期间，这可能导致文件描述符数据被截断。

可以通过禁用打包来保留所有文件描述符信息。这可能会在每个打开的 fd 上浪费最多 PATH_MAX 字节。禁用打包的方法是

```sh
sysctl kern.coredump_pack_fileinfo=0 .
```

类似地，core 文件在写入时会将 vmmap 信息作为 ELF 注释包含在内，其中包含文件路径。默认情况下，它们会被打包以仅使用所需的空间。通过与打开文件注释相同的机制，这些路径也可能随时更改，导致注释被截断。

可以通过禁用打包来保留所有 vmmap 信息。与文件信息一样，这可能会在每个映射对象上浪费最多 PATH_MAX 字节。禁用打包的方法是

```sh
sysctl kern.coredump_pack_vmmapinfo=0 .
```

## 实例

为了将所有 core 映像存储在 **/var/coredumps** 下按用户区分的私有区域中（假设相应的子目录已存在且可由用户写入），可以使用以下 [sysctl(8)](../man8/sysctl.8.md) 命令：

```sh
sysctl kern.corefile=/var/coredumps/%U/%N.core
```

## 参见

gdb(1) (`ports/devel/gdb`), [gzip(1)](../man1/gzip.1.md), kgdb(1) (`ports/devel/gdb`), setrlimit(2), sigaction(2), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`programname.core` 文件格式出现于 Version 1 AT&T UNIX。
