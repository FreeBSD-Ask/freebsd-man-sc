# pw(8)

`pw` — 创建、删除、修改和显示系统用户与组

## 名称

`pw`

## 概要

`pw [-M metalog] [-R rootdir] [-V etcdir] useradd [-n name] [-mNoPq] [-C config] [-c comment] [-d homedir] [-e accexpdate] [-G grouplist] [-g group] [-H fd] [-h fd] [-k skeldir] [-L class] [-M mode] [-p passexpdate] [-s shell] [-u uid] [-w passmethod] [-Y [-y nispasswd]]`
`pw [-R rootdir] [-V etcdir] useradd -D [-q] [-b basehome] [-C config] [-e accexpdays] [-G grouplist] [-g group] [-i mingid,maxgid] [-k skeldir] [-M mode] [-p passexpdays] [-s shell] [-u minuid,maxuid] [-w passmethod] [-Y [-y nispasswd]]`
`pw [-R rootdir] [-V etcdir] userdel [-n name|[-u uid]] [-r] [-Y [-y nispasswd]]`
`pw [-R rootdir] [-V etcdir] usermod [-n name|uid [-u newuid]|[-u uid]] [-mNPq] [-C config] [-c comment] [-d homedir] [-e accexpdate] [-k skeldir] [-G grouplist] [-g group] [-H fd] [-h fd] [-L class] [-l newname] [-M mode] [-p passexpdate] [-s shell] [-w passmethod] [-Y [-y nispasswd]]`
`pw [-R rootdir] [-V etcdir] usershow [-n name|[-u uid]] [-7aFP]`
`pw [-R rootdir] [-V etcdir] usernext [-q] [-C config]`
`pw [-R rootdir] [-V etcdir] groupadd [-n name] [-oNPqY] [-C config] [-g gid] [-H fd] [-h fd] [-M members]`
`pw [-R rootdir] [-V etcdir] groupdel [-n name|[-g gid]] [-Y]`
`pw [-R rootdir] [-V etcdir] groupmod [-n name|gid [-g newgid]|[-g gid]] [-NPqY] [-C config] [-d oldmembers] [-H fd] [-h fd] [-l newname] [-M members] [-m newmembers]`
`pw [-R rootdir] [-V etcdir] groupshow [-n name|[-g gid]] [-aFP]`
`pw [-R rootdir] [-V etcdir] groupnext [-C config] [-q]`
`pw [-R rootdir] [-V etcdir] lock [-n name|[-u uid]] [-q] [-C config]`
`pw [-R rootdir] [-V etcdir] unlock [-n name|[-u uid]] [-q] [-C config]`

## 描述

`pw` 工具是一个基于命令行的系统 `user` 和 `group` 文件编辑器，为超级用户提供了一种易于使用且标准化的方式来添加、修改和删除用户与组。注意，`pw` 仅操作本地的用户和组文件。NIS 用户和组必须在 NIS 服务器上维护。`pw` 工具负责更新 [passwd(5)](../man5/passwd.5.md)、master.passwd(5)、[group(5)](../man5/group.5.md) 以及安全和非安全密码数据库文件，并且必须以 root 身份运行（使用 `-R` 或 `-V` 时除外）。

在命令行上提供给 `pw` 的前一个或两个关键字为其余参数提供上下文。关键字 `user` 和 `group` 可以与 `add`、`del`、`mod`、`show` 或 `next` 以任意顺序组合。（例如，`showuser`、`usershow`、`show user` 和 `user show` 都表示同一含义。）这种灵活性对于调用 `pw` 进行用户和组数据库操作的交互式脚本很有用。在这些关键字之后，可以选择性地指定用户或组名称或数字 id，作为使用 `-n` `name`、`-u` `uid`、`-g` `gid` 选项的替代方式。

以下标志对大多数或所有操作模式通用：

**`-R`** `rootdir` 指定一个替代的根目录，`pw` 将在该目录内操作。任何指定的路径都将相对于 `rootdir`。

**`-V`** `etcdir` 为密码、组和配置文件设置替代位置。可用于在替代位置维护用户/组数据库。如果指定此开关，将不再从系统 **/etc/pw.conf** 读取默认配置数据，而是使用指定目录中的 `pw.conf` 文件（如果不存在则不使用）。`-C` 标志可用于覆盖此行为。作为选项必须跟在操作类型之后这一通用规则的例外，`-V` 标志必须在命令行上操作关键字之前使用。

**`-C`** `config` 默认情况下，`pw` 读取文件 **/etc/pw.conf** 以获取有关如何创建新用户帐户和组的策略信息。`-C` 选项指定不同的配置文件。虽然配置文件的大部分内容可以通过命令行选项覆盖，但将标准信息保存在配置文件中可能更方便。

**`-q`** 使用此选项会使 `pw` 抑制错误消息，这在交互式环境中可能很有用，因为在这种环境中，解释 `pw` 返回的状态码比弄乱精心格式化的显示更可取。

**`-N`** 此选项在 `add` 和 `modify` 操作中可用，告诉 `pw` 输出操作结果而不更新用户或组数据库。可以使用 `-P` 选项在标准 passwd 和可读格式之间切换。

**`-Y`** 在任何更新模式下使用此选项会使 `pw` 在切换到 **/var/yp** 目录后运行 [make(1)](../man1/make.1.md)。这旨在允许自动更新 NIS 数据库文件。如果 NIS 使用了独立的 passwd 和 group 文件，则使用 `-y` `nispasswd` 选项指定 NIS passwd 数据库的位置，以便 `pw` 与系统密码数据库同时更新它。

## 用户选项

以下选项适用于 `useradd` 和 `usermod` 命令：

**`-n`** `name` 除非给出了 `-u` `uid`，否则必需。指定用户/帐户名称。在 `usermod` 的情况下可以是 `uid`。

**`-u`** `uid` 如果未给出 `name` 则必需。指定用户/帐户的数字 id。在 `usermod` 的情况下，如果与 `name` 配对，则更改指定用户/帐户的数字 id。通常只需要其中一个选项，因为帐户名会隐含 uid，反之亦然。但是，有时需要同时使用两者。例如，使用 `usermod` 更改现有用户的 uid 时，或使用 `useradd` 创建新帐户时覆盖默认 uid。要使用 `useradd` 为新用户自动分配 uid，则*不要*使用 `-u` 选项。帐户或 userid 也可以在命令行上紧随 `useradd`、`userdel`、`usermod` 或 `usershow` 关键字之后提供，而无需使用 `-n` 或 `-u` 选项。

**`-c`** `comment` 此字段设置 passwd GECOS 字段的内容，通常包含最多四个以逗号分隔的字段，分别包含用户的全名、办公室或位置，以及工作电话和家庭电话号码。但是，这些子字段仅按约定使用，并且是可选的。如果此字段要包含空格，注释必须用双引号 `"` 括起。避免在此字段中使用逗号，因为它们用作子字段分隔符；冒号 `:` 字符也不能使用，因为它是 passwd 文件本身的字段分隔符。

**`-d`** `homedir` 此选项设置帐户的主目录。通常，仅当主目录要与从 **/etc/pw.conf** 确定的默认值（通常是 **/home** 加帐户名作为子目录）不同时才使用。

**`-e`** `accexpdate` 设置帐户的过期日期。日期格式可以是十进制的 UNIX 时间，也可以是 `dd-mmm-yy[yy]` 格式的日期，其中 dd 是日，mmm 是月（数字或字母格式，如 'Jan'、'Feb' 等），年份是两位或四位。此选项还接受相对日期，格式为 `+n[mhdwoy]`，其中 `n` 是十进制、八进制（前导 0）或十六进制（前导 0x）数字，后跟从当前日期起的分钟、小时、天、周、月或年数，即设置过期日期的时间。

**`-p`** `passexpdate` 设置帐户的密码过期日期。此字段类似于帐户过期日期选项，但它适用于强制密码更改。设置方式与 `-e` 选项相同。

**`-g`** `group` 将帐户的主组设置为给定组。`group` 可以由其名称或组号定义。

**`-G`** `grouplist` 设置帐户的附属组成员资格。`grouplist` 是以逗号、空格或制表符分隔的组名或组号列表。用户被添加到 `grouplist` 中指定的组，并从所有未指定的组中移除。当前登录会话不受组成员资格更改的影响，仅在用户重新连接时生效。注意：不要使用 `grouplist` 将用户添加到其主组。

**`-L`** `class` 此选项为正在创建的用户设置登录类。有关用户登录类的更多信息，请参见 login.conf(5) 和 [passwd(5)](../man5/passwd.5.md)。

**`-m`** 此选项指示 `pw` 尝试创建用户的主目录。虽然主要用于使用 `useradd` 添加新帐户，但在将现有用户的主目录移动到文件系统上的其他位置时也可能有用。新主目录会填充 `skeleton` 目录的内容，该目录通常包含一组 shell 配置文件，用户可以根据自己的喜好进行个性化设置。此目录中的文件通常命名为 `dot`.<`config`>，其中 `dot` 前缀会被剥离。在 `usermod` 的帐户上使用 `-m` 时，用户主目录中的现有配置文件*不会*被 skeleton 文件覆盖。创建用户主目录时，默认情况下它将是 `-b` 选项指定的 `basehome` 目录的子目录，以新帐户名命名。如果需要，可以通过命令行上的 `-d` 选项覆盖。

**`-M`** `metalog` 指定 mtree(5) metalog 文件的路径。`pw` 将为添加到用户主目录的所有文件添加条目。这在以非 root 用户身份构建映像时很有用，因为 metalog 可用作 [tar(1)](../man1/bsdtar.1.md) 或 makefs(8) 的输入。注意，此选项必须在命令行上的 `useradd` 字符串之前，否则它将被解释为 mode 选项。

**`-M`** `mode` 以指定的 `mode` 创建用户主目录，该 mode 受当前 umask(2) 修改。如果省略，则从父进程的 umask(2) 派生。此选项仅在与 `-m` 标志组合时有用。

**`-k`** `skeldir` 设置 `skeleton` 目录，创建用户主目录时从中复制基本启动和配置文件。此选项仅在与 `-d` 或 `-m` 标志一起使用时有意义。

**`-s`** `shell` 将用户的登录 shell 设置或更改为 `shell`。如果省略 shell 程序的路径，`pw` 会搜索 **/etc/pw.conf** 中指定的 `shellpath` 并适当填充。注意，除非有特定理由，否则应避免指定路径——这允许 `pw` 验证程序存在且可执行。指定完整路径（或提供空白 "" shell）可跳过此检查，并允许设置如 **/nonexistent** 之类的条目，这些条目应为不用于交互式登录的帐户设置。

**`-h`** `fd` 此选项提供了一个特殊接口，交互式脚本可通过它使用 `pw` 设置帐户密码。由于命令行和环境是程序接受信息的基本不安全机制，`pw` 仅允许通过文件描述符（通常是交互式脚本与程序之间的管道）设置帐户和组密码。`sh`、`bash`、`ksh` 和 `perl` 都具有实现此操作的机制。或者，如果给定 `-h` `0`，`pw` 将提示输入用户密码，指定 *stdin* 作为读取密码的文件描述符。注意，此密码仅读取一次，旨在供脚本使用而非交互式使用。如果希望像 [passwd(1)](../man1/passwd.1.md) 那样进行新密码确认，则必须将其作为调用 `pw` 的交互式脚本的一部分实现。如果给定 `-` 作为参数 `fd`，则密码将设置为 `*`，使帐户无法通过基于密码的登录访问。

**`-H`** `fd` 从指定的文件描述符读取已加密的密码字符串。这与 `-h` 类似，但密码应以已加密的形式提供，适合直接写入密码数据库。有关生成加密密码哈希的更多详细信息，请参见 openssl-passwd(1) 和 crypt(3)。

可以使用 `useradd` 创建重复现有用户 id 的新帐户。虽然这通常被视为错误并被拒绝，但 `-o` 选项会覆盖唯一性检查并允许复制 uid。如果你允许同一用户在不同上下文下登录（不同的组分配、不同的主目录、不同的 shell），同时为每个帐户中对用户文件的访问提供基本相同的权限，这可能很有用。

`useradd` 命令还具有使用 `-D` 选项设置新用户和组默认值的能力。`pw` 不添加新用户，而是将一组新的默认值写入其配置文件 **/etc/pw.conf**。使用 `-D` 选项时，不得使用 `-n` `name` 或 `-u` `uid`，否则会出错。使用 `-D` 会更改 `useradd` 命令中几个命令行开关的含义。这些是：

**`-D`** 在 **/etc/pw.conf** 配置文件中设置默认值，如果使用 `-C` `config` 选项则设置到不同的命名配置文件。

**`-b`** `basehome` 设置创建用户主目录的根目录。默认值为 **/home**，但可以根据需要设置到其他位置。

**`-e`** `accexpdays` 设置默认的帐户过期天数。使用 `-D` 时，`accexpdays` 参数的解释方式不同。它必须是数字，表示创建后帐户过期的天数。值为 0 时禁止自动计算过期日期。

**`-p`** `passexpdays` 设置默认的密码过期天数。使用 `-D` 时，`passexpdays` 参数的解释方式不同。它必须是数字，表示创建后帐户过期的天数。值为 0 时禁止自动计算过期日期。

**`-g`** `group` 为新用户设置默认组。如果使用 `-g` `""` 指定空组，则新用户将被分配自己的私有主组，名称与其登录名相同。如果提供组，则可以将其名称或 uid 作为参数给出。

**`-G`** `grouplist` 设置授予新用户成员资格的默认组。这是与主组分开的一组组。避免将同一组同时指定为主组和附加组。换句话说，这些附加组确定的是*主组以外*的组成员资格。`grouplist` 是以逗号分隔的组名或 id 列表，始终以其符号名存储在 **/etc/pw.conf** 中。

**`-L`** `class` 此选项为新用户设置默认登录类。

**`-k`** `skeldir` 设置默认的 *skeleton* 目录，当 `pw` 创建用户主目录时，从中复制原型 shell 和其他初始化文件。有关这些文件的命名约定，请参见 `-k` 的描述。

**`-u`** `minuid,maxuid`, **`-i`** `mingid,maxgid` 设置为 `pw` 创建的新帐户和组分配的最小和最大用户及组 id。每个的默认值是最小 1000、最大 32000。`minuid` 和 `maxuid` 都是数字，其中 max 必须大于 min，且两者都必须在 0 到 32767 之间（`mingid` 和 `maxgid` 同理）。通常，小于 100 的用户和组 id 保留供系统使用，大于 32000 的数字也可能保留用于特殊目的（由某些系统守护进程使用）。此外，100 到 999 之间的 uid 和 gid 通常由与第三方程序关联的伪用户使用，通常应避免分配给普通用户。

**`-w`** `passmethod` `-w` 选项选择用于为新创建用户帐户设置密码的默认方法。`passmethod` 是以下之一：

**`no`** 禁用新创建帐户的登录
**`yes`** 强制密码为帐户名
**`none`** 强制使用空白密码
**`random`** 生成随机密码

`random` 或 `no` 方法最安全；在前者情况下，`pw` 生成密码并打印到 stdout，这适用于向用户发放密码而非允许用户选择自己的（可能选择不当的）密码。`no` 方法要求超级用户使用 [passwd(1)](../man1/passwd.1.md) 使帐户可通过密码访问。

**`-y`** `path` 如果你不直接与 NIS 共享 **/etc/master.passwd** 中的信息，则设置 NIS 使用的数据库路径名。仅应为 NIS 服务器设置此选项。

`userdel` 命令有三个不同的选项。`-n` `name` 和 `-u` `uid` 选项已在上面介绍。附加选项是：

**`-r`** 这告诉 `pw` 删除用户的主目录及其所有内容。`pw` 工具在从系统中删除文件时倾向于谨慎。首先，如果要删除的帐户的 uid 也被系统上另一个帐户使用，且密码文件中的“home”目录是以字符 `/` 开头的有效路径，则不会执行删除。其次，它仅删除实际上由用户拥有的文件和目录，或用户主目录下由任何人拥有的符号链接。最后，删除由用户拥有的所有内容后，仅删除空目录。如果主目录是 ZFS 数据集且已清空，则该数据集将被销毁。不处理主目录内的 ZFS 数据集和快照。如果需要任何额外的清理工作，则留给管理员。

删除帐户时，总是会删除邮件 spool 文件和 crontab(5) 文件，因为它们无条件地附加到用户名。如果用户的 uid 是唯一的且未被系统上另一个帐户使用，则由 [at(1)](../man1/at.1.md) 排队处理的作业也会被删除。

`usermod` 命令增加了一个附加选项：

**`-l`** `newname` 此选项允许将现有帐户名更改为 `newname`。新名称必须不存在，任何复制现有帐户名的尝试都将被拒绝。

`usershow` 命令允许以两种格式之一查看帐户。默认情况下，格式与 **/etc/master.passwd** 中使用的格式相同，但密码字段替换为 `*`。如果使用 `-P` 选项，则 `pw` 以更易读的形式输出帐户详细信息。如果使用 `-7` 选项，则以 v7 格式显示帐户详细信息。`-a` 选项列出当前文件中的所有用户。使用 `-F` 强制 `pw` 打印帐户的详细信息，即使该帐户不存在。

`usernext` 命令返回下一个可用的用户和组 id，以冒号分隔。这通常仅对使用 `pw` 的交互式脚本或前端有意义。

## 组选项

`-C` 和 `-q` 选项（在上一节开头已说明）可用于组操作命令。所有与组相关的命令的其他通用选项是：

**`-n`** `name` 除非给出了 `-g` `gid`，否则必需。指定组名。在 `groupmod` 的情况下可以是 gid。

**`-g`** `gid` 如果未给出 `name` 则必需。指定组的数字 id。在 `groupmod` 的情况下，如果与 `name` 配对，则更改指定组的数字 id。与帐户名和 id 字段一样，通常只需提供其中一个，因为组名隐含 uid，反之亦然。仅当为新组设置特定组 id 或更改现有组的 uid 时，才需要同时使用两者。

**`-M`** `memberlist` 此选项提供了一种替代方式，将现有用户添加到新组（在 `groupadd` 中）或替换现有成员列表（在 `groupmod` 中）。`memberlist` 是以逗号、空格或制表符分隔的有效且现有的用户名或 uid 列表。

**`-m`** `newmembers` 类似于 `-M`，此选项允许将现有用户*添加*到组中，而不替换现有成员列表。可以使用登录名或用户 id，重复的用户将被静默消除。

**`-d`** `oldmembers` 类似于 `-M`，此选项允许从组中*删除*现有用户，而不替换现有成员列表。可以使用登录名或用户 id，重复的用户将被静默消除。

`groupadd` 还有一个 `-o` 选项，允许将现有组 id 分配给新组。默认操作是拒绝添加组的尝试，此选项覆盖对重复组 id 的检查。很少需要复制 gid。

`groupmod` 命令增加了一个附加选项：

**`-l`** `newname` 此选项允许将现有组名更改为 `newname`。新名称必须不存在，任何复制现有组名的尝试都将被拒绝。

`groupshow` 的选项与 `usershow` 相同，用 `-g` `gid` 替换 `-u` `uid` 来指定组 id。`-7` 选项不适用于 `groupshow` 命令。

`groupnext` 命令在标准输出上返回下一个可用的组 id。

## 用户锁定

`pw` 工具支持简单的用户密码锁定机制；它通过在 master.passwd(5) 的密码字段开头前置字符串 `*LOCKED*` 来防止成功认证。

`lock` 和 `unlock` 命令分别接受要锁定或解锁的帐户的用户名或 uid。这些命令接受上述的 `-V`、`-C` 和 `-q` 选项。

## 注释

要获取每个命令可用选项的摘要，可以使用

```sh
pw [command] help
```

例如，

```sh
pw useradd help
```

列出 `useradd` 操作的所有可用选项。

`pw` 工具允许在 passwd GECOS 字段（用户全名、办公室、工作和家庭电话号码子字段）中使用 8 位字符，但不允许在用户登录名和组名中使用。谨慎使用 8 位字符，因为连接到 Internet 将要求你的邮件传输程序支持 8BITMIME，并将包含 8 位字符的标头转换为 7 位 quoted-printable 格式。sendmail(8) 确实支持此功能。在 GECOS 字段中使用 8 位字符应与用户的默认 locale 和字符集结合使用，并且不应在没有它们的情况下使用。使用 8 位字符还可能影响通过 Internet 传输 GECOS 字段内容的其他程序，如 fingerd(8)，以及少量 TCP/IP 客户端（如 IRC），其中默认可能使用 passwd 文件中指定的全名。

当发生用户或组的添加或删除等操作时，`pw` 工具会向 **/var/log/userlog** 文件写入日志。此日志文件的位置可以在 pw.conf(5) 中更改。

## 文件

**/etc/master.passwd** 用户数据库
**/etc/passwd** Version 7 格式密码文件
**/etc/login.conf** 用户能力数据库
**/etc/group** 组数据库
**/etc/pw.conf** pw 默认选项文件
**/var/log/userlog** 用户/组修改日志文件

## 实例

添加新用户 Glurmo Smith（gsmith）。如果尚未存在，则创建 gsmith 登录组。登录 shell 设置为 [csh(1)](../man1/csh.1.md)。如果不存在，则创建位于 **/home/gsmith** 的新主目录。最后，生成并显示随机密码：

```sh
pw useradd -n gsmith -c "Glurmo Smith" -s csh -m -w random
```

删除 gsmith 用户及其主目录（包括内容）。

```sh
pw userdel -n gsmith -r
```

将现有用户 jsmith 添加到 wheel 组，同时保留 jsmith 已是成员的其他组。

```sh
pw groupmod wheel -m jsmith
```

生成随机密码，并以纯文本和加密形式显示，不修改任何数据库。

```sh
pw usermod nobody -Nw random
```

## 退出状态

`pw` 工具在操作成功时返回 EXIT_SUCCESS，否则 `pw` 返回 [sysexits(3)](../man3/sysexits.3.md) 定义的以下退出码之一：

**EX_USAGE**
- 命令行语法错误（无效关键字、未知选项）。

**EX_NOPERM**
- 试图以非 root 身份运行其中一种更新模式。

**EX_OSERR**
- 内存分配错误。
- 从密码文件描述符读取错误。

**EX_DATAERR**
- 命令行上或通过密码文件描述符提供或缺失的数据错误或无效。
- 试图删除、重命名 root 帐户或更改其 uid。

**EX_OSFILE**
- skeleton 目录无效或不存在。
- 基本主目录无效或不存在。
- 指定了无效或不存在的 shell。

**EX_NOUSER**
- 指定的用户、用户 id、组或组 id 不存在。
- 记录、添加或修改的用户或组意外消失。

**EX_SOFTWARE**
- 指定范围内没有更多的组或用户 id 可用。

**EX_IOERR**
- 无法重写配置文件。
- 更新组或用户数据库文件出错。
- passwd 或组数据库文件更新错误。

**EX_CONFIG**
- 未配置基本主目录。

## 参见

chpass(1), [passwd(1)](../man1/passwd.1.md), [umask(2)](../sys/umask.2.md), [group(5)](../man5/group.5.md), [login.conf(5)](../man5/login.conf.5.md), [passwd(5)](../man5/passwd.5.md), pw.conf(5), [groups(7)](../man7/groups.7.md), [pwd_mkdb(8)](pwd_mkdb.8.md), [vipw(8)](vipw.8.md), [zfs(8)](zfs.8.md)

## 历史

`pw` 工具的编写旨在模仿 SYSV *shadow* 支持套件中使用的许多选项，但针对 4.4BSD 操作系统特有的 passwd 和 group 字段进行了修改，并将所有主要元素组合到单个命令中。
