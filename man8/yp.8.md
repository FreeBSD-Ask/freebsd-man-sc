# yp(8)

`yp` — YP/NIS 系统说明

## 名称

`yp`

## 概要

`yp`

## 描述

`YP` 子系统允许通过网络管理 passwd、group、netgroup、hosts、services、rpc、bootparams 和 ethers 文件条目，通过 getpwent(3)、getgrent(3)、getnetgrent(3)、gethostent(3)、getnetent(3)、getrpcent(3) 和 ethers(3) 函数实现。bootparamd(8) 守护进程直接调用 NIS 库函数，因为标准 C 库中没有用于读取 bootparams 的函数。NIS 支持在 [nsswitch.conf(5)](../man5/nsswitch.conf.5.md) 中启用。

`YP` 子系统如果在 **/etc/rc.conf** 中已初始化，并且目录 **/var/yp** 存在（在默认发行版中存在），则会在 **/etc/rc** 中自动启动。还必须使用 domainname(1) 命令设置默认 NIS 域名，如果在 **/etc/rc.conf** 中指定了域名，系统启动时会自动设置。

NIS 是一个基于 RPC 的客户端/服务器系统，允许 NIS 域内的一组机器共享一组公共配置文件。这使系统管理员能够以最少的配置数据设置 NIS 客户端系统，并从单一位置添加、删除或修改配置数据。

所有 NIS 信息的规范副本存储在一台称为 NIS *主服务器*（master server）的机器上。用于存储信息的数据库称为 NIS *映射*（maps）。在 FreeBSD 中，这些映射存储在 **/var/yp/<domainname>** 中，其中 <domainname> 是所服务的 NIS 域名。单个 NIS 服务器可以同时支持多个域，因此可能有多个这样的目录，每个支持的域一个。每个域都有自己独立的映射集。

在 FreeBSD 中，NIS 映射是 Berkeley DB 哈希数据库文件（与 [passwd(5)](../man5/passwd.5.md) 数据库文件使用的格式相同）。其他支持 NIS 的操作系统使用老式 `ndbm` 数据库（主要是因为 Sun Microsystems 最初将其 NIS 实现基于 `ndbm`，而其他供应商只是许可了 Sun 的代码，而非使用不同数据库格式设计自己的实现）。在这些系统上，数据库通常分为 `.dir` 和 `.pag` 文件，`ndbm` 代码用它们分别保存哈希数据库的不同部分。Berkeley DB 哈希方法则将两部分信息都使用单个文件。这意味着在其他操作系统上你可能有 `passwd.byname.dir` 和 `passwd.byname.pag` 文件（实际上都是同一映射的部分），而 FreeBSD 只有一个名为 `passwd.byname` 的文件。格式差异并不重要：只有 NIS 服务器 ypserv(8) 及相关工具需要知道 NIS 映射的数据库格式。客户端 NIS 系统以 ASCII 形式接收所有 NIS 数据。

NIS 系统有三种主要类型：

1. NIS 客户端，向 NIS 服务器查询信息。
2. NIS 主服务器，维护所有 NIS 映射的规范副本。
3. NIS 从服务器，维护 NIS 映射的备份副本，由主服务器定期更新。

NIS 客户端使用 ypbind(8) 守护进程与特定 NIS 服务器建立所谓的 *绑定*（binding）。ypbind(8) 工具检查系统的默认域（由 domainname(1) 命令设置），并开始在本地网络上广播 RPC 请求。这些请求指定 ypbind(8) 尝试建立绑定的域名。如果配置为服务所请求域的服务器接收到其中一个广播，它将响应 ypbind(8)，后者将记录该服务器的地址。如果有多个可用服务器（例如一个主服务器和多个从服务器），ypbind(8) 将使用第一个响应的地址。从那时起，客户端系统将把所有 NIS 请求定向到该服务器。ypbind(8) 工具会偶尔“ping”服务器以确保它仍在运行。如果在合理时间内未收到某个 ping 的回复，ypbind(8) 将把该域标记为未绑定，并重新开始广播，希望找到另一台服务器。

NIS 主服务器和从服务器使用 ypserv(8) 守护进程处理所有 NIS 请求。ypserv(8) 工具负责接收来自 NIS 客户端的传入请求，将请求的域名和映射名转换为对应数据库文件的路径，并将数据库中的数据传回客户端。ypserv(8) 设计用于处理一组特定的请求，其中大多数实现为标准 C 库中的函数：

`yp_order()` 检查特定映射的创建日期

`yp_master()` 获取给定映射/域的 NIS 主服务器名

`yp_match()` 在特定映射/域中查找与给定键对应的数据

`yp_first()` 获取特定映射/域中的第一个键/数据对

`yp_next()` 向 ypserv(8) 传递特定映射/域中的键，并让它返回紧随其后的键/数据对（函数 `yp_first()` 和 `yp_next()` 可用于对 NIS 映射进行顺序搜索）

`yp_all()` 检索映射的全部内容

ypserv(8) 还能处理一些其他请求（例如确认你是否能处理特定域（`YPPROC_DOMAIN`），或仅当能处理该域时才确认，否则保持沉默（`YPPROC_DOMAIN_NONACK`）），但这些请求通常仅由 ypbind(8) 生成，不供标准工具使用。

在拥有大量主机的网络上，使用一个主服务器和多个从服务器通常比仅使用单个主服务器更好。从服务器提供与主服务器完全相同的信息：每当主服务器上的映射更新时，应使用 yppush(8) 命令将新数据传播到从服务器系统。如果管理员创建了 **/var/yp/Makefile.local** 并清空 `NOPUSH` 变量，NIS `Makefile`（**/var/yp/Makefile**）将自动执行此操作：

```sh
NOPUSH=
```

（`NOPUSH` 默认设置为 true，因为默认配置是针对只有一台 NIS 服务器的小型网络。）yppush(8) 命令将在主服务器和从服务器之间发起事务，从服务器使用 ypxfr(8) 从主服务器传输指定映射。（从服务器在 ypserv(8) 内部自动调用 ypxfr(8)；因此管理员通常不需要直接使用它。但如果需要，可以手动运行。）维护从服务器通过以下方式帮助改善大型网络上的 NIS 性能：

- 在 NIS 主服务器崩溃或不可达时提供备份服务
- 将客户端负载分散到多台机器上，而非使主服务器过载
- 允许单个 NIS 域扩展到本地网络之外（如果 ypbind(8) 守护进程所在网络超出其广播范围，它可能无法自动定位服务器。可以使用 ypset(8) 强制 ypbind(8) 绑定到特定服务器，但这有时不太方便。只需在本地网络上放置一台从服务器即可避免此问题。）

FreeBSD 的 ypserv(8) 专门设计为在与 FreeBSD 客户端系统一起使用时提供增强的安全性（与其他 NIS 实现相比）。FreeBSD 密码数据库系统（直接源自 4.4BSD）包含对 *shadow 密码* 的支持。标准密码数据库不包含用户的加密密码：这些密码与其它信息一起存储在单独的数据库中，只有超级用户可访问。如果加密密码数据库作为 NIS 映射提供，此安全功能将完全失效，因为允许任何用户检索 NIS 数据。

为帮助防止这种情况，FreeBSD 的 NIS 服务器以特殊方式处理 shadow 密码映射（`master.passwd.byname`、`master.passwd.byuid`、`shadow.byname` 和 `shadow.byuid`）：服务器仅响应源自特权端口的请求才提供对这些映射的访问。由于只有超级用户被允许绑定到特权端口，服务器假定所有此类请求都来自特权用户。所有其他请求都被拒绝：来自非特权端口的请求只会从服务器收到错误代码。此外，FreeBSD 的 ypserv(8) 包含对 Wietse Venema 的 tcp wrapper 包的支持；启用 tcp wrapper 支持后，管理员可以配置 ypserv(8) 仅响应选定的客户端机器。

虽然这些增强功能提供了比标准 NIS 更好的安全性，但绝非 100% 有效。有权访问你网络的人仍可能欺骗服务器泄露 shadow 密码映射。

在客户端，FreeBSD 的 getpwent(3) 函数会自动搜索 `master.passwd` 映射并在存在时使用它们。如果存在，将使用它们，并解码这些特殊映射中的所有字段（类、密码期限和账户过期）。如果未找到，则改用标准 `passwd` 映射。

## 兼容性

当为 [passwd(5)](../man5/passwd.5.md) 文件使用非 FreeBSD 的 NIS 服务器时，它不太可能接受 FreeBSD 用于密码的默认基于 MD5 的格式。如果是这种情况，应将 login.conf(5) 中 `passwd_format` 设置的值更改为 “`des`” 以保持兼容性。

某些系统（如 SunOS 4.x）需要 NIS 运行，其主机名解析函数（`gethostbyname()`、`gethostbyaddr()` 等）才能正常工作。在这些系统上，当被要求返回其 `hosts.byname` 或 `hosts.byaddr` 映射中不存在的主机信息时，ypserv(8) 会执行 DNS 查找。FreeBSD 的解析器默认使用 DNS（如果需要，可以改为使用 NIS），因此其 NIS 服务器默认不执行 DNS 查找。但是，如果以特殊标志启动 ypserv(8)，可使其执行 DNS 查找。它还可以注册为 NIS v1 服务器，以安抚某些坚持需要 v1 服务器存在的系统（FreeBSD 仅使用 NIS v2，但许多其他系统（包括 SunOS 4.x）在绑定时会同时搜索 v1 和 v2 服务器）。FreeBSD 的 ypserv(8) 实际上不处理 NIS v1 请求，但此“kludge 模式”对于让那些同时搜索 v1 和 v2 服务器的顽固系统安静下来很有用。

（有关这些特殊功能和标志的详细描述，请参见 ypserv(8) 手册页。）

## 参见

domainname(1), ypcat(1), ypmatch(1), ypwhich(1), [nsswitch.conf(5)](../man5/nsswitch.conf.5.md), yp_mkdb(8), ypbind(8), ypinit(8), yppoll(8), yppush(8), ypserv(8), ypset(8), ypxfr(8)

## 历史

`YP` 子系统由 Theo de Raadt 从头编写，与 Sun 的实现兼容。后来由 Bill Paul 添加了错误修复、改进和 NIS 服务器支持。服务器端代码最初由 Peter Eriksson 和 Tobias Reber 编写，受 GNU 公共许可证约束。未参考任何 Sun 代码。

## 缺陷

虽然 FreeBSD 现在同时具备 NIS 客户端和服务器功能，但尚不支持 ypupdated(8) 或 `yp_update()` 函数。两者都需要安全 RPC，而 FreeBSD 尚不支持。

getservent(3) 和 getprotoent(3) 函数尚不支持 NIS。幸运的是，这些文件不需要经常更新。

还应编写更多手册页，尤其是 ypclnt(3)。目前，请寻找一台本地 Sun 机器并阅读那里的手册。

无论是 Sun 还是本文作者都未找到一种干净的方法来处理 ypbind 在启动时找不到其服务器时出现的问题。
