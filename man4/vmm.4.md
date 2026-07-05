# vmm.4

`vmm.ko` — bhyve 虚拟机监视器

## 名称

`vmm.ko`

## 概要

`要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
vmm_load="YES"
```

`也可使用 kldload(8) 手动加载此模块：`

```sh
kldload vmm
```

## 描述

`vmm.ko` 提供 [bhyve(4)](bhyve.4.md) hypervisor 的内核部分。支持以下平台：

- amd64：需要支持 VT-x/EPT 的 Intel CPU 或支持 SVM 的 AMD CPU。
- arm64：引导 CPU 必须从 EL2 启动，且系统必须具有 GICv3 中断控制器。如果可用，将使用 VHE 支持。
- riscv：CPU 必须实现 H（hypervisor）RISC-V ISA 扩展。

向虚拟机的 PCI 设备直通需要支持 VT-d 的硬件，且仅在 amd64 上可用。

## 访问控制

仅超级用户和具有对 **/dev/vmmctl** 设备文件写访问权限的进程可创建和销毁虚拟机。默认情况下，`vmm` 组的成员具有此访问权限。虚拟机一旦创建，只能由该用户或超级用户销毁。

无特权用户必须使用“监控模式”来运行虚拟机；在此模式下，虚拟机在其设备文件关闭时会自动销毁。运行 [bhyve(8)](../man8/bhyve.8.md) 时，可通过指定 `-M` 标志选择此模式。

如果 jail 设置了 `allow.vmm` 标志，则可在 jail 中创建虚拟机。

## PCI 直通

在硬件支持 VT-d 的 amd64 上，可为 hypervisor 使用而保留 PCI 设备。由 PCI `bus`/`slot`/`function` 组成的条目被添加到 `pptdevs` loader.conf(5) 变量中。附加条目以空格分隔。匹配条目的主机 PCI 设备将分配给 hypervisor，不会被 FreeBSD 设备驱动探测。参见下文 Sx EXAMPLES 一节了解示例用法。

注意，必须首先给予 `vmm` 对其可能需要声明的所有 [pci(4)](pci.4.md) 设备的拒绝权。因此，`vmm` 内核模块几乎肯定需要从 loader.conf(5) 加载，而不是通过将其添加到 [rc.conf(5)](../man5/rc.conf.5.md) 中的 `kld_list in` 来加载。

大量 PCI 设备条目可能需要比 loader.conf(5) 变量的 128 字符限制更长的字符串。可使用 `pptdevs2` 和 `pptdevs3` 变量添加额外条目。

通常，当以无特权用户或在 jail 中运行 [bhyve(8)](../man8/bhyve.8.md) 时，无法使用 PCI 直通，因为此功能需要对 **/dev/pci** 的写访问权限。

## 加载器可调参数

可调参数可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置，或存储在 loader.conf(5) 中。

**`hw.vmm.maxcpu`** 虚拟 CPU 的最大数量。默认值为系统中的物理 CPU 数量。

## 文件

**`/dev/vmmctl`** 用于创建和销毁虚拟机的控制接口。
**`/dev/vmm/*`** 单个虚拟机的设备接口。
**`/dev/vmm.io/*`** 映射到虚拟机中的设备内存的设备接口。

## 实例

为 hypervisor 使用而保留三个 PCI 设备：bus 10 slot 0 function 0、bus 6 slot 5 function 0 和 bus 6 slot 5 function 1。

```sh
pptdevs="10/0/0 6/5/0 6/5/1"
```

可使用 [devctl(8)](../man8/devctl.8.md) 工具在不重启主机的情况下从 PCI 设备分离 `ppt`，然后附加主机驱动。假设 `ppt` 当前附加到 `pci0:0:1:0`，而我们希望改为附加主机的 [xhci(4)](xhci.4.md) 驱动：

```sh
# devctl set driver -f pci0:0:1:0 xhci
```

同样可用于将 `ppt` 附加回来：

```sh
# devctl set driver -f pci0:0:1:0 ppt
```

## 参见

[bhyve(4)](bhyve.4.md), loader.conf(5), [bhyve(8)](../man8/bhyve.8.md), [bhyvectl(8)](../man8/bhyvectl.8.md), [bhyveload(8)](../man8/bhyveload.8.md), [devctl(8)](../man8/devctl.8.md), [jail(8)](../man8/jail.8.md), [kldload(8)](../man8/kldload.8.md)

## 历史

`vmm.ko` 最早出现于 FreeBSD 10.0。arm64 和 riscv 支持最早出现于 FreeBSD 15.0。

## 作者

Neel Natu <neel@freebsd.org> Peter Grehan <grehan@freebsd.org>
