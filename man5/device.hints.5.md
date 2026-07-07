# device.hints(5)

`device.hints` — 设备资源提示

## 名称

`device.hints`

## 描述

`device.hints` 文件在系统即将启动时由引导 [loader(8)](../man8/loader.8.md) 读入，其内容会传递给内核。该文件包含各种用于控制内核引导行为的变量。这些变量通常是“设备提示”，但也可以包括任何可调的内核变量。

该文件每行一个变量。以 `#` 字符开头的行是注释，引导加载器会忽略这些行。

在引导加载器读取该文件后，你可以用 `show` 命令查看变量，也可以通过引导加载器的 `set` 和 `unset` 命令添加新变量、修改已有变量或删除变量（参见 [loader(8)](../man8/loader.8.md)）。

系统启动后，你可以使用 [kenv(1)](../man1/kenv.1.md) 命令转储这些变量。

## 设备提示

设备提示变量由设备驱动程序用于配置设备。它们最常被 ISA 设备驱动程序使用，以指定驱动程序探测相关设备的位置，以及将尝试使用的资源。

设备提示行的格式如下：

> `hint.` `driver`. `unit`. `keyword` `=` "" `value`

其中 `driver` 是设备驱动程序的名称，`unit` 是单元号，`keyword` 是提示的关键字。关键字可以是：

**`at`** 指定设备所连接的总线。
**`port`** 指定设备使用的 I/O 端口起始地址。
**`portsize`** 指定设备使用的端口数量。
**`irq`** 是使用的中断线编号。
**`drq`** 是 DMA 通道号。
**`maddr`** 指定设备使用的物理内存地址。
**`msize`** 指定设备使用的物理内存大小。
**`flags`** 为设备设置各种标志位。
**`disabled`** 可设为 "1" 以禁用该设备。

设备驱动程序可能需要一个或多个包含这些关键字的提示行，也可能接受此处未列出的其他关键字，通过 [resource_int_value(9)](../man9/resource_int_value.9.md) 读取。请查阅各个设备驱动程序的手册页以了解可用关键字及其可能的取值。

## 文件

**`/boot/device.hints`** 设备资源提示文件。
**`/sys/`** `ARCH``/conf/GENERIC.hints` `GENERIC` 内核的资源提示示例。
**`/sys/`** `ARCH``/conf/NOTES` 关于内核配置文件和设备资源提示的说明。

## 实例

以下示例为 ISA 总线上的 [uart(4)](../man4/uart.4.md) 驱动程序设置资源：

```sh
hint.uart.0.at="isa"
hint.uart.0.port="0x3F8"
hint.uart.0.flags="0x10"
hint.uart.0.irq="4"
```

以下示例禁用 ACPI 驱动程序：

```sh
hint.acpi.0.disabled="1"
```

设置可调变量：

```sh
vm.pmap.pg_ps_enabled=1
```

## 参见

[kenv(1)](../man1/kenv.1.md), loader.conf(5), [loader(8)](../man8/loader.8.md), [resource_int_value(9)](../man9/resource_int_value.9.md)

## 历史

`device.hints` 文件首次出现于 FreeBSD 5.0。
