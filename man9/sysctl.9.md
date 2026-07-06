# sysctl.9

`SYSCTL_DECL` — 动态和静态 sysctl MIB 创建函数

## 名称

`SYSCTL_DECL`, `SYSCTL_ADD_BOOL`, `SYSCTL_ADD_COUNTER_U64`, `SYSCTL_ADD_COUNTER_U64_ARRAY`, `SYSCTL_ADD_INT`, `SYSCTL_ADD_LONG`, `SYSCTL_ADD_NODE`, `SYSCTL_ADD_NODE_WITH_LABEL`, `SYSCTL_ADD_OPAQUE`, `SYSCTL_ADD_PROC`, `SYSCTL_ADD_QUAD`, `SYSCTL_ADD_ROOT_NODE`, `SYSCTL_ADD_S8`, `SYSCTL_ADD_S16`, `SYSCTL_ADD_S32`, `SYSCTL_ADD_S64`, `SYSCTL_ADD_SBINTIME_MSEC`, `SYSCTL_ADD_SBINTIME_USEC`, `SYSCTL_ADD_STRING`, `SYSCTL_ADD_CONST_STRING`, `SYSCTL_ADD_STRUCT`, `SYSCTL_ADD_TIMEVAL_SEC`, `SYSCTL_ADD_U8`, `SYSCTL_ADD_U16`, `SYSCTL_ADD_U32`, `SYSCTL_ADD_U64`, `SYSCTL_ADD_UAUTO`, `SYSCTL_ADD_UINT`, `SYSCTL_ADD_ULONG`, `SYSCTL_ADD_UMA_CUR`, `SYSCTL_ADD_UMA_MAX`, `SYSCTL_ADD_UQUAD`, `SYSCTL_CHILDREN`, `SYSCTL_STATIC_CHILDREN`, `SYSCTL_NODE_CHILDREN`, `SYSCTL_PARENT`, `SYSCTL_BOOL`, `SYSCTL_COUNTER_U64`, `SYSCTL_COUNTER_U64_ARRAY`, `SYSCTL_INT`, `SYSCTL_INT_WITH_LABEL`, `SYSCTL_LONG`, `sysctl_msec_to_ticks`, `SYSCTL_NODE`, `SYSCTL_NODE_WITH_LABEL`, `SYSCTL_OPAQUE`, `SYSCTL_PROC`, `SYSCTL_QUAD`, `SYSCTL_ROOT_NODE`, `SYSCTL_S8`, `SYSCTL_S16`, `SYSCTL_S32`, `SYSCTL_S64`, `SYSCTL_SBINTIME_MSEC`, `SYSCTL_SBINTIME_USEC`, `SYSCTL_STRING`, `SYSCTL_CONST_STRING`, `SYSCTL_STRUCT`, `SYSCTL_TIMEVAL_SEC`, `SYSCTL_U8`, `SYSCTL_U16`, `SYSCTL_U32`, `SYSCTL_U64`, `SYSCTL_UINT`, `SYSCTL_ULONG`, `SYSCTL_UMA_CUR`, `SYSCTL_UMA_MAX`, `SYSCTL_UQUAD`

## 概要

```c
#include <sys/param.h>
#include <sys/sysctl.h>

SYSCTL_DECL(name);

struct sysctl_oid *
SYSCTL_ADD_BOOL(struct sysctl_ctx_list *ctx, struct sysctl_oid_list *parent,
    int number, const char *name, int ctlflags, bool *ptr, uint8_t val,
    const char *descr)

struct sysctl_oid *
SYSCTL_ADD_COUNTER_U64(struct sysctl_ctx_list *ctx,
    struct sysctl_oid_list *parent, int number, const char *name,
    int ctlflags, counter_u64_t *ptr, const char *descr)

struct sysctl_oid *
SYSCTL_ADD_COUNTER_U64_ARRAY(struct sysctl_ctx_list *ctx,
    struct sysctl_oid_list *parent, int number, const char *name,
    int ctlflags, counter_u64_t *ptr, intmax_t len, const char *descr)

struct sysctl_oid *
SYSCTL_ADD_INT(struct sysctl_ctx_list *ctx, struct sysctl_oid_list *parent,
    int number, const char *name, int ctlflags, int *ptr, int val,
    const char *descr)

struct sysctl_oid *
SYSCTL_ADD_LONG(struct sysctl_ctx_list *ctx, struct sysctl_oid_list *parent,
    int number, const char *name, int ctlflags, long *ptr,
    const char *descr)

struct sysctl_oid *
SYSCTL_ADD_NODE(struct sysctl_ctx_list *ctx, struct sysctl_oid_list *parent,
    int number, const char *name, int ctlflags,
    int (*handler)(SYSCTL_HANDLER_ARGS), const char *descr)

struct sysctl_oid *
SYSCTL_ADD_NODE_WITH_LABEL(struct sysctl_ctx_list *ctx,
    struct sysctl_oid_list *parent, int number, const char *name,
    int ctlflags, int (*handler)(SYSCTL_HANDLER_ARGS),
    const char *descr, const char *label)

struct sysctl_oid *
SYSCTL_ADD_OPAQUE(struct sysctl_ctx_list *ctx,
    struct sysctl_oid_list *parent, int number, const char *name,
    int ctlflags, void *ptr, intptr_t len, const char *format,
    const char *descr)

struct sysctl_oid *
SYSCTL_ADD_PROC(struct sysctl_ctx_list *ctx, struct sysctl_oid_list *parent,
    int number, const char *name, int ctlflags, void *arg1, intptr_t arg2,
    int (*handler)(SYSCTL_HANDLER_ARGS), const char *format,
    const char *descr)

struct sysctl_oid *
SYSCTL_ADD_QUAD(struct sysctl_ctx_list *ctx, struct sysctl_oid_list *parent,
    int number, const char *name, int ctlflags, int64_t *ptr,
    const char *descr)

struct sysctl_oid *
SYSCTL_ADD_ROOT_NODE(struct sysctl_ctx_list *ctx, int number,
    const char *name, int ctlflags, int (*handler)(SYSCTL_HANDLER_ARGS),
    const char *descr)

struct sysctl_oid *
SYSCTL_ADD_S8(struct sysctl_ctx_list *ctx, struct sysctl_oid_list *parent,
    int number, const char *name, int ctlflags, int8_t *ptr, int8_t val,
    const char *descr)

struct sysctl_oid *
SYSCTL_ADD_S16(struct sysctl_ctx_list *ctx, struct sysctl_oid_list *parent,
    int number, const char *name, int ctlflags, int16_t *ptr, int16_t val,
    const char *descr)

struct sysctl_oid *
SYSCTL_ADD_S32(struct sysctl_ctx_list *ctx, struct sysctl_oid_list *parent,
    int number, const char *name, int ctlflags, int32_t *ptr, int32_t val,
    const char *descr)

struct sysctl_oid *
SYSCTL_ADD_S64(struct sysctl_ctx_list *ctx, struct sysctl_oid_list *parent,
    int number, const char *name, int ctlflags, int64_t *ptr, int64_t val,
    const char *descr)

struct sysctl_oid *
SYSCTL_ADD_SBINTIME_MSEC(struct sysctl_ctx_list *ctx,
    struct sysctl_oid_list *parent, int number, const char *name,
    int ctlflags, sbintime_t *ptr, const char *descr)

struct sysctl_oid *
SYSCTL_ADD_SBINTIME_USEC(struct sysctl_ctx_list *ctx,
    struct sysctl_oid_list *parent, int number, const char *name,
    int ctlflags, sbintime_t *ptr, const char *descr)

struct sysctl_oid *
SYSCTL_ADD_STRING(struct sysctl_ctx_list *ctx,
    struct sysctl_oid_list *parent, int number, const char *name,
    int ctlflags, char *ptr, intptr_t len, const char *descr)

struct sysctl_oid *
SYSCTL_ADD_CONST_STRING(struct sysctl_ctx_list *ctx,
    struct sysctl_oid_list *parent, int number, const char *name,
    int ctlflags, const char *ptr, const char *descr)

struct sysctl_oid *
SYSCTL_ADD_STRUCT(struct sysctl_ctx_list *ctx,
    struct sysctl_oid_list *parent, int number, const char *name,
    int ctlflags, void *ptr, struct_type, const char *descr)

struct sysctl_oid *
SYSCTL_ADD_TIMEVAL_SEC(struct sysctl_ctx_list *ctx,
    struct sysctl_oid_list *parent, int number, const char *name,
    int ctlflags, struct timeval *ptr, const char *descr)

struct sysctl_oid *
SYSCTL_ADD_U8(struct sysctl_ctx_list *ctx, struct sysctl_oid_list *parent,
    int number, const char *name, int ctlflags, uint8_t *ptr, uint8_t val,
    const char *descr)

struct sysctl_oid *
SYSCTL_ADD_U16(struct sysctl_ctx_list *ctx, struct sysctl_oid_list *parent,
    int number, const char *name, int ctlflags, uint16_t *ptr,
    uint16_t val, const char *descr)

struct sysctl_oid *
SYSCTL_ADD_U32(struct sysctl_ctx_list *ctx, struct sysctl_oid_list *parent,
    int number, const char *name, int ctlflags, uint32_t *ptr,
    uint32_t val, const char *descr)

struct sysctl_oid *
SYSCTL_ADD_U64(struct sysctl_ctx_list *ctx, struct sysctl_oid_list *parent,
    int number, const char *name, int ctlflags, uint64_t *ptr,
    uint64_t val, const char *descr)

struct sysctl_oid *
SYSCTL_ADD_UINT(struct sysctl_ctx_list *ctx, struct sysctl_oid_list *parent,
    int number, const char *name, int ctlflags, unsigned int *ptr,
    unsigned int val, const char *descr)

struct sysctl_oid *
SYSCTL_ADD_ULONG(struct sysctl_ctx_list *ctx,
    struct sysctl_oid_list *parent, int number, const char *name,
    int ctlflags, unsigned long *ptr, const char *descr)

struct sysctl_oid *
SYSCTL_ADD_UQUAD(struct sysctl_ctx_list *ctx,
    struct sysctl_oid_list *parent, int number, const char *name,
    int ctlflags, uint64_t *ptr, const char *descr)

struct sysctl_oid *
SYSCTL_ADD_UMA_CUR(struct sysctl_ctx_list *ctx,
    struct sysctl_oid_list *parent, int number, const char *name,
    int ctlflags, uma_zone_t ptr, const char *descr)

struct sysctl_oid *
SYSCTL_ADD_UMA_MAX(struct sysctl_ctx_list *ctx,
    struct sysctl_oid_list *parent, int number, const char *name,
    int ctlflags, uma_zone_t ptr, const char *descr)

struct sysctl_oid *
SYSCTL_ADD_UAUTO(struct sysctl_ctx_list *ctx,
    struct sysctl_oid_list *parent, int number, const char *name,
    int ctlflags, void *ptr, const char *descr)

struct sysctl_oid_list *
SYSCTL_CHILDREN(struct sysctl_oid *oidp)

struct sysctl_oid_list *
SYSCTL_STATIC_CHILDREN(struct sysctl_oid_list OID_NAME)

struct sysctl_oid_list *
SYSCTL_NODE_CHILDREN(parent, name)

struct sysctl_oid *
SYSCTL_PARENT(struct sysctl_oid *oid)

SYSCTL_BOOL(parent, number, name, ctlflags, ptr, val, descr);
SYSCTL_COUNTER_U64(parent, number, name, ctlflags, ptr, descr);
SYSCTL_COUNTER_U64_ARRAY(parent, number, name, ctlflags, ptr, len, descr);
SYSCTL_INT(parent, number, name, ctlflags, ptr, val, descr);
SYSCTL_INT_WITH_LABEL(parent, number, name, ctlflags, ptr, val, descr, label);
SYSCTL_LONG(parent, number, name, ctlflags, ptr, val, descr);

int
sysctl_msec_to_ticks(SYSCTL_HANDLER_ARGS);

SYSCTL_NODE(parent, number, name, ctlflags, handler, descr);
SYSCTL_NODE_WITH_LABEL(parent, number, name, ctlflags, handler, descr, label);
SYSCTL_OPAQUE(parent, number, name, ctlflags, ptr, len, format, descr);
SYSCTL_PROC(parent, number, name, ctlflags, arg1, arg2, handler, format, descr);
SYSCTL_QUAD(parent, number, name, ctlflags, ptr, val, descr);
SYSCTL_ROOT_NODE(number, name, ctlflags, handler, descr);
SYSCTL_S8(parent, number, name, ctlflags, ptr, val, descr);
SYSCTL_S16(parent, number, name, ctlflags, ptr, val, descr);
SYSCTL_S32(parent, number, name, ctlflags, ptr, val, descr);
SYSCTL_S64(parent, number, name, ctlflags, ptr, val, descr);
SYSCTL_SBINTIME_MSEC(parent, number, name, ctlflags, ptr, descr);
SYSCTL_SBINTIME_USEC(parent, number, name, ctlflags, ptr, descr);
SYSCTL_STRING(parent, number, name, ctlflags, arg, len, descr);
SYSCTL_CONST_STRING(parent, number, name, ctlflags, arg, descr);
SYSCTL_STRUCT(parent, number, name, ctlflags, ptr, struct_type, descr);
SYSCTL_TIMEVAL_SEC(parent, number, name, ctlflags, ptr, descr);
SYSCTL_U8(parent, number, name, ctlflags, ptr, val, descr);
SYSCTL_U16(parent, number, name, ctlflags, ptr, val, descr);
SYSCTL_U32(parent, number, name, ctlflags, ptr, val, descr);
SYSCTL_U64(parent, number, name, ctlflags, ptr, val, descr);
SYSCTL_UINT(parent, number, name, ctlflags, ptr, val, descr);
SYSCTL_ULONG(parent, number, name, ctlflags, ptr, val, descr);
SYSCTL_UQUAD(parent, number, name, ctlflags, ptr, val, descr);
SYSCTL_UMA_MAX(parent, number, name, ctlflags, ptr, descr);
SYSCTL_UMA_CUR(parent, number, name, ctlflags, ptr, descr);
```

## 描述

`SYSCTL` 内核接口允许动态或静态创建 [sysctl(8)](../man8/sysctl.8.md) MIB 条目。所有静态 sysctl 在其所属模块卸载时自动销毁。大多数顶级类别是静态创建的，可供所有内核代码及其模块使用。

## 参数说明

**`N`** 节点

**`A`** `char *`

**`C`** `int8_t`

**`CU`** `uint8_t`

**`I`** `int`

**`IK`** [`n`] 开尔文温度，乘以可选的单数字十的幂缩放因子：1（默认）给出分开尔文，0 给出开尔文，3 给出毫开尔文

**`IU`** `unsigned int`

**`L`** `long`

**`LU`** `unsigned long`

**`Q`** `quad_t`

**`QU`** `u_quad_t`

**`S`** `int16_t`

**`SU`** `uint16_t`

**`S,TYPE`** `struct TYPE` 结构

**`ctx`** 指向 sysctl 上下文的指针，如果没有上下文则为 NULL。有关如何创建新 sysctl 上下文，参见 [sysctl_ctx_init(9)](sysctl_ctx_init.9.md)。强烈建议程序员使用上下文来组织它们创建的动态 OID，因为当上下文被销毁时，所有属于它的 sysctl 也会被销毁。这使得 sysctl 清理代码更简单。否则需要在模块卸载时删除所有创建的 OID。

**`parent`** 指向 `struct sysctl_oid_list` 的指针，这是父节点子列表的头。此指针对于静态 sysctl 使用 `SYSCTL_STATIC_CHILDREN` 宏检索，对于动态 sysctl 使用 `SYSCTL_CHILDREN` 宏检索。`SYSCTL_PARENT` 宏可用于获取 OID 的父节点。如果没有父节点，宏返回 NULL。

**`number`** 将分配给此 OID 的 OID 编号。在几乎所有情况下，这应设置为 `OID_AUTO`，这将导致分配下一个可用的 OID 编号。

**`name`** OID 的名称。新创建的 OID 将包含名称的副本。

**`ctlflags`** sysctl 控制标志的位掩码。参见下面描述所有控制标志的章节。

**`arg1`** 过程 sysctl 的第一个回调参数。

**`arg2`** 过程 sysctl 的第二个回调参数。

**`len`** `ptr` 参数指向的数据长度。对于字符串类型 OID，长度为零意味着每次访问 OID 时将使用 strlen(3) 获取字符串长度。对于数组类型 OID，长度必须大于零。

**`ptr`** 指向 sysctl 变量或字符串数据的指针。对于 sysctl 值，指针可以为 SYSCTL_NULL_XXX_PTR，这意味着 OID 是只读的，返回值应取自 `val` 参数。

**`val`** 如果 `ptr` 参数为 SYSCTL_NULL_XXX_PTR，给出此 OID 返回的常量值。否则不使用此参数。

**`struct_type`** 结构类型名称。

**`handler`** 指向负责处理对此 OID 的读取和写入请求的函数的指针。有几个标准处理程序支持对节点、整数、字符串和不透明对象的操作。可以使用 `SYSCTL_PROC` 宏或 `SYSCTL_ADD_PROC` 函数定义自定义处理程序。

**`format`** 指向以符号方式指定 OID 格式的字符串的指针。此格式被 [sysctl(8)](../man8/sysctl.8.md) 用作应用适当数据格式化以供显示的提示。当前格式：

**`descr`** 指向 OID 文本描述的指针。

**`label`** 指向此 OID 组件的聚合标签的指针。为了便于将 sysctl 数据导出到支持通过标签聚合的监控系统（例如 Prometheus），此参数可用于将标签名称附加到 OID。标签作为提示，表示此组件的名称不应成为指标名称的一部分，而是作为标签附加到指标。标签仅应应用于结构相似且编码相同类型值的同级组件，否则聚合无用。

## 节点值类型

用于创建 sysctl 节点的大多数宏和函数导出与节点值类型匹配的只读常量或内核内变量。例如，`SYSCTL_INT` 报告 `int` 类型关联变量的原始值。但是，节点也可以导出内部表示的转换值。

`sysctl_msec_to_ticks` 处理程序可与 `SYSCTL_PROC` 或 `SYSCTL_ADD_PROC` 一起使用以导出毫秒时间间隔。使用此处理程序时，`arg2` 参数指向 `int` 类型的内核内变量，该变量存储适合与 tsleep(9) 等函数一起使用的滴答计数。`sysctl_msec_to_ticks` 函数在报告节点值时将此值转换为毫秒。类似地，`sysctl_msec_to_ticks` 接受以毫秒为单位的新值，并将等效值以滴答为单位存储到 `*arg2`。注意，新代码应使用 `sbintime_t` 类型的内核变量而不是滴答计数。

`SYSCTL_ADD_SBINTIME_MSEC` 和 `SYSCTL_ADD_SBINTIME_USEC` 函数以及 `SYSCTL_SBINTIME_MSEC` 和 `SYSCTL_SBINTIME_USEC` 宏都创建导出 `sbintime_t` 类型内核内变量的节点。这些节点不导出关联变量的原始值。相反，它们导出包含毫秒（MSEC 变体）或微秒（USEC 变体）计数的 64 位整数。

`SYSCTL_ADD_TIMEVAL_SEC` 函数和 `SYSCTL_TIMEVAL_SEC` 宏创建导出 `struct timeval` 类型内核内变量的节点。这些节点不导出关联结构的完整值。相反，它们导出以秒为单位的计数作为简单整数，存储在关联变量的 `tv_sec` 字段中。此函数和宏旨在与存储非负间隔而非绝对时间的变量一起使用。因此，它们拒绝尝试存储负值。

## 创建根节点

Sysctl MIB 或 OID 在层次树中创建。树底部的节点称为根节点，没有父 OID。要创建底部树节点，需要使用 `SYSCTL_ROOT_NODE` 宏或 `SYSCTL_ADD_ROOT_NODE` 函数。默认情况下，所有静态 sysctl 节点 OID 都是全局的，需要在其 `SYSCTL_NODE` 定义语句之前有 `SYSCTL_DECL` 语句，通常在所谓的头文件中。

## 创建 sysctl 字符串

以零结尾的字符串 sysctl 使用 `SYSCTL_STRING` 宏或 `SYSCTL_ADD_STRING` 函数创建。如果 `len` 参数为零，则每次访问 OID 时使用 strlen(3) 计算字符串长度。使用 `SYSCTL_CONST_STRING` 宏或 `SYSCTL_ADD_CONST_STRING` 函数为常量字符串添加 sysctl。

## 创建不透明 sysctl

`SYSCTL_OPAQUE` 或 `SYSCTL_STRUCT` 宏或 `SYSCTL_ADD_OPAQUE` 或 `SYSCTL_ADD_STRUCT` 函数创建处理 `len` 参数指定大小和 `ptr` 参数指向的数据块的 OID。使用结构版本时，类型被编码为创建的 sysctl 的一部分。

## 创建自定义 sysctl

`SYSCTL_PROC` 宏和 `SYSCTL_ADD_PROC` 函数创建具有指定 `handler` 函数的 OID。处理程序负责处理对 OID 的所有读取和写入请求。如果内核数据不易访问或需要在导出前处理，此 OID 类型特别有用。

## 创建静态 sysctl

静态 sysctl 使用 `SYSCTL_BOOL`、`SYSCTL_COUNTER_U64`、`SYSCTL_COUNTER_U64_ARRAY`、`SYSCTL_INT`、`SYSCTL_INT_WITH_LABEL`、`SYSCTL_LONG`、`SYSCTL_NODE`、`SYSCTL_NODE_WITH_LABEL`、`SYSCTL_OPAQUE`、`SYSCTL_PROC`、`SYSCTL_QUAD`、`SYSCTL_ROOT_NODE`、`SYSCTL_S8`、`SYSCTL_S16`、`SYSCTL_S32`、`SYSCTL_S64`、`SYSCTL_SBINTIME_MSEC`、`SYSCTL_SBINTIME_USEC`、`SYSCTL_STRING`、`SYSCTL_CONST_STRING`、`SYSCTL_STRUCT`、`SYSCTL_TIMEVAL_SEC`、`SYSCTL_U8`、`SYSCTL_U16`、`SYSCTL_U32`、`SYSCTL_U64`、`SYSCTL_UINT`、`SYSCTL_ULONG`、`SYSCTL_UQUAD`、`SYSCTL_UMA_CUR` 或 `SYSCTL_UMA_MAX` 宏之一声明。

## 创建动态 sysctl

动态节点使用 `SYSCTL_ADD_BOOL`、`SYSCTL_ADD_COUNTER_U64`、`SYSCTL_ADD_COUNTER_U64_ARRAY`、`SYSCTL_ADD_INT`、`SYSCTL_ADD_LONG`、`SYSCTL_ADD_NODE`、`SYSCTL_ADD_NODE_WITH_LABEL`、`SYSCTL_ADD_OPAQUE`、`SYSCTL_ADD_PROC`、`SYSCTL_ADD_QUAD`、`SYSCTL_ADD_ROOT_NODE`、`SYSCTL_ADD_S8`、`SYSCTL_ADD_S16`、`SYSCTL_ADD_S32`、`SYSCTL_ADD_S64`、`SYSCTL_ADD_SBINTIME_MSEC`、`SYSCTL_ADD_SBINTIME_USEC`、`SYSCTL_ADD_STRING`、`SYSCTL_ADD_CONST_STRING`、`SYSCTL_ADD_STRUCT`、`SYSCTL_ADD_TIMEVAL_SEC`、`SYSCTL_ADD_U8`、`SYSCTL_ADD_U16`、`SYSCTL_ADD_U32`、`SYSCTL_ADD_U64`、`SYSCTL_ADD_UAUTO`、`SYSCTL_ADD_UINT`、`SYSCTL_ADD_ULONG`、`SYSCTL_ADD_UQUAD`、`SYSCTL_ADD_UMA_CUR` 或 `SYSCTL_ADD_UMA_MAX` 函数之一创建。有关如何销毁动态创建的 OID 的更多信息，参见 sysctl_remove_oid(9) 或 sysctl_ctx_free(9)。

## 控制标志

对于上述大多数函数和宏，不需要将类型声明为访问标志的一部分——但是，当声明由函数实现的 sysctl 时，需要在访问掩码中包含类型：

**`CTLTYPE_NODE`** 这是旨在作为其他节点父节点的节点。

**`CTLTYPE_INT`** 这是有符号整数。

**`CTLTYPE_STRING`** 这是存储在字符数组中的以空字符结尾的字符串。

**`CTLTYPE_S8`** 这是 8 位有符号整数。

**`CTLTYPE_S16`** 这是 16 位有符号整数。

**`CTLTYPE_S32`** 这是 32 位有符号整数。

**`CTLTYPE_S64`** 这是 64 位有符号整数。

**`CTLTYPE_OPAQUE`** 这是不透明数据结构。

**`CTLTYPE_STRUCT`** `CTLTYPE_OPAQUE` 的别名。

**`CTLTYPE_U8`** 这是 8 位无符号整数。

**`CTLTYPE_U16`** 这是 16 位无符号整数。

**`CTLTYPE_U32`** 这是 32 位无符号整数。

**`CTLTYPE_U64`** 这是 64 位无符号整数。

**`CTLTYPE_UINT`** 这是无符号整数。

**`CTLTYPE_LONG`** 这是有符号长整型。

**`CTLTYPE_ULONG`** 这是无符号长整型。

除新节点声明外，所有 sysctl 类型都需要设置以下标志之一，指示 sysctl 的读写处置：

**`CTLFLAG_RD`** 这是只读 sysctl。

**`CTLFLAG_RDTUN`** 这是只读 sysctl 和可调参数，在模块加载或系统启动早期从系统环境中获取一次。

**`CTLFLAG_WR`** 这是可写 sysctl。

**`CTLFLAG_RW`** 此 sysctl 可读可写。

**`CTLFLAG_RWTUN`** 这是可读可写 sysctl 和可调参数，在模块加载或系统启动早期从系统环境中获取一次。

**`CTLFLAG_NOFETCH`** 如果节点使用 CTLFLAG_[XX]TUN 标记为可调参数，此标志将阻止从系统环境获取初始值。通常，此标志仅应用于非常早期的低级系统设置代码，而不用于常见驱动程序和模块。

**`CTLFLAG_MPSAFE`** 此 [sysctl(9)](sysctl.9.md) 处理程序是 MP 安全的。不要在调用此处理程序时获取 Giant。这仅应用于 `SYSCTL_PROC` 条目。

此外，还可以指定以下任一可选标志：

**`CTLFLAG_ANYBODY`** 任何用户或进程都可以写入此 sysctl。

**`CTLFLAG_CAPRD`** 处于能力模式的进程可以读取此 sysctl。

**`CTLFLAG_CAPWR`** 处于能力模式的进程可以写入此 sysctl。

**`CTLFLAG_SECURE`** 仅当进程的有效安全级别 <=0 时才能写入此 sysctl。

**`CTLFLAG_PRISON`** 此 sysctl 可由 jail(2) 中的进程写入。

**`CTLFLAG_SKIP`** 迭代 sysctl 命名空间时，不列出此 sysctl。

**`CTLFLAG_TUN`** 建议标志，表示此变量还存在系统可调参数。初始 sysctl 值在模块加载或系统启动早期从系统环境中获取一次。

**`CTLFLAG_DYN`** 动态创建的 OID 自动设置此标志。

**`CTLFLAG_VNET`** OID 引用启用 VIMAGE 的变量。

## 实例

使用 `SYSCTL_DECL` 声明 `security` sysctl 树供新节点使用的示例：

```sh
SYSCTL_DECL(_security);
```

整数、不透明、字符串和过程 sysctl 的示例如下：

```sh
/*
 * 常量整数值示例。注意控制
 * 标志是 CTLFLAG_RD，变量指针是 SYSCTL_NULL_INT_PTR，
 * 值已声明。
 */
SYSCTL_INT(_kern, OID_AUTO, hz_max, CTLFLAG_RD, SYSCTL_NULL_INT_PTR, HZ_MAXIMUM,
    "Maximum hz value supported");
/*
 * 变量整数值示例。注意控制
 * 标志是 CTLFLAG_RW，变量指针已设置，
 * 值为 0。
 */
static int	doingcache = 1;		/* 1 => 启用缓存 */
SYSCTL_INT(_debug, OID_AUTO, vfscache, CTLFLAG_RW, &doingcache, 0,
    "Enable name cache");
/*
 * 变量字符串值示例。注意控制
 * 标志是 CTLFLAG_RW，变量指针和字符串
 * 大小已设置。与较新的 sysctl 不同，此较旧的 sysctl 使用
 * 静态 oid 编号。
 */
char kernelname[MAXPATHLEN] = "/kernel";	/* XXX bloat */
SYSCTL_STRING(_kern, KERN_BOOTFILE, bootfile, CTLFLAG_RW,
    kernelname, sizeof(kernelname), "Name of kernel file booted");
/*
 * sysctl 导出的不透明数据类型示例。注意
 * 提供了变量指针和大小，以及
 * sysctl(8) 的格式字符串。
 */
static l_fp pps_freq;	/* 缩放频率偏移 (ns/s) */
SYSCTL_OPAQUE(_kern_ntp_pll, OID_AUTO, pps_freq, CTLFLAG_RD,
    &pps_freq, sizeof(pps_freq), "I", "");
/*
 * 导出字符串
 * 信息的过程 sysctl 示例。注意声明了数据类型，NULL
 * 变量指针和 0 大小，函数指针，以及
 * sysctl(8) 的格式字符串。
 */
SYSCTL_PROC(_kern_timecounter, OID_AUTO, hardware, CTLTYPE_STRING |
    CTLFLAG_RW, NULL, 0, sysctl_kern_timecounter_hardware, "A",
    "");
```

以下是如何创建新的顶级类别以及如何将另一个子树连接到现有静态节点的示例。此示例不使用上下文，这导致所有中间 oid 的管理繁琐，因为它们需要稍后释放：

```sh
#include <sys/sysctl.h>
 ...
/*
 * 需要保留指向新创建子树的指针，
 * 以便稍后释放它们：
 */
static struct sysctl_oid *root1;
static struct sysctl_oid *root2;
static struct sysctl_oid *oidp;
static int a_int;
static char *string = "dynamic sysctl";
 ...
root1 = SYSCTL_ADD_ROOT_NODE(NULL,
	OID_AUTO, "newtree", CTLFLAG_RW, 0, "new top level tree");
oidp = SYSCTL_ADD_INT(NULL, SYSCTL_CHILDREN(root1),
	OID_AUTO, "newint", CTLFLAG_RW, &a_int, 0, "new int leaf");
 ...
root2 = SYSCTL_ADD_NODE(NULL, SYSCTL_STATIC_CHILDREN(_debug),
	OID_AUTO, "newtree", CTLFLAG_RW, 0, "new tree under debug");
oidp = SYSCTL_ADD_STRING(NULL, SYSCTL_CHILDREN(root2),
	OID_AUTO, "newstring", CTLFLAG_RD, string, 0, "new string leaf");
```

此示例创建以下子树：

```sh
debug.newtree.newstring
newtree.newint
```

*一旦不再需要 OID，应注意释放所有 OID！*

## sysctl 命名

添加、修改或移除 sysctl 名称时，重要的是要注意这些接口可能被用户、库、应用程序或文档（如已出版的书籍）使用，并且是隐式发布的应用程序接口。与其他应用程序接口一样，必须谨慎不要破坏现有应用程序，并考虑新命名空间的未来使用，以避免需要重命名或移除将来可能被依赖的接口。

为新 sysctl 选择的语义应尽可能清晰，sysctl 的名称必须密切反映其语义。因此 sysctl 名称值得相当多的考虑。它应简短但又能代表 sysctl 的含义。如果名称由多个单词组成，它们应以下划线字符分隔，如 `compute_summary_at_mount`。仅当名称由不超过两个单词组成且每个单词不超过四个字符时，才可以省略下划线字符，如 `bootfile`。

对于布尔 sysctl，应完全避免否定逻辑。也就是说，不要使用 `no_foobar` 或 `foobar_disable` 这样的名称。它们令人困惑并导致配置错误。改用肯定逻辑：`foobar`、`foobar_enable`。

不应依赖的临时 sysctl 节点 OID 必须在其名称中以领先下划线字符指定。例如：`_dirty_hack`。

## 参见

sysctl(3), [sysctl(8)](../man8/sysctl.8.md), [device_get_sysctl(9)](device_get_sysctl.9.md), [sysctl_add_oid(9)](sysctl_add_oid.9.md), sysctl_ctx_free(9), [sysctl_ctx_init(9)](sysctl_ctx_init.9.md), sysctl_remove_oid(9)

## 历史

[sysctl(8)](../man8/sysctl.8.md) 实用程序首次出现在 4.4BSD 中。`SYSCTL_ADD_CONST_STRING` 首次出现在 FreeBSD 12.1 中。

## 作者

BSD 中最初找到的 `sysctl` 实现已被 Poul-Henning Kamp 大量重写，以添加对名称查找、命名空间迭代和动态添加 MIB 节点的支持。

本手册页由 Robert N. M. Watson 编写。

## 安全考虑

创建新 sysctl 时，应仔细注意正在创建的监控或管理接口的安全影响。内核中存在的大多数 sysctl 是只读的或仅可由超级用户写入。导出有关系统数据结构和操作的大量信息的 sysctl，特别是使用过程实现的 sysctl，将希望实施访问控制以限制不必要地暴露有关其他进程、网络连接等的信息。

以下顶级 sysctl 命名空间常用：

**`compat`** 兼容层信息。

**`debug`** 调试信息。`debug` 下存在各种命名空间。

**`hw`** 硬件和设备驱动程序信息。

**`kern`** 内核行为调优；通常不推荐使用，赞成使用更具体的命名空间。

**`machdep`** 机器相关配置参数。

**`net`** 网络子系统。各种协议在 `net` 下有命名空间。

**`regression`** 回归测试配置和信息。

**`security`** 安全和安全策略配置和信息。

**`sysctl`** 保留用于 sysctl 实现的命名空间。

**`user`** 与用户应用程序行为相关的配置设置。通常，不鼓励使用内核 sysctl 配置应用程序。

**`vfs`** 虚拟文件系统配置和信息。

**`vm`** 虚拟内存子系统配置和信息。
