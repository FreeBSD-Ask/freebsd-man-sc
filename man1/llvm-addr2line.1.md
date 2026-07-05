# llvm-addr2line.1

`llvm-addr2line` — a drop-in replacement for addr2line

## 名称

`llvm-addr2line`

## 概要

`llvm-addr2line [options]`

## 描述

`llvm-addr2line` 是 [llvm-symbolizer(1)](llvm-symbolizer.1.md) 工具的别名，但使用了不同的默认值。其目标是成为 GNU 的 addr2line 的直接替代品。

下面列出部分差异：

- `llvm-addr2line` 将所有地址解释为十六进制，并忽略可选的 `0x` 前缀；而 `llvm-symbolizer` 会尝试根据字面量的前缀来确定进制，在没有前缀时默认按十进制处理。
- `llvm-addr2line` 默认不打印函数名。使用 `-f` 可启用该功能。
- `llvm-addr2line` 默认不对函数名进行解符号化（demangle）。使用 `-C` 可开启解符号化。
- `llvm-addr2line` 默认不打印内联帧。使用 `-i` 可显示内联函数中某个源代码位置的内联帧。
- `llvm-addr2line` 默认使用 `--output-style=GNU`。
- `llvm-addr2line` 从环境变量 `LLVM_ADDR2LINE_OPTS` 而非 `LLVM_SYMBOLIZER_OPTS` 解析选项。

## 参见

[llvm-symbolizer(1)](llvm-symbolizer.1.md)

## 作者

由 LLVM Team (<https://llvm.org/>) 维护。

## 版权

2003-2023, LLVM Project
