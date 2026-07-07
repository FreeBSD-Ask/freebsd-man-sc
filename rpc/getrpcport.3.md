# getrpcport(3)

`getrpcport` — 获取 RPC 端口号

## 名称

`getrpcport`

## 库

Lb libc

## 概要

```c
int
getrpcport(char *host, int prognum, int versnum, int proto);
```

## 描述

`getrpcport` 函数返回在 `host` 上运行并使用协议 `proto` 的 RPC 程序 `prognum` 的 `versnum` 版本的端口号。如果无法联系 portmapper，或者 `prognum` 未注册，则返回 0。如果 `prognum` 已注册但不是 `versnum` 版本，仍会返回一个端口号（对应程序的某个版本），表明该程序确实已注册。版本不匹配将在首次调用服务时被检测到。
