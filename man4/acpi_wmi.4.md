# acpi_wmi.4

`acpi_wmi` — ACPI 到 WMI 映射驱动

## 名称

`acpi_wmi`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

```sh
device acpi_wmi
```

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
acpi_wmi_load="YES"
```

## 描述

`acpi_wmi` 驱动为厂商专用的 WMI 实现（例如 HP 和 Acer 笔记本）提供接口。它会创建 **`/dev/wmistat%d`**，读取该设备可获取系统中发现的 GUID 信息。

## 文件

**`/dev/wmistat%d`** WMI 状态设备。

## SYSCTL

目前实现了以下 sysctl 节点：

**`dev.acpi_wmi.%d.bmof`** 二进制托管对象格式（MOF）缓冲区

## 实例

从系统中发现的第一个 WMI 接口读取 GUID：

```sh
# cat /dev/wmistat0
GUID                                  INST EXPE METH STR EVENT OID
{5FB7F034-2C63-45E9-BE91-3D44E2C707E4}   1 NO   WMAA NO  NO    AA
{95F24279-4D7B-4334-9387-ACCDC67EF61C}   1 NO   NO   NO  0x80+ -
{2B814318-4BE8-4707-9D84-A190A859B5D0}   1 NO   NO   NO  0xA0  -
{05901221-D566-11D1-B2F0-00A0C9062910}   1 NO   NO   NO  NO    AB
{1F4C91EB-DC5C-460B-951D-C7CB9B4B8D5E}   1 NO   WMBA NO  NO    BA
{2D114B49-2DFB-4130-B8FE-4A3C09E75133}  57 NO   NO   NO  NO    BC
{988D08E3-68F4-4C35-AF3E-6A1B8106F83C}  20 NO   NO   NO  NO    BD
{14EA9746-CE1F-4098-A0E0-7045CB4DA745}   1 NO   NO   NO  NO    BE
{322F2028-0F84-4901-988E-015176049E2D}   2 NO   NO   NO  NO    BF
{8232DE3D-663D-4327-A8F4-E293ADB9BF05}   0 NO   NO   NO  NO    BG
{8F1F6436-9F42-42C8-BADC-0E9424F20C9A}   0 NO   NO   NO  NO    BH
{8F1F6435-9F42-42C8-BADC-0E9424F20C9A}   0 NO   NO   NO  NO    BI
```

使用 `ports/converters/bmfdec` 中的 **bmf2mof** 读取第一个 WMI 接口描述：

```sh
# sysctl -b dev.acpi_wmi.0.bmof | bmf2mof
[abstract]
class Lenovo_BIOSElement {
};
[WMI, Dynamic, Provider("WMIProv"), WmiExpense(1), Description("Bios Setting"),
GUID("{51F5230E-9677-46cd-A1CF-C0B23EE34DB7}"), Locale("MS\ x409")]
class Lenovo_BiosSetting : Lenovo_BiosElement {
  [key, read] String InstanceName;
    [read] Boolean Active;
      [WmiDataId(1), Description("BIOS setting")] String CurrentSetting;
      };
   ...
```

## 参见

[acpi(4)](acpi.4.md)

## 标准

> "Windows Instrumentation: WMI and ACPI", Microsoft Corporation.

## 历史

`acpi_wmi` 设备驱动首次出现于 FreeBSD 8.0。

## 作者

`acpi_wmi` 驱动由 Michael Gmelin <freebsd@grem.de> 编写。

其工作受到 Carlos Corbacho 编写的 Linux **acpi-wmi** 驱动的启发。

MOF 处理受到 Andy Lutomirski 编写的 Linux **wmi-bmof** 驱动的启发。

本手册页由 Michael Gmelin <freebsd@grem.de> 编写。
