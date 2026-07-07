# tvtohz(9)

`tvtohz` — 将时间间隔转换为时钟滴答数

## 名称

`tvtohz`

## 概要

`#include <sys/time.h>`

`int tvtohz(struct timeval *tv)`

## 描述

`tvtohz()` 函数接受单个参数 `tv`，该参数指定要计算将经过的系统时钟滴答数的时间间隔。

## 返回值

返回在给定间隔内预期经过的系统时钟滴答整数数，包括当前滴答。

## 参见

[callout(9)](callout.9.md), [microtime(9)](microtime.9.md), [microuptime(9)](microuptime.9.md)

## 历史

`tvtohz` 函数首次出现在 FreeBSD 3.0 中。

## 作者

本手册页由 Kelly Yancey <kbyanc@posi.net> 编写。
