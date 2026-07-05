# autofs.4

`autofs` — 自动挂载文件系统

## 名称

`autofs`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> options AUTOFS

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
autofs_load="YES"
```

## 描述

`autofs` 驱动是自动挂载器基础设施的内核组件。其工作是将挂载请求传递给 automountd(8) 守护进程，并暂停尝试访问自动挂载文件系统的进程，直到挂载完成。它由 automount(8) 进行挂载。

## 选项

挂载 `autofs` 文件系统时可使用以下选项：

**`master_options`** 映射条目中指定的所有文件系统的挂载选项。

**`master_prefix`** 文件系统挂载点前缀。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`vfs.autofs.debug`** `autofs` 驱动日志消息的详细级别。设置为 0 可禁用日志记录，设置为 1 可对潜在问题发出警告。更大的值启用调试输出。默认为 1。

**`vfs.autofs.interruptible`** 设置为 1 可允许挂载请求被信号中断。默认为 1。

**`vfs.autofs.retry_delay`** 重试挂载请求前等待的秒数。默认为 1。

**`vfs.autofs.retry_attempts`** 挂载失败前的尝试次数。默认为 3。

**`vfs.autofs.cache`** 为任意给定文件或目录再次调用 automountd(8) 前等待的秒数。默认为 600。

**`vfs.autofs.timeout`** 等待 automountd(8) 处理挂载请求的秒数。默认为 30。

**`vfs.autofs.mount_on_stat`** 设置为 1 可在挂载点上 stat(2) 时触发挂载。默认为 0。

## 实例

卸载所有已挂载的 `autofs` 文件系统：

```sh
umount -At autofs
```

挂载 auto_master(5) 中指定的 `autofs` 文件系统：

```sh
automount
```

## 参见

auto_master(5), automount(8), automountd(8), [autounmountd(8)](../man8/autounmountd.8.md)

## 历史

`autofs` 驱动首次出现于 FreeBSD 10.1。

## 作者

`autofs` 由 Edward Tomasz Napierala <trasz@FreeBSD.org> 在 FreeBSD 基金会赞助下开发。
