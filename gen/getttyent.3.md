# getttyent.3

`getttyent` — ttys(5) 文件例程

## 名称

`getttyent`, `getttynam`, `setttyent`, `endttyent`, `isdialuptty`, `isnettty` ttys(5) 文件例程

## 库

Lb libc

## 概要

`#include <ttyent.h>`

```c
struct ttyent *
getttyent(void)

struct ttyent *
getttynam(const char *name)

int
setttyent(void)

int
endttyent(void)

int
isdialuptty(const char *name)

int
isnettty(const char *name)
```

## 描述

`getttyent` 和 `getttynam` 函数各自返回一个指向对象的指针，该对象具有以下结构，包含 tty 描述文件中某行的分解字段。

```c
struct ttyent {
	char	*ty_name;	/* 终端设备名 */
	char	*ty_getty;	/* 要执行的命令，通常为 getty */
	char	*ty_type;	/* termcap 的终端类型 */
#define	TTY_ON		0x01	/* 启用登录（启动 ty_getty 程序） */
#define	TTY_SECURE	0x02	/* 允许 uid 为 0 的用户登录 */
#define	TTY_DIALUP	0x04	/* 为拨号 tty */
#define	TTY_NETWORK	0x08	/* 为网络 tty */
#define	TTY_IFEXISTS	0x10	/* 配置为 "onifexists" */
#define	TTY_IFCONSOLE	0x20	/* 配置为 "onifconsole" */
	int	ty_status;	/* 状态标志 */
	char	*ty_window;	/* 启动窗口管理器的命令 */
	char	*ty_comment;	/* 注释字段 */
	char	*ty_group;	/* tty 组名 */
};
```

各字段如下：

**`TTY_ON`** 启用登录（即 [init(8)](../man8/init.8.md) 将在此条目上启动 `ty_getty` 所引用的命令）。

**`TTY_SECURE`** 允许 uid 为 0 的用户在此终端上登录。

**`TTY_DIALUP`** 将 tty 标识为拨入线路。如果设置了此标志，`isdialuptty` 将返回非零值。

**`TTY_NETWORK`** 将 tty 标识为用于网络连接。如果设置了此标志，`isnettty` 将返回非零值。

**`TTY_IFEXISTS`** 标识一个不一定存在的 tty。

**`TTY_IFCONSOLE`** 标识一个可能是系统控制台的 tty。

**`ty_name`** 字符特殊文件的名称。

**`ty_getty`** 由 [init(8)](../man8/init.8.md) 调用以初始化 tty 线路特性的命令名称。

**`ty_type`** 连接到此 tty 线路的默认终端类型名称。

**`ty_status`** 一个位字段掩码，指示此 tty 线路上允许的各种操作。可能的标志如下：

**`ty_window`** 为与该线路关联的窗口系统执行的命令。

**`ty_group`** tty 所属的组名。如果在 ttys 描述文件中未指定组，则该 tty 被置于名为 “none” 的匿名组中。

**`ty_comment`** 任何尾随的注释字段，移除了前导的井号（"`#`"）或空白字符。

如果任何指向字符串的字段未指定，则返回空指针。如果未指定任何标志值，`ty_status` 字段将为零。

有关各字段含义和用法的更完整讨论，请参见 ttys(5)。

`getttyent` 函数从 ttys 文件读取下一行，必要时打开该文件。`setttyent` 函数在文件已打开时将其倒回开头，或在文件未打开时打开该文件。`endttyent` 函数关闭所有打开的文件。

`getttynam` 函数从文件开头搜索，直到找到匹配的 `name`（或遇到 `EOF`）。

## 返回值

`getttyent` 和 `getttynam` 例程在遇到 `EOF` 或错误时返回空指针。`setttyent` 和 `endttyent` 函数在失败时返回 0，成功时返回 1。

如果与参数所命名的 tty 相关的 tty 条目设置了拨号或网络标志，`isdialuptty` 和 `isnettty` 例程返回非零值，否则返回零。

## 文件

**/etc/ttys**

## 参见

[login(1)](../man1/login.1.md), gettytab(5), termcap(5), ttys(5), getty(8), [init(8)](../man8/init.8.md)

## 历史

`getttyent`、`getttynam`、`setttyent` 和 `endttyent` 函数出现于 4.3BSD。

## 缺陷

这些函数使用静态数据存储；如果数据需要在后续使用，应在任何后续调用覆盖它之前进行复制。
