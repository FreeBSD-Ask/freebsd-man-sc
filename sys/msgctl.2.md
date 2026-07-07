# msgctl(2)

`msgctl` — 消息队列控制操作

## 名称

`msgctl`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/ipc.h>`

`#include <sys/msg.h>`

```c
int
msgctl(int msqid, int cmd, struct msqid_ds *buf);
```

## 描述

`msgctl()` 系统调用对由 `msqid` 指定的消息队列执行一些控制操作。

每个消息队列都有一个与之关联的数据结构，其中部分内容可由 `msgctl()` 修改，部分内容决定 `msgctl()` 的行为。该数据结构定义在 `sys/msg.h` 中，包含（除其他成员外）以下成员：

```c
struct msqid_ds {
        struct  ipc_perm msg_perm;      /* 消息队列权限位 */
        msglen_t msg_cbytes;    /* 队列中正在使用的字节数 */
        msgqnum_t msg_qnum;     /* 队列中的消息数 */
        msglen_t msg_qbytes;    /* 队列上的最大字节数 */
        pid_t   msg_lspid;      /* 最后一次 msgsnd() 的 pid */
        pid_t   msg_lrpid;      /* 最后一次 msgrcv() 的 pid */
        time_t  msg_stime;      /* 最后一次 msgsnd() 的时间 */
        time_t  msg_rtime;      /* 最后一次 msgrcv() 的时间 */
        time_t  msg_ctime;      /* 最后一次 msgctl() 的时间 */
};
```

在 `msqid_ds` 结构中使用的 `ipc_perm` 结构定义在 `sys/ipc.h` 中，形式如下：

```c
struct ipc_perm {
        uid_t           cuid;   /* 创建者用户 ID */
        gid_t           cgid;   /* 创建者组 ID */
        uid_t           uid;    /* 用户 ID */
        gid_t           gid;    /* 组 ID */
        mode_t          mode;   /* 读/写权限 */
        unsigned short  seq;    /* 序列号（用于生成唯一 ipcid） */
        key_t           key;    /* 用户指定的 msg/sem/shm 键 */
};
```

由 `msgctl()` 执行的操作在 `cmd` 中指定，取下列值之一：

**`IPC_STAT`** 收集关于消息队列的信息，并将其放入 `buf` 所指向的结构中。

**`IPC_SET`** 设置与 `msqid` 关联的结构中的 `msg_perm.uid`、`msg_perm.gid`、`msg_perm.mode` 和 `msg_qbytes` 字段的值。这些值取自 `buf` 所指向结构中的对应字段。此操作只能由超级用户执行，或由有效用户 ID 等于与消息队列关联的数据结构中 `msg_perm.cuid` 或 `msg_perm.uid` 的进程执行。`msg_qbytes` 的值只能由超级用户增加。超过系统限制（来自 `sys/msg.h` 的 MSGMNB）的 `msg_qbytes` 值会被静默截断至该限制。

**`IPC_RMID`** 移除由 `msqid` 指定的消息队列，并销毁与之关联的数据。只有超级用户或有效 uid 等于与队列关联的数据结构中 `msg_perm.cuid` 或 `msg_perm.uid` 值的进程才能执行此操作。

对消息队列进行读或写（参见 [msgsnd(2)](msgsnd.2.md) 和 [msgrcv(2)](msgrcv.2.md)）的权限由 `msg_perm.mode` 字段确定，方式与文件相同（参见 [chmod(2)](chmod.2.md)），但有效 uid 可以匹配 `msg_perm.cuid` 字段或 `msg_perm.uid` 字段，有效 gid 可以匹配 `msg_perm.cgid` 或 `msg_perm.gid`。

## 返回值

若成功，`msgctl()` 函数返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`msgctl()` 函数在以下情况下会失败：

**[`EPERM`]** `cmd` 参数等于 IPC_SET 或 IPC_RMID，且调用者不是超级用户，有效 uid 也不匹配与消息队列关联的数据结构中的 `msg_perm.uid` 或 `msg_perm.cuid` 字段。试图通过 IPC_SET 增加 `msg_qbytes` 的值，但调用者不是超级用户。

**[`EACCES`]** 命令为 IPC_STAT，且调用者对此消息队列没有读权限。

**[`EINVAL`]** `msqid` 参数不是有效的消息队列标识符。`cmd` 不是有效的命令。

**[`EFAULT`]** `buf` 参数指定了无效的地址。

## 参见

[msgget(2)](msgget.2.md), [msgrcv(2)](msgrcv.2.md), [msgsnd(2)](msgsnd.2.md)

## 历史

消息队列出现于 AT&T System V UNIX 的第一个版本。
