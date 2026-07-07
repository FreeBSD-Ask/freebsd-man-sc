# kenv(1)

`kenv` — 列出或修改内核环境

## 名称

`kenv`

## 概要

`kenv [-l | -s] [-hNq]`

`kenv [-qv] variable[=value]`

`kenv [-q] -u variable`

## 描述

如果不带参数调用，`kenv` 实用程序将列出内核环境中的所有变量。

如果指定了 `-l` 选项，则改为列出由 [loader(8)](../man8/loader.8.md) 提供的静态环境。类似地，`-s` 选项将列出由内核配置定义的静态环境。`-l` 和 `-s` 选项都依赖于内核被配置为保留早期内核环境。默认内核配置不保留这些环境。

如果指定了 `-h` 选项，将把报告限制为内核探测提示。如果指定了可选的 `variable` 名称，`kenv` 将仅报告该值。如果指定了 `-N` 选项，`kenv` 将仅显示变量名而不显示其值。如果指定了 `-u` 选项，`kenv` 将删除给定的环境变量。如果环境变量后跟一个可选的 `value`，`kenv` 会将环境变量设置为该值。

如果设置了 `-q` 选项，将抑制因无法执行请求的操作而通常打印的警告信息。

如果设置了 `-v` 选项，当 `kenv` 带变量名执行时，除了值之外还会打印环境变量的变量名。

可以使用 **/boot/loader.conf** 文件将变量添加到内核环境，也可以使用内核配置文件中的以下语句静态编译到内核中：

```sh
env filename
```

该文件可以包含如下形式的行：

```sh
name = "value" # 这是一个注释
```

其中 `name` 和 `=` 周围的空白字符以及 `#` 字符之后的所有内容都会被忽略。除 `=` 外的几乎所有可打印字符都可作为名称的一部分。引号是可选的，仅当值包含空白字符时才需要。

## 实例

显示内核探测提示变量名并过滤 uart 设备：

```sh
$ kenv -h -N | grep uart
hint.uart.0.at
hint.uart.0.flags
hint.uart.0.irq
hint.uart.0.port
hint.uart.1.at
hint.uart.1.irq
hint.uart.1.port
```

显示特定变量的值：

```sh
$ kenv hint.uart.1.at
isa
```

与上面相同，但在报告中添加变量名：

```sh
$ kenv -v hint.uart.1.at
hint.uart.1.at="isa"
```

尝试删除变量并抑制任何警告：

```sh
$ kenv -q -u hint.uart.1.at
```

设置 `verbose_loading` 变量的值：

```sh
$ kenv verbose_loading="YES"
verbose_loading="YES"
```

## 参见

[kenv(2)](../sys/kenv.2.md), [config(5)](../man5/config.5.md), [loader.conf(5)](../man5/loader.conf.5.md), [loader(8)](../man8/loader.8.md)

## 历史

`kenv` 实用程序首次出现于 FreeBSD 4.1.1。

## 安全注意事项

请注意，除非 `security.bsd.unprivileged_kenv_read` sysctl 设置为 0，否则允许非特权用户读取内核环境。这包括列出内核环境以及从环境中获取特定 `variable`。
