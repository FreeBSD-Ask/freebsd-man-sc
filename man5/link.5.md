# link.5

`link` — 动态加载器与链接编辑器接口

## 名称

`link`

## 概要

`#include <sys/types.h>`

`#include <nlist.h>`

`#include <link.h>`

## 描述

头文件

`#include <link.h>`

声明了若干存在于动态链接程序和库中的结构。这些结构定义了链接编辑器和加载器机制中若干组件之间的接口。其中许多结构在二进制文件中的布局在很多地方类似于 a.out 格式，因为它们承担的功能与符号定义（包括附带的字符串表）以及解析外部实体引用所需的重定位记录类似。它还记录了一些动态加载和链接过程所独有的数据结构。这些包括对完成链接编辑过程所需的其他对象的引用，以及用于促进 *位置无关代码*（Position Independent Code，简称 PIC）的间接表，以改善不同进程之间代码页的共享。此处描述的数据结构集合将被称为 *运行时重定位节（Run-time Relocation Section，RRS）*，并嵌入在动态链接程序或共享对象映像的标准文本段和数据段中，因为现有的 [a.out(5)](a.out.5.md) 格式在其他地方没有为它留出空间。

若干工具协同工作，以确保准备程序运行的任务能够以优化系统资源使用的方式成功完成。编译器发出 PIC 代码，[ld(1)](../man1/ld.1.md) 可由此构建共享库。编译器还通过 `.size` 汇编指令包含任何已初始化数据项的大小信息。PIC 代码与常规代码的不同之处在于，它通过一个间接表（全局偏移表，Global Offset Table）访问数据变量，该表按约定可通过保留名 `_GLOBAL_OFFSET_TABLE_` 访问。用于此目的的确切机制取决于机器，通常会为此保留一个机器寄存器。这种构造背后的原理是生成独立于实际加载地址的代码。只有全局偏移表中包含的值可能需要在运行时根据地址空间中各共享对象的加载地址进行更新。

类似地，对全局定义函数的过程调用通过位于核心映像数据段中的过程链接表（Procedure Linkage Table，PLT）进行重定向。同样，这是为了避免对文本段进行运行时修改。

链接编辑器在将 PIC 目标文件组合为适合映射到进程地址空间的映像时，分配全局偏移表和过程链接表。它还收集运行时链接编辑器可能需要的所有符号，并将这些符号与映像的文本和数据位一起存储。另一个保留符号 *_DYNAMIC* 用于指示运行时链接器结构的存在。只要 _DYNAMIC 被重定位为 0，就无需调用运行时链接编辑器。如果该符号非零，它指向一个数据结构，从中可以推导出必要重定位和符号信息的位置。这一点最值得注意的是由启动模块 *crt0* 使用的。_DYNAMIC 结构按约定位于其所属映像数据段的开头。

## 数据结构

支持动态链接和运行时重定位的数据结构既位于其适用的映像的文本段，也位于数据段。文本段包含只读数据，例如符号描述和名称，而数据段包含需要在重定位过程中修改的表。

_DYNAMIC 符号引用一个 `_dynamic` 结构：

```sh
struct	_dynamic {
	int	d_version;
	struct 	so_debug *d_debug;
	union {
		struct section_dispatch_table *d_sdt;
	} d_un;
	struct  ld_entry *d_entry;
};
```

**`d_version`** 该字段用于区分动态链接实现的不同版本。当前 [ld(1)](../man1/ld.1.md) 和 ld.so(1) 能理解的版本号有 *LD_VERSION_SUN (3)*（由 SunOS 4.x 发行版使用）和 *LD_VERSION_BSD (8)*（自 FreeBSD 1.1 起使用）。

**`d_un`** 引用一个依赖于 *d_version* 的数据结构。

**`so_debug`** 该字段为调试器提供了一种钩子，用于访问由于运行时链接编辑器的操作而加载的共享对象的符号表。

`section_dispatch_table` 结构是主要的“分派”表，包含映像各段中各种符号和重定位信息所在位置的偏移量。

```sh
struct section_dispatch_table {
	struct	so_map *sdt_loaded;
	long	sdt_sods;
	long	sdt_filler1;
	long	sdt_got;
	long	sdt_plt;
	long	sdt_rel;
	long	sdt_hash;
	long	sdt_nzlist;
	long	sdt_filler2;
	long	sdt_buckets;
	long	sdt_strings;
	long	sdt_str_sz;
	long	sdt_text_sz;
	long	sdt_plt_sz;
};
```

**`sdt_loaded`** 指向第一个加载的链接映射（见下文）。此字段由 `ld.so` 设置。

**`sdt_sods`** *此* 对象所需的共享对象描述符（链）表的起始位置。

**`sdt_filler1`** 已弃用（SunOS 用于指定库搜索规则）。

**`sdt_got`** 本映像内全局偏移表的位置。

**`sdt_plt`** 本映像内过程链接表的位置。

**`sdt_rel`** 一个 `relocation_info` 结构数组的位置（见 [a.out(5)](a.out.5.md)），指定运行时重定位。

**`sdt_hash`** 用于在此对象符号表中进行快速符号查找的哈希表的位置。

**`sdt_nzlist`** 符号表的位置。

**`sdt_filler2`** 当前未使用。

**`sdt_buckets`** `sdt_hash` 中的桶数。

**`sdt_strings`** 与 `sdt_nzlist` 配套的符号字符串表的位置。

**`sdt_str_sz`** 字符串表的大小。

**`sdt_text_sz`** 对象文本段的大小。

**`sdt_plt_sz`** 过程链接表的大小。

`sod` 结构描述为完成包含它的对象的链接编辑过程所需的共享对象。此类对象的列表（通过 `sod_next` 链接）由 section_dispatch_table 结构中的 `sdt_sods` 指向。

```sh
struct sod {
	long	sod_name;
	u_int	sod_library : 1,
		sod_reserved : 31;
	short	sod_major;
	short	sod_minor;
	long	sod_next;
};
```

**`sod_name`** 文本段中描述此链接对象的字符串的偏移量。

**`sod_library`** 如果设置，`sod_name` 指定一个由 `ld.so` 搜索的库。通过在一组目录中搜索与 *lib<sod_name>.so.n.m* 匹配的共享对象来获得路径名（另见 ldconfig(8)）。如果未设置，`sod_name` 应指向所需共享对象的完整路径名。

**`sod_major`** 指定要加载的共享对象的主版本号。

**`sod_minor`** 指定要加载的共享对象的首选次版本号。

运行时链接编辑器维护一个称为 *链接映射* 的结构列表，以跟踪加载到进程地址空间中的所有共享对象。这些结构仅在运行时使用，不出现在可执行文件或共享库的文本段或数据段中。

```sh
struct so_map {
	caddr_t	som_addr;
	char 	*som_path;
	struct	so_map *som_next;
	struct	sod *som_sod;
	caddr_t som_sodbase;
	u_int	som_write : 1;
	struct	_dynamic *som_dynamic;
	caddr_t	som_spd;
};
```

**`som_addr`** 与此链接映射关联的共享对象的加载地址。

**`som_path`** 加载对象的完整路径名。

**`som_next`** 指向下一条链接映射的指针。

**`som_sod`** 负责加载此共享对象的 `sod` 结构。

**`som_sodbase`** 在运行时链接器的后续版本中已弃用。

**`som_write`** 如果此对象的文本段（某些部分）当前可写，则设置。

**`som_dynamic`** 指向此对象 `_dynamic` 结构的指针。

**`som_spd`** 用于附加运行时链接编辑器维护的私有数据的钩子。

带大小的符号描述。这只是一个 `nlist` 结构，增加了一个字段（`nz_size`）。用于传达共享对象数据段中各项的大小信息。这些结构的数组位于共享对象的文本段中，通过 `section_dispatch_table` 的 `sdt_nzlist` 字段寻址。

```sh
struct nzlist {
	struct nlist	nlist;
	u_long		nz_size;
#define nz_un		nlist.n_un
#define nz_strx		nlist.n_un.n_strx
#define nz_name		nlist.n_un.n_name
#define nz_type		nlist.n_type
#define nz_value	nlist.n_value
#define nz_desc		nlist.n_desc
#define nz_other	nlist.n_other
};
```

**`nlist`** 见 nlist(3)。

**`nz_size`** 此符号表示的数据的大小。

共享对象的文本段中包含一个哈希表，以便在运行时链接编辑期间快速查找符号。`section_dispatch_table` 结构的 `sdt_hash` 字段指向一个 `rrs_hash` 结构数组：

```sh
struct rrs_hash {
	int	rh_symbolnum;		/* 符号编号 */
	int	rh_next;		/* 下一个哈希条目 */
};
```

**`rh_symbolnum`** 符号在共享对象符号表中的索引（由 `ld_symbols` 字段给出）。

**`rh_next`** 发生冲突时，此字段是本哈希表桶中下一个条目的偏移量。对于桶中最后一个元素，该值为零。

`rt_symbol` 结构用于跟踪运行时分配的公共符号和从共享对象复制的数据项。这些项保存在链表上，并通过 `so_debug` 结构中的 `dd_cc` 字段（见下文）导出，供调试器使用。

```sh
struct rt_symbol {
	struct nzlist		*rt_sp;
	struct rt_symbol	*rt_next;
	struct rt_symbol	*rt_link;
	caddr_t			rt_srcaddr;
	struct so_map		*rt_smp;
};
```

**`rt_sp`** 符号描述。

**`rt_next`** 下一个 rt_symbol 的虚拟地址。

**`rt_link`** 哈希桶中的下一个。由 `ld.so` 内部使用。

**`rt_srcaddr`** 共享对象内已初始化数据源的位置。

**`rt_smp`** 作为此运行时符号所描述数据的原始来源的共享对象。

`so_debug` 结构供调试器了解由于运行时链接编辑而加载到进程地址空间中的任何共享对象。由于运行时链接编辑器作为进程初始化的一部分运行，希望从共享对象访问符号的调试器只能在链接编辑器从 crt0 被调用之后才能这样做。动态链接的二进制文件包含一个 `so_debug` 结构，可通过 `_dynamic` 中的 `d_debug` 字段定位。

```sh
struct 	so_debug {
	int	dd_version;
	int	dd_in_debugger;
	int	dd_sym_loaded;
	char    *dd_bpt_addr;
	int	dd_bpt_shadow;
	struct rt_symbol *dd_cc;
};
```

**`dd_version`** 此接口的版本号。

**`dd_in_debugger`** 由调试器设置，向运行时链接器指示程序在调试器的控制下运行。

**`dd_sym_loaded`** 每当运行时链接器通过加载共享对象添加符号时设置。

**`dd_bpt_addr`** 运行时链接器将设置断点的地址，以便将控制权转交给调试器。该地址由启动模块 `crt0.o` 确定，位于调用 _main 之前的某个方便位置。

**`dd_bpt_shadow`** 包含 `dd_bpt_addr` 处的原始指令。调试器应在继续执行程序之前将该指令恢复。

**`dd_cc`** 指向调试器可能感兴趣的运行时分配符号链表的指针。

*ld_entry* 结构定义了 `ld.so` 中的一组服务例程。

```sh
struct ld_entry {
	void	*(*dlopen)(char *, int);
	int	(*dlclose)(void *);
	void	*(*dlsym)(void *, char *);
	char	*(*dlerror)(void);
};
```

`crt_ldso` 结构定义了 crt0 中的启动代码与 `ld.so` 之间的接口。

```sh
struct crt_ldso {
	int		crt_ba;
	int		crt_dzfd;
	int		crt_ldfd;
	struct _dynamic	*crt_dp;
	char		**crt_ep;
	caddr_t		crt_bp;
	char		*crt_prog;
	char		*crt_ldso;
	struct ld_entry	*crt_ldentry;
};
#define CRT_VERSION_SUN		1
#define CRT_VERSION_BSD_2	2
#define CRT_VERSION_BSD_3	3
#define	CRT_VERSION_BSD_4	4
```

**`crt_ba`** crt0 加载 `ld.so` 的虚拟地址。

**`crt_dzfd`** 在 SunOS 系统上，此字段包含一个指向 **/dev/zero** 的打开文件描述符，用于获取按需调页的清零页面。在 FreeBSD 系统上，它包含 -1。

**`crt_ldfd`** 包含 crt0 用于加载 `ld.so` 的打开文件描述符。

**`crt_dp`** 指向 main 的 `_dynamic` 结构的指针。

**`crt_ep`** 指向环境字符串的指针。

**`crt_bp`** 如果主程序由调试器运行，运行时链接器将放置断点的地址。见 `so_debug`。

**`crt_prog`** 由 crt0 确定的主程序名（仅 CRT_VERSION_BSD3）。

**`crt_ldso`** 由 crt0 映射的运行时链接器路径（仅 CRT_VERSION_BSD4）。

`hints_header` 和 `hints_bucket` 结构定义了库提示的布局，通常位于 “**/var/run/ld.so.hints**” 中，`ld.so` 使用它来快速定位文件系统中的共享对象映像。提示文件的组织方式与 “a.out” 目标文件类似，它包含一个头部，确定固定大小的哈希桶表和公共字符串池的偏移量和大小。

```sh
struct hints_header {
	long		hh_magic;
#define HH_MAGIC	011421044151
	long		hh_version;
#define LD_HINTS_VERSION_1	1
	long		hh_hashtab;
	long		hh_nbucket;
	long		hh_strtab;
	long		hh_strtab_sz;
	long		hh_ehints;
};
```

**`hh_magic`** 提示文件的魔数。

**`hh_version`** 接口版本号。

**`hh_hashtab`** 哈希表的偏移量。

**`hh_strtab`** 字符串表的偏移量。

**`hh_strtab_sz`** 字符串的大小。

**`hh_ehints`** 提示文件中可使用的最大偏移量。

```sh
/*
 * 提示文件中的哈希表元素。
 */
struct hints_bucket {
	int		hi_namex;
	int		hi_pathx;
	int		hi_dewey[MAXDEWEY];
	int		hi_ndewey;
#define hi_major hi_dewey[0]
#define hi_minor hi_dewey[1]
	int		hi_next;
};
```

**`hi_namex`** 标识该库的字符串的索引。

**`hi_pathx`** 表示该库完整路径名的字符串的索引。

**`hi_dewey`** 共享库的版本号。

**`hi_ndewey`** `hi_dewey` 中有效条目的数量。

**`hi_next`** 发生哈希冲突时的下一个桶。

## 注意事项

目前只有（GNU）C 编译器支持创建共享库。其他编程语言无法用于此目的。
