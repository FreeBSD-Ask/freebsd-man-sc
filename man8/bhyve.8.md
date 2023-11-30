  BHYVE(8)  

BHYVE(8)

FreeBSD System Manager's Manual

BHYVE(8)

[名称](#__u540D___u79F0_)
=======================

`bhyve` —

在虚拟机中运行来宾操作系统

[概要](#__u6982___u8981_)
=======================

`bhyve` \[`-AaCDeHhPSuWwxY`\] \[`-c `\[\[`cpus=`\]numcpus\]\[`,sockets=`n\]\[`,cores=`n\]\[`,threads=`n\]\] \[`-G` port\] \[`-l` `help`|lpcdev \[`,` conf\]\] \[`-m` memsize\[`K` | `k` | `M`|`m` | `G` | `g`|`T` | `t`\]\] \[`-p` vcpu`:`hostcpu\] \[`-r` file\] \[`-s` `help`|slot `,` emulation\[`,` conf\]\] \[`-U` uuid\] vmname

[描述](#__u63CF___u8FF0_)
=======================

`bhyve` 是一个在虚拟机中运行客户操作系统的管理程序。

可以使用命令行参数指定虚拟 CPU 数量、客户内存量和 I/O 连接等参数。

如果不使用引导 ROM，来宾操作系统必须在运行 `bhyve` 之前使用 bhyveload(8)-
或类似的引导加载程序加载，否则，使用选择的引导 ROM 运行 `bhyve` 就足够了。

`bhyve` 将一直运行，直到客户操作系统重新启动或检测到未处理的管理程序退出。

[选项](#__u9009___u9879_)
=======================

[`-a`](#a)

来宾的本地 APIC 配置为 xAPIC 模式。xAPIC 模式是默认设置，因此此选项是多余的。 它将在未来的版本中被弃用。

[`-A`](#A)

生成 ACPI 表。 FreeBSD/amd64 来宾需要。

[`-c`](#c) \[setting ...\]

来宾虚拟 CPU 的数量和/或 CPU 拓扑。 numcpus, sockets, cores 和 threads 的默认值为 1。 当前来宾虚拟 CPU 的最大数量为 16。 如果未指定 numcpus ，则它将根据其他参数计算。 拓扑必须一致，因为 numcpus 必须等于 sockets, cores 和 threads 的乘积。 如果多次指定一个 setting ，则最后一个设置优先。

[`-C`](#C)

在核心文件中包含来宾内存。

[`-D`](#D)

在来宾启动的关机时销毁 VM。

[`-e`](#e)

当来宾发出对未模拟的 I/O 端口的访问时，强制 `bhyve` 退出。 这是用于调试目的。

[`-G`](#G) port

启动一个调试服务器，它使用 GDB 协议将访客状态导出到调试器。 IPv4 TCP 套接字将绑定到提供的 port 以侦听调试器连接。 一次只能将一个调试器附加到调试服务器。 如果 port 以 ‘w’ 开头， `bhyve` 将在等待调试器附加的第一条指令处暂停执行。

[`-h`](#h)

打印帮助信息并退出。

[`-H`](#H)

当检测到 HLT 指令时，让出虚拟 CPU 线程。 如果未指定此选项，则虚拟 CPU 将使用 100% 的主机 CPU。

[`-l`](#l) \[help|lpcdev\[,conf\]\]

允许配置 LPC PCI-ISA 桥后面的设备。 唯一受支持的设备是 TTY 类设备 com1 到 com4, 引导 ROM 设备 bootrom 和调试/测试设备 pc-testdev 。

help 帮助打印支持的 LPC 设备列表。

[`-m`](#m) memsize\[K|k|M|m|G|g|T|t\]

客户机物理内存大小（以字节为单位）。 这必须与提供给 bhyveload(8) 的大小相同。

size 参数可以后缀为 K、M、G 或 T（大写或小写）之一，以指示千字节、兆字节、千兆字节或太字节的倍数。 如果没有给出后缀，则假定该值以兆字节为单位。

memsize 默认为 256M。

[`-p`](#p) vcpu:hostcpu

将 guest 的虚拟 CPU _vcpu_ 固定到 _hostcpu_ 。

[`-P`](#P)

当检测到 PAUSE 指令时，强制客户虚拟 CPU 退出。

[`-r`](#r) file

从快照恢复来宾。 客户内存内容从 file 恢复，客户设备和 vCPU 状态从 “file.kern” 恢复。

请注意，当前快照文件格式要求通过指定相同的 \[`-s`\] 和 \[`-l`\] 选项，新 VM 中的设备配置与从中获取快照的 VM 匹配。 从快照中读取 vCPU 计数和内存配置。

[`-s`](#s) \[help|slot,emulation\[,conf\]\]

配置虚拟 PCI 插槽和功能。

`bhyve` 提供 PCI 总线仿真和可连接到总线插槽的虚拟设备。 有 32 个可用插槽，每个插槽最多可提供 8 个功能。

help

打印支持的 PCI 设备列表。

slot

pcislot\[:function\] bus:pcislot:function

pcislot 值为 0 到 31。 可选 function 值为 0 到 7。 可选 bus 值为 0 到 255。 如果未指定，则 function 值默认为 0。 如果未指定，则 bus 值默认为 0。

emulation

[`hostbridge`](#hostbridge) | [`amd_hostbridge`](#amd_hostbridge)

提供一个简单的主机桥。 这通常在插槽 0 处配置，并且是大多数客户机操作系统所必需的。 `amd_hostbridge` 仿真是相同的，但使用 `AMD` 的 PCI 供应商 ID。

[`passthru`](#passthru)

PCI 直通设备。

[`virtio-net`](#virtio-net)

网络接口。

[`virtio-blk`](#virtio-blk)

Virtio 块存储接口。

[`virtio-scsi`](#virtio-scsi)

Virtio SCSI 接口。

[`virtio-9p`](#virtio-9p)

Virtio 9p (VirtFS) 接口。

[`virtio-rnd`](#virtio-rnd)

Virtio RNG 接口。

[`virtio-console`](#virtio-console)

Virtio 控制台接口，以简单字符设备的形式向来宾公开多个端口，用于来宾和主机用户空间之间的简单 IO。

[`ahci`](#ahci)

连接到任意设备的 AHCI 控制器。

[`ahci-cd`](#ahci-cd)

连接到 ATAPI CD/DVD 的 AHCI 控制器。

[`ahci-hd`](#ahci-hd)

连接到 SATA 硬盘驱动器的 AHCI 控制器。

[`e1000`](#e1000)

英特尔 e82545 网络接口。

[`uart`](#uart)

PCI 16550 串行设备。

[`lpc`](#lpc)

LPC PCI-ISA 桥，带有 COM1 和 COM2 16550 串行端口、引导 ROM，以及可选的调试/测试设备。 LPC 桥接仿真只能在总线 0 上配置。

[`fbuf`](#fbuf)

连接到 VNC 服务器的原始帧缓冲设备。

[`xhci`](#xhci)

可扩展主机控制器接口 (xHCI) USB 控制器。

[`nvme`](#nvme)

NVM Express (NVMe) 控制器。

[`hda`](#hda)

高清音频控制器。

\[conf\]

此可选参数描述设备仿真的后端。 如果未指定 conf ，则设备仿真没有后端，可以认为是未连接的。

网络后端：

tapN\[,mac=xx:xx:xx:xx:xx:xx\]\[,mtu=N\]

vmnetN\[,mac=xx:xx:xx:xx:xx:xx\]\[,mtu=N\]

netgraph,path=ADDRESS,peerhook=HOOK\[,socket=NAME\]\[,hook=HOOK\]\[,mac=xx:xx:xx:xx:xx:xx\]\[,mtu=N\]

如果未指定 mac ，则 MAC 地址来自固定的 OUI，其余字节来自插槽和功能编号以及设备名称的 MD5 散列。

MAC 地址是 ethers(5) 格式的 ASCII 字符串。

使用 virtio-net 设备，可以指定 mtu 参数来通知来宾应该允许的最大 MTU，以字节表示。

使用 netgraph 后端，必须指定 path 和 peerhook 参数来设置目标节点和相应的 hook。 可选参数 socket 和 hook 可用于设置 ng\_socket(4) 节点名称和源挂钩。 ADDRESS, HOOK 和 NAME 必须符合 netgraph(4) 寻址规则。

块存储设备：

/filename\[,block-device-options\]

/dev/xxx\[,block-device-options\]

block-device-options 是：

[`nocache`](#nocache)

使用 `O_DIRECT` 打开文件。

[`direct`](#direct)

使用 `O_SYNC` 打开文件。

[`ro`](#ro)

强制文件以只读方式打开。

[`sectorsize=`](#sectorsize=)logical\[/physical\]

指定模拟磁盘的逻辑和物理扇区大小。 物理扇区大小是可选的，如果未明确指定，则等于逻辑扇区大小。

[`nodelete`](#nodelete)

通过 `DIOCGDELETE` 请求禁用来宾修剪请求的模拟。

SCSI 设备：

/dev/cam/ctl\[pp.vp\]\[,scsi-device-options\]

scsi-device-options 是：

[`iid=`](#iid=)IID

向指定 CTL 端口发送请求时使用的发起程序 ID。 默认值为 0。

9P 设备：

sharename=/path/to/share\[,9p-device-options\]

9p-device-options 是:

[`ro`](#ro_2)

以只读模式公开共享。

TTY 设备：

[`stdio`](#stdio)

将串口连接到 `bhyve` 进程的标准输入和输出。

/dev/xxx

将主机 TTY 设备用于串行端口 I/O。

引导 ROM 设备：

romfile

在为引导固件保留的来宾地址空间中映射 romfile 。

直通设备：

slot/bus/function

通过 slot, bus 和 function 号描述的选择器连接到主机上的 PCI 设备。

配置直通设备时，必须使用 `-S` 选项连接来宾内存。

主机设备必须在引导时使用 pptdevs 加载程序变量保留，如 vmm(4) 中所述。

Virtio 控制台设备：

[`port1=`](#port1=)/path/to/port1.sock,anotherport=...

每个设备最多可以创建 16 个端口。 每个端口都被命名并对应于一个由 `bhyve` 创建的 Unix 域套接字。 `bhyve` 一次最多接受每个端口的一个连接。

限制：

*   由于 `bhyve` 中缺少析构函数，文件系统上的套接字必须在 `bhyve` 退出后手动清理。
*   目前无法使用 "console port" 功能，也无法调整控制台端口大小。
*   紧急写入广告，但目前没有操作。

帧缓冲设备：

\[rfb=\[IP:\]port\]\[,w=width\]\[,h=height\]\[,vga=vgaconf\]\[,wait\]\[,password=password\]

IPv4:port or \[IPv6%zone\]:port

一个 IP 地址和一个 port VNC 应该监听。默认是侦听 localhost IPv4 地址和默认 VNC 端口 5900。 IPv6 地址必须用方括号括起来，并且可以包含可选的区域标识符。

width and height

分别是显示分辨率、宽度和高度。如果未指定，将使用 1024x768 像素的默认分辨率。 支持的最小分辨率为 640x480 像素，最大支持分辨率为 1920x1200 像素。

vgaconf

此选项的可能值为 “io” (默认), “on” 和 “off” 。 PCI 显卡具有双重特性，即它们是具有 BAR 寻址的标准 PCI 设备，但也可以隐式解码传统 VGA I/O 空间 (0x3c0-3df) 和内存空间 (64KB at 0xA0000) 。 默认的 “io” 选项应该用于尝试发出导致 I/O 端口查询的 BIOS 调用的客户机，并且如果禁用 I/O 解码则无法启动。

“on” 选项应与 UEFI 中的 CSM BIOS 功能一起使用，以引导需要传统 VGA I/O 和内存区域可用的传统 BIOS 来宾。

如果 UEFI 来宾检测到 I/O 端口，则假定存在 VGA 适配器，应使用 “off” 选项。 UEFI 模式下的 OpenBSD 就是这种客户机的一个例子。

请参阅 `bhyve` FreeBSD wiki 页面 ([https://wiki.freebsd.org/bhyve](https://wiki.freebsd.org/bhyve)) 了解特定访客的配置说明。

wait

指示 `bhyve` 仅在启动 VNC 连接时启动，从而简化需要立即键盘输入的操作系统的安装。 这可以删除以供安装后使用。

password

众所周知，这种类型的身份验证在密码学上很弱，不适合在不受信任的网络上使用。 许多实现都希望使用更强的安全性，例如通过 IPsec 或 SSH 提供的加密通道运行会话。

xHCI USB 设备:

[`tablet`](#tablet)

使用 VNC 时提供精确光标同步的 USB 平板设备。

NVMe 设备:

[`devpath`](#devpath)

开发路径 接受的设备路径是： /dev/blockdev 或 /path/to/image 或 ram=size\_in\_MiB 。

[`maxq`](#maxq)

最大队列数。

[`qsz`](#qsz)

每个队列中的最大元素。

[`ioslots`](#ioslots)

最大并发 I/O 请求数。

[`sectsz`](#sectsz)

扇区大小（默认为 blockif 扇区大小）。

[`ser`](#ser)

序列号最多 20 个字符。

AHCI 设备:

[`nmrr`](#nmrr)

标称介质转速，称为 RPM。 值 1 将指示设备为固态磁盘。 默认值为0，不报告。

[`ser`](#ser_2)

序列号，最多 20 个字符。

[`rev`](#rev)

修订号，最多 8 个字符。

[`model`](#model)

型号，最多 40 个字符。

高清音频设备：

[`play`](#play)

播放设备，通常是 /dev/dsp0 。

[`rec`](#rec)

录音设备，通常是 /dev/dsp0 。

[`-S`](#S)

连接访客内存。

[`-u`](#u)

RTC 保持 UTC 时间。

[`-U`](#U) uuid

在客户机的系统管理 BIOS 系统信息结构中设置通用唯一标识符 (UUID) 。 默认情况下，从主机的主机名和 vmname 生成 UUID。

[`-w`](#w)

忽略对未实现的模型特定寄存器 (MSR) 的访问。 这是用于调试目的。

[`-W`](#W)

强制 virtio PCI 设备仿真使用 MSI 中断而不是 MSI-X 中断。

[`-x`](#x)

来宾的本地 APIC 配置为 x2APIC 模式。

[`-Y`](#Y)

禁用 MPtable 生成。

vmname

客人的字母数字姓名。 这应该与 bhyveload(8) 创建的相同。

[调试服务器](#__u8C03___u8BD5___u670D___u52A1___u5668_)
==================================================

当前的调试服务器为调试器提供有限的支持。

[寄存器](#__u5BC4___u5B58___u5668_)
--------------------------------

每个虚拟 CPU 作为一个线程暴露给调试器。

可以查询每个虚拟 CPU 的通用寄存器，但不能查询浮点和系统寄存器等其他寄存器。

[记忆](#__u8BB0___u5FC6_)
-----------------------

内存（包括内存映射的 I/O 区域）可以由调试器读取和写入。 内存操作使用通过当前虚拟 CPU 的活动地址转换解析为物理地址的虚拟地址。

[控制](#__u63A7___u5236_)
-----------------------

正在运行的客户机可以随时被调试器中断 (例如，通过在调试器中按 Ctrl-C) 。

单步仅在支持 MTRAP VM 退出的 Intel CPU 上受支持。

支持单步执行的 Intel CPU 支持断点。 请注意，在客户机中启用中断时从断点继续可能无法按预期工作，因为在单步越过断点时会触发计时器中断。

[信号处理](#__u4FE1___u53F7___u5904___u7406_)
=========================================

`bhyve` 处理以下信号：

SIGTERM

触发 VM 的 ACPI 断电

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

退出状态指示 VM 是如何终止的：

0

重新启动

1

关机

2

停止

3

三重故障

4

由于错误而退出

[实例](#__u5B9E___u4F8B_)
=======================

如果不使用引导 ROM，来宾操作系统必须先加载 bhyveload(8) 或类似的引导加载程序，然后才能运行 bhyve(4) 。 否则，不需要引导加载程序。

要运行具有 1GB 内存、两个虚拟 CPU、一个由 /my/image 文件系统映像支持的 virtio 块设备和一个用于控制台的串行端口的虚拟机：

bhyve -c 2 -s 0,hostbridge -s 1,lpc -s 2,virtio-blk,/my/image \\ -l com1,stdio -A -H -P -m 1G vm1 

运行具有三个网络端口的 24GB 单 CPU 虚拟机，其中一个指定了 MAC 地址：

bhyve -s 0,hostbridge -s 1,lpc -s 2:0,virtio-net,tap0 \\ -s 2:1,virtio-net,tap1 \\ -s 2:2,virtio-net,tap2,mac=00:be:fa:76:45:00 \\ -s 3,virtio-blk,/my/image -l com1,stdio \\ -A -H -P -m 24G bigvm 

运行具有 8 个 AHCI SATA 磁盘、一个 AHCI ATAPI CD-ROM、一个 virtio 网络端口、一个 AMD 主机桥以及连接到 nmdm(4) 空调制解调器设备的控制台端口的 8GB 四 CPU 虚拟机。

bhyve -c 4 \\ -s 0,amd\_hostbridge -s 1,lpc \\ -s 1:0,ahci,hd:/images/disk.1,hd:/images/disk.2,\\ hd:/images/disk.3,hd:/images/disk.4,\\ hd:/images/disk.5,hd:/images/disk.6,\\ hd:/images/disk.7,hd:/images/disk.8,\\ cd:/images/install.iso \\ -s 3,virtio-net,tap0 \\ -l com1,/dev/nmdm0A \\ -A -H -P -m 8G 

运行显示分辨率为 800 x 600 像素的 UEFI 虚拟机，可通过 VNC 访问：0.0.0.0:5900。

bhyve -c 2 -m 4G -w -H \\ -s 0,hostbridge \\ -s 3,ahci-cd,/path/to/uefi-OS-install.iso \\ -s 4,ahci-hd,disk.img \\ -s 5,virtio-net,tap0 \\ -s 29,fbuf,tcp=0.0.0.0:5900,w=800,h=600,wait \\ -s 30,xhci,tablet \\ -s 31,lpc -l com1,stdio \\ -l bootrom,/usr/local/share/uefi-firmware/BHYVE\_UEFI.fd \\ uefivm 

运行带有 VNC 显示的 UEFI 虚拟机，该显示绑定到端口 5900 上的所有 IPv6 地址。

bhyve -c 2 -m 4G -w -H \\ -s 0,hostbridge \\ -s 4,ahci-hd,disk.img \\ -s 5,virtio-net,tap0 \\ -s 29,fbuf,tcp=\[::\]:5900,w=800,h=600 \\ -s 30,xhci,tablet \\ -s 31,lpc -l com1,stdio \\ -l bootrom,/usr/local/share/uefi-firmware/BHYVE\_UEFI.fd \\ uefivm 

[参见](#__u53C2___u89C1_)
=======================

bhyve(4), netgraph(4), ng\_socket(4), nmdm(4), vmm(4), ethers(5), bhyvectl(8), bhyveload(8)

Intel, _64 and IA-32 Architectures Software Developer’s Manual_, Volume 3.

[历史](#__u5386___u53F2_)
=======================

`bhyve` 首次出现在 FreeBSD 10.0 中。

[作者](#__u4F5C___u8005_)
=======================

Neel Natu <[neel@freebsd.org](mailto:neel@freebsd.org)\> Peter Grehan <[grehan@freebsd.org](mailto:grehan@freebsd.org)\>

January 18, 2021

FreeBSD 13.1-RELEASE