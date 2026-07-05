# linux.4

`linux` — Linux ABI 支持

## 名称

`linux`

## 概要

`要在引导时启用 Linux ABI，请在 rc.conf(5) 中加入以下行：`

```sh
linux_enable="YES"
```

## 描述

`linux` 内核模块提供有限的 Linux ABI（应用程序二进制接口）兼容性，使得无需虚拟化或仿真即可运行许多未修改的 Linux 应用程序。提供的部分设施包括：

- Linux 到本机系统调用转换
- Linux 特定系统调用
- Linux 进程的特殊信号处理
- 路径转换机制
- Linux 特定虚拟文件系统

路径转换机制使 Linux 进程在 `/` 之前先在 `emul_path`（默认为 **/compat/linux**）下查找文件路径。例如，当 Linux 进程尝试打开 `/etc/passwd` 时，它将首先访问 **/compat/linux/etc/passwd**，如果兼容路径不存在，则回退到 **/etc/passwd**。这用于确保 Linux 进程加载 Linux 共享库而非类似命名的 FreeBSD 对应库，也用于提供某些其他文件和虚拟文件系统的替代版本。

要将 Linux 共享库和系统文件安装到 **/compat/linux**，使用 `emulators/linux_base-c7` Port 或软件包，或从 `sysutils/debootstrap` 安装的 debootstrap(8)。

要避免在启动时挂载 Linux 特定文件系统，在 [rc.conf(5)](../man5/rc.conf.5.md) 文件中加入以下行：

```sh
linux_mounts_enable="NO"
```

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数提供：

**`compat.linux.debug`** 启用调试消息。设置为 0 可静默。默认为 3。设置为 1 会打印调试消息，告知未实现的内容（仅一次）。设置为 2 类似于 1，但还会打印有关已实现但未测试的内容的消息（仅一次）。设置为 3 或更高类似于 2，但不对消息进行速率限制。

**`compat.linux.default_openfiles`** Linux 应用程序的默认软打开文件资源限制。设置为 -1 可禁用限制。默认为 1024。

**`compat.linux.emul_path`** Linux 运行时环境的路径。默认为 **/compat/linux**。

**`compat.linux.osname`** Linux 内核操作系统名称。默认为 "Linux"。

**`compat.linux.osrelease`** Linux 内核操作系统发行版本。不建议在非开发系统上将其更改为其他值，因为这可能更改 Linux 程序的工作方式。已知某些版本的 GNU libc 会根据此 sysctl 的值使用不同的系统调用。

**`compat.linux.oss_version`** Linux 开放声音系统版本。默认为 198144。

**`compat.linux.preserve_vstatus`** 设置为 1 时，防止 Linux 应用程序重置 termios(4) VSTATUS 设置。从用户角度来看，这使 `SIGINFO` 对 Linux 可执行文件有效。默认为 1。

**`compat.linux.setid_allowed`** 当镜像要在 Linux ABI 下执行时，启用对新进程镜像文件设置用户 ID 和设置组 ID 模式位的处理。设置为 0 时，新的 Linux 镜像始终使用发出 execve(2) 调用的程序的凭据，而不管镜像文件模式如何。这可能是合理或甚至必需的，因为 FreeBSD 不会完全模拟 Linux 环境，遗漏的功能可能导致安全漏洞。默认为 1。

**`compat.linux32.emulate_i386`** 在 x86_64 (amd64) 环境中启用真正的 i386 Linuxulator 行为。例如，设置为 0 时，即使 uname 本身是 i386 Linux 可执行文件，Linux uname -m 也将返回 "x86_64"。设置为 1 时，Linux i386 uname -m 将返回 "i686"。默认为 0。

## 文件

**`/compat/linux`** Linux 运行时环境

**`/compat/linux/dev`** 设备文件系统，参见 [devfs(4)](devfs.4.md)

**`/compat/linux/dev/fd`** 使用 `linrdlnk` 选项挂载的文件描述符文件系统，参见 [fdescfs(4)](fdescfs.4.md)

**`/compat/linux/dev/mqueue`** 指向 mqueuefs 挂载的符号链接，参见 mqueuefs(4)

**`/compat/linux/dev/shm`** 内存文件系统，参见 tmpfs(4)

**`/compat/linux/proc`** Linux 进程文件系统，参见 [linprocfs(4)](linprocfs.4.md)

**`/compat/linux/sys`** Linux 内核对象文件系统，参见 [linsysfs(4)](linsysfs.4.md)

## 参见

brandelf(1), [dtrace_syscall(4)](dtrace_syscall.4.md), [fdescfs(4)](fdescfs.4.md), [linprocfs(4)](linprocfs.4.md), [linsysfs(4)](linsysfs.4.md), mqueuefs(4), pty(4), tmpfs(4), [elf(5)](../man5/elf.5.md)

## 历史

Linux ABI 支持最早出现于 FreeBSD 2.1 中的 i386。对 amd64 二进制文件的支持最早出现于 FreeBSD 10.3。对 arm64 二进制文件的支持最早出现于 FreeBSD 12.0。

## 缺陷

缺少对某些 Linux 特定系统调用和系统调用参数的支持。
