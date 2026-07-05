# domainset.9

`domainset` — domainset 函数与操作

## 名称

`domainset`

## 概要

```c
#include <sys/_domainset.h>
#include <sys/domainset.h>
```

```c
struct domainset {
        domainset_t     ds_mask;
        uint16_t        ds_policy;
        domainid_t      ds_prefer;
	...
};
```

```c
struct domainset *
DOMAINSET_FIXED(domain)

struct domainset *
DOMAINSET_FT()

struct domainset *
DOMAINSET_IL()

struct domainset *
DOMAINSET_RR()

struct domainset *
DOMAINSET_PREF(domain)

struct domainset *
domainset_create(const struct domainset *key)

int
domainset_populate(struct domainset *domain, domainset_t *mask, int policy,
    size_t mask_size)

int
sysctl_handle_domainset(SYSCTL_HANDLER_ARGS)
```

## 描述

`domainset` API 为 NUMA 机器提供内存 domain 分配策略。每个 `domainset` 包含一个允许 domain 的位掩码、一个整数策略以及一个可选的首选 domain。这些共同指定了内存分配的搜索顺序，以及将线程和对象限制到可用内存 domain 子集的能力，以用于系统分区和资源管理。

系统中的每个线程，以及可选的每个 `vm_object_t`（用于表示文件和其他内存源），都引用一个 `struct domainset`。先查询与对象关联的 domainset，如果不存在则系统回退到线程策略。

分配策略有以下可能取值：

**`DOMAINSET_POLICY_ROUNDROBIN`** 以轮转方式从掩码中的每个 domain 分配内存。这会在可用 domain 之间均匀分布带宽。此策略可为固定分配指定单个 domain。

**`DOMAINSET_POLICY_FIRSTTOUCH`** 内存从首次访问它的节点分配。如果当前 domain 不在允许集合中或内存耗尽，则回退到轮转。此策略针对局部性进行优化，但如果内存被许多不在本地 domain 中的 CPU 访问，可能产生最差结果。

**`DOMAINSET_POLICY_PREFER`** 内存从 `prefer` 成员中的节点分配。首选节点必须在允许掩码中被设置。如果首选节点内存耗尽，分配会回退到允许集合中的轮转。

**`DOMAINSET_POLICY_INTERLEAVE`** 内存以条带方式分配，根据对象内的偏移量为集合中的每个 domain 分配多个页面。条带宽度依赖于对象，可大到超级页（在 amd64 上为 2MB）。这能在内存 domain 之间提供良好的分布，同时保持较高的系统效率，对于一般用途优于轮转。

`DOMAINSET_FIXED`、`DOMAINSET_FT`、`DOMAINSET_IL`、`DOMAINSET_RR` 和 `DOMAINSET_PREF` 宏提供指向全局预定义策略的指针，用于在编译时已知所需策略时使用。`DOMAINSET_FIXED` 是一种仅允许从指定 domain 分配的策略。`DOMAINSET_FT` 是一种尝试从当前 CPU 本地分配内存、如果初次分配失败则回退到轮转策略的策略。`DOMAINSET_IL` 和 `DOMAINSET_RR` 在系统中的所有 domain 之间提供轮转选择，分别对应 `DOMAINSET_POLICY_INTERLEAVE` 和 `DOMAINSET_POLICY_ROUNDROBIN` 策略。`DOMAINSET_PREF` 策略尝试从指定 domain 分配，但与 `DOMAINSET_FIXED` 不同，会回退到其他 domain 来满足请求。应优先使用这些策略而非 `DOMAINSET_FIXED`，以避免在 `M_WAITOK` 请求上无限阻塞。

`domainset_create` 函数接受一个部分填写的 domainset 作为键，返回一个有效的 domainset 或 NULL。使用者务必不要使用未由此函数返回的 domainset。`domainset` 是不可变类型，在所有匹配键之间共享，返回后不得修改。

`domainset_populate` 函数使用 domain 掩码和策略填充 `domainset` 结构。它用于在使用 `domainset_create` 创建自定义 domainset 时验证并将 domain 掩码和策略转换为 `domainset` 结构。

`sysctl_handle_domainset` 函数作为便利提供，用于修改或查看通过 cpuset(2) 不可访问的 domainset。它旨在与 [sysctl(9)](sysctl.9.md) 一起使用。

## 参见

[cpuset(1)](../man1/cpuset.1.md), [cpuset(2)](../man2/cpuset.2.md), [cpuset_setdomain(2)](../man2/cpuset_setdomain.2.md), [bitset(9)](bitset.9.md)

## 历史

```c
#include <sys/domainset.h>
```

首次出现于 FreeBSD 12.0。
