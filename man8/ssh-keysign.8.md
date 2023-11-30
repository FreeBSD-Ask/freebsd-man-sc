  SSH-KEYSIGN(8)  

SSH-KEYSIGN(8)

FreeBSD System Manager's Manual

SSH-KEYSIGN(8)

[名称](#__u540D___u79F0_)
=======================

`ssh-keysign` —

用于基于主机的身份验证的 ssh 帮助程序

[概要](#__u6982___u8981_)
=======================

`ssh-keysign`

[描述](#__u63CF___u8FF0_)
=======================

ssh(1) 使用 `ssh-keysign` 访问本地主机密钥并生成基于主机的身份验证期间所需的数字签名。

`ssh-keysign` 默认禁用，只能在全局客户端配置文件 /etc/ssh/ssh\_config 中通过将 `EnableSSHKeysign` 设置为 “yes” 来启用。

`ssh-keysign` 不打算由用户调用，而是从 ssh(1) 调用。 有关基于主机的身份验证的更多信息，请参阅 ssh(1) 和 sshd(8) 。

[文件](#__u6587___u4EF6_)
=======================

/etc/ssh/ssh\_config

控制是否启用 `ssh-keysign` 。

/etc/ssh/ssh\_host\_dsa\_key

/etc/ssh/ssh\_host\_ecdsa\_key

/etc/ssh/ssh\_host\_ed25519\_key

/etc/ssh/ssh\_host\_rsa\_key

这些文件包含用于生成数字签名的主机密钥的私有部分。 它们应该由 root 拥有，只能由 root 读取，并且其他人无法访问。 由于它们只能由 root 读取，因此如果使用基于主机的身份验证，则 `ssh-keysign` 必须设置为 root。

/etc/ssh/ssh\_host\_dsa\_key-cert.pub

/etc/ssh/ssh\_host\_ecdsa\_key-cert.pub

/etc/ssh/ssh\_host\_ed25519\_key-cert.pub

/etc/ssh/ssh\_host\_rsa\_key-cert.pub

如果这些文件存在，则假定它们包含与上述私钥对应的公共证书信息。

[参见](#__u53C2___u89C1_)
=======================

ssh(1), ssh-keygen(1), ssh\_config(5), sshd(8)

[历史](#__u5386___u53F2_)
=======================

`ssh-keysign` 首次出现在 OpenBSD 3.2 中。

[作者](#__u4F5C___u8005_)
=======================

Markus Friedl <[markus@openbsd.org](mailto:markus@openbsd.org)\>

February 17, 2016

FreeBSD 13.1-RELEASE