# cnv(9)

`cnv` — 通过 cookie 管理名称/值对的 API

## 名称

`cnvlist_get`, `cnvlist_take`, `cnvlist_free`

## 库

libnv

## 概要

```c
#include <sys/cnv.h>

const char *
cnvlist_name(const void *cookie)

int
cnvlist_type(const void *cookie)

bool
cnvlist_get_bool(const void *cookie)

uint64_t
cnvlist_get_number(const void *cookie)

const char *
cnvlist_get_string(const void *cookie)

const nvlist_t *
cnvlist_get_nvlist(const void *cookie)

const void *
cnvlist_get_binary(const void *cookie, size_t *sizep)

const bool *
cnvlist_get_bool_array(const void *cookie, size_t *nitemsp)

const uint64_t *
cnvlist_get_number_array(const void *cookie, size_t *nitemsp)

const char * const *
cnvlist_get_string_array(const void *cookie, size_t *nitemsp)

const nvlist_t * const *
cnvlist_get_nvlist_array(const void *cookie, size_t *nitemsp)

int
cnvlist_get_descriptor(const void *cookie)

const int *
cnvlist_get_descriptor_array(const void *cookie, size_t *nitemsp)

bool
cnvlist_take_bool(void *cookie)

uint64_t
cnvlist_take_number(void *cookie)

const char *
cnvlist_take_string(void *cookie)

const nvlist_t *
cnvlist_take_nvlist(void *cookie)

const void *
cnvlist_take_binary(void *cookie, size_t *sizep)

const bool *
cnvlist_take_bool_array(void *cookie, size_t *nitemsp)

const uint64_t *
cnvlist_take_number_array(void *cookie, size_t *nitemsp)

const char * const *
cnvlist_take_string_array(void *cookie, size_t *nitemsp)

const nvlist_t * const *
cnvlist_take_nvlist_array(void *cookie, size_t *nitemsp)

int
cnvlist_take_descriptor(void *cookie)

const int *
cnvlist_take_descriptor_array(void *cookie, size_t *nitemsp)

void
cnvlist_free_null(void *cookie)

void
cnvlist_free_bool(void *cookie)

void
cnvlist_free_number(void *cookie)

void
cnvlist_free_string(void *cookie)

void
cnvlist_free_nvlist(void *cookie)

void
cnvlist_free_descriptor(void *cookie)

void
cnvlist_free_binary(void *cookie)

void
cnvlist_free_bool_array(void *cookie)

void
cnvlist_free_number_array(void *cookie)

void
cnvlist_free_string_array(void *cookie)

void
cnvlist_free_nvlist_array(void *cookie)

void
cnvlist_free_descriptor_array(void *cookie)
```

## 描述

`libnv` 库允许轻松管理名称/值对，并可通过套接字发送和接收它们。更多信息，请参见 [nv(9)](nv.9.md)。

cookie 的概念在 [nv(9)](nv.9.md) 的 `nvlist_next`、`nvlist_get_parent` 和 `nvlist_get_pararr` 中解释。

`cnvlist_name` 函数返回与 `cookie` 关联的元素名称。

`cnvlist_type` 函数返回与 `cookie` 关联的元素类型。可返回的类型在 [nv(9)](nv.9.md) 中描述。

`cnvlist_get` 函数返回与 `cookie` 关联的值。返回的字符串、nvlist、描述符、二进制数据或数组不得被用户修改，因为它们仍属于 nvlist。nvlist 不得处于错误状态。

`cnvlist_take` 函数返回与给定 cookie 关联的值，并从 nvlist 中移除该元素。当值为字符串、二进制数据或数组值时，调用者负责使用 [free(3)](../man3/free.3.md) 释放返回的内存。当值为 nvlist 时，调用者负责使用 `nvlist_destroy` 销毁返回的 nvlist。当值为描述符时，调用者负责使用 [close(2)](../man2/close.2.md) 关闭返回的描述符。

`cnvlist_free` 函数移除由 `cookie` 标识的元素并释放任何关联资源。如果由 `cookie` 标识的元素类型错误或不存在，程序将中止。

## 实例

以下示例演示如何使用 cnvlist API。

```c
int type;
void *cookie, *scookie, *bcookie;
nvlist_t *nvl;
char *name;

nvl = nvlist_create(0);
nvlist_add_bool(nvl, "test", 1 == 2);
nvlist_add_string(nvl, "test2", "cnvlist");
cookie = NULL;

while (nvlist_next(nvl, &type, &cookie) != NULL) {
        switch (type) {
        case NV_TYPE_BOOL:
                printf("test: %d\n", cnvlist_get_bool(cookie));
                bcookie = cookie;
                break;
        case NV_TYPE_STRING:
                printf("test2: %s\n", cnvlist_get_string(cookie));
                scookie = cookie;
                break;
        }
}

name = cnvlist_take_string(scookie);
cnvlist_free_bool(bcookie);

printf("test2: %s\n", name);
free(name);

printf("nvlist_empty = %d\n", nvlist_empty(nvl));
nvlist_destroy(nvl);

return (0);
```

## 参见

[close(2)](../man2/close.2.md), [free(3)](../man3/free.3.md), [nv(9)](nv.9.md)

## 作者

`cnv` API 由 Adam Starak 在 Google Summer Of Code 2016 期间创建。
