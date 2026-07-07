# auditpipe(4)

`auditpipe` — 用于实时审计事件跟踪的伪设备

## 名称

`auditpipe`

## 概要

`options AUDIT`

## 描述

虽然由 [audit(4)](audit.4.md) 生成并由 auditd(8) 维护的审计跟踪文件为审计日志信息提供了可靠的长期存储，但当前日志文件在终止前由审计守护进程拥有，这对于诸如基于主机的入侵检测等实时监控应用来说不太方便。例如，日志可能被轮转，新记录写入新文件，而不会通知可能正在访问该文件的应用程序。

审计设施为需要直接访问实时 BSM 审计数据以进行实时监控的应用程序提供了审计管道设施。审计管道可通过可克隆特殊设备 **/dev/auditpipe** 访问，受设备节点权限限制，提供审计事件流的“tee”（分流）。由于设备是可克隆的，一次可打开多个设备实例；每个设备实例将独立提供对所有记录的访问。

审计管道设备提供离散的 BSM 审计记录；如果应用程序传递的读取缓冲区太小，无法容纳序列中的下一条记录，则该记录将被丢弃。与写入审计跟踪的审计数据不同，记录传送的可靠性不予保证。特别是，当审计管道队列填满时，记录将被丢弃。审计管道设备默认为阻塞模式，但支持非阻塞 I/O、使用 `SIGIO` 的异步 I/O，以及通过 select(2) 和 poll(2) 的轮询操作。

应用程序可选择跟踪全局审计跟踪，或配置独立于全局审计跟踪参数的本地预选参数。

### 审计管道队列 Ioctl

以下 ioctl 检索和设置各种审计管道记录队列属性：

**`AUDITPIPE_GET_QLEN`** 查询管道上当前可供读取的记录数。

**`AUDITPIPE_GET_QLIMIT`** 检索管道上可排队等待读取的最大记录数。

**`AUDITPIPE_SET_QLIMIT`** 设置管道上可排队等待读取的最大记录数。新限制必须介于可通过以下两个 ioctl 查询的队列限制最小值和最大值之间。

**`AUDITPIPE_GET_QLIMIT_MIN`** 查询管道上可排队等待读取的最低可能最大记录数。

**`AUDITPIPE_GET_QLIMIT_MAX`** 查询管道上可排队等待读取的最高可能最大记录数。

**`AUDITPIPE_FLUSH`** 刷新审计管道上所有未完成记录；在设置初始预选属性后很有用，可删除配置过程中排队的、可能不符合用户进程兴趣的记录。

**`AUDITPIPE_GET_MAXAUDITDATA`** 查询审计记录的最大大小，这是用于存放从审计管道读取的审计记录的用户空间缓冲区的有用最小大小。

### 审计管道预选模式 Ioctl

默认情况下，审计管道设施将管道配置为呈现由 auditd(8) 配置的系统级审计跟踪所匹配的记录。但是，审计管道的预选机制可使用替代条件配置，包括管道本地 flags 和 naflags 设置，以及特定 auid 的选择掩码。这允许应用程序跟踪全局审计跟踪中未捕获的事件，以及将呈现的记录限制为应用程序特别感兴趣的记录。

以下 ioctl 配置审计管道上的预选模式：

**`AUDITPIPE_GET_PRESELECT_MODE`** 返回审计管道上的当前预选模式。ioctl 参数应为 `int` 类型。

**`AUDITPIPE_SET_PRESELECT_MODE`** 设置审计管道上的当前预选模式。ioctl 参数应为 `int` 类型。

可能的预选模式值为：

**`AUDITPIPE_PRESELECT_MODE_TRAIL`** 使用全局审计跟踪预选参数为审计管道选择记录。

**`AUDITPIPE_PRESELECT_MODE_LOCAL`** 使用本地审计管道预选；此模型类似于全局审计跟踪配置模型，由全局 flags 和 naflags 参数以及一组按 auid 的掩码组成。这些参数使用更多 ioctl 配置。

更改审计管道预选模式后，先前预选配置下选择的记录可能仍在审计管道队列中。应用程序可在更改配置后刷新当前记录队列以删除可能不希望的记录。

### 审计管道本地预选模式 Ioctl

以下 ioctl 配置当审计管道配置为 `AUDITPIPE_PRESELECT_MODE_LOCAL` 预选模式时使用的预选参数。

**`AUDITPIPE_GET_PRESELECT_FLAGS`** 检索管道上可归属事件的当前默认预选标志。这些标志对应于 audit_control(5) 中的 `flags` 字段。ioctl 参数应为 `au_mask_t` 类型。

**`AUDITPIPE_SET_PRESELECT_FLAGS`** 设置管道上可归属事件的当前默认预选标志。这些标志对应于 audit_control(5) 中的 `flags` 字段。ioctl 参数应为 `au_mask_t` 类型。

**`AUDITPIPE_GET_PRESELECT_NAFLAGS`** 检索管道上不可归属事件的当前默认预选标志。这些标志对应于 audit_control(5) 中的 `naflags` 字段。ioctl 参数应为 `au_mask_t` 类型。

**`AUDITPIPE_SET_PRESELECT_NAFLAGS`** 设置管道上不可归属事件的当前默认预选标志。这些标志对应于 audit_control(5) 中的 `naflags` 字段。ioctl 参数应为 `au_mask_t` 类型。

**`AUDITPIPE_GET_PRESELECT_AUID`** 查询管道上特定 auid 的当前预选掩码。ioctl 参数应为 `struct auditpipe_ioctl_preselect` 类型。要查询的 auid 通过 `au_id_t` 类型的 `ap_auid` 字段指定；掩码将通过 `au_mask_t` 类型的 `ap_mask` 返回。

**`AUDITPIPE_SET_PRESELECT_AUID`** 设置管道上特定 auid 的当前预选掩码。参数与 `AUDITPIPE_GET_PRESELECT_AUID` 相同，但调用者应正确初始化 `ap_mask` 字段以持有所需的预选掩码。

**`AUDITPIPE_DELETE_PRESELECT_AUID`** 删除管道上特定 auid 的当前预选掩码。调用后，与指定 auid 关联的事件将使用默认标志掩码。ioctl 参数应为 `au_id_t` 类型。

**`AUDITPIPE_FLUSH_PRESELECT_AUID`** 删除所有特定 auid 的预选规范。

## 实例

可直接在 **/dev/auditpipe** 上执行 praudit(1) 实用程序以查看默认审计跟踪。

## 参见

poll(2), select(2), [audit(4)](audit.4.md), dtaudit(4), audit_control(5), audit(8), auditd(8)

## 历史

OpenBSM 实现由 McAfee Research（McAfee Inc. 的安全部门）于 2004 年在与 Apple Computer Inc. 的合同下创建。随后被 TrustedBSD 项目采纳为 OpenBSM 发行版的基础。

内核审计支持首次出现于 FreeBSD 6.2。

## 作者

审计管道设施由 Robert Watson <rwatson@FreeBSD.org> 设计和实现。

审计记录的 Basic Security Module（BSM）接口和审计事件流格式由 Sun Microsystems 定义。

## 缺陷

有关审计相关的 bug 和限制信息，请参见 [audit(4)](audit.4.md) 手册页。

可配置的预选机制反映了全局审计跟踪所采用的选择模型。提供更灵活的选择模型可能是理想的。

每个管道的审计事件队列为 fifo，如果用户线程对队列头部的记录提供不足，或入队时空间不足，则会发生丢弃。支持记录的部分读取可能是理想的，这将与系统库中实现的缓冲 I/O 更兼容，并允许应用程序选择丢弃哪些记录，可能采用预选的风格。
