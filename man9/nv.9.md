# nv.9.md

`nvlist_create` — 名称/值对库

## 名称

`nvlist_create`, `nvlist_destroy`, `nvlist_error`, `nvlist_set_error`, `nvlist_empty`, `nvlist_flags`, `nvlist_exists`, `nvlist_free`, `nvlist_clone`, `nvlist_dump`, `nvlist_fdump`, `nvlist_size`, `nvlist_pack`, `nvlist_unpack`, `nvlist_send`, `nvlist_recv`, `nvlist_xfer`, `nvlist_in_array`, `nvlist_next`, `nvlist_add`, `nvlist_move`, `nvlist_get`, `nvlist_take`, `nvlist_append`

## 库

libnv

## 概要

```c
#include <sys/nv.h>
```

```c
nvlist_t *
nvlist_create(int flags)

void
nvlist_destroy(nvlist_t *nvl)

int
nvlist_error(const nvlist_t *nvl)

void
nvlist_set_error(nvlist_t *nvl, int error)

bool
nvlist_empty(const nvlist_t *nvl)

int
nvlist_flags(const nvlist_t *nvl)

bool
nvlist_in_array(const nvlist_t *nvl)

nvlist_t *
nvlist_clone(const nvlist_t *nvl)

void
nvlist_dump(const nvlist_t *nvl, int fd)

void
nvlist_fdump(const nvlist_t *nvl, FILE *fp)

size_t
nvlist_size(const nvlist_t *nvl)

void *
nvlist_pack(const nvlist_t *nvl, size_t *sizep)

nvlist_t *
nvlist_unpack(const void *buf, size_t size, int flags)

int
nvlist_send(int sock, const nvlist_t *nvl)

nvlist_t *
nvlist_recv(int sock, int flags)

nvlist_t *
nvlist_xfer(int sock, nvlist_t *nvl, int flags)

const char *
nvlist_next(const nvlist_t *nvl, int *typep, void **cookiep)

bool
nvlist_exists(const nvlist_t *nvl, const char *name)

bool
nvlist_exists_type(const nvlist_t *nvl, const char *name, int type)

bool
nvlist_exists_null(const nvlist_t *nvl, const char *name)

bool
nvlist_exists_bool(const nvlist_t *nvl, const char *name)

bool
nvlist_exists_number(const nvlist_t *nvl, const char *name)

bool
nvlist_exists_string(const nvlist_t *nvl, const char *name)

bool
nvlist_exists_nvlist(const nvlist_t *nvl, const char *name)

bool
nvlist_exists_descriptor(const nvlist_t *nvl, const char *name)

bool
nvlist_exists_binary(const nvlist_t *nvl, const char *name)

bool
nvlist_exists_bool_array(const nvlist_t *nvl, const char *name)

bool
nvlist_exists_number_array(const nvlist_t *nvl, const char *name)

bool
nvlist_exists_string_array(const nvlist_t *nvl, const char *name)

bool
nvlist_exists_nvlist_array(const nvlist_t *nvl, const char *name)

bool
nvlist_exists_descriptor_array(const nvlist_t *nvl, const char *name)

void
nvlist_add_null(nvlist_t *nvl, const char *name)

void
nvlist_add_bool(nvlist_t *nvl, const char *name, bool value)

void
nvlist_add_number(nvlist_t *nvl, const char *name, uint64_t value)

void
nvlist_add_string(nvlist_t *nvl, const char *name, const char *value)

void
nvlist_add_stringf(nvlist_t *nvl, const char *name, const char *valuefmt, ...)

void
nvlist_add_stringv(nvlist_t *nvl, const char *name, const char *valuefmt, va_list valueap)

void
nvlist_add_nvlist(nvlist_t *nvl, const char *name, const nvlist_t *value)

void
nvlist_add_descriptor(nvlist_t *nvl, const char *name, int value)

void
nvlist_add_binary(nvlist_t *nvl, const char *name, const void *value, size_t size)

void
nvlist_add_bool_array(nvlist_t *nvl, const char *name, const bool *value, size_t nitems)

void
nvlist_add_number_array(nvlist_t *nvl, const char *name, const uint64_t *value, size_t nitems)

void
nvlist_add_string_array(nvlist_t *nvl, const char *name, const char * const *value, size_t nitems)

void
nvlist_add_nvlist_array(nvlist_t *nvl, const char *name, const nvlist_t * const *value, size_t nitems)

void
nvlist_add_descriptor_array(nvlist_t *nvl, const char *name, const int *value, size_t nitems)

void
nvlist_move_string(nvlist_t *nvl, const char *name, char *value)

void
nvlist_move_nvlist(nvlist_t *nvl, const char *name, nvlist_t *value)

void
nvlist_move_descriptor(nvlist_t *nvl, const char *name, int value)

void
nvlist_move_binary(nvlist_t *nvl, const char *name, void *value, size_t size)

void
nvlist_move_bool_array(nvlist_t *nvl, const char *name, bool *value, size_t nitems)

void
nvlist_move_number_array(nvlist_t *nvl, const char *name, uint64_t *value, size_t nitems)

void
nvlist_move_string_array(nvlist_t *nvl, const char *name, char **value, size_t nitems)

void
nvlist_move_nvlist_array(nvlist_t *nvl, const char *name, nvlist_t **value, size_t nitems)

void
nvlist_move_descriptor_array(nvlist_t *nvl, const char *name, int *value, size_t nitems)

bool
nvlist_get_bool(const nvlist_t *nvl, const char *name)

uint64_t
nvlist_get_number(const nvlist_t *nvl, const char *name)

const char *
nvlist_get_string(const nvlist_t *nvl, const char *name)

const nvlist_t *
nvlist_get_nvlist(const nvlist_t *nvl, const char *name)

int
nvlist_get_descriptor(const nvlist_t *nvl, const char *name)

const void *
nvlist_get_binary(const nvlist_t *nvl, const char *name, size_t *sizep)

const bool *
nvlist_get_bool_array(const nvlist_t *nvl, const char *name, size_t *nitems)

const uint64_t *
nvlist_get_number_array(const nvlist_t *nvl, const char *name, size_t *nitems)

const char * const *
nvlist_get_string_array(const nvlist_t *nvl, const char *name, size_t *nitems)

const nvlist_t * const *
nvlist_get_nvlist_array(const nvlist_t *nvl, const char *name, size_t *nitems)

const int *
nvlist_get_descriptor_array(const nvlist_t *nvl, const char *name, size_t *nitems)

const nvlist_t *
nvlist_get_parent(const nvlist_t *nvl, void **cookiep)

const nvlist_t *
nvlist_get_array_next(const nvlist_t *nvl)

const nvlist_t *
nvlist_get_pararr(const nvlist_t *nvl, void **cookiep)

bool
nvlist_take_bool(nvlist_t *nvl, const char *name)

uint64_t
nvlist_take_number(nvlist_t *nvl, const char *name)

char *
nvlist_take_string(nvlist_t *nvl, const char *name)

nvlist_t *
nvlist_take_nvlist(nvlist_t *nvl, const char *name)

int
nvlist_take_descriptor(nvlist_t *nvl, const char *name)

void *
nvlist_take_binary(nvlist_t *nvl, const char *name, size_t *sizep)

bool *
nvlist_take_bool_array(nvlist_t *nvl, const char *name, size_t *nitems)

uint64_t **
nvlist_take_number_array(nvlist_t *nvl, const char *name, size_t *nitems)

char **
nvlist_take_string_array(nvlist_t *nvl, const char *name, size_t *nitems)

nvlist_t **
nvlist_take_nvlist_array(nvlist_t *nvl, const char *name, size_t *nitems)

int *
nvlist_take_descriptor_array(nvlist_t *nvl, const char *name, size_t *nitems)

void
nvlist_append_bool_array(nvlist_t *nvl, const char *name, const bool value)

void
nvlist_append_number_array(nvlist_t *nvl, const char *name, const uint64_t value)

void
nvlist_append_string_array(nvlist_t *nvl, const char *name, const char * const value)

void
nvlist_append_nvlist_array(nvlist_t *nvl, const char *name, const nvlist_t * const value)

void
nvlist_append_descriptor_array(nvlist_t *nvl, const char *name, int value)

void
nvlist_free(nvlist_t *nvl, const char *name)

void
nvlist_free_type(nvlist_t *nvl, const char *name, int type)

void
nvlist_free_null(nvlist_t *nvl, const char *name)

void
nvlist_free_bool(nvlist_t *nvl, const char *name)

void
nvlist_free_number(nvlist_t *nvl, const char *name)

void
nvlist_free_string(nvlist_t *nvl, const char *name)

void
nvlist_free_nvlist(nvlist_t *nvl, const char *name)

void
nvlist_free_descriptor(nvlist_t *nvl, const char *name)

void
nvlist_free_binary(nvlist_t *nvl, const char *name)

void
nvlist_free_bool_array(nvlist_t *nvl, const char *name)

void
nvlist_free_number_array(nvlist_t *nvl, const char *name)

void
nvlist_free_string_array(nvlist_t *nvl, const char *name)

void
nvlist_free_nvlist_array(nvlist_t *nvl, const char *name)

void
nvlist_free_descriptor_array(nvlist_t *nvl, const char *name)
```

## 描述

`libnv` 库允许创建和管理名称/值对，以及通过套接字发送和接收它们。一组名称/值对称为 `nvlist`。API 支持以下数据类型的值：

**null ( NV_TYPE_NULL)** 名称没有关联的数据。

**bool ( NV_TYPE_BOOL)** 值可以是 `true` 或 `false`。

**number ( NV_TYPE_NUMBER)** 值是以 `uint64_t` 存储的数字。

**string ( NV_TYPE_STRING)** 值是 C 字符串。

**nvlist ( NV_TYPE_NVLIST)** 值是嵌套的 nvlist。

**descriptor ( NV_TYPE_DESCRIPTOR)** 值是文件描述符。注意，文件描述符只能通过 [unix(4)](../man4/unix.4.md) 域套接字发送。

**binary ( NV_TYPE_BINARY)** 值是二进制缓冲区。

**bool array ( NV_TYPE_BOOL_ARRAY)** 值是布尔值数组。

**number array ( NV_TYPE_NUMBER_ARRAY)** 值是数字数组，每个以 `uint64_t` 存储。

**string array ( NV_TYPE_STRING_ARRAY)** 值是 C 字符串数组。

**nvlist array ( NV_TYPE_NVLIST_ARRAY)** 值是 nvlist 数组。当 nvlist 被添加到数组时，它成为主 nvlist 的一部分。可以使用 `nvlist_get_array_next` 和 `nvlist_get_pararr` 函数遍历这些数组。

**descriptor array ( NV_TYPE_DESCRIPTOR_ARRAY)** 值是文件描述符数组。

`nvlist_create` 函数分配内存并初始化一个 nvlist。

可以提供以下标志：

**`NV_FLAG_IGNORE_CASE`** 对提供的名称执行不区分大小写的查找。

**`NV_FLAG_NO_UNIQUE`** nvlist 中的名称不必唯一。

`nvlist_destroy` 函数销毁给定的 nvlist。如果 `nvl` 为 `NULL`，此函数不执行任何操作。此函数从不修改 `errno`。

`nvlist_error` 函数返回 `nvl` 上设置的第一个错误。如果 `nvl` 不处于错误状态，此函数返回零。如果 `nvl` 为 `NULL`，返回 `ENOMEM`。

`nvlist_set_error` 函数为 `nvl` 设置错误值。后续对 `nvlist_error` 的调用将返回 `error`。此函数不能用于清除 nvlist 的错误状态。如果 nvlist 已处于错误状态，此函数不执行任何操作。

`nvlist_empty` 函数在 `nvl` 为空时返回 `true`，否则返回 `false`。nvlist 不得处于错误状态。

`nvlist_flags` 函数返回用于创建 `nvl` 的标志（通过 `nvlist_create`、`nvlist_recv`、`nvlist_unpack` 或 `nvlist_xfer` 函数）。

`nvlist_in_array` 函数在 `nvl` 是作为另一个 nvlist 成员的数组的一部分时返回 `true`。

`nvlist_clone` 函数克隆 `nvl`。克隆与其原始对象不共享任何资源。这也意味着作为 nvlist 一部分的所有文件描述符将在放入克隆之前通过 dup(2) 系统调用复制。

`nvlist_dump` 函数将 nvlist 内容转储到文件描述符 `fd` 以供调试。

`nvlist_fdump` 将 nvlist 内容转储到文件流 `fp` 以供调试。

`nvlist_size` 函数返回 `nvlist_pack` 函数将生成的二进制缓冲区的大小。

`nvlist_pack` 函数将给定的 nvlist 转换为二进制缓冲区。函数为缓冲区分配内存，应使用 free(3) 函数释放。如果 `sizep` 参数不为 `NULL`，缓冲区的大小将存储在那里。此函数在出错时（分配失败）返回 `NULL`。如果 nvlist 包含任何文件描述符，将返回 `NULL`。nvlist 不得处于错误状态。

`nvlist_unpack` 函数将二进制缓冲区转换为新的 nvlist。`flags` 参数与传递给 `nvlist_create` 的 `flags` 参数含义相同。如果 `flags` 与打包前用于创建初始 nvlist 的标志不匹配，此函数将失败。嵌套 nvlist 的标志不由该函数验证。调用者有责任使用 `nvlist_flags` 验证任何嵌套 nvlist 上的标志。此函数成功时返回新的 nvlist，出错时返回 `NULL`。

`nvlist_send` 函数通过套接字 `sock` 发送 `nvl`。注意，包含文件描述符的 nvlist 只能通过 [unix(4)](../man4/unix.4.md) 域套接字发送。

`nvlist_recv` 函数通过套接字 `sock` 接收 nvlist。与 `nvlist_unpack` 一样，`flags` 参数用于构造新的 nvlist，必须与对端写入 `sock` 的原始 nvlist 构造时使用的标志匹配。嵌套 nvlist 的标志不由该函数验证。调用者有责任使用 `nvlist_flags` 验证任何嵌套 nvlist 上的标志。此函数成功时返回新的 nvlist，出错时返回 `NULL`。

`nvlist_xfer` 函数通过套接字 `sock` 参数发送 `nvl`，然后通过同一套接字接收新的 nvlist。`flags` 参数类似于 `nvlist_recv` 应用于新的 nvlist。nvlist `nvl` 总是被销毁。此函数成功时返回新的 nvlist，出错时返回 `NULL`。

`nvlist_next` 函数遍历 `nvl`，返回后续元素的名称和类型。`cookiep` 参数确定返回哪个元素。如果 `*cookiep` 为 `NULL`，返回列表中第一个元素的值。否则，`*cookiep` 应包含先前调用 `nvlist_next` 的结果，此时返回 `nvl` 中下一个元素的值。当 `nvl` 上没有更多元素时，此函数返回 `NULL`。`typep` 参数可以为 `NULL`。遍历时不得从 `nvl` nvlist 中移除元素。`nvl` 不得处于错误状态。可以通过 [cnv(9)](cnv.9.md) API 对由 cookie 标识的元素执行附加操作。

`nvlist_exists` 函数在 `nvl` 中存在名为 `name` 的元素时（无论类型）返回 `true`，否则返回 `false`。nvlist 不得处于错误状态。

`nvlist_exists_type` 函数在存在名为 `name` 且类型为 `type` 的元素时返回 `true`，否则返回 `false`。nvlist 不得处于错误状态。

`nvlist_exists_null`、`nvlist_exists_bool`、`nvlist_exists_number`、`nvlist_exists_string`、`nvlist_exists_nvlist`、`nvlist_exists_descriptor`、`nvlist_exists_binary`、`nvlist_exists_bool_array`、`nvlist_exists_number_array`、`nvlist_exists_string_array`、`nvlist_exists_nvlist_array`、`nvlist_exists_descriptor_array` 函数在存在名为 `name` 且类型由函数名确定的元素时返回 `true`，否则返回 `false`。nvlist 不得处于错误状态。

`nvlist_add_null`、`nvlist_add_bool`、`nvlist_add_number`、`nvlist_add_string`、`nvlist_add_stringf`、`nvlist_add_stringv`、`nvlist_add_nvlist`、`nvlist_add_descriptor`、`nvlist_add_binary`、`nvlist_add_bool_array`、`nvlist_add_number_array`、`nvlist_add_string_array`、`nvlist_add_nvlist_array`、`nvlist_add_descriptor_array` 函数向 `nvl` 添加元素。添加字符串或二进制缓冲区时，这些函数分配内存并复制数据。添加 nvlist 时，`value` nvlist 被克隆，克隆被添加到 `nvl`。添加文件描述符时，描述符通过 dup(2) 系统调用复制，新的文件描述符被添加。如果数组中有任何 `NULL` 元素或数组指针为 `NULL`，数组函数将失败。如果在添加新元素时发生错误，将设置内部错误，可以使用 `nvlist_error` 函数检查。

`nvlist_move_string`、`nvlist_move_nvlist`、`nvlist_move_descriptor`、`nvlist_move_binary`、`nvlist_move_bool_array`、`nvlist_move_number_array`、`nvlist_move_string_array`、`nvlist_move_nvlist_array`、`nvlist_move_descriptor_array` 函数向 `nvl` 添加元素，但与 `nvlist_add_<type>` 函数不同，它们消费给定的资源。对于字符串、文件描述符、二进制缓冲区或 nvlist 值，不应将值多次移动到 nvlist 中；这样做将导致该值被多次释放。注意，字符串或二进制缓冲区必须用 malloc(3) 分配，当 `nvl` 被销毁时，指针将通过 free(3) 释放。如果数组中有任何 `NULL` 元素或数组指针为 `NULL`，数组函数将失败。如果在添加新元素时发生错误，资源将被销毁并设置内部错误，可以使用 `nvlist_error` 函数检查。

`nvlist_get_bool`、`nvlist_get_number`、`nvlist_get_string`、`nvlist_get_nvlist`、`nvlist_get_descriptor`、`nvlist_get_binary`、`nvlist_get_bool_array`、`nvlist_get_number_array`、`nvlist_get_string_array`、`nvlist_get_nvlist_array`、`nvlist_get_descriptor_array` 函数返回 `nvl` 中名为 `name` 的第一个元素的值。对于字符串、nvlist、文件描述符、二进制缓冲区或数组值，返回的资源不得修改——它仍属于 `nvl`。

如果名为 `name` 的元素不存在，程序将中止。为避免此情况，调用者应在尝试获取值之前检查元素是否存在，或使用 [dnv(9)](dnv.9.md) 扩展，该扩展在元素缺失时提供默认值。

nvlist 不得处于错误状态。

`nvlist_get_parent` 函数返回 `nvl` 的父 nvlist。

`nvlist_get_array_next` 函数从 nvlist 数组中返回 `nvl` 之后的下一个元素。如果 `nvl` 不在 nvlist 数组中或它是最后一个元素，此函数返回 `NULL`。只有使用 `nvlist_add_nvlist_array`、`nvlist_append_nvlist_array` 或 `nvlist_move_nvlist_array` 将 nvlist 添加到 nvlist 数组时，nvlist 才在 nvlist 数组中。

`nvlist_get_pararr` 函数从 nvlist 数组中返回 `nvl` 之后的下一个元素。如果 `nvl` 是 nvlist 数组中的最后一个元素，则返回 `nvl` 的父 nvlist。如果 `nvl` 不在 nvlist 数组中，返回 `NULL`。

`nvlist_take_bool`、`nvlist_take_number`、`nvlist_take_string`、`nvlist_take_nvlist`、`nvlist_take_descriptor`、`nvlist_take_binary`、`nvlist_take_bool_array`、`nvlist_take_number_array`、`nvlist_take_string_array`、`nvlist_take_nvlist_array`、`nvlist_take_descriptor_array` 函数返回名为 `name` 的元素的值，并从 `nvl` 中移除该元素。对于字符串和二进制缓冲区值，调用者有责任使用 free(3) 函数释放返回的值。对于 nvlist 值，调用者有责任使用 `nvlist_destroy` 函数销毁返回的 nvlist。对于文件描述符值，调用者有责任使用 close(2) 系统调用关闭返回的描述符。对于数组值，调用者有责任根据元素类型销毁数组的每个元素。此外，调用者还必须使用 free(3) 函数释放指向数组的指针。

如果名为 `name` 的元素不存在，程序将中止。为避免此情况，调用者应在尝试获取值之前检查元素是否存在，或使用 [dnv(9)](dnv.9.md) 扩展，该扩展在元素缺失时提供默认值。

nvlist 不得处于错误状态。

`nvlist_append_bool_array`、`nvlist_append_number_array`、`nvlist_append_string_array`、`nvlist_append_nvlist_array`、`nvlist_append_descriptor_array` 函数使用与添加函数相同的语义将元素追加到现有数组（即元素将在适用时被复制）。如果名为 `name` 的数组不存在，则将如同使用 `nvlist_add_<type>_array` 函数一样创建它。如果在追加新元素时发生错误，将在 `nvl` 上设置内部错误。

`nvlist_free` 函数从 `nvl` 中移除名为 `name` 的第一个元素（无论类型）并释放与之关联的所有资源。如果不存在名为 `name` 的元素，程序将中止。nvlist 不得处于错误状态。

`nvlist_free_type` 函数从 `nvl` 中移除名为 `name` 且类型为 `type` 的第一个元素并释放与之关联的所有资源。如果不存在名为 `name` 且类型为 `type` 的元素，程序将中止。nvlist 不得处于错误状态。

`nvlist_free_null`、`nvlist_free_bool`、`nvlist_free_number`、`nvlist_free_string`、`nvlist_free_nvlist`、`nvlist_free_descriptor`、`nvlist_free_binary`、`nvlist_free_bool_array`、`nvlist_free_number_array`、`nvlist_free_string_array`、`nvlist_free_nvlist_array`、`nvlist_free_descriptor_array` 函数从 `nvl` 中移除名为 `name` 且类型由函数名确定的第一个元素并释放与之关联的所有资源。如果不存在名为 `name` 且具有相应类型的元素，程序将中止。nvlist 不得处于错误状态。

### 注意事项

`nvlist_pack` 和 `nvlist_unpack` 函数处理字节序转换，因此二进制缓冲区可以在具有不同字节序的主机上打包和解包。

`nvlist_recv`、`nvlist_send` 和 `nvlist_xfer` 函数可以在具有不同字节序的主机之间传输 nvlist。

### 内核注意事项

`nv`、`cnv` 和 `dnv` API 可以在内核中使用，但有以下区别：

- 不支持文件描述符和文件描述符数组值类型。
- 不支持 `nvlist_recv`、`nvlist_send` 和 `nvlist_xfer`。
- 所有内存分配使用 [malloc(9)](malloc.9.md) 和 free(9) 的 `M_NVLIST` 内存类型。因此，任何移动到 nvlist 中的已分配缓冲区必须用 `M_NVLIST` 分配，而 `nvlist_pack` 等函数返回的缓冲区必须用 `M_NVLIST` 释放。

## 实例

以下示例演示如何准备 nvlist 并通过 [unix(4)](../man4/unix.4.md) 域套接字发送它。

```c
nvlist_t *nvl;
int fd;
fd = open("/tmp/foo", O_RDONLY);
if (fd < 0)
        err(1, "open(\"/tmp/foo\") failed");
nvl = nvlist_create(0);
/*
 * 无需检查 nvlist_create() 是否成功，
 * 因为 nvlist_add_<type>() 函数可以处理。
 * 如果失败，nvlist_send() 也会失败。
 */
nvlist_add_string(nvl, "filename", "/tmp/foo");
nvlist_add_number(nvl, "flags", O_RDONLY);
/*
 * 我们只想发送描述符，所以可以将其交给
 * nvlist 消费（这就是为什么我们使用 nvlist_move
 * 而非 nvlist_add）。
 */
nvlist_move_descriptor(nvl, "fd", fd);
if (nvlist_send(sock, nvl) < 0) {
	nvlist_destroy(nvl);
	err(1, "nvlist_send() failed");
}
nvlist_destroy(nvl);
```

接收 nvlist 并获取元素值：

```c
nvlist_t *nvl;
const char *command;
char *filename;
int fd;
nvl = nvlist_recv(sock, 0);
if (nvl == NULL)
	err(1, "nvlist_recv() failed");
/* 对于 command，我们接受指向 nvlist 内部缓冲区的指针。 */
command = nvlist_get_string(nvl, "command");
/*
 * 对于 filename，我们将其从 nvlist 中移除并
 * 获取缓冲区的所有权。
 */
filename = nvlist_take_string(nvl, "filename");
/* 文件描述符同理。 */
fd = nvlist_take_descriptor(nvl, "fd");
printf("command=%s filename=%s fd=%d\n", command, filename, fd);
/* command 由 nvlist_destroy() 释放 */
nvlist_destroy(nvl);
free(filename);
close(fd);
```

遍历 nvlist：

```c
nvlist_t *nvl;
const char *name;
void *cookie;
int type;
nvl = nvlist_recv(sock, 0);
if (nvl == NULL)
	err(1, "nvlist_recv() failed");
cookie = NULL;
while ((name = nvlist_next(nvl, &type, &cookie)) != NULL) {
	printf("%s=", name);
	switch (type) {
	case NV_TYPE_NUMBER:
		printf("%ju", (uintmax_t)nvlist_get_number(nvl, name));
		break;
	case NV_TYPE_STRING:
		printf("%s", nvlist_get_string(nvl, name));
		break;
	default:
		printf("N/A");
		break;
	}
	printf("\n");
}
```

遍历每个嵌套 nvlist：

```c
nvlist_t *nvl;
const char *name;
void *cookie;
int type;
nvl = nvlist_recv(sock, 0);
if (nvl == NULL)
	err(1, "nvlist_recv() failed");
cookie = NULL;
do {
	while ((name = nvlist_next(nvl, &type, &cookie)) != NULL) {
		if (type == NV_TYPE_NVLIST) {
			nvl = nvlist_get_nvlist(nvl, name);
			cookie = NULL;
		}
	}
} while ((nvl = nvlist_get_parent(nvl, &cookie)) != NULL);
```

遍历每个嵌套 nvlist 和每个 nvlist 元素：

```c
nvlist_t *nvl;
const nvlist_t * const *array;
const char *name;
void *cookie;
int type;
nvl = nvlist_recv(sock, 0);
if (nvl == NULL)
	err(1, "nvlist_recv() failed");
cookie = NULL;
do {
	while ((name = nvlist_next(nvl, &type, &cookie)) != NULL) {
		if (type == NV_TYPE_NVLIST) {
			nvl = nvlist_get_nvlist(nvl, name);
			cookie = NULL;
		} else if (type == NV_TYPE_NVLIST_ARRAY) {
			nvl = nvlist_get_nvlist_array(nvl, name, NULL)[0];
			cookie = NULL;
		}
	}
} while ((nvl = nvlist_get_pararr(nvl, &cookie)) != NULL);
```

或者：

```c
nvlist_t *nvl, *tmp;
const nvlist_t * const *array;
const char *name;
void *cookie;
int type;
nvl = nvlist_recv(sock, 0);
if (nvl == NULL)
	err(1, "nvlist_recv() failed");
cookie = NULL;
tmp = nvl;
do {
	do {
		nvl = tmp;
		while ((name = nvlist_next(nvl, &type, &cookie)) != NULL) {
			if (type == NV_TYPE_NVLIST) {
				nvl = nvlist_get_nvlist(nvl, name);
				cookie = NULL;
			} else if (type == NV_TYPE_NVLIST_ARRAY) {
				nvl = nvlist_get_nvlist_array(nvl, name,
				    NULL)[0];
				cookie = NULL;
			}
		}
		cookie = NULL;
	} while ((tmp = nvlist_get_array_next(nvl)) != NULL);
} while ((tmp = nvlist_get_parent(nvl, &cookie)) != NULL);
```

## 参见

close(2), dup(2), open(2), err(3), free(3), printf(3), [unix(4)](../man4/unix.4.md)

## 历史

`libnv` 库出现于 FreeBSD 11.0。

## 作者

`libnv` 库由 Pawel Jakub Dawidek <pawel@dawidek.net> 在 FreeBSD 基金会赞助下实现。
