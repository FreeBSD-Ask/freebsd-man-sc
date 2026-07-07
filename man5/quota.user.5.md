# quota.user(5)

`quota.user` — 每个文件系统的配额数据库

## 名称

`quota.user`

## 描述

每个启用了配额的文件系统应在文件系统根目录中包含一个 `quota.user` 和 `quota.group` 文件。这些文件由 quotacheck(8) 创建，并应使用 edquota(8) 进行编辑。可以通过 [fstab(5)](fstab.5.md) 文件中的 “`userquota`” 和 “`groupquota`” 选项指定不同的位置和文件名。

数据文件包含以下信息：

- 当前块使用量
- 当前文件数
- 软块限制
- 软文件限制
- 硬块限制
- 硬文件限制
- 超过软限制时剩余的块宽限期
- 超过软限制时剩余的文件宽限期

有关各种限制和宽限期的说明，请参见 edquota(8)。

在正常配额操作期间，使用 quotactl(2) 接口查询或设置配额信息，内核会根据需要维护数据文件。如果文件系统上禁用了配额，但在 [fstab(5)](fstab.5.md) 中标记为已启用配额，则会直接使用配额数据文件。

数据文件以 “`struct dqblk`” 结构数组的形式存储，定义于

`#include <ufs/ufs/quota.h>`

并按 UID 或 GID 索引。如果可能，数据文件将以稀疏文件的形式写入。仅对具有非零使用量或非零配额限制的 ID 维护数据。如果尝试访问超出当前数据文件末尾的 ID 数据，将创建一个所有值均为零的配额结构，并根据需要扩展数据文件。quotacheck(8) 实用程序会将数据文件截断为存储具有非零文件使用量或非零配额限制的最高 ID 所需的最小大小。

ID 为 0 的数据记录具有特殊含义。如果 “`dqb_btime`” 或 “`dbq_itime`” 字段非零，则用于指示该文件系统上已超过软限制的用户的宽限期。这些时间可以通过 edquota(8) 使用 `-t` 标志设置。如果未使用 edquota(8) 显式设置宽限期，则使用默认值 7 天。默认值由 `MAX_DQ_TIME` 和 `MAX_IQ_TIME` 定义，位于

`#include <ufs/ufs/quota.h>`

## 参见

quota(1), quotactl(2), [fstab(5)](fstab.5.md), edquota(8), quotacheck(8), quotaoff(8), quotaon(8), repquota(8)
