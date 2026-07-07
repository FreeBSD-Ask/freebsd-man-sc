# reallocarray(3)

`reallocarray` — 内存重新分配函数

## 名称

`reallocarray`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
void *
reallocarray(void *ptr, size_t nmemb, size_t size);

void *
recallocarray(void *ptr, size_t oldnmemb, size_t nmemb, size_t size);
```

## 描述

`reallocarray` 函数类似于 `realloc` 函数，区别在于它对 `nmemb` 个大小为 `size` 的成员进行操作，并检查计算 `nmemb` * `size` 时是否发生整数溢出。

`recallocarray` 函数类似于 `reallocarray` 函数，区别在于它确保新分配的内存被清零，类似于 `calloc`。若 `ptr` 为 `NULL`，则忽略 `oldnmemb`，该调用等价于 `calloc`。若 `ptr` 不为 `NULL`，`oldnmemb` 必须为一个使得 `oldnmemb` * `size` 等于返回 `ptr` 的先前分配大小的值，否则行为未定义。

## 返回值

`reallocarray` 函数返回指向已分配空间的指针；否则返回 `NULL` 指针，并将 `errno` 设置为 `ENOMEM`。

## 实例

当 `malloc` 或 `realloc` 的 `size` 参数中包含乘法运算时，应考虑使用 `reallocarray`。例如，避免使用以下常见写法，因为它可能导致整数溢出：

```c
if ((p = malloc(num * size)) == NULL)
	err(1, "malloc");
```

可直接替换为 OpenBSD 扩展 `reallocarray`：

```c
if ((p = reallocarray(NULL, num, size)) == NULL)
	err(1, "reallocarray");
```

使用 `realloc` 时，注意避免以下写法：

```c
size += 50;
if ((p = realloc(p, size)) == NULL)
	return (NULL);
```

在分配成功之前，不要调整描述已分配内存大小的变量。若使用了不正确的尺寸值，可能导致程序行为异常。在大多数情况下，上述示例还会导致内存泄漏。如前所述，返回值为 `NULL` 表示旧对象仍处于已分配状态。更好的代码如下：

```c
newsize = size + 50;
if ((newp = realloc(p, newsize)) == NULL) {
	free(p);
	p = NULL;
	size = 0;
	return (NULL);
}
p = newp;
size = newsize;
```

与 `malloc` 一样，务必确保新的尺寸值不会溢出；即避免如下分配：

```c
if ((newp = realloc(p, num * size)) == NULL) {
	...
```

应改用 `reallocarray`：

```c
if ((newp = reallocarray(p, num, size)) == NULL) {
	...
```

## 参见

realloc(3)

## 标准

`reallocarray` 遵循 IEEE Std 1003.1-2024 ("POSIX.1")。

## 历史

`reallocarray` 函数首次出现于 OpenBSD 5.6 和 FreeBSD 11.0。`recallocarray` 函数首次出现于 OpenBSD 6.1 和 FreeBSD 15.1。
