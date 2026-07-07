# enigma(1)

`enigma` — 非常简单的文件加密工具

## 名称

`enigma`, `crypt`

## 概要

`enigma [-s] [-k] [password]`

`crypt [-s] [-k] [password]`

## 描述

`enigma` 实用程序（又称 `crypt`）是一个**非常**简单的加密程序，基于“密钥”方式工作。它作为过滤器运行，即从标准输入读取数据流进行加密或解密，并将结果写入标准输出。由于其操作完全对称，将加密后的数据流再次通过该引擎（使用同一密钥）即可完成解密。

向程序提供密钥的方式有多种。默认情况下，程序会在控制终端上通过 getpass(3) 提示用户输入密钥。这是唯一安全的提供方式。

另一种方式是在启动程序时，将密钥作为唯一的命令行参数 `password` 提供。显然，这种方式下密钥很容易被其他运行 [ps(1)](ps.1.md) 的用户发现。作为另一种替代方案，可以为 `crypt` 指定 `-k` 选项，程序会从环境变量 `CrYpTkEy` 中读取密钥。虽然乍看之下这比前一种方式更安全，但实际上并非如此，因为环境变量同样可以通过 [ps(1)](ps.1.md) 查看。因此该选项主要是为了与其他 `crypt` 实现兼容而提供。

指定 `-s` 选项时，`crypt` 会对加密引擎进行修改，旨在使其稍微更安全，但与其他实现不兼容。

### 警告

`crypt` 的加密价值相当有限。此处提供该程序仅为与同样提供了实现（通常称为 crypt(1)）的其他操作系统兼容。如需真正的加密，请参阅 openssl(1) 或 gpg(1)（`ports/security/gnupg1`）。

## 环境变量

**`CrYpTkEy`** 在指定了 `-k` 选项时用于获取密钥

## 实例

```sh
man enigma | enigma > encrypted
Enter key: (XXX — 密钥不回显)
```

上述命令会生成本手册页的加密形式，并将其存储到文件 `encrypted` 中。

```sh
enigma XXX < encrypted
```

上述命令会在终端上显示先前创建的文件。

## 参见

gpg(1)（`ports/security/gnupg1`），openssl(1)，[ps(1)](ps.1.md)，getpass(3)

## 历史

`crypt` 的实现在 UNIX 操作系统中非常普遍。本实现取自处于公有领域的 *Cryptbreakers Workbench*。
