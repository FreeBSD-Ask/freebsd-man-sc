# vm\_page\_busy.9

`vm_page_busied`, `vm_page_busy_downgrade`, `vm_page_busy_sleep`, `vm_page_sbusied`, `vm_page_sunbusy`, `vm_page_trysbusy`, `vm_page_tryxbusy`, `vm_page_xbusied`, `vm_page_xunbusy`, `vm_page_assert_sbusied`, `vm_page_assert_unbusied`, `vm_page_assert_xbusied` — 保护页面标识更改和页面内容引用

## 名称

`vm_page_busied`, `vm_page_busy_downgrade`, `vm_page_busy_sleep`, `vm_page_sbusied`, `vm_page_sunbusy`, `vm_page_trysbusy`, `vm_page_tryxbusy`, `vm_page_xbusied`, `vm_page_xunbusy`, `vm_page_assert_sbusied`, `vm_page_assert_unbusied`, `vm_page_assert_xbusied`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_page.h>

int
vm_page_busied(vm_page_t m)

void
vm_page_busy_downgrade(vm_page_t m)

bool
vm_page_busy_sleep(vm_page_t m, const char *msg, int allocflags)

int
vm_page_sbusied(vm_page_t m)

void
vm_page_sunbusy(vm_page_t m)

int
vm_page_trysbusy(vm_page_t m)

int
vm_page_tryxbusy(vm_page_t m)

int
vm_page_xbusied(vm_page_t m)

void
vm_page_xunbusy(vm_page_t m)
```

```c
options INVARIANTS
options INVARIANT_SUPPORT

void
vm_page_assert_sbusied(vm_page_t m)

void
vm_page_assert_unbusied(vm_page_t m)

void
vm_page_assert_xbusied(vm_page_t m)
```

## 描述

页面标识通常由 vm_object 锁和 vm page 锁等更高层锁保护。但有时无法在完成标识更改所需的时间内持有此类锁。在这种情况下，需要拥有标识一段时间的线程可以独占地忙碌页面。

在其他情况下，线程不需要更改页面标识，但希望阻止其他线程更改标识。例如，当线程想要在不持有锁的情况下访问或更新页面内容时，页面会被共享忙碌。

在忙碌页面之前，必须持有 vm_object 锁。页面解除忙碌时同样适用此规则。这使 vm_object 锁成为真正的忙碌互锁。

`vm_page_busied` 函数在当前线程以独占或共享模式忙碌 `m` 时返回非零值。否则返回零。

`vm_page_busy_downgrade` 函数必须用于将 `m` 从独占忙碌状态降级为共享忙碌状态。

`vm_page_busy_sleep` 检查页面 `m` 的忙碌状态，如果页面忙碌则将调用线程置为睡眠。页面的 VM 对象必须被锁定。`allocflags` 参数必须为 `0`（此时如果页面忙碌则函数睡眠）或 `VM_ALLOC_IGN_SBUSY`（此时仅当页面以独占方式忙碌时函数才睡眠）。返回值为 true 表示调用线程已被置为睡眠且对象已解锁。返回值为 false 表示调用线程未睡眠且对象保持锁定。参数 `msg` 是描述用户态工具睡眠条件的字符串。

`vm_page_sbusied` 函数在当前线程以共享模式忙碌 `m` 时返回非零值。否则返回零。

`vm_page_sunbusy` 函数共享解除忙碌 `m`。

`vm_page_trysbusy` 尝试共享忙碌 `m`。如果操作无法立即成功，`vm_page_trysbusy` 返回 0，否则返回非零值。

`vm_page_tryxbusy` 尝试独占忙碌 `m`。如果操作无法立即成功，`vm_page_tryxbusy` 返回 0，否则返回非零值。

`vm_page_xbusied` 函数在当前线程以独占模式忙碌 `m` 时返回非零值。否则返回零。

`vm_page_xunbusy` 函数独占解除忙碌 `m`。

对忙碌状态的断言允许使用 `options INVARIANTS` 和 `options INVARIANT_SUPPORT` 编译的内核在不遵守断言时产生恐慌。

`vm_page_assert_sbusied` 函数在 `m` 未共享忙碌时产生恐慌。

`vm_page_assert_unbusied` 函数在 `m` 未解除忙碌时产生恐慌。

`vm_page_assert_xbusied` 函数在 `m` 未独占忙碌时产生恐慌。

## 参见

[vm_page_aflag(9)](vm_page_aflag.9.md), [vm_page_alloc(9)](vm_page_alloc.9.md), [vm_page_deactivate(9)](vm_page_deactivate.9.md), [vm_page_free(9)](vm_page_free.9.md), [vm_page_grab(9)](vm_page_grab.9.md), [vm_page_insert(9)](vm_page_insert.9.md), [vm_page_lookup(9)](vm_page_lookup.9.md), [vm_page_rename(9)](vm_page_rename.9.md), [VOP_GETPAGES(9)](vop_getpages.9.md)
