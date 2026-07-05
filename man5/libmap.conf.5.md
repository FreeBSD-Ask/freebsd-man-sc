# libmap.conf.5

`libmap.conf` — 动态对象依赖映射的配置文件

## 名称

`libmap.conf`

## 描述

ld-elf.so.1(1) 的 `libmap` 功能允许将动态对象依赖映射到任意名称。

**/etc/libmap.conf** 中的每一行可以采用以下五种形式之一：

**`origin`** `target` 当加载动态对象时遇到对 `origin` 的依赖时，使用 `target` 代替在正常库搜索路径中搜索 `origin`。

**`path1`** `path2` 当遍历库搜索路径时，将任何与 `path1` 完全匹配的元素替换为 `path2`。

**[`constraint`]** 将 `constraint` 应用于后续所有映射，直到下一个约束行或文件末尾。详见约束一节。

**`include`** `file` 在继续处理当前文件之前，先解析 `file` 的内容。嵌套深度仅受可用内存限制，但遇到的每个文件仅处理一次，循环将被静默忽略。

**`includedir`** `dir` 递归遍历 `dir`，在继续处理当前文件之前，解析任何以 `.conf` 结尾的文件的内容。嵌套深度仅受可用内存限制，但遇到的每个目录或文件仅处理一次，循环将被静默忽略。

### 约束

受约束的映射仅在处理满足约束的二进制文件或库时才适用。有三种类型的约束：

**Exact** 约束按字面匹配，只有具有相同完全限定路径名的可执行文件才能满足约束。这意味着可执行文件 `/usr/bin/foo` 不会满足约束 [`/usr/bin/./foo`]，反之亦然。这是默认的约束类型。

**Basename** 没有路径的约束与可执行文件的基本名匹配。例如，约束 [`foo`] 将匹配 `/bin/foo`、`/usr/local/sbin/foo` 或任何其他名为 `foo` 的可执行文件，无论它位于哪个目录中。

**Directory** 以斜杠结尾的约束在完整路径名以约束字符串开头时满足。例如，约束 [`/usr/bin/`] 将匹配任何路径以 `/usr/bin/` 开头的可执行文件。

注意，约束是针对作为第一个参数传递给用于执行相关二进制文件的 exec(3) 函数的路径进行匹配的。从 shell 执行的大多数程序都不带完整路径运行，通过 execvp(3) 或类似函数，因此 basename 约束类型最为有用。

> **警告** 约束适用于直到下一个约束或文件末尾的所有映射。因此，无约束的映射必须放在文件顶部。

### ABI 兼容性

在提供 32 位二进制兼容性的 64 位架构上，**/etc/libmap.conf** 中的映射仅适用于 64 位二进制文件。用于 32 位二进制文件的映射必须放在 **/etc/libmap32.conf** 中。

## 文件

**`/etc/libmap.conf`** libmap 配置文件。
**`/etc/libmap32.conf`** 64 位系统上用于 32 位二进制文件的 libmap 配置文件。

## 实例

```sh
#
# origin		target
#
libc_r.so.6		libpthread.so.2	# 所有使用 'libc_r' 的程序
libc_r.so		libpthread.so	# 现在使用 'libpthread'
[/tmp/mplayer]		# 测试版的 mplayer 使用 libc_r
libpthread.so.2		libc_r.so.6
libpthread.so		libc_r.so
[/usr/local/jdk1.4.1/]	# 所有 Java 1.4.1 程序使用 libthr
			# 这之所以有效，是因为 "javavms" 使用
			# 完整路径名执行程序
libpthread.so.2		libthr.so.2
libpthread.so		libthr.so
# 用于将仅限 Linux 的 EPSON 打印机 .so 加载到 cups 等中的粘合代码
[/usr/local/lib/pips/libsc80c.so]
libc.so.6		pluginwrapper/pips.so
libdl.so.2		pluginwrapper/pips.so
```

## 参见

[ldd(1)](../man1/ldd.1.md), rtld(1)

## 历史

`libmap` 机制首次出现于 FreeBSD 5.1。

## 作者

本手册页由 Matthew N. Dodd <winter@jurai.net> 编写，并由 Dag-Erling Sm(/orgrav <des@FreeBSD.org> 大幅重写。
