# kld.4

`kld` — 动态内核链接器设施

## 名称

`kld`

## 描述

LKM（可加载内核模块）设施在 FreeBSD 3.0 及更高版本中已被弃用，由 `kld` 接口取代。此接口与其前身一样，允许系统管理员在运行中的系统上动态添加和删除功能。此功能还帮助软件开发人员开发内核的新部分，而无需不断重启以测试其更改。

可将各种类型的模块加载到系统中。有若干已定义的模块类型（如下所列），可以预定义的方式添加到系统中。此外，还有一种通用类型，由模块本身处理加载和卸载。

FreeBSD 系统广泛使用可加载内核模块，并提供大多数文件系统、NFS 客户端和服务器、所有屏幕保护程序以及 Linux 模拟器的可加载版本。`kld` 模块默认放置在 **/boot/kernel** 目录中，与其匹配的内核一起。

`kld` 接口通过 [kldload(8)](../man8/kldload.8.md)、[kldunload(8)](../man8/kldunload.8.md) 和 [kldstat(8)](../man8/kldstat.8.md) 程序使用。

[kldload(8)](../man8/kldload.8.md) 程序可加载 [a.out(5)](../man5/a.out.5.md) 或 ELF 格式的可加载模块。[kldunload(8)](../man8/kldunload.8.md) 程序卸载任何已加载的模块（如果没有其他模块依赖于该模块）。[kldstat(8)](../man8/kldstat.8.md) 程序用于检查当前加载到系统中的模块的状态。

仅当系统安全级别 `kern.securelevel` 低于 1 时，才能加载或卸载内核模块。

## 模块类型

***Device** 驱动模块* 可使用 `kld` 将新的块和字符设备驱动加载到系统中。加载模块时，[devfs(4)](devfs.4.md) 会自动为已加载的驱动创建设备节点，卸载时销毁。可通过配置 devd(8) 指定在加载模块导致新设备可用或卸载模块导致现有设备消失时要运行的用户态程序。

## 文件

**`/boot/kernel`** 包含为也位于此目录中的内核构建的模块二进制文件的目录。

**`/usr/include/sys/module.h`** 包含编译 `kld` 模块所需定义的文件。

**`/usr/share/examples/kld`** 实现示例 kld 模块的示例源代码。

## 参见

kldfind(2), kldfirstmod(2), kldload(2), kldnext(2), kldstat(2), kldunload(2), [devfs(4)](devfs.4.md), devd(8), [kldload(8)](../man8/kldload.8.md), [kldstat(8)](../man8/kldstat.8.md), [kldunload(8)](../man8/kldunload.8.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`kld` 设施出现于 FreeBSD 3.0，旨在替代 `lkm` 设施，后者在功能上类似于 SunOS 4.1.3 提供的可加载内核模块设施。

## 作者

`lkm` 设施最初由 Doug Rabson <dfr@FreeBSD.org> 实现。

## 缺陷

如果模块 B 依赖于另一个模块 A，但未编译时将模块 A 声明为依赖项，则即使模块 A 已存在于系统中，[kldload(8)](../man8/kldload.8.md) 也无法加载模块 B。

如果多个模块依赖于模块 A，并且编译时将模块 A 声明为依赖项，则加载其中任何一个模块时，[kldload(8)](../man8/kldload.8.md) 都会加载模块 A 的一个实例。

如果模块使用自定义入口点，并且模块编译为“ELF”二进制文件，则 [kldload(8)](../man8/kldload.8.md) 无法执行该入口点。

[kldload(8)](../man8/kldload.8.md) 指示用户阅读 [dmesg(8)](../man8/dmesg.8.md) 以了解加载模块时遇到的任何错误。

当系统内部接口更改时，旧模块通常无法检测到这一点，此类模块加载时通常会导致崩溃或神秘故障。
