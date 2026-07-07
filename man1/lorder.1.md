# lorder(1)

`lorder` — 列出目标文件的依赖关系

## 名称

`lorder`

## 概要

`lorder file`

## 描述

`lorder` 实用程序使用 nm(1) 来确定命令行上列出的目标文件和库归档之间的相互依赖关系。然后输出一组文件名对，其中每对中的第一个文件至少引用了由第二个文件定义的一个符号。

该输出通常在创建库时与 tsort(1) 配合使用，以确定目标模块的最佳排序，使所有引用能在加载器的一次遍历中解析。

类似地，在链接静态二进制文件时，可使用 `lorder` 和 tsort(1) 按依赖顺序对库进行排序。

虽然现代链接器不再需要使用 `lorder`，但为了仍需要它的遗留代码库和构建系统，保留该工具。

## 环境变量

**`NM`** nm(1) 二进制文件的路径，默认为“`nm`”。

**`NMFLAGS`** 传递给 nm(1) 的标志。

## 实例

```sh
ar cr library.a `lorder ${OBJS} | tsort`
cc -o foo ${OBJS} `lorder ${STATIC_LIBS} | tsort`
```

## 参见

[ar(1)](ar.1.md), [ld(1)](ld.1.md), nm(1), [ranlib(1)](ranlib.1.md), tsort(1)

## 历史

`lorder` 实用程序首次出现于 Version 7 AT&T UNIX。

## 注意事项

如果给定的文件名中包含空格或换行符，`lorder` 实用程序将无法正常工作。
