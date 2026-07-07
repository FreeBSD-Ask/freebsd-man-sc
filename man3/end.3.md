# end(3)

`end` — 镜像段的结束边界

## 名称

`end`, `etext`, `edata`

## 概要

```c
extern end;
extern etext;
extern edata;
```

## 描述

全局变量 `end`、`etext` 和 `edata` 是程序段的结束地址。

`etext` 是文本段结束后的第一个地址。

`edata` 是已初始化数据段结束后的第一个地址。

`end` 是程序加载时数据段（BSS）结束后的第一个地址。使用 sbrk(2) 系统调用并以零作为参数，可找到数据段的当前末尾。

## 参见

sbrk(2), malloc(3), [a.out(5)](../man5/a.out.5.md)

## 历史

`edata` 手册页出现于 Version 6 AT&T UNIX。

## 缺陷

按惯例，不存在指向文本段起始位置的变量，因为文本段总是从地址零开始。尽管这一假设已不再成立，但并不存在与上述文档类似的指向文本段起始位置的变量。
