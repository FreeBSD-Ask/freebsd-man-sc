  LOADER.EFI(8)  

LOADER.EFI(8)

FreeBSD System Manager's Manual

LOADER.EFI(8)

[名称](#__u540D___u79F0_)
=======================

`loader.efi` —

UEFI 内核加载器

[描述](#__u63CF___u8FF0_)
=======================

在 UEFI 系统上， `loader.efi` 加载内核。 它被安装到 ESP（EFI 系统分区）中，或者安装在 ESP 中 /efi/boot/bootXXX.efi 的默认位置，或者安装在 FreeBSD 保留区域中的 /efi/freebsd/loader.efi 中，或者安装在 ESP 中系统为 /boot/loader.efi 。 boot1.efi(8) 用于加载 `loader.efi` ，当它被放置在系统中时。

September 1, 2020

FreeBSD 13.1-RELEASE