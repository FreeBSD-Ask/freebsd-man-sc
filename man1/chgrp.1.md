  CHGRP(1)  

CHGRP(1)

FreeBSD General Commands Manual

CHGRP(1)

[名称](#__u540D___u79F0_)
=======================

`chgrp` —

更改组

[概要](#__u6982___u8981_)
=======================

`chgrp` \[`-fhvx`\] \[`-R` \[`-H` | `-L` | `-P`\]\] group file ...

[描述](#__u63CF___u8FF0_)
=======================

`chgrp` 实用程序将由每个 file 操作数命名的文件的 group 设置为由组操作数指定的组 ID。

可以使用以下选项：

[`-H`](#H)

如果指定了 `-R` 选项，则命令行上的符号链接会被跟随，因此不受该命令的影响。 （不遵循遍历过程中遇到的符号链接。）

[`-L`](#L)

如果指定了 `-R` 选项，则遵循所有符号链接。

[`-P`](#P)

如果指定了 `-R` 选项，则不遵循符号链接。 这是默认设置。

[`-R`](#R)

更改以文件为根的文件层次结构的组 ID，而不仅仅是文件本身。 当使用 “`.*`” 等通配符时，请注意无意中将 “..” 硬链接匹配到父目录。

[`-f`](#f)

force 选项忽略错误，除了使用错误并且不查询奇怪的模式（除非用户没有适当的权限）。

[`-h`](#h)

如果文件是符号链接，则链接本身的组 ID 会更改，而不是指向的文件。

[`-v`](#v)

使 `chgrp` 变得冗长，在组被修改时显示文件。 如果多次指定 `-v` 标志， `chgrp` 将打印文件名，后跟旧的和新的数字组 ID。

[`-x`](#x)

不遍历文件系统挂载点。

除非指定了 `-R` 选项，否则 `-H` `-、` `-L` 和 `-P` 选项将被忽略。 此外，这些选项相互覆盖，命令的操作由最后一个指定的操作决定。

group 操作数可以是组数据库中的组名，也可以是数字组 ID。 如果组名也是数字组 ID，则操作数用作组名。

调用 `chgrp` 的用户必须属于指定的组并且是文件的所有者，或者是超级用户。

如果 `chgrp` 接收到 `SIGINFO` 信号（参见 stty(1) 的 `status` 参数），则显示当前文件名以及旧的和新的组名。

[FILES](#FILES)
===============

/etc/group

组 ID 文件

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `chgrp` utility exits 0 on success, and >0 if an error occurs.

[兼容性](#__u517C___u5BB9___u6027_)
================================

在该系统的早期版本中，符号链接没有组。

`-v` 和 `-x` 选项是非标准的，不建议在脚本中使用它们。

[参见](#__u53C2___u89C1_)
=======================

chown(2), fts(3), group(5), passwd(5), symlink(7), chown(8)

[标准](#__u6807___u51C6_)
=======================

`chgrp` 实用程序应与 IEEE Std 1003.2 (“POSIX.2”) 兼容。

January 7, 2017

FreeBSD 13.1-RELEASE