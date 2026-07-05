# dummynet.4

`dummynet` — 流量整形器、带宽管理器和延迟模拟器

## 名称

`dummynet`

## 描述

`dummynet` 系统设施允许通过应用带宽和队列大小限制、实现不同的调度和队列管理策略以及模拟延迟和丢失来控制通过各种网络接口的流量。

`dummynet` 的用户界面由 dnctl(8) 工具实现，因此请参阅 dnctl(8) 手册页以获取 `dummynet` 功能及如何使用它的完整描述。

### 内核选项

内核配置文件中以下选项与 `dummynet` 操作相关：

**`IPFIREWALL`** 启用 ipfirewall（如果 `dummynet` 将与 ipfw 一起使用）
**`IPFIREWALL_VERBOSE`** 启用防火墙输出
**`IPFIREWALL_VERBOSE_LIMIT`** 限制防火墙输出
**`DUMMYNET`** 启用 `dummynet` 操作
**`HZ`** 设置定时器粒度

通常，需要以下选项：

```sh
options IPFIREWALL
options DUMMYNET
options HZ=1000		# 强烈推荐
```

此外，可能需要根据所有已配置管道的带宽延迟乘积和队列大小之和提高 mbuf 簇数（用于存储网络数据包）。

## 参见

setsockopt(2), if_bridge(4), [ip(4)](ip.4.md), [pf.conf(5)](../man5/pf.conf.5.md), dnctl(8), [ipfw(8)](../man8/ipfw.8.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`dummynet` 设施最初由 Luigi Rizzo <luigi@iet.unipi.it> 作为 TCP 拥塞控制的测试工具实现，如 ACM Computer Communication Review 1997 年 1 月刊所述。后来它被修改为在 IP 和桥接层工作，与 ipfw(4) 数据包过滤器集成，并扩展为支持多种排队和调度策略。
