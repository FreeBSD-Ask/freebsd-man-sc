# dummymbuf(4)

`dummymbuf` — mbuf 修改 pfil 钩子

## 名称

`dummymbuf`

## 概要

`若要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device dummymbuf

`或者，若要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
dummymbuf_load="YES"
```

## 描述

此模块用于在异常 mbuf 布局下测试网络代码。其中提供了用于 mbuf 修改的特殊 [pfil(9)](../man9/pfil.9.md) 钩子，可使用 pfilctl(8) 按如下方式列出：

```sh
            Hook                      Type
       dummymbuf:ethernet         Ethernet
       dummymbuf:inet6                IPv6
       dummymbuf:inet                 IPv4
```

要激活某个钩子，必须将其链接到相应的 [pfil(9)](../man9/pfil.9.md) 头。可使用 pfilctl(8) 进行链接。

每次调用钩子时，都会从 `net.dummymbuf.rules` sysctl 读取一组共享的 Sx RULES。规则按顺序求值，每条匹配的规则对 mbuf 执行指定操作。

每次成功应用操作后，`net.dummymbuf.hits` sysctl 计数器都会递增。

钩子会返回修改后的 mbuf 以供进一步处理，但如果规则解析或操作失败，则会丢弃数据包。此外，原始链中的第一个 mbuf 可能被更换。

该模块基于 [VNET(9)](../man9/vnet.9.md)，因此每个 jail(2) 都提供其自己的钩子和 sysctl 变量集合。

## 规则

规则集是以分号分隔的列表。空字符串被视为解析失败。一条规则在概念上分为两部分：过滤器和操作，语法如下：

```sh
{inet | inet6 | ethernet} {in | out} <ifname> <opname>[ <opargs>];
```

### 过滤器

规则的第一个单词匹配 [pfil(9)](../man9/pfil.9.md) 类型。第二个匹配数据包的方向，第三个匹配数据包来源的网络接口。

### 操作

操作可以带有参数，参数与操作名之间以空格分隔。可用操作包括：

**pull-head** <number-of-bytes> 无条件创建一个全新的基于簇的 mbuf，将其链接为原始 mbuf 链的第一个 mbuf，并相应移动数据包头部。之后，从原始 mbuf 链中拉取指定数量的字节。如果要求拉取 0 字节，则结果链的第一个 mbuf 将留空。要求拉取超过 `MCLBYTES` 的字节数视为操作失败。如果 mbuf 链中数据少于请求数量，则会拉取整个数据包，尾部 mbuf 留空。结果仅修改 mbuf 链的布局，其内容在逻辑上保持不变。

**enlarge** <number-of-bytes> 无条件将 mbuf 替换为指定大小的 mbuf。

## SYSCTL 变量

可用变量如下：

**`net.dummymbuf.rules`** 表示所有 `dummymbuf` 钩子共享的一组 Sx RULES 的字符串。

**`net.dummymbuf.hits`** 规则被应用的次数。写入时重置为零。

## 实例

正如设计意图所示，`dummymbuf` 可用于防火墙测试。在 mbuf 链到达防火墙之前对其进行修改，可测试防火墙能否处理相应情形。因此，钩子的顺序很重要。测试用例应首先准备并启用防火墙，使其钩子链接到位。然后使用 pfilctl(8) 链接 `dummymbuf` 钩子，使其位于防火墙之前。

以下命令为入站流量链接 `dummymbuf:inet6` 钩子，并将其置于其他钩子之前：

```sh
pfilctl link -i dummymbuf:inet6 inet6
```

对出站流量执行相同操作：

```sh
pfilctl link -o -a dummymbuf:inet6 inet6
```

例如，我们希望测试链中第一个 mbuf 的 m_len 为零的场景，以验证防火墙在此情况下能否正确读取数据包数据。以下规则集对入站和出站均执行此操作：

```sh
sysctl net.dummymbuf.rules="inet6 in em0 pull-head 0; inet6 out em0 pull-head 0;"
```

建议在执行其他测试断言的同时校验 `net.dummymbuf.hits` sysctl 计数器，以确保 `dummymbuf` 确实在工作，避免因配置错误导致假阳性。在执行操作前重置该计数器是一个好习惯：

```sh
sysctl net.dummymbuf.hits=0
```

测试用例之后清理环境同样重要：

```sh
pfilctl unlink -i dummymbuf:inet6 inet6
pfilctl unlink -o dummymbuf:inet6 inet6
sysctl net.dummymbuf.rules=""
```

如果测试用例在临时 vnet 中运行，则可省略显式清理，`dummymbuf` 设施会随其 vnet 实例一起消失。

## 诊断

- dummymbuf: <filter match>: rule parsing failed: <the rule in question> 若一切看似正常，则可能是多余空格导致的问题，因为解析器保持非常简单。
- dummymbuf: <filter match>: mbuf operation failed: <the rule in question> 找到错误的操作参数、mbuf 分配失败等。

## 参见

jail(2), pfilctl(8), [mbuf(9)](../man9/mbuf.9.md), [pfil(9)](../man9/pfil.9.md), [VNET(9)](../man9/vnet.9.md)

## 作者

此模块及本手册页由 Igor Ostapenko <pm@igoro.pro> 编写。
