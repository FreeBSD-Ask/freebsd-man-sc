# devctl_process_running.9

`devctl_process_running` — 当 devctl 有消费者进程运行时返回真

## 名称

`devctl_process_running`

## 概要

```c
#include <sys/devctl.h>

bool
devctl_process_running(void)
```

## 描述

`devctl_process_running` 调用在某个进程为读取而打开 devctl 设备时返回 `true`，否则返回 `false`。可以由此假定，当返回 `true` 时，默认的 devd(8) 或类似程序正在运行。某些子系统会发送消息并允许用户态在以超时方式进行默认操作之前执行某些操作。此调用允许这些子系统在没有进程运行时立即执行默认操作。

## 参见

devd(8)

## 作者

本手册页由 M. Warner Losh 编写。
