# zforce.1

`zforce` — 强制 gzip 文件具有 .gz 后缀

## 名称

`zforce`

## 概要

`zforce file`

## 描述

`zforce` 工具会将 [gzip(1)](gzip.1.md) 文件重命名为带有 ".gz" 后缀，这样 [gzip(1)](gzip.1.md) 就不会把它们压缩两次。这在文件传输过程中文件名被截断时很有用。已有 ".gz"、"-gz"、"_gz"、".tgz" 或 ".taz" 后缀的文件，或未经 [gzip(1)](gzip.1.md) 压缩的文件，将被忽略。

## 参见

[gzip(1)](gzip.1.md)

## 注意事项

`zforce` 会不加警告地覆盖已存在的文件。
