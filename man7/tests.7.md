# tests(7)

`tests` — FreeBSD 测试套件简介

## 名称

`tests` FreeBSD 测试套件

## 描述

FreeBSD 测试套件提供了一系列自动化测试，用于两个主要目的。一方面，测试套件帮助*开发者*在修改源代码树时检测缺陷和回归。另一方面，它允许*最终用户*（尤其是系统管理员）验证 FreeBSD 操作系统的新安装在其硬件平台上的行为是否正确，同时确保系统在日常运行和维护期间不会出现回归。

FreeBSD 测试套件可在 **/usr/tests** 层次结构中找到。

本手册页描述如何运行测试套件以及如何配置其某些可选功能。有关编写测试的信息，请参见 atf(7)。

### 安装测试套件

如果 **/usr/tests** 目录缺失，则需要启用测试套件的构建，重新构建系统并安装结果。可通过在 **/etc/src.conf** 文件中设置‘WITH_TESTS=yes’（详见 [src.conf(5)](../man5/src.conf.5.md)）并按 [build(7)](build.7.md) 中所述重新构建系统来完成。

### 何时运行测试？

在深入如何运行测试套件的细节之前，以下是一些你应该运行它的场景：

- 在全新安装 FreeBSD 之后，确保系统在你的硬件平台上正常工作。
- 在将 FreeBSD 升级到不同版本之后，确保新代码在你的硬件平台上运行良好，且升级未在你的配置中引入回归。
- 在修改源代码树之后，检测任何新的缺陷和/或回归。
- 定期运行（也许通过 cron(8) 作业），确保对系统的任何更改（如安装第三方软件包或手动修改配置文件）不会引入意外故障。

### 运行测试

默认情况下，Kyua 在当前目录中查找测试。要运行整个测试套件，可使用 `-k` 选项指定顶层 `Kyuafile`：

```sh
$ kyua test -k /usr/tests/Kyuafile
```

或在运行 Kyua 之前切换到测试套件根目录：

```sh
$ cd /usr/tests
$ kyua test
```

上述命令将递归遍历 **/usr/tests** 中的所有测试程序，执行它们，将结果和调试数据存储在 Kyua 的数据库中（默认位于 `~/.kyua/store/`），并打印结果摘要。此摘要包括所有运行的总测试数的简要计数以及其中失败的数量。

可通过在命令行上提供测试名称或其路径的一部分来限制要运行的测试。例如，以下命令将执行为 [cp(1)](../man1/cp.1.md) 和 [stat(1)](../man1/stat.1.md) 实用程序提供的所有测试：

```sh
$ cd /usr/tests
$ kyua test bin/cp usr.bin/stat
```

以下命令将只执行为 [stat(1)](../man1/stat.1.md) 提供的两个测试程序之一：

```sh
$ cd /usr/tests
$ kyua test usr.bin/stat/stat_test
```

以下命令将只执行单个测试用例：

```sh
$ cd /usr/tests
$ kyua test usr.bin/stat/stat_test:t_flag
```

最后，以下命令将以调试模式执行该测试用例：

```sh
$ cd /usr/tests
$ kyua debug -p usr.bin/stat/stat_test:t_flag
```

`-p` 选项告诉 Kyua 在清理之前暂停，以便你检查临时目录，更好地了解测试失败的原因。

请注意，某些测试可能需要 root 权限才能执行：

```sh
$ cd /usr/tests
$ kyua debug usr.bin/stat/stat_test:h_flag
usr.bin/stat/stat_test:h_flag  ->  skipped: Requires root privileges
# kyua debug usr.bin/stat/stat_test:h_flag
[...]
usr.bin/stat/stat_test:h_flag  ->  passed
```

反之，某些测试只有在以非特权用户身份运行时才能正确工作。这通常会在测试的元数据中注明，使 Kyua 在运行测试之前自动放弃权限。

### 获取测试执行报告

可使用 Kyua 的各种报告命令检索有关测试结果的附加信息。例如，以下命令将打印最近一次测试运行中已执行测试的纯文本报告，并显示哪些测试失败了：

```sh
$ kyua report --verbose
```

要显示任意测试运行的结果，可使用 `-r` 选项指定要读取的结果文件：

```sh
$ kyua report --verbose \
    -r ~/.kyua/store/results.usr_tests.20260417-173009-335060.db
```

请记住，如果测试以 root 身份运行，结果将存储在 root 的 `kyua` 目录中，访问它们的最简单方法是以 root 身份运行 `report` 命令：

```sh
$ cd /usr/tests
# kyua test usr.bin/stat
# kyua report --verbose
```

此示例将生成可发布到 Web 服务器的 HTML 报告：

```sh
$ kyua report-html --output ~/public_html/tests
```

有关 Kyua 命令行界面的更多详细信息，请参阅其手册页 kyua(1)。

### 配置测试

FreeBSD 测试套件中的某些测试用例需要管理员手动配置后才能运行。除非定义了某些属性，否则需要这些属性的测试将被跳过。

通过在 **/etc/kyua/kyua.conf** 或命令行中定义配置变量来配置测试套件。配置文件的格式详见 kyua.conf(5)。

FreeBSD 测试套件中提供以下配置变量；所有变量名都以 `test_suites.FreeBSD.` 为前缀。

**`allow_sysctl_side_effects`** 启用会更改具有全局影响的 [sysctl(8)](../man8/sysctl.8.md) 变量的测试。测试将在其清理阶段撤销任何更改。

**`allow_network_access`** 启用需要访问测试主机所连接网络的测试。此类测试可能需要正确配置的 Internet 访问。

**`disks`** 必须设置为以空格分隔的磁盘设备节点列表。需要对磁盘进行破坏性访问的测试必须使用这些设备。测试不需要保留这些磁盘上的任何数据。

**`fibs`** 必须设置为以空格分隔的 FIB（路由表）列表。需要修改路由表的测试可使用其中任何一个。测试将清理其创建的任何新路由。

### 如果出现故障怎么办？

如果在执行测试套件期间出现*任何故障*，请考虑将其报告给 FreeBSD 开发者，以便分析和修复故障。为此，可向相应的邮件列表发送消息或提交问题报告。有关更多详细信息，请参阅：

- Lk https://lists.freebsd.org/ FreeBSD 邮件列表
- Lk https://www.freebsd.org/support/ 问题报告

## 文件

**`/etc/kyua/kyua.conf`** kyua(1) 的系统级配置文件。
**`~/.kyua/kyua.conf`** kyua(1) 的用户特定配置文件；覆盖系统文件。
**`~/.kyua/logs/`** Kyua 调试日志的默认位置（每次测试运行一个 `.log` 文件）。
**`~/.kyua/store/`** Kyua 测试结果的默认位置（每次测试运行一个 `.db` 文件）。
**`/usr/tests/`** FreeBSD 测试套件的位置。
**`/usr/tests/Kyuafile`** 顶层测试套件定义文件。

## 参见

kyua(1), atf(7), [build(7)](build.7.md), [development(7)](development.7.md)

## 历史

FreeBSD 测试套件首次出现于 FreeBSD 10.1，并在 FreeBSD 11.0 中默认安装。

`tests` 手册页首次出现于 NetBSD 6.0，后来移植到 FreeBSD 10.1。

测试驱动程序 kyua(1) 在 FreeBSD 13.0 中作为基本系统的一部分导入，之前仅在 [ports(7)](ports.7.md) 中可用。

## 作者

Julio Merino <jmmv@FreeBSD.org>
