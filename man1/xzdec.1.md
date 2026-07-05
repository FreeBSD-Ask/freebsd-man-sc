# xzdec.1

`xzdec`, `lzmadec` — 小型 `.xz` 和 `.lzma` 解压缩器

## 名称

`xzdec`, `lzmadec`

## 概要

`xzdec [option...] [file...]`

`lzmadec [option...] [file...]`

## 描述

`xzdec` 是一个基于 liblzma 的仅解压缩工具，用于 `.xz` 文件（且仅限 `.xz` 文件）。`xzdec` 旨在最常见的场景下作为 [xz(1)](xz.1.md) 的直接替代品，即当脚本已编写为使用 `xz --decompress --stdout`（可能还有其他一些常用选项）来解压 `.xz` 文件时。`lzmadec` 与 `xzdec` 完全相同，区别仅在于 `lzmadec` 支持 `.lzma` 文件而非 `.xz` 文件。

为了减小可执行文件的体积，`xzdec` 不支持多线程和本地化，也不读取 `XZ_DEFAULTS` 和 `XZ_OPT` 环境变量中的选项。`xzdec` 不支持显示中间进度信息：向 `xzdec` 发送 `SIGINFO` 信号不会产生任何效果，而发送 `SIGUSR1` 信号会终止进程而非显示进度信息。

## 选项

**`-d`**, **`--decompress`**, **`--uncompress`** 为了与 [xz(1)](xz.1.md) 兼容而忽略此选项。`xzdec` 仅支持解压缩。

**`-k`**, **`--keep`** 为了与 [xz(1)](xz.1.md) 兼容而忽略此选项。`xzdec` 从不创建或删除任何文件。

**`-c`**, **`--stdout`**, **`--to-stdout`** 为了与 [xz(1)](xz.1.md) 兼容而忽略此选项。`xzdec` 始终将解压后的数据写入标准输出。

**`-q`**, **`--quiet`** 指定一次不会产生任何效果，因为 `xzdec` 从不显示任何警告或通知。指定两次可抑制错误信息。

**`-Q`**, **`--no-warn`** 为了与 [xz(1)](xz.1.md) 兼容而忽略此选项。`xzdec` 从不使用退出状态 2。

**`-h`**, **`--help`** 显示帮助信息并成功退出。

**`-V`**, **`--version`** 显示 `xzdec` 和 liblzma 的版本号。

## 退出状态

**0** 一切正常。

**1** 发生错误。

`xzdec` 没有像 [xz(1)](xz.1.md) 那样的警告消息，因此 `xzdec` 不使用退出状态 2。

## 注意事项

日常使用请改用 [xz(1)](xz.1.md)。`xzdec` 或 `lzmadec` 仅适用于需要比功能完整的 [xz(1)](xz.1.md) 更小的解压缩器的场合。

`xzdec` 和 `lzmadec` 实际上并不是特别小。可以通过在编译时去除 liblzma 的功能进一步缩小体积，但对于在典型非嵌入式操作系统发行版中分发的可执行文件，通常不应这样做。如果需要真正小巧的 `.xz` 解压缩器，请考虑使用 XZ Embedded。

## 参见

[xz(1)](xz.1.md)

XZ Embedded：<https://tukaani.org/xz/embedded.html>
