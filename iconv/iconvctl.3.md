# iconvctl(3)

`iconvctl` — 控制 [iconv(3)](iconv.3.md) 的诊断设施

## 名称

`iconvctl`

## 库

Lb libc

## 概要

`#include <iconv.h>`

`Ft int Fn iconvctl iconv_t cd int request void *argument`

## 描述

`iconvctl` 函数可从 `cd` 转换描述符中获取或设置特定的转换设置。`request` 参数指定要完成的操作，`argument` 是与操作相关的参数。

可能的操作如下：

**ICONV_TRIVIALP** 此情况下 `argument` 是 `int *` 变量，若编码为平凡编码（即输入和输出编码相同），则设置为 1。否则，变量设置为 0。

**ICONV_GET_TRANSLITERATE** 确定是否启用音译。答案存储在 `argument` 中，类型为 `int *`。若启用此功能则设置为 1，否则设置为 0。

**ICONV_SET_TRANSLITERATE** 若 `argument`（类型为 `int *`）设置为 1 则启用音译，若 `argument` 设置为 0 则禁用。

**ICONV_GET_DISCARD_ILSEQ** 确定是否丢弃非法序列。答案存储在 `argument` 中，类型为 `int *`。若启用此功能则设置为 1，否则设置为 0。

**ICONV_SET_DISCARD_ILSEQ** 设置是否丢弃非法序列。若 `argument`（类型为 `int *`）设置为 1 则启用，若 `argument` 设置为 0 则禁用。

**ICONV_SET_HOOKS** 设置回调函数，在成功转换后被回调。回调函数存储在 `struct iconv_hooks` 变量中，通过其地址经由 `argument` 传递给 `iconvctl`。

**ICONV_GET_ILSEQ_INVALID** 确定输入缓冲区中合法但在目标代码集中不存在相同字符的字符是否返回 EILSEQ。答案存储在 `argument` 中，类型为 `int *`。若启用此功能则设置为 1，否则设置为 0。

**ICONV_SET_ILSEQ_INVALID** 设置输入缓冲区中合法但在目标代码集中不存在相同字符的字符是否返回 EILSEQ。若 `argument`（类型为 `int *`）设置为 1 则启用，若 `argument` 设置为 0 则禁用。

## 返回值

`iconvctl` 成功完成时返回 0。否则，返回 -1 并设置 errno 以指示错误类型。

## 错误

`iconvctl` 函数可能在以下情况下导致错误：

**[Er** EINVAL] 未知或未实现的操作。

**[Er** EBADF] `cd` 指定的转换描述符无效。

## 参见

iconv(1), [iconv(3)](iconv.3.md)

## 标准

`iconvctl` 设施是非标准扩展，最早出现于 GNU 实现，为兼容性考虑在 FreeBSD 9.0 中引入。

## 作者

本手册页由 Gabor Kovesdan <gabor@FreeBSD.org> 编写。

## 缺陷

本实现中音译默认启用，因此从设计上无法关闭。相应地，尝试关闭音译将始终失败并返回 -1。不过，获取音译状态将始终成功并指示其已开启。
