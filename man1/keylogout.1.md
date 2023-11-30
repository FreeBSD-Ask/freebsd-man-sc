  KEYLOGOUT(1)  

KEYLOGOUT(1)

FreeBSD General Commands Manual

KEYLOGOUT(1)

[名称](#__u540D___u79F0_)
=======================

`keylogout` —

删除存储的密钥

[概要](#__u6982___u8981_)
=======================

`keylogout` \[`-f`\]

[描述](#__u63CF___u8FF0_)
=======================

`keylogout` 实用程序删除由密钥服务器进程 keyserv(8) 存储的密钥，以供任何安全网络服务（例如 NFS）使用。 对密钥的进一步访问将被撤销，但当前会话密钥可能会保持有效，直到它们过期或被刷新。 此选项将导致任何需要安全 RPC 服务的后台作业失败，以及任何需要密钥的计划 `at` 作业失败。 此外，由于密钥的机器上只保留一个副本，因此将其放在您的 .logout 文件中是一个坏主意，因为它会影响同一台机器上的其他会话。

以下选项可用：

[`-f`](#f)

忘记根密钥。如果在服务器上完成，这将破坏安全 NFS。

[参见](#__u53C2___u89C1_)
=======================

chkey(1), keylogin(1), login(1), publickey(5), keyserv(8), newkey(8)

April 15, 1989

FreeBSD 13.1-RELEASE