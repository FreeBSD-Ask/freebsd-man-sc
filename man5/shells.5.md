# shells.5

`shells` — shell 数据库

## 名称

`shells`

## 描述

`shells` 文件包含系统上的 shell 列表。对于每种 shell 应单独占一行，由相对于 root 的 shell 路径组成。

`#` 表示注释开始；从 `#` 到行尾的字符不会被搜索该文件的例程解释。空行也会被忽略。

## 文件

**`/etc/shells`** `shells` 文件位于 **/etc**。

## 参见

getusershell(3)

## 历史

`shells` 文件格式出现于 4.3BSD。
