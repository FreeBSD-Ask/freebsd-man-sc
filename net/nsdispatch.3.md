# nsdispatch(3)

`nsdispatch` — 名字服务开关分派例程

## 名称

`nsdispatch`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <stdarg.h>`

`#include <nsswitch.h>`

```c
int
nsdispatch(void *retval, const ns_dtab dtab[], const char *database,
    const char *method_name, const ns_src defaults[], ...);
```

## 描述

`nsdispatch` 函数按 [nsswitch.conf(5)](../man5/nsswitch.conf.5.md) 为数据库 `database` 指定的顺序调用 `dtab` 中指定的方法，直到找到成功的条目。

`retval` 传递给每个方法以根据需要进行修改，用于将结果传回 `nsdispatch` 的调用者。

每个方法具有以下 typedef 描述的函数签名：

```c
typedef int (*nss_method)(void *retval, void *mdata, va_list *ap);
```

`dtab` 是一个 `ns_dtab` 结构数组，其格式如下：

```c
typedef struct _ns_dtab {
	const char	*src;
	nss_method	 method;
	void		*mdata;
} ns_dtab;
```

`dtab` 数组应为每个已实现的源类型包含一个条目，`src` 为源名称，`method` 为处理该源的函数，`mdata` 为要传递给方法的任意数据的句柄。`dtab` 中的最后一个条目应将 `src`、`method` 和 `mdata` 设为 `NULL`。

此外，方法可以在 NSS 模块中实现，此时使用 `database` 和 `method_name` 参数以及配置的源来选择。模块必须使用与内置源不同的源名称。

`defaults` 包含在 [nsswitch.conf(5)](../man5/nsswitch.conf.5.md) 缺失或损坏，或没有 `database` 的相关条目时要尝试的默认源列表。它是 `ns_src` 结构数组，其格式如下：

```c
typedef struct _ns_src {
	const char	*src;
	uint32_t	 flags;
} ns_src;
```

`defaults` 数组应由 `src` 指示的每个默认配置源的一个条目组成，`flags` 设为所需的标准（通常为 `NS_SUCCESS`；更多信息请参见方法返回值）。`defaults` 中的最后一个条目应将 `src` 设为 `NULL`、`flags` 设为 0。

为方便起见，定义了如下全局变量：

```c
extern const ns_src __nsdefaultsrc[];
```

其中包含源 'files' 的单个默认条目，可供不需要复杂默认规则的调用者使用。

'`...`' 是可选的额外参数，作为 `va_list` 类型的可变参数列表传递给相应的方法。

### 有效源类型

虽然支持任意源，但以下为常用实现的源提供的 #define：

| #define | 值 |
| --- | --- |
| `NSSRC_FILES` | "files" |
| `NSSRC_DB` | "db" |
| `NSSRC_DNS` | "dns" |
| `NSSRC_NIS` | "nis" |
| `NSSRC_COMPAT` | "compat" |

关于每种源类型的完整描述，参见 [nsswitch.conf(5)](../man5/nsswitch.conf.5.md)。

### 方法返回值

`nss_method` 函数必须根据查找状态返回以下值之一：

| 返回值 | 状态码 |
| --- | --- |
| `NS_SUCCESS` | success |
| `NS_NOTFOUND` | notfound |
| `NS_UNAVAIL` | unavail |
| `NS_TRYAGAIN` | tryagain |
| `NS_RETURN` | -none- |

关于每个状态码的完整描述，参见 [nsswitch.conf(5)](../man5/nsswitch.conf.5.md)。

`nsdispatch` 函数返回导致分派器终止的方法的返回值，否则返回 `NS_NOTFOUND`。

## 注意事项

FreeBSD 的 libc 为兼容为 GNU C 库 `nsswitch` 接口编写的 NSS 模块提供了桩函数。但这些桩函数仅支持 "`passwd`" 和 "`group`" 数据库的使用。

## 参见

[hesiod(3)](hesiod.3.md), [stdarg(3)](../man3/stdarg.3.md), [nsswitch.conf(5)](../man5/nsswitch.conf.5.md), [yp(8)](../man8/yp.8.md)

## 历史

`nsdispatch` 函数首次出现于 FreeBSD 5.0。它从 NetBSD 项目引入，最初出现于 NetBSD 1.4。对 NSS 模块的支持首次出现于 FreeBSD 5.1。

## 作者

Luke Mewburn <lukem@netbsd.org> 编写了这一可自由分发的名字服务开关实现，采用了来自 ULTRIX svc.conf(5) 和 Solaris nsswitch.conf(4) 手册页的想法。FreeBSD 项目添加了对线程和 NSS 模块的支持，并规范了 `nsdispatch` 在标准 C 库中的使用。
