# sockatmark.3

`sockatmark` — 确定读指针是否位于 OOB 标记处

## 名称

`sockatmark`

## 库

libc

## 概要

`#include <sys/socket.h>`

```c
int
sockatmark(int s);
```

## 描述

为确定读指针当前是否指向数据流中的标记处，提供了 `sockatmark` 函数。如果 `sockatmark` 返回 1，下一次读取将返回标记之后的数据。否则（假设带外数据已到达），下一次读取将提供客户端在传输带外信号之前发送的数据。远程登录进程中用于在收到中断或退出信号时刷新输出的例程如下所示。它读取标记之前的正常数据（以丢弃它们），然后读取带外字节。

```c
#include <sys/socket.h>
...
oob()
{
	int out = FWRITE, mark;
	char waste[BUFSIZ];
	/* 刷新本地终端输出 */
	ioctl(1, TIOCFLUSH, (char *)&out);
	for (;;) {
		if ((mark = sockatmark(rem)) < 0) {
			perror("sockatmark");
			break;
		}
		if (mark)
			break;
		(void) read(rem, waste, sizeof (waste));
	}
	if (recv(rem, &mark, 1, MSG_OOB) < 0) {
		perror("recv");
		...
	}
	...
}
```

## 返回值

成功完成时，如果读指针指向 OOB 标记，`sockatmark` 函数返回值 1，未指向时返回 0。若发生错误，返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`sockatmark` 调用在以下情况失败：

**`[EBADF]`** `s` 参数不是有效的描述符。

**`[ENOTTY]`** `s` 参数是文件的描述符，而非套接字。

## 参见

[recv(2)](../sys/recv.2.md), [send(2)](../sys/send.2.md)

> Stuart Sechrest, "An Introductory 4.4BSD Interprocess Communication Tutorial".

> Samuel J. Leffler, Robert S. Fabry, William N. Joy, Phil Lapsley, Steve Miller, Chris Torek, "An Advanced 4.4BSD Interprocess Communication Tutorial".

## 历史

`sockatmark` 函数由 IEEE Std 1003.1-2001（"POSIX.1"）引入，用于标准化历史上的 `SIOCATMARK` [ioctl(2)](../sys/ioctl.2.md)。使用 `ENOTTY` 错误而非通常的 `ENOTSOCK` 是为了匹配 `SIOCATMARK` 的历史行为。
