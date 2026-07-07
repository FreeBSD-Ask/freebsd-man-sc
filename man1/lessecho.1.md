# lessecho(1)

`lessecho` — expand metacharacters

## 名称

`lessecho`

## 概要

`lessecho [-a] [-ox] [-cx] [-pn] [-dn] [-mx] [-nn] [-ex] file ...`

`lessecho --version`

## 描述

`lessecho` 是一个简单的程序，它将自身的参数回显到标准输出。但输出中的任何元字符前都会加上一个"转义"字符，默认为反斜杠。`lessecho` 由 `less` 内部调用，不打算供用户直接使用。

## 选项

下面是选项的摘要。

`-ex`

指定 `x`（而非反斜杠）作为元字符的转义字符。如果 `x` 为 `-`，则不使用转义字符，包含元字符的参数改用引号包围。

`-ox`

指定 `x`（而非双引号）作为开引号字符，在使用 `-e-` 选项时使用。

`-cx`

指定 `x` 作为闭引号字符。

`-pn`

以整数形式指定 `n` 作为开引号字符。

`-dn`

以整数形式指定 `n` 作为闭引号字符。

`-mx`

指定 `x` 为一个元字符。默认情况下，没有任何字符被视为元字符。

`-nn`

以整数形式指定 `n` 为一个元字符。

`-fn`

以整数形式指定 `n` 作为元字符的转义字符。

`-a`

指定对所有参数加引号。默认仅对包含元字符的参数加引号。

## 参见

[less(1)](less.1.md)

## 作者

本手册页由 Thomas Schoepf <schoepf@debian.org> 为 Debian GNU/Linux 系统编写（也可供他人使用）。

请在 <https://github.com/gwsw/less/issues> 报告缺陷。
