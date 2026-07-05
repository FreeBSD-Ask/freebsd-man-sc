# dtrace.1

`dtrace` — 动态跟踪编译器和跟踪实用程序

## 名称

`dtrace`

## 概要

`dtrace [-32 | -64] [-aACdeFGhHlOqSvVwZ] [--libxo] [-b bufsz] [-c cmd] [-D name[=value]] [-I path] [-L path] [-o output] [-s script] [-U name] [-x arg[=value]] [-X a | c | s | t] [-p pid] [-P provider [[predicate] action]] [-m [provider:]module [[predicate] action]] [-f [[provider:]module:]function [[predicate] action]] [-n [[[provider:]module:]function:]name [[predicate] action]] [-i probe-id [[predicate] action]]`

## 描述

DTrace 是从 Solaris 移植的综合性动态跟踪框架。DTrace 提供了强大的基础设施，使管理员、开发人员和运维人员能够简洁地回答有关操作系统和用户程序行为的任意问题。

`dtrace` 命令提供了对 DTrace 工具所提供核心服务的通用接口，包括：

- 列出 DTrace 当前发布的探针和提供者集合的选项
- 使用任意探针描述说明符（provider、module、function、name）直接启用探针的选项
- 运行 D 编译器并编译一个或多个 D 程序文件或直接在命令行上编写的程序的选项
- 生成匿名跟踪程序的选项
- 生成程序稳定性报告的选项
- 修改 DTrace 跟踪和缓冲行为并启用附加 D 编译器功能的选项

你可以通过在 shebang 声明中使用 `dtrace` 来创建解释器文件，从而编写 D 脚本。也可以使用 `dtrace` 在不实际启用跟踪的情况下尝试编译 D 程序并确定其属性，只需使用 `-e` 选项即可。

## 选项

`-P`、`-m`、`-f`、`-n` 和 `-i` 选项所接受的参数可以包含一个用斜杠括起的可选 D 语言 `predicate`（谓词），以及一个用花括号括起的可选 D 语言 `action`（动作）语句列表。在命令行上指定的 D 程序代码必须适当地加引号，以避免 shell 解释元字符。

支持以下选项：

**`-32` | `-64`** D 编译器使用操作系统内核的本机数据模型生成程序。如果指定了 `-32` 选项，`dtrace` 会强制 D 编译器使用 32 位数据模型编译 D 程序。如果指定了 `-64` 选项，`dtrace` 会强制 D 编译器使用 64 位数据模型编译 D 程序。由于 `dtrace` 默认选择本机数据模型，通常无需指定这些选项。数据模型会影响整数类型的大小和其他语言属性。为任一数据模型编译的 D 程序都可以在 32 位和 64 位内核上执行。`-32` 和 `-64` 选项还决定 `-G` 选项生成的 [elf(5)](../man5/elf.5.md) 文件格式（ELF32 或 ELF64）。

**`-a`** 申领匿名跟踪状态并显示所跟踪的数据。可以将 `-a` 选项与 `-e` 选项组合使用，以强制 `dtrace` 在消费匿名跟踪状态后立即退出，而不是继续等待新数据。

**`-A`** 为匿名跟踪生成指令并将其写入 **/boot/dtrace.dof**。此选项构造一组 dtrace 配置文件指令，启用指定的探针以进行匿名跟踪，然后退出。默认情况下，`dtrace` 尝试将指令存储到文件 **/boot/dtrace.dof**。可以使用 `-o` 选项指定替代的输出文件来修改此行为。

**`-b`** `bufsz` 将主跟踪缓冲区大小设置为 `bufsz`。跟踪缓冲区大小可以包含任意大小后缀 k、m、g 或 t。如果无法分配缓冲区空间，`dtrace` 会根据 bufresize 属性的设置尝试减小缓冲区大小或退出。

**`-c`** `cmd` 运行指定的命令 `cmd` 并在其完成时退出。如果命令行上存在多个 `-c` 选项，`dtrace` 会在所有命令都退出时退出，并在每个子进程终止时报告其退出状态。第一个命令的进程 ID 通过 `$target` 宏变量提供给命令行上指定或使用 `-s` 选项指定的任何 D 程序。

**`-C`** 在编译 D 程序之前对其运行 C 预处理器 [cpp(1)](cpp.1.md)。可以使用 `-D`、`-U`、`-I` 和 `-H` 选项向 C 预处理器传递选项。使用 `-X` 选项可以选择 C 标准符合度。有关 D 编译器在调用 C 预处理器时定义的令牌集合的说明，参见 `-X`。

**`-d`** 在应用语法转换后将 D 脚本转储到标准输出。例如，D 中的 if 语句就是通过此类转换实现的：探针体中的条件子句在编译时被替换为一个以原始条件为谓词的独立探针。

**`-D`** `name`[=`value`] 在调用 [cpp(1)](cpp.1.md) 时定义 `name`（通过 `-C` 选项启用）。如果指定了附加的 `value`，则该名称会被赋予相应的值。此选项将 `-D` 选项传递给每次 [cpp(1)](cpp.1.md) 调用。

**`-e`** 在编译任何请求并消费匿名跟踪状态（`-a` 选项）之后，但在启用任何探针之前退出。可以将此选项与 `-a` 选项组合以打印匿名跟踪数据并退出。也可以将此选项与 D 编译器选项组合。这种组合可在不实际执行程序和启用相应插桩的情况下验证程序是否可编译。

**`-f`** [[`provider`:]`module`:]`function` [[`predicate`] `action`] 指定要跟踪或列出（`-l` 选项）的函数名。相应参数可以包含任意探针描述形式 `provider:module:function`、`module:function` 或 `function`。未指定的探针描述字段留空，并匹配任何探针（无论这些字段的值如何）。如果描述中除 `function` 外未指定其他限定符，则匹配所有具有相应 `function` 的探针。`-f` 参数可以后缀一个可选的 D 探针子句。一次可以在命令行上指定多个 `-f` 选项。

**`-F`** 通过识别函数进入和返回来合并跟踪输出。函数进入探针报告会缩进，其输出前缀为 `->`。函数返回探针报告不缩进，其输出前缀为 `<-`。系统调用进入探针报告会缩进，其输出前缀为 `=>`。系统调用返回探针报告不缩进，其输出前缀为 `<=`。

**`-G`** 生成一个包含嵌入式 DTrace 程序的 ELF 文件。程序中指定的 DTrace 探针保存在一个可重定位的 ELF 对象中，可以链接到另一个程序中。如果存在 `-o` 选项，则使用为该操作数指定的路径名保存 ELF 文件。如果不存在 `-o` 选项，且 DTrace 程序包含在名为 `filename.d` 的文件中，则使用名称 `filename.o` 保存 ELF 文件。否则使用名称 d.out 保存 ELF 文件。

**`-h`** 生成一个头文件，其中包含与指定提供者定义中的探针对应的宏。此选项应用于生成一个头文件，该文件被其他源文件包含，以便稍后与 `-G` 选项一起使用。如果存在 `-o` 选项，则使用为该选项指定的路径名保存头文件。如果不存在 `-o` 选项，且 DTrace 程序包含在名为 `filename.d` 的文件中，则使用名称 `filename.h` 保存头文件。

**`-H`** 调用 [cpp(1)](cpp.1.md) 时打印包含文件的路径名（通过 `-C` 选项启用）。此选项将 `-H` 选项传递给每次 [cpp(1)](cpp.1.md) 调用，使其将路径名列表（每行一个）显示到标准错误。

**`-i`** `probe-id` [[`predicate`] `action`] 指定要跟踪或列出（`-l` 选项）的探针标识符（`probe-id`）。可以使用 `dtrace -l` 所示的十进制整数指定探针 ID。`-i` 参数可以后缀一个可选的 D 探针子句。一次可以指定多个 `-i` 选项。

**`-I`** `path` 在调用 [cpp(1)](cpp.1.md) 时（通过 `-C` 选项启用），将指定的目录 `path` 添加到 #include 文件的搜索路径中。此选项将 `-I` 选项传递给每次 [cpp(1)](cpp.1.md) 调用。指定的 `path` 会插入到搜索路径中默认目录列表之前。

**`-l`** 列出探针而不是启用它们。如果指定了 `-l` 选项，`dtrace` 会生成一份报告，列出与使用 `-P`、`-m`、`-f`、`-n`、`-i` 和 `-s` 选项给出的描述相匹配的探针。如果未指定这些选项中的任何一个，此选项会列出所有探针。

**`-L`** `path` 将指定的目录 `path` 添加到 DTrace 库的搜索路径中。DTrace 库用于包含在编写 D 程序时可使用的通用定义。指定的 `path` 会添加到默认库搜索路径之后。

**`--libxo`** 通过 libxo(3) 生成输出。此选项与指定 **oformat** 相同。

**`-m`** [`provider`:]`module` [[`predicate`] `action`] 指定要跟踪或列出（`-l` 选项）的模块名。相应参数可以包含任意探针描述形式 `provider:module` 或 `module`。未指定的探针描述字段留空，并匹配任何探针（无论这些字段的值如何）。如果描述中除 `module` 外未指定其他限定符，则匹配所有具有相应 `module` 的探针。`-m` 参数可以后缀一个可选的 D 探针子句。一次可以在命令行上指定多个 `-m` 选项。

**`-n`** [[[`provider`:]`module`:]`function`:]`name` [[`predicate`] `action`] 指定要跟踪或列出（`-l` 选项）的探针名。相应参数可以包含任意探针描述形式 `provider:module:function:name`、`module:function:name`、`function:name` 或 `name`。未指定的探针描述字段留空，并匹配任何探针（无论这些字段的值如何）。如果描述中除 `name` 外未指定其他限定符，则匹配所有具有相应 `name` 的探针。`-n` 参数可以后缀一个可选的 D 探针子句。一次可以在命令行上指定多个 `-n` 选项。

**`-O`** 如果指定了 **oformat** 或 `--libxo`，此选项会使 `dtrace` 在退出时打印所有聚合。

**`-o`** `output` 为 `-A`、`-G` 和 `-l` 选项或跟踪数据本身指定 `output` 文件。如果存在 `-A` 选项且不存在 `-o`，默认输出文件为 **/boot/dtrace.dof**。如果存在 `-G` 选项且 `-s` 选项的参数形式为 `filename.d` 且不存在 `-o`，默认输出文件为 `filename.o`。否则默认输出文件为 `d.out`。

**`-p`** `pid` 抓取指定的进程 ID `pid`，缓存其符号表，并在其完成时退出。如果命令行上存在多个 `-p` 选项，`dtrace` 会在所有命令都退出时退出，并在每个进程终止时报告其退出状态。第一个进程 ID 通过 `$target` 宏变量提供给命令行上指定或使用 `-s` 选项指定的任何 D 程序。

**`-P`** `provider` [[`predicate`] `action`] 指定要跟踪或列出（`-l` 选项）的提供者名。其余探针描述字段 module、function 和 name 留空，并匹配任何探针（无论这些字段的值如何）。`-P` 参数可以后缀一个可选的 D 探针子句。一次可以在命令行上指定多个 `-P` 选项。

**`-q`** 设置安静模式。`dtrace` 会抑制诸如指定选项和 D 程序匹配的探针数量之类的消息，并且不打印列标题、CPU ID、探针 ID，也不在输出中插入换行符。只有由 D 程序语句（如 `trace()` 和 `printf()`）跟踪和格式化的数据才会显示到标准输出。

**`-s`** `script` 编译指定的 D 程序源文件。如果存在 `-e` 选项，程序会被编译但不启用插桩。如果存在 `-l` 选项，程序会被编译并列出其匹配的探针集合，但不启用插桩。如果 `-e`、`-l`、`-G` 或 `-A` 均不存在，则启用 D 程序指定的插桩并开始跟踪。

**`-S`** 显示 D 编译器中间代码。D 编译器会为每个 D 程序生成一份中间代码报告到标准错误。

**`-U`** `name` 在调用 [cpp(1)](cpp.1.md) 时取消定义指定的 `name`（通过 `-C` 选项启用）。此选项将 `-U` 选项传递给每次 [cpp(1)](cpp.1.md) 调用。

**`-v`** 设置详细模式。如果指定了 `-v` 选项，`dtrace` 会生成一份程序稳定性报告，显示指定 D 程序的最小接口稳定性和依赖级别。

**`-V`** 报告 `dtrace` 支持的最高 D 编程接口版本。版本信息会打印到标准输出，然后 `dtrace` 命令退出。

**`-w`** 允许在使用 `-s`、`-P`、`-m`、`-f`、`-n` 或 `-i` 选项指定的 D 程序中使用破坏性动作。如果未指定 `-w` 选项，`dtrace` 不允许编译或启用包含破坏性动作的 D 程序。将 `security.bsd.allow_destructive_dtrace` [loader(8)](../man8/loader.8.md) 可调参数设置为 `0` 可彻底禁止在任何时候在系统范围内启用破坏性动作。任何尝试启用破坏性动作的企图都会导致 `dtrace` 以运行时错误退出。

**`-x`** `arg`[=`value`] 启用或修改 DTrace 运行时选项或 D 编译器选项。布尔选项通过指定其名称来启用。带值的选项通过用等号（=）分隔选项名和值来设置。`size` 参数可以后缀 `K`、`M`、`G` 或 `T`（大小写均可）之一，分别表示千字节、兆字节、吉字节或太字节的倍数。`time` 参数可以后缀 `ns`、`nsec`、`us`、`usec`、`ms`、`msec`、`s`、`sec`、`m`、`min`、`h`、`hour`、`d`、`day`、`hz` 之一。如果未指定后缀，则以 `hz` 为单位。

支持以下运行时和编译器选项：

**`aggrate`=`time`** 聚合读取速率。

**`aggsize`=`size`** 聚合缓冲区大小。

**`bufpolicy`=`fill`|`switch`|`ring`** 指定主缓冲区的缓冲策略。

**`bufresize`=`auto`|`manual`** 缓冲区调整大小策略。

**`bufsize`=`size`** 每 CPU 主缓冲区大小。与 `-b` 标志相同。

**`cleanrate`=`time`** 清理速率。必须使用 “`hz`” 后缀以每秒次数指定。

**`cpu`=`scalar`** 指定要启用跟踪的 CPU。

**`cpp`** 对输入文件运行 C 预处理器。与 `-C` 标志相同。

**`cpppath`=`path`** 为 C 预处理器使用指定的路径，而不是在 `PATH` 中搜索 “cpp”。

**`defaultargs`** 允许引用未指定的宏参数。

**`destructive`** 允许破坏性动作。与 `-w` 标志相同。

**`dynvarsize`=`size`** 动态变量空间大小。

**`evaltime`=`exec | preinit | postinit | main`** 进程创建模式。使用 `-c` `cmd` 启动命令时，`dtrace` 会先停止新启动的 `cmd`，求值 [d(7)](../man7/d.7.md) 程序，然后恢复 `cmd`。`evaltime` 选项控制此操作发生的精确时刻。下表描述了支持的模式。通常无需更改默认模式，但在共享库跟踪等情况下可能比较方便。

| Mode | D 程序求值时机 |
| --- | --- |
| `exec` | 命令 `cmd` 执行的第一条指令处。 |
| `preinit` | [elf(5)](../man5/elf.5.md) 的 “.init” 段之前。 |
| `postinit` | [elf(5)](../man5/elf.5.md) 的 “.init” 段之后。FreeBSD 上的默认值。 |
| `main` | `main()` 函数的第一条指令之前。 |

**`flowindent`** 打开流缩进。与 `-F` 标志相同。

**`grabanon`** 申领匿名状态。与 `-a` 标志相同。

**`jstackframes`=`scalar`** `jstack()` 的默认栈帧数。

**`jstackstrsize`=`scalar`** `jstack()` 的默认字符串空间大小。

**`ldpath`=`path`** 指定 `-G` 时，为静态链接器使用指定的路径，而不是在 `PATH` 中搜索 “ld”。

**`libdir`=`path`** 向系统库路径添加目录。

**`nspec`=`scalar`** 推测数量。

**`nolibs`** 不加载 D 系统库。

**`quiet`** 设置安静模式。与 `-q` 标志相同。

**`specsize`=`size`** 推测缓冲区大小。

**`strsize`=`size`** 字符串的最大大小。

**`stackframes`=`scalar`** 执行 `stack()` 动作时回溯的内核空间栈帧最大数量。

**`stackindent`=`scalar`** 缩进 `stack()` 和 `ustack()` 输出时使用的空白字符数。

**`oformat`=`format`** 指定用于输出的格式。将 **oformat** 设置为 `text` 会使 `dtrace` 使用常规的人类可读输出，这是其默认行为。传递给 **oformat** 的选项会直接转发给 libxo(3)。支持的格式化程序包括 `json`、`xml` 和 `html`。请注意，除非显式调用打印函数或指定了 `-O` 标志，否则此选项会导致 `dtrace` 不产生任何输出。更多信息参见“结构化输出”一节。

**`statusrate`=`time`** 状态检查速率。

**`switchrate`=`time`** 缓冲区切换速率。

**`syslibdir`=`path`** 系统库路径。默认为 **/usr/lib/dtrace**。

**`ustackframes`=`scalar`** 执行 `ustack()` 动作时回溯的用户空间栈帧最大数量。

**`-X`** `a | c | s | t` 指定调用 [cpp(1)](cpp.1.md) 时（通过 `-C` 选项启用）应选择的 ISO C 标准符合度。`-X` 选项参数根据参数字母的值影响 __STDC__ 宏的值和存在性。`-X` 选项支持以下参数：

**`a`** 默认。ISO C 加 K&R 兼容性扩展，以及 ISO C 所要求的语义更改。如果未指定 `-X`，这是默认模式。当 [cpp(1)](cpp.1.md) 与 `-Xa` 选项一起调用时，预定义宏 __STDC__ 的值为 0。

**`c`** 符合。严格符合 ISO C，不带 K&R C 兼容性扩展。当 [cpp(1)](cpp.1.md) 与 `-Xc` 选项一起调用时，预定义宏 __STDC__ 的值为 1。

**`s`** 仅 K&R C。当 [cpp(1)](cpp.1.md) 与 `-Xs` 选项一起调用时，不定义宏 __STDC__。

**`t`** 过渡。ISO C 加 K&R C 兼容性扩展，不带 ISO C 所要求的语义更改。当 [cpp(1)](cpp.1.md) 与 `-Xt` 选项一起调用时，预定义宏 __STDC__ 的值为 0。

由于 `-X` 选项仅影响 D 编译器如何调用 C 预处理器，从 D 的角度看 `-Xa` 和 `-Xt` 选项是等价的，二者都只是为了方便复用 C 构建环境中的设置。

无论何种 `-X` 模式，以下附加的 C 预处理器定义始终被指定且在所有模式下都有效：

- __sun
- __unix
- __SVR4
- __i386（仅在编译 32 位程序时的 x86 系统上）
- __amd64（仅在编译 64 位程序时的 x86 系统上）
- __`uname -s`_`uname -r`（例如 `FreeBSD_9.2-RELEASE`）
- __SUNW_D=1
- __SUNW_D_VERSION=0x`MMmmmuuu`，其中 `MM` 是主版本值（十六进制），`mmm` 是次版本值（十六进制），`uuu` 是微版本值（十六进制）

**`-Z`** 允许匹配零个探针的探针描述。如果未指定 `-Z` 选项，当 D 程序文件（`-s` 选项）或命令行上（`-P`、`-m`、`-f`、`-n` 或 `-i` 选项）指定的任何探针描述包含不匹配任何已知探针的描述时，`dtrace` 会报告错误并退出。

## 结构化输出

`dtrace` 支持使用 libxo(3) 进行结构化输出。输出始终有一个名为 “dtrace” 的顶级对象，后跟一个 “probes” 对象列表。每个探针对象都有一个时间戳（在输出时而非探针触发时生成）、一个执行该探针的 CPU 标识符，以及探针的完整规范：

```sh
{
  "dtrace": {
    "probes": [
      {
        "timestamp": ...,
        "cpu": ...,
        "id": ...,
        "provider": ...,
        "module": ...,
        "function": ...,
        "name": ...,
        "output": [
           ... （脚本特定输出）
        ]
      }
    ]
  }
}
<?xml version="1.0"?>
<dtrace>
  <probes>
    <timestamp>...</timestamp>
    <cpu>...</cpu>
    <id>...</id>
    <provider>...</provider>
    <module>...</module>
    <function>...</function>
    <name>...</name>
    <output>
      ... （脚本特定输出）
    </output>
  </probes>
</dtrace>
```

如果某些字段为空（在本例中，module 和 function 值缺失），XML 输出也可能采用以下形式：

```sh
<?xml version="1.0"?>
<dtrace>
  <probes>
    ...
    <module/>
    <function/>
    ...
    <output>
      ... （脚本特定输出）
    </output>
  </probes>
</dtrace>
```

类似地，**oformat** 可用于生成 HTML：

```sh
<div class="line">
<div class="data" data-tag="timestamp">...</div>
<div class="text"></div>
<div class="data" data-tag="cpu">...</div>
<div class="text"></div>
<div class="data" data-tag="id">...</div>
<div class="text"></div>
<div class="data" data-tag="provider">...</div>
<div class="text"></div>
<div class="data" data-tag="module">...</div>
<div class="text"></div>
<div class="data" data-tag="function">...</div>
<div class="text"></div>
<div class="data" data-tag="name">...</div>
<div class="data" data-tag="... （脚本特定输出）">...</div>
</div>
```

与 JSON 和 XML 不同，不存在 “output” 数组。相反，数据被简单地格式化为类 “data” 的 div，每个键都关联一个 data-tag。

“output” 数组的内容取决于探针的动作，下文将加以说明。此处的示例以 JSON 形式呈现，而非 XML 或 HTML，但上述转换适用于所有输出格式。

任何标量输出（例如由 `trace()` 动作产生的输出）形式如下：

```sh
{
  "value": ...
}
```

`printf()` 动作以一个包含 `printf()` 动作格式化输出的对象开始。后续对象以原始形式包含 `printf()` 各参数的值，就像使用了 `trace()` 动作一样。一条不包含消息以外参数的 `printf()` 语句在消息对象之后只会有一个对象，其值始终为 0。这是实现的产物，可安全忽略。

```sh
# dtrace --libxo json,pretty -n 'BEGIN { printf("... %Y, ..", walltimestamp); }'
{
  "message": "... 2023 Sep  7 16:49:02, .."
},
{
  "value": 1694105342633402400
},
{
  ...
}
```

标量聚合是为给定键生成单个值的聚合。这些聚合包括 `count()`、`min()`、`max()`、`stddev()` 和 `sum()`。它们中的每一个都由包含其名称的键表示。例如，`stddev()` 聚合的输出会在一个 “aggregation-data” 对象中包含一个键 “stddev”：

```sh
{
  "aggregation-data": [
    {
      "keys": [
        ...
      ],
      "stddev": ...
    }
  ],
  "aggregation-name": ...
}
```

“keys” 字段在所有聚合中保持一致，但 `quantize()`、`lquantize()` 和 `llquantize()` 需要不同处理。**oformat** 会创建一个名为 “buckets” 的新对象数组。每个对象包含一个 “value” 和一个 “count” 字段，分别是人类可读的 `dtrace` 输出的左侧和右侧。完整对象格式如下：

```sh
{
  "aggregation-data": [
    ...
    {
      "keys": [
        ...
      ],
      "buckets": [
        {
          "value": 32,
          "count": 0
        },
        {
          "value": 64,
          "count": 17
        },
        ...
      ],
    },
    ...
  ]
  "aggregation-name": ...
}
```

与标量聚合类似，命名的标量动作（如 `mod()`、`umod()`、`usym()`、`tracemem()` 和 `printm()`）会输出一个对象，其键等于动作名。例如，`printm()` 输出会产生以下对象：

```sh
{
  "printm": "0x4054171100"
}
```

`sym()` 略有不同。虽然它会创建一个包含其值的 “sym” 字段，但在某些情况下它还会创建附加字段 “object”、“name” 和 “offset”：

```sh
# dtrace -x oformat=json,pretty -On 'BEGIN { sym((uintptr_t)&`prison0); }'
{
  "sym": "kernel`prison0",
  "object": "kernel",
  "name": "prison0"
}
# dtrace --libxo json,pretty -On 'BEGIN { sym((uintptr_t)curthread); }'
{
  "sym": "0xfffffe00c18d2000",
  "offset": "0xfffffe00c18d2000"
}
```

`stack()` 和 `ustack()` 动作将每个栈帧展开为数组中的独立对象。它们之间唯一的真正区别是 `stack()` 动作会生成一个名为 “stack-frames” 的列表，而 `ustack()` 会生成一个名为 “ustack-frames” 的列表。以下是其 **oformat** 输出的示例：

```sh
{
  "stack-frames": [
    {
      "symbol": "dtrace.ko`dtrace_dof_create+0x35",
      "module": "dtrace.ko",
      "name": "dtrace_dof_create",
      "offset": "0x35"
    },
    {
      "symbol": "dtrace.ko`dtrace_ioctl+0x81c",
      "module": "dtrace.ko",
      "name": "dtrace_ioctl",
      "offset": "0x81c"
    },
    ...
  ]
}
{
  "ustack-frames": [
    {
      "symbol": "libc.so.7`ioctl+0xa",
      "module": "libc.so.7",
      "name": "ioctl",
      "offset": "0xa"
    },
    {
      "symbol": "libdtrace.so.2`dtrace_go+0xf3",
      "module": "libdtrace.so.2",
      "name": "dtrace_go",
      "offset": "0xf3"
    },
    ...
  ]
}
```

`print()` 动作产生以下形式的 “type” 列表：

```sh
{
  "type": [
    {
      "object-name": "kernel",
      "name": "struct thread",
      "ctfid": 2372
    },
    {
      "member-name": "td_lock",
      "name": "struct mtx *volatile",
      "ctfid": 2035,
      "value": "0xffffffff82158440"
    },
    ...
}
```

如果类型无效，将产生一个 “warning” 对象，其中包含诊断消息以及两个可能的可选字段：包含该类型 CTF 标识符的 “type-identifier” 和包含整数、枚举或浮点数大小的 “size”。生成的字段取决于处理跟踪数据时遇到的错误类型。

最后，**oformat** 提供了一个特殊的伪探针来表示丢弃。由于 `dtrace` 轮询各种类型的丢弃，**oformat** 会产生类似以下的输出来表示丢弃：

```sh
{
  "cpu": -1,
  "id": -1,
  "provider": "dtrace",
  "module": "INTERNAL",
  "function": "INTERNAL",
  "name": "DROP",
  "timestamp": ...,
  "count": ...,
  "total": ...,
  "kind": 2,
  "msg": "... dynamic variable drops\n"
}
```

## 操作数

你可以在 `dtrace` 命令行上指定零个或多个附加参数来定义一组宏变量等。附加参数可用于使用 `-s` 选项或在命令行上指定的 D 程序中。

## 环境变量

**`DTRACE_DEBUG`** 定义时，`dtrace` 会将调试日志消息输出到 stderr(4)。

## 文件

**/boot/dtrace.dof** 用于匿名跟踪指令的文件。

## 退出状态

返回以下退出状态：

**0** 成功完成。对于 D 程序请求，退出状态 0 表示程序编译成功、探针启用成功或匿名状态检索成功。即使指定的跟踪请求遇到错误或丢弃，`dtrace` 也返回 0。

**1** 发生错误。对于 D 程序请求，退出状态 1 表示程序编译失败或无法满足指定请求。

**2** 指定了无效的命令行选项或参数。

## 诊断

- dtrace: could not enable tracing: Permission denied（dtrace：无法启用跟踪：权限被拒绝） 当 `dtrace` 因 `security.bsd.allow_destructive_dtrace` 在 loader.conf(5) 中被设置为 `0` 而无法启用破坏性动作时，可能会发生此错误。

## 参见

[cpp(1)](cpp.1.md), dwatch(1), [dtrace_audit(4)](../man4/dtrace_audit.4.md), [dtrace_callout_execute(4)](../man4/dtrace_callout_execute.4.md), [dtrace_cam(4)](../man4/dtrace_cam.4.md), [dtrace_dtmalloc(4)](../man4/dtrace_dtmalloc.4.md), [dtrace_dtrace(4)](../man4/dtrace_dtrace.4.md), [dtrace_fbt(4)](../man4/dtrace_fbt.4.md), [dtrace_io(4)](../man4/dtrace_io.4.md), [dtrace_ip(4)](../man4/dtrace_ip.4.md), [dtrace_kinst(4)](../man4/dtrace_kinst.4.md), [dtrace_lockstat(4)](../man4/dtrace_lockstat.4.md), [dtrace_mib(4)](../man4/dtrace_mib.4.md), [dtrace_pid(4)](../man4/dtrace_pid.4.md), [dtrace_proc(4)](../man4/dtrace_proc.4.md), [dtrace_priv(4)](../man4/dtrace_priv.4.md), [dtrace_profile(4)](../man4/dtrace_profile.4.md), [dtrace_sched(4)](../man4/dtrace_sched.4.md), [dtrace_sctp(4)](../man4/dtrace_sctp.4.md), [dtrace_syscall(4)](../man4/dtrace_syscall.4.md), [dtrace_tcp(4)](../man4/dtrace_tcp.4.md), [dtrace_udp(4)](../man4/dtrace_udp.4.md), [dtrace_udplite(4)](../man4/dtrace_udplite.4.md), [dtrace_vfs(4)](../man4/dtrace_vfs.4.md), [elf(5)](../man5/elf.5.md), [d(7)](../man7/d.7.md), [tracing(7)](../man7/tracing.7.md), [SDT(9)](../man9/SDT.9.md)

> "Solaris Dynamic Tracing Guide"

## 历史

`dtrace` 实用程序首次出现于 FreeBSD 7.1。
