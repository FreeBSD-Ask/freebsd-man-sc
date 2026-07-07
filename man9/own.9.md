# own(9)

`own` — Dallas Semiconductor 1-Wire 网络和传输层接口

## 名称

`own`, `own_send_command`, `own_command_wait`, `own_self_command`, `own_acquire_bus`, `own`, `own_release_bus`, `OWN_ACQUIRE_BUS`, `OWN_CRC`, `OWN_RELEASE_BUS`, `OWN_SEND_COMMAND`

## 概要

```c
#include <sys/bus.h>
```

```c
#include <dev/ow/own.h>
```

```c
int
own_send_command(device_t pdev, struct ow_cmd *cmd)

int
own_command_wait(device_t pdev, struct ow_cmd *cmd)

int
own_self_command(device_t pdev, struct ow_cmd *cmd, uint8_t xpt_cmd)

int
own_acquire_bus(device_t pdev, int how)

int
own_release_bus(device_t pdev)

int
own_crc(device_t pdev, uint8_t *buffer, size_t len)

int
OWN_SEND_COMMAND(device_t ndev, device_t pdev, struct ow_cmd *cmd)

int
OWN_ACQUIRE_BUS(device_t ndev, device_t pdev, int how)

void
OWN_RELEASE_BUS(device_t ndev, device_t pdev)

uint8_t
OWN_CRC(device_t ndev, device_t pdev, uint8_t *buffer, size_t len)
```

## 描述

`OWN_SEND_COMMAND` 接口定义了三组用于与 1-Wire 设备交互的函数：发送命令、保留总线和确保数据完整性。为原始 `OWN` [kobj(9)](kobj.9.md) 接口提供了包装函数，出于改进安全性考虑应优先于 [kobj(9)](kobj.9.md) 接口使用。

### 总线命令

1-Wire 总线定义了对总线上设备的不同访问层。`OWN` 函数提供对网络层和传输层的访问。网络层将下一条命令指定为发送给总线上所有设备或特定设备。网络层还指定链路层使用的速度。

`struct ow_cmd` 封装了网络访问、速度和时序信息。它指定要发送的命令以及是否读取数据。其成员包括：

```c
#include <dev/ow/ow.h>
```

**OW_FLAG_OVERDRIVE** 以超速发送 `xpt_cmd` 字节并读取 `xpt_read` 字节。

**OW_FLAG_READ_BIT** 将 `xpt_read_len` 解释为在 `xpt_cmd` 之后要读取的位数而非字节数。

**`flags`** 控制结构解释的标志。这些标志定义在

**`rom_cmd`** 要发送的 ROM 命令字节。

**`rom_len`** 要发送的 ROM 命令字节数。

**`rom_read_len`** 发送 ROM 命令后要读取的字节数。

**`rom_read`** 读取 ROM 命令后字节的缓冲区。

**`xpt_cmd`** 要发送的传输命令。

**`xpt_len`** 要发送的传输命令字节长度。指定为 0 表示无传输命令。

**`xpt_read_len`** 发送 `xpt_cmd` 字节后要读取的字节数。如果 `flags` 中设置了 `OW_FLAG_READ_BIT` 位，则为要读取的位数。读取的位被打包成字节。

**`xpt_read`** 读取数据的缓冲区。

`own_command_wait` 获取 1-Wire 总线（必要时等待），发送命令，然后释放总线。`own_send_command` 在不保留总线的情况下发送命令。`pdev` 是发送命令的客户端设备（表示层设备）。`cmd` 参数描述要发送到 1-Wire 总线的事务。

`own_self_command` 以便捷方式填写 `cmd`，使用 MATCH_ROM ROM 命令、`pdev` 的 ROM 地址和 `xpt_cmd` 来创建定向命令。

### 总线保留

1-Wire 系统包含一个用于总线的咨询锁，表示层设备可使用它来协调访问。此时锁定纯粹是建议性的。

`own_acquire_bus` 保留总线。如果 `how` 参数为 `OWN_WAIT`，则无限期等待；如果传递 `OWN_DONTWAIT` 且总线由另一个客户端拥有，则返回错误 `EWOULDBLOCK`。

`own_release_bus` 释放总线。

### 数据完整性

`own_crc` 对通过 `buffer` 和 `len` 传递的数据计算 1-Wire 标准 CRC 函数，并返回结果。

### 注意事项

1-Wire 标准（Maxim AN937）定义了类似于 ISO 网络层的层。最低的相关层是链路层，定义了轮询窗口和不同模式的信号时序。网络层构建在链路层之上，用于以单播或多播方式寻址设备。传输层定义了来自设备的命令和响应。表示层由用于控制总线上特定 1-Wire 设备的设备特定命令和操作组成。

这些接口由 [ow(4)](../man4/ow.4.md) 设备实现。表示层设备（newbus [ow(4)](../man4/ow.4.md) 设备的子设备）应仅调用此处描述的函数。[owc(4)](../man4/owc.4.md) 设备提供的功能（特别是 [owll(9)](owll.9.md) 接口）应仅由 [ow(4)](../man4/ow.4.md) 驱动程序调用。

## 参见

[ow(4)](../man4/ow.4.md), [owc(4)](../man4/owc.4.md), [owll(9)](owll.9.md) **`https://pdfserv.maximintegrated.com/en/an/AN937.pdf`**

## 法律条款

1-Wire 是 Maxim Integrated Products, Inc. 的注册商标。

## 历史

`OWN` 驱动程序首次出现在 FreeBSD 11.0 中。

## 作者

`OWN` 设备驱动程序和本手册页由 Warner Losh 编写。
