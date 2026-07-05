# veriexec.4

`veriexec` — veriexec 设备

## 名称

`veriexec`

## 概要

`#include <dev/veriexec/veriexec_ioctl.h>`

## 描述

`veriexec` 设备由 veriexec(8) 用于查询和修改 mac_veriexec(4) 的状态。

当 mac_veriexec(4) 处于活动状态后，只有标记为 `trusted` 的进程（通常只有 veriexec(8)）才能执行超出 `VERIEXEC_GETSTATE` ioctl 的操作。

## IOCTL

支持的 ioctl 如下所述。

```sh
struct verified_exec_params  {
	unsigned char flags;
	char fp_type[VERIEXEC_FPTYPELEN];	/* 指纹类型 */
	char file[MAXPATHLEN];
	unsigned char fingerprint[MAXFINGERPRINTLEN];
};
```

```sh
struct verified_exec_label_params  {
	struct verified_exec_params params;
	char label[MAXLABELLEN];
};
```

**`VERIEXEC_SIGNED_LOAD`** `struct verified_exec_params` 将文件信息传递给 mac_veriexec(4)。

**`VERIEXEC_LABEL_LOAD`** `struct verified_exec_label_params` 将文件信息和标签传递给 mac_veriexec(4)。

**`VERIEXEC_ACTIVE`**

**`VERIEXEC_DEBUG_OFF`**

**`VERIEXEC_DEBUG_ON`** `int level`

**`VERIEXEC_ENFORCE`**

**`VERIEXEC_GETSTATE`**

**`VERIEXEC_GETVERSION`**

**`VERIEXEC_LOCK`**

**`VERIEXEC_VERIFIED_FILE`** `int fd` 很少使用。告知 mac_veriexec(4) 与 `fd` 关联的文件已通过验证。

## 历史

`veriexec` 设备最早出现于 NetBSD。在 FreeBSD 13.1 中引入。
