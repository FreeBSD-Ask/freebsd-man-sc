# mac(3)

`mac` — MAC 安全 API 简介

## 名称

`mac`

## 库

libc

## 概要

`#include <sys/mac.h>`

在内核配置文件中：`options MAC`

## 描述

强制访问控制（Mandatory Access Control）标签描述操作系统对象的机密性、完整性及其他安全属性，覆盖自主访问控制。并非所有系统对象都支持 MAC 标签，且 MAC 策略必须由管理员显式启用。此 API 基于 POSIX.1e，包含用于检索、操作、设置以及在文本与文件和进程的 MAC 标签之间转换的例程。

MAC 标签由一组（名称, 值）元组组成，表示来自 MAC 策略的安全属性。例如，以下标签包含由两个策略 [mac_biba(4)](../man4/mac_biba.4.md) 和 [mac_mls(4)](../man4/mac_mls.4.md) 定义的安全标签：

```sh
biba/low,mls/low
```

关于 MAC 标签的进一步语法和语义，可在 [maclabel(7)](../man7/maclabel.7.md) 中找到。

应用程序对存储在 `mac_t` 中的标签进行操作，但可在该内部格式与文本格式之间转换，以便向用户展示或外部存储。查询对象上的标签时，必须首先使用 [mac_prepare(3)](mac_prepare.3.md) 中描述的接口准备 `mac_t`，使应用程序能够声明其希望查询哪些策略。应用程序编写者还可依赖 mac.conf(5) 中声明的默认标签名称。

使用完 `mac_t` 后，应用程序必须调用 [mac_free(3)](mac_free.3.md) 释放其存储空间。

定义了以下函数：

**`mac_is_present`** 此函数在 [mac_is_present(3)](mac_is_present.3.md) 中描述，允许应用程序测试是否配置了 MAC，以及是否配置了特定策略。

**`mac_get_fd`**, **`mac_get_file`**, **`mac_get_link`**, **`mac_get_peer`** 这些函数在 [mac_get(3)](mac_get.3.md) 中描述，检索与文件描述符、文件和套接字对端关联的 MAC 标签。

**`mac_get_pid`**, **`mac_get_proc`** 这些函数在 [mac_get(3)](mac_get.3.md) 中描述，检索与进程关联的 MAC 标签。

**`mac_set_fd`**, **`mac_set_file`**, **`mac_set_link`** 这些函数在 [mac_set(3)](mac_set.3.md) 中描述，设置与文件描述符和文件关联的 MAC 标签。

**`mac_set_proc`** 此函数在 [mac_set(3)](mac_set.3.md) 中描述，设置与当前进程关联的 MAC 标签。

**`mac_free`** 此函数在 [mac_free(3)](mac_free.3.md) 中描述，释放工作 MAC 标签存储。

**`mac_from_text`** 此函数在 [mac_text(3)](mac_text.3.md) 中描述，将文本形式的 MAC 标签转换为工作 MAC 标签存储 `mac_t`。

**`mac_prepare`**, **`mac_prepare_file_label`**, **`mac_prepare_ifnet_label`**, **`mac_prepare_process_label`**, **`mac_prepare_type`** 这些函数在 [mac_prepare(3)](mac_prepare.3.md) 中描述，为 MAC 标签操作分配工作存储。[mac_prepare(3)](mac_prepare.3.md) 基于调用者指定的标签名称准备标签；其他调用依赖于 mac.conf(5) 中指定的默认配置。

**`mac_to_text`** 此函数在 [mac_text(3)](mac_text.3.md) 中描述，可用于将 `mac_t` 转换为文本形式的 MAC 标签。

## 文件

**/etc/mac.conf** MAC 库配置文件，在 mac.conf(5) 中记载。为感知系统对象上 MAC 标签但不具备策略特定知识的应用程序提供默认行为。

## 参见

[mac_free(3)](mac_free.3.md), [mac_get(3)](mac_get.3.md), [mac_is_present(3)](mac_is_present.3.md), [mac_prepare(3)](mac_prepare.3.md), [mac_set(3)](mac_set.3.md), [mac_text(3)](mac_text.3.md), [posix1e(3)](posix1e.3.md), [mac(4)](../man4/mac.4.md), mac.conf(5), [mac(9)](../man9/mac.9.md)

## 标准

这些 API 松散地基于 POSIX.1e 中描述的 API，如 IEEE POSIX.1e 草案 17 所述。然而，这些 API 与 POSIX API 的相似性较为松散，因为 POSIX API 无法表达灵活且可扩展的访问控制所需的某些概念。

## 历史

对强制访问控制（Mandatory Access Control）的支持作为 TrustedBSD 项目的一部分引入于 FreeBSD 5.0。
