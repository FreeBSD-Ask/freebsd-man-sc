# isp.4

`isp` — Qlogic FibreChannel SCSI 主机适配器驱动

## 名称

`isp`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device scbus
> device isp
> device ispfw

`或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
isp_load="YES"
ispfw_load="YES"
```

## 描述

此驱动为 FibreChannel SCSI 设备提供访问。

它支持 FCP SCSI 配置文件的发起端和目标模式，使用 Class 3 和 Class 2 连接。支持 Public 和 Private 环、点对点和 Fabric 连接。

对于支持 FC-Tape 功能的磁带机连接，强烈建议使用 FC-Tape。它包含 T-10 FCP-4 规范中的四个要素：

- 命令的精确传递
- FCP I/O 操作的确认完成
- 未成功传输 IU 的重传
- 任务重试标识

这些功能合起来允许与磁带设备进行链路级错误恢复。没有它，发起端无法判断已超时的磁带写命令导致全部、部分还是没有任何数据写入磁带机。当支持 FC-Tape 的控制器连接到支持 FC-Tape 的目标时，FC-Tape 会自动启用。可使用下文描述的配置和 hint 选项禁用。

## 硬件

`isp` 驱动支持以下光纤通道适配器：

| Model: | Speed: | Bus: |
| ------ | ------ | ---- |
| Qlogic QLE2874 (2814) | 64Gb | PCIe |
| Qlogic QLE2870/QLE2872 (2812) | 64Gb | PCIe |
| Qlogic QLE2774 (2814) | 32Gb | PCIe |
| Qlogic QLE2770/QLE2772 (2812) | 32Gb | PCIe |
| Qlogic 2740/2742/2764 (2722/2714) | 32Gb | PCIe |
| Qlogic 2690/2692/2694 (2684/2692) | 16Gb | PCIe |
| Qlogic 267x/836x (2031/8031) FCoE | 16Gb | PCIe |
| Qlogic 256x (2532) | 8Gb | PCIe |
| Qlogic 246x (2432) | 4Gb | PCIe |
| Qlogic 2422 | 4Gb | PCI-X |

## 固件

固件加载受支持并由 [firmware(9)](../man9/firmware.9.md) 处理。正确的固件会在可用时为此类适配器自动加载，或通过手动加载 [ispfw(4)](ispfw.4.md) 模块加载。强烈建议使用 [ispfw(4)](ispfw.4.md) 提供的固件，因为它最有可能已经过此驱动测试。

## 配置选项

光纤通道适配器的目标模式支持可通过

`options ISP_TARGET_MODE`

选项启用。

要禁用 FC-Tape，使用以下配置选项：

`options ISP_FCTAPE_OFF`

注意，即使使用 ISP_FCTAPE_OFF 选项，仍可被下文描述的 fctape hint 覆盖。

## 引导选项

以下选项可通过在 **/boot/device.hints** 中设置值切换。

它们是：

**`lport`** 优先使用仲裁环，回退到点对点。
**`nport`** 优先使用点对点，回退到仲裁环。
**`lport-only`** 仅使用仲裁环。
**`nport-only`** 仅使用点对点。

**`hint.isp.`** `N``.msi` 限制使用的消息信号中断（MSI）数量。

**`hint.isp.`** `N``.msix` 限制使用的扩展消息信号中断（MSI-X）数量。

**`hint.isp.`** `N``.fwload_disable` 禁用 [ispfw(4)](ispfw.4.md) 提供的固件加载的 hint 值。

**`hint.isp.`** `N``.fwload_force` 优先使用 [ispfw(4)](ispfw.4.md) 提供的固件的 hint 值，即使该固件比板卡 flash 中的固件更旧。如果同时指定了 fwload_disable，则 fwload_force 将被忽略。默认情况下，对于 27XX 及更新控制器，[isp(4)](isp.4.md) 驱动将使用较新的固件。对于较旧控制器，[isp(4)](isp.4.md) 驱动在 [ispfw(4)](ispfw.4.md) 提供固件时使用该固件，否则使用板卡 flash 中的固件。

**`hint.isp.`** `N``.ignore_nvram` 忽略板卡 NVRAM 设置的 hint 值。否则使用 NVRAM 设置。

**`hint.isp.`** `N``.fullduplex` 设置全双工模式的 hint 值。

**`hint.isp.`** `N``.topology` 选择连接拓扑的 hint 值。支持的值有：

**`hint.isp.`** `N``.portwwn` 你想使用的完整 64 位 World Wide Port Name，覆盖卡上 NVRAM 中的值。

**`hint.isp.`** `N``.nodewwn` 你想使用的完整 64 位 World Wide Node Name，覆盖卡上 NVRAM 中的值。

**`hint.isp.`** `N``.iid` 覆盖或设置发起端 ID 或环 ID 的 hint。对于本地环拓扑中的光纤通道卡，`强烈`建议将此值设置为非零。

**`hint.isp.`** `N``.role` 定义 isp 实例默认角色的 hint（0 -- 无，1 -- 目标，2 -- 发起端，3 -- 两者）。

**`hint.isp.`** `N``.debug` 驱动调试级别的 hint 值（值见文件 **/usr/src/sys/dev/isp/ispvar.h**）。

**`hint.isp.`** `N``.vports` 创建指定数量附加虚拟端口的 hint。

**`hint.isp.`** `N``.nofctape` 设置为 1 可禁用给定 isp 实例上的 FC-Tape 操作。

**`hint.isp.`** `N``.fctape` 设置为 1 可在支持 FC-Tape 的目标上为给定 isp 实例启用 FC-Tape 操作。

## SYSCTL 选项

**`dev.isp.`** `N``.loop_down_limit` 此值表示环断开后等待多少秒再放弃并使所有可见设备过期。默认为 300 秒（5 分钟）。引导时使用单独的（不可调）超时，以避免因缺少 FC 连接而停止引导。

**`dev.isp.`** `N``.gone_device_time` 此值表示如果设备因环或 Fabric 事件（临时）消失，等待其重新出现的时间。此超时运行期间，对这些设备的 I/O 将被挂起。

**`dev.isp.`** `N``.use_gff_id`

**`dev.isp.`** `N``.use_gft_id` 将这些选项设置为 0 可在 FC Fabric 扫描期间禁用 GFF_ID 和 GFT_ID SNS 请求。如果交换机未正确实现它们，可能会阻止某些设备被发现，此时禁用它们可能有用。禁用它们可能导致对不支持目标角色甚至 FCP 的端口进行不必要的登录。默认为 1（启用）。

**`dev.isp.`** `N``.wwnn` 此端口的只读 World Wide Node Name 值。

**`dev.isp.`** `N``.wwpn` 此端口的只读 World Wide Port Name 值。

**`dev.isp.`** `N``.fw_version_flash` 控制器活动区域中的只读 flash 固件版本值。

**`dev.isp.`** `N``.fw_version_ispfw` [ispfw(4)](ispfw.4.md) 提供的只读固件版本值。

**`dev.isp.`** `N``.fw_version_run` 控制器上当前执行的只读固件版本值。

## 参见

[da(4)](da.4.md), [intro(4)](intro.4.md), [ispfw(4)](ispfw.4.md), [sa(4)](sa.4.md), [scsi(4)](scsi.4.md), gmultipath(8)

## 作者

`isp` 驱动由 Matthew Jacob 最初为 NASA/Ames Research Center 的 NetBSD 编写。后续改进由 Alexander Motin <mav@FreeBSD.org> 完成。

## 缺陷

该驱动当前忽略某些 NVRAM 设置。
