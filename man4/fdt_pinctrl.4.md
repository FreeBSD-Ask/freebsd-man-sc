# fdt_pinctrl.4

`fdt_pinctrl` — FDT I/O 引脚多路复用支持

## 名称

`fdt_pinctrl`

## 概要

`device fdt_pinctrl`

## 描述

引脚多路复用是一项通过将单个物理连接（视芯片封装而定，可能是引脚、球或焊盘）的信号路由到多个不同 SoC 内部设备之一来重新规划其用途的技术。例如，根据实际设备设计，单个 SoC 芯片引脚可能执行以下任一角色：SPI 时钟、I2C 数据、GPIO 引脚或 PWM 信号。功能选择由 pinmux 控制器执行，这是一个 SoC 硬件块，通常由一组寄存器控制。Pinmux 控制器的能力和寄存器格式取决于实际硬件实现。

在基于 [fdt(4)](fdt.4.md) 的系统上，pinmux 控制器由 device tree 中的一个节点表示。它可以有任意数量的子节点，表示引脚配置组。此类节点的属性是硬件特定的，由各个 pinctrl 驱动程序处理。

### 示例 1

Pinmux 控制器 device tree 节点

```sh
pinctrl@7e220000 {
    compatible = "vndr,soc1715-pinctrl";
    reg = <0x7e220000 0x100>
    spi0_pins: spi0 {
        vndr,pins = <11 12>
        vndr,functions = <ALT0 ALT5>
    }
    i2c0_pins: i2c0 {
        ...
    }
}
```

客户端设备是需要特定引脚配置才能正常工作的硬件设备。根据设备所处状态（活动、空闲），它可能需要不同的引脚配置。每个配置通过将 pinctrl-N 属性设置为指向 pinmux 控制器节点特定子节点的 phandle 列表来描述。N 是从 0 开始的整数值，每增加一组新的引脚配置就递增 1。pinctrl-0 是在 fdt_pinctrl_configure_tree(9) 调用中应用的默认配置。除按索引引用引脚配置外，如果设置了 pinctrl-names 属性，还可以按名称引用。pinctrl-names 的值是一个字符串列表，为每个 pinctrl-N 属性命名。客户端设备可使用 fdt_pinctrl_configure(9) 和 fdt_pinctrl_configure_by_name(9) 请求特定配置。

### 示例 2

```sh
backlight@7f000000 {
    compatible = "vndr,vndr-bl"
    reg = <0x7f000000 0x20>
    ...
    pinctrl-name = "active", "idle"
    pinctrl-0 = <&backlight_active_pins>
    pinctrl-1 = <&backlight_idle_pins>
}
```

pinctrl 驱动程序应实现 FDT_PINCTRL_CONFIGURE 方法，通过调用 fdt_pinctrl_register 函数将自身注册为引脚配置处理程序，并调用 fdt_pinctrl_configure_tree(9) 为所有已启用的设备（“status”属性未设为“disabled”的设备）配置引脚。

## 参见

[fdt_pinctrl(9)](../man9/fdt_pinctrl.9.md)

## 历史

`fdt_pinctrl` 驱动程序首次出现于 FreeBSD 10.2。

## 作者

`fdt_pinctrl` 设备驱动程序由 Ian Lepore <ian@FreeBSD.org> 开发。本手册页由 Oleksandr Tymoshenko <gonzo@FreeBSD.org> 编写。
