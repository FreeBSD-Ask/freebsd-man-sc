# pseudofs.9

`pseudofs` — 伪文件系统构建工具包

## 名称

`pseudofs`

## 概要

```c
#include <fs/pseudofs/pseudofs.h>
```

## 描述

`pseudofs` 模块为伪文件系统（如 [procfs(4)](../man4/procfs.4.md) 和 [linprocfs(4)](../man4/linprocfs.4.md)）提供了抽象 API。它负责处理所有复杂的细节，如与 VFS 系统交互、强制访问控制、跟踪文件号，以及克隆特定于进程的文件和目录。消费者模块（即实现文件系统实际核心的模块）只需提供目录结构（由 `pseudofs` 提供的宏声明和初始化的结构集合表示）以及报告文件属性或将实际文件内容写入 sbuf 的回调函数。

## 参见

[linprocfs(4)](../man4/linprocfs.4.md), [linsysfs(4)](../man4/linsysfs.4.md), [procfs(4)](../man4/procfs.4.md), [sbuf(9)](sbuf.9.md), [vnode(9)](vnode.9.md)

## 历史

`pseudofs` 模块首次出现在 FreeBSD 5.0 中。

## 作者

`pseudofs` 模块和本手册页由 Dag-Erling Smørgrav <des@FreeBSD.org> 编写。
