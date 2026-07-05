# nvdimm.4

`nvdimm` — ACPI NVDIMM 驱动

## 名称

`nvdimm`

## 概要

`要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
nvdimm_load="YES"
```

## 描述

注意：`nvdimm` 驱动正在开发中，存在一些下文所述的重要限制。

`nvdimm` 驱动提供对非易失性 DIMM（NVDIMM）持久内存设备的访问，这些设备在 ACPI 中以 `_HID` 为 `ACPI0012` 的根 NVDIMM 设备枚举，并出现在 `NFIT` 表中。

对于 NFIT 描述的每个系统物理地址（SPA）范围，会创建一个设备节点 `/dev/nvdimm_spaNNN`，其中 `NNN` 为 SPA 在表中的位置。该节点可用于对设备进行 read(2)、write(2) 或 mmap(2) 操作。

此外，对于每个 SPA，会创建 geom 提供者 `spaNNN`，可用于创建常规文件系统（例如通过 newfs(8)）并像任何存储卷一样 [mount(8)](../man8/mount.8.md) 它。通过 `/dev/nvdimm_spaNNN` 和 `/dev/spaNNN` 访问的内容是一致的。

`nvdimm` 驱动支持读取 NVDIMM 命名空间（如果你的硬件支持且已通过其他机制配置，例如 BIOS 配置界面）。驱动会为 SPA 中的每个命名空间提供 `/dev/nvdimm_spaNNNnsMMM` 设备节点和 `spaNNNnsMMM` geom 提供者，其行为类似于上述完整 SPA 的对应物。

## 参见

[acpi(4)](acpi.4.md), GEOM(4), geom(8), [mount(8)](../man8/mount.8.md), newfs(8), [disk(9)](../man9/disk.9.md)

## 历史

`nvdimm` 驱动首次出现于 FreeBSD 12.0。

## 作者

`nvdimm` 驱动最初由 Konstantin Belousov <kib@FreeBSD.org> 编写，后由 D. Scott Phillips <scottph@FreeBSD.org> 更新。

## 缺陷

`nvdimm` 驱动不使用 Block Window 接口，因此如果对 NVDIMM 的写入因系统崩溃或断电而中断，相应页面可能处于部分更新的状态。

不支持设备特定方法（DSM），该方法用于报告和控制设备健康状态和磨损情况。

该驱动依赖 pmap_largemap(9) pmap 接口，目前仅在 amd64 上实现。该接口只能在 64 位架构上合理实现。
