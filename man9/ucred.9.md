# ucred.9

`ucred` — 与用户凭证相关的函数

## 名称

`ucred`, `crget`, `crhold`, `crfree`, `crcopy`, `crdup`, `cru2x`

## 概要

`#include <sys/param.h>`

`#include <sys/ucred.h>`

`struct ucred * crget(void)`

`struct ucred * crhold(struct ucred *cr)`

`void crfree(struct ucred *cr)`

`void crcopy(struct ucred *dest, struct ucred *src)`

`struct ucred * crcopysafe(struct proc *p, struct ucred *cr)`

`struct ucred * crdup(struct ucred *cr)`

`void crsetgroups(struct ucred *cr, int ngrp, gid_t *groups)`

`void crsetgroups_and_egid(struct ucred *cr, int ngrp, gid_t *groups, gid_t default_egid)`

`void cru2x(struct ucred *cr, struct xucred *xcr)`

## 描述

`cru2x` 系列函数用于管理内核中的用户凭证结构（`struct ucred`）。

`crget()` 函数为新结构分配内存，将其引用计数设为 1，并初始化其锁。

`crhold()` 函数增加凭证的引用计数。

`crfree()` 函数减少凭证的引用计数。如果计数降为 0，则释放该结构所占用的存储。

`crcopy()` 函数将源（模板）凭证的内容复制到目标模板中。目标中的 `uidinfo` 结构通过调用 uihold(9) 进行引用。

`crcopysafe()` 函数将与进程 `p` 关联的当前凭证复制到新分配的凭证 `cr` 中。必须持有 `p` 的进程锁，并在需要时释放和重新获取以在 `cr` 中分配组存储空间。

`crdup()` 函数为新结构分配内存并将 `cr` 的内容复制到其中。实际的复制由 `crcopy()` 执行。

`crsetgroups()` 函数设置表示补充组的 `cr_groups` 和 `cr_ngroups` 变量，根据需要分配空间。它还将组列表截断为当前最大组数。`crsetgroups_and_egid()` 函数类似，但将 `groups` 的第一个组单独解释为要设置的有效 GID，仅将后续组设置为补充组。如果 `groups` 为空，它将使用 `default_egid` 作为新的有效 GID。不应使用其他机制修改 `cr_groups` 数组。

`cru2x()` 函数将 `ucred` 结构转换为 `xucred` 结构。即，将数据从 `cr` 复制到 `xcr`；它忽略前者中后者不存在的字段（例如 `cr_uidinfo`），并适当设置后者中前者不存在的字段（例如 `cr_version`）。

## 返回值

`crget()`、`crhold()`、`crdup()` 和 `crcopysafe()` 都返回指向 `ucred` 结构的指针。

## 使用说明

从 FreeBSD 5.0 开始，`ucred` 结构包含可扩展字段。这意味着必须始终遵循正确的协议来创建新鲜且可写的凭证结构：新凭证必须始终使用 `crget()`、`crcopy()` 和 `crcopysafe()` 从现有凭证派生。

在常见情况下，访问控制决策所需的凭证以只读方式使用。在这些情况下，应使用线程凭证 `td_ucred`，因为它无需加锁即可安全访问，并且在调用期间保持稳定，即使多线程应用程序从另一个线程更改进程凭证也是如此。

在进程凭证更新期间，必须在检查和更新期间持有进程锁，以防止竞态条件。进程凭证 `td->td_proc->p_ucred` 必须同时用于检查和更新。如果在系统调用期间更新了进程凭证，并且稍后在同一系统调用期间要根据线程凭证进行检查，则还必须从进程凭证刷新线程凭证，以防止使用过期值。为避免此情况，建议将更新进程凭证的系统调用设计为避免其他授权函数。

如果线程需要临时提升权限，可以在活动期间或系统调用的剩余时间内替换线程凭证。但是，由于线程凭证通常是共享的，应采取适当的谨慎措施，确保通过使用 `crget()` 和 `crcopy()` 对可写凭证进行修改。

在对线程或进程执行授权检查以对另一个线程或进程执行操作时，应谨慎行事。由于临时提升，目标线程凭证*绝不*应作为访问控制决策中的目标凭证：应使用与线程关联的进程凭证 `td->td_proc->p_ucred`。例如，[p_candebug(9)](p_candebug.9.md) 接受目标进程而非目标线程用于访问控制目的。

## 参见

uihold(9)

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
