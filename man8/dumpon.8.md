# dumpon(8)

`dumpon` — 指定崩溃转储设备

## 名称

`dumpon`

## 概要

`dumpon [-i index] [-r] [-v] [-C cipher] [-k pubkey] [-Z] [-z] device` `dumpon [-i index] [-r] [-v] [-C cipher] [-k pubkey] [-Z] [-z] [-g gateway] -s server -c client iface` `dumpon [-v] off` `dumpon [-v] -l`

## 描述

`dumpon` 工具用于配置内核在发生 panic 时可以将崩溃转储保存到哪里。

系统管理员通常应使用 [rc.conf(5)](../man5/rc.conf.5.md) 变量 `dumpdev` 和 `dumpon_flags` 以持久方式配置 `dumpon`。有关此用法的更多信息，请参见 [rc.conf(5)](../man5/rc.conf.5.md)。

从 FreeBSD 13.0 开始，`dumpon` 可以配置一系列回退转储设备。例如，管理员可能默认首选 [netdump(4)](../man4/netdump.4.md)，但如果无法访问 [netdump(4)](../man4/netdump.4.md) 服务或发生其他故障，他们可能会选择本地磁盘转储作为第二选项。

### 通用选项

**`-i`** `index` 将指定的转储配置插入到按优先级排序的回退转储设备列表中的指定索引位置，从零开始。如果未指定 `-i`，则配置的转储设备将被追加到优先级列表末尾。

**`-r`** 从回退转储设备列表中删除指定的转储设备配置，而不是插入或追加它。相比之下，“`dumpon` off”会删除所有已配置的设备。与 `-i` 冲突。

**`-k`** `pubkey` 配置加密内核转储。每次使用 `dumpon` 时都会自动生成一个随机的一次性对称密钥，用于内核转储的批量加密。提供的 `pubkey` 用于加密对称密钥的副本。加密的转储内容由标准转储头、公钥加密的对称密钥内容以及经对称密钥加密的核心转储内容组成。因此，只有拥有相应私钥的人才能解密对称密钥。对称密钥是解密内核核心所必需的。此机制的目标是提供机密性。`pubkey` 文件应为至少 2048 位的 PEM 格式 RSA 密钥。

**`-C`** `cipher` 选择用于加密内核崩溃转储的对称算法。默认为“chacha20”，但也提供“aes256-cbc”。（AES256-CBC 模式不能与压缩同时使用。）

**`-l`** 列出当前配置的转储设备，如果未配置任何设备则为 /dev/null。

**`-v`** 启用详细模式。

**`-Z`** 启用压缩（Zstandard）。

**`-z`** 启用压缩（gzip）。一次只能启用一种压缩方法，因此 `-z` 与 `-Z` 不兼容。Zstandard 提供更优的压缩比和性能。

### Netdump

`dumpon` 还可以配置内核将转储发送到远程 netdumpd(8) 服务器。（netdumpd(8) 服务器在 ports 中可用。）[netdump(4)](../man4/netdump.4.md) 消除了为崩溃转储保留空间的需要。它在无盘环境中特别有用。当使用 `dumpon` 配置 netdump 时，`device`（或 `iface`）参数应指定一个网络接口（例如 `igb1`）。指定的网卡必须处于 up（在线）状态才能配置 netdump。

[netdump(4)](../man4/netdump.4.md) 特定选项包括：

**`-c`** `client` [netdump(4)](../man4/netdump.4.md) 客户端的本地 IP 地址。

**`-g`** `gateway` `client` 和 `server` 之间的第一跳路由器。如果未指定 `-g` 选项且系统有默认路由，则使用默认路由器作为 [netdump(4)](../man4/netdump.4.md) 网关。如果未指定 `-g` 选项且系统没有默认路由，则假定 `server` 与 `client` 在同一链路上。

**`-s`** `server` netdumpd(8) 服务器的 IP 地址。

所有这些选项都可以在 [rc.conf(5)](../man5/rc.conf.5.md) 变量 `dumpon_flags` 中指定。

### Minidumps

内核崩溃转储的默认类型是迷你崩溃转储。迷你崩溃转储只保存内核正在使用的内存页。或者，可以通过将 `debug.minidump` [sysctl(8)](sysctl.8.md) 变量设置为 0 来启用完整内存转储。

### 完整转储

对于使用完整内存转储的系统，指定的转储设备大小必须至少等于物理内存的大小。即使转储中添加了额外的 64 kB 头，平台的 BIOS 通常会保留一些内存，因此通常不需要将转储设备的大小设置得比机器中实际可用的 RAM 量更大。此外，使用完整内存转储时，`dumpon` 工具将拒绝启用小于 `hw.physmem` [sysctl(8)](sysctl.8.md) 变量报告的物理内存总量的转储设备。

## SYSCTL 变量

以下 [sysctl(8)](sysctl.8.md) 变量可用于修改或监视崩溃转储的行为：

**`debug.minidump`** 设置内核崩溃转储的类型。可能值为 0 表示完整崩溃转储，1 表示迷你转储。默认为迷你转储。

**`machdep.dump_retry_count`** 放弃之前转储重试的最大次数。默认值为 5。此 sysctl 仅在 PowerPC 和 AMD64 上受支持。

## 实现说明

由于在获取崩溃转储时文件系统层已经失效，因此无法将崩溃转储直接发送到文件。

[loader(8)](loader.8.md) 变量 `dumpdev` 可用于为在用户空间启动之前发生的系统 panic 启用早期内核核心转储。

## 实例

要生成 RSA 私钥，用户可以使用 genrsa(1) 工具：

```sh
# openssl genrsa -out private.pem 4096
```

可以使用 rsa(1) 工具从私钥中提取公钥：

```sh
# openssl rsa -in private.pem -out public.pem -pubout
```

在安全位置创建 RSA 密钥后，可以将公钥移动到不可信的 netdump 客户端机器上。现在 `public.pem` 可以被 `dumpon` 用来配置加密的内核崩溃转储：

```sh
# dumpon -k public.pem /dev/ada0s1b
```

建议测试内核是否使用当前配置保存加密的崩溃转储。最简单的方法是使用 [ddb(4)](../man4/ddb.4.md) 调试器引发内核 panic：

```sh
# sysctl debug.kdb.panic=1
```

在调试器中，应输入以下命令以写入核心转储并重启：

```sh
db> dump
```

```sh
db> reset
```

重启后，savecore(8) 应该能够将核心转储保存到“dumpdir”目录中，默认为 **`/var/crash`**：

```sh
# savecore /dev/ada0s1b
```

核心目录中应创建三个文件：`info.#`、`key.#` 和 `vmcore_encrypted.#`（其中“#”是 savecore(8) 保存的最后一个核心转储的编号）。`vmcore_encrypted.#` 可以使用 decryptcore(8) 工具解密：

```sh
# decryptcore -p private.pem -k key.# -e vmcore_encrypted.# -c vmcore.#
```

或更简短的形式：

```sh
# decryptcore -p private.pem -n #
```

现在可以使用 kgdb(1)（`ports/devel/gdb`）检查 `vmcore.#`：

```sh
# kgdb /boot/kernel/kernel vmcore.#
```

或更简短的形式：

```sh
# kgdb -n #
```

如果 kgdb(1)（`ports/devel/gdb`）没有打印任何错误，则核心已正确解密。注意，活动内核可能位于不同路径，可以通过查看 `kern.bootfile` [sysctl(8)](sysctl.8.md) 来检查。

`dumpon` [rc(8)](rc.8.md) 脚本在引导早期运行，通常在配置网络之前。这使得它不适合在客户端地址为动态时配置 [netdump(4)](../man4/netdump.4.md)。要在 dhclient(8) 绑定到服务器时配置 [netdump(4)](../man4/netdump.4.md)，可以使用 dhclient-script(8) 来运行 `dumpon`。例如，要在 vtnet0 接口上自动配置 [netdump(4)](../man4/netdump.4.md)，请将以下内容添加到 **`/etc/dhclient-exit-hooks`**。

```sh
case $reason in
BOUND|REBIND|REBOOT|RENEW)
	if [ "$interface" != vtnet0 ] || [ -n "$old_ip_address" -a \
	     "$old_ip_address" = "$new_ip_address" ]; then
		break
	fi
	if [ -n "$new_routers" ]; then
		# 取列表中的第一个路由器
		gateway_flag="-g ${new_routers%% *}"
	fi
	# 配置为最高优先级的转储设备
	dumpon -i 0 -c $new_ip_address -s $server $gateway_flag vtnet0
	;;
esac
```

确保填入服务器 IP 地址，并根据需要更改接口名称。

## 参见

[gzip(1)](../man1/gzip.1.md), kgdb(1) (`ports/devel/gdb`), zstd(1), [ddb(4)](../man4/ddb.4.md), [netdump(4)](../man4/netdump.4.md), [fstab(5)](../man5/fstab.5.md), [rc.conf(5)](../man5/rc.conf.5.md), [config(8)](config.8.md), decryptcore(8), [init(8)](init.8.md), [loader(8)](loader.8.md), [rc(8)](rc.8.md), savecore(8), [sysctl(8)](sysctl.8.md), swapon(8), [panic(9)](../man9/panic.9.md)

## 历史

`dumpon` 工具出现于 FreeBSD 2.0.5。

对加密内核核心转储和 netdump 的支持添加于 FreeBSD 12.0。

## 作者

`dumpon` 手册页由 Mark Johnston <markj@FreeBSD.org>、Conrad Meyer <cem@FreeBSD.org>、Konrad Witaszczyk <def@FreeBSD.org> 以及无数其他人编写。

## 注意事项

要配置加密内核核心转储，运行的内核必须使用 `EKCD` 选项编译。

如果路由拓扑发生变化，Netdump 不会自动更新配置的 `gateway`。

压缩转储或迷你转储的大小不是 RAM 大小的固定函数。因此，当启用这些选项中的至少一个时，`dumpon` 工具无法验证 `device` 是否有足够的空间进行转储。`dumpon` 也无法验证配置的 netdumpd(8) 服务器是否有足够的空间进行转储。

`-Z` 需要使用 `ZSTDIO` 内核选项编译的内核。类似地，`-z` 需要 `GZIO` 选项。

## 缺陷

Netdump 目前仅支持 IPv4。

## 安全注意事项

当前的加密内核核心转储方案不提供完整性或身份验证。也就是说，加密内核核心转储的接收者无法知道他们是否收到了完整的核心转储，也无法验证转储的来源。

小于 1024 位的 RSA 密钥实际上可以被分解，因此是弱的。甚至 1024 位密钥也可能不足以确保多年的隐私，因此 NIST 建议至少使用 2048 位 RSA 密钥。作为安全带，`dumpon` 防止用户使用极其弱的 RSA 密钥配置加密内核转储。如果你不关心加密隐私保证，只需在不指定 `-k` `pubkey` 选项的情况下使用 `dumpon`。

此过程使用 [capsicum(4)](../man4/capsicum.4.md) 进行沙箱隔离。
