# setruid(3)

`setruid` — 设置用户和组 ID

## 名称

`setruid`, `setrgid`

## 库

Lb libc

## 概要

`#include <unistd.h>`

`Ft int Fn setruid uid_t ruid Ft int Fn setrgid gid_t rgid`

## 描述

`setruid` 函数（`setrgid`）设置当前进程的实际用户 ID（组 ID）。

## 返回值

Rv -std

## 兼容性

这些调用的使用不具备可移植性。不鼓励使用它们；它们将在未来被移除。

## 错误

以下情况函数会失败：

**[Er** EPERM] 用户不是超级用户且指定的 ID 不是实际或有效 ID。

## 参见

[getgid(2)](../man2/getgid.2.md), [getuid(2)](../man2/getuid.2.md), setegid(2), seteuid(2), setgid(2), [setuid(2)](../man2/setuid.2.md)

## 历史

`setruid` 和 `setrgid` 系统调用出现于 4.2BSD，在 4.4BSD 中被移除。
