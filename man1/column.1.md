# column.1

`column` — 将列表按列排版

## 名称

`column`

## 概要

`column [-tx] [-c columns] [-l tblcols] [-s sep] [file]`

## 描述

`column` 实用程序将输入格式化为多列。行先于列被填充。输入取自 `file` 操作数，默认情况下取自标准输入。空行被忽略。

选项如下：

**`-c`** 输出格式化为 `columns` 列宽显示。

**`-l`** 与 `-t` 一起使用时，将表格宽度限制为 `tblcols` 列。最后一列将包含该行的剩余部分，包括任何分隔符。

**`-s`** 指定一组字符，用于 `-t` 选项的列分隔。

**`-t`** 确定输入包含的列数并创建表格。默认情况下列以空白分隔，或使用 `-s` 选项提供的字符分隔。适用于美化显示输出。

**`-x`** 先填充列再填充行。

## 环境变量

`COLUMNS`、`LANG`、`LC_ALL` 和 `LC_CTYPE` 环境变量会影响 `column` 的执行，如 [environ(7)](../man7/environ.7.md) 所述。

## 退出状态

`column` 实用程序成功时退出值为 0，发生错误时大于 0。

## 实例

```sh
(printf "PERM LINKS OWNER GROUP SIZE MONTH DAY " ; \
printf "HH:MM/YEAR NAME\n" ; \
ls -l | sed 1d) | column -t
```

## 参见

[colrm(1)](colrm.1.md), [ls(1)](ls.1.md), [paste(1)](paste.1.md), [sort(1)](sort.1.md)

## 历史

`column` 命令首次出现于 4.3BSD Reno。

## 缺陷

输入行长度限制为 `LINE_MAX`（2048）字节。
