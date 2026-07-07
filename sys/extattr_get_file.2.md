# extattr_get_file(2)

`extattr_delete_fd` — 操作 VFS 扩展属性的系统调用

## 名称

`extattr_delete_fd`, `extattr_delete_file`, `extattr_delete_link`, `extattr_get_fd`, `extattr_get_file`, `extattr_get_link`, `extattr_list_fd`, `extattr_list_file`, `extattr_list_link`, `extattr_set_fd`, `extattr_set_file`, `extattr_set_link`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/extattr.h>`

```c
int
extattr_delete_fd(int fd, int attrnamespace, const char *attrname);
```

```c
int
extattr_delete_file(const char *path, int attrnamespace,
    const char *attrname);
```

```c
int
extattr_delete_link(const char *path, int attrnamespace,
    const char *attrname);
```

```c
ssize_t
extattr_get_fd(int fd, int attrnamespace, const char *attrname,
    void *data, size_t nbytes);
```

```c
ssize_t
extattr_get_file(const char *path, int attrnamespace,
    const char *attrname, void *data, size_t nbytes);
```

```c
ssize_t
extattr_get_link(const char *path, int attrnamespace,
    const char *attrname, void *data, size_t nbytes);
```

```c
ssize_t
extattr_list_fd(int fd, int attrnamespace, void *data, size_t nbytes);
```

```c
ssize_t
extattr_list_file(const char *path, int attrnamespace, void *data,
    size_t nbytes);
```

```c
ssize_t
extattr_list_link(const char *path, int attrnamespace, void *data,
    size_t nbytes);
```

```c
ssize_t
extattr_set_fd(int fd, int attrnamespace, const char *attrname,
    const void *data, size_t nbytes);
```

```c
ssize_t
extattr_set_file(const char *path, int attrnamespace,
    const char *attrname, const void *data, size_t nbytes);
```

```c
ssize_t
extattr_set_link(const char *path, int attrnamespace,
    const char *attrname, const void *data, size_t nbytes);
```

## 描述

命名扩展属性是与表示文件和目录的 vnode 关联的元数据。它们以一组命名空间内的 "name=value" 对形式存在。

`extattr_get_file` 系统调用将指定扩展属性的值检索到由 `data` 所指向、大小为 `nbytes` 的缓冲区中。`extattr_set_file` 系统调用将指定扩展属性的值设置为 `data` 所描述的数据。`extattr_delete_file` 系统调用删除指定的扩展属性。`extattr_list_file` 返回请求命名空间中存在的属性列表。每个列表条目由一个包含属性名称长度的单字节组成，其后跟随属性名称。属性名称不以 ASCII 0 (nul) 终止。`extattr_get_file` 和 `extattr_list_file` 调用以 [read(2)](read.2.md) 的方式使用 `data` 和 `nbytes` 参数；`extattr_set_file` 以 [write(2)](write.2.md) 的方式使用这些参数。

如果在调用 `extattr_get_file` 和 `extattr_list_file` 时 `data` 为 `NULL`，则返回已定义的扩展属性数据的大小，而非读取的数量，允许应用程序在不执行读取的情况下测试数据的大小。`extattr_delete_link`、`extattr_get_link` 和 `extattr_set_link` 系统调用的行为与其对应的 "_file" 版本相同，区别在于它们不跟随符号链接。

`extattr_get_fd`、`extattr_delete_fd`、`extattr_list_fd` 和 `extattr_set_fd` 调用与其对应的 "_file" 版本相同，区别仅在于第一个参数。"_fd" 函数接受一个文件描述符，而 "_file" 函数接受一个路径。两个参数都描述与应被操作的扩展属性关联的文件。"_fd" 函数可用于以 `O_PATH` 标志打开的文件描述符。

以下参数对这里描述的所有系统调用都是通用的：

**`attrnamespace`** 扩展属性所在的命名空间；参见 [extattr(9)](../man9/extattr.9.md)

**`attrname`** 扩展属性的名称

命名扩展属性的语义因实现该调用的文件系统而异。并非所有操作都可能对特定属性受支持。此外，`data` 中数据的格式是特定于属性的。

有关命名扩展属性的更多信息，请参见 [extattr(9)](../man9/extattr.9.md)。

## 返回值

如果成功，`extattr_get_fd`、`extattr_get_file`、`extattr_get_link`、`extattr_list_fd`、`extattr_list_file`、`extattr_list_link`、`extattr_set_fd`、`extattr_set_file` 和 `extattr_set_link` 调用分别返回从 `data` 读取或写入的字节数。如果 `data` 为 `NULL`，则 `extattr_get_fd`、`extattr_get_file`、`extattr_get_link`、`extattr_list_fd`、`extattr_list_file` 和 `extattr_list_link` 返回可读取的字节数。如果任何一个调用不成功，返回值 -1，并设置全局变量 `errno` 以指示错误。

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

以下错误可能由系统调用本身返回。此外，实现该调用的文件系统可能返回其希望的任何其他错误。

**[`EFAULT`]** `attrnamespace` 和 `attrname` 参数，或由 `data` 和 `nbytes` 定义的内存范围指向进程已分配地址空间之外。

**[`ENAMETOOLONG`]** 属性名称长于 `EXTATTR_MAXNAMELEN`。

`extattr_get_fd`、`extattr_set_fd`、`extattr_delete_fd` 和 `extattr_list_fd` 系统调用还可能在以下情况下失败：

**[`EBADF`]** 由 `fd` 引用的文件描述符无效。

此外，`extattr_get_file`、`extattr_set_file` 和 `extattr_delete_file` 调用还可能因以下错误而失败：

**[`ENOATTR`]** 所请求的属性未为此文件定义。

**[`ENOTDIR`]** 路径前缀的某个分量不是目录。

**[`ENAMETOOLONG`]** 路径名的某个分量超过了 255 个字符，或整个路径名超过了 1023 个字符。

**[`ENOENT`]** 路径名中必须存在的某个分量不存在。

**[`EACCES`]** 拒绝对路径前缀的某个分量进行搜索权限。

## 参见

[extattr(3)](../man3/extattr.3.md), [getextattr(8)](../man8/getextattr.8.md), [setextattr(8)](../man8/setextattr.8.md), [extattr(9)](../man9/extattr.9.md), [VOP_GETEXTATTR(9)](../man9/VOP_GETEXTATTR.9.md), [VOP_SETEXTATTR(9)](../man9/VOP_SETEXTATTR.9.md)

## 历史

扩展属性支持作为 TrustedBSD 项目的一部分开发，并引入 FreeBSD 5.0。其开发旨在支持需要将附加标签与每个文件或目录关联的安全扩展。

## 注意事项

此接口正在积极开发中，因此可能随着应用程序被适配使用它而发生变化。不建议开发者依赖其稳定性。

## 缺陷

在此 API 的早期版本中，向 `extattr_get_fd`、`extattr_get_file` 或 `extattr_get_link` 传递空字符串作为属性名称会返回为目标对象定义的属性列表。此接口已被弃用，建议使用显式的列表 API，不应再使用。
