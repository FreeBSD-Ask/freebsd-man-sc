# growfs(8)

`growfs` — 扩展已有的 UFS 文件系统

## 名称

`growfs`

## 概要

`growfs [-Ny] [-s size] special | filesystem`

## 描述

`growfs` 工具可用于扩展 UFS 文件系统。在运行 `growfs` 之前，必须先使用 [gpart(8)](gpart.8.md) 扩展包含该文件系统的分区或切片。`growfs` 工具会在指定的 special 文件上扩展文件系统的大小。可用选项如下：

**`-N`** “测试模式”。打印新的文件系统参数，而不实际扩展文件系统。

**`-s`** `size` 确定扩展后文件系统的大小（以扇区为单位）。`Size` 为 512 字节扇区的数量，除非带有后缀 `b`、`k`、`m`、`g` 或 `t`，分别表示字节、千字节、兆字节、吉字节和太字节。该值默认为 `special` 中指定的原始分区的大小（换言之，`growfs` 会将文件系统扩展到整个分区的大小）。

**`-y`** 使 `growfs` 对所有操作者问题都假定回答 yes。

## 退出状态

成功时退出状态为 0，出错时为 >= 1。可通过用户操作恢复的错误以 2 表示。操作系统错误（通常不可恢复）以 3 或更大的值表示。

## 实例

将根文件系统扩展以填满可用空间：

```sh
growfs /
```

刷新 LUN 大小，调整分区以使用所有可用容量，并相应地扩展文件系统：

```sh
camcontrol reprobe da0
```

```sh
gpart recover da0
```

```sh
gpart resize -i 1 da0
```

```sh
growfs /dev/da0p1
```

## 参见

[growfs(7)](../man7/growfs.7.md), [camcontrol(8)](camcontrol.8.md), fsck(8), [gpart(8)](gpart.8.md), newfs(8), tunefs(8)

## 历史

`growfs` 工具首次出现于 FreeBSD 4.4。调整已挂载文件系统大小的功能在 FreeBSD 10.0 中加入。

## 作者

Christoph Herrmann <chm@FreeBSD.org> Thomas-Henning von Kamptz <tomsoft@FreeBSD.org> The GROWFS team <growfs@Tomsoft.COM> Edward Tomasz Napierala <trasz@FreeBSD.org>

## 注意事项

当扩展以读写方式挂载的文件系统时，对该文件系统的任何写入操作都会暂时挂起，直到扩展完成。

## 缺陷

通常 `growfs` 会将柱面组摘要写入磁盘，稍后再读取以进行更多更新。使用 `-N` 时，此读取操作会提供意外数据。因此，这部分无法真正模拟，在测试模式下会被跳过。
