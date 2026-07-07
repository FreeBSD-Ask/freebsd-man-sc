# nsswitch.conf(5)

`nsswitch.conf` — 名称服务切换配置文件

## 名称

`nsswitch.conf`

## 描述

`nsswitch.conf` 文件指定了 C 库中的 nsdispatch(3)（名称服务切换分发器）例程的运行方式。

该配置文件控制进程如何查找包含主机、用户（密码）、组等信息的各类数据库。每个数据库都来自一个数据源（例如本地文件、DNS、NIS 和缓存），而在 `nsswitch.conf` 中指定了查找这些数据源的顺序。

`nsswitch.conf` 中的每个条目由一个数据库名和一个以空格分隔的数据源列表组成。每个数据源可以带有一个可选的尾部判定条件，用于决定是使用下一个列出的数据源，还是在当前数据源处终止查找。每个判定条件由一个或多个状态码以及在该状态码发生时要采取的操作组成。

### 数据源

以下数据源作为基础系统的一部分实现：

**数据源** **描述**

**files** 本地文件，例如 **/etc/hosts** 和 **/etc/passwd**。

**db** 本地数据库。

**dns** Internet 域名系统。“hosts”和“networks”使用 **IN** 类条目，所有其他数据库使用 **HS** 类（Hesiod）条目。

**nis** NIS（以前称为 YP）。

**compat** 在 “passwd” 和 “group” 数据库中支持 “+/-” 语法。如果存在此数据源，它必须是该条目的唯一数据源。

**cache** 使用 nscd(8) 守护进程。

其他数据源可能由第三方软件提供。

### 数据库

以下数据库由相应的 C 库函数使用：

**数据库** **使用者**

**group** getgrent(3), getgrent_r(3), getgrgid_r(3), getgrnam_r(3), setgrent(3), endgrent(3)

**hosts** getaddrinfo(3), gethostbyaddr(3), gethostbyaddr_r(3), gethostbyname(3), gethostbyname2(3), gethostbyname_r(3), getipnodebyaddr(3), getipnodebyname(3)

**networks** getnetbyaddr(3), getnetbyaddr_r(3), getnetbyname(3), getnetbyname_r(3)

**passwd** getpwent(3), getpwent_r(3), getpwnam_r(3), getpwuid_r(3), setpwent(3), endpwent(3)

**shells** getusershell(3)

**services** getservent(3)

**rpc** getrpcbyname(3), getrpcbynumber(3), getrpcent(3)

**proto** getprotobyname(3), getprotobynumber(3), getprotoent(3)

**netgroup** getnetgrent(3), getnetgrent_r(3), setnetgrent(3), endnetgrent(3), innetgr(3)

### 状态码

可以使用以下状态码：

**状态** **描述**

**success** 找到了请求的条目。

**notfound** 该数据源中不存在该条目。

**tryagain** 数据源繁忙，可能会响应重试。

**unavail** 数据源未响应，或条目已损坏。

### 操作

对于每个状态码，可以采取以下两种操作之一：

**操作** **描述**

**continue** 尝试下一个数据源。

**return** 返回当前结果。

### 文件格式

`nsswitch.conf` 语法的 BNF 描述如下：

**<entry>** ::= <database> ":" [<source> [<criteria>]]*

**<criteria>** ::= "[" <criterion>+ "]"

**<criterion>** ::= <status> "=" <action>

**<status>** ::= "success" | "notfound" | "unavail" | "tryagain"

**<action>** ::= "return" | "continue"

每个条目在文件中从新行开始。“#”分隔注释到行尾。空行将被忽略。行尾的 “\” 转义换行符，使下一行成为当前行的延续。所有条目均不区分大小写。

默认判定条件是在 “success” 时返回，在其他任何情况下继续（即 `[success=return notfound=continue unavail=continue tryagain=continue]`）。

### 缓存

你可以在 `nsswitch.conf` 文件中指定 “cache” 来为特定数据库启用缓存。它应当位于 “files” 之后，但在 “nis” 等远程数据源之前。你还应当为该数据库在 nscd.conf(5) 中启用缓存。如果对于特定查询 “cache” 数据源返回成功，则不会查询其他数据源。另一方面，如果之前没有缓存的数据，查询结果将在所有其他数据源处理完毕后放入缓存。注意，“cache” 需要 nscd(8) 守护进程正在运行。

### 兼容模式：+/- 语法

在历史性的多数据源实现中，“+” 和 “-” 字符用于指定从 NIS 导入用户密码和组信息。虽然 `nsswitch.conf` 提供了访问分布式数据源（如 NIS）的替代方法，但指定 “compat” 作为唯一数据源将提供历史性行为。

通过指定 “passwd_compat: source”，可以为通过 “+/-” 访问的信息使用替代数据源。在这种情况下，“source” 可以是 “dns”、“nis” 或除 “files” 和 “compat” 之外的任何其他数据源。

### 注释

从历史上看，许多数据库都有枚举函数，通常采用 Fn getXXXent 形式。当数据库位于本地文件中时，这些函数是有意义的，但当可能存在多个数据源，且每个数据源大小未知时，这些函数就不再有意义或相关性较低。出于兼容性考虑，仍然提供了这些接口，但数据源可能无法提供完整的条目，或者如果指定了多个包含类似信息的数据源，可能会检索到重复的条目。

为确保与先前及当前实现的兼容性，“compat” 数据源对于给定数据库必须单独出现。

### 默认数据源列表

如果由于任何原因 `nsswitch.conf` 不存在，或者其条目缺失或损坏，nsdispatch(3) 将为请求的数据库默认使用 “files” 条目。例外情况如下：

**数据库** **默认数据源列表**

**group** compat

**group_compat** nis

**hosts** files dns

**passwd** compat

**passwd_compat** nis

**services** compat

**services_compat** nis

## 文件

**/etc/nsswitch.conf** 文件 `nsswitch.conf` 位于 **/etc** 中。

## 实例

要在 **/etc/hosts** 中查找主机，然后在缓存中查找，再从 DNS 中查找，并从 NIS 然后从文件中查找用户信息，使用：

**hosts:** files cache dns

**passwd:** nis [notfound=return] files

**group:** nis [notfound=return] files

判定条件 “[notfound=return]” 设置了 “如果在 nis 中未找到用户，则不要尝试 files” 的策略。这将 nis 视为权威信息源，除非服务器宕机。

## 注释

`nsswitch.conf` 文件被每个程序仅解析一次。后续的更改在程序重新启动之前不会生效。

如果系统在编译时使用了 `WITHOUT_NIS`，你必须移除 “nis” 条目。

FreeBSD 的 Lb libc 提供了存根，用于与为 GNU C 库 `nsswitch` 接口编写的 NSS 模块兼容。但是，这些存根仅支持使用 “`passwd`” 和 “`group`” 数据库。

## 参见

nsdispatch(3), nscd.conf(5), resolv.conf(5), nscd(8), ypbind(8)

## 历史

`nsswitch` 文件格式首次出现在 FreeBSD 5.0 中。它是从 NetBSD 项目导入的，最初出现在 NetBSD 1.4 中。

## 作者

Luke Mewburn <lukem@netbsd.org> 编写了这个可自由分发的名称服务切换实现，借鉴了 ULTRIX svc.conf(5) 和 Solaris nsswitch.conf(4) 手册页中的思想。
