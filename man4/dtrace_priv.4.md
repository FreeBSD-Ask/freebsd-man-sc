# dtrace_priv(4)

`dtrace_priv` — 用于内核权限检查 API 的 DTrace 提供者

## 名称

`dtrace_priv`

## 概要

`priv:kernel:priv_check:priv-ok priv:kernel:priv_check:priv-err`

## 描述

`priv` 提供者允许跟踪 [priv(9)](../man9/priv.9.md) API。

`priv`:kernel:priv_check:priv-ok 探测在内核权限检查成功时触发。

`priv`:kernel:priv_check:priv-err 探测在内核权限检查失败时触发。

`priv` 探测的唯一参数 `args[0]` 是所请求的权限编号 Ft int priv。

## 实例

### 实例 1：跟踪内核权限检查失败

以下脚本捕获一个计数器数组，每个计数器对应一条导致内核权限检查失败的栈回溯：

```sh
priv:::priv-err
{
	@traces[stack()] = count();
}
```

## 参见

[dtrace(1)](../man1/dtrace.1.md), [tracing(7)](../man7/tracing.7.md), [priv(9)](../man9/priv.9.md), [SDT(9)](../man9/sdt.9.md)

## 作者

`priv` 提供者由 Robert N. M. Watson <rwatson@FreeBSD.org> 编写。

本手册页由 Mateusz Piotrowski <0mp@FreeBSD.org> 编写。
