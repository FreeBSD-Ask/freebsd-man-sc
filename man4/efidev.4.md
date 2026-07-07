# efidev(4)

`efidev` — 用户态访问 UEFI 运行时服务

## 名称

`efidev`, `efirtc`

## 概要

`若要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> options EFIRT

`或者，若要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
efirt_load="YES"
```

`可通过将 loader(8) 可调参数 efi.rt.disabled 设置为 “1” 来禁用此驱动。`

## 描述

`efirtc` 设备提供用户态对 UEFI 运行时服务的访问。`efirtc` 还包含一个驱动，使用 UEFI 实时时钟（RTC）提供时钟。然而，根据 UEFI 固件的不同，RTC 可能并不总是可用。如果 RTC 不可用，则不会将其注册为时钟，下述与时间相关的 ioctl 也将无法使用。

`efirtc` 提供以下 ioctl，定义于

`#include <sys/efiio.h>`

补充结构和常量定义于

`#include <sys/efi.h>`

```sh
struct efi_get_table_ioc {
	void *buf;
	struct uuid uuid;
	size_t table_len;
	size_t buf_len;
};
```

```sh
struct efi_tm {
	uint16_t	tm_year;
	uint8_t		tm_mon
	uint8_t		tm_mday
	uint8_t		tm_hour;
	uint8_t		tm_min;
	uint8_t		tm_sec;
	uint8_t		 __pad1;
	uint32_t	tm_nsec;
	int16_t		tm_tz;
	uint8_t		tm_dst;
	uint8_t		__pad2;
};
```

```sh
struct efi_var_ioc {
	efi_char	*name;
	size_t		 namesize;
	struct uuid	 vendor;
	uint32_t	 attrib;
	void		*data;
	size_t		 datasize;
};
```

**`EFIIOC_GET_TABLE`** （`struct efi_get_table_ioc`）将 `struct efi_get_table_ioc` 的 `uuid` 字段所指定的 UEFI 表复制到 `buf` 字段。可通过将 `buf` 值传入 `NULL` 指针查询 buf 字段所需的内存大小。所需大小将存储在 `table_len` 字段中。所分配内存的大小必须在 `buf_len` 字段中指定。

**`EFIIOC_GET_TIME`** （`struct efi_tm`）若 RTC 可用，则从 RTC 获取时间。除非发生错误，否则传入的 `struct efi_tm` 将被填充为当前时间。

**`EFIIOC_SET_TIME`** （`struct efi_tm`）若 RTC 可用，则设置 RTC 所存储的时间。

**`EFIIOC_VAR_GET`** （`struct efi_var_ioc`）从 `struct efi_var_ioc` 的 vendor 和 name 字段所描述的变量中读取数据到 `data` 字段。`EFIIOC_VAR_GET` （`struct efi_var_ioc`）还会填充 `attrib` 字段。

**`EFIIOC_VAR_NEXT`** （`struct efi_var_ioc`）用于枚举所有 UEFI 变量。首次调用应将 name 属性设为空字符串。后续调用应提供上次返回变量的 vendor uuid 和名称。

**`EFIIOC_VAR_SET`** （`struct efi_var_ioc`）为 `struct efi_var_ioc` 中 name 和 vendor 所描述的变量设置数据和属性。

## 文件

**`/dev/efi`**

## 参见

efivar(3), [efirt(9)](../man9/efirt.9.md)

## 历史

`efirtc` 设备首次出现于 FreeBSD 11.1。

## 缺陷

`efirtc` 目前仅在 amd64 和 arm64 上可用。
