# sysctl(3)

`sysctl` — 获取或设置系统信息

## 名称

`sysctl`, `sysctlbyname`, `sysctlnametomib`

## 库

Lb libc

## 概要

`#include <sys/sysctl.h>`

```c
int
sysctl(const int *name, u_int namelen, void *oldp, size_t *oldlenp,
    const void *newp, size_t newlen);

int
sysctlbyname(const char *name, void *oldp, size_t *oldlenp,
    const void *newp, size_t newlen);

int
sysctlnametomib(const char *name, int *mibp, size_t *sizep);
```

## 描述

`sysctl` 函数检索系统信息，并允许具有适当特权的进程设置系统信息。可从 `sysctl` 获取的信息由整数、字符串和表组成。可以使用 [sysctl(8)](../man8/sysctl.8.md) 实用程序从命令界面检索和设置信息。

除非下面明确注明，`sysctl` 返回所请求数据的一致快照。一致性是通过将目标缓冲区锁定在内存中获得的，以便可以无阻塞地复制出数据。对 `sysctl` 的调用会串行化以避免死锁。

状态使用 "Management Information Base"（MIB）风格的名称来描述，列在 `name` 中，它是一个 `namelen` 长度的整数数组。

`sysctlbyname` 函数接受名称的 ASCII 表示形式，并在内部查找整数名称向量。除此之外，它的行为与标准 `sysctl` 函数相同。

信息被复制到由 `oldp` 指定的缓冲区中。缓冲区的大小由 `oldlenp` 指定的位置在调用前给出，该位置在成功调用后以及返回错误码 ENOMEM 的调用后给出已复制的数据量。如果可用数据量大于所提供缓冲区的大小，则调用会提供缓冲区能容纳的尽可能多的数据，并返回错误码 ENOMEM。如果不需要旧值，`oldp` 和 `oldlenp` 应设置为 NULL。

可以通过在调用 `sysctl` 时为 `oldp` 传入 `NULL` 参数来确定可用数据的大小。可用数据的大小将返回到 `oldlenp` 所指向的位置。对于某些操作，空间量可能经常变化。对于这些操作，系统会尝试向上取整，使返回的大小足够大，以便随后调用时能返回数据。

要设置新值，将 `newp` 设置为指向长度为 `newlen` 的缓冲区，从中获取所请求的值。如果不设置新值，应将 `newp` 设置为 NULL，`newlen` 设置为 0。

`sysctlnametomib` 函数接受名称的 ASCII 表示形式，查找整数名称向量，并将数值表示返回到 `mibp` 所指向的 mib 数组中。mib 数组中的元素数量由 `sizep` 指定的位置在调用前给出，该位置在成功调用后给出已复制的条目数。生成的 `mib` 和 `size` 可用于后续 `sysctl` 调用中，以获取与所请求 ASCII 名称关联的数据。此接口供想要重复请求同一变量的应用程序使用（`sysctl` 函数的运行时间约为通过 `sysctlbyname` 函数发出的相同请求的三分之一）。`sysctlnametomib` 函数也可用于获取 mib 前缀，然后添加最后一个组件。例如，要获取 pid 小于 100 的进程的进程信息：

```c
int i, mib[4];
size_t len;
struct kinfo_proc kp;
/* 填写 mib 的前三个组件 */
len = 4;
sysctlnametomib("kern.proc.pid", mib, &len);
/* 获取并打印 pid < 100 的条目 */
for (i = 0; i < 100; i++) {
        mib[3] = i;
        len = sizeof(kp);
        if (sysctl(mib, 4, &kp, &len, NULL, 0) == -1)
                perror("sysctl");
        else if (len > 0)
                printkproc(&kp);
}
```

顶级名称在 `#include <sys/sysctl.h>` 中以 CTL_ 前缀定义，如下所示。下一级及更深层级在 此处列出的包含文件中找到，并在以下单独章节中描述。

| **名称** | **下一级名称** | **描述** |
| --- | --- | --- |
| `CTL_DEBUG` | sys/sysctl.h | 调试 |
| `CTL_VFS` | sys/mount.h | 文件系统 |
| `CTL_HW` | sys/sysctl.h | 通用 CPU、I/O |
| `CTL_KERN` | sys/sysctl.h | 高级内核限制 |
| `CTL_MACHDEP` | sys/sysctl.h | 机器相关 |
| `CTL_NET` | sys/socket.h | 网络 |
| `CTL_USER` | sys/sysctl.h | 用户级 |
| `CTL_VM` | vm/vm_param.h | 虚拟内存 |

例如，以下代码检索系统中允许的最大进程数：

```c
int mib[2], maxproc;
size_t len;
mib[0] = CTL_KERN;
mib[1] = KERN_MAXPROC;
len = sizeof(maxproc);
sysctl(mib, 2, &maxproc, &len, NULL, 0);
```

检索系统实用程序的标准搜索路径：

```c
int mib[2];
size_t len;
char *p;
mib[0] = CTL_USER;
mib[1] = USER_CS_PATH;
sysctl(mib, 2, NULL, &len, NULL, 0);
p = malloc(len);
sysctl(mib, 2, p, &len, NULL, 0);
```

### CTL_DEBUG

调试变量因系统而异。调试变量可以在不需要重新编译 `sysctl` 了解它的情况下添加或删除。每次运行时，`sysctl` 从内核获取调试变量列表并显示其当前值。系统定义了二十个（`struct ctldebug`）变量，名为 `debug0` 到 `debug19`。它们被声明为单独的变量，以便可以在其关联变量的位置单独初始化。加载器通过在变量在多个位置初始化时发出错误来防止同一变量的多次使用。例如，要将变量 `dospecialcheck` 导出为调试变量，将使用以下声明：

```c
int dospecialcheck = 1;
struct ctldebug debug5 = { "dospecialcheck", &dospecialcheck };
```

### CTL_VFS

一个特殊的第二级名称 VFS_GENERIC 用于获取关于所有文件系统的一般信息。其第三级标识符之一是 VFS_MAXTYPENUM，它给出最高有效的文件系统类型编号。其另一个第三级标识符是 VFS_CONF，它返回作为第四级标识符给出的文件系统类型的配置信息（参见 [getvfsbyname(3)](getvfsbyname.3.md) 作为其使用示例）。其余的第二级标识符是由 [statfs(2)](../sys/statfs.2.md) 调用或 VFS_CONF 返回的文件系统类型编号。每个文件系统可用的第三级标识符在定义该文件系统挂载参数结构的头文件中给出。
### CTL_HW

CTL_HW 级别可用的字符串和整数信息详述如下。可更改列显示具有适当特权的进程是否可以更改该值。

| **第二级名称** | **类型** | **可更改** |
| --- | --- | --- |
| `HW_MACHINE` | string | no |
| `HW_MODEL` | string | no |
| `HW_NCPU` | integer | no |
| `HW_BYTEORDER` | integer | no |
| `HW_PHYSMEM` | integer | no |
| `HW_USERMEM` | integer | no |
| `HW_PAGESIZE` | integer | no |
| `HW_FLOATINGPT` | integer | no |
| `HW_MACHINE_ARCH` | string | no |
| `HW_REALMEM` | integer | no |
| `HW_AVAILPAGES` | integer | no |

**`HW_MACHINE`** 机器类别。

**`HW_MODEL`** 机器型号。

**`HW_NCPU`** CPU 数量。

**`HW_BYTEORDER`** 字节序（4321 或 1234）。

**`HW_PHYSMEM`** 物理内存总量（字节），减去内核、预加载模块和（在 x86 上）dcons 缓冲区使用的内存。

**`HW_USERMEM`** 未被锁定的内存量（字节）。

**`HW_PAGESIZE`** 软件页面大小。

**`HW_FLOATINGPT`** 如果硬件支持浮点则为非零值。

**`HW_MACHINE_ARCH`** 机器相关的架构类型。

**`HW_REALMEM`** 固件报告的内存量（字节）。该值有时不正常；在这种情况下，内核报告最大内存地址。

**`HW_AVAILPAGES`** 与 `HW_PHYSMEM` 相同的值，以页而不是字节为单位衡量。

### CTL_KERN

CTL_KERN 级别可用的字符串和整数信息详述如下。可更改列显示具有适当特权的进程是否可以更改该值。当前可用的数据类型有进程信息、系统 vnode、打开文件条目、路由表条目、虚拟内存统计、负载平均历史和时钟频率信息。

| **第二级名称** | **类型** | **可更改** |
| --- | --- | --- |
| `KERN_ARGMAX` | integer | no |
| `KERN_ARND` | byte buffer | no |
| `KERN_BOOTFILE` | string | yes |
| `KERN_BOOTTIME` | struct timeval | no |
| `KERN_CLOCKRATE` | struct clockinfo | no |
| `KERN_FILE` | struct xfile | no |
| `KERN_HOSTID` | integer | yes |
| `KERN_HOSTUUID` | string | yes |
| `KERN_HOSTNAME` | string | yes |
| `KERN_IOV_MAX` | integer | no |
| `KERN_JOB_CONTROL` | integer | no |
| `KERN_LOCKF` | struct kinfo_lockf | no |
| `KERN_LOGSIGEXIT` | integer | yes |
| `KERN_MAXFILES` | integer | yes |
| `KERN_MAXFILESPERPROC` | integer | yes |
| `KERN_MAXPHYS` | integer | no |
| `KERN_MAXPROC` | integer | no |
| `KERN_MAXPROCPERUID` | integer | yes |
| `KERN_MAXVNODES` | integer | yes |
| `KERN_NGROUPS` | integer | no |
| `KERN_NISDOMAINNAME` | string | yes |
| `KERN_OSRELDATE` | integer | no |
| `KERN_OSRELEASE` | string | no |
| `KERN_OSREV` | integer | no |
| `KERN_OSTYPE` | string | no |
| `KERN_POSIX1` | integer | no |
| `KERN_PROC` | node | not applicable |
| `KERN_PS_STRINGS` | integer | no |
| `KERN_SAVED_IDS` | integer | no |
| `KERN_SECURELVL` | integer | raise only |
| `KERN_UPDATEINTERVAL` | integer | no |
| `KERN_USRSTACK` | integer | no |
| `KERN_VERSION` | string | no |

`#include <osreldate.h>`

| **第三级名称** | **第四级** |
| --- | --- |
| `KERN_PROC_ALL` | None |
| `KERN_PROC_PID` | A process ID |
| `KERN_PROC_PGRP` | A process group |
| `KERN_PROC_SESSION` | A session |
| `KERN_PROC_TTY` | A tty device |
| `KERN_PROC_UID` | effective user ID |
| `KERN_PROC_RUID` | A real user ID |
| `KERN_PROC_GID` | effective group ID |
| `KERN_PROC_RGID` | A real group ID |

| **第三级名称** | **第四级** |
| --- | --- |
| `KERN_PROC_ARGS` | Set of strings |
| `KERN_PROC_PATHNAME` | String |
| `KERN_PROC_KSTACK` | struct kinfo_stack [] |
| `KERN_PROC_VMMAP` | struct kinfo_vmentry [] |
| `KERN_PROC_FILEDESC` | struct kinfo_file [] |
| `KERN_PROC_GROUPS` | gid_t [] |
| `KERN_PROC_ENV` | Set of strings |
| `KERN_PROC_AUXV` | Elf_Auxinfo [] |
| `KERN_PROC_RLIMIT` | struct rlimit |
| `KERN_PROC_PS_STRINGS` | Pointer to struct ps_strings |
| `KERN_PROC_UMASK` | Integer/short |
| `KERN_PROC_OSREL` | Integer |
| `KERN_PROC_SIGTRAMP` | struct kinfo_sigtramp |
| `KERN_PROC_CWD` | struct kinfo_file |
| `KERN_PROC_NFDS` | Integer |
| `KERN_PROC_SIGFASTBLK` | Address |
| `KERN_PROC_VM_LAYOUT` | struct kinfo_vm_layout |
| `KERN_PROC_RLIMIT_USAGE` | rlim_t [] |
| `KERN_PROC_KQUEUE` | struct kinfo_knote [] |
**`KERN_PROC_ARGS`** 命令行参数数组以扁平化形式返回，即零终止的参数依次排列。返回数组的总大小。进程也可以通过这种方式设置自己的进程标题。

**`KERN_PROC_PATHNAME`** 返回进程文本文件的路径。

**`KERN_PROC_KSTACK`** 指定进程的线程的内核内调用栈。

**`KERN_PROC_VMMAP`** 进程的映射条目描述。另请参阅 kinfo_getvmmap(3)。

**`KERN_PROC_FILEDESC`** 指定进程中打开文件的描述符。另请参阅 kinfo_getfile(3)。

**`KERN_PROC_GROUPS`** 与进程关联的组。

**`KERN_PROC_ENV`** 表示指定进程环境的字符串集合。注意，从内核角度看，环境仅存在于 [execve(2)](../sys/execve.2.md) 系统调用时。此节点方法尝试从进程地址空间中留下的已知痕迹重建环境，但不保证成功或能表示程序维护的当前值。

**`KERN_PROC_AUXV`** ELF auxv 条目集合。参见上面关于环境的注释，该注释也适用于 auxv。

**`KERN_PROC_RLIMIT`** 必须提供额外的 OID 名称元素，按 [getrlimit(2)](../sys/getrlimit.2.md) 指定资源名称。调用返回该进程的给定资源限制。

**`KERN_PROC_PS_STRINGS`** 返回指定进程中最后一次调用 [execve(2)](../sys/execve.2.md) 时 `ps_strings` 结构的位置。

**`KERN_PROC_UMASK`** 当前 umask 值，参见 [umask(2)](../sys/umask.2.md)。

**`KERN_PROC_OSREL`** 进程的 osrel 值，即当前执行的镜像编译时所用的 osrel。在 [execve(2)](../sys/execve.2.md) 时从 elf 可执行文件的 note 中读取。可能被进程修改。

**`KERN_PROC_SIGTRAMP`** 描述进程地址空间中信号蹦床地址范围的结构，简而言之，内核在此传递控制权以进行信号传递。

**`KERN_PROC_CWD`** 返回进程的当前工作目录。

**`KERN_PROC_NFDS`** 返回进程打开的文件描述符总数。

**`KERN_PROC_SIGFASTBLK`** 如果处于活动状态，返回 [sigfastblock(2)](../sys/sigfastblock.2.md) 位置的地址。

**`KERN_PROC_VM_LAYOUT`** 填充描述进程虚拟地址空间布局的结构。

**`KERN_PROC_RLIMIT_USAGE`** 类似于 `KERN_PROC_RLIMIT`，但返回的是已计入的资源使用量而不是限制。如果 MIB 的形式为 `kern.proc.rlimit_usage.`pid`，则返回所有资源的使用值。如果 MIB 的形式为 `kern.proc.rlimit_usage.`pid`.`resource`，则返回指定资源的使用值。对于没有有意义的当前值的资源，返回 `-1`。

**`KERN_PROC_KQUEUE`** 填充描述向指定 kqueue 注册的事件的结构数组。接下来的两个节点值是 `pid` 和 `kqfd`，即要查询的进程的进程 ID 和该进程中 kqueue 的文件描述符。

**`KERN_ARGMAX`** [execve(2)](../sys/execve.2.md) 的最大参数字节数。

**`KERN_ARND`** arc4rand(9) 用内核内随机数据生成器产生的随机字节填充缓冲区。这是 [read(2)](../sys/read.2.md) [random(4)](../man4/random.4.md) 设备的替代接口，不依赖于 [devfs(4)](../man4/devfs.4.md) 节点的可访问性和正确的挂载选项。

**`KERN_BOOTFILE`** 内核加载文件的完整路径名。

**`KERN_BOOTTIME`** 返回 `struct timeval` 结构。此结构包含系统启动的时间。

**`KERN_CLOCKRATE`** 返回 `struct clockinfo` 结构。此结构包含时钟、统计时钟和性能分析时钟频率、每个 hz tick 的微秒数和偏斜率。

**`KERN_FILE`** 返回整个文件表。返回数据由 `struct xfile` 数组组成，其大小取决于系统中此类对象的当前数量。

**`KERN_HOSTID`** 获取或设置主机 ID。

**`KERN_HOSTUUID`** 获取或设置主机的通用唯一标识符（UUID）。

**`KERN_HOSTNAME`** 获取或设置主机名。

**`KERN_IOV_MAX`** 输入输出向量（iovec）中接受的最大元素数，参见 readv(2) 和 writev(2)。

**`KERN_JOB_CONTROL`** 如果此系统上有作业控制可用则返回 1，否则返回 0。

**`KERN_LOCKF`** 返回内核当前已知的文件建议锁列表。

**`KERN_LOGSIGEXIT`** 控制因未捕获信号导致的进程退出的日志记录。

**`KERN_MAXFILES`** 系统中可能打开的最大文件数。

**`KERN_MAXFILESPERPROC`** 单个进程可能打开的最大文件数。此限制仅适用于在打开请求时有效 uid 为非零的进程。如果限制或有效 uid 发生更改，已打开的文件不受影响。

**`KERN_MAXPHYS`** 指定最大块 I/O 大小。可通过可调参数 `kern.maxphys` 更改。

**`KERN_MAXPROC`** 系统允许的最大并发进程数。

**`KERN_MAXPROCPERUID`** 系统允许单个有效 uid 的最大并发进程数。此限制仅适用于在 fork 请求时有效 uid 为非零的进程。如果限制发生更改，已启动的进程不受影响。

**`KERN_MAXVNODES`** 系统上可用的最大 vnode 数。

**`KERN_NGROUPS`** 最大补充组数。

**`KERN_NISDOMAINNAME`** 当前 YP/NIS 域的名称。

**`KERN_OSRELDATE`** 内核发布版本，格式为 `M``mm``file``xx`，其中 `M` 是主版本号，`mm` 是两位数的次版本号，`file` 如果是发布分支则为 0，否则为 1，`xx` 在可用 API 变更时更新。如果需要获取当前安装的 userland 的发布版本，可从解析此文件获得 userland 发布版本。

**`KERN_OSRELEASE`** 系统发布字符串。

**`KERN_OSREV`** 系统修订号。

**`KERN_OSTYPE`** 系统类型字符串。

**`KERN_POSIX1`** 系统尝试遵循的 IEEE Std 1003.1 ("POSIX.1") 版本。

**`KERN_PROC`** 返回有关特定运行进程的选择信息。对于以下名称，返回 `struct kinfo_proc` 结构数组，其大小取决于系统中此类对象的当前数量。对于以下名称，返回有关目标进程的杂项信息，该进程由 oid 名称的第四级指定。进程 ID 为 `-1` 表示当前进程。

**`KERN_PS_STRINGS`** 报告 exec 之后进程 `ps_strings` 结构的位置，用于查询进程的 ABI。

**`KERN_SAVED_IDS`** 如果保存的设置组 ID 和保存的设置用户 ID 可用则返回 1。

**`KERN_SECURELVL`** 系统安全级别。具有适当特权的进程可以提升此级别。但不能降低。

**`KERN_USRSTACK`** 报告当前进程主线程用户栈的顶部。

**`KERN_VERSION`** 系统版本字符串。
### CTL_NET

CTL_NET 级别可用的字符串和整数信息详述如下。可更改列显示具有适当特权的进程是否可以更改该值。

| **第二级名称** | **类型** | **可更改** |
| --- | --- | --- |
| `PF_ROUTE` | routing messages | no |
| `PF_INET` | IPv4 values | yes |
| `PF_INET6` | IPv6 values | yes |

| **第五级** | **第六级** | **第七级** |
| --- | --- | --- |
| `NET_RT_FLAGS` | rtflags | None |
| `NET_RT_DUMP` | None | None or fib number |
| `NET_RT_IFLIST` | 0 or if_index | None |
| `NET_RT_IFMALIST` | 0 or if_index | None |
| `NET_RT_IFLISTL` | 0 or if_index | None |
| `NET_RT_NHOPS` | None | fib number |

| **协议** | **变量** | **类型** | **可更改** |
| --- | --- | --- | --- |
| icmp | bmcastecho | integer | yes |
| icmp | maskrepl | integer | yes |
| ip | forwarding | integer | yes |
| ip | redirect | integer | yes |
| ip | ttl | integer | yes |
| udp | checksum | integer | yes |

**`icmp.bmcastecho`** 如果要应答发送到广播或多播地址的 ICMP 回显请求则返回 1。

**`icmp.maskrepl`** 如果要应答 ICMP 网络掩码请求则返回 1。

**`ip.forwarding`** 当主机启用 IP 转发时返回 1，意味着主机充当路由器。

**`ip.redirect`** 当主机可以发送 ICMP 重定向时返回 1。除非主机正在路由 IP 数据包，否则此选项被忽略，并且应在所有系统上正常启用。

**`ip.ttl`** 系统产生的 IP 数据包的最大生存时间（跳数）值。此值适用于正常传输协议，不适用于 ICMP。

**`udp.checksum`** 当正在计算和检查 UDP 校验和时返回 1。强烈建议不要禁用 UDP 校验和。关于变量 net.inet.*.ipsec，请参阅 [ipsec(4)](../man4/ipsec.4.md)。

**`PF_ROUTE`** 返回整个路由表或其子集。数据以路由消息序列的形式返回（参见 [route(4)](../man4/route.4.md) 了解头文件、格式和含义）。每条消息的长度包含在消息头中。第三级名称是协议号，当前始终为 0。第四级名称是地址族，可设置为 0 以选择所有地址族。第五、第六和第七级名称如下：如果指定 0，`NET_RT_IFMALIST` 名称返回所有接口上的多播组成员身份信息，或返回由 `if_index` 指定的接口的信息。`NET_RT_IFLISTL` 类似于 `NET_RT_IFLIST`，只是返回带有附加字段的消息头结构，允许扩展接口而不破坏二进制兼容性。`NET_RT_IFLISTL` 使用消息头结构的 'l' 版本：`struct if_msghdrl` 和 `struct ifa_msghdrl`。`NET_RT_NHOPS` 返回给定 fib 中指定地址族的所有下一跳。

**`PF_INET`** 获取或设置关于 IPv4（Internet Protocol version 4）的各种全局信息。第三级名称是协议。第四级名称是变量名。当前定义的协议和名称如下：变量如下：

**`PF_INET6`** 获取或设置关于 IPv6（Internet Protocol version 6）的各种全局信息。第三级名称是协议。第四级名称是变量名。关于变量 net.inet6.* 请参阅 [inet6(4)](../man4/inet6.4.md)。关于变量 net.inet6.*.ipsec6，请参阅 [ipsec(4)](../man4/ipsec.4.md)。

### CTL_USER

CTL_USER 级别可用的字符串和整数信息详述如下。可更改列显示具有适当特权的进程是否可以更改该值。

| **第二级名称** | **类型** | **可更改** |
| --- | --- | --- |
| `USER_BC_BASE_MAX` | integer | no |
| `USER_BC_DIM_MAX` | integer | no |
| `USER_BC_SCALE_MAX` | integer | no |
| `USER_BC_STRING_MAX` | integer | no |
| `USER_COLL_WEIGHTS_MAX` | integer | no |
| `USER_CS_PATH` | string | no |
| `USER_EXPR_NEST_MAX` | integer | no |
| `USER_LINE_MAX` | integer | no |
| `USER_LOCALBASE` | string | no |
| `USER_POSIX2_CHAR_TERM` | integer | no |
| `USER_POSIX2_C_BIND` | integer | no |
| `USER_POSIX2_C_DEV` | integer | no |
| `USER_POSIX2_FORT_DEV` | integer | no |
| `USER_POSIX2_FORT_RUN` | integer | no |
| `USER_POSIX2_LOCALEDEF` | integer | no |
| `USER_POSIX2_SW_DEV` | integer | no |
| `USER_POSIX2_UPE` | integer | no |
| `USER_POSIX2_VERSION` | integer | no |
| `USER_RE_DUP_MAX` | integer | no |
| `USER_STREAM_MAX` | integer | no |
| `USER_TZNAME_MAX` | integer | no |

**`USER_BC_BASE_MAX`** [bc(1)](../man1/bc.1.md) 实用程序中的最大 ibase/obase 值。

**`USER_BC_DIM_MAX`** [bc(1)](../man1/bc.1.md) 实用程序中的最大数组大小。

**`USER_BC_SCALE_MAX`** [bc(1)](../man1/bc.1.md) 实用程序中的最大比例值。

**`USER_BC_STRING_MAX`** [bc(1)](../man1/bc.1.md) 实用程序中的最大字符串长度。

**`USER_COLL_WEIGHTS_MAX`** 在区域定义文件中可分配给 LC_COLLATE order 关键字任何条目的最大权重数。

**`USER_CS_PATH`** 返回一个 `PATH` 环境变量的值，用于查找所有标准实用程序。

**`USER_EXPR_NEST_MAX`** expr(1) 实用程序中括号内可嵌套的最大表达式数。

**`USER_LINE_MAX`** 文本处理实用程序输入行的最大长度（字节）。

**`USER_LOCALBASE`** 返回已编译到需要访问 port 或 package 提供的资源的系统实用程序中的 localbase 值。

**`USER_POSIX2_CHAR_TERM`** 如果系统支持至少一种能够执行 IEEE Std 1003.2 ("POSIX.2") 中描述的所有操作的终端类型则返回 1，否则返回 0。

**`USER_POSIX2_C_BIND`** 如果系统的 C 语言开发设施支持 C 语言绑定选项则返回 1，否则返回 0。

**`USER_POSIX2_C_DEV`** 如果系统支持 C 语言开发实用程序选项则返回 1，否则返回 0。

**`USER_POSIX2_FORT_DEV`** 如果系统支持 FORTRAN 开发实用程序选项则返回 1，否则返回 0。

**`USER_POSIX2_FORT_RUN`** 如果系统支持 FORTRAN 运行时实用程序选项则返回 1，否则返回 0。

**`USER_POSIX2_LOCALEDEF`** 如果系统支持区域创建则返回 1，否则返回 0。

**`USER_POSIX2_SW_DEV`** 如果系统支持软件开发实用程序选项则返回 1，否则返回 0。

**`USER_POSIX2_UPE`** 如果系统支持用户可移植性实用程序选项则返回 1，否则返回 0。

**`USER_POSIX2_VERSION`** 系统尝试遵循的 IEEE Std 1003.2 ("POSIX.2") 版本。

**`USER_RE_DUP_MAX`** 使用区间表示法时允许的正则表达式重复出现的最大次数。

**`USER_STREAM_MAX`** 进程在任何时候可能打开的最小最大流数。

**`USER_TZNAME_MAX`** 时区名称支持的最小最大类型数。

### CTL_VM

CTL_VM 级别可用的字符串和整数信息详述如下。可更改列显示具有适当特权的进程是否可以更改该值。

| **第二级名称** | **类型** | **可更改** |
| --- | --- | --- |
| `VM_LOADAVG` | struct loadavg | no |
| `VM_TOTAL` | struct vmtotal | no |
| `VM_SWAPPING_ENABLED` | integer | maybe |
| `VM_V_FREE_MIN` | integer | yes |
| `VM_V_FREE_RESERVED` | integer | yes |
| `VM_V_FREE_TARGET` | integer | yes |
| `VM_V_INACTIVE_TARGET` | integer | yes |
| `VM_V_PAGEOUT_FREE_MIN` | integer | yes |
| `VM_OVERCOMMIT` | integer | yes |

**`VM_LOADAVG`** 返回负载平均历史。返回数据由 `struct loadavg` 组成。

**`VM_TOTAL`** 返回系统范围的虚拟内存统计。返回数据由 `struct vmtotal` 组成。

**`VM_SWAPPING_ENABLED`** 如果启用进程交换则为 1，如果禁用则为 0。如果内核在构建时禁用了交换，此变量永久设置为 0。

**`VM_V_FREE_MIN`** 在等待内存的进程被唤醒之前，需要可用的最小内存量（缓存内存加空闲内存）。

**`VM_V_FREE_RESERVED`** 如果空闲和缓存页数降至低于此值，进程将唤醒 pageout 守护进程并等待内存。

**`VM_V_FREE_TARGET`** pageout 守护进程尝试维持的空闲内存总量（包括缓存内存）。

**`VM_V_INACTIVE_TARGET`** pageout 守护进程运行时应达到的非活动页的期望数量。非活动页可以在需要时快速插入到进程地址空间中。

**`VM_V_PAGEOUT_FREE_MIN`** 如果空闲和缓存内存量降至低于此值，pageout 守护进程将进入"内存保守模式"以避免死锁。

**`VM_OVERCOMMIT`** 超量提交行为，如 [tuning(7)](../man7/tuning.7.md) 中所述。
## 返回值

如果成功，返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 文件

**sys/sysctl.h** 顶级标识符、第二级内核和硬件标识符以及用户级标识符的定义
**sys/socket.h** 第二级网络标识符的定义
**sys/gmon.h** 第三级性能分析标识符的定义
**vm/vm_param.h** 第二级虚拟内存标识符的定义
**netinet/in.h** 第三级 IPv4/IPv6 标识符和第四级 IPv4/v6 标识符的定义
**netinet/icmp_var.h** 第四级 ICMP 标识符的定义
**netinet/icmp6.h** 第四级 ICMPv6 标识符的定义
**netinet/udp_var.h** 第四级 UDP 标识符的定义

## 错误

可能报告以下错误：

**[`EFAULT`]** 缓冲区 `name`、`oldp`、`newp` 或长度指针 `oldlenp` 包含无效地址。

**[`EINVAL`]** `name` 数组少于两个或多于 CTL_MAXNAME。

**[`EINVAL`]** 给定了非空的 `newp`，且其在 `newlen` 中指定的长度太大或太小。

**[`ENOMEM`]** `oldlenp` 所指向的长度太短，无法容纳所请求的值。

**[`ENOMEM`]** `oldlenp` 所指向的长度或返回数据的估计大小中较小者超过系统锁定内存限制。

**[`ENOMEM`]** 锁定缓冲区 `oldp`，或如果要返回的数据的估计大小较小时锁定缓冲区的一部分，会导致进程超过其每进程锁定内存限制。

**[`ENOTDIR`]** `name` 数组指定的是中间名称而非终端名称。

**[`EISDIR`]** `name` 数组指定的是终端名称，但实际名称不是终端的。

**[`ENOENT`]** `name` 数组指定了一个未知的值。

**[`EPERM`]** 尝试设置只读值。

**[`EPERM`]** 没有适当特权的进程尝试设置值。

## 参见

[confstr(3)](confstr.3.md), kinfo_getproc(3), kvm(3), [sysconf(3)](sysconf.3.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`sysctl` 函数首次出现于 4.4BSD。
