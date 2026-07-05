# freebsd-update.conf.5

`freebsd-update.conf` — [freebsd-update(8)](../man8/freebsd-update.8.md) 的配置文件

## 名称

`freebsd-update.conf` [freebsd-update(8)](../man8/freebsd-update.8.md)

## 描述

`freebsd-update.conf` 文件控制 [freebsd-update(8)](../man8/freebsd-update.8.md) 实用程序的行为。该文件包含若干行，每行由一个区分大小写的选项名和零个或多个参数组成。空行以及行中跟在 `#` 字符之后的部分会被忽略。除非另有说明，多次指定同一选项是错误的。

可用的选项及其含义如下：

**`AllowAdd`** 此关键字后的单个参数必须为 “yes” 或 “no”，指定 [freebsd-update(8)](../man8/freebsd-update.8.md) 是否允许在下载的更新中包含新文件、目录和符号链接时创建它们。注意，[freebsd-update(8)](../man8/freebsd-update.8.md) 不会重新添加已从 FreeBSD 安装中删除的文件，除非这些文件此前是作为更新的一部分添加的。

**`AllowDelete`** 此关键字后的单个参数必须为 “yes” 或 “no”，指定 [freebsd-update(8)](../man8/freebsd-update.8.md) 是否允许在下载的更新中删除文件、目录和符号链接。

**`BackupKernel`** 此关键字后的单个参数必须为 “yes” 或 “no”，指定 [freebsd-update(8)](../man8/freebsd-update.8.md) 是否在安装新内核之前创建旧内核的备份。该备份内核可用于在新安装的内核出现问题时恢复系统。注意，[freebsd-update(8)](../man8/freebsd-update.8.md) 的 rollback 命令不会将备份内核恢复到其原始状态。

**`BackupKernelDir`** 此关键字设置用于存储备份内核的目录（如果启用了 BackupKernel 功能）。如果该目录已存在，且不是由 [freebsd-update(8)](../man8/freebsd-update.8.md) 创建的，则跳过该目录。如果主目录名不可用，则在目录名后追加从 ‘1’ 开始的数字。与主目录名一样，构造的目录名仅在该路径不存在或该目录此前由 [freebsd-update(8)](../man8/freebsd-update.8.md) 创建时才使用。如果构造的目录仍然存在，则将追加的数字加 1 并重新启动目录搜索过程。如果数字增量超过 9，[freebsd-update(8)](../man8/freebsd-update.8.md) 将中止。

**`BackupKernelSymbolFiles`** 此关键字后的单个参数必须为 “yes” 或 “no”，指定 [freebsd-update(8)](../man8/freebsd-update.8.md) 是否还会备份内核符号文件（如果存在）。内核符号文件占用大量磁盘空间，且恢复时不需要。如果需要符号文件，在使用备份内核恢复系统后，[freebsd-update(8)](../man8/freebsd-update.8.md) 的 rollback 命令会随旧内核一起重新创建符号文件。

**`Components`** 此关键字后的参数是即将更新的 FreeBSD 组件或子组件。组件为 “src”（源代码）、“world”（非内核二进制文件）和 “kernel”；子组件是作为发布过程一部分生成的各个分发集（例如 “src/base”、“src/sys”、“world/base”、“world/catpages”、“kernel/smp”）。注意，在 FreeBSD 6.1 之前，“kernel” 组件作为 “world/base” 的一部分分发。此选项可以多次指定，参数会累积。

**`CreateBootEnv`** 此关键字后的单个参数必须为 “yes” 或 “no”，指定 [freebsd-update(8)](../man8/freebsd-update.8.md) 是否在安装补丁时使用 bectl(8) 创建新的引导环境。新引导环境的名称由当前 FreeBSD 版本：

```sh
freebsd-version -ku | sort -V | tail -n 1
```

和时间戳：

```sh
date +"%Y-%m-%d_%H%M%S"
```

组成，两者以单个短横线分隔，例如：

```sh
13.0-RELEASE-p7_2022-02-16_141502
```

如果以下任何情况适用，[freebsd-update(8)](../man8/freebsd-update.8.md) 不会尝试创建引导环境：

- 未使用 ZFS。
- ZFS 根未设置为引导环境（详见 bectl(8) 的 check 命令）。
- [freebsd-update(8)](../man8/freebsd-update.8.md) 正在 [jail(8)](../man8/jail.8.md) 中运行。
- [freebsd-update(8)](../man8/freebsd-update.8.md) 正在更新通过 basedir（`-b`）或 jail（`-j`）标志选定的根目录。

**`IDSIgnorePaths`** 此关键字后的参数是正则表达式；以匹配这些正则表达式之一的字符串开头的路径将被 [freebsd-update(8)](../man8/freebsd-update.8.md) IDS 忽略。此选项可以多次指定，参数会累积。

**`IgnorePaths`** 此关键字后的参数是正则表达式；以匹配这些正则表达式之一的字符串开头的路径的更新将被忽略。此选项可以多次指定，参数会累积。

**`KeepModifiedMetadata`** 此关键字后的单个参数必须为 “yes” 或 “no”，指定 [freebsd-update(8)](../man8/freebsd-update.8.md) 在安装更新时是否应保留已本地修改的文件所有权、权限和标志。

**`KeyPrint`** 此关键字后的单个参数是受信任用于签署更新的 RSA 密钥的 SHA256 哈希。

**`MailTo`** 此关键字后的单个参数是 cron(8) 输出将邮寄到的地址。

**`MergeChanges`** 此关键字后的参数是正则表达式；以匹配这些正则表达式之一的字符串开头的路径的更新将与本地修改合并。此选项可以多次指定，参数会累积。

**`ServerName`** 此关键字后的单个参数是即将从中下载更新的服务器或服务器池的名称。

**`StrictComponents`** 此关键字后的单个参数必须为 “yes” 或 “no”，指定 [freebsd-update(8)](../man8/freebsd-update.8.md) 应将通过 `Components` 选项指定的 FreeBSD 组件列表严格解释为已安装且应在 `upgrade` 命令使用时升级的组件列表（“yes”），还是仅作为可能已安装的组件列表，由 [freebsd-update(8)](../man8/freebsd-update.8.md) 识别实际存在哪些（“no”）。

**`UpdateIfUnmodified`** 此关键字后的参数是正则表达式；以匹配这些正则表达式之一的字符串开头的路径的更新，如果文件已在本地修改，将被忽略（除非它们被合并——参见 `MergeChanges` 选项）。此选项可以多次指定，参数会累积。

**`WorkDir`** 此关键字后的单个参数是临时文件和下载的更新将存储于其中的目录。

## 文件

**`/etc/freebsd-update.conf`** [freebsd-update(8)](../man8/freebsd-update.8.md) 配置文件的默认位置。

## 参见

[sha256(1)](../man1/sha256.1.md), bectl(8), [freebsd-update(8)](../man8/freebsd-update.8.md)

## 作者

Colin Percival <cperciva@FreeBSD.org>
