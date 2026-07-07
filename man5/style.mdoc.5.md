# style.mdoc(5)

`style.mdoc` — FreeBSD 手册页风格指南

## 名称

`style.mdoc`

## 描述

本文件规定了 FreeBSD 源码树中手册页的首选风格。

### NAME 章节

- 不要对提供给 **.Nd** 宏的文档描述加引号。

### 代码示例

```sh
Then run
.Ql make install clean .
```

> Then run
> `make install clean`.

```sh
Then run
.Ql Nm make Cm install Cm clean .
```

> Then run
> `Nm make Cm install Cm clean`.

- 对示例和字面 shell 命令使用字面格式，例如：渲染为：错误的方式是使用 **Nm** 等宏来修饰命令调用：渲染为：这会污染 [whatis(1)](../man1/apropos.1.md) 数据库，导致 `whatis clean` 错误地显示编写该命令的手册页。

### 版权头

参见 [style(9)](../man9/style.9.md)。

### HARDWARE 章节

第 4 节的驱动程序手册应包含一个 Sx HARDWARE 章节，描述已知可与该驱动程序一起工作的硬件。此章节会被逐字引入到发布硬件说明中，因此需要注意以下几点：

```sh
The
.Nm
driver supports the following $device_class:
```

- 引言应采用以下形式：后跟支持的硬件列表。这定义了子章节所指的驱动程序，并允许读者在硬件说明中不仅搜索他们拥有的设备型号，还可以搜索他们想要购买的设备类型。
- 支持的硬件应作为项目符号列表列出，如果复杂性需要，则使用列列表。这两种列表类型创建了非常整洁的子章节，具有清晰的开始和结束点。

### EXAMPLES 章节

```sh
.Bl -tag -width 0n
.It Sy Example 1 Doing Something
.Pp
The following command does something.
.Bd -literal -offset 2n
.Ic # make -VLEGAL
.Ed
.It Sy Example 2 Doing Something Different
.Pp
The following command does something different.
.Bd -literal -offset 2n
.Ic # bectl list
.Ed
.Pp
It is good to know this command.
.El
```

```sh
`# make -VLEGAL`
```

```sh
`# bectl list`
```

****Example** 1: Doing Something** The following command does something.

****Example** 2: Doing Something Different** The following command does something different. It is good to know this command.

- 按以下方式格式化 Sx EXAMPLES 章节：渲染为：

### 列表

```sh
.Bl -tag -width "-a address"
.It Fl a Ar address
Set the address.
.It Fl v
Print the version.
.El
```

```sh
.Bl -tag -width "indent"
.It Cm build
Build the port.
.It Cm install
Install the port.
.It Fl install-missing-packages
Install the missing packages.
.El
```

- **.Bl** 宏的 `-width` 参数应与列表中最长渲染项的长度匹配，例如：如果最长项太长而影响可读性，建议将 `-width` 参数设置为 `indent`，例如：

### 引用

- 使用 **Dq**（“”）宏进行引用。在引号内引用时使用 **Sq**（‘’）宏。通常不需要使用 **Qq**（“”）宏。

### 变量

```sh
.Va critical_filesystems_ Ns Aq Ar type
```

> `critical_filesystems_`<`type`>

```sh
.Va critical_filesystems_ Ns Ar type
```

> `critical_filesystems_``type`

- 对 [sysctl(8)](../man8/sysctl.8.md) 变量（如 `kdb.enter.panic`）使用 **Va** 而不是 **Dv**。
- 当参数（**Ar**）与类似 **Pa** 或 **Va** 等类似格式的宏混合使用时，使用尖括号 **Aq**（“<>>”）宏，例如：渲染为：而不是：将渲染为：

## 文件

**/usr/share/examples/mdoc/** 编写手册页的示例。

## 参见

[man(1)](../man1/man.1.md), [mandoc(1)](../man1/mandoc.1.md), mdoc(7), roff(7), [style(9)](../man9/style.9.md)

## 历史

本手册页首次出现于 FreeBSD 13.0。

## 作者

Mateusz Piotrowski <0mp@FreeBSD.org>
