# pflog.4

`pflog` — 包过滤器日志 BPF 抽头

## 名称

`pflog`

## 概要

`device pflog`

## 描述

`pflog` 是一个 BPF 抽头，使包过滤器 [pf(4)](pf.4.md) 记录的所有包可见。通过对 `pflog` BPF 抽头调用 [tcpdump(1)](../man1/tcpdump.1.md) 可轻松实时监视记录的包，或使用 pflogd(8) 存储到磁盘。

加载 `pflog` 模块时创建 pflog0 BPF 抽头；可使用 [ifconfig(8)](../man8/ifconfig.8.md) 创建更多实例。如果同时启用了 [pf(4)](pf.4.md) 和 pflogd(8)，则 `pflog` 模块会自动加载。

在此 BPF 抽头上检索到的每个包都关联有一个长度为 `PFLOG_HDRLEN` 的头。此头记录了被记录包的地址族、接口名、规则号、原因、操作和方向。此结构定义于 <`net/if_pflog.h`>，如下所示

```sh
struct pfloghdr {
	u_int8_t	length;
	sa_family_t	af;
	u_int8_t	action;
	u_int8_t	reason;
	char		ifname[IFNAMSIZ];
	char		ruleset[PF_RULESET_NAME_SIZE];
	u_int32_t	rulenr;
	u_int32_t	subrulenr;
	uid_t		uid;
	pid_t		pid;
	uid_t		rule_uid;
	pid_t		rule_pid;
	u_int8_t	dir;
	u_int8_t	pad[3];
	u_int32_t	ridentifier;
};
```

pflog 设备数可通过 `net.pflog.if_count` sysctl 配置。

## 实例

监视 pflog0 上记录的所有包：

```sh
# tcpdump -n -e -ttt -i pflog0
```

## 参见

[tcpdump(1)](../man1/tcpdump.1.md), [inet(4)](inet.4.md), [inet6(4)](inet6.4.md), [netintro(4)](netintro.4.md), [pf(4)](pf.4.md), [ifconfig(8)](../man8/ifconfig.8.md), pflogd(8)

## 历史

`pflog` 设备首次出现于 OpenBSD 3.0。

## 缺陷

FreeBSD 不会在 pfloghdr 的 `pid` 字段中设置进程 ID。
