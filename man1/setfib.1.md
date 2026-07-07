# setfib(1)

`setfib` — 以更改的默认网络视图执行实用程序

## 名称

`setfib`

## 概要

`setfib [-F] fib utility [argument ...]`

## 描述

`setfib` 实用程序使用不同的路由表运行另一个 `utility`。表号 `fib` 将默认用于此进程及其后代启动的所有套接字。

## 环境变量

如果名称不包含 `/` 字符，`PATH` 环境变量用于定位请求的 `utility`。

## 退出状态

如果调用了 `utility`，`setfib` 的退出状态就是 `utility` 的退出状态。

退出状态 126 表示找到了 `utility`，但无法执行。退出状态 127 表示找不到 `utility`。

## 实例

运行 [netstat(1)](netstat.1.md) 查看第二个路由表。

```sh
setfib -F 1 netstat -rn
```

或

```sh
setfib 1 netstat -rn
```

或

```sh
setfib -1 netstat -rn
```

## 参见

[setfib(2)](../sys/setfib.2.md), setsockopt(2)

## 标准

`setfib` 实用程序是 FreeBSD 特有的扩展。但是，许多类 UNIX 系统具有等效的功能。

## 历史

`setfib` 实用程序出现在 FreeBSD 7.1 中。
