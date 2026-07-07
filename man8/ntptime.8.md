# ntptime(8)

`ntptime` — 读取内核时间变量

## 名称

`ntptime`

## 概要

`ntptime [-chr] [-e est_error] [-f frequency] [-m max_error] [-o offset] [-s status] [-t time_constant]`

## 描述

`ntptime` 工具仅在与“A Kernel Model for Precision Timekeeping”页面中描述的特殊内核配合使用时才有用（该页面作为 **/usr/share/doc/ntp** 中提供的 HTML 文档的一部分提供）。它使用 `gettime()` 和 adjtime(2) 系统调用（如果可用）读取并显示与时间相关的内核变量。使用 ntpdc(8) 程序的 `kerninfo` 命令可获得类似的显示。

以下选项可用：

**`-c`** 显示 `ntptime` 本身的执行时间。

**`-e`** `est_error` 指定估计误差，以微秒为单位。

**`-f`** `frequency` 指定频率偏移，以百万分率为单位。

**`-h`** 显示帮助信息。

**`-m`** `max_error` 指定最大可能误差，以微秒为单位。

**`-o`** `offset` 指定时钟偏移，以微秒为单位。

**`-r`** 以原始格式显示 Unix 和 NTP 时间。

**`-s`** `status`

**`-t`** `time_constant` 指定时间常数，为 0-4 范围内的整数。

## 参见

adjtime(2), ntpdc(8)
