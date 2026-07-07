# devname(3)

`devname` — 获取设备名称

## 名称

`devname`

## 库

Lb libc

## 概要

```c
#include <sys/stat.h>
#include <stdlib.h>

char *
devname(dev_t dev, mode_t type);

char *
devname_r(dev_t dev, mode_t type, char *buf, int len);

char *
fdevname(int fd);

char *
fdevname_r(int fd, char *buf, int len);
```

## 描述

`devname` 函数返回一个指针，指向 **/dev** 中设备号为 `dev` 且文件类型与 `type` 中编码的类型相匹配的块设备或字符设备的名称，其中 `type` 必须是 `S_IFBLK` 或 `S_IFCHR` 之一。为找到正确的名称，`devname` 通过 `kern.devname` sysctl 询问内核。如果无法得出合适的名称，它将以人类可读的格式封装 `dev` 和 `type` 中的信息。

`fdevname` 和 `fdevname_r` 函数直接从指向字符设备的文件描述符获取设备名称。如果无法得出合适的名称，这些函数将返回 NULL 指针。

`devname` 和 `fdevname` 返回存储在静态缓冲区中的名称，该缓冲区在后续调用时会被覆盖。`devname_r` 和 `fdevname_r` 接受缓冲区和长度作为参数以避免此问题。

## 实例

```c
int fd;
struct stat buf;
char *name;

	fd = open("/dev/tun");
	fstat(fd, &buf);
	printf("devname is /dev/%s\n", devname(buf.st_rdev, S_IFCHR));
	printf("fdevname is /dev/%s\n", fdevname(fd));
```

## 参见

[stat(2)](../sys/stat.2.md)

## 历史

`devname` 函数出现于 4.4BSD。`fdevname` 函数出现于 FreeBSD 8.0。
