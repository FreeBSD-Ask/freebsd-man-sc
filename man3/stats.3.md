# stats(3)

`stats` — 统计数据收集

## 名称

`stats`

## 库

Lb libstats

## 概要

```c
#include <sys/arb.h>
```

```c
#include <sys/qmath.h>
```

```c
#include <sys/stats.h>
```

### 统计 Blob 模板管理函数

```c
int
stats_tpl_alloc(const char *name, uint32_t flags);

int
stats_tpl_fetch_allocid(const char *name, uint32_t hash);

int
stats_tpl_fetch(int tpl_id, struct statsblob_tpl **tpl);

int
stats_tpl_id2name(uint32_t tpl_id, char *buf, size_t len);

int
stats_tpl_sample_rates(SYSCTL_HANDLER_ARGS);

int
stats_tpl_sample_rollthedice(struct stats_tpl_sample_rate *rates,
    int nrates, void *seed_bytes, size_t seed_len);

struct voistatspec
STATS_VSS_SUM;

struct voistatspec
STATS_VSS_MAX;

struct voistatspec
STATS_VSS_MIN;

struct voistatspec
STATS_VSS_CRHIST<32|64>_LIN(lb, ub, stepinc, vsdflags);

struct voistatspec
STATS_VSS_CRHIST<32|64>_EXP(lb, ub, stepbase, stepexp, vsdflags);

struct voistatspec
STATS_VSS_CRHIST<32|64>_LINEXP(lb, ub, nlinsteps, stepbase, vsdflags);

struct voistatspec
STATS_VSS_CRHIST<32|64>_USR(**HBKTS**(**CRBKT**(*lb*), ...*), vsdflags);

struct voistatspec
STATS_VSS_DRHIST<32|64>_USR(**HBKTS**(**DRBKT**(*lb, ub*), ...*), vsdflags);

struct voistatspec
STATS_VSS_DVHIST<32|64>_USR(**HBKTS**(**DVBKT**(*val*), ...*), vsdflags);

struct voistatspec
STATS_VSS_TDGSTCLUST<32|64>(nctroids, prec);

int
stats_tpl_add_voistats(uint32_t tpl_id, int32_t voi_id,
    const char *voi_name, enum vsd_dtype voi_dtype,
    uint32_t nvss, struct voistatspec *vss, uint32_t flags);
```

### 统计 Blob 数据收集函数

```c
int
stats_voi_update_<abs|rel>_<dtype>(struct statsblob *sb,
    int32_t voi_id, <dtype> voival);
```

### 统计 Blob 实用函数

```c
struct statsblob *
stats_blob_alloc(uint32_t tpl_id, uint32_t flags);

int
stats_blob_init(struct statsblob *sb, uint32_t tpl_id, uint32_t flags);

int
stats_blob_clone(struct statsblob **dst, size_t dstmaxsz,
    struct statsblob *src, uint32_t flags);

void
stats_blob_destroy(struct statsblob *sb);

int
stats_voistat_fetch_dptr(struct statsblob *sb, int32_t voi_id,
    enum voi_stype stype, enum vsd_dtype *retdtype,
    struct voistatdata **retvsd, size_t *retvsdsz);

int
stats_voistat_fetch_<dtype>(struct statsblob *sb, int32_t voi_id,
    enum voi_stype stype, <dtype> *ret);

int
stats_blob_snapshot(struct statsblob **dst, size_t dstmaxsz,
    struct statsblob *src, uint32_t flags);

int
stats_blob_tostr(struct statsblob *sb, struct sbuf *buf,
    enum sb_str_fmt fmt, uint32_t flags);

int
stats_voistatdata_tostr(const struct voistatdata *vsd,
    enum vsd_dtype dtype, enum sb_str_fmt fmt,
    struct sbuf *buf, int objdump);

typedef int
(*stats_blob_visitcb_t)(struct sb_visit *sbv, void *usrctx);

int
stats_blob_visit(struct statsblob *sb, stats_blob_visitcb_t func,
    void *usrctx);
```

## 描述

`stats` 框架便于进行实时的内核和用户空间统计数据收集。该框架围绕"statsblob"构建，这是一个嵌入在连续内存分配中的对象，对消费者几乎不透明，并存储所有需要的状态。"statsblob"对象可以直接或通过指针间接嵌入到其他对象中。

需要收集统计数据的对象或子系统从模板"statsblob"初始化，该模板充当任意一组感兴趣变量（VOI）及其相关统计信息的蓝图。每个模板定义一个模式和相关元数据，二者分开存放以最小化 blob 的内存占用。

在感兴趣的代码库中适当位置添加的数据收集钩子函数将 VOI 数据送入框架进行处理。

每个"statsblob"由 `struct statsblob` 头和不透明的内部 blob 结构组成，如下图所示：

```
---------------------------------------------------------
|   struct  |		       uint8_t			|
| statsblob |		      opaque[]			|
---------------------------------------------------------
```

公开可见的 8 字节头定义为：

```c
struct statsblob {
	uint8_t		abi;
	uint8_t		endian;
	uint16_t	flags;
	uint16_t	maxsz;
	uint16_t	cursz;
	uint8_t		opaque[];
};
```

`abi` 指定 blob 的 `opaque` 内部结构遵循哪个 API 版本（`STATS_ABI_V1` 是目前唯一定义的版本）。`endian` 指定 blob 各字段的字节序（`SB_LE` 表示小端，`SB_BE` 表示大端，`SB_UE` 表示未知字节序）。`cursz` 指定 blob 的大小，而 `maxsz` 指定嵌入 blob 的底层内存分配大小。`cursz` 和 `maxsz` 默认以字节为单位，除非 `flags` 中设置了指定其他单位的标志。

模板通过将任意 VOI ID 与一组统计信息关联来构造，其中每个统计信息使用 `struct voistatspec` 指定，定义如下：

```c
struct voistatspec {
	vss_hlpr_fn		hlpr;
	struct vss_hlpr_info	*hlprinfo;
	struct voistatdata	*iv;
	size_t			vsdsz;
	uint32_t		flags;
	enum vsd_dtype		vs_dtype : 8;
	enum voi_stype		stype : 8;
};
```

通常预期消费者不会直接使用 `struct voistatspec`，而是使用 `STATS_VSS_*` 辅助宏。

`stats` 框架提供以下可与 VOI 关联的统计信息：

**`VS_STYPE_SUM`** VOI 值的总和。

**`VS_STYPE_MAX`** VOI 值的最大值。

**`VS_STYPE_MIN`** VOI 值的最小值。

**`VS_STYPE_HIST`** VOI 值的静态桶直方图，包括不匹配任何桶的"带外/桶外"值的计数。直方图可以指定为"*连*续范围"（CRHIST）、"*离*散范围"（DRHIST）或"*离*散*值*"（DVHIST），根据 VOI 语义使用 32 或 64 位桶计数器。

**`VS_STYPE_TDGST`** 基于 t-digest 方法的 VOI 值动态桶直方图（参见下文参见部分中的 t-digest 论文）

采用类似"访问者软件设计模式"的方案，便于迭代 blob 的数据而无需关心 blob 的结构。提供给访问者回调函数的数据封装在 `struct sb_visit` 中，定义如下：

```c
struct sb_visit {
	struct voistatdata	*vs_data;
	uint32_t		tplhash;
	uint32_t		flags;
	int16_t			voi_id;
	int16_t			vs_dsz;
	enum vsd_dtype		voi_dtype : 8;
	enum vsd_dtype		vs_dtype : 8;
	int8_t			vs_stype;
	uint16_t		vs_errs;
};
```

`stats_tpl_sample_rates()` 和 `stats_tpl_sample_rollthedice()` 函数利用 `struct stats_tpl_sample_rate` 封装每个模板的采样率信息，定义如下：

```c
struct stats_tpl_sample_rate {
	int32_t		tpl_slot_id;
	uint32_t	tpl_sample_pct;
};
```

`tpl_slot_id` 成员保存从 `stats_tpl_alloc()` 或 `stats_tpl_fetch_allocid()` 获取的模板槽 ID。`tpl_sample_pct` 成员保存模板的采样率，作为 [0, 100] 范围内的整数百分比。

`stats_tpl_sample_rates()` 作为 `arg1` 所需的符合 `stats_tpl_sr_cb_t` 的函数指针定义为：

```c
enum stats_tpl_sr_cb_action {
	TPL_SR_UNLOCKED_GET,
	TPL_SR_RLOCKED_GET,
	TPL_SR_RUNLOCK,
	TPL_SR_PUT
};
typedef int (*stats_tpl_sr_cb_t)(enum stats_tpl_sr_cb_action action,
    struct stats_tpl_sample_rate **rates, int *nrates, void *ctx);
```

符合要求的函数必须：

- 出错时返回适当的 errno(2)，否则返回 0。
- 当以 "action == TPL_SR_*_GET" 调用时，返回子系统的速率列表指针和计数，按要求加锁或解锁。
- 当以 "action == TPL_SR_RUNLOCK" 调用时，解锁子系统的速率列表指针和计数。与先前的 "action == TPL_SR_RLOCKED_GET" 调用配对使用。
- 当以 "action == TPL_SR_PUT" 调用时，将子系统的速率列表指针和计数更新为 sysctl 处理后的值，并在 `rates` 和 `nrates` 中返回非活动列表详情，供 `stats_tpl_sample_rates()` 进行垃圾回收。

当需要通过文本方式引用模板时（例如通过 MIB 变量），可以使用以下基于字符串的模板规范格式：

- "<tplname>" :<tplhash> ，例如 "TCP_DEFAULT" :1731235399
- "<tplname>" ，例如 "TCP_DEFAULT"
- :<tplhash> ，例如 :1731235399

第一种形式是框架生成的规范规范格式，而第二种和第三种形式主要是为用户输入提供的便利格式。模板名称两端的引号是可选的。

### MIB 变量

内核中的 `stats` 框架在 sysctl(3) MIB 的 `kern.stats` 分支中暴露以下框架特定的变量：

**templates** 以规范模板规范形式注册的模板的只读 CSV 列表。

### 模板管理函数

`stats_tpl_alloc()` 函数分配一个具有指定唯一名称的新模板，并返回其运行时稳定的模板槽 ID 以供其他 API 函数使用。`flags` 参数目前未使用。

`stats_tpl_fetch_allocid()` 函数返回任何与指定名称和哈希匹配的已注册模板的运行时稳定模板槽 ID。

`stats_tpl_fetch()` 函数返回指定模板槽 ID 处已注册模板对象的指针。

`stats_tpl_id2name()` 函数返回指定模板槽 ID 处已注册模板对象的名称。

`stats_tpl_sample_rates()` 函数提供通过 sysctl(3) MIB 变量进行模板采样率管理和报告的通用处理器。子系统可以使用此函数创建管理并报告子系统特定模板采样率的子系统特定 SYSCTL_PROC(9) MIB 变量。子系统必须提供符合 `stats_tpl_sr_cb_t` 的函数指针作为 sysctl 的 `arg1`，这是一个用于与子系统统计模板采样率列表交互的回调。子系统可以选择将 sysctl 的 `arg2` 指定为非零值，这会导致在堆上分配 arg2 大小的零初始化上下文内存，并在 `stats_tpl_sample_rates()` 操作期间传递给所有子系统回调。

`stats_tpl_sample_rollthedice()` 函数从提供的模板采样率数组中按权重随机选择模板。所有采样率的累积百分比不应超过 100。如果未提供种子，则使用 PRNG 生成真正的随机数，使每次选择独立。如果提供了种子，则在不同种子间随机选择，但对于相同种子是确定性的。

`stats_tpl_add_voistats()` 函数用于向指定模板槽 ID 处的已注册模板对象添加 VOI 和相关统计信息集合。统计信息集合作为 `struct voistatspec` 数组传递，可使用 `STATS_VSS_*` 辅助宏初始化，或对于非标准用例手动初始化。对于静态 `vss` 数组，可以通过将 `vss` 传递给 `NVSS` 宏来确定数组元素的 `nvss` 计数。可以传递 `SB_VOI_RELUPDATE` 标志来配置 VOI 以便与 `stats_voi_update_rel_<dtype>()` 一起使用，这需要在每次更新时在 blob 中维护额外的 8 字节状态。

### 数据收集函数

`stats_voi_update_abs_<dtype>()` 和 `stats_voi_update_rel_<dtype>()` 函数都更新与 `voi_id` 标识的 VOI 关联的所有统计信息。"abs" 调用将 `voival` 用作绝对值，而 "rel" 调用将 `voival` 用作相对于上一次更新函数调用的值，方法是将其加到先前值并使用结果进行更新。只有在使用 `SB_VOI_RELUPDATE` 标志向 `stats_tpl_add_voistats()` 添加到模板的 VOI 才能进行相对更新。

### 实用函数

`stats_blob_alloc()` 函数基于指定模板槽 ID 处的已注册模板对象分配并初始化新 blob。

`stats_blob_init()` 函数基于指定模板槽 ID 处的已注册模板对象在现有内存分配中初始化新 blob。

`stats_blob_clone()` 函数将 `src` blob 复制到 `dst`，仅保持 `dst` 的 `maxsz` 字段不变。可以传递 `SB_CLONE_ALLOCDST` 标志以指示函数分配适当大小的新 blob 来复制 `src`，将新指针存储在 `*dst` 中。可以设置 `SB_CLONE_USRDSTNOFAULT` 或 `SB_CLONE_USRDST` 标志，分别表示应使用 copyout_nofault(9) 或 copyout(9)，因为 `*dst` 是用户空间地址。

`stats_blob_snapshot()` 函数调用 `stats_blob_clone()` 获取 `src` 的副本，然后执行生成一致 blob 快照所需的任何附加功能。`stats_blob_clone()` 解释的标志也适用于 `stats_blob_snapshot()`。此外，`SB_CLONE_RSTSRC` 标志可用于在成功获取快照后重置 `src` blob 的统计信息。

`stats_blob_destroy()` 函数销毁先前由 `stats_blob_alloc()`、`stats_blob_clone()` 或 `stats_blob_snapshot()` 创建的 blob。

`stats_blob_visit()` 函数允许调用者迭代 blob 的内容。回调函数 `func` 为 blob 中的每个 VOI 和统计信息调用，将 `struct sb_visit` 和用户上下文参数 `usrctx` 传递给回调函数。传递给回调函数的 `sbv` 可能在 `flags` 结构成员中设置一个或多个以下标志，以提供有关迭代的有用元数据：`SB_IT_FIRST_CB`、`SB_IT_LAST_CB`、`SB_IT_FIRST_VOI`、`SB_IT_LAST_VOI`、`SB_IT_FIRST_VOISTAT`、`SB_IT_LAST_VOISTAT`、`SB_IT_NULLVOI` 和 `SB_IT_NULLVOISTAT`。从回调函数返回非零值会终止迭代。

`stats_blob_tostr()` 将 blob 的字符串表示渲染到 [sbuf(9)](../man9/sbuf.9.md) `buf` 中。目前支持的渲染格式为 `SB_STRFMT_FREEFORM` 和 `SB_STRFMT_JSON`。可以传递 `SB_TOSTR_OBJDUMP` 标志以渲染版本特定的不透明实现细节，用于调试或字符串到二进制 blob 重构目的。可以传递 `SB_TOSTR_META` 标志以将模板元数据渲染到字符串表示中，使用 blob 的模板哈希查找对应模板。

`stats_voistatdata_tostr()` 将单个统计信息数据的字符串表示渲染到 [sbuf(9)](../man9/sbuf.9.md) `buf` 中。可以指定 `stats_blob_tostr()` 函数支持的相同渲染格式，`objdump` 布尔值的含义与 `SB_TOSTR_OBJDUMP` 标志相同。

`stats_voistat_fetch_dptr()` 函数返回指向 VOI `voi_id` 指定 `stype` 统计信息数据的内部 blob 指针。`stats_voistat_fetch_<dtype>()` 函数是 `stats_voistat_fetch_dptr()` 的便利包装器，用于执行简单数据类型的提取。

## 实现说明

以下说明适用于 STATS_ABI_V1 格式的 statsblob。

### 时空复杂度

Blob 按照头之后的三个不同内存区域布局：

```
------------------------------------------------------
|   struct    | struct |   struct   |     struct     |
| statsblobv1 | voi [] | voistat [] | voistatdata [] |
------------------------------------------------------
```

Blob 将 VOI 和统计信息 blob 状态（`struct voi` 8 字节和 `struct voistat` 8 字节）存储在稀疏数组中，使用 `voi_id` 和 `enum voi_stype` 作为数组索引。这允许 O(1) 访问 blob 中的任何 voi/voistat 对，代价是对于未指定连续编号 VOI 和/或统计类型的模板，每个空槽浪费 8 字节内存。仅为非空槽对分配统计信息的数据存储。

为提供具体示例，具有以下规范的 blob：

- 两个 VOI；ID 为 0 和 2；按该顺序添加到模板
- VOI 0 的数据类型为 `int64_t`，配置了 `SB_VOI_RELUPDATE` 以启用使用 `stats_voi_update_rel_<dtype>()` 的相对更新支持，并关联了 `VS_STYPE_MIN` 统计信息。
- VOI 2 的数据类型为 `uint32_t`，关联了 `VS_STYPE_SUM` 和 `VS_STYPE_MAX` 统计信息。

将具有以下内存布局：

```
--------------------------------------
| header			     | struct statsblobv1, 32 bytes
|------------------------------------|
| voi[0]			     | struct voi, 8 bytes
| voi[1] (vacant)		     | struct voi, 8 bytes
| voi[2]			     | struct voi, 8 bytes
|------------------------------------|
| voi[2]voistat[VOISTATE] (vacant)   | struct voistat, 8 bytes
| voi[2]voistat[SUM]		     | struct voistat, 8 bytes
| voi[2]voistat[MAX]		     | struct voistat, 8 bytes
| voi[0]voistat[VOISTATE]	     | struct voistat, 8 bytes
| voi[0]voistat[SUM] (vacant)	     | struct voistat, 8 bytes
| voi[0]voistat[MAX] (vacant)	     | struct voistat, 8 bytes
| voi[0]voistat[MIN]		     | struct voistat, 8 bytes
|------------------------------------|
| voi[2]voistat[SUM]voistatdata      | struct voistatdata_int32, 4 bytes
| voi[2]voistat[MAX]voistatdata      | struct voistatdata_int32, 4 bytes
| voi[0]voistat[VOISTATE]voistatdata | struct voistatdata_numeric, 8 bytes
| voi[0]voistat[MIN]voistatdata      | struct voistatdata_int64, 8 bytes
--------------------------------------
				       TOTAL 136 bytes
```

当使用 `stats_blob_tostr()`、`SB_STRFMT_FREEFORM` `fmt` 和 `SB_TOSTR_OBJDUMP` 标志渲染为字符串格式时，渲染输出为：

```
struct statsblobv1@0x8016250a0, abi=1, endian=1, maxsz=136, cursz=136, \
  created=6294158585626144, lastrst=6294158585626144, flags=0x0000, \
  stats_off=56, statsdata_off=112, tplhash=2994056564
    vois[0]: id=0, name="", flags=0x0001, dtype=INT_S64, voistatmaxid=3, \
      stats_off=80
        vois[0]stat[0]: stype=VOISTATE, flags=0x0000, dtype=VOISTATE, \
          dsz=8, data_off=120
            voistatdata: prev=0
        vois[0]stat[1]: stype=-1
        vois[0]stat[2]: stype=-1
        vois[0]stat[3]: stype=MIN, flags=0x0000, dtype=INT_S64, \
          dsz=8, data_off=128
            voistatdata: 9223372036854775807
    vois[1]: id=-1
    vois[2]: id=2, name="", flags=0x0000, dtype=INT_U32, voistatmaxid=2, \
      stats_off=56
        vois[2]stat[0]: stype=-1
        vois[2]stat[1]: stype=SUM, flags=0x0000, dtype=INT_U32, dsz=4, \
          data_off=112
            voistatdata: 0
        vois[2]stat[2]: stype=MAX, flags=0x0000, dtype=INT_U32, dsz=4, \
          data_off=116
            voistatdata: 0
```

注意：上面渲染输出中的 "\n" 表示为使手册页保持在 80 列以内而手动插入的换行符，并非实际输出的一部分。

### 锁

`stats` 框架不在单个 blob 级别提供任何并发保护，而是要求消费者在调用引用非模板 blob 的 API 函数时保证互斥。

模板列表在内核中使用 [rwlock(9)](../man9/rwlock.9.md) 保护，在用户空间使用 [pthread(3)](pthread.3.md) rw 锁保护，以支持模板管理和 blob 初始化操作之间的并发。

## 返回值

`stats_tpl_alloc()` 成功时返回运行时稳定的模板槽 ID，失败时返回负 errno。如果检测到参数有任何问题，返回 -EINVAL。如果已有同名的模板注册，返回 -EEXIST。如果所需的内存分配失败，返回 -ENOMEM。

`stats_tpl_fetch_allocid()` 返回运行时稳定的模板槽 ID，或失败时返回负 errno。如果没有注册的模板匹配指定的名称和/或哈希，返回 -ESRCH。

`stats_tpl_fetch()` 成功时返回 0，如果指定了无效的 `tpl_id` 则返回 ENOENT。

`stats_tpl_id2name()` 成功时返回 0，或失败时返回 errno。如果 `len` 指定的 `buf` 长度太短无法容纳模板名称，返回 EOVERFLOW。如果指定了无效的 `tpl_id`，返回 ENOENT。

`stats_tpl_sample_rollthedice()` 返回从 `rates` 中选择的有效模板槽 ID，如果进行了 NULL 选择（即本次掷骰不收集统计信息），则返回 -1。

`stats_tpl_add_voistats()` 成功时返回 0，或失败时返回 errno。如果检测到参数有任何问题，返回 EINVAL。如果生成的 blob 会超过最大大小，返回 EFBIG。如果尝试向先前已配置的 VOI 添加更多 VOI 统计信息，返回 EOPNOTSUPP。如果所需的内存分配失败，返回 ENOMEM。

`stats_voi_update_abs_<dtype>()` 和 `stats_voi_update_rel_<dtype>()` 成功时返回 0，如果检测到参数有任何问题，返回 EINVAL。

`stats_blob_init()` 成功时返回 0，或失败时返回 errno。如果检测到参数有任何问题，返回 EINVAL。如果模板 blob 的 `cursz` 大于正在初始化的 blob 的 `maxsz`，返回 EOVERFLOW。

`stats_blob_alloc()` 返回指向基于指定模板（槽 ID 为 `tpl_id`）新分配并初始化的 blob 的指针，如果内存分配失败则返回 NULL。

`stats_blob_clone()` 和 `stats_blob_snapshot()` 成功时返回 0，或失败时返回 errno。如果检测到参数有任何问题，返回 EINVAL。如果指定了 SB_CLONE_ALLOCDST 标志但 `dst` 的内存分配失败，返回 ENOMEM。如果 src blob 的 `cursz` 大于 `dst` blob 的 `maxsz`，返回 EOVERFLOW。

`stats_blob_visit()` 成功时返回 0，如果检测到参数有任何问题，返回 EINVAL。

`stats_blob_tostr()` 和 `stats_voistatdata_tostr()` 成功时返回 0，或失败时返回 errno。如果检测到参数有任何问题，返回 EINVAL，否则返回 `sbuf_error()` 为 `buf` 返回的任何错误。

`stats_voistat_fetch_dptr()` 成功时返回 0，如果检测到参数有任何问题，返回 EINVAL。

`stats_voistat_fetch_<dtype>()` 成功时返回 0，或失败时返回 errno。如果检测到参数有任何问题，返回 EINVAL。如果请求的数据类型与 blob 中指定 `voi_id` 和 `stype` 的数据类型不匹配，返回 EFTYPE。

## 参见

errno(2), [arb(3)](arb.3.md), [qmath(3)](qmath.3.md), [tcp(4)](../man4/tcp.4.md), [sbuf(9)](../man9/sbuf.9.md)

> Ted Dunning, Otmar Ertl, "Computing Extremely Accurate Quantiles Using t-digests"。

## 历史

`stats` 框架首次出现于 FreeBSD 13.0。

## 作者

`stats` 框架和本手册页由 Lawrence Stewart <lstewart@FreeBSD.org> 编写，由 Netflix, Inc. 赞助。

## 注意事项

依赖时序的网络统计信息（特别是 TCP_RTT）的粒度取决于 `HZ` 定时器。为最小化测量误差，避免使用低于 1000 的 HZ。
