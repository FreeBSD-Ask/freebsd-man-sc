  KEYLOGIN(1)  

KEYLOGIN(1)

FreeBSD General Commands Manual

KEYLOGIN(1)

[名称](#__u540D___u79F0_)
=======================

`keylogin` —

解密和存储密钥

[概要](#__u6982___u8981_)
=======================

`keylogin`

[描述](#__u63CF___u8FF0_)
=======================

`keylogin` 实用程序提示用户输入登录密码，并使用它来解密存储在 publickey(5) 数据库中的用户密钥。解密后，用户的密钥由本地密钥服务器进程 keyserv(8) 存储，以供任何安全网络服务（例如 NFS）使用。

[参见](#__u53C2___u89C1_)
=======================

chkey(1), keylogout(1), login(1), publickey(5), keyserv(8), newkey(8)

September 9, 1987

FreeBSD 13.1-RELEASE