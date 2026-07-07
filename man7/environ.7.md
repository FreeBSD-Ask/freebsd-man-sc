# environ(7)

`environ` — 用户环境

## 名称

`environ`

## 概要

`extern char **environ;`

## 描述

进程开始时，execve(2) 向每个进程提供一个称为 `environment` 的字符串数组。按照惯例，这些字符串具有 `name`=`value` 的形式，并称为“环境变量”。进程可分别使用 getenv(3)、setenv(3) 和 unsetenv(3) 函数查询、更新和删除这些字符串。shell 也提供操作环境的命令；它们在相应的 shell 手册页中描述。

以下是 UNIX 系统上通常可见的环境变量列表。它仅包括用户在日常使用系统时预期可见的变量，远非完整。特定程序或库函数专属的环境变量记录在相应手册页的 Sx ENVIRONMENT 章节中。

## 环境变量

```sh
env TZ=America/Los_Angeles date
```

**`ARCHLEVEL`** 在 *amd64* 上，控制使用的 SIMD 增强级别。详情参见 [simd(7)](simd.7.md)。

**`BLOCKSIZE`** 几个与磁盘相关的命令使用的块单位尺寸，最显著的是 [df(1)](../man1/df.1.md)、[du(1)](../man1/du.1.md) 和 [ls(1)](../man1/ls.1.md)。`BLOCKSIZE` 可以通过指定数字以字节为单位指定，通过指定数字后跟 `K` 或 `k` 以千字节为单位指定，通过指定数字后跟 `M` 或 `m` 以兆字节为单位指定，通过指定数字后跟 `G` 或 `g` 以千兆字节为单位指定。小于 512 字节或大于 1 千兆字节的尺寸将被忽略。此变量由 getbsize(3) 函数处理。

**`COLUMNS`** 用户偏好的终端列宽位置。诸如 [ls(1)](../man1/ls.1.md) 和 [who(1)](../man1/who.1.md) 等实用程序使用此值将输出格式化为列。如果未设置或为空，实用程序将使用 ioctl(2) 调用询问终端驱动程序以获取宽度。

**`EDITOR`** 默认编辑器名称。

**`EXINIT`** ex(1) 和 [vi(1)](../man1/vi.1.md) 读取的启动命令列表。

**`EXTERROR_VERBOSE`** 请求 err(3) 和 uexterr_gettext 函数无条件报告附加信息，主要对（内核）开发者诊断问题有用。更多细节参见 err(3) 和 [exterror(9)](../man9/exterror.9.md)。

**`HOME`** 用户登录目录，由 [login(1)](../man1/login.1.md) 从密码文件 [passwd(5)](../man5/passwd.5.md) 设置。

**`LANG`** 此变量配置所有使用 setlocale(3) 的程序使用指定的区域设置，除非设置了 `LC_*` 变量。

**`LC_ALL`** 覆盖 `LC_COLLATE`、`LC_CTYPE`、`LC_MESSAGES`、`LC_MONETARY`、`LC_NUMERIC`、`LC_TIME` 和 `LANG` 的值。

**`LC_COLLATE`** 用于字符串排序的区域设置。

**`LC_CTYPE`** 用于字符分类（字母、空格、数字等）和将字节序列解释为多字节字符的区域设置。

**`LC_MESSAGES`** 用于诊断消息的区域设置。

**`LC_MONETARY`** 用于解释货币输入和格式化输出的区域设置。

**`LC_NUMERIC`** 用于解释数字输入和格式化输出的区域设置。

**`LC_TIME`** 用于解释日期输入和格式化输出的区域设置。

**`MAIL`** 用户邮箱的位置，而非 /var/mail 中的默认位置，由 mail(1)、[sh(1)](../man1/sh.1.md) 和许多其他邮件客户端使用。

**`MANPATH`** [man(1)](../man1/man.1.md) 查找手册页时搜索的以冒号分隔的目录序列。

**`NLSPATH`** 为 `LC_MESSAGES` 引用的消息目录搜索的目录列表。参见 catopen(3)。

**`PAGER`** 默认分页程序。此变量指定的程序由 mail(1)、[man(1)](../man1/man.1.md)、[ftp(1)](../man1/ftp.1.md) 等用于显示超过当前显示长度的信息。

**`PATH`** [csh(1)](../man1/csh.1.md)、[sh(1)](../man1/sh.1.md)、system(3)、execvp(3) 等查找可执行文件时搜索的以冒号分隔的目录序列。`PATH` 最初由 [login(1)](../man1/login.1.md) 设置为 ``/usr/bin:/bin''。

**`POSIXLY_CORRECT`** 设置为任何值时，此环境变量修改某些命令的行为以（主要）严格符合 POSIX 的方式执行。

**`PRINTER`** lpr(1)、lpq(1) 和 lprm(1) 使用的默认打印机名称。

**`PWD`** 当前目录路径名。

**`SHELL`** 用户登录 shell 的完整路径名。

**`TERM`** 准备输出所针对的终端类型。此信息由命令使用，如 nroff(1)（`ports/textproc/groff`）或 plot(1)，它们可能利用特殊终端能力。终端类型列表参见 `/usr/share/misc/termcap`（termcap(5)）。

**`TERMCAP`** 描述 `TERM` 中终端的字符串，或者如果以 '/' 开头，则为 termcap 文件名。参见下文的 `TERMPATH`，以及 termcap(5)。

**`TERMPATH`** 以冒号或空格分隔的 termcap 文件路径名序列，按列出顺序搜索终端描述。没有 `TERMPATH` 等效于 `TERMPATH` 为 `$HOME/.termcap:/etc/termcap`。如果 `TERMCAP` 包含完整路径名，则忽略 `TERMPATH`。

**`TMPDIR`** 存储临时文件的目录。大多数应用程序使用 `/tmp` 或 `/var/tmp`。设置此变量将使它们使用其他目录。

**`TZ`** 显示日期时使用的时区。正常格式是相对于 `/usr/share/zoneinfo` 的路径名。例如，该命令显示加利福尼亚的当前时间。更多信息参见 tzset(3)。

**`USER`** 用户的登录名。建议可移植应用程序改用 `LOGNAME`。

可通过 `export` 命令和 [sh(1)](../man1/sh.1.md) 中的 `name=value` 参数，或如果使用 [csh(1)](../man1/csh.1.md) 通过 `setenv` 命令将更多名称放入环境中。更改 `.profile` 文件频繁导出的某些 [sh(1)](../man1/sh.1.md) 变量（如 `MAIL`、`PS1`、`PS2` 和 `IFS`）是不明智的，除非你知道自己在做什么。

当前环境变量可用 [sh(1)](../man1/sh.1.md) 中的 [env(1)](../man1/env.1.md)、set(1) 或 [printenv(1)](../man1/printenv.1.md) 打印，或 [csh(1)](../man1/csh.1.md) 中的 [env(1)](../man1/env.1.md)、[printenv(1)](../man1/printenv.1.md) 或 `printenv` 内建命令打印。

## 参见

cd(1), [csh(1)](../man1/csh.1.md), [env(1)](../man1/env.1.md), err(3), ex(1), [login(1)](../man1/login.1.md), [printenv(1)](../man1/printenv.1.md), [sh(1)](../man1/sh.1.md), execve(2), execle(3), getbsize(3), getenv(3), setenv(3), setlocale(3), system(3), termcap(3), termcap(5), [simd(7)](simd.7.md), [exterror(9)](../man9/exterror.9.md)

## 历史

`environ` 手册页出现于 Version 7 AT&T UNIX。
