# dtrace_io(4)

`dtrace_io` — 用于跟踪磁盘 I/O 相关事件的 DTrace 提供者

## 名称

`dtrace_io`

## 概要

`Fn io:::start struct bio * struct devstat * Fn io:::done struct bio * struct devstat *`

## 描述

`io` 提供者允许跟踪磁盘 I/O 事件。Fn io:::start 探测在 I/O 请求即将发送到 [disk(9)](../man9/disk.9.md) 对象的后端驱动时触发。这发生在对请求执行所有 GEOM(4) 转换之后。Fn io:::done 探测在 I/O 请求完成时触发。两个探测都接受表示 I/O 请求的 `struct bio *` 作为第一个参数。第二个参数是底层 [disk(9)](../man9/disk.9.md) 对象的 `struct devstat *`。

## 参数

`struct bio` 的字段在 [g_bio(9)](../man9/g_bio.9.md) 手册页中描述，`struct devstat` 的字段在 [devstat(9)](../man9/devstat.9.md) 手册页中描述。`bufinfo_t` 和 `devinfo_t` D 类型的转换器定义在 **/usr/lib/dtrace/io.d** 中。

## 文件

**`/usr/lib/dtrace/io.d`** `io` 提供者的 DTrace 类型和转换器定义。

## 实例

以下脚本按磁盘设备显示每个进程的总 I/O 分解：

```sh
#pragma D option quiet
io:::start
{
        @[args[1]->device_name, execname, pid] = sum(args[0]->bio_length);
}
END
{
        printf("%10s %20s %10s %15sn", "DEVICE", "APP", "PID", "BYTES");
        printa("%10s %20s %10d %15@dn", @);
}
```

## 兼容性

此提供者与 Solaris 中的 `io` 提供者不兼容，因为其探测使用原生 FreeBSD 参数类型。

## 参见

[dtrace(1)](../man1/dtrace.1.md), [devstat(9)](../man9/devstat.9.md), [SDT(9)](../man9/sdt.9.md)

## 历史

`io` 提供者首次出现于 FreeBSD 9.2 和 10.0。

## 作者

本手册页由 Mark Johnston <markj@FreeBSD.org> 编写。

## 缺陷

Fn io:::wait-start 和 Fn io:::wait-done 探测目前在 FreeBSD 上未实现。
