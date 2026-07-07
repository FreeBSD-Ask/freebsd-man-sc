# lzmainfo(1)

`lzmainfo` — 显示 .lzma 文件头中存储的信息

## 名称

`lzmainfo`

## 概要

`lzmainfo [--help] [--version] [file...]`

## 描述

`lzmainfo` 显示 `.lzma` 文件头中存储的信息。它从指定 `file` 读取前 13 个字节，解码头，并以人类可读格式打印到标准输出。如果未给定 `files` 或 `file` 为 `-`，则读取标准输入。

通常最有趣的信息是未压缩大小和字典大小。仅当文件为非流式 `.lzma` 格式变体时才能显示未压缩大小。解压缩文件所需的内存量为几十 KB 加上字典大小。

`lzmainfo` 包含在 XZ Utils 中主要是为了向后兼容 LZMA Utils。

## 退出状态

**0** 一切正常。
**1** 发生错误。

## 缺陷

`lzmainfo` 使用 `MB`，而正确的后缀应为 `MiB`（2^20 字节）。这是为了保持输出与 LZMA Utils 兼容。

## 参见

xz(1)
