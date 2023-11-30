  NTPTIME(8)  

NTPTIME(8)

FreeBSD System Manager's Manual

NTPTIME(8)

[名称](#__u540D___u79F0_)
=======================

`ntptime` —

读取内核时间变量

[概要](#__u6982___u8981_)
=======================

`ntptime` \[`-chr`\] \[`-e` est\_error\] \[`-f` frequency\] \[`-m` max\_error\] \[`-o` offset\] \[`-s` status\] \[`-t` time\_constant\]

[描述](#__u63CF___u8FF0_)
=======================

`ntptime` 实用程序仅对 “用于精确计时的内核模型” 页面中描述的特殊内核有用（作为 /usr/share/doc/ntp 中提供的 HTML 文档的一部分提供）。 它使用 `gettime`() 和 adjtime(2) 系统调用（如果可用）读取和显示与时间相关的内核变量。 使用 ntpdc(8) 程序的 `kerninfo` 命令可以获得类似的显示。

可以使用以下选项：

[`-c`](#c)

显示 `ntptime` 本身的执行时间。

[`-e`](#e) est\_error

指定估计误差，以微秒为单位。

[`-f`](#f) frequency

指定频率偏移，以百万分之几为单位。

[`-h`](#h)

显示帮助信息。

[`-m`](#m) max\_error

指定最大可能的错误，以微秒为单位。

[`-o`](#o) offset

指定时钟偏移，以微秒为单位。

[`-r`](#r)

以原始格式显示 Unix 和 NTP 时间。

[`-s`](#s) status

[`-t`](#t) time\_constant

指定时间常数，0-4 范围内的整数。

[参见](#__u53C2___u89C1_)
=======================

adjtime(2), ntpdc(8)

April 27, 2015

FreeBSD 13.1-RELEASE