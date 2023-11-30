   HIER(7)  

HIER(7)

FreeBSD Miscellaneous Information Manual

HIER(7)

名称
==

`hier` — 文件系统布局

描述
==

文件系统层次结构草图。

/

文件系统的根目录

/bin/

单用户和多用户环境的基本用户实用程序

/boot/

操作系统启动时使用的程序和配置文件

defaults/

默认引导配置文件；参见 loader.conf(5)

dtb/

编译后的扁平化设备树 (FDT) 文件；请参见 fdt(4) 和 dtc(1)

efi/

UEFI 系统上 EFI 系统分区 (ESP) 的挂载点

firmware/

可加载的内核模块，包含二进制固件，用于需要下载固件才能运行的硬件

kernel/

纯内核可执行文件（启动时加载到内存中的操作系统）和内核模块

modules/

第三方可加载内核模块，例如从 ports(7) 安装的模块

overlays/

编译后的扁平化设备树（FDT）覆盖；参见 fdt(4) 和 dtc(1)

zfs/

zfs(8) zpool 缓存文件

/cdrom/

光盘驱动器的默认挂载点

/compat/

通常是指向 /usr/compat 的链接。如果不是，则适用 /usr/compat 注释

/dev/

由 devfs(5) 管理的设备特殊文件

fd/

文件描述符文件；参见 fd(4)

/etc/

系统配置文件和脚本

defaults/

系默认系统配置文件；参见统配置文件和脚本 rc(8)

bluetooth/

蓝牙配置文件

localtime

本地时区信息；参见 ctime(3)

mail/

Sendmail 控制文件

mtree/

mtree 配置文件；参见 mtree(8)

pam.d/

可插拔验证模块（PAM）库的配置文件

periodic/

通过 cron(8) 每天、每周和每月运行的脚本；请参阅 periodic(8)

rc.d/

系统和守护进程启动/控制脚本；参见 rc(8)

security/

OpenBSM 审计配置文件；参见 audit(8)

ppp/

ppp 配置文件；参见 ppp(8)

ssh/

OpenSSH 配置文件；参见 ssh(1)

ssl/

OpenSSL 配置文件

/lib/

/bin 和 /sbin 中的二进制文件所需的关键系统库

casper/

特定于服务的 libcasper(3) Capsicum 支持库

geom/

geom(8) 工具的特定类库

nvmecontrol/

用于扩展 nvmecontrol(8) 工具的特定于供应商的库

/libexec/

/bin 和 /sbin 中的二进制文件所需的关键系统实用程序

/media/

包含子目录，可用作光盘、USB 驱动器和软盘等可移动媒体的挂载点

/mnt/

系统管理员通常用作临时挂载点的空目录

/net/

自动挂载的 NFS 共享；请参阅 auto\_master(5)

/proc/

进程文件系统；请参阅 procfs(5)

/rescue/

用于紧急恢复的静态链接程序；参见 rescue(8)

/root/

根目录

/sbin/

单用户和多用户环境下的基本系统程序和管理工具

/tmp/

不能保证在系统重启时仍然存在的临时文件

/usr/

包含大部分用户实用程序和应用程序

bin/

常用实用程序、编程工具和应用程序

compat/

支持与其他操作系统二进制兼容所需的文件；参见 linux(4)

include/

标准 C 包含文件

arpa/

互联网服务协议的 C 包含文件

bsnmp/

用于 SNMP 守护进程的 C 包含文件

c++/

C++ 包含文件

cam/

通用访问方法层的 C 语言包含文件

scsi/

CAM 上的 SCSI 设备

dev/

用于编程各种 FreeBSD 设备的 C 包含文件

ic/

描述与驱动程序和总线无关的硬件电路的各种头文件

ofw/

开放固件支持

pbio/

8255 PPI 卡；见 pbio(4)

ppbus/

并行端口总线；参见 ppbus(4)

usb/

USB 子系统

fs/

fdescfs/

每个进程的文件描述符文件系统

msdosfs/

MS-DOS 文件系统

nfs/

用于 NFS（网络文件系统）版本 2、3 和 4 的 C 包含文件

nullfs/

回环文件系统

procfs/

进程文件系统

smbfs/

SMB/CIFS 文件系统

udf/

UDF 文件系统

unionfs

联合文件系统

geom/

GEOM 框架

concat/

CONCAT GEOM 类

gate/

GATE GEOM 类

mirror/

MIRROR GEOM 类

nop/

NOP GEOM 类

raid3/

RAID3 GEOM 类

stripe/

STRIPE GEOM 类

libmilter/

用于 sendmail(8) 邮件过滤 API libmilter 的 C 包含文件

machine/

特定机器的 C 包含文件

net/

杂项网络 C 包含文件

altq/

用于交替排队的 C 包含文件

net80211/

用于 802.11 无线网络的 C 语言包含文件；参见 net80211(4)

netinet/

用于互联网标准协议的 C 语言包含文件；参见 inet(4)

netinet6/

互联网协议版本 6 的 C 语言包含文件；参见 inet6(4)

netipsec/

内核密钥管理服务；参见 ipsec(4)

netsmb/

SMB/CIFS 请求器

nfs/

用于 NFS（网络文件系统）版本 2 和 3（传统）的 C 包含文件

openssl/

OpenSSL （密码学/SSL 工具包）头文件

protocols/

伯克利服务协议的 C 包含文件

rpc/

远程过程调用；参见 rpc(3)

rpcsvc/

远程过程调用服务结构的定义；参见 rpc(3)

security/

PAM; 参见 pam(8)

sys/

系统 C 包括文件（内核数据结构）

ufs/

用于 UFS（U 字文件系统）的 C 包含文件

ffs/

快速文件系统

ufs/

UFS 文件系统

vm/

虚拟内存；参见 vmstat(8)

lib/

共享和归档 ar(1)\-type 类型库

aout/

a.out 存档库

compat/

用于兼容的共享库

aout/

a.out 向后兼容库

debug/

内核和基本系统库及二进制文件的独立调试数据

dtrace/

DTrace 库脚本

engines/

OpenSSL （密码学/SSL 工具包）动态加载引擎

libdata/

杂项实用程序数据文件

gcc/

gcc(1) 配置数据

ldscripts/

链接器脚本；参见 ld(1)

libexec/

系统守护进程和系统实用程序（由其他程序执行）

aout/

操作 a.out 可执行文件的实用程序

elf/

操作 ELF 可执行文件的实用程序

lpr/

用于 LP 打印系统的实用程序和过滤器；参见 lpr(1)

sendmail/

sendmail(8) 二进制文件；参见 mailwrapper(8)

sm.bin/

用于 sendmail(8) 的限制 shell；参见 smrsh(8)

local/

本地可执行文件、库等。也用作 ports(7) 框架的默认目标。在 local/ 中，应使用 `hier` 为 /usr 画的一般布局。ports 文档 (share/doc/<port>/) 和 /usr/local/etc (mimics 模仿 /etc) 除外。

obj/

通过构建 /usr/src 目录生成的特定于体系结构的目标树

ports/

ports(7), FreeBSD 移植程序集

sbin/

系统守护进程和系统实用程序（由用户执行）

share/

与体系结构无关的文件

calendar/

各种预制日历文件；参见 calendar(1)

dict/

单词表；参见 look(1)

freebsd

FreeBSD专用术语、专有名词和行话

web2

韦氏第二国际词典中的单词

doc/

杂项文档；大部分印刷版 BSD 手册的来源（可从 USENIX 协会获取）

FAQ/

常见问题

IPv6/

实施说明

es/

/usr/share/doc中文件的西班牙语翻译

handbook/

FreeBSD 手册

ja/

/usr/share/doc中文件的日语翻译

legal/

供应商提供的固件文件的许可证文件

ncurses/

有关 ncurses 的 HTML 文档；参见 ncurses(3)

ntp/

与网络时间协议有关的 HTML 文档

ru/

/usr/share/doc 文件的俄语翻译

tutorials/

FreeBSD 教程

zh/

/usr/share/doc 中文档的中文翻译

examples/

为用户和程序员提供的各种示例

firmware/

用户程序加载的固件映像

games/

各种游戏使用的 ASCII 文本文件

keys/

已知的受信任和已撤销密钥。

pkg/

用于 pkg(7) 和 pkg(8) 的指纹

locale/

本地化文件；参见 setlocale(3)

man/

手册页面

misc/

杂项系统 ASCII 文本文件

fonts/

???

termcap

终端特性数据库；参见 termcap(5)

mk/

用于 make 的模板；参见 make(1)

nls/

国家语言支持文件

security/

安全策略的数据文件，如 mac\_lomac(4)

sendmail/

sendmail(8) 配置文件

skel/

用于新账户的示例 . （点）文件

snmp/

用于 SNMP 守护进程的 MIB、示例文件和树定义。

defs/

与 gensnmptree(1) 一起使用的树定义文件

mibs/

MIB 文件

syscons/

使用的文件；参见 syscons(4)

fonts/

控制台字体；参见 vidcontrol(1) 和 vidfont(1)

keymaps/

控制台键盘映射；请参见 kbdcontrol(1) 和 kbdmap(1)

scrnmaps/

控制台屏幕地图

tabset/

各种终端的选项卡描述文件；用于 termcap 文件；参见 termcap(5)

vi/

vi(1) 的本地化支持和实用程序

vt/

vt 使用的文件；参见 vt(4)

fonts/

控制台字体；参见 vidcontrol(1) 和 vidfont(1)

keymaps/

控制台键盘映射；请参见 kbdcontrol(1) 和 kbdmap(1)

zoneinfo/

时区配置信息；参见 tzfile(5)

src/

FreeBSD 源代码

bin/

/bin 中文件的源代码

cddl/

通用开发和发布许可证涵盖的实用程序

contrib/

贡献软件的源代码

crypto/

贡献的密码学软件的源代码

etc/

/etc 文件的源代码

gnu/

GNU 通用公共许可证涵盖的实用程序

include/

/usr/include 文件的源代码

kerberos5/

为 Kerberos 版本 5 构建基础架构

lib/

/lib 和 /usr/lib 中文件的源代码

libexec/

/usr/libexec 中文件的源代码

release/

生成 FreeBSD 发行版所需的文件

rescue/

/rescue 中文件的源代码

sbin/

/sbin 中文件的源代码

secure/

/usr/src/crypto 中文件的构建目录

share/

/usr/share 中文件的源代码

stand/

引导加载器源代码

sys/

内核源代码

amd64/

AMD64 架构支持

arm/

ARM 架构支持

arm64/

ARMv8 架构支持

cam/

cam(4) 和 ctl(4)

cddl/

CDDL 许可的可选源代码，包括 ZFS 和 DTrace

ddb/

ddb(4)

fs/

大多数文件系统

dev/

设备驱动程序

geom/

geom(4)

i386/

支持 i386（32 位）架构

kern/

内核的主要部分

mips/

MIPS 架构支持

net80211/

net80211(4)

netgraph/

netgraph(4)

netinet/

inet(4)

netinet6/

inet6(4)

netipsec/

ipsec(4)

netpfil/

ipfw(4) and pf(4)

opencrypto/

crypto(7)

powerpc/

PowerPC/POWER 架构支持

riscv/

RISC-V 架构支持

security/

audit(4) and mac(4)

sparc64/

SPARC64 架构支持

sys/

内核头文件

ufs/

Unix 文件系统

x86/

AMD64 和 i386 架构共享的代码

targets/

支持试验性 DIRDEPS\_BUILD

tests/

/usr/tests 中文件的源代码

tools/

用于维护和测试 FreeBSD 的工具

usr.bin/

/usr/bin 中文件的源代码

usr.sbin/

/usr/sbin 中文件的源代码

tests/

FreeBSD 测试套件；参见 tests(7)

/var/

多用途日志、临时、暂存和 spool 文件

account/

系统会计文件

acct

执行会计文件；见 acct(5)

at/

定时命令调度文件；见 at(1)

jobs/

包含任务文件的目录

spool/

包含输出线轴文件的目录

backups/

杂项备份文件

cache/

各种缓存文件

pkg/

缓存的 pkg(8) 软件包

crash/

存储内核崩溃转储的默认目录；参见 crash(8) 和 savecore(8)

cron/

使用的文件；参见 cron(8)

tabs/

文件；请参见 crontab(5)

db/

自动生成的系统专用数据库文件

empty/

空目录，供需要特定空目录的程序使用。例如， sshd(8) 用于权限分离。

games/

杂项游戏状态和分数文件

heimdal/

Kerberos 服务器数据库；参见 kdc(8)

log/

杂项系统日志文件

utx.lastlogin

最后登录日志；参见 getutxent(3)

utx.log

登录/注销日志；参见 getutxent(3)

mail/

用户邮箱文件

msgs/

系统消息数据库；参见 msgs(1)

preserve/

编辑者意外死亡后保存文件的临时存放处；参见 ex(1)

quotas/

文件系统配额信息文件

run/

描述系统启动后各种信息的系统信息文件

ppp/

可由 “network” 组写，用于命令连接套接字；参见 ppp(8)

utx.active

当前用户数据库；参见 getutxent(3)

rwho/

数据文件；参见 rwhod(8), rwho(1) 和 ruptime(1)

spool/

-
杂项打印机和邮件系统线轴目录

clientmqueue/

未投递的提交邮件队列；参见 sendmail(8)

ftp/

通常为 ~ftp；匿名 ftp 根目录

mqueue/

未投递邮件队列；参见 sendmail(8)

output/

行式打印机线轴目录

tmp/

系统重启时保留的临时文件

vi.recover/

存储恢复文件的目录

yp/

NIS 地图

注释
==

本手册记录了 FreeBSD 默认的文件系统布局，但系统上的实际层次结构由系统管理员自行决定。维护良好的安装系统将包含本文档的定制版本。

参见
==

apropos(1), find(1), finger(1), grep(1), ls(1), whatis(1), whereis(1), which(1), fd(4), devfs(5), fsck(8)

历史
==

Version 7 AT&T UNIX 中出现了 `hier` 手册页面。

January 9, 2021

FreeBSD 13.2-RELEASE