# fail.9

`DEBUG_FP` — 故障点

## 名称

`DEBUG_FP`, `KFAIL_POINT_CODE`, `KFAIL_POINT_CODE_FLAGS`, `KFAIL_POINT_CODE_COND`, `KFAIL_POINT_ERROR`, `KFAIL_POINT_EVAL`, `KFAIL_POINT_DECLARE`, `KFAIL_POINT_DEFINE`, `KFAIL_POINT_GOTO`, `KFAIL_POINT_RETURN`, `KFAIL_POINT_RETURN_VOID`, `KFAIL_POINT_SLEEP_CALLBACKS`, `fail_point`

## 概要

```c
#include <sys/fail.h>

KFAIL_POINT_CODE(parent, name, code)
KFAIL_POINT_CODE_FLAGS(parent, name, flags, code)
KFAIL_POINT_CODE_COND(parent, name, cond, flags, code)
KFAIL_POINT_ERROR(parent, name, error_var)
KFAIL_POINT_EVAL(name, code)
KFAIL_POINT_DECLARE(name)
KFAIL_POINT_DEFINE(parent, name, flags)
KFAIL_POINT_GOTO(parent, name, error_var, label)
KFAIL_POINT_RETURN(parent, name)
KFAIL_POINT_RETURN_VOID(parent, name)
KFAIL_POINT_SLEEP_CALLBACKS(parent, name, pre_func, pre_arg, post_func,
    post_arg, code)
```

## 描述

故障点用于添加代码点，使得错误可以按用户控制的方式注入。故障点为用户提供的错误注入代码提供了便捷的包装，并提供一个 [sysctl(9)](sysctl.9.md) MIB，以及一个解析该 MIB 的解析器，描述错误注入代码应如何触发。

基础的故障点宏是 `KFAIL_POINT_CODE`，其中 `parent` 是 sysctl 树（内核故障点通常为 `DEBUG_FP`，但各子系统可能希望提供自己的故障点树），`name` 是该树中 MIB 的名称，`code` 是错误注入代码。`code` 参数不需要花括号，但对于任何多行代码参数，使用花括号被视为良好的风格。在 `code` 参数内部，`RETURN_VALUE` 的求值源自 sysctl MIB 中设置的返回值。

此外，`KFAIL_POINT_CODE_FLAGS` 提供了一个 `flags` 参数，用于控制故障点的行为。例如，可用于将故障点的上下文标记为不可休眠，从而使 `sleep` 动作被强制为忙等待。支持的标志有：

**`FAIL_POINT_USE_TIMEOUT_PATH`** 不在 `sleep` 调用上休眠，而是在超时触发后执行休眠后函数。

**`FAIL_POINT_NONSLEEPABLE`** 将故障点标记为处于不可休眠上下文中，将 `sleep` 调用强制为 `delay` 调用。

同样，`KFAIL_POINT_CODE_COND` 提供了一个 `cond` 参数，允许设置故障点代码可能触发的条件。这等价于：

```c
if (cond)
    KFAIL_POINT_CODE_FLAGS(...);
```

参见下文的 SYSCTL 变量。

其余 `KFAIL_POINT_*` 宏是常见错误注入路径的包装：

**`KFAIL_POINT_RETURN`**(*parent*, *name*) 等价于 `KFAIL_POINT_CODE(..., return RETURN_VALUE)`

**`KFAIL_POINT_RETURN_VOID`**(*parent*, *name*) 等价于 `KFAIL_POINT_CODE(..., return)`

**`KFAIL_POINT_ERROR`**(*parent*, *name*, *error_var*) 等价于 `KFAIL_POINT_CODE(..., error_var = RETURN_VALUE)`

**`KFAIL_POINT_GOTO`**(*parent*, *name*, *error_var*, *label*) 等价于 `KFAIL_POINT_CODE(..., { error_var = RETURN_VALUE; goto label;})`

你也可以通过分离声明、定义和求值部分来引入故障点。

**`KFAIL_POINT_DECLARE`**(*name*) 用于声明 `fail_point` 结构。

**`KFAIL_POINT_DEFINE`**(*parent*, *name*, *flags*) 定义并初始化 `fail_point`，并设置其 [sysctl(9)](sysctl.9.md)。

**`KFAIL_POINT_EVAL`**(*name*, *code*) 在故障点执行处使用。

## SYSCTL 变量

`KFAIL_POINT_*` 宏在指定位置添加 sysctl MIB。许多基础内核 MIB 可在 `debug.fail_point` 树中找到（在代码中通过 `DEBUG_FP` 引用）。

sysctl 变量可以多种方式设置：

```sh
[<pct>%][<cnt>*]<type>[(args...)][-><more terms>]
```

`<type>` 参数指定要采取的动作；可以是以下之一：

**`off`** 不采取动作（不触发故障点代码）

**`return`** 以指定参数触发故障点代码

**`sleep`** 休眠指定的毫秒数

**`panic`** 内核崩溃

**`break`** 进入调试器，若无调试器支持则触发陷阱

**`print`** 打印故障点已执行

**`pause`** 线程在故障点休眠，直到故障点被设置为 `off`

**`yield`** 故障点求值时线程让出 CPU

**`delay`** 类似于 sleep，但忙等待 CPU。（适用于不可休眠上下文。）

`<type>` 之前的 `<pct>%` 和 `<cnt>*` 修饰符控制 `<type>` 何时执行。`<pct>%` 形式（例如“1.2%”）可用于指定 `<type>` 执行的概率。这是范围 (0, 100] 内的十进制数，可指定高达 1/10,000% 的精度。`<cnt>*` 形式（例如“5\*”）可用于指定 `<type>` 应执行的次数，之后该 `<term>` 被禁用。如果指定了多个，仅使用最后一个概率和最后一个计数，即“1.2%2%”等同于“2%”。当同时指定概率和计数时，概率先于计数求值，即“2%5\*”意为“2% 的时间，但总共最多 5 次”。

运算符 -> 可用于表达级联项。如果指定 `<term1>-><term2>`，意味着如果 `<term1>` 未 `execute`，则求值 `<term2>`。就此运算符而言，`return` 和 `print` 运算符是仅有的会级联的类型。`return` 项仅在代码执行时级联，`print` 项仅在传入非零参数时级联。可选择性地指定 pid。故障点项仅在由具有匹配 `p_pid` 的进程调用时执行。

## 实例

**`sysctl debug.fail_point.foobar="2.1%return(5)"`** 21/1000 的概率，执行 `code`，RETURN_VALUE 设置为 5。

**`sysctl debug.fail_point.foobar="2%return(5)->5%return(22)"`** 2/100 的概率，执行 `code`，RETURN_VALUE 设置为 5。如果未发生，则 5% 的概率执行 `code`，RETURN_VALUE 设置为 22。

**`sysctl debug.fail_point.foobar="5*return(5)->0.1%return(22)"`** 5 次返回 5。之后，1/1000 的概率返回 22。

**`sysctl debug.fail_point.foobar="0.1%5*return(5)"`** 每 1000 次执行中返回 5 一次，但总共最多 5 次。

**`sysctl debug.fail_point.foobar="1%*sleep(50)"`** 1/100 的概率，休眠 50ms。

**`sysctl debug.fail_point.foobar="1*return(5)[pid 1234]"`** 当 pid 1234 执行故障点时返回 5 一次。

## 作者

本手册页由以下人员编写：

Matthew Bryan <matthew.bryan@isilon.com> 和

Zach Loafman <zml@FreeBSD.org>。

## 注意事项

过于激进地设置故障点或组合设置过多故障点，很容易弄巧成拙。例如，强制 `malloc` 持续失败可能对系统正常运行时间有害。

`sleep` sysctl 设置可能并非在所有情况下都合适。目前，`fail_point_eval` 不验证上下文是否适合调用 `msleep`。你可以通过在故障点声明处指定 `FAIL_POINT_NONSLEEPABLE` 标志，强制将 `sleep` 动作求值为 `delay` 动作。
