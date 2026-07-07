# vm_map_lock(9)

`vm_map_lock`, `vm_map_unlock`, `vm_map_lock_read`, `vm_map_unlock_read`, `vm_map_trylock`, `vm_map_trylock_read`, `vm_map_lock_upgrade`, `vm_map_lock_downgrade` — vm_map 加锁宏

## 名称

`vm_map_lock`, `vm_map_unlock`, `vm_map_lock_read`, `vm_map_unlock_read`, `vm_map_trylock`, `vm_map_trylock_read`, `vm_map_lock_upgrade`, `vm_map_lock_downgrade`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_map.h>

void
vm_map_lock(vm_map_t map)

void
vm_map_unlock(vm_map_t map)

void
vm_map_lock_read(vm_map_t map)

void
vm_map_unlock_read(vm_map_t map)

int
vm_map_trylock(vm_map_t map)

int
vm_map_trylock_read(vm_map_t map)

int
vm_map_lock_upgrade(vm_map_t map)

int
vm_map_lock_downgrade(vm_map_t map)
```

## 描述

`vm_map_lock` 宏获取 `map` 上的独占锁。

`vm_map_unlock` 宏释放 `map` 上的独占锁。

`vm_map_lock_read` 宏获取 `map` 上的读锁。

`vm_map_unlock_read` 宏释放 `map` 上的读锁。

`vm_map_trylock` 宏尝试获取 `map` 上的独占锁。如果无法立即获取锁，则返回 `FALSE`；否则获取锁并返回 `TRUE`。

`vm_map_trylock_read` 宏尝试获取 `map` 上的读锁。如果无法立即获取锁，则返回 `FALSE`；否则获取锁并返回 `TRUE`。

`vm_map_lock_upgrade` 宏尝试原子地将 `map` 上的读锁升级为独占锁。

`vm_map_lock_downgrade` 宏尝试将 `map` 上的独占锁降级为读锁。

## 实现说明

目前，所有的加锁宏都将其锁实现为睡眠锁。

## 参见

[vm_map(9)](vm_map.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
