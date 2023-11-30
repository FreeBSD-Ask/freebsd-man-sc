  TOUCH(1)  

TOUCH(1)

FreeBSD General Commands Manual

TOUCH(1)

[名称](#__u540D___u79F0_)
=======================

`touch` —

更改文件访问和修改时间

[概要](#__u6982___u8981_)
=======================

`touch` \[`-A` \[-\]\[\[hh\]mm\]SS\] \[`-achm`\] \[`-r` file\] \[`-t` \[\[CC\]YY\]MMDDhhmm\[.SS\]\] \[`-d` YYYY-MM-DDThh:mm:SS\[.frac\]\[tz\]\] file ...

[描述](#__u63CF___u8FF0_)
=======================

`touch` 实用程序设置文件的修改和访问时间。 如果任何文件不存在，则使用默认权限创建它。

默认情况下， `touch` 更改修改和访问时间。 `-a` 和 `-m` 标志可用于单独选择访问时间或修改时间。 选择两者等同于默认设置。 默认情况下，时间戳设置为当前时间。 `-d` 和 `-t` 标志明确指定不同的时间，而 `-r` 标志指定设置指定文件的时间。 `-A` 标志按指定量调整值。

可以使用以下选项：

[`-A`](#A)

按指定值调整文件的访问和修改时间戳。 此标志用于修改时间戳设置不正确的文件。

参数的格式为 “\[-\]\[\[hh\]mm\]SS” ，其中每对字母代表以下内容：

\-

使调整为负：新时间戳设置在旧时间戳之前。

hh

小时数，从 00 到 99。

mm

分钟数，从 00 到 59。

SS

秒数，从 00 到 59。

`-A` 标志暗示 `-c` 标志：如果指定的任何文件不存在，它将被静默忽略。

[`-a`](#a)

更改文件的访问时间。 除非还指定了 `-m` 标志，否则文件的修改时间不会更改。

[`-c`](#c)

如果文件不存在，请不要创建该文件。 `touch` 实用程序不会将此视为错误。 不显示错误消息，退出值不受影响。

[`-d`](#d)

将访问和修改时间更改为指定的日期时间，而不是当前时间。 参数的格式为 “YYYY-MM-DDThh:mm:SS\[.frac\]\[tz\]” ，其中字母表示以下内容：

YYYY

至少四位十进制数字表示年份。

MM, DD, hh, mm, SS

与 `-t` 时间一样。

T

字母 `T` 或空格是时间指示符。

.frac

可选分数，由句点或逗号后跟一个或多个数字组成。 有效位数取决于内核配置和文件系统，并且可能为零。

tz

表示时间的可选字母 `Z` 采用 UTC 。 否则，时间假定为当地时间。 本地时间受 `TZ` 环境变量的值影响。

[`-h`](#h)

如果文件是符号链接，请更改链接本身的时间，而不是链接指向的文件。 请注意， `-h` 意味着 `-c` ，因此不会创建任何新文件。

[`-m`](#m)

更改文件的修改时间。 除非还指定了 `-a` 标志，否则文件的访问时间不会更改。

[`-r`](#r)

使用指定文件中的访问和修改时间，而不是当前时间。

[`-t`](#t)

将访问和修改时间更改为指定时间，而不是当前时间。 参数的格式为 “\[\[CC\]YY\]MMDDhhmm\[.SS\]” ，其中每对字母代表以下内容：

CC

年份的前两位数字（世纪）。

YY

年份的后两位数。 如果指定了 “YY” ，但未指定 “CC” ，则 “YY” 的值介于 69 和 99 之间时， “CC” 的值为 19。 否则，使用 20 的 “CC” 值。

MM

一年中的月份，从 01 到 12。

DD

月份中的某一天，从 01 到 31。

hh

一天中的小时，从 00 到 23。

mm

小时的分钟，从 00 到 59。

SS

分钟的秒数，从 00 到 60。

如果未指定 “CC” 和 “YY” 字母对，则默认值为当前年份。 如果未指定 “SS” 字母对，则该值默认为 0。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `touch` utility exits 0 on success, and >0 if an error occurs.

[兼容性](#__u517C___u5BB9___u6027_)
================================

支持过时的 `touch` 形式，其中将时间格式指定为第一个参数。 如果未指定 `-r` 或 `-t` 选项，则至少有两个参数，第一个参数是长度为 8 或 10 个字符的数字字符串，第一个参数被解释为 “MMDDhhmm\[YY\]” 。

“MM”, “DD”, “hh” 和 “mm” 字母对被视为指定给 `-t` 选项的对应项。 如果 “YY” 字母对在 39 到 99 范围内，则年份设置为 1939 到 1999，否则，年份设置为 21 世纪。

[参见](#__u53C2___u89C1_)
=======================

utimensat(2)

[标准](#__u6807___u51C6_)
=======================

`touch` 实用程序预计将成为 IEEE Std 1003.2 (“POSIX.2”) 规范的超集。

[历史](#__u5386___u53F2_)
=======================

`touch` 实用程序出现在 Version 7 AT&T UNIX 中。

June 1, 2018

FreeBSD 13.1-RELEASE