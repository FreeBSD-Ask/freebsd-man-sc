# fdescfs(4)

`fdescfs` — 文件描述符文件系统

## 名称

`fdescfs`

## 概要

```sh
fdescfs	/dev/fd	fdescfs rw 0 0
```

## 描述

文件描述符文件系统（`fdescfs`）提供对全局文件系统命名空间中每进程文件描述符命名空间的访问。常规挂载点为 **/dev/fd**。

该文件系统的内容显示为一系列编号文件，这些文件对应于读取目录的进程当前打开的文件。**/dev/fd/0** 到 **/dev/fd/#** 这些文件指向可以通过文件系统访问的文件描述符。

挂载 `fdescfs` 文件系统时可以使用以下挂载选项：

**`nodup`** 对于引用 vnode 的文件描述符，不使用上文所述的 dup(2) 语义，而是重新打开所引用的 vnode。详见下文。

**`linrdlnk`** 将 `fdescfs` vnode 的类型报告为 `VLNK`，而非 FreeBSD 传统的 `VCHR`。为兼容 [linux(4)](linux.4.md) ABI，应使用 `linrdlnk` 选项挂载 `fdescfs` 卷。

**`rdlnk`** 始终将 `fdescfs` vnode 视为符号链接，特别是会跟随解析后的名称进行名称查找。此选项严格强于 `linrdlnk` 选项，它不仅改变 stat(2) 返回的类型，还会使 `fdescfs` 文件表现为符号链接。

对于未使用 `nodup` 挂载选项挂载的 `fdescfs`，如果文件描述符已打开，并且打开文件时使用的模式是已有描述符模式的子集，那么调用：

```sh
fd = open("/dev/fd/0", mode);
```

与调用：

```sh
fd = fcntl(0, F_DUPFD, 0);
```

是等价的。open(2) 调用中除 `O_RDONLY`、`O_WRONLY` 和 `O_RDWR` 之外的标志将被忽略。

对于使用 `nodup` 选项挂载的 `fdescfs`，且文件描述符引用的是一个 vnode，调用：

```sh
fd = open("/dev/fd/0", mode);
```

将以指定的 `mode` 重新打开所引用的 vnode。换言之，上述 open 调用等价于：

```sh
fd = openat(0, "", O_EMPTY_PATH, mode);
```

特别地，如果文件描述符是用 `O_PATH` 标志打开的，那么 `O_EMPTY_PATH` 或在带 `nodup` 选项的 `fdescfs` 挂载上使用 open 调用，可以在当前权限允许所请求 `mode` 的前提下，将其转换为常规打开的文件。

*注意：* 仅挂载 devfs 时默认会创建 **/dev/fd/0**、**/dev/fd/1** 和 **/dev/fd/2** 文件。`fdescfs` 会为进程打开的所有文件描述符创建条目。

## 文件

**/dev/fd/#**

## 实例

挂载位于 **/dev/fd** 的 `fdescfs` 卷：

```sh
mount -t fdescfs none /dev/fd
```

为兼容 [linux(4)](linux.4.md) ABI：

```sh
mount -t fdescfs -o linrdlnk none /compat/linux/dev/fd
```

为替代 `O_EMPTY_PATH` 标志，使用：

```sh
mount -t fdescfs -o nodup none /dev/fdpath
```

## 参见

[devfs(4)](devfs.4.md), [mount(8)](../man8/mount.8.md)

## 历史

`fdescfs` 文件系统首次出现于 4.4BSD。`fdescfs` 手册页首次出现于 FreeBSD 2.2。

## 作者

`fdescfs` 手册页由 Mike Pritchard <mpp@FreeBSD.org> 编写，基于 Jan-Simon Pendry 编写的手册页。
