# flockfile(3)

`flockfile` — stdio 锁定函数

## 名称

`flockfile`, `ftrylockfile`, `funlockfile`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`Ft void Fn flockfile FILE *stream Ft int Fn ftrylockfile FILE *stream Ft void Fn funlockfile FILE *stream`

## 描述

这些函数提供应用层面的显式 stdio 流锁定。它们可用于避免多线程输出交错、输入分散到多个读取者，以及避免每次操作都锁定流的开销。

`flockfile` 函数获取指定流的独占锁。若另一线程已锁定该流，`flockfile` 将阻塞直至锁被释放。

`ftrylockfile` 函数是 `flockfile` 的非阻塞版本；若无法立即获取锁，`ftrylockfile` 返回非零值而非阻塞。

`funlockfile` 函数释放由先前调用 `flockfile` 或 `ftrylockfile` 获取的流锁。

这些函数的行为如同每个流关联一个锁计数。每次对该流调用 `flockfile`，计数递增；每次调用 `funlockfile`，计数递减。仅当计数减至零时，锁才真正释放。

## 返回值

`flockfile` 和 `funlockfile` 函数不返回值。

`ftrylockfile` 函数成功锁定流时返回零，否则返回非零值。

## 参见

getc_unlocked(3), putc_unlocked(3)

## 标准

`flockfile`、`ftrylockfile` 和 `funlockfile` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1") 标准。
