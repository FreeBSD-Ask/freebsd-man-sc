# ssh-keysign.8

`ssh-keysign` — 用于基于主机的认证的 OpenSSH 助手

## 名称

`ssh-keysign`

## 概要

`ssh-keysign`

## 描述

`ssh-keysign` 由 [ssh(1)](../man1/ssh.1.md) 使用，用于访问本地主机密钥并生成基于主机的认证过程中所需的数字签名。

`ssh-keysign` 默认禁用，只能在全局客户端配置文件 **/etc/ssh/ssh_config** 中通过将 `EnableSSHKeysign` 设置为 “yes” 来启用。

`ssh-keysign` 不应由用户直接调用，而是由 [ssh(1)](../man1/ssh.1.md) 调用。关于基于主机的认证的更多信息，参见 [ssh(1)](../man1/ssh.1.md) 和 sshd(8)。

## 文件

**`/etc/ssh/ssh_config`** 控制是否启用 `ssh-keysign`。

**`/etc/ssh/ssh_host_ecdsa_key`**

**`/etc/ssh/ssh_host_ed25519_key`**

**`/etc/ssh/ssh_host_rsa_key`** 这些文件包含用于生成数字签名的主机密钥的私钥部分。它们应归 root 所有，仅 root 可读，且其他人不可访问。由于仅 root 可读，若使用基于主机的认证，`ssh-keysign` 必须设置为 set-uid root。

**`/etc/ssh/ssh_host_ecdsa_key-cert.pub`**

**`/etc/ssh/ssh_host_ed25519_key-cert.pub`**

**`/etc/ssh/ssh_host_rsa_key-cert.pub`** 如果这些文件存在，则假定它们包含与上述私钥对应的公共证书信息。

## 参见

[ssh(1)](../man1/ssh.1.md), [ssh-keygen(1)](../man1/ssh-keygen.1.md), ssh_config(5), sshd(8)

## 历史

`ssh-keysign` 首次出现于 OpenBSD 3.2。

## 作者

Markus Friedl <markus@openbsd.org>
