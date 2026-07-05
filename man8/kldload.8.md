# kldload.8

`kldload` — 将文件加载到内核中

## 名称

`kldload`

## 概要

`kldload [-nqv] file`

## 描述

`kldload` 工具使用内核链接器将 `file` `.ko` 加载到内核中。注意，如果指定了多个模块，则会尝试加载所有模块，即使某些模块加载失败。使用 `kldload` 加载给定模块时，`.ko` 扩展名不是必需的，但指定它也无妨。

如果请求的是纯文件名，则只有在该文件位于由 sysctl `kern.module_path` 定义的模块路径内时才会被加载。要从当前目录加载模块，必须指定为完整路径或相对路径。如果模块以纯文件名请求且存在于当前目录中，`kldload` 工具会发出警告。

可用选项如下：

**`-n`** 如果模块已加载，则不再尝试加载。

**`-v`** 显示更详细的信息。

**`-q`** 静默所有无关警告。

## 注释

内核安全级别设置可能通过返回 *Operation not permitted* 来阻止模块被加载或卸载。

## 文件

**/boot/kernel** 包含可加载模块的目录。模块必须具有 `.ko` 扩展名。

## 退出状态

`kldload` 工具成功时退出值为 0，发生错误时大于 0。

## 实例

按模块名称加载：

```sh
# kldload foo
```

按模块路径内的文件名加载：

```sh
# kldload foo.ko
```

按相对路径加载：

```sh
# kldload ./foo.ko
```

按完整路径加载：

```sh
# kldload /boot/kernel/foo.ko
```

## 自动加载模块

某些模块（pf、ipfw、ipf 等）可以在引导时使用相应的 [rc.conf(5)](../man5/rc.conf.5.md) 语句自动加载。模块也可以通过将其添加到 loader.conf(5) 或 [rc.conf(5)](../man5/rc.conf.5.md) 中的 kld_list 来自动加载。

只有引导系统所必需的模块（包括挂载根文件系统所需的模块）才应由 loader.conf(5) 处理。

## 参见

[kenv(1)](../man1/kenv.1.md), kldload(2), loader.conf(5), [rc.conf(5)](../man5/rc.conf.5.md), [security(7)](../man7/security.7.md), [kldconfig(8)](kldconfig.8.md), [kldstat(8)](kldstat.8.md), [kldunload(8)](kldunload.8.md), [kldxref(8)](kldxref.8.md)

## 历史

`kldload` 工具首次出现于 FreeBSD 3.0，替代了 `lkm` 接口。

## 作者

Doug Rabson <dfr@FreeBSD.org>
