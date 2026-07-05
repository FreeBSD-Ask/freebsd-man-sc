# mod_cc.4

`mod_cc` — 模块化拥塞控制

## 名称

`mod_cc`

## 描述

模块化拥塞控制框架允许 TCP 实现动态更改由新连接和现有连接使用的拥塞控制算法。算法通过唯一的 [ascii(7)](../man7/ascii.7.md) 名称进行标识。算法模块可以编译进内核，也可使用 [kld(4)](kld.4.md) 机制作为内核模块加载。

默认算法为 CUBIC，所有连接都使用该默认值，除非通过 `TCP_CONGESTION` 套接字选项显式覆盖（详见 [tcp(4)](tcp.4.md)）。可使用 sysctl(3) MIB 变量更改默认值，该变量在下文的 MIB 变量章节中详细说明。

可通过 `TCP_CCALGOOPT` 套接字选项设置或查询特定于算法的参数（详见 [tcp(4)](tcp.4.md)）。调用者必须传递一个指向算法特定数据的指针，并指定其大小。

如果某个拥塞控制模块被任何 Vnet 用作默认值，则卸载该模块将失败。卸载模块时，会使用 Vnet 默认值将连接切换到备用拥塞控制。注意，新的拥塞控制模块可能无法初始化其内部内存，若如此则模块卸载将失败。如果这种情况经常发生，重试卸载通常会成功，因为新 CC 模块 malloc 内存时阻止切换的临时内存短缺通常是暂时的。

## MIB 变量

该框架在 sysctl(3) MIB 的 `net.inet.tcp.cc` 分支下暴露以下变量：

**`available`** 只读列表，按名称列出当前可用的拥塞控制算法。

**`algorithm`** 读取时返回当前默认拥塞控制算法，设置时更改默认值。尝试更改默认算法时，应将此变量设置为 `net.inet.tcp.cc.available` MIB 变量所列名称之一。

**`abe`** 启用对 RFC 8511 的支持，该 RFC 修改了响应 ECN 拥塞信号时应用于拥塞窗口的窗口减小因子。请参阅各个拥塞控制手册页以确定其是否实现了 ABE 支持以及相关配置详情。

**`abe_frlossreduce`** 若非零，在 ECN 信号通知的拥塞恢复期间若同时需要修复丢失，则应用标准 beta 而非 ABE-beta。

**`hystartplusplus.bblogs`** 此布尔值控制是否对 hystart++ 事件进行黑盒日志记录。设为零（默认）时不进行日志记录。设为一时所有 hystart++ 事件都会生成黑盒日志。

**`hystartplusplus.css_rounds`** 此值控制 CSS 运行的轮数。默认值与当前互联网草案一致，为 5。

**`hystartplusplus.css_growth_div`** 此值控制 CSS 期间应用于慢启动的除数。默认值与当前互联网草案一致，为 4。

**`hystartplusplus.n_rttsamples`** 此值控制每轮必须收集多少个 rtt 样本才能使 hystart++ 处于活动状态。默认值与当前互联网草案一致，为 8。

**`hystartplusplus.maxrtt_thresh`** 此值控制考虑是否需要 CSS 时的最大 rtt 方差钳制值。默认值与当前互联网草案一致，为 16000（单位为微秒）。进一步说明请参阅互联网草案。

**`hystartplusplus.minrtt_thresh`** 此值控制考虑是否需要 CSS 时的最小 rtt 方差钳制值。默认值与当前互联网草案一致，为 4000（单位为微秒）。进一步说明请参阅互联网草案。

每个拥塞控制模块还可暴露其他 MIB 变量以控制其行为。注意，NewReno 和 CUBIC 现在都基于互联网草案版本 3 支持 Hystart++。

## 内核配置

所有可用的拥塞控制模块也可通过内核配置选项加载。内核配置需要通过内核选项内置至少一种拥塞控制算法，并指定一个系统默认值。如果不满足这两个条件，内核编译将失败。

## 内核配置选项

该框架暴露以下内核配置选项。

**`CC_NEWRENO`** 此指令加载 NewReno 拥塞控制算法。

**`CC_CUBIC`** 此指令加载 CUBIC 拥塞控制算法，默认包含在 GENERIC 中。

**`CC_VEGAS`** 此指令加载 vegas 拥塞控制算法，注意此算法还需要 TCP_HHOOK 选项。

**`CC_CDG`** 此指令加载 cdg 拥塞控制算法，注意此算法还需要 TCP_HHOOK 选项。

**`CC_DCTCP`** 此指令加载 dctcp 拥塞控制算法。

**`CC_HD`** 此指令加载 hd 拥塞控制算法，注意此算法还需要 TCP_HHOOK 选项。

**`CC_CHD`** 此指令加载 chd 拥塞控制算法，注意此算法还需要 TCP_HHOOK 选项。

**`CC_HTCP`** 此指令加载 htcp 拥塞控制算法。

**`CC_DEFAULT`** 此指令指定表示系统默认算法名称的字符串，GENERIC 内核默认将其设置为 CUBIC。

## 参见

[cc_cdg(4)](cc_cdg.4.md), [cc_chd(4)](cc_chd.4.md), [cc_cubic(4)](cc_cubic.4.md), [cc_dctcp(4)](cc_dctcp.4.md), [cc_hd(4)](cc_hd.4.md), [cc_htcp(4)](cc_htcp.4.md), [cc_newreno(4)](cc_newreno.4.md), [cc_vegas(4)](cc_vegas.4.md), [tcp(4)](tcp.4.md), [config(5)](../man5/config.5.md), [config(8)](../man8/config.8.md), [mod_cc(9)](../man9/mod_cc.9.md)

## 致谢

本软件的开发和测试部分得益于 FreeBSD 基金会和 Community Foundation Silicon Valley 下的 Cisco 大学研究计划基金的资助。

## 历史

`mod_cc` 模块化拥塞控制框架首次出现于 FreeBSD 9.0。

该框架于 2007 年由 James Healy 和 Lawrence Stewart 首次发布，当时他们在澳大利亚墨尔本斯威本科技大学先进互联网架构中心从事 NewTCP 研究项目，该项目部分得益于 Community Foundation Silicon Valley 下的 Cisco 大学研究计划基金的资助。更多详情见：

<http://caia.swin.edu.au/urp/newtcp/>

## 作者

`mod_cc` 机制由 Lawrence Stewart <lstewart@FreeBSD.org>、James Healy <jimmy@deefa.com> 和 David Hayes <david.hayes@ieee.org> 编写。

本手册页由 David Hayes <david.hayes@ieee.org> 和 Lawrence Stewart <lstewart@FreeBSD.org> 编写。
