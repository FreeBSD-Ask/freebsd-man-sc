# dlinfo(3)

`dlinfo` — 获取有关动态加载对象的信息

## 名称

`dlinfo`

## 库

Lb libc

## 概要

```c
#include <link.h>
#include <dlfcn.h>

int
dlinfo(void * restrict handle, int request, void * restrict p);
```

## 描述

`dlinfo()` 函数提供有关动态加载对象的信息。 `dlinfo()` 所采取的操作以及 `p` 参数的确切含义和类型，取决于调用者提供的 `request` 参数的值。

`handle` 参数要么是 [dlopen(3)](dlopen.3.md) 函数调用返回的值，要么是特殊句柄 `RTLD_SELF`。如果 `handle` 是 [dlopen(3)](dlopen.3.md) 返回的值，则 `dlinfo()` 函数返回的信息属于指定的对象。如果 `handle` 是特殊句柄 `RTLD_SELF`，则返回的信息属于调用者本身。

`request` 参数的可能取值如下：

**`RTLD_DI_LINKMAP`** 检索指定 `handle` 对应的 `Link_map`（`struct link_map`）结构指针。成功返回时， `p` 参数将被填入指向 `Link_map` 结构（`Link_map **p`）的指针，该结构描述了由 `handle` 参数指定的共享对象。 `Link_map` 结构由 ld.so(1) 维护为一个双向链表，其顺序与调用 [dlopen(3)](dlopen.3.md) 和 dlclose(3) 的顺序相同。参见“实例”章节的示例 1。

`Link_map` 结构定义于 `<link.h>`，其成员如下：

```c
caddr_t         l_base;    /* 库的基地址 */
const char      *l_name;   /* 库的绝对路径 */
const void      *l_ld;     /* 指向内存中 .dynamic 的指针 */
struct link_map *l_next,   /* 已映射库的链表 */
                *l_prev;
caddr_t         l_addr;     /* 库的加载偏移 */
const char      *l_refname; /* 该对象所过滤的对象 */
```

**`l_base`** 加载到内存中的对象的基地址。

**`l_name`** 已加载共享对象的全名。

**`l_ld`** 加载到内存中的动态链接信息段（`PT_DYNAMIC`）的地址。

**`l_next`** 链接映射列表中的下一个 `Link_map` 结构。

**`l_prev`** 链接映射列表中的上一个 `Link_map` 结构。

**`l_addr`** 对象的加载偏移，即实际加载地址与对象链接时的基地址之差。

**`l_refname`** 该对象所过滤的对象的名称（如果有的话）。如果存在多个被过滤对象，则提供第一个 `DT_FILTER` 动态项中的名称。

**`RTLD_DI_SERINFO`** 检索与给定 `handle` 参数关联的库搜索路径。 `p` 参数应指向 `Dl_serinfo` 结构缓冲区（`Dl_serinfo *p`）。必须先用 `RTLD_DI_SERINFOSIZE` 请求初始化 `Dl_serinfo` 结构。返回的 `Dl_serinfo` 结构包含 `dls_cnt` 个 `Dl_serpath` 条目。每个条目的 `dlp_name` 字段指向搜索路径。相应的 `dlp_info` 字段包含一个或多个标志，指示路径的来源（参见 `<link.h>` 头文件中定义的 `LA_SER_*` 标志）。用法示例参见“实例”章节的示例 2。

**`RTLD_DI_SERINFOSIZE`** 初始化 `Dl_serinfo` 结构，以供 `RTLD_DI_SERINFO` 请求使用。将返回 `dls_cnt` 和 `dls_size` 两个字段，分别指示适用于该句柄的搜索路径数量，以及容纳 `dls_cnt` 个 `Dl_serpath` 条目和相关搜索路径字符串所需的 `Dl_serinfo` 缓冲区的总大小。用法示例参见“实例”章节的示例 2。

**`RTLD_DI_ORIGIN`** 检索与该句柄关联的动态对象的起源路径。成功返回时， `p` 参数将被填入 `char` 指针（`char *p`）。

## 返回值

`dlinfo()` 函数成功时返回 0，出错时返回 -1。每当检测到错误时，可以通过调用 dlerror(3) 获取描述该错误的详细信息。

## 实例

示例 1：使用 `dlinfo()` 检索 `Link_map` 结构。

以下示例展示动态库如何检测在调用者之后加载的共享库列表。为简洁起见，省略了错误检查。

```c
Link_map *map;

dlinfo(RTLD_SELF, RTLD_DI_LINKMAP, &map);

while (map != NULL) {
        printf("%p: %s\n", map->l_addr, map->l_name);
        map = map->l_next;
}
```

示例 2：使用 `dlinfo()` 检索库搜索路径。

以下示例展示动态对象如何检查用于通过 [dlopen(3)](dlopen.3.md) 定位简单文件名的库搜索路径。为简洁起见，省略了错误检查。

```c
Dl_serinfo       _info, *info = &_info;
Dl_serpath      *path;
unsigned int     cnt;

/* 确定搜索路径数量及所需缓冲区大小 */
dlinfo(RTLD_SELF, RTLD_DI_SERINFOSIZE, (void *)info);

/* 分配新缓冲区并初始化 */
info = malloc(_info.dls_size);
info->dls_size = _info.dls_size;
info->dls_cnt = _info.dls_cnt;

/* 获取搜索路径信息 */
dlinfo(RTLD_SELF, RTLD_DI_SERINFO, (void *)info);

path = &info->dls_serpath[0];

for (cnt = 1; cnt <= info->dls_cnt; cnt++, path++) {
        (void) printf("%2d: %s\n", cnt, path->dls_name);
}
```

## 参见

rtld(1), [dladdr(3)](dladdr.3.md), [dlopen(3)](dlopen.3.md), dlsym(3)

## 历史

`dlinfo()` 函数首次出现在 Solaris 操作系统中。在 FreeBSD 中，它首次出现在 FreeBSD 4.8。

## 作者

FreeBSD 版本的 `dlinfo()` 函数最初由 Alexey Zelkin <phantom@FreeBSD.org> 编写，后由 Alexander Kabaev <kan@FreeBSD.org> 扩展和改进。

该函数的手册页由 Alexey Zelkin <phantom@FreeBSD.org> 编写。
