# devfs_set_cdevpriv(9)

`devfs_set_cdevpriv` — 管理设备的每次打开文件描述符数据

## 名称

`devfs_set_cdevpriv`, `devfs_get_cdevpriv`, `devfs_clear_cdevpriv`, `devfs_foreach_cdevpriv`

## 概要

```c
#include <sys/param.h>
#include <sys/conf.h>
```

```c
typedef	void d_priv_dtor_t(void *data);
```

```c
int
devfs_get_cdevpriv(void **datap)

int
devfs_set_cdevpriv(void *priv, d_priv_dtor_t *dtr)

void
devfs_clear_cdevpriv(void)

int
devfs_foreach_cdevpriv(struct cdev *dev,
    int (*cb)(void *data, void *arg), void *arg)
```

## 描述

`devfs_xxx_cdevpriv` 系列函数允许 `cdev` 驱动程序方法将某些驱动程序特定的数据与每个用户进程对设备特殊文件的 open(2) 关联。目前，这些函数的功能仅限于在响应使用文件描述符的系统调用时作为 [devfs(4)](../man4/devfs.4.md) 操作而执行的 `cdevsw` 切换方法调用的上下文中。

`devfs_set_cdevpriv` 函数将由 `priv` 指向的数据与当前调用上下文（文件描述符）关联。该数据可以稍后由 `devfs_get_cdevpriv` 函数检索，可能是从在该文件描述符上执行的另一次调用中检索。`devfs_clear_cdevpriv` 解除先前附加到上下文的数据。在 `devfs_clear_cdevpriv` 完成操作后立即调用 `dtr` 回调，并以私有数据作为 `data` 参数。如果打开回调函数返回错误代码，也会调用 `devfs_clear_cdevpriv` 函数。

在最后一次文件描述符关闭时，系统会自动安排调用 `devfs_clear_cdevpriv`。

如果成功，函数返回 0。

`devfs_set_cdevpriv` 函数在出错时返回以下值：

[`ENOENT`] 当前调用未与任何文件描述符关联。

[`EBUSY`] 私有驱动程序数据已与当前文件描述符关联。

`devfs_get_cdevpriv` 函数在出错时返回以下值：

[`EBADF`] 当前调用未与任何文件描述符关联。

[`ENOENT`] 私有驱动程序数据未与当前文件描述符关联，或已调用 `devfs_clear_cdevpriv`。

`devfs_foreach_cdevpriv` 函数按顺序对当前与 `cdev` 设备关联的每个 `cdevpriv` 结构调用函数 `cb`。迭代到的 `cdevpriv` 数据指针和用户提供的上下文 `arg` 被传递给函数 `cb`。如果 `cb` 返回非零值，迭代在该元素上停止。`devfs_foreach_cdevpriv` 返回最后一次调用 `cb` 的返回值，如果当前没有 `cdevpriv` 数据与设备关联，则返回零。

当前迭代器的实现使得无法在回调 `cb` 内部使用任何可阻塞的锁。

## 参见

close(2), open(2), [devfs(4)](../man4/devfs.4.md)

## 历史

`devfs_cdevpriv` 系列函数首次出现于 FreeBSD 7.1。
