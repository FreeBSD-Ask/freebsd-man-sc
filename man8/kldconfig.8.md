# kldconfig.8

`kldconfig` — 显示或修改内核模块搜索路径

## 名称

`kldconfig`

## 概要

`kldconfig [-dfimnUv] [-S sysctlname] [path ...]`

`kldconfig -r`

## 描述

`kldconfig` 工具显示或修改内核在使用 [kldload(8)](kldload.8.md) 工具或 kldload(2) 系统调用加载模块时所使用的搜索路径。

可用选项如下：

**`-d`** 从模块搜索路径中移除指定的路径。

**`-f`** 如果要添加的路径已存在于搜索路径中，或要移除的路径不存在于搜索路径中，也不报错。这在启动/关闭脚本中可能很有用，用于向尚未挂载的文件系统添加路径，或在关闭脚本中无条件移除可能在启动期间添加的路径。

**`-i`** 将指定路径添加到搜索路径的开头，而不是末尾。此选项只能在添加路径时使用。

**`-m`** 不用指定的路径集替换模块搜索路径，而是“合并”新条目。

**`-n`** 不实际更改模块搜索路径。

**`-r`** 显示当前搜索路径。如果同时指定了任何路径，则不能使用此选项。

**`-S`** `sysctlname` 指定要使用的 sysctl 名称，代替默认的 `kern.module_path`。

**`-U`** 对当前搜索路径进行“去重”——如果任何目录重复了一次或多次，则只保留第一次出现。此选项隐含 `-m`。

**`-v`** 详细输出：显示新的模块搜索路径。如果路径已更改，且 `-v` 标志被指定多次，则同时显示旧路径。

## 文件

**/boot/kernel**, **/boot/modules**, **/modules** 内核使用的默认模块搜索路径。

## 退出状态

`kldconfig` 工具成功时退出值为 0，发生错误时大于 0。

## 实例

显示模块搜索路径：

```sh
$ kldconfig -r
/boot/kernel;/boot/modules;/boot/dtb;/boot/dtb/overlays
```

尝试从搜索路径中删除 **/boot** 目录。该命令将失败：

```sh
$ kldconfig -d /boot
kldconfig: not in module search path: /boot
$ echo $?
1
```

同上但强制执行操作。这次命令将成功：

```sh
$ kldconfig -d -f /boot
$ echo $?
0
```

将 **/boot** 目录添加到搜索路径开头并显示额外详细输出：

```sh
$ kldconfig -i -m -vv /boot
/boot/kernel;/boot/modules -> /boot;/boot/kernel;/boot/modules
```

不使用 `-m` 时，`-i` 标志将覆盖搜索路径列表的内容：

```sh
$ kldconfig -i -vv /boot
/boot;/boot/kernel;/boot/modules;/boot/dtb;/boot/dtb/overlays -> /boot
```

同上但使用 `-n` 模拟操作而不实际执行：

```sh
$ kldconfig -i -n -vv /boot
/boot;/boot/kernel;/boot/modules;/boot/dtb;/boot/dtb/overlays -> /boot
```

向搜索路径添加目录并删除重复项。注意，如果任何目录已在搜索路径中，需要使用 `-f` 强制操作。**/boot/kernel** 目录将只被添加一次：

```sh
$ kldconfig -f -U /boot/kernel /boot/kernel /boot/modules /boot/dtb /boot/dtb/overlays
```

## 参见

kldload(2), [kldload(8)](kldload.8.md), [kldxref(8)](kldxref.8.md), [sysctl(8)](sysctl.8.md)

## 历史

`kldconfig` 工具首次出现于 FreeBSD 4.4。

## 作者

Peter Pentchev <roam@FreeBSD.org>
