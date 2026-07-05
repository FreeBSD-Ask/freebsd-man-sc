# superio.4

`superio` — Super I/O 控制器和总线驱动

## 名称

`superio`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device superio

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
superio_load="YES"
```

## 描述

Super I/O 是一种 I/O 控制器，组合了多种功能上彼此可能不相关的低带宽设备。典型的 Super I/O 可包含如下设备

- 软盘控制器
- 并口
- 串口
- PS/2 鼠标和键盘控制器
- 硬件监控控制器
- 看门狗定时器
- 通用输入输出控制器

`superio` 驱动为位于 Super I/O 控制器中、只能使用控制器接口访问或发现的设备提供支持。某些 Super I/O 设备具有标准化接口。此类设备要么使用众所周知的遗留资源，要么通过 ACPI 通告，或两者兼有。它们可使用 ISA 总线 hints 配置，或由 [acpi(4)](acpi.4.md) 自动配置。`superio` 驱动并非为与此类设备交互而设计。它们可由各自的驱动处理，无需了解 Super I/O 的具体细节。例如，[fdc(4)](fdc.4.md) 提供对软盘控制器的访问。

其他 Super I/O 设备没有任何标准化接口。可使用 `superio` 驱动的功能为这些设备编写驱动。

驱动本身附加到 ISA 总线，因为所有受支持的控制器都通过 LPC I/O 端口访问。

`superio` 驱动不同寻常，因为它既是各种 Super I/O 控制器的控制器驱动，也是这些控制器中受支持设备的总线驱动。

## 硬件

`superio` 驱动支持 Nuvoton（前身为 Winbond）和 ITE 生产的众多 Super I/O 控制器，即：

- Fintek F81803
- Fintek F81865
- Nuvoton NCT5104D/NCT6102D/NCT6106D rev. A 和 B+
- Nuvoton NCT5585D
- Nuvoton NCT6116D
- Nuvoton NCT6775
- Nuvoton NCT6776
- Nuvoton NCT6779
- Nuvoton NCT6791
- Nuvoton NCT6792
- Nuvoton NCT6793
- Nuvoton NCT6795
- Nuvoton NCT6796D-E
- Winbond 83627HF/F/HG/G/S/THF/EHF/DHG/UHG/DHG-P
- Winbond 83637HF
- Winbond 83667HG/HG-B
- Winbond 83687THF
- Winbond 83697HF/UG

## 参见

[superio(9)](../man9/superio.9.md)

## 历史

`superio` 驱动由 Andriy Gapon <avg@FreeBSD.org> 编写。
