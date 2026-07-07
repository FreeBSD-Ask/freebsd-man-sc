# audit(4)

`audit` — 安全事件审计

## 名称

`audit`

## 概要

`options AUDIT`

## 描述

安全事件审计是一种提供细粒度、可配置的安全相关事件日志记录的设施，旨在满足通用准则（CC）通用访问保护轮廓（CAPP）评估的要求。FreeBSD 的 `audit` 设施实现了事实上的工业标准 BSM API、文件格式和命令行界面，最早出现于 Solaris 操作系统。关于用户空间实现的信息可参见 libbsm(3)。

如果在内核中启用，审计支持会在引导时通过 [rc.conf(5)](../man5/rc.conf.5.md) 标志启用。审计守护进程 auditd(8) 负责配置内核以执行 `audit`，并将各审计配置文件中的配置数据推送到内核中。

### 审计专用设备

内核 `audit` 设施提供一个专用设备 **`/dev/audit`**，auditd(8) 通过它监视 `audit` 事件，例如轮转日志的请求、磁盘空间不足的情况以及终止审计的请求。此设备不供应用程序使用。

### 审计管道专用设备

审计管道专用设备（参见 [auditpipe(4)](auditpipe.4.md)）提供可配置的实时跟踪机制，允许应用程序对审计流进行分流（tee），并配置自定义预选参数以细粒度地跟踪用户和事件。

### DTrace 审计提供器

DTrace 审计提供器 dtaudit(4) 允许 D 脚本启用对内核审计事件类型的内核审计记录捕获，然后在审计提交或 BSM 生成期间处理其内容。

## 参见

auditreduce(1), praudit(1), audit(2), auditctl(2), auditon(2), getaudit(2), getauid(2), poll(2), select(2), setaudit(2), setauid(2), libbsm(3), [auditpipe(4)](auditpipe.4.md), dtaudit(4), audit.log(5), audit_class(5), audit_control(5), audit_event(5), audit_user(5), audit_warn(5), [rc.conf(5)](../man5/rc.conf.5.md), audit(8), auditd(8), auditdistd(8)

## 历史

OpenBSM 实现由 McAfee Research（McAfee Inc. 的安全部门）于 2004 年根据与 Apple Computer Inc. 签订的合同创建。随后被 TrustedBSD 项目采纳，作为 OpenBSM 发行版的基础。

内核 `audit` 支持首次出现于 FreeBSD 6.2。

## 作者

本软件由 McAfee Research（McAfee, Inc. 的安全研究部门）根据与 Apple Computer Inc. 签订的合同创建。其他作者包括 Wayne Salamon、Robert Watson 和 SPARTA Inc.

审计记录的 Basic Security Module（BSM）接口和审计事件流格式由 Sun Microsystems 定义。

本手册页由 Robert Watson <rwatson@FreeBSD.org> 编写。

## 缺陷

FreeBSD 内核不会完整校验用户应用程序提交的审计记录是否为语法有效的 BSM；由于记录提交仅限于特权进程，这并非关键 bug。

内核中可审计事件的插桩并不完整，某些系统调用不会生成审计记录，或者生成的审计记录参数信息不完整。

由 [mac(4)](mac.4.md) 设施提供的强制访问控制（MAC）标签不会作为涉及 MAC 决策的记录的一部分被审计。

目前 `audit` 系统调用不支持 jail 内的进程。但是，如果某个进程关联了 `audit` 会话状态，仍会生成审计记录，且审计记录中会包含带有该 jail ID 或名称的 zonename token。
