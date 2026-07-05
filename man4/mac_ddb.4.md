# mac_ddb.4

`mac_ddb` — 受限的内核调试器接口策略

## 名称

`mac_ddb`

## 概要

要将 ddb 策略编译进内核，请在内核配置文件中加入以下行：

> options MAC
> options MAC_DDB

或者，要在引导时加载 ddb 模块，请在内核配置文件中加入以下行：

> options MAC

并在 loader.conf(5) 中加入：

```sh
mac_ddb_load="YES"
```

## 描述

`mac_ddb` 策略模块实现一个 MAC 策略，限制可在 [ddb(4)](ddb.4.md) 命令提示符下使用的命令集。允许的命令子集仅限于那些不会读写任意内存位置的命令。这样做是为了阻止可能泄露系统机密的行为，同时仍允许足够的调试器功能来诊断内核 panic。例如，此策略允许 `trace` 或 `show registers` 命令，但不允许 `show` `buffer` `addr`。

所有以 `DB_CMD_MEMSAFE` 标志声明的调试器命令都被 `mac_ddb` 允许。该策略提供验证函数，根据用户提供的参数有条件地允许某些额外命令。

加载时，`mac_ddb` 策略还确保仅可执行 [ddb(4)](ddb.4.md) 调试器后端；不可执行 [gdb(4)](gdb.4.md)。

### 标签格式

`mac_ddb` 未定义任何标签。

## 参见

[ddb(4)](ddb.4.md), [mac(4)](mac.4.md), [mac_biba(4)](mac_biba.4.md), [mac_bsdextended(4)](mac_bsdextended.4.md), [mac_ifoff(4)](mac_ifoff.4.md), [mac_lomac(4)](mac_lomac.4.md), [mac_mls(4)](mac_mls.4.md), [mac_none(4)](mac_none.4.md), [mac_partition(4)](mac_partition.4.md), [mac_portacl(4)](mac_portacl.4.md), [mac_seeotheruids(4)](mac_seeotheruids.4.md), [mac_test(4)](mac_test.4.md), [mac(9)](../man9/mac.9.md)

## 缺陷

虽然 MAC 框架设计旨在支持对 root 用户的限制，但并非所有攻击渠道目前都受到入口点检查的保护。因此，不应单独依赖 MAC 框架策略来防范恶意的特权用户。
