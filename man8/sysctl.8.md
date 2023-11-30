  SYSCTL(8)  

SYSCTL(8)

FreeBSD System Manager's Manual

SYSCTL(8)

[名称](#__u540D___u79F0_)
=======================

`sysctl` —

获取或设置内核状态

[概要](#__u6982___u8981_)
=======================

`sysctl` \[`-bdehiNnoTtqWx`\] \[`-B` bufsize\] \[`-f` filename\] name\[=value\[,value\]\] ... `sysctl` \[`-bdehNnoTtqWx`\] \[`-B` bufsize\] `-a`

[描述](#__u63CF___u8FF0_)
=======================

`sysctl` 实用程序检索内核状态并允许具有适当权限的进程设置内核状态。 要检索或设置的状态使用 “管理信息库” (“MIB”) 样式名称来描述，描述为组件的虚线集。

可以使用以下选项：

[`-A`](#A)

等效于 `-o` `-a` （为了兼容性）。

[`-a`](#a)

列出所有当前可用的非透明值。 如果在命令行上指定了一个或多个变量名称，则忽略此选项。

[`-b`](#b)

强制以原始二进制格式输出变量的值。 不打印名称，也不输出终止换行符。 这对于单个变量最有用。

[`-B`](#B) bufsize

将要从 `sysctl` 读取的缓冲区大小设置为 bufsize 。 这对于具有可变长度的 `sysctl` 是必需的，并且探测值 0 是有效长度，例如 kern.arandom 。

[`-d`](#d)

打印变量的描述而不是其值。

[`-e`](#e)

用 ‘`=`’ 分隔变量的名称和值。 这对于生成可以反馈给 `sysctl` 实用程序的输出很有用。 如果指定了 `-N` 或 `-n` ，或者正在设置变量，则忽略此选项。

[`-f`](#f) filename

指定每行包含一对名称和值的文件。 `sysctl` 首先读取并处理指定的文件，然后处理命令行参数中的名称和值对。

[`-h`](#h)

为人类而非机器的可读性格式化输出。

[`-i`](#i)

忽略未知的 OID。 目的是利用 `sysctl` 从各种机器（并非所有机器都必须运行完全相同的软件）更容易收集数据。

[`-N`](#N)

只显示变量名，而不是它们的值。 这对于提供可编程完成的 shell 特别有用。 要在 zsh(1) (ports/shells/zsh) 中启用变量名的补全，请使用以下代码：

listsysctls () { set -A reply $(sysctl -AN ${1%.\*}) } compctl -K listsysctls sysctl 

要在 tcsh(1) 中启用变量名的补全，请使用：

```complete sysctl 'n/*/`sysctl -Na`/'```

[`-n`](#n)

不显示变量名。 此选项对于设置 shell 变量很有用。 例如，要将页面大小保存在变量 psize 中，请使用：

```set psize=`sysctl -n hw.pagesize` ```

[`-o`](#o)

显示不透明变量（通常被抑制）。 打印格式和长度，以及值的前 16 个字节的十六进制转储。

[`-q`](#q)

将 `sysctl` 生成的一些警告抑制为标准错误。

[`-T`](#T)

仅显示可通过加载程序 (CTLFLAG\_TUN) 设置的变量。

[`-t`](#t)

打印变量的类型。

[`-W`](#W)

仅显示非统计的可写变量。 对于确定一组运行时可调 sysctl 很有用。

[`-X`](#X)

等效于 `-x` `-a` （为了兼容性）。

[`-x`](#x)

与 `-o` 一样，但打印整个值的十六进制转储，而不仅仅是前几个字节。

`sysctl` 提供的信息包括整数、字符串和不透明类型。 `sysctl` 实用程序只知道几个不透明类型，其余的将求助于 hexdump。 如果由 ps(1), systat(1) 和 netstat(1) 等特殊用途的程序检索，不透明信息会更加有用。

一些在正常系统操作期间无法修改的变量可以通过 loader(8) 可调参数进行初始化。 例如，这可以通过在 loader.conf(5) 中设置它们来完成。 请参阅 loader.conf(5) 以获取有关哪些可调参数可用以及如何设置它们的更多信息。

字符串和整数信息总结如下。 有关这些变量的详细说明，请参见 sysctl(3) 。

可更改的列指示具有适当权限的进程是否可以更改该值。 可以使用 `sysctl` 设置字符串和整数值。

**Name**

Type

Changeable

kern.ostype

string

no

kern.osrelease

string

no

kern.osrevision

integer

no

kern.version

string

no

kern.maxvnodes

integer

yes

kern.maxproc

integer

no

kern.maxprocperuid

integer

yes

kern.maxfiles

integer

yes

kern.maxfilesperproc

integer

yes

kern.argmax

integer

no

kern.securelevel

integer

raise only

kern.hostname

string

yes

kern.hostid

integer

yes

kern.clockrate

struct

no

kern.posix1version

integer

no

kern.ngroups

integer

no

kern.job\_control

integer

no

kern.saved\_ids

integer

no

kern.boottime

struct

no

kern.domainname

string

yes

kern.filedelay

integer

yes

kern.dirdelay

integer

yes

kern.metadelay

integer

yes

kern.osreldate

integer

no

kern.bootfile

string

yes

kern.corefile

string

yes

kern.logsigexit

integer

yes

security.bsd.suser\_enabled

integer

yes

security.bsd.see\_other\_uids

integer

yes

security.bsd.unprivileged\_proc\_debug

integer

yes

security.bsd.unprivileged\_read\_msgbuf

integer

yes

vm.loadavg

struct

no

hw.machine

string

no

hw.model

string

no

hw.ncpu

integer

no

hw.byteorder

integer

no

hw.physmem

integer

no

hw.usermem

integer

no

hw.pagesize

integer

no

hw.floatingpoint

integer

no

hw.machine\_arch

string

no

hw.realmem

integer

no

machdep.adjkerntz

integer

yes

machdep.disable\_rtc\_set

integer

yes

machdep.guessed\_bootdev

string

no

user.cs\_path

string

no

user.bc\_base\_max

integer

no

user.bc\_dim\_max

integer

no

user.bc\_scale\_max

integer

no

user.bc\_string\_max

integer

no

user.coll\_weights\_max

integer

no

user.expr\_nest\_max

integer

no

user.line\_max

integer

no

user.re\_dup\_max

integer

no

user.posix2\_version

integer

no

user.posix2\_c\_bind

integer

no

user.posix2\_c\_dev

integer

no

user.posix2\_char\_term

integer

no

user.posix2\_fort\_dev

integer

no

user.posix2\_fort\_run

integer

no

user.posix2\_localedef

integer

no

user.posix2\_sw\_dev

integer

no

user.posix2\_upe

integer

no

user.stream\_max

integer

no

user.tzname\_max

integer

no

user.localbase

string

no

[文件](#__u6587___u4EF6_)
=======================

`<sys/sysctl.h>`

顶级标识符、二级内核和硬件标识符以及用户级标识符的定义

`<sys/socket.h>`

二级网络标识符的定义

`<sys/gmon.h>`

第三级分析标识符的定义

`<vm/vm_param.h>`

二级虚拟内存标识符的定义

`<netinet/in.h>`

三级互联网标识符和四级 IP 标识符的定义

`<netinet/icmp_var.h>`

第四级 ICMP 标识符的定义

`<netinet/udp_var.h>`

第四级 UDP 标识符的定义

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `sysctl` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

例如，要检索系统中允许的最大进程数，可以使用以下请求：

`sysctl kern.maxproc`

要将每个 uid 允许的最大进程数设置为 1000，可以使用以下请求：

`sysctl kern.maxprocperuid=1000`

可以通过以下方式获得有关系统时钟速率的信息：

`sysctl kern.clockrate`

有关负载平均历史的信息可以通过以下方式获得：

`sysctl vm.loadavg`

存在比这些更多的变量，而寻找其更深层含义的最佳且可能唯一的地方无疑是定义它们的来源。

[兼容性](#__u517C___u5BB9___u6027_)
================================

`-w` 选项已被弃用，并被默默地忽略。

[参见](#__u53C2___u89C1_)
=======================

sysctl(3), loader.conf(5), sysctl.conf(5), loader(8)

[历史](#__u5386___u53F2_)
=======================

`sysctl` 实用程序首先出现在 4.4BSD 中。

在 FreeBSD 2.2 中， `sysctl` 进行了重大改造。

[缺陷](#__u7F3A___u9677_)
=======================

`sysctl` 实用程序目前利用内核 sysctl 工具的未记录接口来遍历 sysctl 树并检索格式和名称信息。 目前正在考虑这个正确的接口。

October 30, 2020

FreeBSD 13.1-RELEASE