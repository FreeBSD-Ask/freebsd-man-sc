# rev.1

`rev` — 反转文件的行

## 名称

`rev` — 反转文件的行

## 概要

`rev [file]`

## 描述

`rev` 实用程序将指定文件复制到标准输出，反转每行中字符的顺序。如果未指定文件，则读取标准输入。

## 实例

从标准输入反转文本：

```sh
$ echo -e "reverse \t these\ntwo lines" | rev
eseht    esrever
senil owt
```
