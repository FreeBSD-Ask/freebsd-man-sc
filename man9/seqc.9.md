# seqc(9)

`seqc_consistent` — 无锁读算法

## 名称

`seqc_consistent`, `seqc_read`, `seqc_write_begin`, `seqc_write_end`

## 概要

```c
#include <sys/seqc.h>
```

```c
void
seqc_write_begin(seqc_t *seqcp)

void
seqc_write_end(seqc_t *seqcp)

seqc_t
seqc_read(seqc_t *seqcp)

seqc_t
seqc_consistent(const seqc_t *seqcp, seqc_t oldseqc)
```

## 描述

`seqc` 允许零个或多个读者和零个或一个写者并发访问对象，为读者提供对象的一致快照。读者和写者之间不需要互斥，但读者可能会被写者无限期地饿死。

`seqc_write_begin` 和 `seqc_write_end` 函数用于为写者创建事务，并通知读者对象将被修改。

`seqc_read` 函数返回当前序列号。如果写者已启动事务，此函数将自旋直到事务结束。

`seqc_consistent` 函数将序列号与先前获取的值进行比较。`oldseqc` 变量应包含读事务开始时的序列号。

读者在事务结束时检查序列号是否已更改。如果序列号未更改，则对象未被修改，获取的变量有效。如果序列号已更改，则对象已被修改，应重复获取。如果序列号为奇数，则对象更改正在进行中，读者将等待直到写操作使序列号变为偶数。

## 实例

以下写者示例更改 `obj` 结构中的 `var1` 和 `var2` 变量：

```c
lock_exclusive(&obj->lock);
seqc_write_begin(&obj->seqc);
obj->var1 = 1;
obj->var2 = 2;
seqc_write_end(&obj->seqc);
unlock_exclusive(&obj->lock);
```

以下读者示例从 `obj` 结构中读取 `var1` 和 `var2` 变量。如果序列号已更改，则重新开始整个过程。

```c
int var1, var2;
seqc_t seqc;
for (;;) {
	seqc = seqc_read(&obj->seqc);
	var1 = obj->var1;
	var2 = obj->var2;
	if (seqc_consistent(&obj->seqc, seqc))
		break;
}
```

## 作者

`seqc` 函数由 Mateusz Guzik <mjg@FreeBSD.org> 实现。本手册页由 Mariusz Zaborski <oshogbo@FreeBSD.org> 编写。

## 注意事项

不保证读者会有进展。当有大量写者时，读者可能会被饿死。可以通过在几次尝试后返回错误来解决此问题。

理论上，如果读取耗时很长，且有许多写者，计数器可能会溢出并绕回到相同的值。在这种情况下，读者将不会注意到对象已被更改。鉴于这需要在单个争用的读者上进行 40 亿次事务写入，这种情况不太可能发生。可以通过扩展接口以允许 64 位计数器来避免此问题。
