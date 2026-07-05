# makedev.3

`makedev` — 设备号转换

## 名称

`makedev`, `major`, `minor`

## 概要

`#include <sys/types.h>`

`Ft dev_t Fn makedev int major int minor Ft int Fn major dev_t dev Ft int Fn minor dev_t dev`

## 描述

`Fn makedev` 宏返回由所提供的 `major` 和 `minor` 号创建的设备号。`Fn major` 和 `Fn minor` 宏从设备号 `dev` 中还原出原始号码。换句话说，对于类型为 `dev_t` 的值 `dev`，以及类型为 `int` 的值 `ma`、`mi`，以下断言成立：

```sh
dev == makedev(major(dev), minor(dev))
```

```sh
ma == major(makedev(ma, mi))
```

```sh
mi == minor(makedev(ma, mi))
```

在 FreeBSD 的早期实现中，所有块设备和字符设备都通过一对稳定的主次设备号唯一标识。主设备号指向某一设备类别（例如磁盘、TTY），而次设备号标识该设备类别中的一个实例。FreeBSD 后续版本会为 **`/dev/`** 中可见的每个字符设备自动生成唯一的设备号。这些号码不按设备类别划分，且在系统重启或驱动重新加载后不保证保持稳定。

在 FreeBSD 上，这些宏仅用于需要与可能对 `dev_t` 使用不同编码的其他操作系统交换号码的工具，以及以更传统方式将这些号码呈现给用户的应用程序。

## 返回值

`Fn major` 和 `Fn minor` 宏返回的数字取值范围可覆盖整个 `int` 范围。

## 参见

mknod(2), devname(3), [devfs(4)](../man4/devfs.4.md)
