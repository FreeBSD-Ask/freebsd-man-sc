# mdocml(1)

`mandoc` — 格式化手册页

## 名称

`mandoc`

## 概要

`mandoc [-ac] [-I os=name] [-K encoding] [-mdoc | -man] [-O options] [-T output] [-W level] [file]`

## 描述

`mandoc` 实用程序用于格式化手册页以便显示。

默认情况下，`mandoc` 从标准输入读取 mdoc(7) 或 man(7) 文本，并产生 `-T` `locale` 输出。

选项如下：

> .\" -*- [...; ] coding: encoding; -*-

- 如果输入文件的前三个字节是 UTF-8 字节顺序标记（BOM，0xefbbbf），输入按 `utf-8` 解释。
- 如果输入文件的第一行或第二行匹配 **emacs** 模式行格式，则按 `encoding` 解释输入。
- 如果文件中第一个非 ASCII 字节引入了有效的 UTF-8 序列，输入按 `utf-8` 解释。
- 否则，输入按 `iso-8859-1` 解释。

**`-a`** 如果标准输出是终端设备且未指定 `-c`，则使用 [less(1)](less.1.md) 对输出分页，如同 [man(1)](man.1.md) 那样。

**`-c`** 将格式化后的手册页复制到标准输出，不使用 [less(1)](less.1.md) 分页。这是默认行为。可指定以覆盖 `-a`。

**`-I`** `os`=`name` 覆盖 mdoc(7) `Os` 和 man(7) `TH` 宏的默认操作系统 `name`。

**`-K`** `encoding` 指定输入编码。支持的 `encoding` 参数为 `us-ascii`、`iso-8859-1` 和 `utf-8`。如果未指定，自动检测使用以下列表中第一个匹配项：

**`-mdoc`** | **`-man`** 使用 `-mdoc` 时，所有输入文件按 mdoc(7) 解释。使用 `-man` 时，所有输入文件按 man(7) 解释。默认情况下，对每个文件自动检测输入语言：如果第一个宏是 `Dd` 或 `Dt`，使用 mdoc(7) 解析器；否则使用 man(7) 解析器。对于其他参数，`-m` 被静默忽略。

**`-O`** `options` 以逗号分隔的输出选项。参见各个输出格式的描述以了解支持的 `options`。

**`-T`** `output` 选择输出格式。支持的 `output` 参数值为 `ascii`、`html`、默认的 `locale`、`man`、`markdown`、`pdf`、`ps`、`tree` 和 `utf8`。特殊的 `-T` `lint` 模式仅解析输入，不产生输出。它隐含 `-W` `all`，并将通常出现在标准错误输出上的解析器消息重定向到标准输出。

**`-W`** `level` 指定在标准错误输出上报告并影响退出状态的最低消息 `level`。`level` 可以是 `base`、`style`、`warning`、`error` 或 `unsupp`。`base` 级别自动从 `Os` 宏内容、`-Ios` 命令行选项或 uname(3) 返回值推导操作系统。`openbsd` 和 `netbsd` 级别是 `base` 的变体，绕过自动检测，请求验证特定操作系统的基本系统约定。`all` 级别是 `base` 的别名。默认情况下，`mandoc` 保持静默。详见 “退出状态” 和 “诊断”。特殊选项 `-W` `stop` 告知 `mandoc` 在解析导致至少达到请求级别的警告或错误的文件后退出。该文件不会产生格式化输出。如果同时请求 `level` 和 `stop`，可以用逗号连接，例如 `-W` `error`,`stop`。

**`file`** 从给定输入文件读取。如果指定多个文件，按给定顺序处理。如果未指定，`mandoc` 从标准输入读取。

选项 `-fhklw` 也受支持，详见 [man(1)](man.1.md)。在 `-f` 和 `-k` 模式下，`mandoc` 还支持 [apropos(1)](apropos.1.md) 手册中描述的 `-CMmOSs` 选项。选项 `-fkl` 互斥，相互覆盖。

### ASCII 输出

使用 `-T` `ascii` 强制以 [ascii(7)](../man7/ascii.7.md) 手册页中记录的 7 位 ASCII 字符编码进行文本输出，忽略环境中设置的 locale(1)。

字体样式通过退格编码应用，使得下划线字符 ‘c’ 渲染为 ‘_`\[bs]`c’，其中 ‘`\[bs]`’ 是退格字符编号 8。粗体字符渲染为 ‘c`\[bs]`c’。此标记通常由分页器或 ul(1) 转换为适当的终端序列。要去除标记，可将输出通过 col(1) `-b` 处理。

mandoc_char(7) 中记录的特殊字符以 ASCII 等价物尽力渲染。特别是，开闭 ‘单引号’ 分别表示为字符编号 0x60 和 0x27，这与从 1965 年到最新修订版（2012 年）的所有 ASCII 标准一致，也匹配 roff(7) 格式化器在 ASCII 输出中表示单引号的传统方式。这种正确的 ASCII 渲染在使用现代 Unicode 兼容字体时可能看起来奇怪，因为与 ASCII 不同，Unicode 仅将码点 U+0060 用于重音符号，从不用于开引号。

接受以下 `-O` 参数：

**`indent`** =`indent` 普通文本的左边距设置为 `indent` 个空格字符，而非默认的五个。不建议增加此值；可能导致格式变差，例如行溢出或不美观的换行。当输出到宽度小于 66 列的终端上的分页器时，默认值减少为三列。

**`tag`** [=`term`] 如果格式化后的手册页在分页器中打开，跳转到 `term` 的定义处，而非从头显示手册页。如果未指定 `term`，重用第一个不是 `section` 编号的命令行参数。如果该参数为 [apropos(1)](apropos.1.md) 的 `key`=`val` 格式，则仅使用 `val` 而非整个参数。这对于 `man -akO tag Ic=ulimit` 之类的命令很有用，可搜索关键字并直接跳转到匹配手册页中的定义。

**`width`** =`width` 输出宽度设置为 `width`，而非默认的 78。当输出到宽度小于 79 列的终端上的分页器时，默认值减少为比终端宽度小一。在任何情况下，以字面模式输出的行从不换行，可能超出输出宽度。

### HTML 输出

`-T` `html` 产生的输出符合 HTML5，使用可选的自闭合标签。从 eqn(7) 块渲染的方程使用 MathML。非 ASCII 字符渲染为十六进制 Unicode 字符引用。

接受以下 `-O` 参数：

```sh
MANPAGER='lynx -force_html' man -T html -O tag=MANPAGER man
MANPAGER='w3m -T text/html' man -T html -O tag=toc mandoc
```

**`fragment`** 省略 <!DOCTYPE> 声明以及 <html>、<head> 和 <body> 元素，仅输出 <body> 元素下方的子树。`style` 参数将被忽略。这在将手册内容嵌入现有文档时很有用。

**`includes`** =`fmt` 字符串 `fmt`（例如 `../src/%I.html`）用作链接头文件（通常通过 `In` 宏）的模板。‘%I’ 的实例替换为包含文件名。默认不呈现超链接。

**`man`** =`fmt`[;`fmt`] 字符串 `fmt`（例如 `../html%S/%N.%S.html`）用作链接手册（通常通过 `Xr` 宏）的模板。‘%N’ 和 ‘%S’ 的实例分别替换为所链接手册的名称和章节。如果未包含章节，则假定章节 1。默认不呈现超链接。如果给出两种格式且当前目录中存在文件 `%N.%S`，则使用第一种格式；否则使用第二种格式。

**`style`** =`style.css` 文件 `style.css` 用作外部样式表。必须是有效的绝对或相对 URI。推荐使用随 `mandoc` 分发的 `mandoc.css` 文件。它提供类似于终端输出的外观，以及 `mandoc` HTML 输出特有的额外功能，特别是通过在支持深链接的锚点位置加下划虚线使其在视觉上突出，提供显示元素语义功能（宏名称）的工具提示，提供响应式 Web 设计的某些简单方面，以及为偏好深色配色方案的用户提供简单支持。可以使用自定义 CSS 文件，但编写它需要精通 HTML 5、CSS 4 和 mdoc(7) 所有语言，以及熟悉 `mandoc.css` 中使用的 `mandoc` 特定类。此外，虽然 `mandoc.css` 文件始终适应与其一起分发的 `mandoc` 版本生成的 HTML 输出，但维护自定义 CSS 文件通常需要在每次 `mandoc` 升级到新版本时进行调整。如果未通过 `-O` `style` 指定样式表，`-T` `html` 会在 HTML 输出中嵌入一个最小样式表，主要用于为各种宏选择适当的 font-style 和 font-weight 属性。结果在任何图形或基于文本的 Web 浏览器中都可读，但不追求看起来类似于终端输出。相反，格式化主要留给浏览器默认设置和浏览器配置中的用户设置。

**`tag`** [=`term`] 语法和语义与 “ASCII 输出” 相同。这通过向分页器传递以片段标识符结尾的 `file://` URI 实现，而非仅传递文件名。使用此参数时，请使用支持此类 URI 的分页器，例如：因此，对于 HTML 输出，此参数不适用于 [more(1)](less.1.md) 或 [less(1)](less.1.md)。例如，`MANPAGER=less man -T html -O tag=toc mandoc` 不起作用，因为 [less(1)](less.1.md) 不支持 `file://` URI。

**`toc`** 如果输入文件包含至少两个非标准章节，在输出开头附近打印目录。

### Locale 输出

默认情况下，`mandoc` 根据当前 locale(1) 自动选择 UTF-8 或 ASCII 输出。如果环境变量 `LC_ALL`、`LC_CTYPE` 或 `LANG` 中任一被设置且第一个被设置的选择了 UTF-8 字符编码，则产生 “UTF-8 输出”；否则回退到 “ASCII 输出”。此输出模式也可通过 `-T` `locale` 显式选择。

### Man 输出

使用 `-T` `man` 将 mdoc(7) 输入翻译为 man(7) 输出格式。这对于向缺乏 mdoc(7) 格式器的传统系统分发手册源码很有用。不支持嵌入的 eqn(7) 和 tbl(7) 代码。

如果文件的输入格式为 man(7)，输入被复制到输出。解析器也会运行，与通常一样，`-W` 级别控制在将输入复制到输出之前显示哪些 “诊断”。

### Markdown 输出

使用 `-T` `markdown` 将 mdoc(7) 输入翻译为符合 John Gruber 2004 年规范（<https://daringfireball.net/projects/markdown/syntax.text>）的 markdown 格式。输出也几乎符合 CommonMark 规范（<https://commonmark.org/>）。

markdown 输出使用的字符集为 ASCII。非 ASCII 字符编码为 HTML 实体。由于在字面字体上下文中不可能这样做（因为这些在 markdown 输出中渲染为代码跨段和代码块），非 ASCII 字符在这些上下文中被音译为 ASCII 近似值。

Markdown 是一种非常弱的标记语言，因此所有语义标记都会丢失，甚至部分表现标记也可能丢失。不要将其用作转换为 HTML 的中间步骤；应直接使用 `-T` `html`。

man(7)、tbl(7) 和 eqn(7) 输入语言不被 `-T` `markdown` 输出模式支持。

### PDF 输出

可通过 `-T` `pdf` 生成 PDF-1.1 输出。`-O` 参数和默认值参见 “PostScript 输出”。

### PostScript 输出

可通过 `-T` `ps` 生成 PostScript "Adobe-3.0" Level-2 页面。输出页面默认为 letter 大小，以 Times 字体族、11 磅渲染。页边距按页面长度和宽度的 1/9 计算。行高为 1.4m。

特殊字符的渲染与 “ASCII 输出” 相同。

接受以下 `-O` 参数：

**`paper`** =`name` 纸张大小 `name` 可为 `a3`、`a4`、`a5`、`legal` 或 `letter` 之一。也可手动指定尺寸为 `NNxNN`，宽乘高以毫米为单位。如果遇到未知值，使用 `letter`。

### UTF-8 输出

使用 `-T` `utf8` 强制以 UTF-8 多字节字符编码进行文本输出，忽略环境中的 locale(1) 设置。关于字体样式和 `-O` 参数，参见 “ASCII 输出”。

在缺乏 locale 或宽字符支持的操作系统上，以及内部字符表示不是 UCS-4 的操作系统上，`mandoc` 总是回退到 “ASCII 输出”。

### 语法树输出

使用 `-T` `tree` 显示语法树的人类可读表示。它对手册页源代码的调试很有用。确切格式可能更改，因此不要为其编写解析器。

第一段显示在 mdoc(7) 序言、man(7) `TH` 行或所用回退中找到的元数据。

在树转储中，每行输出显示一个语法树节点。子节点相对于其父节点缩进。各列为：

- 如果节点是开分隔符，则为开括号。
- 如果节点开始新输入行，则为星号。
- 输入行号（从 1 开始）。
- 冒号。
- 输入列号（从 1 开始）。
- 如果节点是闭分隔符，则为闭括号。
- 如果节点结束句子，则为句号。
- BROKEN 如果节点被另一个块打断。
- NOSRC 如果节点不在输入文件中，而是从宏自动生成。
- NOPRT 如果节点不应为任何输出格式生成输出。

- 对于宏节点，为宏名称；对于文本和 tbl(7) 节点，为内容。eqn(7) 节点有特殊格式。
- 节点类型（text、elem、block、head、body、body-end、tail、tbl、eqn）。
- 标志：

接受以下 `-O` 参数：

**`noval`** 跳过验证并显示未验证的语法树。这有助于查明给定行为是由解析器还是验证器引起的。在这种情况下，元数据不可用。

## 环境变量

**`LC_CTYPE`** 字符编码 locale(1)。当选择 “Locale 输出” 时，它决定使用 ASCII 还是 UTF-8 输出格式。它从不影响输入文件的解释。

**`MANPAGER`** 环境变量 `MANPAGER` 的任何非空值用于代替标准分页程序 [less(1)](less.1.md)；详见 [man(1)](man.1.md)。仅在指定 `-a` 或 `-l` 时使用。

**`PAGER`** 指定当 `MANPAGER` 未定义时使用的分页程序。如果 PAGER 和 MANPAGER 均未定义，则使用 [less(1)](less.1.md)。仅在指定 `-a` 或 `-l` 时使用。

## 退出状态

`mandoc` 实用程序以下列值之一退出，由与 `-W` 选项关联的消息 `level` 控制：

**0** 未发生基本系统约定违规、风格建议、警告或错误，或发生的因低于请求的 `level` 而被忽略。

**1** 至少发生一个基本系统约定违规或风格建议，但无警告或错误，且指定了 `-W` `base` 或 `-W` `style`。

**2** 至少发生一个警告，但无错误，且请求了 `-W` `warning` 或更低 `level`。

**3** 至少发生一个解析错误，但未遇到不支持的功能，且请求了 `-W` `error` 或更低 `level`。

**4** 至少遇到一个不支持的功能，且请求了 `-W` `unsupp` 或更低 `level`。

**5** 指定了无效的命令行参数。未读取任何输入文件。

**6** 发生操作系统错误，例如内存、文件描述符或进程表项耗尽。此类错误可能导致 `mandoc` 立即退出，可能在解析或格式化文件过程中。

注意，选择 `-T` `lint` 输出模式隐含 `-W` `all`。

## 实例

将手册分页到终端：

```sh
$ mandoc -a mandoc.1 man.1 apropos.1 makewhatis.8
```

使用 **`/usr/share/misc/mandoc.css`** 作为样式表生成 HTML 手册：

```sh
$ mandoc -T html -O style=/usr/share/misc/mandoc.css mdoc.7 > mdoc.7.html
```

检查大量手册：

```sh
$ mandoc -T lint `find /usr/src -name *.[1-9]`
```

为 A4 纸张生成一系列 PostScript 手册：

```sh
$ mandoc -T ps -O paper=a4 mdoc.7 man.7 > manuals.ps
```

将现代 mdoc(7) 手册转换为较旧的 man(7) 格式，用于缺乏 mdoc(7) 解析器的系统：

```sh
$ mandoc -T man foo.mdoc > foo.man
```

## 诊断

`mandoc` 显示的消息遵循以下格式：

> `mandoc`:
> `file`:`line`:`column` : level : message : macro argument ...
> (`os`)

前三个字段标识触发消息的输入文件的 `file` 名、`line` 号和 `column` 号。行号和列号从 1 开始。对于涉及整个输入文件的消息，两者均省略。所有 `level` 和 `message` 字符串的含义在下面解释。触发消息的 `macro` 名称及其参数在无意义时省略。`os` 操作系统说明符对于与所有操作系统相关的消息省略。关于无效命令行参数或操作系统错误的致命消息（例如内存耗尽时），也可能省略 `file` 和 `level` 字段。

消息级别含义如下：

**`syserr`** 发生操作系统错误。输入文件不一定有问题。输出可能仍然缺失或不完整。

**`badarg`** 指定了无效的命令行参数。未读取任何输入文件，不产生输出。

**`unsupp`** 输入文件使用了不支持的低级 roff(7) 功能。输出可能不完整和/或格式错误，因此使用 GNU troff 而非 `mandoc` 处理该文件可能更可取。

**`error`** 表示有信息丢失或严重格式错误的风险，多数情况下由严重语法错误引起。

**`warning`** 表示所显示信息或其格式可能在次要方面与作者意图不符的风险。此外，语法错误至少被归类为警告，即使它们通常不导致格式错误。

**`style`** 输入文件使用了可疑或不鼓励的风格。这不是对语法的抱怨，格式质量或可移植性可能都不受影响。虽然在较高级别的消息上非常注意避免误报，但 `style` 级别试图减少问题被忽视的概率，因此偶尔会发出虚假建议。请运用判断力决定某个特定 `style` 建议是否真的值得更改输入文件。

**`base`** 未遵守特定操作系统基本系统中使用的约定。这些不是标记错误，格式质量和可移植性都不受影响。`base` 级别的消息以更直观的 `style` `level` 标签打印。

`base`、`style`、`warning`、`error` 和 `unsupp` 级别的消息默认隐藏，除非通过 `-W` 选项或 `-T` `lint` 输出模式请求其级别或更低级别。

如下所示，所有 `base` 和部分 `style` 检查仅在 `-W` 命令行选项参数、`Os` 宏参数、`-Ios` 命令行选项参数中，或两者均不存在时在 uname(3) 函数返回值中出现特定操作系统名称时才执行。

### 基本系统手册的约定

**Mdocdate found** (mdoc，NetBSD) `Dd` 宏使用 CVS `Mdocdate` 关键字替换，NetBSD 基本系统不支持。考虑改用传统的 “Month dd, yyyy” 格式。

**Mdocdate missing** (mdoc，OpenBSD) `Dd` 宏未使用 CVS `Mdocdate` 关键字替换，但 OpenBSD 基本系统中按约定预期使用它。

**unknown architecture** (mdoc，OpenBSD，NetBSD) `Dt` 宏的第三个参数不匹配此操作系统运行的任何架构。

**operating system explicitly specified** (mdoc，OpenBSD，NetBSD) `Os` 宏有参数。在基本系统中，按约定留空。

**RCS id missing** (OpenBSD，NetBSD) 手册页缺少 CVS `OpenBSD` 或 `NetBSD` 关键字替换生成的 RCS 标识符注释行，这些操作系统按约定使用。

### 风格建议

**legacy man(7) date format** (mdoc) `Dd` 宏使用传统的 man(7) 日期格式 “yyyy-mm-dd”。考虑改用传统的 mdoc(7) 日期格式 “Month dd, yyyy”。

**normalizing date format to:** ... (mdoc，man) `Dd` 或 `TH` 宏提供了缩写月份名称或带前导零的日期号。在格式化输出中，月份名称写全，前导零省略。

**lower case character in document title** (mdoc，man) 标题仍按 `Dt` 或 `TH` 宏中给定的方式使用。

**duplicate RCS id** 单个手册页包含同一操作系统的两份 RCS 标识符。考虑删除后一个实例并将第一个移到页面顶部。

**possible typo in section name** (mdoc) 模糊字符串匹配发现 `Sh` 宏的参数与标准章节名称相似但不完全相同。

**unterminated quoted argument** (roff) 宏参数可用双引号字符括起，使得所括参数中的空格字符和宏名无需转义。宏最后一个参数的闭合引号可省略。但不建议省略，因为这使代码更难阅读。

**useless macro** (mdoc) 发现 `Bt`、`Tn` 或 `Ud` 宏。直接删除它：它没有有用目的。

**consider using OS macro** (mdoc) 在纯文本或 `Bx` 宏中发现可使用 `Ox`、`Nx`、`Fx` 或 `Dx` 表示的字符串。

**errnos out of order** (mdoc，NetBSD) `Bl` 列表中的 `Er` 项未按字母顺序排列。

**duplicate errno** (mdoc，NetBSD) `Bl` 列表包含描述同一 `Er` 号的两个连续 `It` 条目。

**referenced manual not found** (mdoc) `Xr` 宏引用了未找到的手册页。使用 `-W` `base` 运行时，搜索限制在基本系统，默认为 **`/usr/share/man`**:**`/usr/X11R6/man`**。此路径可在编译时使用 `MANPATH_BASE` 预处理宏配置。使用 `-W` `style` 运行时，搜索沿 [man(1)](man.1.md) 手册页中描述的完整搜索路径进行，尊重 `-m` 和 `-M` 命令行选项、`MANPATH` 环境变量、man.conf(5) 文件并回退到默认的 **`/usr/share/man`**:**`/usr/X11R6/man`**:**`/usr/local/man`**，也可在编译时使用 `MANPATH_DEFAULT` 预处理宏配置。

**trailing delimiter** (mdoc) `Ex`、`Fo`、`Nd`、`Nm`、`Os`、`Sh`、`Ss`、`St` 或 `Sx` 宏的最后一个参数以尾分隔符结尾。这通常是糟糕的风格，常表明拼写错误。很可能可以删除分隔符。

**no blank before trailing delimiter** (mdoc) 支持尾分隔符参数的宏的最后一个参数长于一个字节且以尾分隔符结尾。考虑插入一个空格使分隔符成为单独参数，从而将其移出宏的作用域。

**fill mode already enabled, skipping** (man) 即使文档仍处于填充模式或已切回填充模式，仍出现 `fi` 请求。它无效果。

**fill mode already disabled, skipping** (man) 即使文档已切换到非填充模式且尚未切回填充模式，仍出现 `nf` 请求。它无效果。

**input text line longer than 80 bytes** 考虑在第 80 列之前的某个空格字符处断开输入文本行。

**verbatim "--", maybe consider using \-** (mdoc) 即使 ASCII 输出设备将破折号渲染为 "--"，在输入文件中这样写也不好，因为它在所有其他输出设备上渲染效果差。

**function name without markup** (mdoc) 文本行上出现后跟空括号对的单词。考虑使用 `Fn` 或 `Xr` 宏。

**whitespace at end of input line** (mdoc，man，roff) 输入行末尾的空格几乎从无语义意义——但在偶发可能有的情况下，审阅和维护文档时极其令人困惑。

**bad comment style** (roff) 注释行以点、反斜杠和双引号字符开头。`mandoc` 实用程序即使没有反斜杠也将该行视为注释行，但省略反斜杠可能不可移植。

### 与文档序言相关的警告

**missing manual title, using UNTITLED** (mdoc，man) `Dt` 或 `TH` 宏无参数，其第一个参数为空字符串，或在第一个非序言 mdoc(7) 宏之前没有 `Dt` 宏。

**missing manual title, using ""** (man) 输入文档不包含任何 `TH` 宏。

**missing manual section, using ""** (mdoc，man) `Dt` 或 `TH` 宏缺少必需的 section 参数。

**unknown manual section** (mdoc) `Dt` 行中的章节号无效，但仍被使用。

**filename/section mismatch** (mdoc，man) 正在处理的输入文件名已知且其文件扩展名以非零数字开头，但 `Dt` 或 `TH` 宏包含以不同非零数字开头的 `section` 参数。`section` 参数仍按提供使用。考虑检查文件名或参数是否需要更正。

**missing date, using ""** (mdoc，man) 文档被解析为 mdoc(7) 且无 `Dd` 宏，或 `Dd` 宏无参数或仅有空参数；或文档被解析为 man(7) 且无 `TH` 宏，或 `TH` 宏少于三个参数或其第三个参数为空。

**cannot parse date, using it verbatim** (mdoc，man) `Dd` 或 `TH` 宏中给出的日期不遵循传统格式。

**date in the future, using it anyway** (mdoc，man) `Dd` 或 `TH` 宏中给出的日期比当前系统时间 time(3) 超前一天以上。

**missing Os macro, using ""** (mdoc) 在这种情况下不显示默认或当前系统。

**late prologue macro** (mdoc) `Dd` 或 `Os` 宏出现在某个非序言宏之后，但仍生效。

**prologue macros out of order** (mdoc) 序言宏未按传统顺序 `Dd`、`Dt`、`Os` 给出。即使以其他顺序给出，所有三个宏仍被使用。

### 关于文档结构的警告

**.so is fragile, better use ln(1)** (roff) 包含文件仅在解析程序以正确的当前工作目录运行时才有效。

**no document body** (mdoc，man) 文档正文既不含文本也不含宏。显示空文档，仅由页眉和页脚行组成。

**content before first section header** (mdoc，man) 某些宏或文本出现在第一个 `Sh` 或 `SH` 章节头之前。违规的宏和文本被解析并添加到语法树的顶层，不在任何章节块中。

**first section is not NAME** (mdoc) 第一个 `Sh` 宏的参数不是 ‘NAME’。这可能使 makewhatis(8) 和 [apropos(1)](apropos.1.md) 混淆。

**NAME section without Nm before Nd** (mdoc) NAME 章节在第一个 `Nd` 宏之前不包含任何 `Nm` 子宏。

**NAME section without description** (mdoc) NAME 章节缺少必需的 `Nd` 子宏。

**description not at the end of NAME** (mdoc) NAME 章节确实包含 `Nd` 子宏，但其后还有其他内容。

**bad NAME section content** (mdoc) NAME 章节包含 `Nm` 和 `Nd` 以外的纯文本或宏。

**missing comma before name** (mdoc) NAME 章节包含的 `Nm` 宏既不是第一个也不以逗号开头。

**missing description line, using ""** (mdoc) `Nd` 宏缺少必需的参数。手册的标题行将在破折号后结束。

**description line outside NAME section** (mdoc) `Nd` 宏出现在 NAME 章节之外。参数仍被打印，后续文本用于 [apropos(1)](apropos.1.md)，但该行为不可移植。

**sections out of conventional order** (mdoc) 标准章节出现在通常在其之后的另一个章节之后。所有章节标题按给定使用，章节顺序不更改。

**duplicate section title** (mdoc) 同一标准章节标题出现多次。

**unexpected section** (mdoc) 标准章节头出现在手册中通常无用的章节中。

**cross reference to self** (mdoc，man) `Xr` 或 `MR` 宏引用的名称和章节匹配当前手册页的章节，且匹配 NAME 或 SYNOPSIS 章节中 `Nm` 宏、或 SYNOPSIS 中 `Fn` 或 `Fo` 宏提及的名称。考虑使用 `Nm` 或 `Fn` 而非 `Xr`。

**unusual Xr order** (mdoc) 在 SEE ALSO 章节中，章节号较低的 `Xr` 宏跟在章节号较高的之后，或引用同一章节的两个 `Xr` 宏未按字母顺序排列。

**unusual Xr punctuation** (mdoc) 在 SEE ALSO 章节中，两个 `Xr` 宏之间的标点不同于单个逗号，或最后一个 `Xr` 宏后有尾标点。

**AUTHORS section without An macro** (mdoc) AUTHORS 章节不含 `An` 宏，或仅含空的。可能有缺少标记的作者姓名。

### 与宏和嵌套相关的警告

- 在章节和子章节的开头和结尾
- 在非紧凑列表和显示之前
- 在非列、非紧凑列表中条目的结尾
- 以及多个连续的段落宏处

- 对于空的 `P`、`PP` 和 `LP` 宏
- 对于既无 head 也无 body 参数的 `IP` 宏
- 对于紧跟在 `SH` 或 `SS` 之后的 `br` 或 `sp`

**obsolete macro** (mdoc) 替换见 mdoc(7) 手册。

**macro neither callable nor escaped** (mdoc) 不可调用的宏的名称出现在宏行上。它被原样打印。如果意图是调用它，将其移到自己的输入行；否则，通过前加 ‘`\&`’ 转义。

**skipping paragraph macro** 在 mdoc(7) 文档中，这发生在 man(7) 文档中，发生在

**moving paragraph macro out of list** (mdoc) `Bl` 列表中的列表项包含尾段落宏。段落宏被移到列表末尾之后。

**skipping no-space macro** (mdoc) 输入行以 `Ns` 宏开头，或 `Ns` 宏之后的下一个参数是孤立的闭分隔符。该宏被忽略。

**blocks badly nested** (mdoc) 如果两个块相交，一个应完全包含另一个。否则，渲染输出在任何输出格式中可能看起来奇怪，在基于 SGML 的输出格式中渲染可能完全错误，因为此类语言根本不支持嵌套不良的块。嵌套不良的块的典型例子是 `Ao Bo Ac Bc` 和 `Ao Bq Ac`。在这些例子中，`Ac` 分别打断了 `Bo` 和 `Bq`。

**nested displays are not portable** (mdoc) `Bd`、`D1` 或 `Dl` 显示嵌套在另一个 `Bd` 显示中。这在 `mandoc` 中可用，但在大多数其他实现中失败。

**moving content out of list** (mdoc) `Bl` 列表块在第一个 `It` 宏之前包含文本或宏。违规子项被移到列表开头之前。

**first macro on line** 在 `Bl` `-column` 列表内，`Ta` 宏作为一行的第一个宏出现，这不可移植。

**line scope broken** (man) 在解析前一个宏的下一行作用域时，发现另一个宏过早终止了前一个。前一个被中断的宏从解析树中删除。

### 与缺少参数相关的警告

- ‘`\{`’ 关键字用于打开多行作用域。
- 一个请求或宏或某些文本，导致单行作用域。
- 逻辑行的立即结束，无任何中间空格，导致下一行作用域。

**skipping empty request** (roff，eqn) 宏定义请求中缺少宏名，或 eqn(7) 控制语句或操作关键字缺少其必需的参数。

**conditional request controls empty scope** (roff) 条件请求仅在以下情况之一跟随在同一逻辑输入行上时才有用：此处，条件请求之后仅有尾随空格，且其逻辑输入行上无其他内容。注意，逻辑输入行是否使用 ‘`\`’ 行继续字符跨多物理输入行分割并不重要。这是尾随空格在语法上有意义的罕见情况之一。条件请求控制仅含空格的作用域，因此不太可能有显著效果，除非它可能控制后面的 `el` 子句。

**skipping empty macro** (mdoc) 指示的宏无参数，因此无效果。

**empty block** (mdoc，man) `Bd`、`Bk`、`Bl`、`D1`、`Dl` 或 `RS` 块的正文不含内容，将不产生输出。

**empty argument, using 0n** (mdoc) `Bd` 或 `Bl` `-offset` 或 `-width` 之后缺少必需的宽度。

**missing display type, using -ragged** (mdoc) `Bd` 宏未带必需的显示类型调用。

**list type is not the first argument** (mdoc) 在 `Bl` 宏中，至少有一个其他参数在类型参数之前。`mandoc` 实用程序可处理任何参数顺序，但某些其他 mdoc(7) 实现不能。

**missing -width in -tag list, using 8n** (mdoc) 每个带 `-tag` 参数的 `Bl` 宏也需要 `-width`。

**missing utility name, using ""** (mdoc) `Ex` `-std` 宏在 `Nm` 首次带参数调用之前无参数调用。

**missing function name, using ""** (mdoc) `Fo` 宏无参数调用。不打印函数名。

**empty head in list item** (mdoc) 在 `Bl` `-diag`、`-hang`、`-inset`、`-ohang` 或 `-tag` 列表中，`It` 宏缺少必需的参数。条目头留空。

**empty list item** (mdoc) 在 `Bl` `-bullet`、`-dash`、`-enum` 或 `-hyphen` 列表中，`It` 块为空。显示空的列表项。

**missing argument, using next line** (mdoc) `Bd` `-column` 列表中的 `It` 宏无参数。虽然 `mandoc` 使用下一行（如果有）的文本或宏作为单元格，其他格式化器可能错误格式化该列表。

**missing font type, using \fR** (mdoc) `Bf` 宏无参数。它切换到默认字体。

**unknown font type, using \fR** (mdoc) `Bf` 参数无效。改用默认字体。

**nothing follows prefix** (mdoc) `Pf` 宏无参数，或仅有一个参数且同一输入行上无宏跟随。这使其失去目的；特别是，不抑制后续下一输入行上文本或宏之前的空格。

**empty reference block** (mdoc) `Rs` 宏在下一输入行上立即被 `Re` 宏跟随。这样的空块不产生任何输出。

**missing section argument** (mdoc，man) `Xr` 或 `MR` 宏缺少其第二个章节号参数。第一个参数（即名称）被打印，但无章节号。在 `Xr` 的情况下，括号也省略。

**missing -std argument, adding it** (mdoc) `Ex` 或 `Rv` 宏缺少必需的 `-std` 参数。`mandoc` 实用程序即使未指定也假定 `-std`，但其他实现可能不会。

**missing option string, using ""** (man) `OP` 宏无参数调用。显示一对空的方括号。

**missing resource identifier, using ""** (man) `MT` 或 `UR` 宏无参数调用。显示一对空的尖括号。

**missing eqn box, using ""** (eqn) 找到变音符号或二元运算符，但其左侧无内容。插入空框。

### 与错误宏参数相关的警告

**duplicate argument** (mdoc) `Bd` 或 `Bl` 宏有多个 `-compact`、多个 `-offset` 或多个 `-width` 参数。除最后一个外的所有这些参数实例被忽略。

**skipping duplicate argument** (mdoc) `An` 宏有多个 `-split` 或 `-nosplit` 参数。除第一个外的所有这些参数被忽略。

**skipping duplicate display type** (mdoc) `Bd` 宏有多个类型参数；使用第一个。

**skipping duplicate list type** (mdoc) `Bl` 宏有多个类型参数；使用第一个。

**skipping -width argument** (mdoc) `Bl` `-column`、`-diag`、`-ohang`、`-inset` 或 `-item` 列表有 `-width` 参数。这无效果。

**wrong number of cells** 在 `Bl` `-column` 列表的一行中，制表符或 `Ta` 宏的数量少于列表头行所期望的数量，或超出期望数量一个以上。缺失的单元格保持为空，超出列数的所有单元格合并为一个单元格。

**unknown AT&T UNIX version** (mdoc) `At` 宏有无效参数。它被原样使用，前加 "AT&T UNIX"。

**comma in function argument** (mdoc) `Fa` 或 `Fn` 宏的参数包含逗号；可能应拆分为两个参数。

**parenthesis in function name** (mdoc) `Fc` 或 `Fn` 宏的第一个参数包含开或闭括号；这可能错误，括号是自动添加的。

**unknown library name** (mdoc，不在 OpenBSD 上) `Lb` 宏有未知的名称参数，将渲染为 "library" “`name`”。

**invalid content in Rs block** (mdoc) `Rs` 块包含纯文本或非 `%` 宏。虚假内容留在语法树中。格式可能差。

**invalid Boolean argument** (mdoc) `Sm` 宏有 `on` 或 `off` 以外的参数。无效参数被移出宏，使宏为空，导致它切换空格模式。

**argument contains two font escapes** (roff) `char` 请求的第二个参数包含多个字体转义序列。使用该字符后可能保持错误的字体活动。

**unknown font, skipping request** (man，tbl) roff(7) `ft` 请求或 tbl(7) `f` 布局修饰符有未知的 `font` 参数。

**ignoring distance argument** (roff) 除了边距字符外，`mc` 请求还有第二个假定表示距离的参数，但 `mc` 的 `mandoc` 实现总是忽略第二个参数。

**odd number of characters in request** (roff) `tr` 请求包含奇数个字符。最后一个字符映射到空格字符。

### 与纯文本相关的警告

**blank line in fill mode, using .sp** (mdoc，man) 空白输入行的含义仅在非填充模式中有良好定义：在填充模式中，文本输入行的换行不应有意义。然而，为了与 groff 兼容，填充模式中的空白行像 `sp` 请求一样格式化。要请求段落中断，使用 `Pp` 或 `PP` 而非空白行。

**tab in filled text** (mdoc，man) 制表符的含义仅在非填充模式中有良好定义：在填充模式中，空格在文本输入行上不应有意义。作为实现相关选择，文本行上的制表符在任何情况下都传递给格式化器。鉴于制表符之前的文本将被填充，很难预测制表符将前进到哪个制表位。

**new sentence, new line** (mdoc) 新句子在文本行中间开始。在新的输入行上开始它以帮助格式化器产生正确的间距。

**invalid escape sequence argument** (roff) 转义序列的参数格式无效。无效转义序列被忽略。

**undefined escape, printing literally** (roff) 在转义序列中，前导反斜杠之后的第一个字符无效。该字符被原样打印，等同于忽略反斜杠。

**undefined string, using ""** (roff) 如果字符串在使用前未定义，其值隐式设置为空字符串。然而，在使用前显式定义字符串使代码更易读。

### 与表格相关的警告

**tbl line starts with span** (tbl) 表格布局行的第一个单元格是水平跨度（‘`s`’）。为此单元格提供的数据被忽略，单元格中不打印任何内容。

**tbl column starts with span** (tbl) 表格布局规范的第一行请求垂直跨度（‘`^`’）。为此单元格提供的数据被忽略，单元格中不打印任何内容。

**skipping vertical bar in tbl layout** (tbl) 表格布局规范包含两个以上连续的竖线。打印双竖线，所有额外的竖线被丢弃。

### 与表格相关的错误

**non-alphabetic character in tbl options** (tbl) 表格选项行在期望选项名开头处包含非字母、非空格、非逗号的字符。该字符被忽略。

**skipping unknown tbl option** (tbl) 表格选项行包含不匹配任何已知选项名的字母串。该词被忽略。

**missing tbl option argument** (tbl) 需要参数的表格选项后未跟开括号，或开括号后立即跟闭括号。该选项被忽略。

**wrong tbl option argument size** (tbl) 表格选项参数包含无效数量的字符。选项和参数均被忽略。

**empty tbl layout** (tbl) 表格布局规范完全为空，指定零行零列。作为回退，使用单个左对齐列。

**invalid character in tbl layout** (tbl) 表格布局规范包含的字符既不能解释为布局键字符也不能解释为布局修饰符，或修饰符在第一个键之前。无效字符被丢弃。

**unmatched parenthesis in tbl layout** (tbl) 表格布局规范包含开括号但无匹配的闭括号。输入行从括号开始的其余部分无效果。

**ignoring invalid column width in tbl layout** (tbl) 表格布局中的列宽说明符为空、零或无效数字表达式。宽度说明符被忽略，列被设为足够宽以容纳其所有数据单元格。

**ignoring excessive spacing in tbl layout** (tbl) 表格布局中的间距修饰符过大。改用默认间距 3n。

**tbl without any data cells** (tbl) 表格不包含任何数据单元格。它可能不产生输出。

**ignoring data in spanned tbl cell** (tbl) 表格单元格在表格布局中被标记为水平跨度（‘`s`’）或垂直跨度（‘`^`’），但包含数据。数据被忽略。

**ignoring extra tbl data cells** (tbl) 数据行包含的单元格多于相应布局行。额外单元格中的数据被忽略。

**data block open at end of tbl** (tbl) 数据块以 `T{` 打开，但从未以匹配的 `T}` 闭合。表格的剩余数据行全部放入一个单元格，任何剩余单元格保持为空。

### 与 roff、mdoc 和 man 代码相关的错误

- 包括字符串和数字寄存器展开的嵌套转义序列展开
- 嵌套用户定义宏的展开
- 以及 `so` 文件包含

- 带多个参数的 `Fo`、`MT`、`PD`、`RS`、`UR`、`ft` 或 `sp`
- `-split` 或 `-nosplit` 之后带另一个参数的 `An`
- 带多个参数或非整数参数的 `RE`
- 带两个以上参数的 `OP` 或 `de` 系列请求
- 带三个以上参数的 `Dt` 或 `MR`
- 带五个以上参数的 `TH`
- 带无效参数的 `Bd`、`Bk` 或 `Bl`

**duplicate prologue macro** (mdoc) 某个序言宏出现多次。最后一个实例覆盖所有之前的。

**skipping late title macro** (mdoc) `Dt` 宏出现在第一个非序言宏之后。传统格式化器无法处理这种情况，因为它们在解析文档正文之前写入页眉。即使此技术限制不适用于 `mandoc`，仍保留传统语义。迟到的宏被丢弃，包括其参数。

**input stack limit exceeded, infinite loop?** (roff) 为以下功能实现了显式递归限制，以防止无限循环：当达到限制时，输出不正确，通常会丢失一些内容，但解析器可继续。

**skipping bad character** (mdoc，man，roff) 输入文件包含不可打印的 [ascii(7)](../man7/ascii.7.md) 字符的字节。消息提及字符编号。违规字节替换为问号（‘?’）。考虑编辑输入文件，将字节替换为预期字符的 ASCII 音译。

**skipping unknown macro** (mdoc，man，roff) 请求或宏行上的第一个标识符既不被识别为 roff(7) 请求，也不被识别为用户定义宏，也不分别被识别为 mdoc(7) 或 man(7) 宏。它可能拼写错误或不支持。请求或宏被丢弃，包括其参数。

**skipping request outside macro** (roff) `shift` 或 `return` 请求出现在任何宏定义之外，无效果。

**skipping insecure request** (roff) 输入文件尝试运行 shell 命令或读写外部文件。出于安全原因，此类尝试被拒绝。

**skipping item outside list** (mdoc，eqn) `It` 宏出现在任何 `Bl` 列表之外，或 eqn(7) `above` 分隔符出现在任何堆之外。它被丢弃，包括其参数。

**skipping column outside column list** (mdoc) `Ta` 宏出现在任何 `Bl` `-column` 块之外。它被丢弃，包括其参数。

**skipping end of block that is not open** (mdoc，man，eqn，tbl，roff) 各种语法元素只能用于显式关闭先前已打开的块。遇到 mdoc(7) 块关闭宏、man(7) `ME`、`RE` 或 `UE` 宏、eqn(7) 右分隔符或闭括号、或方程、表格或 roff(7) 条件请求的结尾，但没有匹配的打开块。违规请求或宏被丢弃。

**fewer RS blocks open, skipping** (man) `RE` 宏带参数调用，但打开的 `RS` 块数少于指定数量。`RE` 宏被丢弃。

**inserting missing end of block** (mdoc，tbl) 各种 mdoc(7) 宏以及表格需要通过专用宏显式关闭。不支持嵌套不良的块在其所有子项正确关闭之前结束。打开的子节点被隐式关闭。

**appending missing end of block** (mdoc，man，eqn，tbl，roff) 在文档末尾，仍有打开的显式 mdoc(7) 块、man(7) 下一行作用域或 `MT`、`RS` 或 `UR` 块、方程、表格或 roff(7) 条件或忽略块。打开的块被隐式关闭。

**escaped character not allowed in a name** (roff) 宏、字符串和寄存器标识符由可打印的非空格 ASCII 字符组成。转义序列和用其表示的字符和字符串不能构成名称的一部分。`am`、`as`、`de`、`ds`、`nr` 或 `rr` 请求的第一个参数，或 `rm` 请求的任何参数，或正在调用的请求或用户定义宏的名称，被转义序列终止。在 `as`、`ds` 和 `nr` 的情况下，请求完全无效果。在 `am`、`de`、`rr` 和 `rm` 的情况下，到此为止解析的内容用作请求的参数，输入行的其余部分被丢弃，包括转义序列。在解析要调用的请求或用户定义宏名称时，仅丢弃转义序列。其前面的字符用作请求或宏名，其后面的字符用作请求或宏的参数。

**using macro argument outside macro** (roff) 转义序列 `\$` 出现在任何宏定义之外，展开为空字符串。

**argument number is not numeric** (roff) 转义序列 `\$` 的参数不是数字；转义序列展开为空字符串。

**negative argument, using 0** (roff) `shift` 请求有负参数或因整数溢出而为负的参数。宏参数编号保持不变。

**NOT IMPLEMENTED: Bd -file** (mdoc) 出于安全原因，`Bd` 宏不支持 `-file` 参数。通过请求包含敏感文件，恶意文档可能诱骗特权用户无意中在屏幕上显示该文件，将文件内容暴露给旁观者。该参数被忽略，包括其后的文件名。

**skipping display without arguments** (mdoc) `Bd` 块宏无任何参数。该块被丢弃，块内容以块之前活动的任何模式显示。

**missing list type, using -item** (mdoc) `Bl` 宏未指定列表类型。

**argument is not numeric, using 1** (roff) `ce` 请求的参数不是数字。

**argument is not a character** (roff) `char` 请求的第一个参数既不是单个 ASCII 字符也不是单个字符转义序列。请求被忽略，包括其所有参数。

**skipping unusable escape sequence** (roff) `mc` 请求的第一个参数既不是单个 ASCII 字符也不是单个字符转义序列。所有参数被忽略，边距字符打印被禁用。

**missing manual name, using ""** (mdoc，man) 对 `Nm` 的第一次调用，或 NAME 章节中的任何调用，缺少必需的参数，或 `MR` 无任何参数调用。

**uname(3) system call failed, using UNKNOWN** (mdoc) `Os` 宏无参数调用，且 uname(3) 系统调用失败。作为变通方法，`mandoc` 可用 `-D` `OSNAME=""` `string` `""` 编译。

**unknown standard specifier** (mdoc) `St` 宏有未知参数，被丢弃。

**skipping request without numeric argument** (roff，eqn) `it` 请求或 eqn(7) `size` 或 `gsize` 语句有非数字或负参数或完全无参数。无效请求或语句被忽略。

**excessive shift** (roff) `shift` 请求的参数大于当前正在执行的宏的参数数量。所有宏参数被删除，`\n(.$` 设为零。

**NOT IMPLEMENTED: .so with absolute path or ".."** (roff) 出于安全原因，`mandoc` 仅允许带相对路径且不升级到任何父目录的 `so` 文件包含请求。通过请求包含敏感文件，恶意文档可能诱骗特权用户无意中在屏幕上显示该文件，将文件内容暴露给旁观者。`mandoc` 仅显示 `so` 后面出现的路径。

**.so request failed** (roff) 服务 `so` 请求需要读取外部文件，但文件无法打开。`mandoc` 仅显示 `so` 后面出现的路径。

**skipping all arguments** (mdoc，man，eqn，roff) mdoc(7) `Bt`、`Ed`、`Ef`、`Ek`、`El`、`Lp`、`Pp`、`Re`、`Rs` 或 `Ud` 宏，不支持条目头的列表中的 `It` 宏，man(7) `LP`、`P` 或 `PP` 宏，eqn(7) `EQ` 或 `EN` 宏，或 roff(7) `br`、`fi` 或 `nf` 请求或 ‘..’ 块关闭请求以至少一个参数调用。所有参数被忽略。

**skipping excess arguments** (mdoc，man，roff) 宏或请求以过多参数调用：多余参数被忽略。

### 与转义序列相关的错误

**incomplete escape sequence** (roff) 在解析转义序列的参数时遇到输入行尾。在这种情况下，`\*` 和 `\n` 展开为空字符串，`\B` 展开为数字 ‘0’，`\w` 展开为不完整参数的长度。所有其他不完整转义序列被忽略。

**invalid special character** (roff) 特殊字符转义序列无效，例如指向代理或超出 Unicode 范围的 Unicode 序列，表示控制字符或超出 `unsigned char` 范围的 `\[char...]` 转义序列，或单字节字符转义序列的无效变长形式，例如写 "\[\]" 或 "\[~]" 而非 "\[]" 或 "\~"。转义序列被忽略。

**unknown special character** (roff) 特殊字符转义序列中给出的名称不为 `mandoc` 所知。转义序列被忽略。

**invalid escape argument delimiter** (roff) 期望数字参数的转义序列尝试使用字符 "%&()*+-./0123456789:<=>" 之一作为参数分隔符。转义序列被忽略，包括无效的开分隔符，参数的其余部分可能作为输出文本出现。虽然各种字符可用作参数分隔符，但为可读性和健壮性推荐使用撇号引号字符（‘`'`’）。

### 不支持的功能

**input too large** (mdoc，man) 目前，`mandoc` 无法处理大于其任意大小限制 2^31 字节（2 GB）的输入文件。由于有用的手册总是小的，这在实践中不是问题。一旦检测到条件，解析立即中止。

**unsupported control character** (roff) 输入文件中发现其他 roff(7) 实现支持但 `mandoc` 不支持的 ASCII 控制字符。它被问号替换。

**unsupported escape sequence** (roff) 输入文件包含 GNU troff 或 Heirloom troff 支持但 `mandoc` 不支持的转义序列，这很可能导致信息丢失或相当大的格式错误。

**unsupported roff request** (roff) 输入文件包含 GNU troff 或 Heirloom troff 支持但 `mandoc` 不支持的 roff(7) 请求，这很可能导致信息丢失或相当大的格式错误。

**eqn delim option in tbl** (eqn，tbl) 表格的选项行定义方程分隔符。表中包含的任何方程源码将未格式化打印。

**unsupported table layout modifier** (tbl) 表格布局规范包含 ‘`m`’ 修饰符。该修饰符被丢弃。

**ignoring macro in table** (tbl，mdoc，man) 表格包含 mdoc(7) 或 man(7) 宏或未定义宏的调用。该宏被忽略，其参数被当作文本行处理。

**skipping tbl in -Tman mode** (mdoc，tbl) 输入文件包含 `TS` 宏。此消息仅在 `-T` `man` 输出模式中生成，该模式不支持 tbl(7) 输入。

**skipping eqn in -Tman mode** (mdoc，eqn) 输入文件包含 `EQ` 宏。此消息仅在 `-T` `man` 输出模式中生成，该模式不支持 eqn(7) 输入。

### 错误的命令行参数

**bad command line argument** `-IKMmOTW` 命令行选项之一后的参数无效，或作为命令行参数给出的 `file` 无法打开。

**duplicate command line argument** `-I` 命令行选项被指定两次。

**option has a superfluous value** `-O` 选项的参数有值但不接受值。

**missing option value** `-O` 选项的参数无参数但需要参数。

**bad option value** `-O` `indent` 或 `width` 选项的参数值无效。

**duplicate option value** 同一 `-O` 选项被指定多次。

**no such tag** 指定了 `-O` `tag` 选项，但在显示的任何手册页中未找到标签。

**-Tmarkdown unsupported for man(7) input** (man) 指定了 `-T` `markdown` 选项但输入文件使用 man(7) 语言。该输入文件不产生输出。

## 参见

[apropos(1)](apropos.1.md), [man(1)](man.1.md), eqn(7), man(7), mandoc_char(7), mdoc(7), roff(7), tbl(7)

## 历史

`mandoc` 实用程序首次出现于 OpenBSD 4.8。`-I` 选项出现于 OpenBSD 5.2，`-aCcfhKklMSsw` 出现于 OpenBSD 5.7。

## 作者

`mandoc` 实用程序由 Kristaps Dzonsons <kristaps@bsd.lv> 编写，由 Ingo Schwarze <schwarze@openbsd.org> 维护。
