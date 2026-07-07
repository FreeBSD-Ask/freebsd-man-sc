# uidinfo(9)

`uidinfo` — 管理 UID 信息的函数

## 名称

`uidinfo`, `uihashinit`, `uifind`, `uihold`, `uifree`

## 概要

`#include <sys/param.h>`

`#include <sys/proc.h>`

`#include <sys/resourcevar.h>`

`void uihashinit(void)`

`struct uidinfo * uifind(uid_t uid)`

`void uihold(struct uidinfo *uip)`

`void uifree(struct uidinfo *uip)`

## 描述

`uifree` 系列函数用于管理 `uidinfo` 结构。每个 `uidinfo` 结构维护每个 UID 的资源消耗计数，包括进程数和套接字缓冲区空间使用量。

`uihashinit()` 函数初始化 `uidinfo` 哈希表及其互斥锁。此函数仅在系统初始化期间调用。

`uifind()` 函数查找并返回 `uid` 对应的 `uidinfo` 结构。如果 `uid` 不存在对应的 `uidinfo` 结构，将分配并初始化一个新结构。会获取和释放 `uifree` 哈希互斥锁。

`uihold()` 函数增加 `uip` 的引用计数。会获取和释放 `uip` 的锁。

`uifree()` 函数减少 `uip` 的引用计数，如果计数达到 0 则释放 `uip`。会获取和释放 `uip` 的锁，并可能获取和释放 uidinfo 哈希互斥锁。

## 返回值

`uifind()` 返回指向已初始化 `uidinfo` 结构的指针，且不会失败。

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
