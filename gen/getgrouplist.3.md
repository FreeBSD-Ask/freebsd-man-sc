# getgrouplist(3)

`getgrouplist` — 生成用户的有效组列表

## 名称

`getgrouplist`

## 库

Lb libc

## 概要

`#include <unistd.h>`

`Ft int Fn getgrouplist const char *name gid_t basegid gid_t *groups int *ngroups`

## 描述

`getgrouplist` 函数从组数据库中检索由 `name` 指定的用户的补充组，并返回有效组列表，其中第一个组是 `basegid` 的值，其余为补充组。`basegid` 通常是从密码数据库中获取的用户初始数字组 ID。

有效组列表通过 `groups` 所指向的数组返回。调用者通过 `ngroups` 所指向的整数指定 `groups` 数组的长度。有效组列表的组数（可能大于 `groups` 数组的长度）通过 `ngroups` 返回。

## 返回值

`getgrouplist` 函数成功时返回 0，若组列表长度太小而无法容纳用户的所有组则返回 -1。后一种情况下，`groups` 数组从有效组列表开头尽可能多地填入组，`ngroups` 所指向的长度被设置为有效组列表的完整长度，即严格大于调用前的值。

## 文件

**/etc/group** 组成员列表

## 参见

[setcred(2)](../sys/setcred.2.md), [setgroups(2)](../sys/setgroups.2.md), [initgroups(3)](initgroups.3.md)

## 历史

`getgrouplist` 函数首次出现于 4.4BSD。
