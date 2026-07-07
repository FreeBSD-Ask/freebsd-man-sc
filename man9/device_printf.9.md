# device_printf(9)

`device_printf` — 格式化输出转换

## 名称

`device_printf`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

int
device_printf(device_t dev, const char *fmt, ...);
```

## 描述

`device_printf` 函数是 [printf(9)](printf.9.md) 函数的便捷接口。它先输出 `dev` 设备的名称，后跟一个冒号和一个空格，然后输出将 `fmt` 及其余参数传递给 [printf(9)](printf.9.md) 时所会打印的内容。

## 返回值

`device_printf` 函数返回显示的字符数。

## 参见

[printf(3)](../stdio/printf.3.md), [printf(9)](printf.9.md)
