# CMSG_DATA.3

`CMSG_DATA` — 用于访问辅助数据的套接字控制消息例程

## 名称

`CMSG_DATA`, `CMSG_FIRSTHDR`, `CMSG_LEN`, `CMSG_NXTHDR`, `CMSG_SPACE`

## 概要

`#include <sys/socket.h>`

```c
unsigned char *CMSG_DATA(struct cmsghdr *);
struct cmsghdr *CMSG_FIRSTHDR(struct msghdr *);
size_t CMSG_LEN(size_t);
struct cmsghdr *CMSG_NXTHDR(struct msghdr *, struct cmsghdr *);
size_t CMSG_SPACE(size_t);
```

## 描述

控制消息 API 用于构造辅助数据对象，以便在套接字之间发送和接收控制消息时使用。

控制消息通过 recvmsg(2) 和 sendmsg(2) 系统调用传递。recvmsg(2) 中描述的 `cmsghdr` 结构用于指定控制消息链。

应当使用这些例程而非直接访问控制消息头部成员和数据缓冲区，因为它们能够确保满足必要的对齐约束。

提供以下例程：

**`CMSG_DATA(cmsg)`** 该例程访问控制消息头 `cmsg` 的数据部分。它确保辅助数据起始位置的对齐约束得到满足。

**`CMSG_FIRSTHDR(msghdr)`** 该例程访问附加到消息 `msghdr` 的第一个控制消息。如果消息未附加任何控制消息，该例程返回 `NULL`。

**`CMSG_LEN(len)`** 该例程确定包含控制消息头在内的控制消息大小（以字节为单位）。`len` 指定控制消息所持有数据的长度。该值通常存储在每个控制消息的 `cmsg_len` 中。该例程考虑了辅助数据起始位置的任何对齐约束。

**`CMSG_NXTHDR(msghdr, cmsg)`** 该例程返回消息 `msghdr` 中紧随 `cmsg` 之后的控制消息的位置。如果 `cmsg` 是链中的最后一个控制消息，该例程返回 `NULL`。

**`CMSG_SPACE(len)`** 该例程确定保存控制消息及其长度为 `len` 的内容（包括控制消息头）所需的大小（以字节为单位）。该值通常存储在 `msg_msgcontrollen` 中。该例程考虑了辅助数据起始位置的任何对齐约束，以及填充下一个控制消息所需的任何对齐。

## 实例

以下示例在父进程中构造一个包含文件描述符的控制消息，并通过预共享套接字传递给子进程。然后子进程使用接收到的文件描述符向父进程发送 "hello" 字符串。

```c
#include <sys/socket.h>
#include <err.h>
#include <stdio.h>
#include <string.h>
#include <sysexits.h>
#include <unistd.h>
#define	HELLOLEN    sizeof("hello")
int
main()
{
	struct msghdr msg;
	union {
		struct cmsghdr hdr;
		unsigned char	 buf[CMSG_SPACE(sizeof(int))];
	} cmsgbuf;
	char buf[HELLOLEN];
	int hellofd[2];
	int presharedfd[2];
	struct cmsghdr *cmsg;
	if (socketpair(PF_LOCAL, SOCK_STREAM, 0, presharedfd) == -1)
		err(EX_OSERR, "failed to create a pre-shared socket pair");
	memset(&msg, 0, sizeof(msg));
	msg.msg_control = &cmsgbuf.buf;
	msg.msg_controllen = sizeof(cmsgbuf.buf);
	msg.msg_iov = NULL;
	msg.msg_iovlen = 0;
	switch (fork()) {
	case -1:
		err(EX_OSERR, "fork");
	case 0:
		close(presharedfd[0]);
		strlcpy(buf, "hello", HELLOLEN);
		if (recvmsg(presharedfd[1], &msg, 0) == -1)
			err(EX_IOERR, "failed to receive a message");
		if (msg.msg_flags & (MSG_CTRUNC | MSG_TRUNC))
			errx(EX_IOERR, "control message truncated");
		for (cmsg = CMSG_FIRSTHDR(&msg); cmsg != NULL;
		    cmsg = CMSG_NXTHDR(&msg, cmsg)) {
			if (cmsg->cmsg_len == CMSG_LEN(sizeof(int)) &&
			    cmsg->cmsg_level == SOL_SOCKET &&
			    cmsg->cmsg_type == SCM_RIGHTS) {
				hellofd[1] = *(int *)CMSG_DATA(cmsg);
				printf("child: sending '%s'\n", buf);
				if (write(hellofd[1], buf, HELLOLEN) == -1)
				    err(EX_IOERR, "failed to send 'hello'");
			}
		}
		break;
	default:
		close(presharedfd[1]);
		if (socketpair(PF_LOCAL, SOCK_STREAM, 0, hellofd) == -1)
			err(EX_OSERR, "failed to create a 'hello' socket pair");
		cmsg = CMSG_FIRSTHDR(&msg);
		cmsg->cmsg_len = CMSG_LEN(sizeof(int));
		cmsg->cmsg_level = SOL_SOCKET;
		cmsg->cmsg_type = SCM_RIGHTS;
		*(int *)CMSG_DATA(cmsg) = hellofd[1];
		if (sendmsg(presharedfd[0], &msg, 0) == -1)
			err(EX_IOERR, "sendmsg");
		close(hellofd[1]);
		if (read(hellofd[0], buf, HELLOLEN) == -1)
			err(EX_IOERR, "failed to receive 'hello'");
		printf("parent: received '%s'\n", buf);
		break;
	}
	return (0);
}
```

## 参见

recvmsg(2), sendmsg(2), socket(2), [ip(4)](../man4/ip.4.md), [ip6(4)](../man4/ip6.4.md), [unix(4)](../man4/unix.4.md)

## 标准

> W. Stevens, M. Thomas, "Advanced Sockets API for IPv6", February 1998.

> W. Stevens, M. Thomas, E. Nordmark, T. Jinmei, "Advanced Sockets Application Program Interface (API) for IPv6", May 2003.

## 历史

控制消息 API 最早出现于 4.2BSD。本手册页最初由 Jared Yanovich <jaredy@OpenBSD.org> 为 OpenBSD 3.8 编写，后由 Mateusz Piotrowski <0mp@FreeBSD.org> 引入 FreeBSD 12.0。
