# dtrace_dtmalloc(4)

`dtrace_dtmalloc` — 用于按类型跟踪内核内存分配的 DTrace 提供者

## 名称

`dtrace_dtmalloc`

## 概要

`dtmalloc::function:malloc dtmalloc::function:free`

## 描述

`dtmalloc` 提供者检测 [malloc(9)](../man9/malloc.9.md) 和 free(9) 内核函数，以按类型跟踪内存分配。有关 malloc 类型的更多详情，请参见 [malloc(9)](../man9/malloc.9.md)。

`dtmalloc``::``function``:malloc` 探测在成功分配时触发。其探测参数为：

| **探测参数** | **定义** |
| ------------ | -------- |
| `args[0]` | Ft struct malloc_type *mtp |
| `args[1]` | Ft struct malloc_type_internal *mtip |
| `args[2]` | Ft struct malloc_type_stats *mtsp |
| `args[3]` | Ft unsigned long size |
| `args[4]` | Ft int zindx |

`dtmalloc``::``function``:free` 探测在释放操作时触发。其探测参数为：

| **free 探测参数** | **定义** |
| ----------------- | -------- |
| `args[0]` | Ft struct malloc_type *mtp |
| `args[1]` | Ft struct malloc_type_internal *mtip |
| `args[2]` | Ft struct malloc_type_stats *mtsp |
| `args[3]` | Ft unsigned long size |
| `args[4]` | 始终为 0 |

每个探测的前三个参数（即 `mtp , mtip` 和 `mtsp`）提供对 [malloc(9)](../man9/malloc.9.md) 类型内部的引用；`size` 是分配的大小；`zindx` 是用于分配的 `kmemzones[]` 数组的索引。实践中，`size` 是最有用的跟踪参数。

## 实现说明

`dtmalloc` 提供者中探测描述的 `function` 部分是 [malloc(9)](../man9/malloc.9.md) 类型的简短描述，其中所有空白字符均替换为下划线。例如，由以下定义的 malloc 类型

```sh
MALLOC_DEFINE(M_FOO_BAR, "foo bar", "FooBar subsystem");
```

将具有名为

```sh
dtmalloc::foo_bar:
```

的探测。

## 文件

**sys/malloc.h** 定义 `struct malloc_type` 的头文件。

## 实例

### 实例 1：按类型统计成功的内存分配

```sh
# dtrace -n 'dtmalloc:::malloc {@[stringof args[0]->ks_shortdesc] = count()}'
dtrace: description 'dtmalloc:::malloc ' matched 480 probes
^C
  80211node                                                         1
  CAM CCB                                                           1
  CAM periph                                                        1
  ioctlops                                                          1
  netlink                                                           1
  soname                                                            4
  sysctltmp                                                         4
  solaris                                                           5
  acpica                                                           16
  temp                                                             36
  lkpikmalloc                                                      44
  iov                                                             100
  selfd                                                           648
```

## 参见

[dtrace(1)](../man1/dtrace.1.md), [tracing(7)](../man7/tracing.7.md), [malloc(9)](../man9/malloc.9.md)

## 作者

`dtmalloc` 由 John Birrell <jb@FreeBSD.org> 编写。

本手册页由 Mateusz Piotrowski <0mp@FreeBSD.org> 编写。

## 注意事项

`dtmalloc` 提供者不跟踪 uma(9) 分配。
