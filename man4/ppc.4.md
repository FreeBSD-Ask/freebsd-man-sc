# ppc(4)

`ppc` — 并口芯片组驱动

## 名称

`ppc`

## 概要

`device ppc`

`在 /boot/device.hints 中：hint.ppc.0.at="isa" hint.ppc.0.irq="7"`

`对于一个或多个 PPBUS 总线：device ppbus`

## 描述

`ppc` 驱动为 [ppbus(4)](ppbus.4.md) 系统的各种并口芯片组提供低级支持。

在探测阶段，`ppc` 检测并口芯片组并根据其操作模式初始化私有数据：COMPATIBLE、NIBBLE、PS/2、EPP、ECP 和其他混合模式。如果在启动时通过引导接口的 `flags` 变量提供了模式，则根据 `flags` 和硬件支持的模式强制芯片组的操作模式。

在附加阶段，`ppc` 分配 ppbus 结构，初始化它并调用 ppbus 附加函数。

### 支持的标志

```sh
PPB_COMPATIBLE  0x0     /* Centronics 兼容模式 */
PPB_NIBBLE      0x1     /* 反向 4 位模式 */
PPB_PS2         0x2     /* PS/2 字节模式 */
PPB_EPP         0x4     /* EPP 模式，32 位 */
PPB_ECP         0x8     /* ECP 模式 */
```

- 位 0-3：芯片组强制模式（以及任何混合值）。
- 位 4：EPP 协议（0 为 EPP 1.9，1 为 EPP 1.7）
- 位 5：激活 IRQ（1 为禁用 IRQ，0 为启用 IRQ）
- 位 6：禁用芯片组特定检测
- 位 7：禁用 FIFO 检测

### 支持的芯片组

某些并口芯片组受显式支持：已根据其数据手册编写检测和初始化代码。

- SMC FDC37C665GT 和 FDC37C666GT 芯片组
- Natsemi PC873xx 系列（PC87332 和 PC87306）
- Winbond W83877xx 系列（W83877F 和 W83877AF）
- 具有混合模式的类 SMC 芯片组（参见 [ppbus(4)](ppbus.4.md)）

### 为新芯片组添加支持

你可能希望为你主板所搭载的最新芯片组添加支持。对于 ISA 总线，只需检索芯片组的规格并编写相应的 Fn ppc_mychipset_detect 函数。然后向通用 Fn ppc_detect 函数添加一个条目。

你的 Fn ppc_mychipset_detect 函数应确保：如果 `flags` 引导变量的 mode 字段不为空，则操作模式被强制为给定模式，并且没有其他模式可用，且 ppb->ppb_avm 字段包含芯片组的可用模式。

## 参见

[ppbus(4)](ppbus.4.md), [ppi(4)](ppi.4.md), [device.hints(5)](../man5/device.hints.5.md)

## 历史

`ppc` 手册页首次出现于 FreeBSD 3.0。

## 作者

本手册页由 Nicolas Souchu 编写。

## 缺陷

芯片组检测过程可能损坏你的芯片组配置。可使用上述标志禁用芯片组特定检测。
