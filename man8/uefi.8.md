# uefi(8)

`UEFI` — 统一可扩展固件接口引导程序

## 名称

`UEFI`

## 描述

`UEFI` 统一可扩展固件接口为操作系统提供引导时和运行时服务。`UEFI` 是 i386 和 amd64 CPU 架构上传统 BIOS 的替代品，也用于 arm、arm64 和 riscv 架构。

UEFI 规范是可扩展固件接口（EFI）规范的后继者。UEFI 和 EFI 这两个术语经常互换使用。

`UEFI` 引导过程加载位于 EFI 系统分区（ESP）中的系统引导程序代码。ESP 是一个具有特定标识符的 GPT 或 MBR 分区，包含一个 [msdosfs(4)](../man4/msdosfs.4.md) FAT 文件系统及指定的文件层次结构。

| **分区方案** | **ESP 标识符** |
| ------------ | -------------- |
| GPT | C12A7328-F81F-11D2-BA4B-00A0C93EC93B |
| MBR | 0xEF |

`UEFI` 引导过程如下：

| **架构** | **默认路径** |
| -------- | ------------ |
| amd64 | `/EFI/BOOT/BOOTX64.EFI` |
| arm | `/EFI/BOOT/BOOTARM.EFI` |
| arm64 | `/EFI/BOOT/BOOTAA64.EFI` |
| i386 | `/EFI/BOOT/BOOTIA32.EFI` |
| riscv | `/EFI/BOOT/BOOTRISCV64.EFI` |

- `UEFI` 固件在加电时运行，在 EFI 系统分区中搜索操作系统加载器。加载器的路径可由 efibootmgr(8) 管理的 EFI 环境变量设置。如果未设置，则使用上表中特定于架构的默认值。FreeBSD 的默认 `UEFI` 引导配置将 `loader.efi` 安装在默认路径中。
- `loader.efi` 从 **/boot.config** 或 **/boot/config** 读取引导配置。
- `loader.efi` 加载并引导内核，如 [loader.efi(8)](loader.efi.8.md) 中所述。

通过 `UEFI` 引导时自动选择 [vt(4)](../man4/vt.4.md) 系统控制台。

## 文件

`UEFI` 引导

**/boot/loader.efi** 最终阶段引导程序

**/boot/kernel/kernel** 默认内核

**/boot/kernel.old/kernel** 典型的非默认内核（可选）

## 参见

[msdosfs(4)](../man4/msdosfs.4.md), [vt(4)](../man4/vt.4.md), [boot.config(5)](../man5/boot.config.5.md), [boot(8)](boot.8.md), efibootmgr(8), efidp(8), efivar(8), [gpart(8)](gpart.8.md), [loader.efi(8)](loader.efi.8.md), uefisign(8)

## 历史

ia64 架构的 EFI 引导支持首次出现于 FreeBSD 5.0。amd64 的 `UEFI` 引导支持首次出现于 FreeBSD 10.1；arm64 在 FreeBSD 11.0；armv7 在 FreeBSD 12.0；riscv 在 FreeBSD 13.0。

## 缺陷

不支持通过 UEFI 进行 32 位 i386 引导。
