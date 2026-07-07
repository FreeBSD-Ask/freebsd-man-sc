# undelete.2

`undelete` — 尝试恢复已删除的文件

## 名称

`undelete`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
int
undelete(const char *path)
```

## 描述

`undelete()` 系统调用尝试恢复由 `path` 命名的已删除文件。目前，这仅在命名对象是联合文件系统中的 whiteout 时有效。该系统调用移除 whiteout，使联合栈下层中的任何对象再次变为可见。

最终，`undelete()` 功能可能会扩展到其他能够恢复已删除文件的文件系统，如日志结构文件系统。

## 返回值

成功完成时，`undelete()` 函数返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`undelete()` 在以下情况之外会成功：

**[`ENOTDIR`]** 路径前缀的某个组件不是目录。

**[`ENAMETOOLONG`]** 路径名的某个组件超过 255 个字符，或整个路径名超过 1023 个字符。

**[`EEXIST`]** 路径未引用 whiteout。

**[`ENOENT`]** 指定的 whiteout 不存在。

**[`EACCES`]** 拒绝对路径前缀某个组件的搜索权限。

**[`EACCES`]** 拒绝对包含要恢复名称的目录的写权限。

**[`ELOOP`]** 在转换路径名时遇到过多的符号链接。

**[`EPERM`]** 包含该名称的目录被标记为粘滞位，且包含目录并非由有效用户 ID 拥有。

**[`EINVAL`]** 路径的最后一个组件是 `..`。

**[`EIO`]** 更新目录项时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

**[`EROFS`]** 该名称位于只读文件系统上。

**[`EFAULT`]** `path` 参数指向进程已分配的地址空间之外。

## 参见

[unlink(2)](unlink.2.md), mount_unionfs(8)

## 历史

`undelete()` 系统调用首次出现于 4.4BSD。
