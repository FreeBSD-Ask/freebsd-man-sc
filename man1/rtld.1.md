# rtld(1)

`ld-elf.so.1` — 运行时链接编辑器

## 名称

`ld-elf.so.1`, `ld.so`, `rtld`

## 描述

`rtld` 实用程序是一个自包含的共享对象，为将共享对象加载和链接编辑到进程地址空间提供运行时支持。它通常也被称为动态链接器。它使用动态链接程序中包含的数据结构来确定需要哪些共享库，并使用 [mmap(2)](../man2/mmap.2.md) 系统调用加载它们。

在所有共享库成功加载后，`rtld` 继续解析来自主程序和所有已加载对象的外部引用。提供了一种机制，可以按对象调用初始化例程，使共享对象有机会在程序正式开始执行之前执行任何额外的设置。这对于包含静态构造函数的 C++ 库很有用。

在解析已加载对象的依赖项时，`rtld` 会翻译 rpath 和 soname 中的动态令牌字符串。如果在链接二进制文件时设置了静态链接器的 `-z origin` 选项，则在对象加载时执行令牌扩展，参见 [ld(1)](ld.1.md)。当前可识别以下字符串：

**`$ORIGIN`** 翻译为已加载对象的完整路径。

**`$OSNAME`** 翻译为操作系统实现的名称。

**`$OSREL`** 翻译为操作系统的发布级别。

**`$PLATFORM`** 翻译为机器硬件平台。

**`$LIB`** 翻译为平台上的系统库路径组件。对于本机二进制文件，它是 `lib`；对于 compat32 二进制文件，通常是 `lib32`。平台上支持的其他 ABI 可能存在其他翻译。

`rtld` 实用程序本身由内核连同任何要执行的动态链接程序一起加载。内核将控制权转移给动态链接器。在动态链接器完成加载、重定位和初始化程序及其所需共享对象后，它将控制权转移给程序的入口点。使用以下搜索顺序来定位所需的共享对象：

- 引用对象的 `DT_RPATH`，除非该对象还包含 `DT_RUNPATH` 标记
- 程序的 `DT_RPATH`，除非引用对象包含 `DT_RUNPATH` 标记
- `LD_LIBRARY_PATH` 环境变量指示的路径
- 引用对象的 `DT_RUNPATH`
- ldconfig(8) 实用程序生成的提示文件
- **/lib** 和 **/usr/lib** 目录，除非引用对象是使用“`-z` `nodefaultlib`”选项链接的

`rtld` 实用程序识别许多环境变量，可用于修改其行为。在 64 位架构上，32 位对象的链接器识别下面列出的所有环境变量，但以 `LD_32_` 为前缀，例如：`LD_32_TRACE_LOADED_OBJECTS`。如果激活的映像是 setuid 或 setgid 的，则忽略这些变量。

运行时链接器能够访问进程启动时提供的环境。启动后，环境变量由更高级别的库维护，运行时链接器无法访问。在运行时，可以使用 [rtld_get_var(3)](../man3/rtld_get_var.3.md) 查询有效设置，其中一些可以使用 rtld_set_var(3) 更改。

**`%a`** 主程序的名称（也称为“\_\_progname）”。

**`%A`** 环境变量 `LD_TRACE_LOADED_OBJECTS_PROGNAME` 的值。通常用于打印正在使用 [ldd(1)](ldd.1.md) 检查的程序和共享库的名称。

**`%o`** 库名称。

**`%p`** 由 `rtld` 的库搜索规则确定的完整路径名。

**`%x`** 库的加载地址。

**`LD_DUMP_REL_POST`** 如果设置，`rtld` 将在符号绑定和重定位之后打印包含所有重定位的表。

**`LD_DEBUG`** 如果设置，`rtld` 将在加载和链接程序时打印大量内部调试消息。

**`LD_DUMP_REL_PRE`** 如果设置，`rtld` 将在符号绑定和重定位之前打印包含所有重定位的表。

**`LD_DYNAMIC_WEAK`** 如果设置，使用符合 ELF 标准的符号查找行为：解析为第一个找到的符号定义。默认情况下，FreeBSD 提供非标准的符号查找行为：当找到弱符号定义时，记住该定义并继续在其余共享对象中搜索非弱定义。如果找到，则优先使用非弱定义，否则返回记住的弱定义。动态链接器本身导出的符号（参见 dlfcn(3)）始终使用 FreeBSD 规则解析，无论该变量是否存在。对于 set-user-ID 和 set-group-ID 程序，此变量未设置。

**`LD_LIBMAP`** 库替换列表，格式与 [libmap.conf(5)](../man5/libmap.conf.5.md) 相同。为方便起见，可以使用字符 `=` 和 `,` 来代替空格和换行符。此变量在 [libmap.conf(5)](../man5/libmap.conf.5.md) 之后解析，并将覆盖其条目。对于 set-user-ID 和 set-group-ID 程序，此变量未设置。

**`LD_LIBMAP_DISABLE`** 如果设置，禁用 [libmap.conf(5)](../man5/libmap.conf.5.md) 和 `LD_LIBMAP` 的使用。对于 set-user-ID 和 set-group-ID 程序，此变量未设置。

**`LD_ELF_HINTS_PATH`** 此变量将覆盖“提示”文件的默认位置。对于 set-user-ID 和 set-group-ID 程序，此变量未设置。

**`LD_LIBRARY_PATH`** 以冒号分隔的目录列表，覆盖共享库的默认搜索路径。对于 set-user-ID 和 set-group-ID 程序，此变量未设置。

**`LD_LIBRARY_PATH_RPATH`** 如果指定了该变量且其值以 'y'、'Y' 或 '1' 符号开头，则对于不包含 `DT_RUNPATH` 标记的二进制文件，`LD_LIBRARY_PATH` 变量指定的路径允许覆盖 `DT_RPATH` 中的路径。对于此类二进制文件，当设置了 `LD_LIBRARY_PATH_RPATH` 变量时，“`-z` `nodefaultlib`”链接时选项也将被忽略。

**`LD_PRELOAD`** 以冒号和/或空格分隔的共享库列表，在任何其他共享库之前链接。如果未指定目录，则首先搜索 `LD_LIBRARY_PATH` 指定的目录，然后是内置标准目录集。对于 set-user-ID 和 set-group-ID 程序，此变量未设置。

**`LD_PRELOAD_FDS`** 以冒号分隔的库文件描述符编号列表。这用于预加载我们已有文件描述符的库。这可以优化加载库的过程，因为我们不必在目录中查找它们。在我们无法访问文件系统等全局命名空间的能力基础系统中，它也可能很有用。

**`LD_LIBRARY_PATH_FDS`** 以冒号分隔的库目录文件描述符编号列表。这用于在 [capsicum(4)](../man4/capsicum.4.md) 沙箱内使用，当文件系统等全局命名空间不可用时。它在 LD_LIBRARY_PATH 之后查询。对于 set-user-ID 和 set-group-ID 程序，此变量未设置。

**`LD_BIND_NOT`** 当设置为非空字符串时，阻止在进行绑定时修改 PLT 槽。结果是，PLT 解析的函数的每次调用都会被解析。与调试输出结合使用时，这提供了运行时所有绑定操作的完整记录。对于 set-user-ID 和 set-group-ID 程序，此变量未设置。

**`LD_BIND_NOW`** 当设置为非空字符串时，使 `rtld` 在开始执行程序之前重定位所有外部函数调用。通常，函数调用是延迟绑定的，在第一次调用每个函数时绑定。`LD_BIND_NOW` 增加了程序的启动时间，但避免了由意外未定义的函数引起的运行时意外。

**`LD_TRACE_LOADED_OBJECTS`** 当设置为非空字符串时，使 `rtld` 在加载共享对象并打印摘要（包括所有对象的绝对路径名）到标准输出后退出。

**`LD_TRACE_LOADED_OBJECTS_ALL`** 当设置为非空字符串时，使 `rtld` 扩展摘要以指示哪些对象导致每个对象被加载。

**`LD_TRACE_LOADED_OBJECTS_FMT1`**

**`LD_TRACE_LOADED_OBJECTS_FMT2`** 设置时，这些变量被解释为类似于 [printf(3)](../man3/printf.3.md) 的格式字符串，用于自定义跟踪输出，并由 [ldd(1)](ldd.1.md) 的 `-f` 选项使用，使 [ldd(1)](ldd.1.md) 更方便地作为过滤器操作。如果依赖项名称以字符串 `lib` 开头，则使用 `LD_TRACE_LOADED_OBJECTS_FMT1`，否则使用 `LD_TRACE_LOADED_OBJECTS_FMT2`。可以使用以下转换：此外，识别 `en` 和 `et` 并具有其通常含义。

**`LD_UTRACE`** 如果设置，`rtld` 将通过 [utrace(2)](../man2/utrace.2.md) 记录共享对象的加载和卸载等事件。

**`LD_LOADFLTR`** 如果设置，`rtld` 将立即处理已加载对象的 filtee 依赖项，而不是推迟到需要时。通常，filtee 在从过滤器对象第一次符号解析时打开。

**`LD_SHOW_AUXV`** 如果设置，使 `rtld` 在将控制权传递给任何用户代码之前，将 aux 向量的内容转储到标准输出。

**`LD_STATIC_TLS_EXTRA`** 如果指定了该变量且具有数值，`rtld` 将静态 TLS 额外空间的大小设置为指定的字节数。静态 TLS 额外空间在使用 [dlopen(3)](../man3/dlopen.3.md) 加载为 initial-exec TLS 代码模型编译的对象时使用。可指定的最小值为 '128'。

**`LD_NO_DL_ITERATE_PHDR_AFTER_FORK`** 允许 [dl_iterate_phdr(3)](../man3/dl_iterate_phdr.3.md) 在回调中阻塞，而不会导致 [fork(2)](../man2/fork.2.md) 死锁。缺点是以此模式启动的映像在 fork 之后不能使用 [dl_iterate_phdr(3)](../man3/dl_iterate_phdr.3.md)。

## 直接执行模式

`rtld` 通常隐式使用，由内核根据执行二进制文件的 `PT_INTERP` 程序头请求加载。FreeBSD 还支持动态链接器的直接执行模式。在此模式下，用户显式执行 `rtld` 并提供要链接和执行的程序的路径作为参数。此模式允许为程序激活使用非标准动态链接器，而无需更改二进制文件或更改已安装的动态链接器。可以指定执行选项。

直接调用的语法为

> **/libexec/ld-elf.so.1**
> [`-b` `exe`]
> [`-d`]
> [`-f` `fd`]
> [`-o` `OPT=VALUE`]
> [`-p`]
> [`-u`]
> [`-v`]
> [`--`]
> `image_path`
> [`image arguments`]

选项如下：

**`-b`** `exe` 使用可执行文件 `exe` 而不是 `image_path` 进行激活。如果指定了此选项，`image_path` 仅用于向程序提供 `argv[0]` 值。

**`-d`** 关闭二进制文件执行权限的模拟。

**`-f`** `fd` 文件描述符 `fd` 引用要由 `rtld` 激活的二进制文件。在执行 `rtld` 时，它必须已经在进程中打开。如果指定了此选项，`image_path` 仅用于向程序提供 `argv[0]` 值。

**`-o`** `OPT=VALUE` 将 `OPT` 配置变量设置为值 `VALUE`。可能的变量名称在上面作为 `LD_` 前缀环境变量列出，但此处引用时不带 `LD_` 前缀。以这种方式设置的配置变量不会泄漏到激活映像的环境中。该选项可以根据需要重复多次以设置所有配置参数。使用此选项设置的参数优先于通过环境分配的相同参数。

**`-p`** 如果 `image_path` 参数指定了不包含斜杠“`/`”字符的名称，`rtld` 使用环境变量 `PATH` 提供的搜索路径来查找要执行的二进制文件。

**`-u`** 忽略所有 `LD_` 环境变量和之前影响动态链接器行为的命令行 `-o` 选项。

**`-v`** 显示有关此运行时链接器二进制文件的信息，然后退出。

**`--`** 结束 `rtld` 选项。`--` 之后的参数被解释为要执行的二进制文件的路径。

在直接执行模式下，`rtld` 模拟对当前用户的二进制执行权限验证。这样做是为了避免在简单限制的执行环境中破坏用户期望。验证仅使用 Unix `DACs`，忽略 `ACLs`，并且自然容易出现竞争条件。依赖此类限制的环境本身就很弱且可破坏。可以使用 `-d` 选项关闭它。

## 版本控制

较新的 `rtld` 可能提供一些在运行时无法通过检查正常导出的符号来轻松检测的功能或运行时行为更改。请注意，在用户空间中验证 `__FreeBSD_version` 来检测功能几乎总是错误的，无论是在编译时还是运行时，因为内核、libc 或环境变量可能与运行的 `rtld` 不匹配。

为解决此问题，`rtld` 在 FreeBSD 私有符号命名空间 `FBSDprivate_1.0` 中导出一些功能指示符。符号以 `_rtld_version` 前缀开头。当前定义的符号及相应功能列表为：

**`_rtld_version__FreeBSD_version`** 符号导出在 `rtld` 构建期间提供的 `__FreeBSD_version` 定义的值。自引入 `_rtld_version` 设施以来，该符号始终存在。

**`_rtld_version_laddr_offset`** `link_map` 结构的 `l_addr` 成员包含共享对象的加载偏移量。在此之前，`l_addr` 包含库的基地址。参见 [dlinfo(3)](../man3/dlinfo.3.md)。它还指示结构中 `l_refname` 成员的存在。

**`_rtld_version_dlpi_tls_data`** 结构 `dl_phdr_info` 的 `dlpi_tls_data` 成员包含调用线程的模块 TLS 段地址，而不是初始化段的地址。

## 文件

**/var/run/ld-elf.so.hints** 提示文件。

**/var/run/ld-elf32.so.hints** 64 位系统上 32 位二进制文件的提示文件。

**/etc/libmap.conf** libmap 配置文件。

**/etc/libmap32.conf** 64 位系统上 32 位二进制文件的 libmap 配置文件。

## 参见

[ld(1)](ld.1.md), [ldd(1)](ldd.1.md), [dlinfo(3)](../man3/dlinfo.3.md), [rtld_get_var(3)](../man3/rtld_get_var.3.md), [capsicum(4)](../man4/capsicum.4.md), [elf(5)](../man5/elf.5.md), [libmap.conf(5)](../man5/libmap.conf.5.md), ldconfig(8)
