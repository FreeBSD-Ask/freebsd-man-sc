# getdomainname.3

`getdomainname` — 获取/设置当前主机的 NIS 域名

## 名称

`getdomainname`, `setdomainname`

## 库

Lb libc

## 概要

`#include <unistd.h>`

`Ft int Fn getdomainname char *name int namelen Ft int Fn setdomainname const char *name int namelen`

## 描述

`getdomainname` 函数返回当前主机的标准 NIS 域名，该域名此前由 `setdomainname` 设置。`namelen` 参数指定 `name` 数组的大小。除非提供的空间不足，否则返回的名称以 null 结尾。

`setdomainname` 函数将主机的 NIS 域名设置为 `name`，其长度为 `namelen`。此调用仅限超级用户使用，通常仅在系统引导时使用。

## 返回值

Rv -std

## 错误

这些调用可能返回以下错误：

**[Er** EFAULT] `name` 或 `namelen` 参数给出了无效地址。

**[Er** EPERM] 调用者试图设置主机名且不是超级用户。

## 参见

[gethostid(3)](../compat-43-1/gethostid.3.md), [gethostname(3)](gethostname.3.md), [sysctl(3)](sysctl.3.md)

## 历史

`getdomainname` 函数出现于 4.2BSD。

## 缺陷

域名长度限制为 `MAXHOSTNAMELEN`（来自

`#include <sys/param.h>`

）个字符，当前为 256。
