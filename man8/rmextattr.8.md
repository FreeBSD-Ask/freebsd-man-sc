# rmextattr(8)

`rmextattr` — 操作扩展属性

## 名称

`getextattr`, `lsextattr`, `rmextattr`, `setextattr`

## 概要

`getextattr [-fhqsx] attrnamespace attrname filename ...` `lsextattr [-fhq] attrnamespace filename ...` `rmextattr [-fhq] attrnamespace attrname filename ...` `setextattr [-fhnq] attrnamespace attrname attrvalue filename ...` `setextattr -i [-fhnq] attrnamespace attrname filename ...`

## 描述

这些工具是用于操作文件和目录上命名扩展属性的用户工具。`attrnamespace` 参数应为要获取的属性的命名空间：合法值为 `user` 和 `system`。`attrname` 参数应为属性名，`filename` 为目标文件或目录的名称，`attrvalue` 为要存储在属性中的字符串。

可用选项如下：

**`-f`** （强制。）忽略单个文件名上的错误并继续处理剩余参数。

**`-h`** （不跟随。）如果文件是符号链接，则对链接本身执行操作，而不是对链接指向的文件执行操作。

**`-i`** （从标准输入。）从标准输入读取属性数据，而不是作为参数提供。

**`-n`** （NUL 终止。）以 `NUL` 终止写出的扩展内容。

**`-q`** （安静。）不打印路径名并抑制错误消息。给出两次时，仅打印属性值，不带尾随换行符。

**`-s`** （字符串化。）转义不可打印字符并在输出周围加引号。

**`-x`** （十六进制。）以十六进制打印输出。

## 实例

```sh
setextattr system md5 `md5 -q /boot/kernel/kernel` /boot/kernel/kernel
md5 -q /boot/kernel/kernel | setextattr -i system md5 /boot/kernel/kernel
getextattr system md5 /boot/kernel/kernel
getextattr -qq system md5 /boot/kernel/kernel | od -x
lsextattr system /boot/kernel/kernel
rmextattr system md5 /boot/kernel/kernel
```

## 参见

[extattr(2)](../sys/extattr_get_file.2.md), [extattr(3)](../posix1e/extattr.3.md), extattrctl(8), [extattr(9)](../man9/extattr.9.md)

## 历史

扩展属性支持作为 TrustedBSD 项目的一部分开发，并引入 FreeBSD 5.0。开发它是为了支持需要将附加标签与每个文件或目录关联的安全扩展。

## 作者

Robert N M Watson

Poul-Henning Kamp
