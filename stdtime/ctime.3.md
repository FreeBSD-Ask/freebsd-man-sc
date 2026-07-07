# ctime(3)

`asctime` — 转换二进制日期和时间值

## 名称

`asctime`, `asctime_r`, `ctime`, `ctime_r`, `difftime`, `gmtime`, `gmtime_r`, `localtime`, `localtime_r`, `mktime`, `offtime`, `offtime_r`, `timegm`

## 库

Lb libc

## 概要

`#include <time.h>`

`extern char *tzname[2]; Ft char * Fn asctime const struct tm *tm Ft char * Fn asctime_r const struct tm *tm char *buf Ft char * Fn ctime const time_t *clock Ft char * Fn ctime_r const time_t *clock char *buf Ft double Fn difftime time_t time1 time_t time0 Ft struct tm * Fn gmtime const time_t *clock Ft struct tm * Fn gmtime_r const time_t *clock struct tm *result Ft struct tm * Fn localtime const time_t *clock Ft struct tm * Fn localtime_r const time_t *clock struct tm *result Ft time_t Fn mktime struct tm *tm Ft struct tm * Fn offtime const time_t *clock long offset Ft struct tm * Fn offtime_r const time_t *clock long offset struct tm *result Ft time_t Fn timegm struct tm *tm`

## 描述

`ctime`、`gmtime`、`localtime` 和 `offtime` 函数均接受一个指向时间值的指针作为参数，该时间值表示自 Epoch（1970 年 1 月 1 日 00:00:00 UTC）以来的秒数；参见 [time(3)](time.3.md)。

`localtime` 函数转换 `clock` 所指向的时间值，并返回指向 `struct tm`（见下文）的指针，该结构包含经当前时区调整后的分解时间信息（参见 [tzset(3)](tzset.3.md)）。当指定时间对应的年份无法容纳于 `int` 类型时，`localtime` 返回 `NULL`。若进程此前未调用过 [tzset(3)](tzset.3.md)，`localtime` 会使用 [tzset(3)](tzset.3.md) 初始化时间转换信息。

填充 `struct tm` 后，`localtime` 将 `tzname` 的第 `tm_isdst` 个元素设置为指向一个 ASCII 字符串的指针，该字符串为与 `localtime` 返回值配合使用的时区缩写。

`gmtime` 函数类似地转换时间值，但不进行任何时区调整，返回指向 `struct tm` 的指针。

`offtime` 函数类似地转换时间值，使用与所提供 `offset` 对应的时区调整，offset 以秒为单位表示，正值表示早于 UTC 的时区（本初子午线以东）。它不会调用 [tzset(3)](tzset.3.md)，也不会修改 `tzname`。

`ctime` 函数以与 `localtime` 相同的方式针对当前时区调整时间值，并返回指向 26 字符字符串的指针，格式如下：

```sh
Thu Nov 24 18:22:48 1986ene0
```

所有字段均为固定宽度。

`asctime` 函数将 `tm` 所指向的 `struct tm` 中的分解时间转换为上述示例所示的格式。

`ctime_r` 和 `asctime_r` 函数提供与 `ctime` 和 `asctime` 相同的功能，区别在于调用者必须提供输出缓冲区 `buf`（长度至少为 26 字符）用于存储结果。`localtime_r`、`gmtime_r` 和 `offtime_r` 函数分别提供与 `localtime`、`gmtime` 和 `offtime` 相同的功能，区别在于调用者必须提供输出缓冲区 `result`。

`mktime` 和 `timegm` 函数将 `tm` 所指向的 `struct tm` 中的分解时间转换为时间值，其编码与 [time(3)](time.3.md) 函数返回值相同（即自 Epoch UTC 以来的秒数）。`mktime` 根据当前时区设置解释输入结构（参见 [tzset(3)](tzset.3.md)），而 `timegm` 将输入结构解释为表示协调世界时（UTC）。

结构的 `tm_wday` 和 `tm_yday` 成员的原始值将被忽略，其他成员的原始值不受其正常范围的限制，必要时会被规范化。例如，10 月 40 日会被改为 11 月 9 日，`tm_hour` 为 -1 表示午夜前 1 小时，`tm_mday` 为 0 表示当前月份的前一天，`tm_mon` 为 -2 表示 `tm_year` 中 1 月之前 2 个月。（`tm_isdst` 为正或零时，会使 `mktime` 初步假定夏令时（例如日光节约时间）对指定时间生效或不生效。`tm_isdst` 为负值时，`mktime` 函数会尝试推测指定时间是否处于夏令时。`tm_isdst` 和 `tm_gmtoff` 成员会被 `timegm` 强制置零。）

成功完成时，结构的 `tm_wday` 和 `tm_yday` 成员被适当设置，其他成员被设置为表示指定的日历时间，但其值被强制限制在正常范围内；`tm_mday` 的最终值在 `tm_mon` 和 `tm_year` 确定之后才会设置。`mktime` 函数返回指定的日历时间；若无法表示该日历时间，则返回 -1 并将 errno(3) 设置为适当的值。

注意 -1 是合法结果（表示 1969 年 12 月 31 日午夜前 1 秒的 UTC 时间），因此不能据此判断成功或失败；应在调用 `mktime` 或 `timegm` 之前将 `tm_wday` 和/或 `tm_yday` 设置为越界值（如 -1），并在调用后检查。

`difftime` 函数返回两个时间值之间的差值（秒），即 `time1` - `time0`。

外部声明以及 `struct tm` 的定义位于以下头文件中：

`#include <time.h>`

`tm` 结构至少包含以下字段：

```sh
int tm_sec;	/* 秒 (0 - 60) */
int tm_min;	/* 分 (0 - 59) */
int tm_hour;	/* 小时 (0 - 23) */
int tm_mday;	/* 月中日期 (1 - 31) */
int tm_mon;	/* 年中月份 (0 - 11) */
int tm_year;	/* 年份 - 1900 */
int tm_wday;	/* 周中日期 (周日 = 0) */
int tm_yday;	/* 年中日期 (0 - 365) */
int tm_isdst;	/* 夏令时是否生效？ */
char *tm_zone;	/* 时区名称缩写 */
long tm_gmtoff;	/* 与 UTC 的偏移量（秒） */
```

若夏令时生效，`tm_isdst` 字段非零。

`tm_gmtoff` 字段表示所表示时间与 UTC 的偏移量（秒），正值表示早于 UTC 的时区（本初子午线以东）。

## 参见

[date(1)](../man1/date.1.md), [clock_gettime(2)](../man2/clock_gettime.2.md), [gettimeofday(2)](../man2/gettimeofday.2.md), [getenv(3)](getenv.3.md), [time(3)](time.3.md), [tzset(3)](tzset.3.md), tzfile(5)

## 标准

`asctime`、`ctime`、`difftime`、`gmtime`、`localtime` 和 `mktime` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")，在所选取的本地时区不包含闰秒表的情况下（参见 zic(8)），也遵循 ISO/IEC 9945-1:1996 ("POSIX.1")。

`asctime_r`、`ctime_r`、`gmtime_r` 和 `localtime_r` 函数预期遵循 ISO/IEC 9945-1:1996 ("POSIX.1")（同样要求所选本地时区不包含闰秒表）。

`timegm` 函数预期遵循 -isoC-2023，约束条件相同。

## 历史

本手册页源自 Arthur Olson 贡献给 Berkeley 的时间包，最早出现在 4.3BSD 中。

`asctime`、`gmtime` 和 `localtime` 函数首次出现于 Version 5 AT&T UNIX，`difftime` 和 `mktime` 出现于 4.3BSD，`timegm` 和 `timelocal` 出现于 SunOS 4.0。

`asctime_r`、`ctime_r`、`gmtime_r` 和 `localtime_r` 函数自 FreeBSD 8.0 起可用。`offtime` 和 `offtime_r` 函数于 FreeBSD 15.0 中引入。

## 缺陷

除 `difftime`、`mktime` 以及其他函数的 `_r` 变体外，这些函数将结果留在内部静态对象中并返回指向该对象的指针。对这些函数的后续调用将修改同一对象。

C 标准未提供程序修改其当前本地时区设置的机制，而 POSIX 标准的方法不可重入。（不过，POSIX 线程环境中提供了线程安全的实现。）

返回的 `tm` 结构中的 `tm_zone` 字段指向静态字符数组，也会被任何后续调用（以及后续对 [tzset(3)](tzset.3.md) 的调用）覆盖。

不鼓励使用外部变量 `tzname`；建议使用 tm 结构中的 `tm_zone` 条目。
