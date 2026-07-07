# publickey(3)

`publickey` — 获取公钥或私钥

## 名称

`publickey`

## 库

Lb librpcsvc

## 概要

`#include <rpc/rpc.h>`

`#include <rpc/key_prot.h>`

```c
int
getpublickey(const char netname[MAXNETNAMELEN+1],
    char publickey[HEXKEYBYTES+1]);

int
getsecretkey(char netname[MAXNETNAMELEN+1],
    char secretkey[HEXKEYBYTES+1], char *passwd);
```

## 描述

这些例程用于从 YP 数据库获取公钥和私钥。`getsecretkey` 函数有一个额外的参数 `passwd`，用于解密存储在数据库中的已加密私钥。两个例程在成功找到密钥时返回 1，否则返回 0。密钥以 `NUL` 结尾的十六进制字符串形式返回。如果提供给 `getsecretkey` 的密码未能解密私钥，例程将返回 1，但 `secretkey` 参数将为 `NUL` 字符串（“”）。

## 参见

publickey(5)

RPC Programmer's Manual 位于 **/usr/share/doc/psd/23.rpc**。
