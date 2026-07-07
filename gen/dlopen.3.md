# dlopen(3)

`dlopen` — 动态链接器的编程接口

## 名称

`dlopen`, `fdlopen`, `dlsym`, `dlvsym`, `dlfunc`, `dlerror`, `dlclose`

## 库

Lb libc

## 概要

`#include <dlfcn.h>`

```c
void *
dlopen(const char *path, int mode);

void *
fdlopen(int fd, int mode);

void *
dlsym(void * restrict handle, const char * restrict symbol);

void *
dlvsym(void * restrict handle, const char * restrict symbol,
    const char * restrict version);

dlfunc_t
dlfunc(void * restrict handle, const char * restrict symbol);

char *
dlerror(void);

int
dlclose(void *handle);
```

## 描述

这些函数为动态链接器的服务提供了简单的编程接口。提供的操作包括：向程序的地址空间添加新的共享对象、获取此类对象定义的符号的地址绑定，以及在不再需要时移除此类对象。

`dlopen` 函数提供对 `path` 中共享对象的访问，返回一个描述符，可用于在后续调用 `dlsym`、`dlvsym` 和 `dlclose` 时引用该对象。如果在调用 `dlopen` 之前 `path` 不在地址空间中，则将其放入地址空间。当对象以这种方式首次加载到地址空间时，动态链接器会调用其 `_init` 函数（如果存在）。如果 `path` 已在先前调用 `dlopen` 时放入地址空间，则不会再次添加，但会维护对 `path` 的 `dlopen` 操作的引用计数。为 `path` 提供的空指针被解释为对进程主可执行文件的引用。`mode` 参数控制从加载对象的外部函数引用绑定到其引用对象的方式。它必须包含以下值之一，可能与随后描述的附加标志进行按位或运算：

**`RTLD_LAZY`** 每个外部函数引用在函数首次调用时解析。

**`RTLD_NOW`** 所有外部函数引用由 `dlopen` 立即绑定。

出于效率原因，通常首选 `RTLD_LAZY`。但是，`RTLD_NOW` 可用于确保在调用 `dlopen` 期间发现任何未定义的符号。

以下标志之一可以按位或到 `mode` 参数中：

**`RTLD_GLOBAL`** 此共享对象及其所需对象的有向无环图 (DAG) 中的符号将可用于解析来自所有其他共享对象的未定义引用。

**`RTLD_LOCAL`** 此共享对象及其所需对象 DAG 中的符号仅可用于解析来自同一 DAG 中其他对象的未定义引用。这是默认值，但可以通过此标志显式指定。

**`RTLD_TRACE`** 设置时，动态链接器在加载此共享对象所需的所有对象并向标准输出打印包含所有对象绝对路径名的摘要后退出。使用此标志时，`dlopen` 仅在出错时才返回给调用者。

**`RTLD_NODELETE`** 防止在 `dlclose` 时卸载已加载的对象。可通过静态链接器 [ld(1)](../man1/ld.lld.1.md) 的 `-z nodelete` 选项请求相同的行为。

**`RTLD_NOLOAD`** 仅当对象已加载到进程地址空间中时才返回有效句柄，否则返回 `NULL`。可以指定其他模式标志，这些标志将应用于所找到对象的提升。

**`RTLD_DEEPBIND`** 解析源自该库的符号引用时，已加载库中的符号置于全局符号之前。

`path` 支持一种特殊语法，形式为：

```
#number/name
```

`number` 应为十进制数，引用一个打开的文件描述符，并且该描述符也必须列在环境变量 `LD_LIBRARY_PATH_FDS` 中。在这种情况下，链接器尝试加载可由 `openat(number, path, O_RDONLY)` 打开的对象。此功能仅对受信任的进程可用，即激活的映像不能是 set-uid 或 set-gid 的。

如果 `dlopen` 失败，它返回空指针，并设置一个可通过 `dlerror` 查询的错误条件。

`fdlopen` 函数类似于 `dlopen`，但它接受文件描述符参数 `fd`，用于将对象加载到地址空间所需的文件操作。无论执行结果如何，文件描述符 `fd` 都不会被该函数关闭，但文件描述符的副本会被关闭。如果在传递的描述符上持有 [lockf(3)](../sys-1/lockf.3.md) 锁，这可能很重要。`fd` 参数 -1 被解释为对进程主可执行文件的引用，类似于 `dlopen` 的 `name` 参数为 `NULL` 值的情况。需要对加载的对象执行额外检查的代码可以使用 `fdlopen` 函数，以防止与符号链接或重命名的竞争。使用 [capsicum(4)](../man4/capsicum.4.md) 沙箱化的应用程序也可以有益地使用 `fdlopen`。

`dlsym` 函数返回以空字符结尾的字符串 `symbol` 所描述的符号的地址绑定，该符号出现在由 `handle` 标识的共享对象中。由 `dlopen` 添加到地址空间的对象所导出的符号只能通过调用 `dlsym` 来访问。这些符号不会取代加载对象时地址空间中已存在的这些符号的任何定义，也不能用于满足正常的动态链接引用。

如果使用特殊 `handle` `NULL` 调用 `dlsym`，则将其解释为对发起调用的可执行文件或共享对象的引用。因此，共享对象可以引用自身的符号。

如果使用特殊 `handle` `RTLD_DEFAULT` 调用 `dlsym`，则符号搜索遵循加载对象时用于解析未定义符号的算法。搜索的对象如下，按给定顺序：

- 引用对象本身（或发起 `dlsym` 调用的对象），如果该对象是使用 [ld(1)](../man1/ld.lld.1.md) 的 `-Bsymbolic` 选项链接的。
- 程序启动时加载的所有对象。
- 通过 `dlopen` 加载且 `mode` 参数中设置了 `RTLD_GLOBAL` 标志的所有对象。
- 通过 `dlopen` 加载且位于也包含引用对象的所需对象 DAG 中的所有对象。

如果使用特殊 `handle` `RTLD_NEXT` 调用 `dlsym`，则符号搜索仅限于在发起 `dlsym` 调用的对象之后加载的共享对象。因此，如果从主程序调用该函数，则搜索所有共享库。如果从共享库调用，则搜索所有后续的共享库。`RTLD_NEXT` 可用于实现库函数的包装器。例如，包装函数 `getpid` 可以通过 `dlsym(RTLD_NEXT, "getpid")` 访问“真正的” `getpid`。（实际上，应使用下文的 `dlfunc` 接口，因为 `getpid` 是函数而非数据对象。）

如果使用特殊 `handle` `RTLD_SELF` 调用 `dlsym`，则符号搜索仅限于发起 `dlsym` 调用的共享对象及其之后加载的共享对象。

如果找不到符号，`dlsym` 函数返回空指针，并设置一个可通过 `dlerror` 查询的错误条件。

`dlvsym` 函数的行为类似于 `dlsym`，但接受一个额外参数 `version`：一个以空字符结尾的字符串，用于请求 `symbol` 的特定版本。

`dlfunc` 函数实现了 `dlsym` 的所有行为，但其返回类型可以转换为函数指针而不会触发编译器诊断。（`dlsym` 函数返回对象指针；在 C 标准中，对象指针与函数指针类型之间的转换是未定义的。某些编译器和 lint 工具会对此类转换发出警告。）`dlfunc` 的精确返回类型未指定；应用程序必须将其转换为适当的函数指针类型。

`dlerror` 函数返回一个以空字符结尾的字符串，描述在调用 `dlopen`、`dladdr`、`dlinfo`、`dlsym`、`dlvsym`、`dlfunc` 或 `dlclose` 期间发生的最后一个错误。如果没有发生此类错误，`dlerror` 返回空指针。每次调用 `dlerror` 时，错误指示都会被重置。因此，在两次调用 `dlerror` 的情况下，如果第二次调用紧跟在第一次之后，第二次调用将始终返回空指针。

`dlclose` 函数删除对 `handle` 所引用共享对象的引用。如果引用计数降为 0，则将该对象从地址空间中移除，`handle` 变为无效。在以这种方式移除共享对象之前，动态链接器会调用对象的 `_fini` 函数（如果该对象定义了这样的函数）。如果 `dlclose` 成功，返回值为 0。否则返回 -1，并设置一个可通过 `dlerror` 查询的错误条件。

对象内在的 `_init` 和 `_fini` 函数在调用时不带参数，且不应返回值。

## 注释

ELF 可执行文件需要使用 [ld(1)](../man1/ld.lld.1.md) 的 `-export-dynamic` 选项链接，才能使可执行文件中定义的符号对 `dlsym`、`dlvsym` 或 `dlfunc` 可见。

其他 ELF 平台需要与 `libdl` 链接以提供 `dlopen` 和其他函数。FreeBSD 不需要与该库链接，但为兼容性而支持它。

在先前的实现中，必须为所有外部符号添加下划线前缀，才能获得与从 C 语言编译的对象代码的符号兼容性。在使用 C 语言编译器的（已弃用的）`-aout` 选项时，情况仍然如此。

## 错误

`dlopen`、`fdlopen`、`dlsym`、`dlvsym` 和 `dlfunc` 函数在出错时返回空指针。`dlclose` 函数成功时返回 0，出错时返回 -1。每当检测到错误时，可通过调用 `dlerror` 来检索详细说明该错误的消息。

## 参见

[ld(1)](../man1/ld.lld.1.md), [rtld(1)](../man1/rtld.1.md), [dladdr(3)](dladdr.3.md), [dlinfo(3)](dlinfo.3.md), [link(5)](../man5/link.5.md)
