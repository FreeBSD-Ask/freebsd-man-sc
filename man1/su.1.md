# su.1

`su` — 切换用户身份

## 名称

`su`

## 概要

`su [-] [-c class] [-flms] [login [args]]`

## 描述

`su` 实用程序通过 PAM 请求适当的用户凭证，并切换到该用户 ID（默认用户是超级用户）。然后执行一个 shell。

PAM 用于设置 `su` 将使用的策略。特别是，默认情况下只有“`wheel`”组中的用户才能切换到 UID 0（“`root`”）。可以通过修改 **/etc/pam.d/su** 中的“`pam_group`”部分来更改此组要求。有关如何修改此设置的详情，参见 pam_group(8)。

默认情况下，环境保持不变，但 `USER`、`HOME` 和 `SHELL` 除外。`HOME` 和 `SHELL` 设置为目标登录的默认值。`USER` 设置为目标登录名，除非目标登录的用户 ID 为 0，此时保持不变。调用的 shell 属于目标登录。这是 `su` 的传统行为。适用于原始用户登录类（参见 login.conf(5)）的资源限制和会话优先级通常也会保留，除非目标登录的用户 ID 为 0。

选项如下：

**`-c`** `class` 使用指定登录类的设置。登录类必须在 login.conf(5) 中定义。仅允许超级用户使用。

**`-f`** 如果调用的 shell 是 [csh(1)](csh.1.md)，此选项阻止它读取“`.cshrc`”文件。

**`-l`** 模拟完整登录。环境被丢弃，但 `HOME`、`SHELL`、`PATH`、`TERM` 和 `USER` 除外。`HOME` 和 `SHELL` 按上述方式修改。`USER` 设置为目标登录名。`PATH` 设置为“`/bin:/usr/bin`”。`TERM` 从当前环境导入。可根据目标登录的类别，从登录类能力数据库中设置或覆盖环境变量。调用的 shell 是目标登录的 shell，`su` 会切换到目标登录的家目录。资源限制和会话优先级修改为目标账户登录类的设置。

**`-`** （无字母）与 `-l` 相同。

**`-m`** 保持环境不变。调用的 shell 是你的登录 shell，且不更改目录。作为安全预防措施，如果目标用户的 shell 是非标准 shell（由 getusershell(3) 定义）且调用者的真实 uid 不为零，`su` 将失败。

**`-s`** 将 MAC 标签设置为用户的默认标签，作为用户凭证设置的一部分。如果调用进程的 MAC 标签不足以转换为用户的默认 MAC 标签，则设置 MAC 标签可能失败。如果无法设置标签，`su` 将失败。

`-l`（或 `-`）和 `-m` 选项互斥；最后指定的选项覆盖之前的所有选项。

如果在命令行上提供了可选的 `args`，它们将传递给目标登录的登录 shell。注意，目标登录名之前的所有命令行参数都由 `su` 自身处理，目标登录名之后的所有内容都传递给登录 shell。

默认情况下（除非启动文件重置了提示符），超级用户的提示符设置为“**#**”，以提醒其强大的能力。

## 环境变量

`su` 使用的环境变量：

**`HOME`** 真实用户 ID 的默认家目录，除非按上述方式修改。

**`PATH`** 真实用户 ID 的默认搜索路径，除非按上述方式修改。

**`TERM`** 提供终端类型，可为切换后的用户 ID 保留。

**`USER`** 在执行 `su` 后，用户 ID 始终是有效 ID（目标用户 ID），除非用户 ID 为 0（root）。

## 文件

**`/etc/pam.d/su`** `su` 的 PAM 配置。

## 实例

**`su -m operator -c poweroff`** 以用户 `operator` 启动 shell，并运行命令 `poweroff`。除非你的真实 UID 为 0，否则会询问 operator 的密码。注意，由于用户“operator”默认没有有效 shell，因此需要 `-m` 选项。在此示例中，`-c` 传递给用户“operator”的 shell，而不被解释为 `su` 的参数。

**`su -m operator -c 'shutdown -p now'`** 同上，但目标命令包含多个单词，因此用引号括起以配合传递给 shell 的 `-c` 选项使用。（大多数 shell 期望 `-c` 的参数是单个单词。）

**`su -m -c staff operator -c 'shutdown -p now'`** 同上，但目标命令以登录类“staff”的资源限制运行。注意：在此示例中，第一个 `-c` 选项应用于 `su`，而第二个是所调用 shell 的参数。

**`su -l foo`** 为用户 foo 模拟登录。

**`su - foo`** 同上。

**`su -`** 为 root 模拟登录。

## 参见

[csh(1)](csh.1.md), mdo(1), [sh(1)](sh.1.md), [group(5)](../man5/group.5.md), login.conf(5), [passwd(5)](../man5/passwd.5.md), [environ(7)](../man7/environ.7.md), pam_group(8)

## 历史

`su` 命令出现在 Version 1 AT&T UNIX 中。
