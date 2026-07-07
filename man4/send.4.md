# send(4)

`send` — 安全邻居发现（SeND）的内核侧支持

## 名称

`send`

## 概要

`#include <sys/socket.h>`

`#include <netinet/in.h>`

`#include <netinet6/send.h>`

`int socket(PF_INET6, SOCK_RAW, IPPROTO_SEND)`

`要在引导时以模块形式加载此驱动，请将以下行添加到 loader.conf(5) 中：`

```sh
send_load="YES"
```

## 描述

IPv6 节点使用邻居发现协议（NDP）来发现链路上的其他节点，确定它们的链路层地址以查找路由器，并维护到活动成员路径的可达性信息。NDP 容易受到各种攻击 [RFC3756]。安全邻居发现是 NDP 的一组扩展，用于应对 NDP 面临的威胁 [RFC3971]。

SeND 的内核侧支持由一个带钩子的内核模块组成，这些钩子将相关数据包（邻居请求、邻居通告、路由器请求、路由器通告和重定向）从 NDP 栈中转移，通过专用套接字发送到用户空间，并重新注入以进行进一步处理。仅当 `send` 模块已加载时才会触发钩子。

原生 SeND 套接字类似于原始 IP 套接字，但使用其自己的内部伪协议（IPPROTO_SEND）。struct sockaddr_send 定义于

`#include <netinet6/send.h>`

它定义了结构体的总长度、地址族、从接口角度看数据包的传入或传出方向，以及接口索引。

```sh
struct sockaddr_send {
        unsigned char           send_len;       /* 总长度 */
        sa_family_t             send_family;    /* 地址族 */
        int                     send_direction;
        int                     send_ifidx;
        char                    send_zero[8];
};
```

地址族始终为 `AF_INET6`。`send_direction` 变量表示从接口角度看数据包的方向，取值为 `SND_IN` 或 `SND_OUT`。`send_ifidx` 变量是接收或发送接口的接口索引。`send_zero` 变量为填充字段，必须始终为零。

如果没有用户空间应用程序连接到 send 套接字，处理将正常继续，如同模块未加载一样。

## 输入钩子

输入钩子以传入或传出 NDP 数据包的输入路径命名，从网线经 nd6 栈到用户空间。如果 `send` 模块已加载，相关数据包通过向 [mbuf(9)](../man9/mbuf.9.md) 添加 mbuf_tag（参见 [mbuf_tags(9)](../man9/mbuf_tags.9.md)）来标识。然后将其传递给内核-用户空间接口，供 SeND 应用程序进行加密保护或验证。钩子接受一个描述数据包方向的参数，对传入和传出数据包均如此。`SND_IN` 是传入数据包的方向，通常由 SeND 选项保护，然后发送到用户空间进行加密验证。`SND_OUT` 是传出方向。它描述了发送到用户空间以添加 SeND 选项的应答和本地发起的传出数据包。

## 传入数据包

来自网线的传入 ND 数据包：

```sh
                                        内核空间 ( 用户空间
                                                    )
 传入 SeND/ND 数据包                                 (
            |                                       )
            v                 ( SND_IN )            (
           icmp6_input() -> send_input_hook ---> send socket ----+
            :                                       )            |
            :             #                 #       (            |
   正常     :             #                 #       )            v
 处理       :             #     send.ko     #       (    SeND 应用程序
 路径       :             #                 #       )            |
            :             #                 #       (            |
            v                                       )            |
   icmp6/nd6_??_input() <- 协议开关    <--- send socket <---+
            |         结构 (IPPPROTO_SEND)     )
            |                ( SND_IN )             (
            v                                       )
 继续正常 ND 处理                                  (
```

## 传出数据包

传出 ND 数据包（应答或本地触发）：

```sh
                                        内核空间 ( 用户空间
                                                    )
 nd6_na_input()                                     (
 +PACKET_TAG_ND_OUTGOING                            )
 |                                                  )
 |   传出数据包                                     (
 |          |                                       )
 |          v                                       (
 |   icmp6_redirect_output()                        )
 |   nd6_ns_output()                                (
 |   nd6_na_output()                                )
 |   +PACKET_TAG_ND_OUTGOING                        (
 |          |                                       )
 |          +-----------<- rip6_output() <----------)----- rtsol/rtadvd/..
 |          |              +PACKET_TAG_ND_OUTGOING  (
 |          v                                       )
 |       ip6_output()                               (
 |          |                                       )
 +-------->-+                                       (
            |                                       )
            v                ( SND_OUT )            (
        nd6_output_lle() -> send_input_hook ---> send socket ----+
 -PACKET_TAG_ND_OUTGOING                            )            |
            :             #                 #       (            |
   正常     :             #                 #       )            v
 处理       :             #     send.ko     #       (    SeND 应用程序
 路径       :             #                 #       )            |
            :             #                 #       (            |
            v                                       )            |
    (*ifp->if_output)() <- 协议开关    <--- send socket <---+
            |         结构 (IPPPROTO_SEND)     )
            |                ( SND_OUT )            (
            v                                       )
 继续正常数据包输出                                (
```

## 错误

套接字操作可能失败并返回以下错误之一：

**[EEXIST]** 另一个用户空间 SeND 应用程序已绑定到该套接字。

**[ENOBUFS]** 缺少空间来接收来自 SeND 应用程序的传入（受 SeND 保护的）或传出（经 SeND 验证的）数据包。

**[ENOSYS]** 从用户空间接收并传递到 NDP 栈进行进一步处理的数据包既不是邻居请求、邻居通告、路由器请求、路由器通告，也不是重定向。

**[ENOENT]** 接口输出例程未能将数据包发送出接口时发生。

## 参见

recvfrom(2), sendto(2), socket(2), loader.conf(5)

## 历史

`send` 模块最早出现于 FreeBSD 9.0。

## 作者

Ana Kukec <anchie@FreeBSD.org>, University of Zagreb

## 缺陷

由于缺乏 NDP 锁定，目前无法卸载 `send` 模块。
