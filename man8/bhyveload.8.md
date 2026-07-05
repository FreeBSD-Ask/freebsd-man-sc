# bhyveload.8

`bhyveload` — 在 bhyve 虚拟机中加载 FreeBSD 客户机

## 名称

`bhyveload`

## 概要

`bhyveload [-C] [-S] [-c cons-dev] [-d disk-path] [-e name=value] [-h host-path] [-l os-loader] [-m memsize[K|k|M|m|G|g|T|t]] vmname`

## 描述

`bhyveload` 用于在 [bhyve(4)](../man4/bhyve.4.md) 虚拟机中加载 FreeBSD 客户机。

`bhyveload` 基于 [loader(8)](loader.8.md)，会在用户终端上呈现与 FreeBSD loader 完全一致的界面。可以通过指定不同的 OS loader 来改变此行为。

虚拟机由 `vmname` 标识；如果该虚拟机不存在，则会创建它。

## 选项

可用选项如下：

**`-c`** `cons-dev` `cons-dev` 是一个 [tty(4)](../man4/tty.4.md) 设备，用于 `bhyveload` 的终端 I/O。字符串 "stdio" 也被接受，表示使用无缓冲的标准 I/O。这是默认值。

**`-d`** `disk-path` `disk-path` 是客户机启动磁盘镜像的路径名。

**`-e`** `name=value` 将 FreeBSD loader 环境变量 `name` 设置为 `value`。此选项可多次使用以设置多个环境变量。

**`-h`** `host-path` `host-path` 是客户机启动文件系统根目录在主机上的目录。

**`-l`** `os-loader` 指定不同的 OS loader。默认情况下 `bhyveload` 使用 **/boot/userboot.so**，它提供标准的 FreeBSD loader。

**`-m`** `memsize`[`K|k|M|m|G|g|T|t`] `memsize` 是分配给客户机的内存大小。`memsize` 参数可以后跟 `K`、`M`、`G` 或 `T` 之一（大小写均可），分别表示千字节、兆字节、吉字节或太字节的倍数。`memsize` 默认为 256M。

**`-C`** 当 `bhyveload` 生成核心转储时，将客户机内存包含在核心文件中。此选项用于调试 OS loader，便于检查客户机内存。

**`-S`** 锁定客户机内存。

## 实例

创建名为 `freebsd-vm` 的虚拟机，从 ISO 镜像 **/freebsd/release.iso** 启动，并分配 1GB 内存：

```sh
bhyveload -m 1G -d /freebsd/release.iso freebsd-vm
```

创建名为 `test-vm` 的虚拟机，分配 256MB 内存，客户机根文件系统位于主机目录 **/user/images/test** 下，终端 I/O 发送至 [nmdm(4)](../man4/nmdm.4.md) 设备 **/dev/nmdm1B**：

```sh
bhyveload -m 256MB -h /usr/images/test -c /dev/nmdm1B test-vm
```

## 参见

[bhyve(4)](../man4/bhyve.4.md), [nmdm(4)](../man4/nmdm.4.md), [vmm(4)](../man4/vmm.4.md), [bhyve(8)](bhyve.8.md), [loader(8)](loader.8.md)

## 历史

`bhyveload` 首次出现在 FreeBSD 10.0 中，由 NetApp Inc. 开发。

## 作者

`bhyveload` 由 NetApp Inc. 的 Neel Natu <neel@FreeBSD.org> 在 Doug Rabson <dfr@FreeBSD.org> 的大力帮助下开发。

## 缺陷

`bhyveload` 只能加载 FreeBSD 作为客户机。

## 安全注意事项

请注意，在某些配置下，`bhyveload` 会在主机环境中执行客户机 loader 脚本。但 `bhyveload` 在加载 `os-loader` 或执行任何 loader 脚本之前，会进入 [capsicum(4)](../man4/capsicum.4.md) 沙箱。在主机文件系统上，沙箱仅能访问由 `-h` 标志指定的路径、未指定 `-l` 时 **/boot** 目录的内容，以及所选的控制台设备。

请注意，客户机 loader 脚本本身已受到一些限制，这些限制不会仅因为运行在用户态而放宽。例如，loader 脚本中对 loader “host” 设备的任何 I/O 操作都受限于 `bhyveload` 提供的接口，而 `bhyveload` 本身会将可访问的路径限制在指定的 `-h` 目录内（如果指定了的话）。在沙箱中访问 **/boot** 内的文件需要 userboot 中的任意代码执行，而 userboot 通常由主机提供，并非客户机镜像的一部分。沙箱中对 `-h` 目录以及 **/boot** 的所有访问均严格只读。
