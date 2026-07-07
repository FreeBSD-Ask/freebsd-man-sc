# textdump(4)

`textdump` — textdump 内核转储设施

## 名称

`textdump`

## 概要

`options DDB options KDB`

`options TEXTDUMP_PREFERRED options TEXTDUMP_VERBOSE`

## 描述

`textdump` 设施允许以人类可读的形式而非内核内存转储和小型转储通常使用的机器可读形式将内核调试信息捕获到磁盘。这种表示虽然不那么完整（因为它不捕获完整内核状态），但可以比传统转储更紧凑、可移植和持久的形式提供调试信息。通过将 `textdump` 与其他 [ddb(4)](ddb.4.md) 设施（如脚本和输出捕获）结合，可以完全自动化的方式捕获详细的错误信息。

## 格式

`textdump` 数据以与常规内存转储相同的风格存储在转储分区中，如果引导时存在，将由 savecore(8) 自动提取。

`textdump` 文件以 tar(5) 格式存储，由一个或多个文本文件组成，每个文件存储特定类型的调试输出。可能存在以下部分：

**`ddb.txt`** 捕获的 [ddb(4)](ddb.4.md) 输出（如果使用了捕获设施）。可通过清除 `debug.ddb.textdump.do_ddb` sysctl 禁用。

**`config.txt`** 内核配置（如果已将 `options INCLUDE_CONFIG_FILE` 编译进内核）。可通过清除 `debug.ddb.textdump.do_config` sysctl 禁用。

**`msgbuf.txt`** 内核消息缓冲区，包括最近的控制台输出（如果使用了捕获设施）。可通过清除 `debug.ddb.textdump.do_msgbuf` sysctl 禁用。

**`panic.txt`** 内核 panic 字符串（如果内核在转储生成之前发生 panic）。可通过清除 `debug.ddb.textdump.do_panic` sysctl 禁用。

**`version.txt`** 内核版本字符串。可通过清除 `debug.ddb.textdump.do_version` sysctl 禁用。

可使用 [tar(1)](../man1/bsdtar.1.md) 提取内核 textdump。

## 配置

`textdump` 设施作为内核调试器的一部分通过 `options KDB` 和 `options DDB` 启用。默认情况下，panic 时生成的内核转储或通过显式转储请求生成的转储将是常规内存转储；但是，通过在 [ddb(4)](ddb.4.md) 中使用 `textdump set` 命令，或使用 [sysctl(8)](../man8/sysctl.8.md) 将 `debug.ddb.textdump.pending` sysctl 设为 1，可以请求下一次转储为 textdump。也可以通过运行命令 `textdump dump` 在 [ddb(4)](ddb.4.md) 中直接触发 textdump。

如果在 [ddb(4)](ddb.4.md) 命令行，可使用命令 `textdump set`、`textdump status` 和 `textdump unset` 设置、查询和清除 textdump 挂起标志。

与常规内核转储一样，必须使用 dumpon(8) 自动或手动配置转储分区。

额外的内核 [config(8)](../man8/config.8.md) 选项：

**`TEXTDUMP_PREFERRED`** 将 textdump 设为执行转储的默认方式。这意味着无需 [sysctl(8)](../man8/sysctl.8.md) 或使用 `textdump set` ddb(8) 命令。

**`TEXTDUMP_VERBOSE`** 让 textdump 设施更详细地描述它发出的每个文件以及对调试 textdump 设施本身有用的其他诊断信息。

## 实例

在以下示例中，脚本 `kdb.enter.panic` 将在内核调试器因 panic 进入时运行，启用输出捕获，转储若干有用的调试信息，然后调用 panic 以强制写出内核转储，随后重启：

```sh
script kdb.enter.panic=textdump set; capture on; show allpcpu; bt;
  ps; alltrace; show alllocks; textdump dump; reset
```

在以下示例中，脚本 `kdb.enter.witness` 将在内核调试器因 witness 违规进入时运行，为用户打印锁相关信息：

```sh
script kdb.enter.witness=show locks
```

这些脚本也可使用 ddb(8) 实用程序配置。

## 参见

[tar(1)](../man1/bsdtar.1.md), [ddb(4)](ddb.4.md), tar(5), ddb(8), dumpon(8), savecore(8), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`textdump` 设施首次出现于 FreeBSD 7.1。

## 作者

`textdump` 设施由 Robert N. M. Watson 创建。
