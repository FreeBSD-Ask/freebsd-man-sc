# fd.4

`fd` — 文件描述符文件

## 名称

`fd`, `stdin`, `stdout`, `stderr`

## 描述

**/dev/fd/0** 到 **/dev/fd/#** 这些文件指向可以通过文件系统访问的文件描述符。如果文件描述符已打开，并且打开文件时使用的模式是已有描述符模式的子集，那么调用：

```sh
fd = open("/dev/fd/0", mode);
```

与调用：

```sh
fd = fcntl(0, F_DUPFD, 0);
```

是等价的。

打开文件 **/dev/stdin**、**/dev/stdout** 和 **/dev/stderr** 等价于以下调用：

```sh
fd = fcntl(STDIN_FILENO,  F_DUPFD, 0);
fd = fcntl(STDOUT_FILENO, F_DUPFD, 0);
fd = fcntl(STDERR_FILENO, F_DUPFD, 0);
```

open(2) 调用中除 `O_RDONLY`、`O_WRONLY` 和 `O_RDWR` 之外的标志将被忽略。

## 实现说明

默认情况下，**/dev/fd** 由 [devfs(4)](devfs.4.md) 提供，它为前三个文件描述符提供节点。某些站点可能需要为额外的文件描述符提供节点；可以通过将 [fdescfs(4)](fdescfs.4.md) 挂载到 **/dev/fd** 来使这些节点可用。

## 文件

**/dev/fd/#**
**/dev/stdin**
**/dev/stdout**
**/dev/stderr**

## 参见

[devfs(4)](devfs.4.md), [fdescfs(4)](fdescfs.4.md), [tty(4)](tty.4.md)
