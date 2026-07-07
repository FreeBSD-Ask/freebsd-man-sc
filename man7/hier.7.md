# hier(7)

`hier` — 文件系统层次结构索引

## 名称

`hier` FreeBSD 文件系统层次结构

## 描述

**`overlays/`** 已编译的 [fdt(4)](../man4/fdt.4.md) 覆盖；参见 loader.conf(5) 中的 `fdt_overlays`

**`defaults/`** 默认引导配置文件；参见 loader.conf(5)
**`device.hints`** 用于控制驱动程序的内核变量；参见 [device.hints(5)](../man5/device.hints.5.md)
**`dtb/`** 已编译的扁平设备树（FDT）文件；参见 [fdt(4)](../man4/fdt.4.md) 和 dtc(1)
**`efi/`** [uefi(8)](../man8/uefi.8.md) EFI 系统分区（ESP）挂载点
**`firmware/`** 可加载的二进制固件内核模块
**`fonts/`** 二进制位图控制台字体；参见 loader.conf(5) 和 vtfontcvt(8)
**`images/`** beastie 引导菜单图像；参见 loader_lua(8)
**`kernel/`** FreeBSD 内核和模块；参见 [kldstat(8)](../man8/kldstat.8.md)
**`kernel.old/`** 备用内核和模块
**`loader.conf`** 引导加载器配置；参见 loader.conf(5)
**`loader.conf.d/`** loader.conf(5) 配置文件
**`lua/`** Lua 引导加载器的脚本；参见 loader_lua(8)
**`modules/`** 第三方可加载内核模块，例如使用 [pkg(8)](../man8/pkg.8.md) 安装的模块或来自 [ports(7)](ports.7.md) 的模块
**`zfs/`** ZFS zpool(8) 缓存文件

**`linux/`** [linux(4)](../man4/linux.4.md) 兼容运行时的默认位置

**`ada0`** 第一个 ATA 存储设备
**`ada0p1`** ada0 上的第一个分区
**`cd0`** 第一个光驱
**`cuaU0`** 第一个 USB 串口；参见 cu(1)
**`da0`** 第一个 SCSI 存储设备
**`da0s1`** da0 上的第一个分区
**`dri/`** GPU 字符设备节点；参见 drm(7)
**`drm/`** GPU drm(7) 特殊文件
**`fd/`** 文件描述符文件；参见 [fd(4)](../man4/fd.4.md)
**`fd0`** 第一个软盘驱动器
**`gpt/`** 按 GPT 标签的存储分区
**`mmcsd0`** 第一个 SD 存储设备
**`mmcsd0s1`** mmcsd0 上的第一个分区
**`nda0`** 通过 cam(3) 连接的第一个 NVMe 存储设备
**`null`** 接受任何内容但不包含任何内容的无限循环
**`nvd0`** 使用 NVMe 命名空间的第一个 NVMe 存储设备
**`pts/`** 伪终端；参见 [pts(4)](../man4/pts.4.md)
**`random`** 弱随机源；参见 [random(4)](../man4/random.4.md)
**`sa0`** 第一个磁带驱动器
**`usb/`** USB 总线
**`vmm/`** 活动的 [bhyve(8)](../man8/bhyve.8.md) 虚拟机
**`zvol/`** [zfs(8)](../man8/zfs.8.md) 卷

**`aliases`** 用于投递系统邮件的地址
**`mailer.conf`** mailwrapper(8) 配置

**`cert.pem`** 捆绑形式的系统信任库；参见 certctl(8)。
**`certs/`** OpenSSL 哈希目录形式的系统信任库；参见 certctl(8)。
**`openssl.cnf`** OpenSSL 配置文件；参见 openssl.cnf(5)。
**`untrusted/`** 显式不信任的证书；参见 certctl(8)。

**`auto_master`** autofs automount(8) 配置
**`bluetooth/`** 蓝牙配置文件
**`cron.d/`** 用于驱动计划任务的表；参见 crontab(5)
**`crontab`** root 的 cron 表
**`defaults/`** 默认系统配置文件；参见 [rc(8)](../man8/rc.8.md)
**`devd/`** devd(8)（设备状态变更守护进程）的配置
**`devfs.conf`** 引导时的设备配置
**`dma/`** dma(8) 的配置
**`freebsd-update.conf`** 基本系统更新器的配置；参见 [freebsd-update(8)](../man8/freebsd-update.8.md)
**`fstab`** 静态文件系统配置；参见 [fstab(5)](../man5/fstab.5.md)
**`hosts`** 当没有网络名称服务器运行时的本地主机数据库
**`inetd.conf`** BSD 传统的 Internet 服务器配置；参见 [inetd(8)](../man8/inetd.8.md)
**`localtime`** 本地时区信息；参见 ctime(3)
**`jail.conf.d/`** [jail(8)](../man8/jail.8.md) 启动脚本
**`login.conf`** 登录类能力数据库；参见 login.conf(5)
**`machine-id`** 定义本地系统的 UUID，dbus 所需
**`mail/`** sendmail(8) 控制文件
**`motd.template`** tty 登录时显示的消息；参见 [motd(5)](../man5/motd.5.md)
**`mtree/`** 系统映射规范；参见 [mtree(8)](../man8/mtree.8.md)
**`newsyslog.conf.d/`** 日志轮转配置文件。
**`ntp/`** 网络时间协议的存储时间
**`ntp.conf`** NTP 客户端 ntpd(8) 的配置
**`pam.d/`** 可插拔认证模块（PAM）库的配置文件；参见 pam(3)
**`periodic/`** 由 cron(8) 每天、每周或每月运行的脚本；参见 [periodic(8)](../man8/periodic.8.md)
**`pf.conf`** Packet Filter 防火墙的配置；参见 [pf(4)](../man4/pf.4.md)
**`pkg/`** 软件包管理器 [pkg(8)](../man8/pkg.8.md) 的默认配置
**`ppp/`** PPP 配置文件；参见 ppp(8)
**`rc.conf`** 系统和守护进程配置；参见 [rc.conf(5)](../man5/rc.conf.5.md)
**`rc.d/`** 系统和守护进程启动/控制脚本；参见 [rc(8)](../man8/rc.8.md)
**`resolv.conf`** DNS 配置；参见 resolv.conf(5)
**`resolvconf.conf`** DNS 配置管理器配置，通常由 local-unbound 生成；参见 local-unbound(8) 或 resolvconf(8)
**`security/`** OpenBSM 审计配置文件；参见 audit(8)
**`ssh/`** OpenSSH 配置文件；参见 [ssh(1)](../man1/ssh.1.md)
**`ssl/`** OpenSSL 配置文件
**`sysctl.conf`** 内核状态默认值；参见 [sysctl.conf(5)](../man5/sysctl.conf.5.md)
**`syslog.conf`** 系统消息日志配置
**`ttys`** tty 创建配置；参见 getty(8)
**`wpa_supplicant.conf`** 客户端 wifi 配置；参见 wpa_supplicant.conf(5)

**`geom/`** geom(8) 实用程序的类特定库
**`nvmecontrol/`** 用于扩展 nvmecontrol(8) 实用程序的厂商特定库

**`clang/`** 系统编译器 [clang(1)](../man1/clang.1.md) 的共享库
**`compat/`** 用于兼容性的共享库
**`debug/`** 内核和基本系统库及二进制文件的独立调试数据
**`dtrace/`** [dtrace(1)](../man1/dtrace.1.md) 库脚本
**`engines/`** OpenSSL（加密/SSL 工具包）动态可加载引擎
**`flua/`** FreeBSD Lua 共享库
**`i18n/`** 用于国际化的共享库

**`ldscripts/`** 链接器脚本；参见 [ld(1)](../man1/ld.lld.1.md)
**`pkgconfig/`** pkgconf(1) 开发工具的编译器和链接器标志集合

**`bsdconfig/`** 由 ncurses FreeBSD 配置向导调用的实用程序
**`bsdinstall/`** bsdinstall(8) 的实用程序
**`dwatch/`** dwatch(1) 的配置文件
**`fwget/`** 由 fwget(8) 调用的实用程序
**`hyperv/`** 用于与 Hyper-V hypervisor 通信的脚本
**`lpr/`** 行式打印机系统的实用程序和过滤器；参见 lpr(1)
**`sendmail/`** sendmail(8) 二进制文件；参见 mailwrapper(8)
**`sm.bin/`** sendmail(8) 的受限 shell；参见 smrsh(8)
**`zfs/`** Z 文件系统实用程序

**`bin/`** 本地用户实用程序，参见 [intro(1)](../man1/intro.1.md)
**`etc/`** 本地程序配置
**`include/`** 本地库头文件
**`lib/`** 本地库
**`lib32/`** 本地 32 位兼容库
**`libdata/`** 本地实用程序数据文件
**`libexec/`** 由本地实用程序执行的实用程序
**`sbin/`** 本地管理实用程序
**`share/`** 本地体系结构无关文件
**`share/doc/`** 本地文档
**`share/doc/freebsd/`** FreeBSD 项目提供的文章、书籍、FAQ 和手册
**`share/man/`** 本地手册页；参见 [man(1)](../man1/man.1.md)

**`freebsd`** FreeBSD 特定的术语、专有名词和行话
**`web2`** 来自 Webster's Second International 的单词

**`pkg/`** pkg(7) 和 [pkg(8)](../man8/pkg.8.md) 的指纹

**`ascii`** ASCII 码点图表
**`flowers`** 花卉的含义
**`magic`** file(1) 使用的魔数
**`termcap`** 终端特性数据库；参见 termcap(5)

**`defs/`** 用于 gensnmptree(1) 的树定义文件
**`mibs/`** 管理信息库（MIB）文件

**`fonts/`** 控制台字体；参见 vidcontrol(1) 和 vidfont(1)
**`keymaps/`** 控制台键盘映射；参见 kbdcontrol(1) 和 kbdmap(1)
**`scrnmaps/`** 控制台屏幕映射

**`VERSION/`** FreeBSD 发行版 VERSION 的文件；按照约定，“VERSION”与 [uname(1)](../man1/uname.1.md) `-r` 匹配
**`VERSION/MACHINE.MACHINE_ARCH/`** 表示这些文件的二进制 ABI；“MACHINE”与 [uname(1)](../man1/uname.1.md) `-m` 匹配；“MACHINE_ARCH”与 [uname(1)](../man1/uname.1.md) `-p` 匹配

**`fonts/`** 控制台字体；参见 vidcontrol(1)、vidfont(1) 和 vtfontcvt(8)
**`keymaps/`** 控制台键盘映射；参见 kbdcontrol(1) 和 kbdmap(1)

**`atf/`** 自动化测试框架的脚本；参见 ATF(7)
**`bhyve/`** [bhyve(8)](../man8/bhyve.8.md) 键盘映射
**`calendar/`** 系统范围的日历文件；参见 calendar(1)
**`certs/`** openssl(1) 的 TLS 证书
**`dict/`** 单词列表；参见 [look(1)](../man1/look.1.md)
**`doc/`** 杂项文档
**`dtrace/`** 动态跟踪编译器的脚本；参见 [dtrace(1)](../man1/dtrace.1.md)
**`examples/`** 面向用户和程序员的各类示例
**`firmware/`** 由用户空间程序加载的固件映像
**`games/`** BSD 传统游戏使用的 ASCII 文本文件，参见 [intro(6)](../man6/intro.6.md)
**`keys/`** 已知的可信和已撤销密钥
**`locale/`** 本地化文件；参见 setlocale(3)
**`man/`** 系统手册页；参见 [man(1)](../man1/man.1.md)
**`misc/`** 杂项系统范围文件
**`mk/`** make 模板；参见 [make(1)](../man1/make.1.md)
**`nls/`** 国家语言支持文件
**`security/`** 用于诸如 [mac_lomac(4)](../man4/mac_lomac.4.md) 等安全策略的数据文件
**`sendmail/`** sendmail(8) 配置文件
**`skel/`** 用于新账户的示例 `.`（点）文件
**`snmp/`** SNMP 守护进程的 MIB、示例文件和树定义
**`syscons/`** [syscons(4)](../man4/syscons.4.md) 文件
**`sysroot/`** -sysroot 编译器/链接器参数构建非原生二进制文件所需的文件
**`tabset/`** 各种终端的制表符描述文件；用于 termcap 文件；参见 termcap(5)
**`vi/`** [vi(1)](../man1/vi.1.md) 编辑器的本地化支持和实用程序
**`vt/`** 系统控制台使用的文件；参见 [vt(4)](../man4/vt.4.md)
**`zoneinfo/`** 时区配置信息；参见 tzfile(5)

**`bin/`** 通用实用程序、编程工具和应用程序；参见 [intro(1)](../man1/intro.1.md)
**`freebsd-dist/`** 发行文件（如 base.txz）；参见 [release(7)](release.7.md) 和 bsdinstall(8)
**`include/`** 标准 C 头文件
**`lib/`** 共享库和 [ar(1)](../man1/ar.1.md) 类型库；参见 [intro(3)](../man3/intro.3.md)
**`lib32/`** 32 位兼容库
**`libdata/`** 杂项实用程序数据文件
**`libexec/`** 由程序执行的系统守护进程和实用程序
**`local/`** 由 pkg(7) 或 [ports(7)](ports.7.md) 安装的本地可执行文件、库等
**`obj/`** 从源代码构建 FreeBSD 生成的体系结构特定目标树；参见 [build(7)](build.7.md)
**`ports/`** FreeBSD ports 集合；参见 [ports(7)](ports.7.md)
**`sbin/`** 供用户执行的系统守护进程和实用程序；参见 [intro(8)](../man8/intro.8.md)
**`share/`** 体系结构无关文件
**`src/`** FreeBSD 源代码；参见 [development(7)](development.7.md)；源代码树的布局由顶层 `README.md` 文件描述
**`tests/`** FreeBSD 测试套件；参见 [tests(7)](tests.7.md)

**`acct`** 执行记账文件；参见 [acct(5)](../man5/acct.5.md)

**`jobs/`** 作业文件
**`spool/`** 输出假脱机文件

**`pkg/`** [pkg(8)](../man8/pkg.8.md) 的缓存软件包
**`cups/`** 通用 UNIX 打印系统的缓存打印机；参见 cups(1)

**`tabs/`** crontab 文件；参见 crontab(5)

**`etcupdate/`** etcupdate(8) 的临时文件和日志
**`freebsd-update/`** [freebsd-update(8)](../man8/freebsd-update.8.md) 的下载和临时文件
**`pkg/`** 软件包数据库

**`Xorg.0.log`** Xserver(1) 日志，如果安装了 X(7)，轮转为 `Xorg.0.log.old`
**`aculog`** 串行线路访问日志；参见 cu(1)
**`auth.log`** 系统身份验证日志
**`bsdinstall_log`** 系统安装日志
**`cron`** 计划任务日志；参见 cron(8)
**`cups/`** cups(1) 的日志
**`daemon.log`** 系统守护进程的默认日志
**`devd.log`** 设备状态变更守护进程的默认日志
**`dmesg.today`** 内核消息缓冲区日志，轮转为 `dmesg.yesterday`
**`debug.log`** 未丢弃的调试 syslog 消息
**`lpd-errs`** 行式打印机假脱机守护进程的日志；参见 lpd(8)
**`maillog`** sendmail(8) 日志，轮转并压缩为 maillog.0.bz2
**`messages`** 通用系统消息日志；参见 syslogd(8)
**`mount.today`** 当前加载的 [fstab(5)](../man5/fstab.5.md)，轮转为 `mount.yesterday`
**`pf.today`** 数据包过滤器防火墙日志；参见 [pf(4)](../man4/pf.4.md)
**`pflog`** 由 pflogd(8) 捕获的已保存数据包
**`ppp.log`** 参见 ppp(8)
**`security`** 标记为安全标志的事件记录
**`setuid.today`** 以提升权限运行的可执行文件列表，轮转为 `setuid.yesterday`
**`userlog`** 记录用户或组更改的日志
**`utx.lastlogin`** 上次登录日志；参见 getutxent(3)
**`utx.log`** 登录/注销日志；参见 getutxent(3)

**`bhyve/`** [bhyve(8)](../man8/bhyve.8.md) 虚拟机 [unix(4)](../man4/unix.4.md) 域套接字
**`ppp/`** 可由 “network” 组写入，用于命令连接套接字；参见 ppp(8)
**`utx.active`** 当前用户数据库；参见 getutxent(3)
**`wpa_supplicant/`** IEEE Std. 802.11 wifi 运行时文件

**`clientmqueue/`** 未投递的提交邮件队列；参见 sendmail(8)
**`cups/`** cups(1) 的打印作业和临时文件
**`dma/`** DMA 邮件代理的未投递邮件队列；参见 dma(8)
**`lock/`** 串行设备锁；参见 uucplock(3)
**`lpd/`** 行式打印机假脱机守护进程假脱机
**`mqueue/`** sendmail(8) 的未投递邮件队列
**`output/`** 行式打印机假脱机目录

**`vi.recover/`** [vi(1)](../man1/vi.1.md) 编辑器的恢复文件

**`account/`** 系统记账文件
**`at/`** 定时命令调度文件；参见 [at(1)](../man1/at.1.md)
**`audit/`** 安全事件审计跟踪文件；参见 audit(8)
**`authpf/`** 用于认证网关的用户 shell 会话；参见 [authpf(8)](../man8/authpf.8.md)
**`backups/`** 关键系统配置备份
**`cache/`** 杂项缓存文件
**`crash/`** 存储内核崩溃转储的默认目录；参见 [crash(8)](../man8/crash.8.md) 和 savecore(8)
**`cron/`** cron 使用的文件；参见 cron(8)
**`db/`** 自动生成的系统特定数据库文件
**`empty/`** 供需要空目录的程序使用，例如 sshd(8) 用于权限分离
**`games/`** BSD 传统游戏的状态和得分文件
**`heimdal/`** Kerberos 服务器数据库；参见 kdc(8)
**`lib/`** 移植的 Linux 应用程序的状态信息
**`log/`** 系统日志文件
**`mail/`** 用户邮箱文件
**`msgs/`** 系统消息数据库；参见 msgs(1)
**`preserve/`** 未使用，出于历史原因保留
**`quotas/`** UFS 配额信息文件
**`run/`** 包含操作系统自引导以来信息的文件
**`rwho/`** 关于本地网络上其他系统的信息；参见 rwhod(8)、[rwho(1)](../man1/rwho.1.md) 和 [ruptime(1)](../man1/ruptime.1.md)
**`spool/`** 打印机和邮件系统假脱机目录
**`tmp/`** 系统重启之间不删除的临时文件
**`unbound/`** unbound(8) 的文件和配置
**`yp/`** NIS 映射；参见 [yp(8)](../man8/yp.8.md)

**`/`** 文件系统的根目录

**`/COPYRIGHT`** FreeBSD 版权信息

**`/bin/`** 基本的 BSD 用户实用程序；参见 [intro(1)](../man1/intro.1.md)

**`/boot/`** FreeBSD [boot(8)](../man8/boot_i386.8.md) 期间使用的程序和配置

**`/compat/`** 支持与其他操作系统二进制兼容的文件

**`/dev/`** 设备节点和特殊文件；参见 [intro(4)](../man4/intro.4.md) 和 [devfs(4)](../man4/devfs.4.md)

**`/entropy`** 为 RNG 提供初始状态；参见 save-entropy(8)

**`/etc/`** 基本系统配置文件和脚本；参见 [intro(5)](../man5/intro.5.md)

**`/home/`** 用户的家目录；交互式用户 `beastie` 的典型家目录为 **/home/beastie/**

**`/lib/`** 对 **/bin** 和 **/sbin** 中的二进制文件至关重要的系统库

**`/libexec/`** 对 **/bin** 和 **/sbin** 中的二进制文件至关重要的系统实用程序

**`/media/`** 可移动存储介质（如 CD、DVD 和 USB 驱动器）的挂载点；参见 automount(8)，或者如果使用来自 [ports(7)](ports.7.md) 的桌面环境，则参见 bsdisks(8)

**`/mnt/`** 系统管理员通常用作临时挂载点的空目录

**`/net/`** 自动挂载的 NFS 共享；参见 auto_master(5)

**`/nonexistent/`** 不存在的目录；按照约定，它作为不需要家目录的用户账户的家目录；另见 **/var/empty/**

**`/proc/`** 进程文件系统；参见 [procfs(4)](../man4/procfs.4.md)

**`/rescue/`** 用于紧急恢复的静态链接程序；参见 [rescue(8)](../man8/rescue.8.md)

**`/root/`** root 用户的家目录

**`/sbin/`** 基本的 BSD 系统管理实用程序；参见 [intro(8)](../man8/intro.8.md)

**`/tmp/`** 通常在系统重启之间删除的临时文件；参见 [rc.conf(5)](../man5/rc.conf.5.md) 中的 `clear_tmp_enable`

**`/usr/`** 包含大多数用户实用程序和应用程序

**`/var/`** 日志、临时、过渡和假脱机文件

## 注释

本手册页记录了默认的 FreeBSD 文件系统布局。给定系统上的实际层次结构由系统管理员自行定义。维护良好的安装会包含本文档的自定义版本。

## 参见

[apropos(1)](../man1/apropos.1.md), [find(1)](../man1/find.1.md), [grep(1)](../man1/grep.1.md), [ls(1)](../man1/ls.1.md), [whereis(1)](../man1/whereis.1.md), [which(1)](../man1/which.1.md)

## 历史

`hier` 手册页首次出现于 1979 年的 Version 7 AT&T UNIX。
