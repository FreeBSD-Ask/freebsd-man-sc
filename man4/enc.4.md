# enc.4

`enc` — 封装接口

## 名称

`enc`

## 概要

`若要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device enc

`或者，若要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_enc_load="YES"
```

## 描述

`enc` 接口是一种软件回环机制，允许主机或防火墙使用任何通过 [pfil(9)](../man9/pfil.9.md) 框架接入的防火墙软件包来过滤 [ipsec(4)](ipsec.4.md) 流量。

`enc` 接口允许管理员通过 [tcpdump(1)](../man1/tcpdump.1.md) 查看 [ipsec(4)](ipsec.4.md) 处理前后（即将处理或已处理）的传入和传出数据包。

“`enc0`”接口继承所有 IPsec 流量。因此，所有 IPsec 流量都可基于“`enc0`”进行过滤，并且通过在“`enc0`”接口上调用 [tcpdump(1)](../man1/tcpdump.1.md) 可查看所有 IPsec 流量。

可通过以下 [sysctl(8)](../man8/sysctl.8.md) 变量独立控制 [tcpdump(1)](../man1/tcpdump.1.md) 能看到的内容以及通过 [pfil(9)](../man9/pfil.9.md) 框架传递给防火墙的内容：

| **名称	默认值	建议值** |
| --- |
| net.enc.out.ipsec_bpf_mask	0x00000003	0x00000001 |
| net.enc.out.ipsec_filter_mask	0x00000001	0x00000001 |
| net.enc.in.ipsec_bpf_mask	0x00000001	0x00000002 |
| net.enc.in.ipsec_filter_mask	0x00000001	0x00000002 |

对于传入路径，值 `0x1` 表示“`在剥离外部头之前`”，`0x2` 表示“`在剥离外部头之后`”。对于传出路径，`0x1` 表示“`仅含内部头`”，`0x2` 表示“`含外部和内部头`”。

```sh
incoming path                                          |------|
---- IPsec processing ---- (before) ---- (after) ----> |      |
                                                       | Host |
<--- IPsec processing ---- (after) ----- (before) ---- |      |
outgoing path                                          |------|
```

大多数用户会希望以建议的默认值运行 `ipsec_filter_mask`，并依赖安全策略数据库处理外部头。

注意，数据包由 BPF 在防火墙处理之前捕获。可在 `ipsec_bpf_mask` 中配置特殊值 0x4，数据包也会在防火墙处理之后被捕获。

## 实例

要查看通过 [ipsec(4)](ipsec.4.md) 处理的数据包，按需调整 [sysctl(8)](../man8/sysctl.8.md) 变量，然后运行：

```sh
tcpdump -i enc0
```

## 参见

[tcpdump(1)](../man1/tcpdump.1.md), [bpf(4)](bpf.4.md), ipf(4), ipfw(4), [ipsec(4)](ipsec.4.md), [pf(4)](pf.4.md)
