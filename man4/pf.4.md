# pf.4

`pf` — 包过滤器

## 名称

`pf`

## 概要

`device pf options PF_DEFAULT_TO_DROP`

`在 rc.conf(5) 中：pf_enable="YES"`

`在 loader.conf(5) 中：net.pf.states_hashsize net.pf.source_nodes_hashsize net.pf.rule_tag_hashsize net.pf.udpendpoint_hashsize net.pf.default_to_drop`

`在 sysctl.conf(5) 中：net.pf.request_maxcount net.pf.filter_local`

## 描述

包过滤在内核中进行。伪设备 `/dev/pf` 允许用户态进程通过 ioctl(2) 接口控制包过滤器的行为。有启用和禁用过滤器、加载规则集、添加和删除单个规则或状态表条目以及检索统计信息的命令。最常用的功能由 pfctl(8) 涵盖。

诸如加载规则集之类涉及多个 ioctl(2) 调用的操作需要所谓的 *ticket,* 以防止出现多个并发操作。

ioctl(2) 参数结构中引用包数据（如地址和端口）的字段通常应使用网络字节序。

规则和地址表包含在所谓的 *锚点（anchor）* 中。在服务 ioctl(2) 请求时，如果参数结构的锚点字段为空，内核将在操作中使用默认锚点（即主规则集）。锚点按名称指定，可嵌套，组件之间以‘/’字符分隔，类似于文件系统层次的布局。锚点路径的最后一个组件是将在其下执行操作的锚点。

## SYSCTL 变量

以下变量可在 [loader(8)](../man8/loader.8.md) 提示符处输入、在 loader.conf(5) 中设置、在 [sysctl.conf(5)](../man5/sysctl.conf.5.md) 中设置，或在运行时使用 [sysctl(8)](../man8/sysctl.8.md) 更改：

**`net.pf.filter_local`** 通知 `pf` 也对环回输出钩子进行过滤。这通常用于允许重定向规则调整源地址。

**`net.pf.request_maxcount`** 单次 ioctl 调用中的最大项数。

## 加载器可调参数

以下可调参数可在 [loader(8)](../man8/loader.8.md) 提示符处输入，或在 loader.conf(5) 中设置：

**`net.pf.states_hashsize`** 存储状态的哈希表大小。应为 2 的幂。默认值为 131072。

**`net.pf.source_nodes_hashsize`** 存储源节点的哈希表大小。应为 2 的幂。默认值为 32768。

**`net.pf.rule_tag_hashsize`** 存储标签的哈希表大小。

**`net.pf.udpendpoint_hashsize`** 存储 UDP 端点映射的哈希表大小。应为 2 的幂。默认值为 32768。

**`net.pf.default_to_drop`** 此值覆盖内核配置文件中的 `options PF_DEFAULT_TO_DROP`。

**`net.pf.filter_local`** 通知 `pf` 也对环回输出钩子进行过滤。这通常用于允许重定向规则调整源地址。

**`net.pf.request_maxcount`** 单次 ioctl 调用中的最大项数。

提供具有匹配名称的只读 [sysctl(8)](../man8/sysctl.8.md) 变量以在运行时获取当前值。

## 内核选项

内核配置文件中与 `pf` 操作相关的以下选项：

**`PF_DEFAULT_TO_DROP`** 将默认策略更改为默认丢弃

## IOCTL 接口

`pf` 支持以下 ioctl(2) 命令，可通过 <`net/pfvar.h`> 获得：

```sh
struct pfioc_pooladdr {
	u_int32_t		action;
	u_int32_t		ticket;
	u_int32_t		nr;
	u_int32_t		r_num;
	u_int8_t		r_action;
	u_int8_t		r_last;
	u_int8_t		af;
	char			anchor[MAXPATHLEN];
	struct pf_pooladdr	addr;
};
```

```sh
struct pfioc_rule {
	u_int32_t	action;
	u_int32_t	ticket;
	u_int32_t	pool_ticket;
	u_int32_t	nr;
	char		anchor[MAXPATHLEN];
	char		anchor_call[MAXPATHLEN];
	struct pf_rule	rule;
};
```

```sh
struct pfioc_altq {
	u_int32_t	action;
	u_int32_t	ticket;
	u_int32_t	nr;
	struct pf_altq  altq;
};
```

```sh
struct pfioc_qstats {
	u_int32_t	 ticket;
	u_int32_t	 nr;
	void		*buf;
	int		 nbytes;
	u_int8_t	 scheduler;
};
```

```sh
struct pfioc_ruleset {
	u_int32_t	 nr;
	char		 path[MAXPATHLEN];
	char		 name[PF_ANCHOR_NAME_SIZE];
};
```

```sh
struct pfioc_state {
	struct pfsync_state	state;
};
```

```sh
nvlist pf_state_cmp {
	number			id;
	number			creatorid;
	number			direction;
};
nvlist pf_kill {
	nvlist pf_state_cmp	cmp;
	number			af;
	number			proto;
	nvlist pf_rule_addr	src;
	nvlist pf_rule_addr	dst;
	string			ifname[IFNAMSIZ];
	string			label[PF_RULE_LABEL_SIZE];
};
```

```sh
struct pfioc_if {
	char		 ifname[IFNAMSIZ];
};
```

```sh
struct pf_status {
	u_int64_t	counters[PFRES_MAX];
	u_int64_t	lcounters[LCNT_MAX];
	u_int64_t	fcounters[FCNT_MAX];
	u_int64_t	scounters[SCNT_MAX];
	u_int64_t	pcounters[2][2][3];
	u_int64_t	bcounters[2][2];
	u_int32_t	running;
	u_int32_t	states;
	u_int32_t	src_nodes;
	u_int32_t	since;
	u_int32_t	debug;
	u_int32_t	hostid;
	char		ifname[IFNAMSIZ];
	u_int8_t	pf_chksum[MD5_DIGEST_LENGTH];
};
```

```sh
struct pfioc_natlook {
	struct pf_addr	 saddr;
	struct pf_addr	 daddr;
	struct pf_addr	 rsaddr;
	struct pf_addr	 rdaddr;
	u_int16_t	 sport;
	u_int16_t	 dport;
	u_int16_t	 rsport;
	u_int16_t	 rdport;
	sa_family_t	 af;
	u_int8_t	 proto;
	u_int8_t	 direction;
};
```

```sh
enum	{ PF_DEBUG_NONE, PF_DEBUG_URGENT, PF_DEBUG_MISC,
	  PF_DEBUG_NOISY };
```

```sh
struct pfioc_states_v2 {
	int		ps_len;
	uint64_t	ps_req_version;
	union {
		void			*ps_buf;
		struct pf_state_export	*ps_states;
	};
};
struct pf_state_export {
	uint64_t	 version;
	uint64_t	 id;
	char		 ifname[IFNAMSIZ];
	char		 orig_ifname[IFNAMSIZ];
	struct pf_state_key_export	 key[2];
	struct pf_state_peer_export	 src;
	struct pf_state_peer_export	 dst;
	struct pf_addr	 rt_addr;
	uint32_t	 rule;
	uint32_t	 anchor;
	uint32_t	 nat_rule;
	uint32_t	 creation;
	uint32_t	 expire;
	uint32_t	 spare0;
	uint64_t	 packets[2];
	uint64_t	 bytes[2];
	uint32_t	 creatorid;
	uint32_t	 spare1;
	sa_family_t	 af;
	uint8_t		 proto;
	uint8_t		 direction;
	uint8_t		 log;
	uint8_t		 state_flags_compat;
	uint8_t		 timeout;
	uint8_t		 sync_flags;
	uint8_t		 updates;
	uint16_t	 state_flags;
	uint16_t	 qid;
	uint16_t	 pqid;
	uint16_t	 dnpipe;
	uint16_t	 dnrpipe;
	int32_t		 rtableid;
	uint8_t		 min_ttl;
	uint8_t		 set_tos;
	uint16_t	 max_mss;
	uint8_t		 set_prio[2];
	uint8_t		 rt;
	char		 rt_ifname[IFNAMSIZ];
	uint8_t		 spare[72];
};
```

```sh
enum	{ PF_CHANGE_NONE, PF_CHANGE_ADD_HEAD, PF_CHANGE_ADD_TAIL,
	  PF_CHANGE_ADD_BEFORE, PF_CHANGE_ADD_AFTER,
	  PF_CHANGE_REMOVE, PF_CHANGE_GET_TICKET };
```

```sh
struct pfioc_tm {
	int		 timeout;
	int		 seconds;
};
```

```sh
struct pfioc_limit {
	int		index;
	unsigned	limit;
};
enum	{ PF_LIMIT_STATES, PF_LIMIT_SRC_NODES, PF_LIMIT_FRAGS,
	  PF_LIMIT_TABLE_ENTRIES, PF_LIMIT_MAX };
```

```sh
struct pfioc_table {
	struct pfr_table	 pfrio_table;
	void			*pfrio_buffer;
	int			 pfrio_esize;
	int			 pfrio_size;
	int			 pfrio_size2;
	int			 pfrio_nadd;
	int			 pfrio_ndel;
	int			 pfrio_nchange;
	int			 pfrio_flags;
	u_int32_t		 pfrio_ticket;
};
#define pfrio_exists    pfrio_nadd
#define pfrio_nzero     pfrio_nadd
#define pfrio_nmatch    pfrio_nadd
#define pfrio_naddr     pfrio_size2
#define pfrio_setflag   pfrio_size2
#define pfrio_clrflag   pfrio_nadd
```

```sh
struct pfr_table {
	char		pfrt_anchor[MAXPATHLEN];
	char		pfrt_name[PF_TABLE_NAME_SIZE];
	u_int32_t	pfrt_flags;
	u_int8_t	pfrt_fback;
};
```

```sh
struct pfr_tstats {
	struct pfr_table pfrts_t;
	u_int64_t	 pfrts_packets
			     [PFR_DIR_MAX][PFR_OP_TABLE_MAX];
	u_int64_t	 pfrts_bytes
			     [PFR_DIR_MAX][PFR_OP_TABLE_MAX];
	u_int64_t	 pfrts_match;
	u_int64_t	 pfrts_nomatch;
	time_t		 pfrts_tzero;
	int		 pfrts_cnt;
	int		 pfrts_refcnt[PFR_REFCNT_MAX];
};
#define pfrts_name	 pfrts_t.pfrt_name
#define pfrts_flags	 pfrts_t.pfrt_flags
```

```sh
struct pfr_addr {
	union {
		struct in_addr	 _pfra_ip4addr;
		struct in6_addr	 _pfra_ip6addr;
	}		 pfra_u;
	u_int8_t	 pfra_af;
	u_int8_t	 pfra_net;
	u_int8_t	 pfra_not;
	u_int8_t	 pfra_fback;
};
#define pfra_ip4addr    pfra_u._pfra_ip4addr
#define pfra_ip6addr    pfra_u._pfra_ip6addr
```

```sh
struct pfr_astats {
	struct pfr_addr	 pfras_a;
	u_int64_t	 pfras_packets
			     [PFR_DIR_MAX][PFR_OP_ADDR_MAX];
	u_int64_t	 pfras_bytes
			     [PFR_DIR_MAX][PFR_OP_ADDR_MAX];
	time_t		 pfras_tzero;
};
```

```sh
struct pfioc_trans {
	int		 size;	/* 元素数量 */
	int		 esize;	/* 每个元素的字节大小 */
	struct pfioc_trans_e {
		int		rs_num;
		char		anchor[MAXPATHLEN];
		u_int32_t	ticket;
	}		*array;
};
```

**`PF_RULESET_SCRUB`** Scrub（包规范化）规则。
**`PF_RULESET_FILTER`** 过滤规则。
**`PF_RULESET_NAT`** NAT（网络地址转换）规则。
**`PF_RULESET_BINAT`** 双向 NAT 规则。
**`PF_RULESET_RDR`** 重定向规则。
**`PF_RULESET_ALTQ`** ALTQ 调度规则。
**`PF_RULESET_TABLE`** 地址表。

```sh
struct pf_osfp_ioctl {
	struct pf_osfp_entry {
		SLIST_ENTRY(pf_osfp_entry) fp_entry;
		pf_osfp_t		fp_os;
		char			fp_class_nm[PF_OSFP_LEN];
		char			fp_version_nm[PF_OSFP_LEN];
		char			fp_subtype_nm[PF_OSFP_LEN];
	} 			fp_os;
	pf_tcpopts_t		fp_tcpopts;
	u_int16_t		fp_wsize;
	u_int16_t		fp_psize;
	u_int16_t		fp_mss;
	u_int16_t		fp_flags;
	u_int8_t		fp_optcnt;
	u_int8_t		fp_wscale;
	u_int8_t		fp_ttl;
	int			fp_getnum;
};
```

```sh
struct pfioc_src_nodes {
	int	psn_len;
	union {
		caddr_t		psu_buf;
		struct pf_src_node	*psu_src_nodes;
	} psn_u;
#define psn_buf		psn_u.psu_buf
#define psn_src_nodes	psn_u.psu_src_nodes
};
```

```sh
struct pfioc_iface {
	char			 pfiio_name[IFNAMSIZ];
	void			*pfiio_buffer;
	int			 pfiio_esize;
	int			 pfiio_size;
	int			 pfiio_nzero;
	int			 pfiio_flags;
};
```

```sh
struct pfi_kif {
	char				 pfik_name[IFNAMSIZ];
	union {
		RB_ENTRY(pfi_kif)	 pfik_tree;
		LIST_ENTRY(pfi_kif)	 pfik_list;
	};
	u_int64_t			 pfik_packets[2][2][2];
	u_int64_t			 pfik_bytes[2][2][2];
	u_int32_t			 pfik_tzero;
	u_int				 pfik_flags;
	struct ifnet			*pfik_ifp;
	struct ifg_group		*pfik_group;
	u_int				 pfik_rulerefs;
	TAILQ_HEAD(, pfi_dynaddr)	 pfik_dynaddrs;
};
```

```sh
#define PFI_IFLAG_SKIP	0x0100	/* 在接口上跳过过滤 */
```

**`DIOCSTART`** 启动包过滤器。

**`DIOCSTOP`** 停止包过滤器。

**`DIOCSTARTALTQ`** 启动 ALTQ 带宽控制系统（参见 [altq(9)](../man9/altq.9.md)）。

**`DIOCSTOPALTQ`** 停止 ALTQ 带宽控制系统。

**`DIOCBEGINADDRS`** `struct pfioc_pooladdr *pp` 清除缓冲地址池，并为后续的 `DIOCADDADDR`、`DIOCADDRULE` 和 `DIOCCHANGERULE` 调用获取 `ticket`。

**`DIOCADDADDR`** `struct pfioc_pooladdr *pp` 将池地址 `addr` 添加到缓冲地址池，用于随后的 `DIOCADDRULE` 或 `DIOCCHANGERULE` 调用。结构中的所有其他成员都被忽略。

**`DIOCADDRULE`** `struct pfioc_rule *pr` 在非活动规则集的末尾添加 `rule`。此调用需要通过前一次 `DIOCXBEGIN` 调用获得的 `ticket`，以及通过前一次 `DIOCBEGINADDRS` 调用获得的 `pool_ticket`。如果需要任何池地址，还必须调用 `DIOCADDADDR`。可选的 `anchor` 名称指示要将规则附加到的锚点。`nr` 和 `action` 被忽略。

**`DIOCADDALTQ`** `struct pfioc_altq *pa` 添加一个 ALTQ 调度规则或队列。

**`DIOCGETRULES`** `struct pfioc_rule *pr` 为后续的 `DIOCGETRULE` 调用获取 `ticket` 和活动规则集中的规则数 `nr`。

**`DIOCGETRULE`** `struct pfioc_rule *pr` 使用通过前一次 `DIOCGETRULES` 调用获得的 `ticket` 按其编号 `nr` 获取 `rule`。如果 `action` 设为 `PF_GET_CLR_CNTR`，则清除所请求规则的按规则统计信息。

**`DIOCGETADDRS`** `struct pfioc_pooladdr *pp` 为后续的 `DIOCGETADDR` 调用获取 `ticket` 以及由 `r_action`、`r_num` 和 `anchor` 指定的规则中的池地址数 `nr`。

**`DIOCGETADDR`** `struct pfioc_pooladdr *pp` 使用通过前一次 `DIOCGETADDRS` 调用获得的 `ticket` 按其编号 `nr` 从由 `r_action`、`r_num` 和 `anchor` 指定的规则中获取池地址 `addr`。

**`DIOCGETALTQS`** `struct pfioc_altq *pa` 为后续的 `DIOCGETALTQ` 调用获取 `ticket` 和活动列表中的队列数 `nr`。

**`DIOCGETALTQ`** `struct pfioc_altq *pa` 使用通过前一次 `DIOCGETALTQS` 调用获得的 `ticket` 按其编号 `nr` 获取队列调度规则 `altq`。

**`DIOCGETQSTATS`** `struct pfioc_qstats *pq` 获取队列的统计信息。此调用填充指向长度为 `nbytes` 的统计信息缓冲区 `buf` 的指针，用于由 `nr` 指定的队列。

**`DIOCGETRULESETS`** `struct pfioc_ruleset *pr` 获取直接附加到 `path` 命名锚点的规则集（即锚点）数 `nr`，用于后续的 `DIOCGETRULESET` 调用。嵌套锚点（由于不直接附加到给定锚点）将不被包括在内。如果 `path` 处给定的父锚点不存在，此 ioctl 返回 Er ENOENT。

**`DIOCGETRULESET`** `struct pfioc_ruleset *pr` 从给定锚点 `path` 按编号 `nr` 获取规则集（即锚点）`name`，其最大数量可从前一次 `DIOCGETRULESETS` 调用获得。如果 `path` 处给定的父锚点不存在，此 ioctl 返回 Er ENOENT；如果 `nr` 传入的索引大于锚点数，返回 Er EBUSY。

**`DIOCADDSTATE`** `struct pfioc_state *ps` 添加状态条目。

**`DIOCGETSTATENV`** `struct pfioc_nv *nv` 从状态表中提取由 `state` nvlist 的 `id` 和 `creatorid` 字段标识的条目。

**`DIOCKILLSTATESNV`** `struct pfioc_nv nv` 从状态表中删除匹配的条目。此 ioctl 在 `killed` 中返回被杀掉的状态数。

**`DIOCCLRSTATESNV`** `struct pfioc_nv nv` 清除所有状态。其工作方式类似于 `DIOCKILLSTATESNV`，但忽略 `pf_kill` nvlist 的 `af`、`proto`、`src` 和 `dst` 字段。

**`DIOCSETSTATUSIF`** `struct pfioc_if *pi` 指定用于累计统计信息的接口。

**`DIOCGETSTATUS`** `struct pf_status *s` 获取内部包过滤器统计信息。

**`DIOCCLRSTATUS`** 清除内部包过滤器统计信息。

**`DIOCNATLOOK`** `struct pfioc_natlook *pnl` 按源和目的地址及端口查找状态表条目。

**`DIOCSETDEBUG`** `u_int32_t *level` 设置调试级别。

**`DIOCGETSTATESV2`** `struct pfioc_states_v2 *ps` 获取状态表条目。

**`DIOCCHANGERULE`** `struct pfioc_rule *pcr` 在由 `rule.action` 指定的规则集中添加或删除 `rule`。要执行的操作类型由 `action` 指示，可为以下任意一种：对于除 `PF_CHANGE_GET_TICKET` 之外的所有操作，`ticket` 必须设为通过 `PF_CHANGE_GET_TICKET` 获得的值。对于除 `PF_CHANGE_REMOVE` 和 `PF_CHANGE_GET_TICKET` 之外的所有操作，`pool_ticket` 必须设为通过 `DIOCBEGINADDRS` 调用获得的值。`anchor` 指示操作应用到的锚点。`nr` 指示应用 `PF_CHANGE_ADD_BEFORE`、`PF_CHANGE_ADD_AFTER` 或 `PF_CHANGE_REMOVE` 操作所针对的规则编号。

**`DIOCCHANGEADDR`** `struct pfioc_pooladdr *pca` 从由 `r_action`、`r_num` 和 `anchor` 指定的规则中添加或删除池地址 `addr`。

**`DIOCSETTIMEOUT`** `struct pfioc_tm *pt` 将 `timeout` 的状态超时设为 `seconds`。旧值将被放入 `seconds`。`timeout` 的可能值请参见 <`net/pfvar.h`> 中的 `PFTM_*` 值。

**`DIOCGETTIMEOUT`** `struct pfioc_tm *pt` 获取 `timeout` 的状态超时。该值将被放入 `seconds` 字段。

**`DIOCCLRRULECTRS`** 清除按规则统计信息。

**`DIOCSETLIMIT`** `struct pfioc_limit *pl` 设置包过滤器使用的内存池的硬限制。

**`DIOCGETLIMIT`** `struct pfioc_limit *pl` 获取由 `index` 指示的内存池的硬 `limit`。

**`DIOCRCLRTABLES`** `struct pfioc_table *io` 清除所有表。所有操作 radix 表的 ioctl 都使用下文所述的同一结构。对于 `DIOCRCLRTABLES`，退出时 `pfrio_ndel` 包含已删除的表数。

**`DIOCRADDTABLES`** `struct pfioc_table *io` 创建一个或多个表。在进入时，`pfrio_buffer` 必须指向一个 `struct pfr_table` 数组，其中至少包含 `pfrio_size` 个元素。`pfrio_esize` 必须为 `struct pfr_table` 的大小。退出时，`pfrio_nadd` 包含实际创建的表数。

**`DIOCRDELTABLES`** `struct pfioc_table *io` 删除一个或多个表。在进入时，`pfrio_buffer` 必须指向一个 `struct pfr_table` 数组，其中至少包含 `pfrio_size` 个元素。`pfrio_esize` 必须为 `struct pfr_table` 的大小。退出时，`pfrio_ndel` 包含实际删除的表数。

**`DIOCRGETTABLES`** `struct pfioc_table *io` 获取所有表的列表。在进入时，`pfrio_buffer[pfrio_size]` 包含一个有效的可写缓冲区用于 `pfr_table` 结构。退出时，`pfrio_size` 包含写入缓冲区的表数。如果缓冲区太小，内核不存储任何内容，仅返回所需的缓冲区大小，不返回错误。

**`DIOCRGETTSTATS`** `struct pfioc_table *io` 此调用类似于 `DIOCRGETTABLES`，但用于获取 `pfr_tstats` 结构的数组。

**`DIOCRCLRTSTATS`** `struct pfioc_table *io` 清除一个或多个表的统计信息。在进入时，`pfrio_buffer` 必须指向一个 `struct pfr_table` 数组，其中至少包含 `pfrio_size` 个元素。`pfrio_esize` 必须为 `struct pfr_table` 的大小。退出时，`pfrio_nzero` 包含实际清除的表数。

**`DIOCRCLRADDRS`** `struct pfioc_table *io` 清除表中的所有地址。在进入时，`pfrio_table` 包含要清除的表。退出时，`pfrio_ndel` 包含已删除的地址数。

**`DIOCRADDADDRS`** `struct pfioc_table *io` 向表中添加一个或多个地址。在进入时，`pfrio_table` 包含表 ID，`pfrio_buffer` 必须指向一个 `struct pfr_addr` 数组，其中至少包含 `pfrio_size` 个要添加到表中的元素。`pfrio_esize` 必须为 `struct pfr_addr` 的大小。退出时，`pfrio_nadd` 包含实际添加的地址数。

**`DIOCRDELADDRS`** `struct pfioc_table *io` 从表中删除一个或多个地址。在进入时，`pfrio_table` 包含表 ID，`pfrio_buffer` 必须指向一个 `struct pfr_addr` 数组，其中至少包含 `pfrio_size` 个要从表中删除的元素。`pfrio_esize` 必须为 `struct pfr_addr` 的大小。退出时，`pfrio_ndel` 包含实际删除的地址数。

**`DIOCRSETADDRS`** `struct pfioc_table *io` 用新的地址列表替换表的内容。这是最复杂的命令，使用了所有结构成员。在进入时，`pfrio_table` 包含表 ID，`pfrio_buffer` 必须指向一个 `struct pfr_addr` 数组，其中至少包含 `pfrio_size` 个元素，这些元素成为表的新内容。`pfrio_esize` 必须为 `struct pfr_addr` 的大小。此外，如果 `pfrio_size2` 不为零，`pfrio_buffer[pfrio_size..pfrio_size2]` 必须是可写缓冲区，内核可以将替换操作期间已删除的地址复制到其中。退出时，`pfrio_ndel`、`pfrio_nadd` 和 `pfrio_nchange` 包含内核删除、添加和更改的地址数。如果进入时设置了 `pfrio_size2`，`pfrio_size2` 将指向所用缓冲区的大小，与 `DIOCRGETADDRS` 完全相同。

**`DIOCRGETADDRS`** `struct pfioc_table *io` 获取表的所有地址。在进入时，`pfrio_table` 包含表 ID，`pfrio_buffer[pfrio_size]` 包含一个有效的可写缓冲区用于 `pfr_addr` 结构。退出时，`pfrio_size` 包含写入缓冲区的地址数。如果缓冲区太小，内核不存储任何内容，仅返回所需的缓冲区大小，不返回错误。

**`DIOCRGETASTATS`** `struct pfioc_table *io` 此调用类似于 `DIOCRGETADDRS`，但用于获取 `pfr_astats` 结构的数组。

**`DIOCRCLRASTATS`** `struct pfioc_table *io` 清除一个或多个地址的统计信息。在进入时，`pfrio_table` 包含表 ID，`pfrio_buffer` 必须指向一个 `struct pfr_addr` 数组，其中至少包含 `pfrio_size` 个要从表中清除的元素。`pfrio_esize` 必须为 `struct pfr_addr` 的大小。退出时，`pfrio_nzero` 包含实际清除的地址数。

**`DIOCRTSTADDRS`** `struct pfioc_table *io` 测试给定地址是否与表匹配。在进入时，`pfrio_table` 包含表 ID，`pfrio_buffer` 必须指向一个 `struct pfr_addr` 数组，其中至少包含 `pfrio_size` 个元素，每个元素都将在表中测试是否匹配。`pfrio_esize` 必须为 `struct pfr_addr` 的大小。退出时，内核通过适当设置 `pfra_fback` 成员来更新 `pfr_addr` 数组。

**`DIOCRSETTFLAGS`** `struct pfioc_table *io` 更改表的 `PFR_TFLAG_CONST` 或 `PFR_TFLAG_PERSIST` 标志。在进入时，`pfrio_buffer` 必须指向一个 `struct pfr_table` 数组，其中至少包含 `pfrio_size` 个元素。`pfrio_esize` 必须为 `struct pfr_table` 的大小。`pfrio_setflag` 必须包含要添加的标志，而 `pfrio_clrflag` 必须包含要删除的标志。退出时，`pfrio_nchange` 和 `pfrio_ndel` 包含内核更改或删除的表数。是的，如果删除未引用表的 `PFR_TFLAG_PERSIST` 标志，则可以删除该表。

**`DIOCRINADEFINE`** `struct pfioc_table *io` 在非活动集中定义一个表。在进入时，`pfrio_table` 包含表 ID，`pfrio_buffer[pfrio_size]` 包含要放入表中的 `pfr_addr` 结构数组。还必须向 `pfrio_ticket` 提供有效的 ticket。退出时，如果该表已在非活动列表中定义，`pfrio_nadd` 包含 0；如果已创建新表，包含 1。`pfrio_naddr` 包含实际放入表中的地址数。

**`DIOCXBEGIN`** `struct pfioc_trans *io` 清除 `pfioc_trans_e` 数组中指定的所有非活动规则集。对于每个规则集，返回一个 ticket 用于后续的“添加规则”ioctl，以及 `DIOCXCOMMIT` 和 `DIOCXROLLBACK` 调用。由 `rs_num` 标识的规则集类型包括以下几种：

**`DIOCXCOMMIT`** `struct pfioc_trans *io` 原子地将一组非活动规则集切换为活动规则集。此调用实现为标准的两阶段提交，要么所有规则集都失败，要么完全成功。所有 ticket 都必须有效。如果另一个进程正在并发更新某些相同的规则集，此 ioctl 返回 Er EBUSY。

**`DIOCXROLLBACK`** `struct pfioc_trans *io` 通过撤销自上次 `DIOCXBEGIN` 以来在非活动规则集上发生的所有更改来清理内核。`DIOCXROLLBACK` 将静默忽略 ticket 无效的规则集。

**`DIOCSETHOSTID`** `u_int32_t *hostid` 设置主机 ID，[pfsync(4)](pfsync.4.md) 使用它来标识哪个主机创建了状态表条目。

**`DIOCOSFPFLUSH`** 刷新被动 OS 指纹表。

**`DIOCOSFPADD`** `struct pf_osfp_ioctl *io` 向表中添加被动 OS 指纹。将 `fp_os.fp_os` 设为打包的指纹，`fp_os.fp_class_nm` 设为类名（Linux、Windows 等），`fp_os.fp_version_nm` 设为版本名（NT、95、98），`fp_os.fp_subtype_nm` 设为子类型或补丁级别名。成员 `fp_mss`、`fp_wsize`、`fp_psize`、`fp_ttl`、`fp_optcnt` 和 `fp_wscale` 分别设为 TCP SYN 包的 TCP MSS、TCP 窗口大小、IP 长度、IP TTL、TCP 选项数和 TCP 窗口缩放常数。`fp_flags` 成员根据 <`net/pfvar.h`> 包含文件的 `PF_OSFP_*` 定义填充。`fp_tcpopts` 成员包含打包的 TCP 选项。每个选项在打包值中使用 `PF_OSFP_TCPOPT_BITS` 位。选项包括 `PF_OSFP_TCPOPT_NOP`、`PF_OSFP_TCPOPT_SACK`、`PF_OSFP_TCPOPT_WSCALE`、`PF_OSFP_TCPOPT_MSS` 或 `PF_OSFP_TCPOPT_TS` 中的任意一个。`fp_getnum` 成员不用于此 ioctl。结构的空闲空间必须清零才能正确操作；在填充和发送到内核之前，将整个结构 memset(3) 为零。

**`DIOCOSFPGET`** `struct pf_osfp_ioctl *io` 从内核的指纹列表中获取被动 OS 指纹编号 `fp_getnum`。结构的其余成员将被填充返回。通过重复递增 `fp_getnum` 编号直到 ioctl 返回 Er EBUSY 来获取整个列表。

**`DIOCGETSRCNODES`** `struct pfioc_src_nodes *psn` 获取由粘性地址和源跟踪保留的源节点列表。必须先用 `psn_len` 设为 0 调用此 ioctl。如果 ioctl 无错误返回，`psn_len` 将被设为保存表中所有 `pf_src_node` 结构所需缓冲区的大小。然后应分配此大小的缓冲区，并将指向此缓冲区的指针放入 `psn_buf`。然后必须再次调用此 ioctl 以用实际源节点数据填充此缓冲区。该调用之后，`psn_len` 将被设为实际使用的缓冲区长度。

**`DIOCCLRSRCNODES`** 清除源跟踪节点树。

**`DIOCIGETIFACES`** `struct pfioc_iface *io` 获取 `pf` 已知的接口和接口组列表。所有操作接口的 ioctl 都使用下文所述的同一结构：如果不为空，`pfiio_name` 可用于将搜索限制为特定接口或组。`pfiio_buffer[pfiio_size]` 是用户提供的用于返回数据的缓冲区。在进入时，`pfiio_size` 包含可放入缓冲区的 `pfi_kif` 条目数。内核将用其要返回的实际条目数替换此值。`pfiio_esize` 应设为 `sizeof(struct pfi_kif)`。数据以下文所述的 `pfi_kif` 结构返回：

**`DIOCSETIFFLAG`** `struct pfioc_iface *io` 设置 `pf` 内部接口描述的用户可设置标志（如上所述）。过滤过程与 `DIOCIGETIFACES` 相同。

**`DIOCCLRIFFLAG`** `struct pfioc_iface *io` 工作方式类似于上面的 `DIOCSETIFFLAG`，但清除标志。

**`DIOCKILLSRCNODES`** `struct pfioc_iface *io` 显式删除源跟踪节点。

## 文件

**`/dev/pf`** 包过滤设备。

## 实例

以下示例演示如何使用 `DIOCNATLOOK` 命令查找 NAT 连接的内部主机/端口：

```sh
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/ioctl.h>
#include <sys/fcntl.h>
#include <net/if.h>
#include <netinet/in.h>
#include <net/pfvar.h>
#include <err.h>
#include <stdio.h>
#include <stdlib.h>
u_int32_t
read_address(const char *s)
{
	int a, b, c, d;
	sscanf(s, "%i.%i.%i.%i", &a, &b, &c, &d);
	return htonl(a << 24 | b << 16 | c << 8 | d);
}
void
print_address(u_int32_t a)
{
	a = ntohl(a);
	printf("%d.%d.%d.%d", a >> 24 & 255, a >> 16 & 255,
	    a >> 8 & 255, a & 255);
}
int
main(int argc, char *argv[])
{
	struct pfioc_natlook nl;
	int dev;
	if (argc != 5) {
		printf("%s <gwy addr> <gwy port> <ext addr> <ext port>n",
		    argv[0]);
		return 1;
	}
	dev = open("/dev/pf", O_RDWR);
	if (dev == -1)
		err(1, "open(\"/dev/pf\") failed");
	memset(&nl, 0, sizeof(struct pfioc_natlook));
	nl.saddr.v4.s_addr	= read_address(argv[1]);
	nl.sport		= htons(atoi(argv[2]));
	nl.daddr.v4.s_addr	= read_address(argv[3]);
	nl.dport		= htons(atoi(argv[4]));
	nl.af			= AF_INET;
	nl.proto		= IPPROTO_TCP;
	nl.direction		= PF_IN;
	if (ioctl(dev, DIOCNATLOOK, &nl))
		err(1, "DIOCNATLOOK");
	printf("internal host ");
	print_address(nl.rsaddr.v4.s_addr);
	printf(":%un", ntohs(nl.rsport));
	return 0;
}
```

## 参见

ioctl(2), altq(4), if_bridge(4), [pflog(4)](pflog.4.md), [pfsync(4)](pfsync.4.md), pfctl(8), [altq(9)](../man9/altq.9.md)

## 历史

`pf` 包过滤机制首次出现于 OpenBSD 3.0，然后是 FreeBSD 5.2。

此实现派生自 OpenBSD 4.5。许多单独的功能、改进、错误修复和安全修复已从更高版本的 OpenBSD 移植。已对其进行了大量修改，使其能够在多线程 FreeBSD 内核中运行并在多个 CPU 上扩展性能。
