  KENV(1)  

KENV(1)

FreeBSD General Commands Manual

KENV(1)

[名称](#__u540D___u79F0_)
=======================

`kenv` —

转储或修改内核环境

[概要](#__u6982___u8981_)
=======================

`kenv` \[`-hNq`\] `kenv` \[`-qv`\] variable\[=value\] `kenv` \[`-q`\] `-u` variable

[描述](#__u63CF___u8FF0_)
=======================

如果在没有参数的情况下调用 `kenv` 实用程序，它将转储内核环境。 如果指定了 `-h` 选项，它会将报告限制为内核探测提示。 如果指定了可选 variable 名， `kenv` 将只报告该值。 如果指定了 `-N` 选项， `kenv` 将只显示变量名而不显示它们的值。 如果指定了 `-u` 选项， `kenv` 将删除给定的环境变量。 如果环境变量后面跟着一个可选 value, `kenv` 会将环境变量设置为这个值。

如果设置了 `-q` 选项，则由于无法执行请求的操作而通常打印的警告将被禁止。

如果设置了 `-v` 选项，除了使用变量名执行 `kenv` 时的值之外，还将为环境变量打印变量名。

变量可以使用 /boot/loader.conf 文件添加到内核环境中，也可以使用语句静态编译到内核中

``` `env` filename```

在内核配置文件中。该文件可以包含以下形式的行

`name = value # this is a comment`

其中 ‘name’ 和 ‘=’ 周围的空格以及 ‘#’ 字符之后的所有内容都将被忽略。 除了 ‘=’ 之外，几乎所有可打印字符都可以作为名称的一部分。 仅当值包含空格时，引号是可选的并且是必需的。

[实例](#__u5B9E___u4F8B_)
=======================

显示 uart 设备的内核探测提示变量名称和过滤器

$ kenv -h -N | grep uart hint.uart.0.at hint.uart.0.flags hint.uart.0.irq hint.uart.0.port hint.uart.1.at hint.uart.1.irq hint.uart.1.port 

显示特定变量的值：

$ kenv hint.uart.1.at isa 

与上面相同，但在报告中添加变量的名称：

$ kenv -v hint.uart.1.at hint.uart.1.at="isa" 

尝试删除变量并抑制警告（如果有）：

$ kenv -q -u hint.uart.1.at 

设置 `verbose_loading` 变量的值

$ kenv verbose\_loading="YES" verbose\_loading="YES" 

[参见](#__u53C2___u89C1_)
=======================

kenv(2), config(5), loader.conf(5), loader(8)

[历史](#__u5386___u53F2_)
=======================

`kenv` 实用程序出现在 FreeBSD 4.1.1 中。

October 5, 2020

FreeBSD 13.1-RELEASE