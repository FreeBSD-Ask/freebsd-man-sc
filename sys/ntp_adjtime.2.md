# ntp_adjtime(2)

`ntp_adjtime` — 网络时间协议守护进程（ntpd）接口系统调用

## 名称

`ntp_adjtime`, `ntp_gettime`

## 库

Lb libc

## 概要

`#include <sys/timex.h>`

```c
int
ntp_adjtime(struct timex *);

int
ntp_gettime(struct ntptimeval *);
```

## 描述

`ntp_adjtime()` 和 `ntp_gettime()` 这两个系统调用是内核与网络时间协议（NTP）守护进程 ntpd(8) 之间的接口。

`ntp_adjtime()` 函数供 NTP 守护进程用于将系统时钟调整到外部导出的时间。由 `ntp_adjtime()` 设置的时间偏移和相关变量被 `hardclock()` 用于调整控制系统时钟的相位锁定环或频率锁定环（分别为 PLL 或 FLL）的相位和频率。

`ntp_gettime()` 函数向客户端用户应用程序提供时间、最大误差（同步距离）和估计误差（散布）。

在下文中，所有涉及 PPS 的变量仅在内核中启用 *PPS_SYNC* 选项时才相关。

`ntp_adjtime()` 的参数是一个 `struct timex *`，形式如下：

```c
struct timex {
        unsigned int modes;     /* 时钟模式位（只写） */
        long offset;            /* 时间偏移（微秒）（读写） */
        long freq;              /* 频率偏移（缩放 ppm）（读写） */
        long maxerror;          /* 最大误差（微秒）（读写） */
        long esterror;          /* 估计误差（微秒）（读写） */
        int status;             /* 时钟状态位（读写） */
        long constant;          /* PLL 时间常数（读写） */
        long precision;         /* 时钟精度（微秒）（只读） */
        long tolerance;         /* 时钟频率容差（缩放
                                 * ppm）（只读） */
        /*
         * 以下只读结构成员仅在内核中配置了
         * PPS 信号规范时才实现。
         */
        long ppsfreq;           /* PPS 频率（缩放 ppm）（只读） */
        long jitter;            /* PPS 抖动（微秒）（只读） */
        int shift;              /* 间隔持续时间（秒）（位移）（只读） */
        long stabil;            /* PPS 稳定性（缩放 ppm）（只读） */
        long jitcnt;            /* 抖动超限次数（只读） */
        long calcnt;            /* 校准间隔数（只读） */
        long errcnt;            /* 校准错误数（只读） */
        long stbcnt;            /* 稳定性超限次数（只读） */
};
```

此结构的成员在用作 `ntp_adjtime()` 的参数时具有以下含义：

**`modes`** 定义当前 `ntp_adjtime()` 调用应更改哪些设置（只写）。以下常量的按位或：

- **`MOD_OFFSET`** 设置时间偏移
- **`MOD_FREQUENCY`** 设置频率偏移
- **`MOD_MAXERROR`** 设置最大时间误差
- **`MOD_ESTERROR`** 设置估计时间误差
- **`MOD_STATUS`** 设置时钟状态位
- **`MOD_TIMECONST`** 设置 PLL 时间常数
- **`MOD_CLKA`** 设置时钟 A
- **`MOD_CLKB`** 设置时钟 B

**`offset`** 时间偏移（以微秒为单位），由 PLL/FLL 用于以小增量调整系统时间（读写）。

**`freq`** 频率偏移（缩放 ppm）（读写）。

**`maxerror`** 最大误差（以微秒为单位）。由 `ntp_adjtime()` 调用初始化，内核每秒增加一次以反映最大误差界限的增长（读写）。

**`esterror`** 估计误差（以微秒为单位）。由 `ntp_adjtime()` 设置和读取，但内核不使用（读写）。

**`status`** 系统时钟状态位（读写）。以下常量的按位或：

- **`STA_PLL`** 启用 PLL 更新（读写）。
- **`STA_PPSFREQ`** 启用 PPS 频率规范（读写）。
- **`STA_PPSTIME`** 启用 PPS 时间规范（读写）。
- **`STA_FLL`** 选择频率锁定模式（读写）。
- **`STA_INS`** 插入闰秒（读写）。
- **`STA_DEL`** 删除闰秒（读写）。
- **`STA_UNSYNC`** 时钟未同步（读写）。
- **`STA_FREQHOLD`** 保持频率（读写）。
- **`STA_PPSSIGNAL`** PPS 信号存在（只读）。
- **`STA_PPSJITTER`** PPS 信号抖动超限（只读）。
- **`STA_PPSWANDER`** PPS 信号漂移超限（只读）。
- **`STA_PPSERROR`** PPS 信号校准错误（只读）。
- **`STA_CLOCKERR`** 时钟硬件故障（只读）。

**`constant`** PLL 时间常数，决定 PLL 的带宽或“刚度”（读写）。

**`precision`** 时钟精度（以微秒为单位）。在大多数情况下与内核 tick 变量相同（参见 [hz(9)](../man9/hz.9.md)）。如果有精密时钟计数器或外部计时信号可用，它可能低得多（并取决于信号状态）（只读）。

**`tolerance`** 最大频率误差，或 CPU 时钟振荡器的容差（缩放 ppm）。通常是架构的属性，但在外部计时信号的影响下可能改变（只读）。

**`ppsfreq`** 由频率中值滤波器产生的 PPS 频率偏移（缩放 ppm）（只读）。

**`jitter`** 由时间中值滤波器测量的 PPS 抖动，以微秒为单位（只读）。

**`shift`** 间隔持续时间（以秒为单位）以 2 为底的对数（PPS，只读）。

**`stabil`** PPS 稳定性（缩放 ppm）；由频率中值滤波器测量的散布（漂移）（只读）。

**`jitcnt`** 因时间中值滤波器测量的抖动超过 *MAXTIME* 限制而丢弃的秒数（PPS，只读）。

**`calcnt`** 校准间隔的计数（PPS，只读）。

**`errcnt`** 因漂移超过 *MAXFREQ* 限制或校准间隔抖动超过两个 tick 而丢弃的校准间隔数（PPS，只读）。

**`stbcnt`** 因频率漂移超过 *MAXFREQ*/4 限制而丢弃的校准间隔数（PPS，只读）。

在 `ntp_adjtime()` 调用之后，`struct timex *` 结构包含相应变量的当前值。

`ntp_gettime()` 的参数是一个 `struct ntptimeval *`，包含以下成员：

```c
struct ntptimeval {
        struct timeval time;    /* 当前时间（只读） */
        long maxerror;          /* 最大误差（微秒）（只读） */
        long esterror;          /* 估计误差（微秒）（只读） */
};
```

这些成员具有以下含义：

**`time`** 当前时间（只读）。

**`maxerror`** 最大误差，以微秒为单位（只读）。

**`esterror`** 估计误差，以微秒为单位（只读）。

## 返回值

`ntp_adjtime()` 和 `ntp_gettime()` 成功时返回时钟的当前状态，或返回 [copyin(9)](../man9/copy.9.md) 和 [copyout(9)](../man9/copy.9.md) 的任何错误。如果调用 `ntp_adjtime()` 的用户没有足够的权限，`ntp_adjtime()` 还可能返回 `EPERM`。

时钟的可能状态有：

**`TIME_OK`** 一切正常，无闰秒警告。

**`TIME_INS`** “插入闰秒”警告。在一天结束时，将在 23:59:59 之后插入一个闰秒。

**`TIME_DEL`** “删除闰秒”警告。在一天结束时，将跳过 23:59:59 秒。

**`TIME_OOP`** 闰秒正在进行中。

**`TIME_WAIT`** 闰秒在过去几秒内已发生。

**`TIME_ERROR`** 时钟未同步。

## 错误

`ntp_adjtime()` 系统调用在调用者没有足够权限时可能返回 `EPERM`。

## 参见

options(4), ntpd(8), [hardclock(9)](../man9/hardclock.9.md), [hz(9)](../man9/hz.9.md)

- `http://www.bipm.fr/enus/5_Scientific/c_time/time_1.html`
- `http://www.boulder.nist.gov/timefreq/general/faq.htm`
- `ftp://time.nist.gov/pub/leap-seconds.list`

## 缺陷

请注意，此 API 极其复杂且有状态。用户不应在没有首先深入审查 ntpd(8) 源代码的情况下尝试修改。
