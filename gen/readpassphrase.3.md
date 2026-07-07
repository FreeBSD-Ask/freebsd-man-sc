# readpassphrase(3)

`readpassphrase` — 从用户获取口令

## 名称

`readpassphrase`

## 概要

`#include <readpassphrase.h>`

```c
char *
readpassphrase(const char *prompt, char *buf, size_t bufsiz,
    int flags);
```

## 描述

`readpassphrase` 函数向 **/dev/tty** 显示提示并从中读取口令。如果此文件不可访问且未设置 `RPP_REQUIRE_TTY` 标志，`readpassphrase` 在标准错误输出上显示提示并从标准输入读取。在这种情况下，通常无法关闭回显。

最多 `bufsiz` - 1 个字符（一个用于 `NUL`）被读入所提供的缓冲区 `buf`。任何额外字符和终止换行（或回车）字符都被丢弃。

`readpassphrase` 函数接受以下可选 `flags`：

**`RPP_ECHO_OFF`** 关闭回显（默认行为）
**`RPP_ECHO_ON`** 保持回显开启
**`RPP_REQUIRE_TTY`** 如果没有 tty 则失败
**`RPP_FORCELOWER`** 强制输入为小写
**`RPP_FORCEUPPER`** 强制输入为大写
**`RPP_SEVENBIT`** 去除输入的高位
**`RPP_STDIN`** 强制从 stdin 读取口令

调用进程应尽快将口令清零，以避免在进程的地址空间中留下明文口令。

## 返回值

成功完成时，`readpassphrase` 返回指向以 NUL 结尾的口令的指针。如果遇到错误，终端状态将被恢复并返回 `NULL` 指针。

## 文件

**/dev/tty**

## 实例

以下代码片段将 **/dev/tty** 中的口令读入缓冲区 `passbuf`。

```c
char passbuf[1024];
...
if (readpassphrase("Response: ", passbuf, sizeof(passbuf),
    RPP_REQUIRE_TTY) == NULL)
	errx(1, "unable to read passphrase");
if (compare(transform(passbuf), epass) != 0)
	errx(1, "bad passphrase");
...
memset(passbuf, 0, sizeof(passbuf));
```

## 错误

**[`EINTR`]** `readpassphrase` 函数被信号中断。

**[`EINVAL`]** `bufsiz` 参数为零。

**[`EIO`]** 进程是后台进程组的成员，试图从其控制终端读取，进程正在忽略或阻塞 `SIGTTIN` 信号，或者进程组是孤立的。

**[`EMFILE`]** 进程已达到其打开文件描述符的限制。

**[`ENFILE`]** 系统文件表已满。

**[`ENOTTY`]** 没有控制终端且指定了 `RPP_REQUIRE_TTY` 标志。

## 信号

`readpassphrase` 函数将捕获以下信号：

```c
SIGALRM		SIGHUP		SIGINT
SIGPIPE		SIGQUIT		SIGTERM
SIGTSTP		SIGTTIN		SIGTTOU
```

当上述信号之一被拦截时，如果终端回显先前已被关闭，则会恢复。如果在调用 `readpassphrase` 时为该信号安装了信号处理程序，则执行该处理程序。如果先前未为该信号安装处理程序，则按照 [sigaction(2)](../sys/sigaction.2.md) 采取默认操作。

`SIGTSTP`、`SIGTTIN` 和 `SIGTTOU` 信号（由于键盘或后台进程的终端 I/O 而生成的停止信号）被特殊处理。当进程在被停止后恢复时，`readpassphrase` 将重新打印提示，用户随后可以输入口令。

## 参见

[sigaction(2)](../sys/sigaction.2.md), [getpass(3)](getpass.3.md)

## 标准

`readpassphrase` 函数是一个扩展，如果需要可移植性，不应使用它。

## 历史

`readpassphrase` 函数首次出现于 FreeBSD 4.6 和 OpenBSD 2.9。