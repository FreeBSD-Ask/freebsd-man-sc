# rpc_secure(3)

`rpc_secure` — 用于安全远程过程调用的库例程

## 名称

`rpc_secure`

## 概要

`#include <rpc/rpc.h>`

```c
AUTH *
authdes_create(char *name, unsigned window, struct sockaddr *addr,
    des_block *ckey);

int
authdes_getucred(struct authdes_cred *adc, uid_t *uid, gid_t *gid,
    int *grouplen, gid_t *groups);

int
getnetname(char *name);

int
host2netname(char *name, const char *host, const char *domain);

int
key_decryptsession(const char *remotename, des_block *deskey);

int
key_encryptsession(const char *remotename, des_block *deskey);

int
key_gendes(des_block *deskey);

int
key_setsecret(const char *key);

int
netname2host(char *name, char *host, int hostlen);

int
netname2user(char *name, uid_t *uidp, gid_t *gidp, int *gidlenp,
    gid_t *gidlist);

int
user2netname(char *name, const uid_t uid, const char *domain);
```

## 描述

这些例程是 RPC 库的一部分，实现了 DES 认证。关于 RPC 的更多细节，参见 [rpc(3)](rpc.3.md)。

`authdes_create` 是与 RPC 安全认证系统（即 DES 认证）接口的两个例程中的第一个。第二个是下文所述的 `authdes_getucred`。

注意：DES 认证系统要正常工作，必须运行 keyserv(8) 守护进程。

`authdes_create` 函数用于客户端，返回一个认证句柄，使安全认证系统可用。第一个参数 `name` 是服务器进程所有者的网络名称（即 `netname`）。该字段通常表示来自实用例程 `host2netname` 的 `hostname`，但也可以使用 `user2netname` 表示用户名。第二个字段是客户端凭据的有效窗口，以秒为单位。小窗口比大窗口更安全，但如果窗口太小，会因时钟漂移而增加重新同步的频率。第三个参数 `addr` 是可选的。如果为 `NULL`，认证系统将假定本地时钟始终与服务器时钟同步，不会尝试重新同步。但是，如果提供了地址，则系统会在需要重新同步时使用该地址查询远程时间服务。此参数通常是 RPC 服务器本身的地址。最后一个参数 `ckey` 也是可选的。如果为 `NULL`，认证系统将生成一个随机 DES 密钥，用于加密凭据。但是，如果提供了该参数，则使用它代替。

`authdes_getucred` 函数是两个 DES 认证例程中的第二个，用于在服务器端将操作系统无关的 DES 凭据转换为 UNIX 凭据。该例程与实用例程 `netname2user` 的不同之处在于，`authdes_getucred` 从缓存中获取信息，不必每次调用时都进行 Yellow Pages 查找。

`getnetname` 函数将调用方的唯一、操作系统无关的网络名称安装到定长数组 `name` 中。成功时返回 `TRUE`，失败时返回 `FALSE`。

`host2netname` 函数将特定于域的主机名转换为操作系统无关的网络名称。成功时返回 `TRUE`，失败时返回 `FALSE`。是 `netname2host` 的逆操作。

`key_decryptsession` 函数是与 RPC 安全认证系统（即 DES 认证）相关的密钥服务器守护进程接口。用户程序很少需要调用它或其相关例程 `key_encryptsession`、`key_gendes` 和 `key_setsecret`。系统命令（如 [login(1)](../man1/login.1.md)）和 RPC 库是这四个例程的主要客户端。

`key_decryptsession` 函数接受服务器网络名称和 DES 密钥，并使用服务器的公钥和与调用进程有效 uid 关联的私钥解密该密钥。它是 `key_encryptsession` 的逆操作。

`key_encryptsession` 函数是密钥服务器接口例程。它接受服务器网络名称和 DES 密钥，并使用服务器的公钥和与调用进程有效 uid 关联的私钥加密该密钥。它是 `key_decryptsession` 的逆操作。

`key_gendes` 函数是密钥服务器接口例程。它用于向密钥服务器请求安全会话密钥。选择一个“随机”密钥通常不够好，因为常见的随机数选择方法（如使用当前时间）非常容易被猜到。

`key_setsecret` 函数是密钥服务器接口例程。它用于设置调用进程有效 `uid` 的密钥。

`netname2host` 函数将操作系统无关的网络名称转换为特定于域的主机名。成功时返回 `TRUE`，失败时返回 `FALSE`。是 `host2netname` 的逆操作。

`netname2user` 函数将操作系统无关的网络名称转换为特定于域的用户 ID。成功时返回 `TRUE`，失败时返回 `FALSE`。是 `user2netname` 的逆操作。

`user2netname` 函数将特定于域的用户名转换为操作系统无关的网络名称。成功时返回 `TRUE`，失败时返回 `FALSE`。是 `netname2user` 的逆操作。

## 参见

[rpc(3)](rpc.3.md), [xdr(3)](xdr.3.md)

以下手册：

> *Remote Procedure Calls: Protocol Specification*.

> *Remote Procedure Call Programming Guide*.

> *Rpcgen Programming Guide*.

> *RPC: Remote Procedure Call Protocol Specification*, RFC1050, Sun Microsystems Inc., USC-ISI.
