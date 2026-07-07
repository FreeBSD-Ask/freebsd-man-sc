# memory(3)

`aligned_alloc` — 内存管理函数

## 名称

`aligned_alloc`, `alloca`, `calloc`, `free`, `free_sized`, `free_aligned_sized`, `malloc`, `posix_memalign`, `realloc`, `reallocf`, `valloc`, `mmap`, `munmap`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
void *
aligned_alloc(size_t alignment, size_t size);

void *
alloca(size_t size);

void *
calloc(size_t nelem, size_t elsize);

void
free(void *ptr);

void
free_sized(void *ptr, size_t size);

void
free_aligned_sized(void *ptr, size_t alignment, size_t size);

void *
malloc(size_t size);

int
posix_memalign(void **ptr, size_t alignment, size_t size);

void *
realloc(void *ptr, size_t size);

void *
reallocf(void *ptr, size_t size);

void *
valloc(size_t size);
```

`#include <sys/types.h>`

`#include <sys/mman.h>`

```c
void *
mmap(void *addr, size_t len, int prot, int flags, int fd, off_t offset);

int
munmap(void *addr, size_t len);
```

## 描述

这些函数为调用进程分配和释放内存。各函数的说明详见各自的手册页。

## 参见

mmap(2), aligned_alloc(3), alloca(3), calloc(3), free(3), free_aligned_sized(3), [free_sized(3)](free_sized.3.md), malloc(3), posix_memalign(3), realloc(3), [reallocf(3)](reallocf.3.md), valloc(3)

## 标准

`calloc`、`free`、`malloc` 和 `realloc` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。

`mmap`、`munmap` 和 `posix_memalign` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")。

`free_sized` 和 `free_aligned_sized` 函数遵循 ISO/IEC 9899:2023 ("ISO C23")。
