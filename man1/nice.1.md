# nice.1

`nice` — 以调整后的调度优先级执行实用程序

## 名称

`nice`

## 概要

`nice [-n increment] utility [argument ...]`

## 描述

`nice` 实用程序以调整后的调度优先级运行 `utility`，将其“nice”值增加指定的 `increment`，或默认值 10。进程的 nice 值越低，其调度优先级越高。

超级用户可以指定负的增量，以更高的调度优先级运行实用程序。

某些 shell 可能提供与本实用程序相似或相同的内建 `nice` 命令。请参阅 [builtin(1)](builtin.1.md) 手册页。

## 环境变量

如果名称中不含 `/` 字符，`PATH` 环境变量用于定位所请求的 `utility`。

## 退出状态

如果调用了 `utility`，`nice` 的退出状态就是 `utility` 的退出状态。

退出状态 126 表示找到了 `utility`，但无法执行。退出状态 127 表示找不到 `utility`。

## 实例

假设 shell 的优先级为 0，以优先级 5 执行实用程序 ‘date’：

```sh
nice -n 5 date
```

假设 shell 的优先级为 0 且你是超级用户，以优先级 -19 执行实用程序 ‘date’：

```sh
nice -n 16 nice -n -35 date
```

## 兼容性

传统的 `-increment` 选项已弃用，但仍受支持。

## 参见

[builtin(1)](builtin.1.md), csh(1), idprio(1), rtprio(1), getpriority(2), setpriority(2), [renice(8)](../man8/renice.8.md)

## 标准

`nice` 实用程序遵循 IEEE Std 1003.1-2001 ("POSIX.1") 规范。

## 历史

`nice` 实用程序出现于 Version 4 AT&T UNIX。
