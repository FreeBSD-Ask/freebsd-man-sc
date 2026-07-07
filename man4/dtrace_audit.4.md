# dtrace_audit(4)

`dtrace_audit` — 用于跟踪的 DTrace 提供者

## 名称

`dtrace_audit` [audit(4)](audit.4.md) 事件

## 概要

`Fn audit:event:aue_*:commit char *eventname struct audit_record *ar Fn audit:event:aue_*:bsm char *eventname struct audit_record *ar const void * size_t`

`若要将此模块编译进内核，请在内核配置文件中加入以下内容：`

```sh
options DTAUDIT
```

`或者，若要在引导时加载此模块，请在 loader.conf(5) 中加入以下行：`

```sh
dtaudit_load="YES"
```

## 描述

DTrace `dtaudit` 提供者允许用户跟踪内核安全审计子系统 [audit(4)](audit.4.md) 中的事件。[audit(4)](audit.4.md) 提供对可配置的安全相关系统调用集合的详细日志记录，包括关键参数（如文件路径）和返回值，这些在系统调用进行过程中以无竞争方式复制。`dtaudit` 提供者允许 DTrace 脚本有选择地为系统调用启用内核内审计记录捕获，然后在系统调用完成时以内核内格式或 BSM 格式（c audit.log(5)）访问这些记录。虽然内核内审计记录数据结构会随内核随时间变化而变化，但对于在 D 脚本中使用而言，它比 DTrace 系统调用提供者或 BSM 轨迹本身可用的接口要友好得多。

### 配置

`dtaudit` 提供者依赖于编译进内核的 [audit(4)](audit.4.md)。只有在内核中安装了事件到名称的映射后，`dtaudit` 探测才可用，这通常由 auditd(8) 在引导过程中完成，前提是在 [rc.conf(5)](../man5/rc.conf.5.md) 中启用了 audit：

```sh
auditd_enable="YES"
```

如果需要在引导更早阶段使用 `dtaudit` 探测——例如在单用户模式下——或不启用 [audit(4)](audit.4.md)，可通过在 loader.conf(5) 中加入以下行在引导加载器中预加载。

```sh
audit_event_load="YES"
```

### 探测

Fn audit:event:aue_*:commit 探测在系统调用返回期间同步触发，提供两个参数的访问：一个 `char *` 审计事件名称，以及 `struct audit_record *` 内核内审计记录。由于探测在系统调用返回时触发，用户线程尚未重新获得控制权，来自线程和进程的额外信息仍可被脚本捕获。

Fn audit:event:aue_*:bsm 探测在系统调用返回后异步触发，在 BSM 转换之后、写入磁盘之前，提供四个参数的访问：一个 `char *` 审计事件名称、`struct audit_record *` 内核内审计记录、一个指向已转换 BSM 记录的 `const void *` 指针，以及一个表示 BSM 记录长度的 `size_t`。

## 实现说明

当一组 `dtaudit` 探测被注册时，将捕获相应的内核内审计记录并触发其探测，无论 [audit(4)](audit.4.md) 子系统本身是否会为了将其写入审计轨迹或交付给 [auditpipe(4)](auditpipe.4.md) 而捕获该记录。仅因启用了 dtaudit(4) 探测而分配的内核内审计记录不会不必要地写入审计轨迹或启用的管道。

## 参见

[dtrace(1)](../man1/dtrace.1.md), [audit(4)](audit.4.md), audit.log(5), loader.conf(5), [rc.conf(5)](../man5/rc.conf.5.md), auditd(8)

## 历史

`dtaudit` 提供者首次出现于 FreeBSD 12.0。

## 作者

本软件和本手册页由 BAE Systems、剑桥大学计算机实验室和纪念大学在 DARPA/AFRL 合同（FA8650-15-C-7558）（“CADETS”）下开发，作为 DARPA 透明计算（TC）研究计划的一部分。`dtaudit` 提供者和本手册页由 Robert Watson <rwatson@FreeBSD.org> 编写。

## 缺陷

由于 [audit(4)](audit.4.md) 在用户空间维护其主事件到名称映射数据库，因此在 `dtaudit` 探测可用之前必须将该数据库加载到内核中。

`dtaudit` 只能提供对系统调用审计事件的访问，而不能访问用户态事件的全部范围，例如与登录、密码更改等相关的事件。
