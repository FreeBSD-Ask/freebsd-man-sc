# veriexec(8)

`veriexec` — 操作 mac_veriexec 的状态

## 名称

`veriexec`

## 概要

`veriexec [-v] [-C directory] [-S] manifest` `veriexec -z state` `veriexec -i state` `veriexec -l file ...` `veriexec -x file ...`

## 描述

`veriexec` 是一个用于查询或操作 mac_veriexec(4) 状态的工具。

第一种形式用于加载 `manifest`。`veriexec` 首先验证 `manifest` 的数字签名，如果成功，则解析它并将其内容馈送给内核。`-S` 标志指示应检查证书有效性。没有此标志，具有过期证书的有效签名仍会被接受。

带 `-z` 的第二种形式用于修改 `state`，带 `-i` 的形式用于查询当前 `state`。

带 `-l` 时，`veriexec` 将报告与假定作为文件的剩余参数关联的任何标签。如果只给出单个文件参数，将报告裸标签（如果有），否则报告路径名后跟标签。

带 `-x` 的最后一种形式用于测试 `file` 是否已验证。这要求 mac_veriexec(4) 处于 `active` 或 `enforce` 状态。

可能的状态如下：

**`loaded`** 在第一个 `manifest` 加载后自动设置。

**`active`** mac_veriexec(4) 将开始检查文件。此状态只能从 `loaded` 状态进入。

**`enforce`** mac_veriexec(4) 将拒绝尝试 [execve(2)](../sys/execve.2.md) 或 [open(2)](../sys/open.2.md) 带 `O_VERIFY` 的文件，除非已验证。

**`locked`** 阻止加载更多清单。

设置或查询状态时，提供所需状态的唯一前缀即可。因此 `-i` `a` 或 `-z` `e` 已足够，但 `-i` `loc` 是为避免与 `loaded` 混淆所需的最低要求。

## 清单

清单包含相对路径名到指纹的映射，带有可选标志。例如：

```sh
sbin/veriexec sha256=f22136...c0ff71 no_ptrace trusted
usr/bin/python sha256=5944d9...876525 indirect
sbin/somedaemon sha256=77fc2f...63f5687 label=mod1/val1,mod2/val2
```

支持的标志如下：

**`indirect`** 该可执行文件不能直接运行，但可以用作解释器，例如通过：

```sh
#!/usr/bin/python
```

**`no_fips`** 如果系统有在 FIPS 模式下运行的概念，则标记为此标志的文件将不允许被执行。

**`no_ptrace`** 不允许在调试器下运行可执行文件。对任何对系统安全状态至关重要的应用程序很有用。

**`trusted`** 进程要使用 [veriexec(4)](../man4/veriexec.4.md) 与 mac_veriexec(4) 交互，需要此标志。通常只有 `veriexec` 需要此标志。隐含 `no_ptrace`。

`label` 参数允许将 [maclabel(7)](../man7/maclabel.7.md) 与文件关联。`veriexec` 和 mac_veriexec(4)（如果它支持标签）都不关注标签的内容，它们提供标签是为了供其他 [mac(4)](../man4/mac.4.md) 模块或其他应用程序使用。

## 实例

为挂载在 **`/mnt`** 上的 tarfs(5) 软件包加载清单，并严格执行证书有效性检查：

```sh
# veriexec -S -C /mnt /mnt/manifest
```

`veriexec` 将查找它识别的分离签名，例如 `manifest.asc`（OpenPGP）或 `manifest.*sig`（X.509）。对于 X.509 签名，还需要匹配的证书链 `manifest.*certs`。无论哪种情况，信任库中都需要有合适的信任锚。

现在可以激活：

```sh
# veriexec -z active
```

任何用户都可以检查 mac_veriexec(4) 是否为 `active`：

```sh
$ veriexec -i active
```

任何用户都可以检查 **`/mnt/bin/app`** 是否已验证：

```sh
$ veriexec -x /mnt/bin/app
```

如果未验证，将收到 Authentication 错误，但除非 mac_veriexec(4) 处于 enforce 状态，否则仍能运行它。

## 注释

只有当已加载足够的清单以覆盖所有可能需要运行的应用程序时，将 mac_veriexec(4) 设置为 `enforce` 状态才是安全的。

## 历史

Verified Exec 系统首次出现于 NetBSD。此工具源自 Junos 中的工具，后者要求数字签名清单文件。
