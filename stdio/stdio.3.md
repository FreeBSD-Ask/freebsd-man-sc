# stdio(3)

`stdio` — 标准输入输出库函数

## 名称

`stdio`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`FILE *stdin; FILE *stdout; FILE *stderr;`

## 描述

标准 I/O 库提供简单高效的缓冲流 I/O 接口。输入和输出被映射为逻辑数据流，物理 I/O 特性被隐藏。相关函数和宏如下所列；更多信息可从各 man 页面获取。

通过*打开*文件，流与外部文件（可能是物理设备）关联，这可能涉及创建新文件。创建已存在的文件会导致其原有内容被丢弃。若文件支持定位请求（如磁盘文件，与终端不同），则与流关联的*文件位置指示器*定位在文件起始（字节零），除非以追加模式打开文件。若使用追加模式，位置指示器将置于文件末尾。位置指示器由后续的读取、写入和定位请求维护。所有输入如同通过连续调用 fgetc(3) 函数读取字符；所有输出如同通过连续调用 fputc(3) 函数写入所有字符。

通过*关闭*文件，文件与流解除关联。在流与文件解除关联之前，输出流会被刷新（任何未写入的缓冲内容都传输到宿主环境）。文件关闭后，指向 `FILE` 对象的指针值是不确定的（无效）。

文件可随后由同一或另一程序执行重新打开，并取回或修改其内容（若可重定位到起始）。若 `main` 函数返回其原始调用者，或调用 [exit(3)](exit.3.md) 函数，则所有打开的文件在程序终止前都会被关闭（因此所有输出流都会被刷新）。其他程序终止方式可能无法正确关闭文件，因此缓冲输出可能丢失。特别是，[_exit(2)](../man2/_exit.2.md) 不会刷新 stdio 文件。因信号而退出时也不会。根据 POSIX 要求，[abort(3)](abort.3.md) 会刷新缓冲区，尽管先前的实现并未如此。

此实现不区分"文本"流和"二进制"流。实际上，所有流都是二进制流。不进行任何转换，也不在任何流上出现额外填充。

程序启动时，预定义了三个流，无需显式打开：

- *标准输入*（用于读取常规输入），
- *标准输出*（用于写入常规输出），以及
- *标准错误*（用于写入诊断输出）。

这些流缩写为 `stdin`、`stdout` 和 `stderr`。初始时，标准错误流是无缓冲的；标准输入和输出流是全缓冲的，当且仅当这些流不引用交互式或"终端"设备（由 isatty(3) 函数判定）。事实上，*所有*新打开的引用终端设备的流默认为行缓冲，且每当从此类输入流读取时，挂起的输出会自动写入。注意，这仅适用于"真正的读取"；若读取请求可由现有缓冲数据满足，则不会发生自动刷新。在这些情况下，或在输出终端上打印部分行后进行大量计算时，必须在离开并计算之前 [fflush(3)](fflush.3.md) 标准输出，以使输出出现。或者，可通过 setvbuf(3) 函数修改这些默认值。

`stdio` 库是 `libc` 库的一部分，其例程由 C 编译器按需自动加载。以下各 man 页面的概要章节指明了应使用哪些头文件、函数的编译器声明形式，以及哪些外部变量值得关注。

以下定义为宏；这些名称不可在不先用 `#undef` 移除其当前定义的情况下重新使用：`BUFSIZ`、`EOF`、`FILENAME_MAX`、`FOPEN_MAX`、`L_ctermid`、`L_cuserid`、`L_tmpnam`、`NULL`、`P_tmpdir`、`SEEK_CUR`、`SEEK_END`、`SEEK_SET`、`TMP_MAX`、`clearerr`、`clearerr_unlocked`、`feof`、`feof_unlocked`、`ferror`、`ferror_unlocked`、`fileno`、`fileno_unlocked`、`fropen`、`fwopen`、`getc`、`getc_unlocked`、`getchar`、`getchar_unlocked`、`putc`、`putc_unlocked`、`putchar`、`putchar_unlocked`、`stderr`、`stdin` 和 `stdout`。宏函数 `clearerr`、`clearerr_unlocked`、`feof`、`feof_unlocked`、`ferror`、`ferror_unlocked`、`fileno`、`fileno_unlocked`、`getc`、`getc_unlocked`、`getchar`、`getchar_unlocked`、`putc`、`putc_unlocked`、`putchar` 和 `putchar_unlocked` 存在函数版本，若显式移除宏定义则将使用函数版本。

## 参见

[close(2)](../man2/close.2.md), [open(2)](../man2/open.2.md), [read(2)](../man2/read.2.md), [write(2)](../man2/write.2.md)

## 标准

`libc` 库遵循 ISO/IEC 9899:1999 ("ISO C99") 标准。

## 函数列表

| **函数 描述** |
| --- |
| asprintf 格式化输出转换 |
| clearerr 检查并重置流状态 |
| dprintf 格式化输出转换 |
| fclose 关闭流 |
| fdopen 流打开函数 |
| feof 检查并重置流状态 |
| ferror 检查并重置流状态 |
| fflush 刷新流 |
| fgetc 从输入流获取下一个字符或字 |
| fgetln 从流中获取一行 |
| fgetpos 重定位流 |
| fgets 从流中获取一行 |
| fgetwc 从输入流获取下一个宽字符 |
| fgetws 从流中获取一行宽字符 |
| fileno 将流指针映射到文件描述符 |
| fopen 流打开函数 |
| fprintf 格式化输出转换 |
| fpurge 刷新流 |
| fputc 向流输出字符或字 |
| fputs 向流输出一行 |
| fputwc 向流输出宽字符 |
| fputws 向流输出一行宽字符 |
| fread 二进制流输入/输出 |
| freopen 流打开函数 |
| fropen 打开流 |
| fscanf 输入格式转换 |
| fseek 重定位流 |
| fsetpos 重定位流 |
| ftell 重定位流 |
| funopen 打开流 |
| fwide 设置/获取流方向 |
| fwopen 打开流 |
| fwprintf 格式化宽字符输出转换 |
| fwrite 二进制流输入/输出 |
| getc 从输入流获取下一个字符或字 |
| getchar 从输入流获取下一个字符或字 |
| getdelim 从流中获取一行 |
| getline 从流中获取一行 |
| getw 从输入流获取下一个字符或字 |
| getwc 从输入流获取下一个宽字符 |
| getwchar 从输入流获取下一个宽字符 |
| mkdtemp 创建唯一临时目录 |
| mkstemp 创建唯一临时文件 |
| mktemp 创建唯一临时文件 |
| perror 系统错误消息 |
| printf 格式化输出转换 |
| putc 向流输出字符或字 |
| putchar 向流输出字符或字 |
| puts 向流输出一行 |
| putw 向流输出字符或字 |
| putwc 向流输出宽字符 |
| putwchar 向流输出宽字符 |
| remove 删除目录项 |
| rewind 重定位流 |
| scanf 输入格式转换 |
| setbuf 流缓冲操作 |
| setbuffer 流缓冲操作 |
| setlinebuf 流缓冲操作 |
| setvbuf 流缓冲操作 |
| snprintf 格式化输出转换 |
| sprintf 格式化输出转换 |
| sscanf 输入格式转换 |
| strerror 系统错误消息 |
| swprintf 格式化宽字符输出转换 |
| sys_errlist 系统错误消息 |
| sys_nerr 系统错误消息 |
| tempnam 临时文件例程 |
| tmpfile 临时文件例程 |
| tmpnam 临时文件例程 |
| ungetc 从输入流回退字符 |
| ungetwc 从输入流回退宽字符 |
| vasprintf 格式化输出转换 |
| vdprintf 格式化输出转换 |
| vfprintf 格式化输出转换 |
| vfscanf 输入格式转换 |
| vfwprintf 格式化宽字符输出转换 |
| vprintf 格式化输出转换 |
| vscanf 输入格式转换 |
| vsnprintf 格式化输出转换 |
| vsprintf 格式化输出转换 |
| vsscanf 输入格式转换 |
| vswprintf 格式化宽字符输出转换 |
| vwprintf 格式化宽字符输出转换 |
| wprintf 格式化宽字符输出转换 |

## 缺陷

标准缓冲函数与某些其他库和系统函数交互不佳，尤其是 [vfork(2)](../man2/vfork.2.md)。
