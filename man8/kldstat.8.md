# kldstat.8

`kldstat` — 显示动态内核链接器状态

## 名称

`kldstat`

## 概要

`kldstat [-h] [-q] [-v] [-d] [-i id] [-n filename]`

`kldstat [-q] [-d] [-m modname]`

## 描述

`kldstat` 工具显示动态链接到内核的任何文件的状态。

可用选项如下：

**`-d`** 显示模块特定数据（以 int、unsigned int 和 unsigned long 形式）

**`-h`** 以人类可读的形式显示 size 字段，使用单位后缀代替十六进制值。

**`-i`** `id` 仅显示具有此 ID 的文件的状态。

**`-m`** `modname` 仅显示具有此 modname 的模块的状态。

**`-n`** `filename` 仅显示具有此 filename 的文件的状态。

**`-q`** 静默检查文件是否已加载或编译进内核。

**`-v`** 显示更详细的信息。

## 退出状态

`kldstat` 工具成功时退出值为 0，发生错误时大于 0。

## 实例

显示动态链接到内核的文件。注意内核本身也显示在列表中。*Refs* 显示每个文件引用的模块数量：

```sh
$ kldstat
Id Refs Address                Size Name
 1   38 0xffffffff80200000  2448f20 kernel
 2    3 0xffffffff82649000    b7bd8 linux.ko
 3    5 0xffffffff82701000     9698 linux_common.ko
 4    1 0xffffffff82b11000     1eae linsysfs.ko
 5    1 0xffffffff82b13000    f2af8 nvidia-modeset.ko
 6    1 0xffffffff82c06000  122b020 nvidia.ko
 7    1 0xffffffff83e32000     2668 intpm.ko
 8    1 0xffffffff83e35000      b50 smbus.ko
 9    1 0xffffffff83e36000     18a0 uhid.ko
10    1 0xffffffff83e38000     2928 ums.ko
11    1 0xffffffff83e3b000     1aa0 wmt.ko
12    1 0xffffffff83e3d000     cd70 snd_uaudio.ko
```

显示 *linux* 文件的详细状态，并以人类可读的方式显示大小：

```sh
$ kldstat -h -v -n linux
Id Refs Address             Size Name
 2    3 0xffffffff82649000  735K linux.ko (/boot/kernel/linux.ko)
        Contains modules:
                 Id Name
                  2 linuxelf
```

同上，但使用文件的 *id*：

```sh
$ kldstat -h -i 2 -v
Id Refs Address             Size Name
 2    3 0xffffffff82649000  735K linux.ko (/boot/kernel/linux.ko)
        Contains modules:
                 Id Name
                  2 linuxelf
```

显示上例中获得的 *linuxelf* 模块的状态：

```sh
$ kldstat -v -m linuxelf
Id  Refs Name
  2    1 linuxelf
```

显示 *g_raid* 模块的模块特定数据：

```sh
$ kldstat -d -m g_raid
Id  Refs Name data..(int, uint, ulong)
366    1 g_raid (0, 0, 0x0)
```

检查模块 *fakefile* 是否已链接。如果是则返回 0，否则返回 1：

```sh
$ kldstat -q -n fakefile || echo file not linked
file not linked
```

## 参见

kldstat(2), [kldload(8)](kldload.8.md), [kldunload(8)](kldunload.8.md)

## 历史

`kldstat` 工具首次出现于 FreeBSD 3.0，替代了 `lkm` 接口。

## 作者

Doug Rabson <dfr@FreeBSD.org>
