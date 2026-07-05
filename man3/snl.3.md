# snl.3

`snl_init` — 简单 Netlink 库

## 名称

`snl_init`, `snl_free`, `snl_read_message`, `snl_send`, `snl_get_seq`, `snl_allocz`, `snl_clear_lb`, `snl_parse_nlmsg`, `snl_parse_header`, `snl_parse_attrs`, `snl_parse_attrs_raw`, `snl_attr_get_flag`, `snl_attr_get_ip`, `snl_attr_get_uint16`, `snl_attr_get_uint32`, `snl_attr_get_string`, `snl_attr_get_stringn`, `snl_attr_get_nla`, `snl_field_get_uint8`, `snl_field_get_uint16`, `snl_field_get_uint32`

## 概要

```c
#include <netlink/netlink_snl.h>
```

```c
#include <netlink/netlink_snl_route.h>
```

```c
bool
snl_init(struct snl_state *ss, int netlink_family);

void
snl_free(struct snl_state *ss);

struct nlmsghdr *
snl_read_message(struct snl_state *ss);

bool
snl_send(struct snl_state *ss, void *data, int sz);

uint32_t
snl_get_seq(struct snl_state *ss);

void *
snl_allocz(struct snl_state *ss, int len);

void
snl_clear_lb(struct snl_state *ss);

bool
snl_parse_nlmsg(struct snl_state *ss, struct nlmsghdr *hdr,
    const struct snl_hdr_parser *ps, void *target);

bool
snl_parse_header(struct snl_state *ss, void *hdr, int len,
    const struct snl_hdr_parser *ps, int pslen, void *target);

bool
snl_parse_attrs(struct snl_state *ss, struct nlmsghdr *hdr,
    int hdrlen, const struct snl_attr_parser *ps, int pslen,
    void *target);

bool
snl_parse_attrs_raw(struct snl_state *ss, struct nlattr *nla_head,
    int len, const struct snl_attr_parser *ps, int pslen,
    void *target);

bool
snl_attr_get_flag(struct snl_state *ss, struct nlattr *nla,
    void *target);

bool
snl_attr_get_uint8(struct snl_state *ss, struct nlattr *nla,
    void *target);

bool
snl_attr_get_uint16(struct snl_state *ss, struct nlattr *nla,
    void *target);

bool
snl_attr_get_uint32(struct snl_state *ss, struct nlattr *nla,
    void *target);

bool
snl_attr_get_uint64(struct snl_state *ss, struct nlattr *nla,
    void *target);

bool
snl_attr_get_string(struct snl_state *ss, struct nlattr *nla,
    void *target);

bool
snl_attr_get_stringn(struct snl_state *ss, struct nlattr *nla,
    void *target);

bool
snl_attr_get_nla(struct snl_state *ss, struct nlattr *nla,
    void *target);

bool
snl_attr_get_ip(struct snl_state *ss, struct nlattr *nla,
    void *target);

bool
snl_attr_get_ipvia(struct snl_state *ss, struct nlattr *nla,
    void *target);
```

## 描述

[snl(3)](snl.3.md) 库提供了一种简单的方式来发送和接收 Netlink 消息，负责处理序列化和反序列化。

### 初始化

调用 `snl_init()` 时传入指向 `struct snl_state` 的指针和所需的 Netlink 协议族以初始化库实例。要释放库实例，调用 `snl_free()`。

该库函数不是多线程安全的。如果需要多线程，考虑为每个线程初始化一个实例。

### 内存分配

该库使用预分配的可扩展内存缓冲区来处理消息解析。典型的使用模式是在消息解析或写入过程中通过 `snl_allocz()` 分配必要的数据结构，并在处理完消息后使用 `snl_clear_lb()` 一次性释放所有已分配的数据。

### 组合和发送消息

该库目前不提供任何用于写入 netlink 消息的包装器。简单请求消息可以通过直接填充所有需要的字段来组合。构造接口转储请求的示例：

```c
	struct {
		struct nlmsghdr hdr;
		struct ifinfomsg ifmsg;
	} msg = {
		.hdr.nlmsg_type = RTM_GETLINK,
		.hdr.nlmsg_flags = NLM_F_DUMP | NLM_F_REQUEST,
		.hdr.nlmsg_seq = snl_get_seq(ss),
	};
	msg.hdr.nlmsg_len = sizeof(msg);
```

可以使用 `snl_get_seq()` 生成唯一的消息编号。要发送生成的消息，可以使用 `snl_send()`。

### 接收和解析消息

要接收消息，使用 `snl_read_message()`。目前，此调用是阻塞的。

该库提供了一种简单的方式将消息转换为预定义的 C 结构。对于每种消息类型，需要定义规则，将协议头字段和所需属性转换到指定结构。这可以通过使用消息解析器来完成。每个消息解析器由一个属性获取器数组和一个头字段获取器数组组成。前一个数组需要按属性类型排序。有一个 `SNL_VERIFY_PARSERS` 宏可用于检查顺序是否正确。可以使用 `SNL_DECLARE_PARSER(parser_name, family, header_type, struct snl_field_parser[], struct snl_attr_parser[])` 创建新解析器。可以使用 `SNL_DECLARE_ATTR_PARSER(parser_name, struct snl_field_parser[])` 创建仅属性的消息解析器。

每个属性获取器需要嵌入以下结构中：

```c
typedef bool snl_parse_attr_f(struct snl_state *ss, struct nlattr *attr, const void *arg, void *target);
struct snl_attr_parser {
	uint16_t		type;	/* 属性类型 */
	uint16_t		off;	/* 目标结构中的字段偏移量 */
	snl_parse_attr_f	*cb;	/* 要调用的获取器函数 */
	const void		*arg;	/* 获取器函数的自定义参数 */
};
```

通用属性获取器具有以下签名：`bool snl_attr_get_<type>(struct snl_state *ss, struct nlattr *nla, const void *arg, void *target)`。`nla` 包含要用作数据源的属性指针。`target` 字段是指向目标结构中字段的指针。获取器需要知道目标字段的类型。获取器必须检查输入属性，如果属性格式不正确则返回 false。否则，获取器获取属性值并将其存储在目标中，然后返回 true。可以使用 `snl_allocz()` 创建所需的数据结构。对于常见数据类型存在若干预定义获取器。`snl_attr_get_flag()` 将标志类型属性转换为 uint8_t 值 1 或 0，取决于属性是否存在。`snl_attr_get_uint8()` 将 uint8_t 类型属性存储到 uint8_t 目标字段中。`snl_attr_get_uint16()` 将 uint16_t 类型属性存储到 uint16_t 目标字段中。`snl_attr_get_uint32()` 将 uint32_t 类型属性存储到 uint32_t 目标字段中。`snl_attr_get_uint64()` 将 uint64_t 类型属性存储到 uint64_t 目标字段中。`snl_attr_get_ip()` 和 `snl_attr_get_ipvia()` 存储指向 sockaddr 结构的指针，该结构包含属性中的 IPv4/IPv6 地址。sockaddr 使用 `snl_allocz()` 分配。`snl_attr_get_string()` 存储指向以 NULL 结尾的字符串的指针。字符串本身使用 `snl_allocz()` 分配。`snl_attr_get_nla()` 存储指向指定属性的指针。`snl_attr_get_stringn()` 存储指向非 NULL 结尾字符串的指针。

类似地，每个协议族头获取器需要嵌入以下结构中：

```c
typedef void snl_parse_field_f(struct snl_state *ss, void *hdr, void *target);
struct snl_field_parser {
	uint16_t		off_in;	/* 输入结构中的字段偏移量 */
	uint16_t                off_out;/* 目标结构中的字段偏移量 */
	snl_parse_field_f       *cb;	/* 要调用的获取器函数 */
};
```

通用字段获取器具有以下签名：`void snl_field_get_<type>(struct snl_state *ss, void *src, void *target)`。对于常见数据类型存在若干预定义获取器。`snl_field_get_uint8()` 获取 uint8_t 值并将其存储在目标中。`snl_field_get_uint16()` 获取 uint16_t 值并将其存储在目标中。`snl_field_get_uint32()` 获取 uint32_t 值并将其存储在目标中。

## 实例

以下示例演示如何使用 netlink 列出所有系统接口。

```c
#include <stdio.h>
#include <netlink/netlink.h>
#include <netlink/netlink_route.h>
#include "netlink/netlink_snl.h"
#include "netlink/netlink_snl_route.h"
struct nl_parsed_link {
	uint32_t		ifi_index;
	uint32_t		ifla_mtu;
	char			*ifla_ifname;
};
#define	_IN(_field)	offsetof(struct ifinfomsg, _field)
#define	_OUT(_field)	offsetof(struct nl_parsed_link, _field)
static const struct snl_attr_parser ap_link[] = {
	{ .type = IFLA_IFNAME, .off = _OUT(ifla_ifname), .cb = snl_attr_get_string },
	{ .type = IFLA_MTU, .off = _OUT(ifla_mtu), .cb = snl_attr_get_uint32 },
};
static const struct snl_field_parser fp_link[] = {
	{.off_in = _IN(ifi_index), .off_out = _OUT(ifi_index), .cb = snl_field_get_uint32 },
};
#undef _IN
#undef _OUT
SNL_DECLARE_PARSER(link_parser, struct ifinfomsg, fp_link, ap_link);
int
main(int ac, char *argv[])
{
	struct snl_state ss;
	if (!snl_init(&ss, NETLINK_ROUTE))
		return (1);
	struct {
		struct nlmsghdr hdr;
		struct ifinfomsg ifmsg;
	} msg = {
		.hdr.nlmsg_type = RTM_GETLINK,
		.hdr.nlmsg_flags = NLM_F_DUMP | NLM_F_REQUEST,
		.hdr.nlmsg_seq = snl_get_seq(&ss),
	};
	msg.hdr.nlmsg_len = sizeof(msg);
	if (!snl_send(&ss, &msg, sizeof(msg))) {
		snl_free(&ss);
		return (1);
	}
	struct nlmsghdr *hdr;
	while ((hdr = snl_read_message(&ss)) != NULL && hdr->nlmsg_type != NLMSG_DONE) {
		if (hdr->nlmsg_seq != msg.hdr.nlmsg_seq)
			break;
		struct nl_parsed_link link = {};
		if (!snl_parse_nlmsg(&ss, hdr, &link_parser, &link))
			continue;
		printf("Link#%u %s mtu %u\n", link.ifi_index, link.ifla_ifname, link.ifla_mtu);
	}
	return (0);
}
```

## 参见

[genetlink(4)](../man4/genetlink.4.md), [netlink(4)](../man4/netlink.4.md), [rtnetlink(4)](../man4/rtnetlink.4.md)

## 历史

`SNL` 库出现于 FreeBSD 13.2。

## 作者

本库由 Alexander Chernikov <melifaro@FreeBSD.org> 实现。
