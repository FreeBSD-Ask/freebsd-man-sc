# getpass(3)

`getpass` — 获取密码

## 名称

`getpass`

## 库

Lb libc

## 概要

```c
#include <pwd.h>
#include <unistd.h>

char *
getpass(const char *prompt);
```

## 描述

`getpass` 函数向 **/dev/tty** 显示提示符，并从中读取密码。如果该文件不可访问，`getpass` 在标准错误输出上显示提示符，并从标准输入读取。

密码长度最多为 `_PASSWORD_LEN`（当前为 128）个字符。任何额外字符及终止换行符均被丢弃。

`getpass` 函数在读取密码时关闭字符回显。

## 返回值

`getpass` 函数返回指向以 null 终止的密码的指针。

## 文件

**/dev/tty**

## 参见

crypt(3), [readpassphrase(3)](readpassphrase.3.md)

## 历史

`getpass` 函数出现于 Version 7 AT&T UNIX。

## 缺陷

`getpass` 函数将其结果保留在内部静态对象中，并返回指向该对象的指针。后续对 `getpass` 的调用将修改同一对象。

调用进程应尽快将密码清零，以避免明文密码在进程地址空间中可见。

收到 `SIGTSTP` 时，输入缓冲区将被刷新，因此进程继续时必须重新输入任何已部分输入的密码。
