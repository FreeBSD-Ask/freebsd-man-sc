  QEMU(1)  

QEMU(1)

QEMU

QEMU(1)

[NAME](#NAME)
=============

qemu - QEMU 用户文档

[概要](#__u6982___u8981_)
=======================

qemu-system-x86\_64 \[options\] \[disk\_image\] 

-

-

[描述](#__u63CF___u8FF0_)
=======================

QEMU PC 系统仿真器模拟以下外围设备：

*   i440FX 主机 PCI 桥和 PIIX3 PCI 到 ISA 桥
*   Cirrus CLGD 5446 PCI VGA 卡或带 Bochs VESA 扩展的虚拟 VGA 卡（硬件级别，包括所有非标准模式）。
*   PS/2 鼠标和键盘
*   2个PCI IDE接口，支持硬盘和CD-ROM
*   软盘
*   PCI 和 ISA 网络适配器
*   串口
*   IPMI BMC，内部或外部之一
*   Creative SoundBlaster 16 声卡
*   ENSONIQ AudioPCI ES1370 声卡
*   Intel 82801AA AC97 音频兼容声卡
*   英特尔高清音频控制器和 HDA 编解码器
*   Adlib (OPL2) - Yamaha YM3812 兼容芯片
*   Gravis Ultrasound GF1 声卡
*   CS4231A 兼容声卡
*   电脑音箱
*   PCI UHCI, OHCI, EHCI 或 XHCI USB 控制器和一个虚拟 USB-1.1 集线器。

-

SMP 支持多达 255 个 CPU。

QEMU 使用来自 Seabios 项目的 PC BIOS 和 Plex86/Bochs LGPL VGA BIOS。

QEMU 使用 Tatsuyuki Satoh 的 YM3812 仿真。

QEMU 使用 Tibor "TS" Schütz 的 GUS 仿真 (GUSEMU32 _http://www.deinmeister.de/gusemu/_) 。

请注意，默认情况下，GUS 与并行端口共享 IRQ(7)，因此必须告知 QEMU 没有并行端口才能使 GUS 正常工作。

qemu-system-x86\_64 dos.img -device gus -parallel none 

-

-

或者：

qemu-system-x86\_64 dos.img -device gus,irq=5 

-

-

或其他一些无人认领的 IRQ。

CS4231A是Windows Sound System和GUSMAX产品中使用的芯片

可以使用 pcspk-audiodev 机器属性来配置 PC 扬声器音频设备，即

qemu-system-x86\_64 some.img -audiodev <backend>,id=<name> -machine pcspk-audiodev=<name> 

-

-

[选项](#__u9009___u9879_)
=======================

disk\_image 是 IDE 硬盘 0 的原始硬盘映像。有些目标不需要磁盘映像。

[标准选项](#__u6807___u51C6___u9009___u9879_)
-----------------------------------------

****\-h****

显示帮助并退出

****\-version****

显示版本信息并退出

****\-machine \[type=\]name\[,prop=value\[,...\]\]****

按名称选择模拟机器。 使用 **\-machine help** p 列出可用的机器。

对于旨在支持跨版本实时迁移兼容性的架构，每个版本都将引入新的版本化机器类型。 例如，2.8.0 版本为 x86\_64/i686 架构引入了机器类型 "pc-i440fx-2.8" 和 "pc-q35-2.8" 。

为了允许从 QEMU 2.8.0 版实时迁移到 QEMU 2.9.0 版，2.9.0 版也必须支持 "pc-i440fx-2.8" 和 "pc-q35-2.8" 机器。 为了让用户实时迁移虚拟机在升级时跳过多个中间版本，QEMU 的新版本将支持许多以前版本的机器类型。

支持的机器属性有：

****accel=accels1\[:accels2\[:...\]\]****

这用于启用加速器。 根据目标架构，可以使用 kvm、xen、hax、hvf、nvmm、whpx 或 tcg。 默认情况下，使用 tcg。 如果指定了多个加速器，则在前一个未能初始化的情况下使用下一个。

****vmport=on|off|auto****

启用 VMWare IO 端口的仿真，用于 vmmouse 等。 auto 表示根据加速度选择值。 对于 accel=xen，默认为关闭，否则默认为开启。

****dump-guest-core=on|off****

在核心转储中包含来宾内存。 默认为开启。

****mem-merge=on|off****

启用或禁用内存合并支持。 当主机支持此功能时，会在 VM 实例之间重复删除相同的内存页面（默认启用）。

****aes-key-wrap=on|off****

在 s390-ccw 主机上启用或禁用 AES 密钥包装支持。 此功能控制是否将创建 AES 包装密钥以允许执行 AES 加密功能。默认为开启。

****dea-key-wrap=on|off****

在 s390-ccw 主机上启用或禁用 DEA 密钥包装支持。 此功能控制是否创建 DEA 包装密钥以允许执行 DEA 加密功能。默认为开启。

****nvdimm=on|off****

启用或禁用 NVDIMM 支持。默认为关闭。

****memory-encryption=****

要使用的内存加密对象。 默认值为无。

****hmat=on|off****

启用或禁用 ACPI 异构内存属性表 (HMAT) 支持。 默认为关闭。

****memory-backend='id'****

传统 **\-mem-path** 和 **mem-prealloc** 选项的替代方案。 允许使用内存后端作为主 RAM。

例如：

\-object memory-backend-file,id=pc.ram,size=512M,mem-path=/hugetlbfs,prealloc=on,share=on -machine memory-backend=pc.ram -m 512M 

-

-

迁移兼容性说明：

*   作为后端 id，如果需要迁移到/从旧 QEMU (<5.0) 迁移，则应使用按机器类型通告的 'default-ram-id\[u503C\]（可通过 **query-machines** 命令获得）。
*   对于 4.0 及更早的机器类型，如果需要迁移到/从旧 QEMU (<5.0) 迁移，用户应使用 **x-use-canonical-path-for-ramblock-id=off** 后端选项。

-

例如：

\-object memory-backend-ram,id=pc.ram,size=512M,x-use-canonical-path-for-ramblock-id=off -machine memory-backend=pc.ram -m 512M 

-

-

-

****sgx-epc.0.memdev=@var{memid}****

定义一个新交所 EPC 部分。

****\-cpu model****

选择 CPU 型号（列表和附加功能选择的 **\-cpu help** )

****\-accel name\[,prop=value\[,...\]\]****

这用于启用加速器。 根据目标架构，可以使用 kvm、xen、hax、hvf、nvmm、whpx 或 tcg。 默认情况下，使用 tcg。 如果指定了多个加速器，则在前一个未能初始化的情况下使用下一个。

****igd-passthru=on|off****

使用 Xen 时，此选项控制是否可以将 Intel 集成显卡设备传递给来宾（默认 = 关闭）

****kernel-irqchip=on|off|split****

控制 KVM 内核 irqchip 支持。 默认值为中断控制器的完全加速。 在 x86 上，拆分 irqchip 减少了内核攻击面，但会降低非 MSI 中断的性能。 不建议完全禁用内核中的 irqchip，除非出于调试目的。

****kvm-shadow-mem=size****

定义 KVM 影子 MMU 的大小。

****split-wx=on|off****

控制对 TCG 代码生成缓冲区使用拆分 w^x 映射。 某些操作系统需要启用此功能，在这种情况下，这将默认启用。 在其他操作系统上，这将默认关闭，但可以启用它以进行测试或调试。

****tb-size=n****

控制 TCG 转换块缓存的大小（以 MiB 为单位）。

****thread=single|multi****

控制 TCG 线程的数量。 当 TCG 是多线程时，每个 vCPU 将有一个线程，因此可以利用额外的主机内核。 默认情况下启用多线程，后端和前端都支持它并且没有启用不兼容的 TCG 功能（例如 icount/replay）。

****dirty-ring-size=n****

当使用 KVM 加速器时，它控制每个 vCPU 的脏页环形缓冲区的大小（每个 vCPU 的条目数）。 它应该是 2 的幂的值，并且应该是 1024 或更大（但仍小于内核支持的最大值）。 如果您不知道哪个是最好的，4096 可能是一个很好的初始值。 将此值设置为 0 可禁用该功能。 默认情况下，此功能被禁用 (dirty-ring-size=0)。 启用后，KVM 将改为在位图中记录脏页。

-

****\-smp \[\[cpus=\]n\]\[,maxcpus=maxcpus\]\[,sockets=sockets\]\[,dies=dies\]\[,cores=cores\]\[,threads=threads\]****

使用机器类型板上最初存在的 '**n**' 个 CPU 来模拟 SMP 系统。 在支持 CPU 热插拔的板上，可以设置可选的 '**maxcpus**' 参数以允许在运行时添加更多 CPU。 当这两个参数都省略时，CPU 的最大数量将从提供的拓扑成员中计算出来，并且初始 CPU 计数将与最大数量匹配。 当只给出其中之一时，省略的将设置为其对应的值。 可以指定这两个参数，但最大 CPU 数必须等于或大于初始 CPU 计数。 这两个参数都受一个由所选特定机器类型决定的上限。

为了控制 CPU 拓扑信息的报告，可以指定插槽数、每个插槽的裸片、每个裸片的内核数和每个内核的线程数。 总和 \`\` sockets \* cores \* dies \* threads \`\` 必须等于最大 CPU 计数。 CPU 目标可能只支持拓扑参数的一个子集。 如果 CPU 目标不支持使用特定拓扑参数，则应假定其值为 1，以便计算 CPU 最大计数。

必须指定初始 CPU 计数或至少一个拓扑参数。 指定的参数必须大于零，不允许像 "cpus=0" 这样的显式配置。 任何省略的参数的值都将从给定的参数中计算出来。 历史上在计算缺失值时优先考虑最粗略的拓扑参数（即套接字优先于内核，内核优先于线程），但是，这种行为被认为容易改变。 在 6.2 之前，首选是套接字而不是内核而不是线程。 从 6.2 开始，首选是内核而不是套接字而不是线程。

****\-numa node\[,mem=size\]\[,cpus=firstcpu\[-lastcpu\]\]\[,nodeid=node\]\[,initiator=initiator\]****

****\-numa node\[,memdev=id\]\[,cpus=firstcpu\[-lastcpu\]\]\[,nodeid=node\]\[,initiator=initiator\]****

****\-numa dist,src=source,dst=destination,val=distance****

****\-numa cpu,node-id=node\[,socket-id=x\]\[,core-id=y\]\[,thread-id=z\]****

****\-numa hmat-lb,initiator=node,target=node,hierarchy=hierarchy,data-type=tpye\[,latency=lat\]\[,bandwidth=bw\]****

****\-numa hmat-cache,node-id=node,size=size,level=level\[,associativity=str\]\[,policy=str\]\[,line=size\]****

定义一个 NUMA 节点并为其分配 RAM 和 VCPU。 设置从源节点到目标节点的 NUMA 距离。 为给定节点设置 ACPI 异构内存属性。

旧版 VCPU 分配使用 '**cpus**' 选项，其中 firstcpu 和 lastcpu 是 CPU 索引。 每个 '**cpus**' 选项代表一个连续范围的 CPU 索引（如果 lastcpu 被省略，则表示单个 VCPU）。 一组不连续的 VCPU 可以通过提供多个 '**cpus**' 选项来表示。 如果在所有节点上都省略了 '**cpus**' ，则 VCPU 会自动在它们之间拆分。

例如，以下选项将 VCPU 0、1、2 和 5 分配给 NUMA 节点：

\-numa node,cpus=0-2,cpus=5 

-

-

'**cpu**' 选项是 '**cpus**' o选项的新替代方案，它使用 '**socket-id|core-id|thread-id**' 属性使用 CPU 的拓扑布局属性将 CPU 对象分配给节点。 属性集是特定于机器的，并且取决于使用的机器类型/'**smp**' 选项。 可以使用 '**hotpluggable-cpus**' 监控命令查询。 '**node-id**' 属性指定将分配 CPU 对象的节点，在与 '**cpu**' 选项一起使用之前，需要使用 '**node**' 选项声明节点。

例如：

\-M pc \\ -smp 1,sockets=2,maxcpus=2 \\ -numa node,nodeid=0 -numa node,nodeid=1 \\ -numa cpu,node-id=0,socket-id=0 -numa cpu,node-id=1,socket-id=1 

-

-

旧版 '**mem**' 将给定的 RAM 数量分配给节点（5.1 和更新的机器类型不支持）。 '**memdev**' 将 RAM 从给定的内存后端设备分配给节点。 如果在所有节点中都省略了 '**mem**' 和 '**memdev**' ，则 RAM 在它们之间平均分配。

'**mem**' 和 '**memdev**' 是互斥的。 此外，如果一个节点使用 '**memdev**' ，则所有节点都必须使用它。

'**initiator**' 是一个附加选项，它指向对这个 NUMA 节点具有最佳性能（最低延迟或最大带宽）的启动器 NUMA 节点。 请注意，仅当机器属性 'hmat' 设置为 'on' 时才能设置此选项。

以下示例创建具有 2 个 NUMA 节点的机器，节点 0 具有 CPU。 节点 1 只有内存，它的发起者是节点 0。 注意，因为节点 0 有 CPU，默认情况下节点 0 的发起者是自己，而且必须是自己。

\-machine hmat=on \\ -m 2G,slots=2,maxmem=4G \\ -object memory-backend-ram,size=1G,id=m0 \\ -object memory-backend-ram,size=1G,id=m1 \\ -numa node,nodeid=0,memdev=m0 \\ -numa node,nodeid=1,memdev=m1,initiator=0 \\ -smp 2,sockets=2,maxcpus=2 \\ -numa cpu,node-id=0,socket-id=0 \\ -numa cpu,node-id=0,socket-id=1 

-

-

source 和 destination 是 NUMA 节点 ID。 distance 是从源到目的地的 NUMA 距离。 节点到自身的距离始终为 10。 如果给定任何一对节点的距离，则必须给所有对节点的距离。 虽然，当每对节点仅在一个方向上给出距离时，则假定相反方向上的距离相同。 然而，如果甚至为一个节点对给出了一对不对称的距离，则必须为所有节点对提供两个方向的距离值，即使它们是对称的。 当一个节点无法从另一个节点到达时，将对的距离设置为 255。

请注意， -**numa** 选项不分配任何指定的资源，它只是将现有资源分配给 NUMA 节点。 这意味着仍然必须使用 **\-m**, **\-smp** 选项来分别分配 RAM 和 VCPU。

使用 '**hmat-lb**' 在 ACPI 异构属性内存表 (HMAT) 中设置启动器和目标 NUMA 节点之间的系统位置延迟和带宽信息。 Initiator NUMA 节点可以创建内存请求，通常它有一个或多个处理器。 目标 NUMA 节点包含可寻址内存。

在 '**hmat-lb**' 选项中，节点是 NUMA 节点 ID。 hierarchy 是目标NUMA节点的内存层次结构：如果 hierarchy 是 'memory', 这个结构体代表内存性能；如果层次结构是 'first-level|second-level|third-level', 则此结构表示每个域的内存端缓存的聚合性能。 'data-type' 的类型是这个结构实例表示的数据类型：如果 'hierarchy' 是 'memory', 'data-type' 是 'access|read|write' 延迟或 'access|read|write' 带宽目标内存；如果 'hierarchy' 是 'first-level|second-level|third-level', 'data-type' is 'access|read|write' 命中延迟或 'access|read|write' 目标内存端缓存的命中带宽.

lat 是以纳秒为单位的延迟值。 bw 是带宽值，可能的值和单位是 NUM\[M|G|T\]，表示带宽值是每秒 NUM 字节（或 MB/s、GB/s 或 TB/s，取决于使用的后缀）。 请注意，如果延迟或带宽值为 0，则表示未提供相应的延迟或带宽信息。

在 '**hmat-cache**' 选项中， node-id 是内存所属的 NUMA-id 。是内存端缓存的大小（以字节为单位）。 level 是此结构中描述的缓存级别，请注意缓存级别 0 不应与 '**hmat-cache**' 选项一起使用。 associativity 是缓存关联性，可能的值是 'none/direct(direct-mapped)/complex(complex cache indexing)' 。 策略是写策略。line 是以字节为单位的缓存行大小。

例如，以下选项描述了 2 个 NUMA 节点。 节点 0 有 2 个 CPU 和一个内存，节点 1 只有一个内存。 节点 0 中的处理器访问节点 0 中的内存，访问延迟为 5 纳秒，访问带宽为 200 MB/s；NUMA 节点 0 中的处理器访问 NUMA 节点 1 中的内存，访问延迟为 10 纳秒，访问带宽为 100 MB/s。 而对于内存端缓存信息，NUMA节点0和1都有1级内存缓存，大小为10KB，策略为回写，缓存行大小为8字节：

\-machine hmat=on \\ -m 2G \\ -object memory-backend-ram,size=1G,id=m0 \\ -object memory-backend-ram,size=1G,id=m1 \\ -smp 2,sockets=2,maxcpus=2 \\ -numa node,nodeid=0,memdev=m0 \\ -numa node,nodeid=1,memdev=m1,initiator=0 \\ -numa cpu,node-id=0,socket-id=0 \\ -numa cpu,node-id=0,socket-id=1 \\ -numa hmat-lb,initiator=0,target=0,hierarchy=memory,data-type=access-latency,latency=5 \\ -numa hmat-lb,initiator=0,target=0,hierarchy=memory,data-type=access-bandwidth,bandwidth=200M \\ -numa hmat-lb,initiator=0,target=1,hierarchy=memory,data-type=access-latency,latency=10 \\ -numa hmat-lb,initiator=0,target=1,hierarchy=memory,data-type=access-bandwidth,bandwidth=100M \\ -numa hmat-cache,node-id=0,size=10K,level=1,associativity=direct,policy=write-back,line=8 \\ -numa hmat-cache,node-id=1,size=10K,level=1,associativity=direct,policy=write-back,line=8 

-

-

****\-add-fd fd=fd,set=set\[,opaque=opaque\]****

将文件描述符添加到 fd 集。 有效的选项是：

****fd=fd****

此选项定义将其副本添加到 fd 集的文件描述符。 文件描述符不能是标准输入、标准输出或标准错误。

****set=set****

此选项定义要添加文件描述符的 fd 集的 ID。

****opaque=opaque****

此选项定义可用于描述 fd 的自由格式字符串。

-

您可以使用 fd 集中预先打开的文件描述符打开图像：

qemu-system-x86\_64 \\ -add-fd fd=3,set=2,opaque="rdwr:/path/to/file" \\ -add-fd fd=4,set=2,opaque="rdonly:/path/to/file" \\ -drive file=/dev/fdset/2,index=0,media=disk 

-

-

****\-set group.id.arg=value****

为类型组的项目 ID 设置参数 arg

****\-global driver.prop=value****

****\-global driver=driver,property=property,value=value****

将驱动程序属性 prop 的默认值设置为 value，例如：

qemu-system-x86\_64 -global ide-hd.physical\_block\_size=4096 disk-image.img 

-

-

特别是，您可以使用它来设置由机器模型自动创建的设备的驱动程序属性。要创建不是自动创建的设备并在其上设置属性，请使用 -**device**。

\-global driver.prop=value 是 -global driver=driver,property=prop,value=value 的简写。 即使驱动程序包含点，速记语法也有效。

****\-boot \[order=drives\]\[,once=drives\]\[,menu=on|off\]\[,splash=sp\_name\]\[,splash-time=sp\_time\]\[,reboot-timeout=rb\_timeout\]\[,strict=on|off\]****

将引导顺序驱动器指定为驱动器号字符串。 有效的驱动器号取决于目标体系结构。 x86 PC 使用：a、b（软盘 1 和 2）、c（第一个硬盘）、d（第一个 CD-ROM), n-p （从网络适配器 1-4 的以太网引导），硬盘引导是默认设置。 要仅在第一次启动时应用特定的引导顺序，请通过 **once** 指定它。 请注意， **order** 或 **once** 参数不应与设备的 **bootindex** 属性一起使用，因为固件实现通常不会同时支持两者。

只要固件/BIOS 支持，交互式启动菜单/提示可以通过 **menu=on** 启用。 默认为非交互式引导。

可以将Splash图片传递给BIOS，从而使用户可以将其显示为徽标，当option splash = sp\_name时，如果固件/bios支持它们，则可以将其显示为徽标。 目前 Seabios for X86 系统支持。限制：splash 文件可以是 24 BPP 格式（真彩色）的 jpeg 文件或 BMP 文件。 分辨率应该是SVGA模式支持的，所以推荐320x240、640x480、800x640。

可以将超时传递给 bios，当启动失败时，guest 将暂停 rb\_timeout ms，然后重新启动。 如果 rb\_timeout 为 '-1', guest 将不会重新启动，qemu 默认将 '-1' 传递给 bios。 目前 Seabios for X86 系统支持。

只要固件/BIOS 支持，请通过 **strict=on** 进行严格引导。 这仅在 bootindex 选项更改引导优先级时有效。 默认为非严格引导。

\# try to boot from network first, then from hard disk qemu-system-x86\_64 -boot order=nc # boot from CD-ROM first, switch back to default order after reboot qemu-system-x86\_64 -boot once=d # boot with a splash picture for 5 seconds. qemu-system-x86\_64 -boot menu=on,splash=/root/boot.bmp,splash-time=5000 

-

-

注意：仍然支持旧格式 '-boot drives' ，但不鼓励使用它，因为它可能会从未来的版本中删除。

****\-m \[size=\]megs\[,slots=n,maxmem=size\]****

将客户机启动 RAM 大小设置为 megs 兆字节。 默认值为 128 MiB。 可选地，后缀 "M" 或 "G" 可用于分别表示以兆字节或千兆字节为单位的值。 可选对插槽，maxmem 可用于设置热插拔内存插槽数量和最大内存数量。 请注意，maxmem 必须与页面大小对齐。

例如，以下命令行将客户机启动 RAM 大小设置为 1GB，创建 3 个插槽以热插拔额外内存，并将客户机可以达到的最大内存设置为 4GB：

qemu-system-x86\_64 -m 1G,slots=3,maxmem=4G 

-

-

如果未指定 slot 和 maxmem，则不会启用内存热插拔，并且客户机启动 RAM 将永远不会增加。

****\-mem-path path****

从路径中临时创建的文件分配来宾 RAM。

****\-mem-prealloc****

使用 -mem-path 时预分配内存。

****\-k language****

使用键盘布局语言（例如法语的 **fr** ）。 只有在不容易获得原始 PC 密钥代码的情况下才需要此选项（例如，在 Mac 上，带有一些 X11 服务器或带有 VNC 或 curses 显示器）。 您通常不需要在 PC/Linux 或 PC/Windows 主机上使用它。

可用的布局是：

ar de-ch es fo fr-ca hu ja mk no pt-br sv da en-gb et fr fr-ch is lt nl pl ru th de en-us fi fr-be hr it lv nl-be pt sl tr 

-

-

默认值为 **en-us**。

****\-audio-help****

将显示当前指定（已弃用）环境变量的 -audiodev 等效项。

****\-audiodev \[driver=\]driver,id=id\[,prop\[=value\]\[,...\]\]****

添加由 id 标识的新音频后端驱动程序。 有全局和驱动程序特定的属性。 有些值可以为输入和输出设置不同的值，它们用 **in|out.** 标记。 您可以使用 **in.prop** 设置输入的属性，使用 **out.prop** 设置输出的属性。 例如：

\-audiodev alsa,id=example,in.frequency=44110,out.frequency=8000 -audiodev alsa,id=example,out.channels=1 # leaves in.channels unspecified 

-

-

注意：已知参数验证是不完整的，在许多情况下指定无效选项会导致 QEMU 打印错误消息并继续模拟而没有声音。

有效的全局选项是：

****id=identifier****

标识音频后端。

****timer-period=period****

设置音频子系统使用的计时器周期（以微秒为单位）。 默认值为 10000（10 毫秒）。

****in|out.mixing-engine=on|off****

使用 QEMU 的混合引擎混合 QEMU 内部的所有流，并在后端不支持时转换音频格式。 关闭时，固定设置也必须关闭。 请注意，禁用此选项意味着所选后端必须支持多个流和虚拟卡使用的音频格式，否则您将听不到声音。 除非您想使用 5.1 或 7.1 音频，否则不建议禁用此选项，因为混合引擎仅支持单声道和立体声音频。 默认开启。

****in|out.fixed-settings=on|off****

对主机音频使用固定设置。 关闭时，它将根据客人打开声卡的方式而改变。 在这种情况下，您不得指定频率、频道或格式。 默认开启

****in|out.frequency=frequency****

指定使用固定设置时使用的频率。 默认值为 44100Hz。

****in|out.channels=channels****

指定使用固定设置时要使用的通道数。 默认值为 2（立体声）。

****in|out.format=format****

指定使用固定设置时要使用的样本格式。 有效值为: **s8**, **s16**, **s32**, **u8**, **u16**, **u32**, **f32** 。 默认为 **s16** 。

****in|out.voices=voices****

指定要使用的声音数量。 默认值为 1。

****in|out.buffer-length=usecs****

以微秒为单位设置缓冲区的大小。

-

****\-audiodev none,id=id\[,prop\[=value\]\[,...\]\]****

创建一个丢弃所有输出的虚拟后端。 此后端没有后端特定属性。

****\-audiodev alsa,id=id\[,prop\[=value\]\[,...\]\]****

使用 ALSA 创建后端。 此后端仅在 Linux 上可用。

ALSA 特定选项是：

****in|out.dev=device****

指定用于输入和/或输出的 ALSA 设备。 默认为 **default**。

****in|out.period-length=usecs****

以微秒为单位设置周期长度。

****in|out.try-poll=on|off****

尝试对设备使用轮询模式。 默认开启。

****threshold=threshold****

播放开始时的阈值（以微秒为单位）。 默认值为 0。

-

****\-audiodev coreaudio,id=id\[,prop\[=value\]\[,...\]\]****

使用 Apple 的 Core Audio 创建后端。 此后端仅在 Mac OS 上可用，并且仅支持播放。

核心音频特定选项是：

****in|out.buffer-count=count****

设置缓冲区的计数。

-

****\-audiodev dsound,id=id\[,prop\[=value\]\[,...\]\]****

使用 Microsoft 的 DirectSound 创建后端。 此后端仅在 Windows 上可用，并且仅支持播放。

DirectSound 特定选项是：

****latency=usecs****

为播放添加额外的 usecs 微秒延迟。 默认值为 10000（10 毫秒）。

-

****\-audiodev oss,id=id\[,prop\[=value\]\[,...\]\]****

使用 OSS 创建后端。 这个后端在大多数类 Unix 系统上都可用。

OSS 特定选项是：

****in|out.dev=device****

指定要使用的 OSS 设备的文件名。 默认为 **/dev/dsp**。

****in|out.buffer-count=count****

设置缓冲区的计数。

****in|out.try-poll=on|of****

尝试对设备使用轮询模式。 默认开启。

****try-mmap=on|off****

尝试使用内存映射设备访问。默认为关闭。

****exclusive=on|off****

以独占模式打开设备（在这种情况下，vmix 不起作用）。 默认为关闭。

****dsp-policy=policy****

设置计时策略（介于 0 和 10 之间，数字越小意味着延迟越小，但 CPU 使用率越高）。 使用 -1 使用由 **buffer** 和 **buffer-count** 指定的缓冲区大小。 如果您没有 OSS 4，则忽略此选项。 默认值为 5。

-

****\-audiodev pa,id=id\[,prop\[=value\]\[,...\]\]****

使用 PulseAudio 创建后端。 此后端可在大多数系统上使用。

PulseAudio 特定选项是：

****server=server****

设置要连接的 PulseAudio 服务器。

****in|out.name=sink****

使用指定的源/接收器进行录制/播放。

****in|out.latency=usecs****

所需的延迟（以微秒为单位）。 PulseAudio 服务器将尝试遵守此值，但实际延迟可能会更低或更高。

-

****\-audiodev sdl,id=id\[,prop\[=value\]\[,...\]\]****

使用 SDL 创建后端。 此后端在大多数系统上都可用，但如果可能，您应该使用平台的本机后端。

SDL 特定选项包括：

****in|out.buffer-count=count****

设置缓冲区的计数。

-

****\-audiodev spice,id=id\[,prop\[=value\]\[,...\]\]****

创建一个通过 SPICE 发送音频的后端。 此后端需要 **\-spice** 并在这种情况下自动选择，因此通常您可以忽略此选项。 此后端没有后端特定属性。

****\-audiodev wav,id=id\[,prop\[=value\]\[,...\]\]****

创建一个将音频写入 WAV 文件的后端。

后端特定选项是：

****path=path****

将录制的音频写入指定文件。 默认为 **qemu.wav**。

-

****\-soundhw card1\[,card2,...\] or -soundhw all****

启用音频和选定的声音硬件。 使用 'help' 打印所有可用的声音硬件。例如：

qemu-system-x86\_64 -soundhw sb16,adlib disk.img qemu-system-x86\_64 -soundhw es1370 disk.img qemu-system-x86\_64 -soundhw ac97 disk.img qemu-system-x86\_64 -soundhw hda disk.img qemu-system-x86\_64 -soundhw all disk.img qemu-system-x86\_64 -soundhw help 

-

-

请注意，Linux 的 i810\_audio OSS 内核（用于 AC97）模块可能需要手动指定时钟。

modprobe i810\_audio clocking=48000 

-

-

****\-device driver\[,prop\[=value\]\[,...\]\]****

添加设备驱动程序。 prop=value 设置驱动程序属性。有效属性取决于驱动程序。 要获得有关可能的驱动程序和属性的帮助，请使用 **\-device help** 和 **\-device driver,help**。

一些驱动程序是：

****\-device ipmi-bmc-sim,id=id\[,prop\[=value\]\[,...\]\]****

添加 IPMI BMC。 这是对通常位于系统上的硬件管理接口处理器的模拟。 它提供了一个看门狗以及对系统进行复位和电源控制的能力。 您需要将其连接到 IPMI 接口以使其有用

用于 BMC 的 IPMI 从属地址。 默认值为 0x20。 此地址是管理控制器 I2C 网络上 BMC 的地址。 如果你不知道这意味着什么，忽略它是安全的。

****id=id****

使用此设备的接口的 BMC id。

****slave\_addr=val****

定义用于 BMC 的从地址。默认值为 0x20。

****sdrfile=file****

包含原始传感器数据记录 (SDR) 数据的文件。 默认值为无。

****fruareasize=val****

现场可更换单元 (FRU) 区域的大小。 默认值为 1024。

****frudatafile=file****

包含原始现场可更换单元 (FRU) 库存数据的文件。默认值为无。

****guid=uuid****

BMC 的 GUID 值，采用标准 UUID 格式。 如果已设置，获取 "Get GUID" 命令给 BMC 将返回它。否则 "Get GUID" 将返回错误。

-

****\-device ipmi-bmc-extern,id=id,chardev=id\[,slave\_addr=val\]****

添加与外部 IPMI BMC 模拟器的连接。 不是像上面那样在本地模拟 BMC，而是连接到提供 IPMI 服务的外部实体。

连接到外部 BMC 模拟器。 如果这样做，强烈建议您在连接丢失时使用 "reconnect=" chardev 选项重新连接到模拟器。 请注意，如果不小心使用它，则可能是一个安全问题，因为该接口具有发送重置、NMI 和关闭 VM 电源的能力。 最好 QEMU 连接到在 localhost 的安全端口上运行的外部模拟器，这样模拟器和 QEMU 都不会暴露给任何外部网络。

有关外部接口的更多详细信息，请参见 OpenIPMI 库中的 "lanserv/README.vm" 文件。

****\-device isa-ipmi-kcs,bmc=id\[,ioport=val\]\[,irq=val\]****

在 ISA 总线上添加 KCS IPMI 接口。 如果合适，这还会添加相应的 ACPI 和 SMBIOS 条目。

****bmc=id****

要连接的 BMC，上面的 ipmi-bmc-sim 或 ipmi-bmc-extern 之一。

****ioport=val****

定义接口的 I/O 地址。 KCS 的默认值为 0xca0。

****irq=val****

定义要使用的中断。默认值为 5。 要禁用中断，请将其设置为 0。

-

****\-device isa-ipmi-bt,bmc=id\[,ioport=val\]\[,irq=val\]****

与KCS接口类似，但定义了BT接口。 默认端口为 0xe4，默认中断为 5。

****\-device pci-ipmi-kcs,bmc=id****

在 PCI 总线上添加一个 KCS IPMI 接口。

****bmc=id****

要连接的 BMC，上面的 ipmi-bmc-sim 或 ipmi-bmc-extern 之一。

-

****\-device pci-ipmi-bt,bmc=id****

与KCS接口类似，但在PCI总线上定义了一个BT接口。

****\-device intel-iommu\[,option=...\]****

这仅受 **\-machine q35** 支持，它将在来宾中启用 Intel VT-d 仿真。 它支持以下选项：

****intremap=on|off** (default: auto)**

这将启用中断重新映射功能。 需要启用完整的 x2apic。 目前只支持 **off** 或 **split** kvm kernel-irqchip 模式，还不支持 full kernel-irqchip 。 默认值为 "auto" ，由 kernel-irqchip 的模式决定。

****caching-mode=on|off** (default: off)**

这将为 VT-d 仿真设备启用缓存模式。 启用缓存模式后，每个来宾 DMA 缓冲区映射都会以同步方式从来宾 IOMMU 驱动程序到 vIOMMU 设备生成 IOTLB 失效。 **\-device vfio-pci** 需要使用 VT-d 设备，因为主机分配的设备需要在来宾 DMA 启动之前在主机上设置 DMA 映射。

****device-iotlb=on|off** (default: off)**

这为模拟的 VT-d 设备启用了 device-iotlb 功能。 到目前为止，virtio/vhost 应该是该参数的唯一真实用户，与为设备配置的 ats=on 配对。

****aw-bits=39|48** (default: 39)**

这决定了 IOVA 地址空间的地址宽度。 地址空间对于 3 级 IOMMU 页表有 39 位宽度，对于 4 级 IOMMU 页表有 48 位宽度。

-

有关 QEMU 中 VT-d 仿真的一般场景，请参阅 wiki 页面： _https://wiki.qemu.org/Features/VT-d_。

****\-name name****

设置来宾的名称。 此名称将显示在 SDL 窗口标题中。 该名称也将用于 VNC 服务器。 还可以选择在 Linux 中设置顶部可见的进程名称。 也可以在 Linux 上启用单个线程的命名以帮助调试。

****\-uuid uuid****

设置系统 UUID。

-

[块设备选项](#__u5757___u8BBE___u5907___u9009___u9879_)
--------------------------------------------------

****\-fda file****

****\-fdb file****

使用文件作为软盘 0/1 映像（请参阅系统仿真用户指南中的磁盘映像章节）。

****\-hda file****

****\-hdb file****

****\-hdc file****

****\-hdd file****

将文件用作硬盘 0、1、2 或 3 映像（请参阅系统仿真用户指南中的磁盘映像章节）。

****\-cdrom file****

使用 file 作为 CD-ROM 映像（不能同时使用 **\-hdc** 和 **\-cdrom** ）。 您可以通过使用 **/dev/cdrom** 作为文件名来使用主机 CD-ROM 。

****\-blockdev option\[,option\[,option\[,...\]\]\]****

定义一个新的块驱动节点。 一些选项适用于所有块驱动程序，其他选项仅适用于特定的块驱动程序。 有关最常见块驱动程序的通用选项和选项的列表，请参见下文。

期望引用另一个节点（例如 **file** ）的选项可以通过两种方式给出。 您可以指定现有节点的节点名称 (file=node-name), 或者定义一个新的内联节点，在点后添加引用节点的选项 (file.filename=path,file.aio=native)。

使用 **\-blockdev** 创建的块驱动程序节点可用于来宾设备，方法是在定义块设备的 **\-device** 参数中为 **drive** 属性指定其节点名称。

****任何块驱动节点的有效选项：****

****driver****

指定用于给定节点的块驱动程序。

****node-name****

这定义了稍后将引用的块驱动程序节点的名称。 该名称必须是唯一的，即它不能与不同块驱动节点的名称匹配，或者（如果您也使用 **\-drive** ）驱动器的ID。

如果没有指定节点名，则自动生成。 生成的节点名称不是可预测的，并且在 QEMU 调用之间会发生变化。 对于顶级，必须指定显式节点名称。

****read-only****

以只读方式打开节点。 来宾写入尝试将失败。

请注意，某些块驱动程序通常或在某些配置中仅支持只读访问。 在这种情况下，默认值 **read-only=off** 不起作用，必须明确指定选项。

****auto-read-only****

如果设置了 **auto-read-only=on** ，即使请求 **read-only=off** ，QEMU 也可能回退到只读使用，甚至根据需要在模式之间切换，例如取决于图像文件是否可写或是否写入用户附加到节点。

****force-share****

通过强制节点在通常会请求独占访问的情况下使用较弱的共享访问权限来覆盖 QEMU 的图像锁定系统。 当多个实例有可能打开同一个文件时（无论此 QEMU 调用是第一个实例还是第二个实例），两个实例都必须允许共享访问，第二个实例才能成功打开文件。

启用 **force-share=on** 需要 **read-only=on**。

****cache.direct****

使用 **cache.direct=on** 可以避免主机页面缓存。 这将尝试直接对来宾的内存进行磁盘 IO。 QEMU 可能仍会执行数据的内部副本。

****cache.no-flush****

如果您不关心主机故障时的数据完整性，您可以使用 **cache.no-flush=on** 。 这个选项告诉 QEMU 它永远不需要将任何数据写入磁盘，而是可以将内容保存在缓存中。 如果出现任何问题，例如您的主机断电、磁盘存储意外断开连接等。 您的图像很可能会变得无法使用。

****discard=discard****

丢弃是 "ignore" (或 "off") 或 "unmap" (或 "on") 之一，并控制 **discard** (也称为 **trim** 或 **unmap**) 请求是否被忽略或传递给文件系统。 某些机器类型可能不支持丢弃请求。

****detect-zeroes=detect-zeroes****

detect-zeroes 为 "off", "on" 或 "unmap" ，并启用操作系统将纯零写入自动转换为驱动程序特定优化的零写入命令。 如果将丢弃设置为 "unmap" 以允许将零写入转换为 **unmap** 操作，您甚至可以选择 "unmap" 。

-

****文件的驱动程序特定选项****

这是用于访问常规文件的协议级块驱动程序。

****filename****

本地文件系统中图像文件的路径

****aio****

指定 AIO 后端（threads/native/io\_uring，默认值：threads）

****locking****

指定是否使用 Linux OFD / POSIX 锁保护映像文件。 默认是使用 Linux Open File Descriptor API（如果可用），否则不应用锁定。（自动/开/关，默认：自动）

-

例子：

\-blockdev driver=file,node-name=disk,filename=disk.img 

-

-

****raw 的驱动程序特定选项****

这是用于原始图像的图像格式块驱动程序。 它通常堆叠在诸如 **file** 之类的协议级块驱动程序之上。

****file****

引用或定义数据源块驱动节点（例如 **file** 驱动节点）

-

示例 1：

\-blockdev driver=file,node-name=disk\_file,filename=disk.img -blockdev driver=raw,node-name=disk,file=disk\_file 

-

-

示例 2：

\-blockdev driver=raw,node-name=disk,file.driver=file,file.filename=disk.img 

-

-

****qcow2 的驱动程序特定选项****

这是 qcow2 图像的图像格式块驱动程序。 它通常堆叠在诸如 **file** 之类的协议级块驱动程序之上。

****file****

引用或定义数据源块驱动节点（例如 **file** 驱动节点）

****backing****

对支持文件块设备的引用或定义（默认取自图像文件）。 允许在此处传递 **null** 以禁用默认支持文件。

****lazy-refcounts****

是否启用惰性引用计数功能（开/关；默认取自图像文件）

****cache-size****

L2 表和 refcount 块缓存的最大总大小（以字节为单位）（默认值： l2-cache-size 和 refcount-cache-size 的总和）

****l2-cache-size****

L2 表缓存的最大大小（以字节为单位）（默认值：如果未指定缓存大小， Linux 平台上为 32M，非 Linux 平台上为 8M；否则，在缓存大小内尽可能大，同时允许请求或最小引用计数缓存大小）

****refcount-cache-size****

refcount 块缓存的最大大小（以字节为单位）（默认值：集群大小的 4 倍；或者如果指定了 cache-size ，则它的不用于 L2 缓存的部分）

****cache-clean-interval****

清理 L2 和 refcount 缓存中未使用的条目。 间隔以秒为单位。 支持平台默认值为 600，其他平台默认值为 0。 将其设置为 0 将禁用此功能。

****pass-discard-request****

对 qcow2 设备的丢弃请求是否应该转发到数据源（开/关；默认值：如果指定了discard=unmap，则打开，否则关闭）

****pass-discard-snapshot****

当快照操作（例如删除快照）释放 qcow2 文件中的集群时，是否应发出对数据源的丢弃请求（开/关；默认值：开）

****pass-discard-other****

是否应该在集群被释放的其他情况下发出数据源的丢弃请求（开/关；默认值：关）

****overlap-check****

对图像的写入执行哪些重叠检查 (none/constant/cached/all; 默认值: cached)。 有关详细信息或更精细的粒度控制，请参阅 **blockdev-add** 的 QAPI 文档。

-

示例 1：

\-blockdev driver=file,node-name=my\_file,filename=/tmp/disk.qcow2 -blockdev driver=qcow2,node-name=hda,file=my\_file,overlap-check=none,cache-size=16777216 

-

-

示例 2：

\-blockdev driver=qcow2,node-name=disk,file.driver=http,file.filename=http://example.com/image.qcow2 

-

-

****其他驱动程序的驱动程序特定选项****

请参考 **blockdev-add** QMP 命令的 QAPI 文档。

-

****\-drive option\[,option\[,option\[,...\]\]\]****

这包括创建一个块驱动节点（后端）以及一个来宾设备，并且主要是定义相应的 **\-blockdev** 和 **\-device** 选项的快捷方式。

**\-drive** 接受 **\-blockdev** 接受的所有选项。 此外，它知道以下选项：

****file=file****

此选项定义与此驱动器一起使用的磁盘映像（请参阅系统仿真用户指南中的磁盘映像章节）。 如果文件名包含逗号，则必须将其加倍（例如， "file=my,,file" 以使用文件 "my,file")。

可以使用特定于协议的 URL 指定特殊文件，例如 iSCSI 设备。 有关详细信息，请参阅 "Device URL Syntax" 部分。

****if=interface****

此选项定义驱动器连接的接口类型。 可用类型有： ide, scsi, sd, mtd, floppy, pflash, virtio, none。

****bus=bus,unit=unit****

这些选项通过定义总线编号和单元 ID 来定义驱动器的连接位置。

****index=index****

此选项通过使用给定接口类型的可用连接器列表中的索引来定义驱动器的连接位置。

****media=media****

此选项定义媒体的类型：磁盘或 cdrom。

****snapshot=snapshot****

snapshot 是 "on" 或 "off" 并控制给定驱动器的快照模式（请参阅 **\-snapshot**)。

****cache=cache****

cache 是 "none", "writeback", "unsafe", "directsync" 或 "writethrough" ，并控制如何使用主机缓存访问块数据。 这是设置 **cache.direct** 和 **cache.no-flush** 选项的快捷方式（如 **\-blockdev** 中), 另外还有 **cache.writeback**, 它为块客户机设备的 **write-cache** 选项提供默认值（如 **\-device** 中） . 这些模式对应于以下设置：

cache.writeback

cache.direct

cache.no-flush

writeback

on

off

off

none

on

on

off

writethrough

off

off

off

directsync

off

on

off

unsafe

on

off

on

默认模式是 **cache=writeback**。

****aio=aio****

aio 是 "threads", "native" 或 "io\_uring" ，可在基于 pthread 的磁盘 I/O、本机 Linux AIO 或 Linux io\_uring API 之间进行选择。

****format=format****

指定将使用哪种磁盘格式而不是检测格式。 可用于指定 format=raw 以避免解释不受信任的格式标头。

****werror=action,rerror=action****

指定对写入和读取错误采取的操作。 有效动作有： "ignore" (忽略错误并尝试继续), "stop" (暂停 QEMU), "report" (向客户机报告错误), "enospc" (仅当主机磁盘已满时才暂停 QEMU ; 否则向客人报告错误）。 默认设置是 **werror=enospc** 和 **rerror=report**。

****copy-on-read=copy-on-read****

copy-on-read 是 "on" 或 "off" ，并启用是否将读取的备份文件扇区复制到映像文件中。

****bps=b,bps\_rd=r,bps\_wr=w****

为所有请求类型或仅针对读取或写入指定带宽限制（以每秒字节数为单位）。 较小的值可能导致超时或在客户机内部挂起。 磁盘的安全最小值为 2 MB/s。

****bps\_max=bm,bps\_rd\_max=rm,bps\_wr\_max=wm****

为所有请求类型或仅针对读取或写入指定以每秒字节数为单位的突发。 突发允许来宾 I/O 暂时超过限制。

****iops=i,iops\_rd=r,iops\_wr=w****

以每秒请求数为单位指定请求速率限制，适用于所有请求类型或仅适用于读取或写入。

****iops\_max=bm,iops\_rd\_max=rm,iops\_wr\_max=wm****

为所有请求类型或仅针对读取或写入指定每秒请求的突发量。 突发允许来宾 I/O 暂时超过限制。

****iops\_size=is****

让请求的每一个字节都算作一个新的请求，以达到 iops 节流的目的。 使用此选项可防止访客通过发送更少但更大的请求来规避 iops 限制。

****group=g****

加入具有给定名称 g 的限制配额组。 属于同一组的所有驱动器一起计算。 使用此选项可防止来宾通过使用许多小磁盘而不是单个较大磁盘来规避限制。

-

默认情况下，使用 **cache.writeback=on** 模式。 一旦数据存在于主机页面缓存中，它将报告数据写入完成。 只要您的客户操作系统确保在需要的地方正确刷新磁盘缓存，这就是安全的。 如果您的客户操作系统无法正确处理易失性磁盘写入缓存并且您的主机崩溃或断电，那么客户可能会遇到数据损坏。

对于此类客人，您应该考虑使用 **cache.writeback=off** 。 这意味着主机页面缓存将用于读取和写入数据，但只有在 QEMU 确保将每次写入刷新到磁盘后，才会向客户机发送写入通知。 请注意，这会对性能产生重大影响。

使用 **\-snapshot** 选项时，始终使用不安全的缓存。

读取时复制可避免重复访问相同的备份文件扇区，并且在备份文件通过慢速网络时很有用。 默认情况下，读取时复制是关闭的。

您可以使用以下命令代替 **\-cdrom** :

qemu-system-x86\_64 -drive file=file,index=2,media=cdrom 

-

-

可以使用以下命令代替 **\-hda**, **\-hdb**, **\-hdc**, **\-hdd** :

qemu-system-x86\_64 -drive file=file,index=0,media=disk qemu-system-x86\_64 -drive file=file,index=1,media=disk qemu-system-x86\_64 -drive file=file,index=2,media=disk qemu-system-x86\_64 -drive file=file,index=3,media=disk 

-

-

可以使用 fd 集中预先打开的文件描述符打开图像：

qemu-system-x86\_64 \\ -add-fd fd=3,set=2,opaque="rdwr:/path/to/file" \\ -add-fd fd=4,set=2,opaque="rdonly:/path/to/file" \\ -drive file=/dev/fdset/2,index=0,media=disk 

-

-

可以将 CDROM 连接到 ide0 的从机：

qemu-system-x86\_64 -drive file=file,if=ide,index=1,media=cdrom 

-

-

如果您不指定 "file=" 参数，则定义一个空驱动器：

qemu-system-x86\_64 -drive if=ide,index=1,media=cdrom 

-

-

可以使用以下命令代替 **\-fda**, **\-fdb** :

qemu-system-x86\_64 -drive file=file,index=0,if=floppy qemu-system-x86\_64 -drive file=file,index=1,if=floppy 

-

-

默认情况下，接口是 "ide" 并且索引会自动递增：

qemu-system-x86\_64 -drive file=a -drive file=b" 

-

-

被解释为：

qemu-system-x86\_64 -hda a -hdb b 

-

-

****\-mtdblock file****

使用文件作为板载闪存映像。

****\-sd file****

使用文件作为 SecureDigital 卡图像。

****\-pflash file****

将文件用作并行闪存映像。

****\-snapshot****

写入临时文件而不是磁盘映像文件。 在这种情况下，您使用的原始磁盘映像不会被写回。 但是，您可以通过按 C-a s 强制回写（请参阅系统仿真用户指南中的磁盘映像章节）。

****\-fsdev local,id=id,path=path,security\_model=security\_model \[,writeout=writeout\]\[,readonly=on\]\[,fmode=fmode\]\[,dmode=dmode\] \[,throttling.option=value\[,throttling.option=value\[,...\]\]\]****

****\-fsdev proxy,id=id,socket=socket\[,writeout=writeout\]\[,readonly=on\]****

****\-fsdev proxy,id=id,sock\_fd=sock\_fd\[,writeout=writeout\]\[,readonly=on\]****

****\-fsdev synth,id=id\[,readonly=on\]****

定义一个新的文件系统设备。 有效的选项是：

****local****

对文件系统的访问由 QEMU 完成。

****proxy****

对文件系统的访问由 virtfs-proxy-helper(1) 完成。

****synth****

合成文件系统，仅由 QTests 使用。

****id=id****

指定此设备的标识符。

****path=path****

指定文件系统设备的导出路径。 此路径下的文件将可供来宾上的 9p 客户端使用。

****security\_model=security\_model****

指定要用于此导出路径的安全模型。支持的安全模型是 "passthrough", "mapped-xattr", "mapped-file" 和 "none" 。 在 "passthrough" 安全模型中，文件使用与在来宾上创建的相同凭据进行存储。 这需要 QEMU 以 root 身份运行。 在 "mapped-xattr" 安全模型中，一些文件属性如 uid、gid、模式位和链接目标被存储为文件属性。 对于 "mapped-file" ，这些属性存储在隐藏的 .virtfs\_metadata 目录中。 此安全模型导出的目录无法与其他 unix 工具交互。 "none" 安全模型与直通相同，只是服务器在设置文件属性（如所有权）失败时不会报告失败。 安全模型仅对本地 fsdriver 是强制性的。 其他 fsdrivers（如代理）不将安全模型作为参数。

****writeout=writeout****

这是一个可选参数。 唯一支持的值是 "immediate"。 这意味着主机页面缓存将用于读取和写入数据，但仅当数据已被报告为由存储子系统写入时，才会向客户机发送写入通知。

****readonly=on****

允许将 9p 共享导出为来宾的只读挂载。 默认情况下提供读写访问权限。

****socket=socket****

允许代理文件系统驱动程序使用传递的套接字文件与 virtfs-proxy-helper(1) 进行通信。

****sock\_fd=sock\_fd****

允许代理文件系统驱动程序使用传递的套接字描述符与 virtfs-proxy-helper(1) 进行通信。 通常，像 libvirt 这样的助手会创建 socketpair 并将其中一个 fds 作为 sock\_fd 传递。

****fmode=fmode****

指定主机上新创建文件的默认模式。 仅适用于安全模型 "mapped-xattr" 和 "mapped-file"。

****dmode=dmode****

指定主机上新创建目录的默认模式。 仅适用于安全模型 "mapped-xattr" 和 "mapped-file"。

****throttling.bps-total=b,throttling.bps-read=r,throttling.bps-write=w****

为所有请求类型或仅针对读取或写入指定带宽限制（以每秒字节数为单位）。

****throttling.bps-total-max=bm,bps-read-max=rm,bps-write-max=wm****

为所有请求类型或仅针对读取或写入指定以每秒字节数为单位的突发。 突发允许来宾 I/O 暂时超过限制。

****throttling.iops-total=i,throttling.iops-read=r, throttling.iops-write=w****

以每秒请求数为单位指定请求速率限制，适用于所有请求类型或仅适用于读取或写入。

****throttling.iops-total-max=im,throttling.iops-read-max=irm, throttling.iops-write-max=iwm****

为所有请求类型或仅针对读取或写入指定每秒请求的突发量。 突发允许来宾 I/O 暂时超过限制。

****throttling.iops-size=is****

让请求的每一个字节都算作一个新的请求，以达到 iops 节流的目的。

-

\-fsdev 选项与 -device driver "virtio-9p-..." 一起使用。

****\-device virtio-9p-type,fsdev=id,mount\_tag=mount\_tag****

virtio-9p-... 驱动程序的选项有：

****type****

指定要使用的变体。 支持的值为 "pci", "ccw" 或 "device", 具体取决于机器类型。

****fsdev=id****

指定与 -fsdev 选项一起指定的 id 值。

****mount\_tag=mount\_tag****

指定来宾用于挂载此导出点的标记名称。

-

****\-virtfs local,path=path,mount\_tag=mount\_tag ,security\_model=security\_model\[,writeout=writeout\]\[,readonly=on\] \[,fmode=fmode\]\[,dmode=dmode\]\[,multidevs=multidevs\]****

****\-virtfs proxy,socket=socket,mount\_tag=mount\_tag \[,writeout=writeout\]\[,readonly=on\]****

****\-virtfs proxy,sock\_fd=sock\_fd,mount\_tag=mount\_tag \[,writeout=writeout\]\[,readonly=on\]****

****\-virtfs synth,mount\_tag=mount\_tag****

定义一个新的虚拟文件系统设备并使用 virtio-9p-device (a.k.a. 9pfs)将其公开给来宾，这实质上意味着来宾可以通过使用 9P 直接访问主机上的某个目录作为传递文件系统主机和来宾之间通信的网络协议，如果需要，甚至可以访问，由多个来宾同时共享。

请注意， **\-virtfs** 实际上只是其通用形式 **\-fsdev -device virtio-9p-pci** 的便捷快捷方式。

传递文件系统选项的一般形式是：

****local****

对文件系统的访问由 QEMU 完成。

****proxy****

对文件系统的访问由 virtfs-proxy-helper(1) 完成。

****synth****

合成文件系统，仅由 QTests 使用。

****id=id****

指定文件系统设备的标识符

****path=path****

指定文件系统设备的导出路径。 此路径下的文件将可供来宾上的 9p 客户端使用。

****security\_model=security\_model****

指定要用于此导出路径的安全模型。支持的安全模型是 "passthrough", "mapped-xattr", "mapped-file" 和 "none" 。 在 "passthrough" 安全模型中，文件使用与在来宾上创建的相同凭据进行存储。 这需要 QEMU 以 root 身份运行。 在 "mapped-xattr" 安全模型中，一些文件属性如 uid、gid、模式位和链接目标被存储为文件属性。 对于 "mapped-file" ，这些属性存储在隐藏的 .virtfs\_metadata 目录中。 此安全模型导出的目录无法与其他 unix 工具交互。 "none" 安全模型与直通相同，只是服务器在设置文件属性（如所有权）失败时不会报告失败。 安全模型仅对本地 fsdriver 是强制性的。 其他 fsdrivers（如代理）不将安全模型作为参数。

****writeout=writeout****

这是一个可选参数。 唯一支持的值是 "immediate" 。 这意味着主机页面缓存将用于读取和写入数据，但仅当数据已被报告为由存储子系统写入时，才会向客户机发送写入通知。

****readonly=on****

允许将 9p 共享导出为来宾的只读挂载。 默认情况下提供读写访问权限。

****socket=socket****

允许代理文件系统驱动程序使用传递的套接字文件与 virtfs-proxy-helper(1) 进行通信。 通常，像 libvirt 这样的助手会创建 socketpair 并将其中一个 fds 作为 sock\_fd 传递。

****sock\_fd****

允许代理文件系统驱动程序使用传递的 'sock\_fd' 作为与 virtfs-proxy-helper(1) 交互的套接字描述符。

****fmode=fmode****

指定主机上新创建文件的默认模式。仅适用于安全模型 "mapped-xattr" 和 "mapped-file"。

****dmode=dmode****

指定主机上新创建目录的默认模式。仅适用于安全模型 "mapped-xattr" 和 "mapped-file"。

****mount\_tag=mount\_tag****

指定来宾用于挂载此导出点的标记名称。

****multidevs=multidevs****

指定如何处理通过 9p 导出共享的多个设备。 支持的行为是 "remap", "forbid" 或 "warn" 。 后者是 virtfs 9p 期望只有一个设备与同一个导出共享的默认行为，如果通过同一个 9p 导出共享和访问多个设备，那么 qemu on 只会记录（一次）警告消息主机端。 为了避免来宾上的文件 ID 冲突，您应该为要与来宾共享的每个设备创建一个单独的 virtfs 导出（推荐方式），或者您可以使用 "remap" ，它允许您仅通过一个导出共享多个设备，这是通过以防止此类冲突的方式将原始 inode 编号从主机重新映射到客户机来实现的。 在这种用例中需要重新映射 inode，因为来自主机的原始设备 ID 永远不会传递并暴露在来宾上。 相反，与 virtfs 共享的所有导出文件始终在来宾上共享相同的设备 ID。 因此，两个具有相同 inode 编号但来自主机上实际不同设备的文件会导致文件 ID 冲突，从而导致客户机上的潜在不当行为。 另一方面， "forbid" 假设像 "warn" 一样，同一导出仅共享一个设备，但是它不仅会记录警告消息，还会拒绝访问来宾上的其他设备。 请注意，尽管 "forbid" 当前不会阻止所有可能的文件访问操作（例如 readdir() 仍会从其他设备返回条目）。

-

****\-iscsi****

配置 iSCSI 会话参数。

-

[USB 便利选项](#USB___u4FBF___u5229___u9009___u9879_)
-------------------------------------------------

****\-usb****

在具有板载 USB 主机控制器的机器类型上启用 USB 仿真（如果默认情况下未启用）。 请注意，板载 USB 主机控制器可能不支持 USB 3.0。 在这种情况下 **\-device qemu-xhci** 可以在带有 PCI 的机器上使用。

****\-usbdevice devname****

添加 USB 设备 devname，并在可能和必要时启用板载 USB 控制器（就像可以通过 **\-machine usb=on** 完成一样）。 请注意，此选项主要是为了方便用户。 通过选择 USB 主机控制器（如果需要）和通过 **\-device** 选项选择所需的 USB 设备，可以实现更细粒度的控制。 例如，可以不使用 **\-usbdevice mouse** 而是使用 **\-device qemu-xhci -device usb-mouse** 将 USB 鼠标连接到 USB 3.0 控制器（至少在支持 PCI 且没有 USB 控制器的机器上）默认情况下启用）。 有关详细信息，请参阅系统仿真用户指南中有关连接 USB 设备的章节。 devname 的可能设备有：

****braille****

盲文设备。 这将使用 BrlAPI 在真机或假设备上显示盲文输出（即，它还会在 **usb-braille** USB 设备旁边自动创建相应的 **braille** chardev ）。

****keyboard****

标准 USB 键盘。将覆盖 PS/2 键盘（如果存在）。

****mouse****

虚拟鼠标。 这将在激活时覆盖 PS/2 鼠标仿真。

****tablet****

使用绝对坐标的指针设备（如触摸屏）。 这意味着 QEMU 能够报告鼠标位置而无需抓住鼠标。 激活时还会覆盖 PS/2 鼠标仿真。

****wacom-tablet****

Wacom PenPartner USB 数位板。

-

-

[显示选项](#__u663E___u793A___u9009___u9879_)
-----------------------------------------

****\-display type****

选择要使用的显示器类型。 此选项是旧样式 -sdl/-curses/... 选项的替代品。 使用 **\-display help** 列出可用的显示类型。类型的有效值为

****spice-app\[,gl=on|off\]****

启动 QEMU 作为 Spice 服务器并启动默认的 Spice 客户端应用程序。 Spice 服务器将重定向串行控制台和 QEMU 监视器。（自 4.0 起）

****sdl****

通过 SDL 显示视频输出（通常在单独的图形窗口中；有关其他可能性，请参阅 SDL 文档）。有效参数是：

**grab-mod=<mods>** : 用于选择修饰键，以与 "g" 键一起切换鼠标抓取。 **<mods>** 可以是 **lshift-lctrl-lalt** 或 **rctrl**。

**alt\_grab=on|off** : 使用 Control+Alt+Shift-g 切换鼠标抓取。 此参数已弃用 - 请改用 **grab-mod** 。

**ctrl\_grab=on|off** : 使用 Right-Control-g 切换鼠标抓取。 此参数已弃用 - 请改用 **grab-mod** 。

**gl=on|off|core|es** : 使用 OpenGL 进行显示

**show-cursor=on|off** : 强制显示鼠标光标

**window-close=on|off** : 允许使用窗口关闭按钮退出 qemu

****gtk****

在 GTK 窗口中显示视频输出。 此界面提供下拉菜单和其他 UI 元素，以在运行时配置和控制 VM。 有效参数是：

**full-screen=on|off** : 以全屏模式启动

**gl=on|off** : 使用 OpenGL 进行显示

**grab-on-hover=on|off** : 鼠标悬停时抓取键盘输入

**show-cursor=on|off** : 强制显示鼠标光标

**window-close=on|off** : 允许使用窗口关闭按钮退出 qemu

****curses\[,charset=<encoding>\]****

通过curses显示视频输出。 对于支持文本模式的图形设备模型，QEMU 可以使用 curses/ncurses 界面显示此输出。 当图形设备处于图形模式或图形设备不支持文本模式时，不显示任何内容。 通常只有 VGA 设备型号支持文本模式。 来宾使用的字体字符集可以使用 **charset** 选项指定，例如 **charset=CP850** 用于 IBM CP850 编码。 默认值为 **CP437**。

****egl-headless\[,rendernode=<file>\]****

将所有 OpenGL 操作卸载到本地 DRI 设备。 对于任何图形显示器，该显示器都需要与 VNC 或 SPICE 显示器配对。

****vnc=<display>****

在显示 <display> 上启动 VNC 服务器

****none****

不显示视频输出。 来宾仍然会看到模拟图形卡，但其输出不会显示给 QEMU 用户。 此选项与 -nographic 选项的不同之处在于它只影响视频输出的操作； -nographic 还会更改串行和并行端口数据的目的地。

-

****\-nographic****

通常，如果 QEMU 编译时支持图形窗口，它会在一个窗口中显示客户图形、客户控制台和 QEMU 监视器等输出。 使用此选项，您可以完全禁用图形输出，使 QEMU 成为一个简单的命令行应用程序。 模拟的串行端口在控制台上重定向并与监视器混合（除非明确重定向到其他地方）。 因此，您仍然可以使用 QEMU 通过串行控制台调试 Linux 内核。 使用 C-a h 在控制台和显示器之间切换时获得帮助。

****\-curses****

通常，如果 QEMU 编译时支持图形窗口，它会在一个窗口中显示客户图形、客户控制台和 QEMU 监视器等输出。 使用这个选项，QEMU 可以在文本模式下使用 curses/ncurses 界面显示 VGA 输出。 图形模式下不显示任何内容。

****\-alt-grab****

使用 Ctrl-Alt-Shift 来抓取鼠标（而不是 Ctrl-Alt)。 请注意，这也会影响特殊键（用于全屏、监视器模式切换等）。 此选项已弃用 - 请改用 **\-display sdl,grab-mod=lshift-lctrl-lalt** 。

****\-ctrl-grab****

使用 Right-Ctrl 来抓取鼠标（而不是 Ctrl-Alt)。 请注意，这也会影响特殊键（用于全屏、监视器模式切换等）。 此选项已弃用 - 请改用 **\-display sdl,grab-mod=rctrl** 。

****\-no-quit****

禁用窗口关闭功能（仅限 SDL 和 GTK）。 此选项已弃用，请改用 **\-display ...,window-close=off** 。

****\-sdl****

启用 SDL。

****\-spice option\[,option\[,...\]\]****

启用 spice 远程桌面协议。 有效的选项是

****port=<nr>****

设置 TCP 端口 spice 正在侦听纯文本通道。

****addr=<addr>****

设置spice监听的IP地址。 默认为任何地址。

****ipv4=on|off**; **ipv6=on|off**; **unix=on|off****

强制使用指定的 IP 版本。

****password=<string>****

设置您需要进行身份验证的密码。

设置您需要进行身份验证的密码。 此选项已弃用且不安全，因为它使密码在进程列表中可见。 请改用 **password-secret** 。

****password-secret=<secret-id>****

设置包含您需要进行身份验证的密码的 **secret** 对象的 ID。

****sasl=on|off****

要求客户端使用 SASL 对 spice 进行身份验证。 使用的身份验证方法的确切选择由系统/用户的 'qemu' 服务的 SASL 配置文件控制。 这通常位于 /etc/sasl2/qemu.conf 中。 如果以非特权用户身份运行 QEMU，可以使用环境变量 SASL\_CONF\_PATH 使其搜索服务配置的备用位置。 虽然某些 SASL 身份验证方法也可以提供数据加密（例如 GSSAPI），但建议始终将 SASL 与 'tls' 和 'x509' 设置结合使用，以启用 SSL 和服务器证书。 这确保了数据加密，防止身份验证凭据受到损害。

****disable-ticketing=on|off****

允许客户端无需身份验证即可连接。

****disable-copy-paste=on|off****

禁用客户端和来宾之间的复制粘贴。

****disable-agent-file-xfer=on|off****

在客户端和来宾之间禁用基于 spice-vdagent 的 file-xfer 。

****tls-port=<nr>****

设置 TCP 端口 spice 正在侦听加密通道。

****x509-dir=<dir>****

设置 x509 文件目录。期望与 -vnc $display,x509=$dir 相同的文件名

****x509-key-file=<file>**; **x509-key-password=<file>**; **x509-cert-file=<file>**; **x509-cacert-file=<file>**; **x509-dh-key-file=<file>****

x509 文件名也可以单独配置。

****tls-ciphers=<list>****

指定要使用的密码。

****tls-channel=\[main|display|cursor|inputs|record|playback\]**; **plaintext-channel=\[main|display|cursor|inputs|record|playback\]****

强制使用或不使用 TLS 加密的特定通道。 可以多次指定选项以配置多个通道。 特殊名称 "default" 可用于设置默认模式。 对于没有明确强制进入一种模式的频道，spice 客户端可以随意选择 tls/plaintext。

****image-compression=\[auto\_glz|auto\_lz|quic|glz|lz|off\]****

配置图像压缩（无损）。

****jpeg-wan-compression=\[auto|never|always\]**; **zlib-glz-wan-compression=\[auto|never|always\]****

配置 wan 图像压缩（对于慢速链接有损）。默认为自动。

****streaming-video=\[off|all|filter\]****

配置视频流检测。默认为关闭。

****agent-mouse=\[on|off\]****

启用/禁用通过 vdagent 传递鼠标事件。

****playback-compression=\[on|off\]****

启用/禁用音频流压缩（使用 celt 0.5.1）。默认开启。

****seamless-migration=\[on|off\]****

启用/禁用 spice 无缝迁移。默认为关闭。

****gl=\[on|off\]****

启用/禁用 OpenGL 上下文。 默认为关闭。

****rendernode=<file>****

用于 OpenGL 渲染的 DRM 渲染节点。 如果未指定，它将选择第一个可用的。（自 2.9 起）

-

****\-portrait****

将图形输出向左旋转 90 度（仅限 PXA LCD）。

****\-rotate deg****

将图形输出向左旋转一些度（仅限 PXA LCD）。

****\-vga type****

选择要模拟的 VGA 卡类型。 类型的有效值为

****cirrus****

Cirrus Logic GD5446 视频卡。 从 Windows 95 开始的所有 Windows 版本都应识别并使用此显卡。 为获得最佳性能，请在客户机和主机操作系统中使用 16 位色深。 （此卡是 QEMU 2.2 之前的默认卡）

****std****

带有 Bochs VBE 扩展的标准 VGA 卡。 如果您的客户操作系统支持 VESA 2.0 VBE 扩展（例如 Windows XP）并且如果您想使用高分辨率模式 (>= 1280x1024x16)，那么您应该使用此选项。 （此卡是 QEMU 2.2 以来的默认卡）

****vmware****

VMWare SVGA-II 兼容适配器。 如果您有足够新的 XFree86/XOrg 服务器或带有此卡驱动程序的 Windows 客户机，请使用它。

****qxl****

QXL 半虚拟显卡。 它与 VGA 兼容（包括 VESA 2.0 VBE 支持）。 最好与安装的 qxl 来宾驱动程序一起使用。 使用 spice 协议时的推荐选择。

****tcx****

（仅限 sun4m）Sun TCX 帧缓冲区。 这是 sun4m 机器的默认帧缓冲区，并以 1024x768 的固定分辨率提供 8 位和 24 位颜色深度。

****cg3****

（仅限 sun4m）Sun cgthree 帧缓冲区。 这是一个简单的 8 位帧缓冲区，适用于 sun4m 机器，提供 1024x768 (OpenBIOS) 和 1152x900 (OBP) 两种分辨率，面向希望运行旧 Solaris 版本的用户。

****virtio****

Virtio 显卡。

****none****

禁用 VGA 卡。

-

****\-full-screen****

全屏启动。

****\-g** _width_**x**_height_**\[x**_depth_**\]****

设置初始图形分辨率和深度（仅限 PPC、SPARC）。

对于 PPC，默认值为 800x600x32。

对于带有 TCX 图形设备的 SPARC，默认值为 1024x768x8，选项为 1024x768x24。 对于 cgthree，默认值为 1024x768x8，对于希望使用 OBP 的人，可以选择 1152x900x8。

****\-vnc display\[,option\[,option\[,...\]\]\]****

通常，如果 QEMU 编译时支持图形窗口，它会在一个窗口中显示客户图形、客户控制台和 QEMU 监视器等输出。 使用此选项，您可以让 QEMU 监听 VNC 显示并通过 VNC 会话重定向 VGA 显示。 使用此选项时启用 USB 平板设备非常有用（选项 **\-device usb-tablet** ）。 使用 VNC 显示时，如果不使用 en-us，则必须使用 **\-k** 参数设置键盘布局。 显示的有效语法是

****to=L****

使用这个选项，QEMU 将尝试下一个可用的 VNC 显示器，直到数字 L，如果最初定义的 "-vnc display" 不可用，例如端口 5900+显示器已被另一个应用程序使用。默认情况下，to=0。

****host:d****

TCP 连接将只允许来自显示 d 上的主机。 按照惯例，TCP 端口是 5900+d。 可选地，host 可以省略，在这种情况下 s服务器将接受来自任何主机的连接。

****unix:path****

将允许通过 UNIX 域套接字进行连接，其中 path 是用于侦听连接的 unix 套接字的位置。

****none****

VNC 已初始化但未启动。 监视器 **change** 命令可用于稍后启动 VNC 服务器。

-

在显示值之后可能有一个或多个选项标志，以逗号分隔。 有效的选项是

****reverse=on|off****

通过 "reverse" 连接连接到监听 VNC 客户端。 客户端由显示器指定。 对于反向网络连接 (host:d,\`\`reverse\`\`), d 参数是 TCP 端口号，而不是显示号。

****websocket=on|off****

打开一个额外的 TCP 监听端口，专用于 VNC Websocket 连接。 如果给出了裸 websocket 选项，则 Websocket 端口为 5700+display。 可以使用语法 **websocket**\=port 指定替代端口。

如果指定了主机，则仅允许来自该主机的连接。 可以使用语法 **websocket**\=host:port 独立控制 websocket 监听地址。

如果未提供 TLS 凭据，则 websocket 连接以未加密模式运行。 如果提供了 TLS 凭据，则 websocket 连接需要加密的客户端连接。

****password=on|off****

要求对客户端连接使用基于密码的身份验证。

密码必须在 QEMU 监视器中使用 **set\_password** 命令单独设置。 更改密码的语法是： **set\_password <protocol> <password>** 其中 <protocol> 可以是 "vnc" 或 "spice"。

如果您想更改 <protocol> 密码过期时间，您应该使用 **expire\_password <protocol> <expiration-time>** 其中过期时间可以是以下选项之一： now, never, +seconds 或 UNIX 过期时间，例如 +60使密码在 60 秒后过期，或 1335196800 使密码在 "Mon Apr 23 12:00:00 EDT 2012" （此日期和时间的 UNIX 时间）过期。

您还可以使用关键字 "now" 或 "never" 作为过期时间，以允许 <protocol> 密码立即过期或永不过期。

****password-secret=<secret-id>****

要求对客户端连接使用基于密码的身份验证，使用由 **secret-id** 标识的 **secret** 对象提供的密码。

****tls-creds=ID****

提供一组 TLS 凭据的 ID，用于保护 VNC 服务器。 它们将适用于普通 VNC 服务器套接字和 websocket 套接字（如果启用）。 设置 TLS 凭据将导致 VNC 服务器套接字启用 VeNCrypt 身份验证机制。 之前应该使用 **\-object tls-creds** 参数创建了凭据。

****tls-authz=ID****

提供 QAuthZ 授权对象的 ID，客户端的 x509 专有名称将根据该对象进行验证。 此对象仅在使用时解析，因此可以在 VNC 服务器处于活动状态时动态删除和重新创建。 如果缺少，它将默认拒绝访问。

****sasl=on|off****

要求客户端使用 SASL 与 VNC 服务器进行身份验证。 使用的身份验证方法的确切选择由系统/用户的 'qemu' 服务的 SASL 配置文件控制。 这通常位于 /etc/sasl2/qemu.conf 中。 如果以非特权用户身份运行 QEMU，可以使用环境变量 SASL\_CONF\_PATH 使其搜索服务配置的备用位置。 虽然某些 SASL 身份验证方法也可以提供数据加密（例如 GSSAPI），但建议始终将 SASL 与 'tls' 和 'x509' 设置结合使用，以启用 SSL 和服务器证书。 这确保了数据加密，防止身份验证凭据受到损害。 有关使用 SASL 身份验证的详细信息，请参阅系统仿真用户指南中的 VNC 安全部分。

****sasl-authz=ID****

提供将验证客户端的 SASL 用户名的 QAuthZ 授权对象的 ID。 此对象仅在使用时解析，因此可以在 VNC 服务器处于活动状态时动态删除和重新创建。 如果缺少，它将默认拒绝访问。

****acl=on|off****

针对 x509 专有名称和 SASL 用户名启用客户端授权的传统方法。 它导致创建两个 **authz-list** 对象，其 ID 为 **vnc.username** 和 **vnc.x509dname** 。 必须使用 HMP ACL 命令配置这些对象的规则。

此选项已弃用，不应再使用。 新的 **sasl-authz** 和 **tls-authz** 选项是替代品。

****lossy=on|off****

启用有损压缩方法（渐变、JPEG、...）。 如果设置了此选项，VNC 客户端可能会根据其编码设置接收有损帧缓冲区更新。 启用此选项可以以牺牲质量为代价节省大量带宽。

****non-adaptive=on|off****

禁用自适应编码。 默认情况下启用自适应编码。 自适应编码将尝试检测频繁更新的屏幕区域，并使用有损编码（如 JPEG）在这些区域中发送更新。 这对于在播放视频时节省带宽非常有帮助。 禁用自适应编码会恢复像 Tight 这样的编码的原始静态行为。

****share=\[allow-exclusive|force-shared|ignore\]****

设置显示共享策略。 'allow-exclusive' 允许客户请求独占访问。正如 rfb 规范所建议的，这是通过删除其他连接来实现的。 并行连接多个客户端需要所有客户端都请求共享会话 (vncviewer: -shared switch)。这是默认设置。 'force-shared' 禁用独占客户端访问。 对于共享桌面会话很有用，您不希望有人忘记指定 -shared 断开其他所有人。 'ignore' 完全忽略共享标志并允许每个人无条件地连接。 不符合 rfb 规范，而是传统的 QEMU 行为。

****key-delay-ms****

为按键按下和按键向上事件设置键盘延迟，以毫秒为单位。 默认值为 10。 键盘是低带宽设备，因此这种减速可以帮助设备和访客跟上并且不会丢失事件，以防万一事件大量到达。 后者的可能原因是不稳定的网络连接或用于自动测试的脚本。

****audiodev=audiodev****

当 VNC 客户端请求音频传输时，使用指定的 audiodev。 不使用 -audiodev 参数时，必须省略此选项，否则必须存在 is 并指定有效的 audiodev。

****power-control=on|off****

允许远程客户端发出关闭、重新启动或重置电源控制请求。

-

-

[仅i386 目标](#__u4EC5_i386___u76EE___u6807_)
------------------------------------------

****\-win2k-hack****

在安装 Windows 2000 时使用它以避免磁盘已满错误。 安装 Windows 2000 后，您不再需要此选项（此选项会减慢 IDE 传输速度）。

****\-no-fd-bootchk****

在 BIOS 中禁用软盘启动签名检查。 可能需要从旧软盘启动。

****\-no-acpi****

禁用 ACPI（高级配置和电源接口）支持。 如果您的客户操作系统抱怨 ACPI 问题（仅限 PC 目标机器），请使用它。

****\-no-hpet****

禁用 HPET 支持。

****\-acpitable \[sig=str\]\[,rev=n\]\[,oem\_id=str\]\[,oem\_table\_id=str\]\[,oem\_rev=n\] \[,asl\_compiler\_id=str\]\[,asl\_compiler\_rev=n\]\[,data=file1\[:file2\]...\]****

从指定文件中添加具有指定标头字段和上下文的 ACPI 表。 对于 file=，从指定的文件中获取整个 ACPI 表，包括所有 ACPI 标头（可能被其他选项覆盖）。 对于data=，仅使用表的数据部分，所有标题信息都在命令行中指定。 如果向 QEMU 提供 SLIC 表，则 SLIC 的 oem\_id 和 oem\_table\_id 字段将覆盖 RSDT 和 FADT（又名 FACP）中的相同字段，以确保 Microsoft SLIC 规范和 ACPI 规范要求的字段匹配。

****\-smbios file=binary****

从二进制文件加载 SMBIOS 条目。

****\-smbios type=0\[,vendor=str\]\[,version=str\]\[,date=str\]\[,release=%d.%d\]\[,uefi=on|off\]****

指定 SMBIOS 类型 0 字段

****\-smbios type=1\[,manufacturer=str\]\[,product=str\]\[,version=str\]\[,serial=str\]\[,uuid=uuid\]\[,sku=str\]\[,family=str\]****

指定 SMBIOS 类型 1 字段

****\-smbios type=2\[,manufacturer=str\]\[,product=str\]\[,version=str\]\[,serial=str\]\[,asset=str\]\[,location=str\]****

指定 SMBIOS 类型 2 字段

****\-smbios type=3\[,manufacturer=str\]\[,version=str\]\[,serial=str\]\[,asset=str\]\[,sku=str\]****

指定 SMBIOS 类型 3 字段

****\-smbios type=4\[,sock\_pfx=str\]\[,manufacturer=str\]\[,version=str\]\[,serial=str\]\[,asset=str\]\[,part=str\]****

指定 SMBIOS 类型 4 字段

****\-smbios type=11\[,value=str\]\[,path=filename\]****

指定 SMBIOS 类型 11 字段

该参数可以重复多次，并按照解析顺序添加值。 鼓励打算使用 OEM 字符串数据的应用程序使用其应用程序名称作为值字符串的前缀。 这有助于同时为多个应用程序传递信息。

**value=str** 语法提供字符串数据内联，而 **path=filename** 语法从磁盘上的文件加载数据。 请注意，该文件不允许包含任何 NUL 字节。

**value** 和 **path** 选项都可以重复多次，并将按照它们出现的顺序添加到 SMBIOS 表中。

请注意，在 x86 架构上，所有 SMBIOS 表的总大小限制为 65535 字节。 因此，OEM 字符串数据不适合将大量数据传递给来宾。 相反，它应该被用作一个指示符来通知客户在哪里可以找到真实的数据集，例如，通过指定块设备的序列号。

传递三个字符串的示例是

\-smbios type=11,value=cloud-init:ds=nocloud-net;s=http://10.10.0.1:8000/,\\ value=anaconda:method=http://dl.fedoraproject.org/pub/fedora/linux/releases/25/x86\_64/os,\\ path=/some/file/with/oemstringsdata.txt 

-

-

在来宾操作系统中，这可以通过 **dmidecode** 命令看到

$ dmidecode -t 11 Handle 0x0E00, DMI type 11, 5 bytes OEM Strings String 1: cloud-init:ds=nocloud-net;s=http://10.10.0.1:8000/ String 2: anaconda:method=http://dl.fedoraproject.org/pub/fedora/linux/releases/25/x86\_64/os String 3: myapp:some extra data 

-

-

-

-

****\-smbios type=17\[,loc\_pfx=str\]\[,bank=str\]\[,manufacturer=str\]\[,serial=str\]\[,asset=str\]\[,part=str\]\[,speed=%d\]****

指定 SMBIOS 类型 17 字段

****\-smbios type=41\[,designation=str\]\[,kind=str\]\[,instance=%d\]\[,pcidev=str\]****

指定 SMBIOS 类型 41 字段

这个论点可以重复多次。 它的主要用途是允许在 Linux 上将网络接口创建为 **enoX** ，其中 X 是实例编号，而不是取决于 PCI 总线上接口位置的名称。

这是一个使用示例：

\-netdev user,id=internet \\ -device virtio-net-pci,mac=50:54:00:00:00:42,netdev=internet,id=internet-dev \\ -smbios type=41,designation='Onboard LAN',instance=1,kind=ethernet,pcidev=internet-dev 

-

-

在来宾操作系统中，设备应显示为 **eno1**:

..parsed-literal:

$ ip -brief l lo UNKNOWN 00:00:00:00:00:00 <LOOPBACK,UP,LOWER\_UP> eno1 UP 50:54:00:00:00:42 <BROADCAST,MULTICAST,UP,LOWER\_UP> 

-

-

目前，PCI 设备必须连接到根总线。

-

[网络选项](#__u7F51___u7EDC___u9009___u9879_)
-----------------------------------------

****\-nic \[tap|bridge|user|l2tpv3|vde|netmap|vhost-user|socket\]\[,...\]\[,mac=macaddr\]\[,model=mn\]****

此选项是一次性配置板载（默认）访客 NIC 硬件和主机网络后端的快捷方式。 主机后端选项与下面相应的 **\-netdev** 选项相同。 可以使用 **model=modelname** 设置来宾 NIC 型号。 使用 **model=help** 列出可用的设备类型。 可以使用 **mac=macaddr** 设置硬件 MAC 地址。

以下两个示例完全相同，以显示如何使用 **\-nic** 缩短命令行长度：

qemu-system-x86\_64 -netdev user,id=n1,ipv6=off -device e1000,netdev=n1,mac=52:54:98:76:54:32 qemu-system-x86\_64 -nic user,ipv6=off,model=e1000,mac=52:54:98:76:54:32 

-

-

****\-nic none****

指示不应配置任何网络设备。 它用于覆盖默认配置（带有 "user" 主机网络后端的默认 NIC），如果没有提供其他网络选项，则会激活该配置。

****\-netdev user,id=id\[,option\]\[,option\]\[,...\]****

配置无需管理员权限即可运行的用户模式主机网络后端。 有效的选项是：

****id=id****

分配符号名称以在监视器命令中使用。

****ipv4=on|off and ipv6=on|off****

指定必须启用 IPv4 或 IPv6。 如果两者都未指定，则启用两个协议。

****net=addr\[/mask\]****

设置访客将看到的 IP 网络地址。 可以选择指定网络掩码，格式为 abcd 或有效最高位的数量。 默认值为 10.0.2.0/24。

****host=addr****

指定主机的访客可见地址。默认是访客网络中的第二个 IP，即x.x.x.2。

****ipv6-net=addr\[/int\]****

设置访客将看到的 IPv6 网络地址（默认为 fec0::/64）。 网络前缀以通常的十六进制 IPv6 地址表示法给出。 前缀大小是可选的，并以有效最高位的数量给出（默认为 64）。

****ipv6-host=addr****

指定主机的访客可见 IPv6 地址。 默认为访客网络中的第二个 IPv6，即 xxxx::2。

****restrict=on|off****

如果启用此选项，guest 将被隔离，即它将无法联系主机，并且不会将guest IP 数据包通过主机路由到外部。 此选项不影响任何明确设置的转发规则。

****hostname=name****

指定内置 DHCP 服务器报告的客户端主机名。

****dhcpstart=addr****

指定内置 DHCP 服务器可以分配的 16 个 IP 中的第一个。 默认是访客网络中的第 15 到 31 个 IP，即 x.x.x.15 到 x.x.x.31。

****dns=addr****

指定 IPv6 虚拟名称服务器的来宾可见地址。 该地址必须与主机地址不同。 默认为访客网络中的第三个 IP，即 x.x.x.3。

****ipv6-dns=addr****

指定 IPv6 虚拟名称服务器的来宾可见地址。 该地址必须与主机地址不同。 默认为访客网络中的第三个 IP，即 xxxx::3。

****dnssearch=domain****

为内置 DHCP 服务器发送的域搜索列表提供一个条目。 通过多次指定此选项可以传输多个域后缀。 如果支持，这将导致来宾自动尝试附加给定的域后缀，以防无法解析域名。

例子：

qemu-system-x86\_64 -nic user,dnssearch=mgmt.example.org,dnssearch=example.org 

-

-

****domainname=domain****

指定内置DHCP服务器上报的客户端域名。

****tftp=dir****

使用用户模式网络堆栈时，请激活内置 TFTP 服务器。 dir 中的文件将作为 TFTP 服务器的根目录公开。 客户机上的 TFTP 客户端必须配置为二进制模式（使用 Unix TFTP 客户端的命令 **bin** ）。

****tftp-server-name=name****

在 BOOTP 回复中，广播名称为 "TFTP server name" （RFC2132 选项 66）。 这可用于建议来宾从与主机地址不同的服务器加载引导文件或配置。

****bootfile=file****

使用用户模式网络堆栈时，广播文件作为 BOOTP 文件名。 与 **tftp** 结合使用，这可用于从本地目录网络引导来宾。

示例（使用 pxelinux）：

qemu-system-x86\_64 -hda linux.img -boot n -device e1000,netdev=n1 \\ -netdev user,id=n1,tftp=/path/to/tftp/files,bootfile=/pxelinux.0 

-

-

****smb=dir\[,smbserver=addr\]****

使用用户模式网络堆栈时，激活内置的 SMB 服务器，以便 Windows 操作系统可以透明地访问 **dir** 中的主机文件。 SMB 服务器的 IP 地址可以设置为 addr。 默认情况下，使用访客网络中的第 4 个 IP，即 x.x.x.4。

在来宾 Windows 操作系统中，该行：

10.0.2.4 smbserver 

-

-

必须添加到文件 **C:\\WINDOWS\\LMHOSTS** (适用于 9x/Me) 或 **C:\\WINNT\\SYSTEM32\\DRIVERS\\ETC\\LMHOSTS** (Windows NT/2000)中。

然后可以在 **\\\\smbserver\\qemu** 中访问 **dir** 。

请注意，必须在主机操作系统上安装 SAMBA 服务器。

****hostfwd=\[tcp|udp\]:\[hostaddr\]:hostport-\[guestaddr\]:guestport****

将传入的 TCP 或 UDP 连接重定向到主机端口 hostport 到来宾端口 guestport 上的来宾 IP 地址 guestaddr。 如果未指定 guestaddr，则其值为 x.x.x.15 （内置 DHCP 服务器给出的默认首地址）。 通过指定 hostaddr，可以将规则绑定到特定的主机接口。 如果未设置连接类型，则使用 TCP。 该选项可以多次给出。

例如，要将主机 X11 连接从屏幕 1 重定向到访客屏幕 0，请使用以下命令：

\# on the host qemu-system-x86\_64 -nic user,hostfwd=tcp:127.0.0.1:6001-:6000 # this host xterm should open in the guest X11 server xterm -display :1 

-

-

要将 telnet 连接从主机端口 5555 重定向到客户机上的 telnet 端口，请使用以下命令：

\# on the host qemu-system-x86\_64 -nic user,hostfwd=tcp::5555-:23 telnet localhost 5555 

-

-

然后，当您在主机上使用 **telnet localhost 5555** 时，您连接到来宾 telnet 服务器。

****guestfwd=\[tcp\]:server:port-dev**; **guestfwd=\[tcp\]:server:port-cmd:command****

将访客 TCP 连接转发到端口端口上的 IP 地址服务器到字符设备 dev 或由 cmd:command 执行的程序，该程序为每个连接生成。 该选项可以多次给出。

您可以直接使用 chardev 并在 QEMU 的整个生命周期中使用它，如下例所示：

\# open 10.10.1.1:4321 on bootup, connect 10.0.2.100:1234 to it whenever # the guest accesses it qemu-system-x86\_64 -nic user,guestfwd=tcp:10.0.2.100:1234-_tcp:10.10.1.1:4321_ 

-

-

或者，您可以在来宾建立的每个 TCP 连接上执行命令，以便 QEMU 的行为类似于该虚拟服务器的 inetd 进程：

\# call "netcat 10.10.1.1 4321" on every TCP connection to 10.0.2.100:1234 # and connect the TCP stream to its stdin/stdout qemu-system-x86\_64 -nic 'user,id=n1,guestfwd=tcp:10.0.2.100:1234-cmd:netcat 10.10.1.1 4321' 

-

-

-

****\-netdev tap,id=id\[,fd=h\]\[,ifname=name\]\[,script=file\]\[,downscript=dfile\]\[,br=bridge\]\[,helper=helper\]****

使用 ID id 配置主机 TAP 网络后端。

使用网络脚本文件对其进行配置，并使用网络脚本 dfile 对其进行取消配置。 如果没有提供名称，操作系统会自动提供一个。 默认的网络配置脚本是 **/etc/qemu-ifup** ，默认的网络解除配置脚本是 **/etc/qemu-ifdown** 。 使用 **script=no** 或 **downscript=no** 禁用脚本执行。

如果以非特权用户身份运行 QEMU，请使用网络助手配置 TAP 接口并将其附加到网桥。 默认的网络助手可执行文件是 **/path/to/qemu-bridge-helper** ，默认的网桥设备是 **br0**。

**fd**\=h 可用于指定已打开的主机 TAP 接口的句柄。

例子：

#launch a QEMU instance with the default network script qemu-system-x86\_64 linux.img -nic tap 

-

-

#launch a QEMU instance with two NICs, each one connected #to a TAP device qemu-system-x86\_64 linux.img \\ -netdev tap,id=nd0,ifname=tap0 -device e1000,netdev=nd0 \\ -netdev tap,id=nd1,ifname=tap1 -device rtl8139,netdev=nd1 

-

-

#launch a QEMU instance with the default network helper to #connect a TAP device to bridge br0 qemu-system-x86\_64 linux.img -device virtio-net-pci,netdev=n1 \\ -netdev tap,id=n1,"helper=/path/to/qemu-bridge-helper" 

-

-

****\-netdev bridge,id=id\[,br=bridge\]\[,helper=helper\]****

将主机 TAP 网络接口连接到主机桥设备。

使用 network helper helper 配置 TAP 接口并将其附加到网桥。 默认的网络助手可执行文件是 **/path/to/qemu-bridge-helper** ，默认的网桥设备是 **br0**。

例子:

#launch a QEMU instance with the default network helper to #connect a TAP device to bridge br0 qemu-system-x86\_64 linux.img -netdev bridge,id=n1 -device virtio-net,netdev=n1 

-

-

#launch a QEMU instance with the default network helper to #connect a TAP device to bridge qemubr0 qemu-system-x86\_64 linux.img -netdev bridge,br=qemubr0,id=n1 -device virtio-net,netdev=n1 

-

-

****\-netdev socket,id=id\[,fd=h\]\[,listen=\[host\]:port\]\[,connect=host:port\]****

此主机网络后端可用于使用 TCP 套接字连接将访客网络连接到另一个 QEMU 虚拟机。 如果指定了 **listen** 会等待端口上的传入连接（主机是可选的）。 **connect** 用于使用 **listen** 选项连接到另一个 QEMU 实例。 **fd**\=h 指定一个已经打开的 TCP 套接字。

例子：

\# launch a first QEMU instance qemu-system-x86\_64 linux.img \\ -device e1000,netdev=n1,mac=52:54:00:12:34:56 \\ -netdev socket,id=n1,listen=:1234 # connect the network of this instance to the network of the first instance qemu-system-x86\_64 linux.img \\ -device e1000,netdev=n2,mac=52:54:00:12:34:57 \\ -netdev socket,id=n2,connect=127.0.0.1:1234 

-

-

****\-netdev socket,id=id\[,fd=h\]\[,mcast=maddr:port\[,localaddr=addr\]\]****

配置套接字主机网络后端以使用 UDP 多播套接字与另一个 QEMU 虚拟机共享来宾的网络流量，有效地为每个具有相同多播地址 maddr 和端口的 QEMU 建立总线。 笔记：

1.

多个 QEMU 可以在不同的主机上运行并共享相同的总线（假设这些主机的多播设置正确）。

2.

mcast 支持与用户模式 Linux 兼容（参数 **ethN=mcast**), 请参阅 _http://user-mode-linux.sf.net_。

3.

使用 **fd=h** 指定一个已经打开的 UDP 多播套接字。

-

例子：

\# launch one QEMU instance qemu-system-x86\_64 linux.img \\ -device e1000,netdev=n1,mac=52:54:00:12:34:56 \\ -netdev socket,id=n1,mcast=230.0.0.1:1234 # launch another QEMU instance on same "bus" qemu-system-x86\_64 linux.img \\ -device e1000,netdev=n2,mac=52:54:00:12:34:57 \\ -netdev socket,id=n2,mcast=230.0.0.1:1234 # launch yet another QEMU instance on same "bus" qemu-system-x86\_64 linux.img \\ -device e1000,netdev=n3,mac=52:54:00:12:34:58 \\ -netdev socket,id=n3,mcast=230.0.0.1:1234 

-

-

示例（用户模式 Linux 兼容）：

\# launch QEMU instance (note mcast address selected is UML's default) qemu-system-x86\_64 linux.img \\ -device e1000,netdev=n1,mac=52:54:00:12:34:56 \\ -netdev socket,id=n1,mcast=239.192.168.1:1102 # launch UML /path/to/linux ubd0=/path/to/root\_fs eth0=mcast 

-

-

示例（从主机的 1.2.3.4 发送数据包）：

qemu-system-x86\_64 linux.img \\ -device e1000,netdev=n1,mac=52:54:00:12:34:56 \\ -netdev socket,id=n1,mcast=239.192.168.1:1102,localaddr=1.2.3.4 

-

-

****\-netdev l2tpv3,id=id,src=srcaddr,dst=dstaddr\[,srcport=srcport\]\[,dstport=dstport\],txsession=txsession\[,rxsession=rxsession\]\[,ipv6=on|off\]\[,udp=on|off\]\[,cookie64\]\[,counter\]\[,pincounter\]\[,txcookie=txcookie\]\[,rxcookie=rxcookie\]\[,offset=offset\]****

配置 L2TPv3 伪线主机网络后端。 L2TPv3 (RFC3931) 是一种流行的协议，用于在两个系统之间传输以太网（和其他第 2 层）数据帧。 它存在于路由器、防火墙和 Linux 内核中（从 3.3 版开始）。

此传输允许 VM 直接与另一个 VM、路由器或防火墙通信。

****src=srcaddr****

源地址（必填）

****dst=dstaddr****

目的地址（必填）

****udp****

选择 udp 封装（默认为 ip）。

****srcport=srcport****

源 udp 端口。

****dstport=dstport****

目标 udp 端口。

****ipv6****

强制 v6，否则默认为 v4。

****rxcookie=rxcookie**; **txcookie=txcookie****

Cookie 是 l2tpv3 规范中一种较弱的安全形式。 它们的功能主要是防止配置错误。 默认情况下，它们是 32 位的。

****cookie64****

将 cookie 大小设置为 64 位而不是默认的 32 位

****counter=off****

像在 draft-mkonstan-l2tpext-keyed-ipv6-tunnel-00 中那样强制“缩减”L2TPv3，没有计数器

****pincounter=on****

解决对等体中损坏的计数器处理。 这也可能有助于具有数据包重新排序的网络。

****offset=offset****

在标头和数据之间添加额外的偏移量

-

例如，要通过 L2TPv3 将在主机 4.3.2.1 上运行的 VM 连接到远程 Linux 主机 1.2.3.4 上的网桥 br-lan :

\# Setup tunnel on linux host using raw ip as encapsulation # on 1.2.3.4 ip l2tp add tunnel remote 4.3.2.1 local 1.2.3.4 tunnel\_id 1 peer\_tunnel\_id 1 \\ encap udp udp\_sport 16384 udp\_dport 16384 ip l2tp add session tunnel\_id 1 name vmtunnel0 session\_id \\ 0xFFFFFFFF peer\_session\_id 0xFFFFFFFF ifconfig vmtunnel0 mtu 1500 ifconfig vmtunnel0 up brctl addif br-lan vmtunnel0 # on 4.3.2.1 # launch QEMU instance - if your network has reorder or is very lossy add ,pincounter qemu-system-x86\_64 linux.img -device e1000,netdev=n1 \\ -netdev l2tpv3,id=n1,src=4.2.3.1,dst=1.2.3.4,udp,srcport=16384,dstport=16384,rxsession=0xffffffff,txsession=0xffffffff,counter 

-

-

****\-netdev vde,id=id\[,sock=socketpath\]\[,port=n\]\[,group=groupname\]\[,mode=octalmode\]****

将 VDE 后端配置为连接到在主机上运行的 vde 交换机的端口 n，并侦听套接字路径上的传入连接。 使用 GROUP 组名和 MODE 八进制模式来更改通信端口的默认所有权和权限。 仅当 QEMU 已在启用 vde 支持的情况下编译时，此选项才可用。

例子：

\# launch vde switch vde\_switch -F -sock /tmp/myswitch # launch QEMU instance qemu-system-x86\_64 linux.img -nic vde,sock=/tmp/myswitch 

-

-

****\-netdev vhost-user,chardev=id\[,vhostforce=on|off\]\[,queues=n\]****

建立一个由 chardev id 支持的 vhost-user 。 chardev 应该是一个支持 unix 域套接字的。 vhost-user 使用专门定义的协议将 vhost ioctl 替换消息传递给套接字另一端的应用程序。 在非 MSIX 客户机上，可以使用 vhostforce 强制执行该功能。 使用 'queues=n' 指定要为多队列 vhost-user 创建的队列数。

例子：

qemu -m 512 -object memory-backend-file,id=mem,size=512M,mem-path=/hugetlbfs,share=on \\ -numa node,memdev=mem \\ -chardev socket,id=chr0,path=/path/to/socket \\ -netdev type=vhost-user,id=net0,chardev=chr0 \\ -device virtio-net-pci,netdev=net0 

-

-

****\-netdev vhost-vdpa,vhostdev=/path/to/dev****

建立一个 vhost-vdpa netdev。

vDPA 设备是使用符合 virtio 规范和供应商特定控制路径的数据路径的设备。 vDPA 设备既可以物理上位于硬件上，也可以由软件模拟。

****\-netdev hubport,id=id,hubid=hubid\[,netdev=nd\]****

在具有 ID hubid 的模拟集线器上创建集线器端口。

hubport netdev 允许您将 NIC 连接到 QEMU 模拟集线器，而不是单个 netdev。 或者，您也可以使用 **netdev=nd** 选项将集线器端口连接到 ID 为 nd 的另一个 netdev。

****\-net nic\[,netdev=nd\]\[,macaddr=mac\]\[,model=type\] \[,name=name\]\[,addr=addr\]\[,vectors=v\]****

用于配置或创建板载（或机器默认）网络接口卡 (NIC) 并将其连接到 ID 为 0 的模拟集线器（即默认集线器）或 netdev nd 的传统选项。 如果省略模型，则使用与机器类型关联的默认 NIC 模型。 请注意，默认 NIC 模型可能会在未来的 QEMU 版本中更改，因此强烈建议始终指定模型。 或者，可以将 MAC 地址更改为 mac，将设备地址设置为 addr（仅限 PCI 卡），并且可以分配名称以用于监控命令。 或者，对于 PCI 卡，您可以指定卡应具有的 MSI-X 向量的数量 v；此选项目前仅影响 virtio 卡；设置 v = 0 以禁用 MSI-X 。 如果未指定 **\-net** 选项，则创建单个 NIC。 QEMU 可以模拟几种不同型号的网卡。 使用 **\-net nic,model=help** 获取目标可用设备的列表。

****\-net user|tap|bridge|socket|l2tpv3|vde\[,...\]\[,name=name\]****

配置主机网络后端（使用与相同的 **\-netdev** 选项对应的选项）并将其连接到模拟集线器 0（默认集线器）。 使用 name 指定集线器端口的名称。

-

[字符设备选项](#__u5B57___u7B26___u8BBE___u5907___u9009___u9879_)
-----------------------------------------------------------

字符设备选项的一般形式是：

****\-chardev backend,id=id\[,mux=on|off\]\[,options\]****

后端是以下之一: **null**, **socket**, **udp**, **msmouse**, **vc**, **ringbuf**, **file**, **pipe**, **console**, **serial**, **pty**, **stdio**, **braille**, **tty**, **parallel**, **parport**, **spicevmc**, **spiceport** 。 具体的后端将确定适用的选项。

使用 **\-chardev help** 打印所有可用的 chardev 后端类型。

所有设备都必须有一个 id，它可以是最长 127 个字符的任何字符串。 它用于在其他命令行指令中唯一标识此设备。

一个字符设备可以被多个前端以多路复用模式使用。 指定 **mux=on** 以启用此模式。 多路复用器是 "1:N" 设备，这里 "1" 端是您指定的 chardev 后端， "N" 端是 QEMU 中可以与 chardev 通信的各个部分。 如果您使用 **id=myid** 和 **mux=on** 创建一个 chardev，QEMU 将使用您指定的 ID 创建一个多路复用器，然后您可以配置多个前端以使用该 chardev ID 进行输入/输出。 最多可以将四个不同的前端连接到一个多路复用 chardev。 （不启用多路复用，一个 chardev 只能由单个前端使用。） 例如，您可以使用它来允许两个串行端口和 QEMU 监视器使用单个 stdio chardev：

\-chardev stdio,mux=on,id=char0 \\ -mon chardev=char0,mode=readline \\ -serial chardev:char0 \\ -serial chardev:char0 

-

-

一个系统配置中可以有多个多路复用器；例如，您可以在 UART 0 和 UART 1 之间多路复用 TCP 端口，并在 QEMU 监视器和并行端口之间多路复用 stdio：

\-chardev stdio,mux=on,id=char0 \\ -mon chardev=char0,mode=readline \\ -parallel chardev:char0 \\ -chardev tcp,...,mux=on,id=char1 \\ -serial chardev:char1 \\ -serial chardev:char1 

-

-

当您使用多路复用字符设备时，会在输入中解释一些转义序列。 有关详细信息，请参阅系统仿真用户指南中有关字符后端多路复用器中的键的章节。

请注意，其他一些命令行选项可能会隐式创建多路复用字符后端；例如 **\-serial mon:stdio** 创建一个多路复用的 stdio 后端，连接到串行端口和 QEMU 监视器， **\-nographic** 还将控制台和监视器多路复用到 stdio。

目前不支持其他方向的多路复用（单个 QEMU 前端从多个 chardev 获取输入和输出）。

每个后端都支持 **logfile** 选项，该选项提供文件路径以记录通过后端传输的所有数据。 **logappend** 选项控制日志文件在打开时是否被截断或附加。

-

可用的后端是：

****\-chardev null,id=id****

一个虚空装置。 该设备不会发出任何数据，并且会丢弃它接收到的任何数据。 空后端不接受任何选项。

****\-chardev socket,id=id\[,TCP options or unix options\]\[,server=on|off\]\[,wait=on|off\]\[,telnet=on|off\]\[,websocket=on|off\]\[,reconnect=seconds\]\[,tls-creds=id\]\[,tls-authz=id\]****

创建双向流套接字，可以是 TCP 或 unix 套接字。 如果指定了 **path** ，则将创建一个 unix 套接字。 如果为 unix 套接字指定了 TCP 选项，则行为未定义。

**server=on|off** 指定套接字应为监听套接字。

**wait=on|off** 指定 QEMU 不应阻塞等待客户端连接到侦听套接字。

**telnet=on|off** 指定套接字上的流量应该解释 telnet 转义序列。

**websocket=on|off** 指定套接字使用 WebSocket 协议进行通信。

**reconnect** 设置当远程端离开时重新连接非服务器套接字的超时时间。 qemu 会延迟这么多秒，然后尝试重新连接。 零禁用重新连接，是默认设置。

**tls-creds** 请求启用 TLS 协议进行加密，并指定用于握手的 TLS 凭证的 id。 必须使用 **\-object tls-creds** 参数先前创建凭据。

**tls-auth** 提供 QAuthZ 授权对象的 ID，客户端的 x509 可分辨名称将根据该 ID 进行验证。 此对象仅在使用时解析，因此可以在 chardev 服务器处于活动状态时动态删除和重新创建。 如果缺少，它将默认拒绝访问。

TCP 和 unix 套接字选项如下：

****TCP options: port=port\[,host=host\]\[,to=to\]\[,ipv4=on|off\]\[,ipv6=on|off\]\[,nodelay=on|off\]****

监听套接字的 **host** 指定要绑定的本地地址。 对于要连接的远程主机的连接套接字种类。 **host** 对于侦听套接字是可选的。 如果未指定，则默认为 **0.0.0.0** 。

监听套接字的 **port** 指定要绑定的本地端口。 对于连接套接字，指定远程主机上要连接的 **port** 。 port 可以作为端口号或服务名称给出。 **port** 是必需的。

**to** 仅与侦听套接字有关。 如果它被指定，并且 **port** 不能被绑定，QEMU 将尝试绑定到后续端口，直到它成功为止。 **to** 必须指定为端口号。

**ipv4=on|off** 和 **ipv6=on|off** 指定必须使用 IPv4 或 IPv6。 如果两者都没有指定，则套接字可以使用任一协议。

**nodelay=on|off** 禁用 Nagle 算法。

****unix options: path=path\[,abstract=on|off\]\[,tight=on|off\]****

**path** 指定 unix 套接字的本地路径。 **path** 是必需的。 **abstract=on|off** 指定使用抽象套接字命名空间，而不是文件系统。 可选，默认为 false。 **tight=on|off** 将抽象套接字的套接字长度设置为最小值，而不是完整的 sun\_path 长度。可选，默认为真。

-

****\-chardev udp,id=id\[,host=host\],port=port\[,localaddr=localaddr\]\[,localport=localport\]\[,ipv4=on|off\]\[,ipv6=on|off\]****

通过 UDP 将访客的所有流量发送到远程主机。

**host** 指定要连接的远程主机。 如果未指定，则默认为 **localhost**。

**port** 指定要连接的远程主机上的端口。 **port** 是必需的。

**localaddr** 指定要绑定的本地地址。 如果未指定，则默认为 **0.0.0.0**。

**localport** 指定要绑定的本地端口。 如果未指定，将使用任何可用的本地端口。

**ipv4=on|off** 和 **ipv6=on|off** 指定必须使用 IPv4 或 IPv6。 如果两者均未指定，则设备可以使用任一协议。

****\-chardev msmouse,id=id****

将 QEMU 的模拟 msmouse 事件转发给来宾。 **msmouse** 没有任何选项。

****\-chardev vc,id=id\[\[,width=width\]\[,height=height\]\]\[\[,cols=cols\]\[,rows=rows\]\]****

连接到 QEMU 文本控制台。 **vc** 可以选择指定一个特定的大小。

**width** 和 **height** 分别指定控制台的宽度和高度，以像素为单位。

**cols** 和 **rows** 指定控制台的大小以适合具有给定尺寸的文本控制台。

****\-chardev ringbuf,id=id\[,size=size\]****

创建一个固定大小 **size** 的环形缓冲区。 size 必须是 2 的幂，默认为 **64K**。

****\-chardev file,id=id,path=path****

将从来宾收到的所有流量记录到文件中。

**path** 指定要打开的文件的路径。 如果该文件尚不存在，则将创建该文件，如果存在则将其覆盖。 **path** 是必需的。

****\-chardev pipe,id=id,path=path****

创建与来宾的双向连接。 Windows 主机和其他主机之间的行为略有不同：

在 Windows 上，将在 **\\\\.pipe\\path** 处创建单个双工管道。

在其他主机上，将创建两个名为 **path.in** 和 **path.out** 的管道。 写入 **path.in** 的数据将被访客接收。 来宾写入的数据可以从 **path.out** 中读取。 QEMU 不会创建这些 fifo，并要求它们存在。

**path** 构成上述管道路径的一部分。 **path** 是必需的。

****\-chardev console,id=id****

将访客的流量发送到 QEMU 的标准输出。 **console** 不采取任何选项。

**console** 仅在 Windows 主机上可用。

****\-chardev serial,id=id,path=path****

将访客的流量发送到主机上的串行设备。

在 Unix 主机上，serial 实际上会接受任何 tty 设备，而不仅仅是串行线路。

**path** 指定要打开的串行设备的名称。

****\-chardev pty,id=id****

在主机上创建一个新的伪终端并连接到它。 **pty** 不采取任何选择。

**pty** 在 Windows 主机上不可用。

****\-chardev stdio,id=id\[,signal=on|off\]****

连接到 QEMU 进程的标准输入和标准输出。

**signal** 控制是否在终端上启用信号，包括使用键序列 Control-c 退出 QEMU。 此选项默认启用，使用 **signal=off** 禁用它。

****\-chardev braille,id=id****

连接到本地 BrlAPI 服务器。**braille** 没有任何选择。

****\-chardev tty,id=id,path=path****

**tty** 仅在 Linux, Sun, FreeBSD, NetBSD, OpenBSD 和 DragonFlyBSD 主机上可用。 它是 **serial** 的别名。

**path** 指定 tty 的路径。 **path** 是必需的。

****\-chardev parallel,id=id,path=path****

****\-chardev parport,id=id,path=path****

**parallel** 仅在 Linux, FreeBSD 和 DragonFlyBSD 主机上可用。

连接到本地并行端口。

**path** 指定并行端口设备的路径。 **path** 是必需的。

****\-chardev spicevmc,id=id,debug=debug,name=name****

**spicevmc** 仅在内置 spice 支持时可用。

spicevmc 的 **debug** 调试级别

**name** 要连接的香料通道的名称

连接到 spice 虚拟机通道，例如 vdiport。

****\-chardev spiceport,id=id,debug=debug,name=name****

**spiceport** 仅在内置 spice 支持时可用。

spicevmc 的 **debug** 调试级别

**name** 要连接的 spice 端口的名称

连接到 spice 端口，允许 Spice 客户端处理由名称（最好是 fqdn）标识的流量。

-

[TPM 设备选项](#TPM___u8BBE___u5907___u9009___u9879_)
-------------------------------------------------

TPM 设备选项的一般形式是：

****\-tpmdev backend,id=id\[,options\]****

具体的后端类型将决定适用的选项。 **\-tpmdev** 选项创建 TPM 后端并需要一个指定 TPM 前端接口模型的 **\-device** 选项。

使用 **\-tpmdev help** 打印所有可用的 TPM 后端类型。

-

可用的后端是：

****\-tpmdev passthrough,id=id,path=path,cancel-path=cancel-path****

（仅限 Linux 主机）使用直通驱动程序启用对主机 TPM 的访问。

**path** 指定主机的 TPM 设备的路径，即在 Linux 主机上，这将是 **/dev/tpm0** 。 **path** i是可选的，默认使用 **/dev/tpm0** 。

**cancel-path** 指定主机 TPM 设备的 sysfs 条目的路径，允许取消正在进行的 TPM 命令。 **cancel-path** 是可选的，默认情况下 QEMU 将搜索要使用的 sysfs 条目。

关于将主机的 TPM 与直通驱动程序一起使用的一些注意事项：

主机上的任何其他应用程序不得使用直通驱动程序访问的 TPM 设备。

由于主机的固件 (BIOS/UEFI) 已经初始化了 TPM，VM 的固件 (BIOS/UEFI) 将无法再次初始化 TPM，因此可能不会显示 TPM 特定的菜单，否则用户可以配置TPM，例如，允许用户启用/禁用或激活/停用TPM。 此外，如果从 VM 中释放 TPM 所有权，则主机的 TPM 将被禁用和停用。 之后要再次启用和激活 TPM，必须重新启动主机，并且用户需要进入固件菜单以启用和激活 TPM。 如果 TPM 被禁用和/或停用，大多数 TPM 命令将失败。

要创建直通 TPM，请使用以下两个选项：

\-tpmdev passthrough,id=tpm0 -device tpm-tis,tpmdev=tpm0 

-

-

请注意， **\-tpmdev** id 是 **tpm0** ，并且在设备选项中由 **tpmdev=tpm0** 引用。

****\-tpmdev emulator,id=id,chardev=dev****

（仅限 Linux 主机）使用基于 Unix 域套接字的 chardev 后端启用对 TPM 模拟器的访问。

**chardev** 指定提供与软件 TPM 服务器连接的字符设备后端的唯一 ID。

要使用 chardev 套接字后端创建 TPM 仿真器后端设备：

\-chardev socket,id=chrtpm,path=/tmp/swtpm-sock -tpmdev emulator,id=tpm0,chardev=chrtpm -device tpm-tis,tpmdev=tpm0 

-

-

-

[Linux/Multiboot 引导特定](#Linux/Multiboot___u5F15___u5BFC___u7279___u5B9A_)
-------------------------------------------------------------------------

使用这些选项时，您可以使用给定的 Linux 或 Multiboot 内核，而无需将其安装在磁盘映像中。 它可用于更轻松地测试各种内核。

****\-kernel bzImage****

使用 bzImage 作为内核映像。 内核可以是 Linux 内核或多重引导格式。

****\-append cmdline****

使用 cmdline 作为内核命令行

****\-initrd file****

使用文件作为初始 ram 磁盘。

****\-initrd file1 arg=foo,file2****

此语法仅适用于多重引导。

使用 file1 和 file2 作为模块并将 arg=foo 作为参数传递给第一个模块。

****\-dtb file****

将文件用作设备树二进制 (dtb) 映像，并在启动时将其传递给内核。

-

[调试/专家选项](#__u8C03___u8BD5_/__u4E13___u5BB6___u9009___u9879_)
-------------------------------------------------------------

****\-compat \[deprecated-input=@var{input-policy}\]\[,deprecated-output=@var{output-policy}\]****

设置处理弃用管理接口的策略（实验性）：

****deprecated-input=accept** (default)**

接受不推荐使用的命令和参数

****deprecated-input=reject****

拒绝不推荐使用的命令和参数

****deprecated-input=crash****

不推荐使用的命令和参数崩溃

****deprecated-output=accept** (default)**

发出不推荐使用的命令结果和事件

****deprecated-output=hide****

抑制不推荐使用的命令结果和事件

-

限制：仅涵盖 QMP 的句法方面。

****\-compat \[unstable-input=@var{input-policy}\]\[,unstable-output=@var{output-policy}\]****

设置处理不稳定管理接口的策略（实验性）：

****unstable-input=accept** (default)**

接受不稳定的命令和参数

****unstable-input=reject****

拒绝不稳定的命令和参数

****unstable-input=crash****

不稳定的命令和参数崩溃

****unstable-output=accept** (default)**

发出不稳定的命令结果和事件

****unstable-output=hide****

抑制不稳定的命令结果和事件

-

限制：仅涵盖 QMP 的句法方面。

****\-fw\_cfg \[name=\]name,file=file****

使用文件文件中的内容添加命名的 fw\_cfg 条目。

****\-fw\_cfg \[name=\]name,string=str****

使用字符串 str 中的内容添加命名的 fw\_cfg 条目。

str 内容的终止 NUL 字符将不包含在 fw\_cfg 项目数据中。 要插入带有嵌入 NUL 字符的内容，您必须使用 file 参数。

fw\_cfg 条目由 QEMU 传递给来宾。

例子：

\-fw\_cfg name=opt/com.mycompany/blob,file=./my\_blob.bin 

-

-

创建一个名为 opt/com.mycompany/blob 的 fw\_cfg 条目，其内容来自 ./my\_blob.bin。

****\-serial dev****

将虚拟串行端口重定向到主机字符设备 dev。 默认设备是图形模式下的 **vc** 和非图形模式下的 **stdio** 。

此选项可多次使用以模拟最多 4 个串行端口。

使用 **\-serial none** 禁用所有串行端口。

可用的字符设备有：

****vc\[:WxH\]****

虚拟控制台。可选地，宽度和高度可以以像素为单位给出

vc:800x600 

-

-

也可以在字符中指定宽度或高度：

vc:80Cx24C 

-

-

****pty****

\[仅限 Linux\] 伪 TTY（自动分配新的 PTY）

****none****

没有分配设备。

****null****

无效装置

****chardev:id****

使用使用 **\-chardev** 选项定义的命名字符设备。

****/dev/XXX****

\[仅限 Linux\] 使用主机 tty，例如 **/dev/ttyS0** 。 主机串口参数根据仿真设置。

****/dev/parportN****

\[仅限 Linux，仅限并行端口\] 使用主机并行端口 N。 目前可以使用 SPP 和 EPP 并口功能。

****file:filename****

将输出写入文件名。无法读取任何字符。

****stdio****

\[仅限 Unix\] 标准输入/输出

****pipe:filename****

命名管道文件名

****COMn****

\[仅限 Windows\] 使用主机串行端口 n

****udp:\[remote\_host\]:remote\_port\[@\[src\_ip\]:src\_port\]****

这实现了 UDP 网络控制台。 如果未指定 remote\_host 或 src\_ip，它们默认为 **0.0.0.0** 。 当不使用指定的 src\_port 时，会自动选择随机端口。

如果您只想要一个简单的只读控制台，您可以使用 **netcat** 或 **nc**，通过使用以下命令启动 QEMU: **\-serial udp::4555** 和 nc : **nc -u -l -p 4555**。 每当 QEMU 向该端口写入内容时，它都会出现在 netconsole 会话中。

如果您打算通过 netconsole 发送回字符，或者您想多次停止和启动 QEMU，您应该让 QEMU 每次都使用相同的源端口，方法是对 QEMU 使用 **\-serial** **udp::4555@:4556** 之类的东西。 另一种方法是使用修补版本的 netcat，它可以侦听 TCP 端口并通过 udp 发送和接收字符。 如果您有一个激活 telnet 远程回显和单字符传输的 netcat 补丁版本，那么您可以使用以下选项来设置 netcat 重定向器以允许端口 5555 上的 telnet 访问 QEMU 端口。

****QEMU 选项:****

\-serial udp::4555@:4556

****netcat options:****

\-u -P 4555 -L 0.0.0.0:4556 -t -p 5555 -I -T

****telnet options:****

localhost 5555

-

****tcp:\[host\]:port\[,server=on|off\]\[,wait=on|off\]\[,nodelay=on|off\]\[,reconnect=seconds\]****

TCP 网络控制台有两种操作模式。 它可以将串行 I/O 发送到某个位置或等待来自某个位置的连接。 默认情况下，TCP 网络控制台被发送到端口的主机。 如果你使用 **server=on** 选项 QEMU 将等待客户端套接字应用程序在继续之前连接到端口，除非指定了 **wait=on|off** 选项。 The **nodelay=on|off** 选项禁用 Nagle 缓冲算法。 **reconnect=on** 选项仅在设置 **server=no** 时适用，如果连接断开，它将尝试在给定的时间间隔重新连接。 如果省略主机，则假定为 0.0.0.0。 一次只接受一个 TCP 连接。 您可以使用 **telnet=on** 连接到相应的字符设备。

****将 tcp 控制台发送到 192.168.0.2 端口 4444 的示例****

\-serial _tcp:192.168.0.2:4444_

****监听并等待端口 4444 连接的示例****

\-serial _tcp::4444,server=on_

****不等待并侦听 ip 192.168.0.100 端口 4444 的示例****

\-serial _tcp:192.168.0.100:4444,server=on,wait=off_

-

****telnet:host:port\[,server=on|off\]\[,wait=on|off\]\[,nodelay=on|off\]****

使用 telnet 协议而不是原始 tcp 套接字。 这些选项的工作方式与您指定 **\-serial tcp** 相同。 不同之处在于端口的作用类似于使用 telnet 选项协商的 telnet 服务器或客户端。 如果您使用支持发送中断序列的 telnet，这也将允许您发送 MAGIC\_SYSRQ 序列。 通常在 unix telnet 中，您使用 Control-\] 执行此操作，然后键入 "send break" ，然后按回车键。

****websocket:host:port,server=on\[,wait=on|off\]\[,nodelay=on|off\]****

使用 WebSocket 协议代替原始 tcp 套接字。 该端口充当 WebSocket 服务器。 不支持客户端模式。

****unix:path\[,server=on|off\]\[,wait=on|off\]\[,reconnect=seconds\]****

使用 unix 域套接字而不是 tcp 套接字。 该选项的工作方式与您指定 **\-serial tcp** 相同，但 unix 域套接字路径用于连接。

****mon:dev\_string****

这是一个特殊选项，允许将监视器多路复用到另一个串行端口。 使用 Control-a 的键序列然后按 c 可以访问监视器。 dev\_string 应该是上面指定的任何一种串行设备。 将监视器多路复用到侦听端口 4444 的 telnet 服务器上的示例如下：

**\-serial mon:telnet::4444,server=on,wait=off**

当监视器以这种方式多路复用到 stdio 时，Ctrl+C 将不再终止 QEMU，而是传递给来宾。

****braille****

盲文设备。这将使用 BrlAPI 在真机或假设备上显示盲文输出。

****msmouse****

三键串行鼠标。 将来宾配置为使用 Microsoft 协议。

-

****\-parallel dev****

将虚拟并行端口重定向到主机设备 dev（与串行端口相同的设备）。 在 Linux 主机上，**/dev/parportN** 可用于使用连接在相应主机并行端口上的硬件设备。

此选项可多次使用以模拟最多 3 个并行端口。

使用 **\-parallel none** 禁用所有并行端口。

****\-monitor dev****

将监视器重定向到主机设备 dev（与串行端口相同的设备）。 默认设备是图形模式下的 **vc** 和非图形模式下的 **stdio** 。 使用 **\-monitor none** 禁用默认监视器。

****\-qmp dev****

与 -monitor 类似，但以 'control' 模式打开。

****\-qmp-pretty dev****

与 -qmp 类似，但使用漂亮的 JSON 格式。

****\-mon \[chardev=\]name\[,mode=readline|control\]\[,pretty\[=on|off\]\]****

在 chardev 名称上设置监视器。 **mode=control** 配置 QMP 监视器（JSON RPC 样式协议），它与 HMP 不同，HMP 是具有 "(qemu)" 提示的人工监视器。 **pretty** 仅在 **mode=control** 时有效，打开 JSON 漂亮打印以方便人工阅读和调试。

****\-debugcon dev****

将调试控制台重定向到主机设备 dev（与串行端口相同的设备）。 调试控制台是一个 I/O 端口，通常是端口 0xe9；写入该 I/O 端口会将输出发送到该设备。 默认设备是图形模式下的 **vc** 和非图形模式下的 **stdio** 。

****\-pidfile file****

将 QEMU 进程 PID 存储在文件中。 如果您从脚本启动 QEMU，它会很有用。

****\-singlestep****

以单步模式运行仿真。

****\--preconfig****

在创建机器之前暂停 QEMU 进行交互式配置，这允许查询和配置会影响机器初始化的属性。 使用QMP 命令 'x-exit-preconfig' 退出预配置状态并进入下一个状态（即，如果未使用 -S ，则运行guest，如果使用 -S ，则第二次暂停）。 此选项是实验性的。

****\-S****

不要在启动时启动 CPU（您必须在监视器中键入 'c' )。

****\-overcommit mem-lock=on|off****

****\-overcommit cpu-pm=on|off****

运行 qemu 并提供有关主机资源过度使用的提示。 默认情况是假定主机过量使用所有资源。

锁定 qemu 和客户内存可以通过 **mem-lock=on** 启用（默认禁用）。 这在主机内存没有过度使用并减少来宾的最坏情况延迟时有效。

可以通过 **cpu-pm=on** 启用来宾管理主机 cpu 电源状态的能力（增加同一主机 cpu 上其他进程的延迟，但减少来宾的延迟）（默认情况下禁用）。 当主机 CPU 未过度使用时，此方法效果最佳。 使用时，主机对 CPU 周期和电源利用率的估计将不正确，未考虑来宾空闲时间。

****\-gdb dev****

在设备 dev 上接受 gdb 连接（请参阅系统仿真用户指南中的 GDB 使用章节）。 请注意，此选项不会暂停 QEMU 的执行 -- 如果您希望 QEMU 在您连接 gdb 并发出 **continue** 命令之前不启动客户机，您还需要将 **\-S** 选项传递给 QEMU。

最常用的配置是监听本地 TCP 套接字：

\-gdb tcp::3117 

-

-

但您可以指定其他后端；UDP、伪 TTY 甚至 stdio 都是合理的用例。 例如，stdio 连接允许您从 gdb 中启动 QEMU 并通过管道建立连接：

(gdb) target remote | exec qemu-system-x86\_64 -gdb stdio ... 

-

-

****\-s****

\-gdb _tcp::1234_ 的简写，即在 TCP 端口 1234 上打开 gdbserver（请参阅系统仿真用户指南中的 GDB 使用章节）。

****\-d item1\[,...\]****

启用指定项目的日志记录。 使用 '-d help' 获取日志项列表。

****\-D logfile****

在 logfile 中输出日志而不是到 stderr

****\-dfilter range1\[,...\]****

将调试输出过滤到与目标地址范围相关的内容。 过滤器规范可以是 start+size, start-size 或 start..end ，其中 start end 和 size 是所需的地址和大小。

\-dfilter 0x8000..0x8fff,0xffffffc000080000+0x200,0xffffffc000060000-0x1000 

-

-

将为从 0x8000 开始的 0x1000 大小的块和从 0xffffffc000080000 开始的 0x200 大小的块以及从 0xffffffc00005f000 开始的另一个 0x1000 大小的块中的任何代码转储输出。

****\-seed number****

强制客人使用确定性伪随机数生成器，以数字为种子。 这不会影响主机内的加密例程。

****\-L path****

设置 BIOS、VGA BIOS 和键盘映射的目录。

要列出所有数据目录，请使用 **\-L help**。

****\-bios file****

设置 BIOS 的文件名。

****\-enable-kvm****

启用 KVM 完全虚拟化支持。 仅当编译时启用 KVM 支持时，此选项才可用。

****\-xen-domid id****

指定 xen 来宾域 ID（仅限 XEN）。

****\-xen-attach****

附加到现有的 xen 域。 libxl 将在启动 QEMU 时使用它（仅限 XEN）。 将一组可用的 xen 操作限制为指定的域 id（仅限 XEN）。

****\-no-reboot****

退出而不是重新启动。

****\-no-shutdown****

不要在客户机关闭时退出 QEMU，而只是停止仿真。 这允许例如切换到监视器以提交对磁盘映像的更改。

****\-action event=action****

action 参数用于在某些访客事件发生时修改 QEMU 的默认行为。 它提供了一种通用方法来指定由 **\-no-reboot** 和 **\-no-shutdown** 参数修改的相同行为。

例子:

**\-action panic=none** **\-action reboot=shutdown,shutdown=pause** **\-watchdog i6300esb -action watchdog=pause**

****\-loadvm file****

立即从保存的状态开始（监视器中的**loadvm**)

****\-daemonize****

初始化后守护 QEMU 进程。 QEMU 在准备好接收其任何设备上的连接之前不会与标准 IO 分离。 这个选项对于外部程序启动 QEMU 来说是一种有用的方式，而不必处理初始化竞争条件。

****\-option-rom file****

将文件的内容加载为选项 ROM。 此选项对于加载诸如 EtherBoot 之类的东西很有用。

****\-rtc \[base=utc|localtime|datetime\]\[,clock=host|rt|vm\]\[,driftfix=none|slew\]****

将 **base** 指定为 **utc** 或 **localtime** 以让 RTC 分别从当前 UTC 或本地时间开始。 在 MS-DOS 或 Windows 中正确的日期需要 **localtime** 。 要从特定时间点开始，请以 **2006-06-17T16:01:21** 或 **2006-06-17**格式提供日期时间。 默认基准为 UTC。

默认情况下，RTC 由主机系统时间驱动。 这允许在客户机内部使用 RTC 作为准确的参考时钟，特别是如果主机时间平滑地遵循准确的外部参考时钟，例如通过 NTP。 如果要将访客时间与主机隔离，可以将 **clock** 设置为 **rt** ，如果主机支持，它会提供主机单调时钟。 为了防止 RTC 在暂停期间继续进行，您可以将 **clock** 设置为 **vm** （虚拟时钟）。尤其是在 icount 模式下建议使用 '**clock=vm**' ，以保持确定性；但是，请注意，在 icount 模式下，虚拟时钟的速度是可变的，并且通常与主机时钟不同。

如果您遇到时间漂移问题，尤其是 Windows 的 ACPI HAL，请启用 **driftfix** （仅限 i386 目标）。 此选项将尝试找出 Windows 客户机未处理多少计时器中断，并将重新注入它们。

****\-icount \[shift=N|auto\]\[,align=on|off\]\[,sleep=on|off\]\[,rr=record|replay,rrfile=filename\[,rrsnapshot=snapshot\]\]****

启用虚拟指令计数器。 虚拟 CPU 将每 2^N ns 的虚拟时间执行一条指令。 如果指定了 **auto** ，那么虚拟 cpu 速度将自动调整，以将虚拟时间保持在实时的几秒钟内。

请注意，虽然此选项可以提供确定性行为，但它不提供周期精确仿真。 现代 CPU 包含具有复杂缓存层次结构的超标量乱序内核。 执行的指令数量通常与实际性能几乎没有相关性或没有相关性。

当虚拟 CPU 处于睡眠状态时，除非指定 **sleep=on** ，否则虚拟时间将以默认速度提前。 使用 **sleep=on** 时，只要虚拟 CPU 进入睡眠模式，虚拟时间就会立即跳到下一个定时器截止时间，如果没有启用定时器，则不会提前。 从客户的角度来看，这种行为给出了确定的执行时间。 如果启用了 icount，则默认值为 **sleep=off**。 **sleep=on** 不能与 **shift=auto** 或 **align=on**一起使用。

**align=on** 将激活延迟算法，该算法将尝试同步主机时钟和虚拟时钟。 目标是让客人以换档选项施加的真实频率运行。 每当访客时钟落后于主机时钟并且指定了 **align=on** 时，我们就会向用户打印一条消息以告知延迟。 目前，当 **shift** 为 **auto** 时，此选项不起作用。 注意：同步算法将适用于访客时钟运行在主机时钟之前的那些移位值。 通常，当移位值很高时会发生这种情况（多高取决于主机）。 如果启用了 icount，则默认值为 is **align=off**。

当指定 **rr** 选项时，启用确定性记录/重播。 还必须提供 **rrfile=** 选项以指定重播日志的路径。 在记录模式下，数据被写入该文件，而在重放模式下，数据被读回。 如果给出 **rrsnapshot** 选项，则它指定 VM 快照名称。 在记录模式下，在开始执行记录时会创建一个具有给定名称的新 VM 快照。 在重放模式下，此选项指定用于加载初始 VM 状态的快照名称。

****\-watchdog model****

创建一个虚拟硬件看门狗设备。 一旦启用（通过来宾操作），必须由来宾内部的代理定期轮询看门狗，否则来宾将重新启动。 选择您的客人有驱动程序的型号。

该模型是要仿真的硬件看门狗模型。 使用 **\-watchdog help** 列出可用的硬件型号。 一个访客只能启用一个看门狗。

可能提供以下型号：

****ib700****

iBASE 700 是一个非常简单的带有单个定时器的 ISA 看门狗。

****i6300esb****

Intel 6300ESB I/O 控制器集线器是一个功能更强大的基于 PCI 的双定时器看门狗。

****diag288****

由诊断 288 超级调用（当前仅 KVM）支持的 s390x 虚拟看门狗。

-

****\-watchdog-action action****

该操作控制 QEMU 在看门狗计时器到期时将执行的操作。 默认为 **reset** （强制重置来宾）。 其他可能的操作包括： **shutdown** (尝试正常关闭客户机), **poweroff** (强制关闭客户机), **inject-nmi** (向客户机注入 NMI), **pause** (暂停客户机), **debug** (打印调试消息并继续) 或 **none** (什么都不做)。

请注意， **shutdown** 操作要求来宾响应 ACPI 信号，在看门狗可能已过期的情况下，它可能无法执行此操作，因此不建议将 **\-watchdog-action shutdown** 用于生产用途。

例子：

**\-watchdog i6300esb -watchdog-action pause**; **\-watchdog ib700**

****\-echr numeric\_ascii\_value****

更改使用监视器和串行共享时用于切换到监视器的转义字符。 使用 **\-nographic** 选项时，默认值为 **0x01** 。 **0x01** 等于按下 **Control-a**。 您可以从 1 到 26 映射到 Control-a 到 Control-z的 ascii 控制键中选择不同的字符。 例如，您可以使用以下任一方法将转义字符更改为 Control-t。

**\-echr 0x14**; **\-echr 20**

****\-incoming tcp:\[host\]:port\[,to=maxport\]\[,ipv4=on|off\]\[,ipv6=on|off\]****

****\-incoming rdma:host:port\[,ipv4=on|off\]\[,ipv6=on|off\]****

准备传入迁移，侦听给定的 tcp 端口。

****\-incoming unix:socketpath****

准备传入迁移，监听给定的 unix 套接字。

****\-incoming fd:fd****

接受来自给定文件描述符的传入迁移。

****\-incoming exec:cmdline****

接受传入迁移作为指定外部命令的输出。

****\-incoming defer****

等待通过 migrate\_incoming 指定 URI。 监视器可用于在发出 migrate\_incoming 之前更改设置（例如迁移参数）以允许迁移开始。

****\-only-migratable****

仅允许可迁移设备。 不允许设备进入不可迁移状态。

****\-nodefaults****

不要创建默认设备。 通常，QEMU 会设置默认设备，如串口、并口、虚拟控制台、监视器设备、VGA 适配器、软盘和光驱等。 **\-nodefaults** 选项将禁用所有这些默认设备。

****\-chroot dir****

在开始来宾执行之前，chroot 到指定的目录。 与 -runas 结合使用尤其有用。

****\-runas user****

在开始执行来宾之前，立即删除 root 权限，切换到指定的用户。

****\-prom-env variable=value****

将 OpenBIOS nvram 变量设置为给定值（仅限 PPC、SPARC）。

qemu-system-sparc -prom-env 'auto-boot?=false' \\ -prom-env 'boot-device=sd(0,2,0):d' -prom-env 'boot-args=linux single' 

-

-

qemu-system-ppc -prom-env 'auto-boot?=false' \\ -prom-env 'boot-device=hd:2,\\yaboot' \\ -prom-env 'boot-args=conf=hd:2,\\yaboot.conf' 

-

-

****\-semihosting****

启用半主机模式（仅限 ARM, M68K, Xtensa, MIPS, Nios II, RISC-V)。

请注意，这允许来宾直接访问主机文件系统，因此只能与受信任的来宾操作系统一起使用。

请参阅 -semihosting-config 选项文档以获取有关此启用的设施的更多信息。

****\-semihosting-config \[enable=on|off\]\[,target=native|gdb|auto\]\[,chardev=id\]\[,arg=str\[,...\]\]****

启用和配置半主机（仅限 ARM, M68K, Xtensa, MIPS, Nios II, RISC-V)。

请注意，这允许来宾直接访问主机文件系统，因此只能与受信任的来宾操作系统一起使用。

在 Arm 上，这实现了标准的半主机 API，版本 2.0。

在 M68K 上，它实现了 libgloss 使用的 "ColdFire GDB" 接口。

Xtensa 半主机提供基本的文件 IO 调用，例如 open/read/write/seek/select。 用于 ISS 和 linux 平台 "sim" 的 Tensilica baremetal libc 使用此接口。

在 RISC-V 上，这实现了标准的半主机 API，版本 0.2。

****target=native|gdb|auto****

定义半主机调用将被寻址到 QEMU (**native**) 或 GDB (**gdb**)。 默认值为 **auto** ，这意味着在调试会话期间使用 **gdb** ，否则为 **native** 。

****chardev=str1****

当不在 gdb 中时，将输出发送到 chardev 后端输出以进行本机或自动输出

****arg=str1,arg=str2,...****

允许用户传递输入参数，并且可以多次使用来建立一个列表。 为了向后兼容，仍然支持传递命令行的旧式-style **\-kernel**/**\-append** 方法。 如果同时指定了 **\--semihosting-config arg** 参数和 **\-kernel**/**\-append** ，则前者将传递给 semihosting，因为它始终具有优先权。

-

****\-old-param****

旧参数模式（仅限 ARM）。

****\-sandbox arg\[,obsolete=string\]\[,elevateprivileges=string\]\[,spawn=string\]\[,resourcecontrol=string\]****

启用 Seccomp 模式 2 系统调用过滤器。 'on' 将启用系统调用过滤， 'off' 将禁用它。 默认值为 'off'。

****obsolete=string****

启用过时的系统调用

****elevateprivileges=string****

禁用 set\*uid|gid 系统调用

****spawn=string****

禁用 \*fork 和 execve

****resourcecontrol=string****

禁用进程关联和计划优先级

-

****\-readconfig file****

从文件中读取设备配置。 当您想使用许多命令行选项生成 QEMU 进程但又不想超过命令行字符限制时，这种方法很有用。

****\-no-user-config****

**\-no-user-config** 选项使 QEMU 不会在 sysconfdir 上加载任何用户提供的配置文件。

****\-trace \[\[enable=\]pattern\]\[,events=file\]\[,file=file\]****

指定跟踪选项。

**\[enable=\]PATTERN**

立即启用匹配 _PATTERN_ 的事件（事件名称或通配模式）。 此选项仅在 QEMU 已使用 **simple**, **log** 或 **ftrace** 跟踪后端编译时可用。 要指定多个事件或模式，请多次指定 **\-trace** 选项。

使用 **\-trace help** 打印跟踪点名称的列表。

-

-

**events=FILE**

立即启用 _FILE_ 中列出的事件。 该文件的每一行必须包含一个事件名称（如 **trace-events-all** 文件中所列）；通配模式也被接受。 此选项仅在 QEMU 已使用 **simple**, **log** 或 **ftrace** 跟踪后端编译时可用。

-

-

**file=FILE**

将输出跟踪记录到 _FILE_ 。 仅当 QEMU 已使用 **simple** 跟踪后端编译时，此选项才可用。

-

-

****\-plugin file=file\[,argname=argvalue\]****

加载插件。

****file=file****

从共享库文件加载给定的插件。

****argname=argvalue****

参数传递给插件。 （可以多次给予。）

-

****\-enable-fips****

启用 FIPS 140-2 合规模式。

****\-msg \[timestamp\[=on|off\]\]\[,guest-name\[=on|off\]\]****

控制错误消息格式。

****timestamp=on|off****

带有时间戳的消息前缀。默认为关闭。

****guest-name=on|off****

使用来宾名称为消息添加前缀，但仅当设置了 -name guest 选项时，否则该选项将被忽略。 默认为关闭。

-

****\-dump-vmstate file****

将当前机器类型的 json 编码的 vmstate 信息转储到文件中

****\-enable-sync-profile****

启用同步分析。

-

[通用对象创建](#__u901A___u7528___u5BF9___u8C61___u521B___u5EFA_)
-----------------------------------------------------------

****\-object typename\[,prop1=value1,...\]****

按照指定的顺序创建类型名称设置属性的新对象。 请注意，必须设置 'id' 属性。 这些对象放置在 '/objects' 路径中。

****\-object memory-backend-file,id=id,size=size,mem-path=dir,share=on|off,discard-data=on|off,merge=on|off,dump=on|off,prealloc=on|off,host-nodes=host-nodes,policy=default|preferred|bind|interleave,align=align,readonly=on|off****

创建一个内存文件后端对象，该对象可用于支持具有大页面的来宾 RAM。

**id** 参数是一个唯一的 ID，将用于在其他参数中引用此内存区域，例如 **\-numa**, **\-device nvdimm** 等。

**size** 选项提供内存区域的大小，并接受常见的后缀，例如 **500M** 。

**mem-path** 提供了共享内存或大页面文件系统挂载的路径。

**share** 布尔选项确定内存区域是标记为 QEMU 私有还是共享。 后者允许协作的外部进程访问 QEMU 内存区域。

由于 Linux 提供的 RDMA API 的限制，pvrdma 设备也需要 **share** 。

在某些情况下，设置 share=on 可能会影响为内存后端配置 NUMA 绑定的能力，有关更多详细信息，请参阅 Linux 内核源代码树上的 Documentation/vm/numa\_memory\_policy.txt 。

将 **discard-data** 布尔选项设置为 on 表示可以在 QEMU 退出时销毁文件内容，以避免不必要地将数据刷新到支持文件。 请注意， **discard-data** i只是一种优化，如果 QEMU 意外中止或使用 SIGKILL 终止，QEMU 可能不会丢弃文件内容。

**merge** 布尔选项启用内存合并，也称为 MADV\_MERGEABLE，以便内核 Samepage Merging 将考虑内存重复数据删除的页面。

将 **dump** 布尔选项设置为关闭会从核心转储中排除内存。 此功能也称为 MADV\_DONTDUMP。

**prealloc** 布尔选项启用内存预分配。

**host-nodes** 选项将内存范围绑定到 NUMA 主机节点列表。

**policy** 选项将 NUMA 策略设置为以下值之一：

****default****

默认主机策略

****preferred****

首选给定的主机节点列表进行分配

****bind****

将内存分配限制到给定的主机节点列表

****interleave****

在给定的主机节点列表中交错内存分配

-

**align** 选项指定 QEMU mmap(2) **mem-path** 时的基地址对齐，并接受常见的后缀，例如 **2M** 。 某些由 **mem-path** 指定的后端存储需要与 QEMU 使用的默认对齐不同的对齐方式，例如设备 DAX /dev/dax0.0 需要 2M 对齐而不是 4K。 在这种情况下，用户可以通过此选项指定所需的对齐方式。

**pmem** 选项指定 **mem-path** 指定的后备文件是否位于可以使用 SNIA NVM 编程模型（例如 Intel NVDIMM）访问的主机持久内存中。 如果 **pmem** 设置为 'on' ，QEMU 将采取必要的操作来保证它自己对 **mem-path** 的写入的持久性（例如在 vNVDIMM 标签仿真和实时迁移中）。 此外，我们将使用 MAP\_SYNC 标志映射后端文件，以确保在主机崩溃或电源故障的情况下文件元数据与 **mem-path** 同步。 MAP\_SYNC 需要主机内核（自 Linux 内核 4.15 起）和使用 DAX 选项挂载的 **mem-path** 文件系统的支持。

**readonly** 选项指定备份文件是以只读方式打开还是以读写方式打开（默认）。

****\-object memory-backend-ram,id=id,merge=on|off,dump=on|off,share=on|off,prealloc=on|off,size=size,host-nodes=host-nodes,policy=default|preferred|bind|interleave****

创建一个内存后端对象，该对象可用于支持来宾 RAM。 内存后端对象比传统上用于定义来宾 RAM 的 **\-m** 选项提供更多控制。 有关选项的描述，请参阅 **memory-backend-file** 。

****\-object memory-backend-memfd,id=id,merge=on|off,dump=on|off,share=on|off,prealloc=on|off,size=size,host-nodes=host-nodes,policy=default|preferred|bind|interleave,seal=on|off,hugetlb=on|off,hugetlbsize=size****

创建一个匿名内存文件后端对象，它允许 QEMU 与外部进程共享内存（例如，当使用 vhost-user 时）。 内存分配有 memfd 和可选的密封。（仅限 Linux）

**seal** 选项创建一个密封文件，它将阻止进一步调整内存大小（默认为 'on' )。

**hugetlb** 选项指定要创建的文件驻留在hugetlbfs 文件系统中（从Linux 4.14 开始）。 与 **hugetlb** 选项一起使用时， **hugetlbsize** 选项在支持多个hugetlb 页面大小的系统上指定hugetlb 页面大小（它必须是系统支持的2 的幂值）。

在某些版本的 Linux 中， **hugetlb** 选项与 **seal** 选项不兼容（至少需要 Linux 4.16）。

有关其他选项的说明，请参阅 **memory-backend-file** 。

默认情况下，memfd 的 **share** 布尔选项是打开的。

****\-object rng-builtin,id=id****

创建一个随机数生成器后端，该后端从 QEMU 内置函数中获取熵。 **id** 参数是一个唯一的 ID，将用于从 **virtio-rng** 设备引用这个熵后端。 默认情况下， **virtio-rng** 设备使用这个 RNG 后端。

****\-object rng-random,id=id,filename=/dev/random****

创建一个随机数生成器后端，该后端从主机上的设备获取熵。 **id** 参数是一个唯一的 ID，将用于从 **virtio-rng** 设备引用这个熵后端。 **filename** 参数指定从哪个文件获取熵，如果省略则默认为 **/dev/urandom** 。

****\-object rng-egd,id=id,chardev=chardevid****

创建一个随机数生成器后端，该后端从主机上运行的外部守护程序获取熵。 **id** 参数是一个唯一的 ID，将用于从 **virtio-rng** 设备引用这个熵后端。 **chardev** 参数是提供与 RNG 守护程序连接的字符设备后端的唯一 ID。

****\-object tls-creds-anon,id=id,endpoint=endpoint,dir=/path/to/cred/dir,verify-peer=on|off****

创建一个 TLS 匿名凭证对象，该对象可用于在网络后端提供 TLS 支持。 **id** 参数是网络后端用于访问凭证的唯一 ID。 **endpoint** 是 **server** 还是 **client** ，具体取决于使用凭据的 QEMU 网络后端是充当客户端还是充当服务器。 如果启用了 **verify-peer** （默认值），则一旦握手完成，将对等凭据进行验证，尽管这是匿名凭据的无操作。

dir 参数告诉 QEMU 在哪里可以找到凭证文件。 对于服务器端点，此目录可能包含一个文件 dh-params.pem ，提供用于 TLS 服务器的 diffie-hellman 参数。 如果该文件丢失，QEMU 将在启动时生成一组 DH 参数。 这是一个消耗随机池熵的计算量大的操作，因此建议预先生成一组持久的参数并保存。

****\-object tls-creds-psk,id=id,endpoint=endpoint,dir=/path/to/keys/dir\[,username=username\]****

创建 TLS 预共享密钥 (PSK) 凭据对象，可用于在网络后端提供 TLS 支持。 **id** 参数是网络后端用于访问凭证的唯一 ID。 **endpoint** 是 **server** 还是 **client** ，具体取决于使用凭据的 QEMU 网络后端是充当客户端还是充当服务器。 仅对于客户端， **username** 是将发送到服务器的用户名。 如果省略，则默认为 "qemu"。

dir 参数告诉 QEMU 在哪里可以找到密钥文件。 它被称为 "dir/keys.psk" 并包含 "username:key" 对。 使用 GnuTLS **psktool** 程序可以最轻松地创建此文件。

对于服务器端点，dir 还可能包含一个文件 dh-params.pem ，提供用于 TLS 服务器的 diffie-hellman 参数。 如果该文件丢失，QEMU 将在启动时生成一组 DH 参数。 这是一个消耗随机池熵的计算成本高的操作，因此建议预先生成一组持久的参数并保存。

****\-object tls-creds-x509,id=id,endpoint=endpoint,dir=/path/to/cred/dir,priority=priority,verify-peer=on|off,passwordid=id****

创建一个 TLS 匿名凭证对象，该对象可用于在网络后端提供 TLS 支持。 **id** 参数是网络后端用于访问凭证的唯一 ID。 **endpoint** 是 **server** 还是 **client** ，具体取决于使用凭据的 QEMU 网络后端是充当客户端还是充当服务器。 如果启用了 **verify-peer** （默认），那么一旦握手完成，将对等凭据进行验证。 对于 x509 证书，这意味着客户端也必须提供有效的客户端证书。

dir 参数告诉 QEMU 在哪里可以找到凭证文件。 对于服务器端点，此目录可能包含一个文件 dh-params.pem ，提供用于 TLS 服务器的 diffie-hellman 参数。 如果该文件丢失，QEMU 将在启动时生成一组 DH 参数。 这是一个消耗随机池熵的计算量大的操作，因此建议预先生成一组持久的参数并保存。

对于 x509 证书凭证，该目录将包含提供 x509 证书的更多文件。 证书必须以 PEM 格式存储，文件名为 ca-cert.pem, ca-crl.pem (可选), server-cert.pem (仅限服务器), server-key.pem (仅限服务器), client-cert.pem (仅限客户端), and client-key.pem (仅限客户端)。

对于包含敏感私钥的 server-key.pem 和 client-key.pem 文件，可以通过提供 passwordid 参数来使用加密版本。 这提供了先前创建的包含解密密码的 **secret** 对象的 ID。

priority 参数允许覆盖 gnutls 使用的全局默认优先级。 如果系统管理员需要为 QEMU 使用一组较弱的加密优先级，而不可能将弱点强加到所有应用程序上，这将很有用。 或者相反，如果想要 QEMU 的默认值比所有其他应用程序更强，他们可以通过这个参数来实现。 它的格式是一个 gnutls 优先级字符串，如 _https://gnutls.org/manual/html\_node/Priority-Strings.html_ 中所述。

****\-object tls-cipher-suites,id=id,priority=priority****

创建一个 TLS 密码套件对象，该对象可用于控制允许应用程序使用的 TLS 密码/协议算法。

**id** 参数是一个唯一 ID，前端将使用它从主机访问允许的 TLS 密码套件的有序列表。

**priority** 参数允许覆盖 gnutls 使用的全局默认优先级。 如果系统管理员需要为 QEMU 使用一组较弱的加密优先级，而不可能将弱点强加到所有应用程序上，这将很有用。 或者相反，如果想要 QEMU 的默认值比所有其他应用程序更强，他们可以通过这个参数来实现。 它的格式是一个 gnutls 优先级字符串，如 _https://gnutls.org/manual/html\_node/Priority-Strings.html_ 中所述。

使用此对象的一个示例是控制 UEFI HTTPS 引导。 tls-cipher-suites 对象通过 fw\_cfg 将允许的 TLS 密码套件的有序列表从主机端公开给客户固件。 该列表表示为 IANA\_TLS\_CIPHER 对象的数组。 固件使用 IANA\_TLS\_CIPHER 阵列来配置访客端 TLS。

在以下示例中，检索主机端策略的优先级由 **priority** 属性给出。 鉴于 QEMU 使用 GNUTLS， **priority=@SYSTEM** 可用于引用 /etc/crypto-policies/back-ends/gnutls.config。

\# qemu-system-x86\_64 \\ -object tls-cipher-suites,id=mysuite0,priority=@SYSTEM \\ -fw\_cfg name=etc/edk2/https/ciphers,gen\_id=mysuite0 

-

-

****\-object filter-buffer,id=id,netdev=netdevid,interval=t\[,queue=all|rx|tx\]\[,status=on|off\]\[,position=head|tail|id=<id>\]\[,insert=behind|before\]****

间隔 t 不能为 0，此过滤器对数据包传送进行批处理：在 netdev netdevid 上的给定间隔内到达的所有数据包都会延迟到间隔结束。 间隔以微秒为单位。 **status** 是可选的，指示 netfilter 是打开（启用）还是关闭（禁用），netfilter 的默认状态将是 'on' 。

queue all|rx|tx 是一个可以应用于任何网络过滤器的选项。

**all**: 过滤器连接到 netdev 的接收和发送队列（默认）。

**rx**: 过滤器附加到 netdev 的接收队列，它将接收发送到 netdev 的数据包。

**tx**: 过滤器附加到netdev的传输队列，它将接收netdev发送的数据包。

position head|tail|id=<id> 是一个选项，用于指定过滤器应该在过滤器列表中的什么位置插入。 它可以应用于任何网络过滤器。

**head**: 过滤器插入到过滤器列表的头部，在任何现有过滤器之前。

**tail**: 过滤器插入到过滤器列表的尾部，位于任何现有过滤器之后（默认）。

**id=<id>**: 过滤器插入到<id>指定的过滤器之前或之后，见下面的插入选项。

insert behind|before 是一个选项，用于指定相对于 position=id=<id> 指定的过滤器插入新过滤器的位置。 它可以应用于任何网络过滤器。

**before**: 在指定过滤器之前插入。

**behind**: 在指定过滤器后面插入（默认）。

****\-object filter-mirror,id=id,netdev=netdevid,outdev=chardevid,queue=all|rx|tx\[,vnet\_hdr\_support\]\[,position=head|tail|id=<id>\]\[,insert=behind|before\]****

netdev netdevid 上的 filter-mirror ，将网络数据包镜像到 chardevchardevid，如果它有 vnet\_hdr\_support 标志， filter-mirror 将使用 vnet\_hdr\_len 镜像数据包。

****\-object filter-redirector,id=id,netdev=netdevid,indev=chardevid,outdev=chardevid,queue=all|rx|tx\[,vnet\_hdr\_support\]\[,position=head|tail|id=<id>\]\[,insert=behind|before\]****

netdev netdevid 上的 filter-redirector ，将过滤器的网络数据包重定向到 chardev chardevid，并将 indev 的数据包重定向到过滤器。如果它具有 vnet\_hdr\_support 标志， filter-redirector 将使用 vnet\_hdr\_len 重定向数据包。 创建一个 filter-redirector ，我们需要区分 outdev id 和 indev id，id 不能相同。 我们可以只使用 indev 或 outdev，但至少需要指定 indev 或 outdev 之一。

****\-object filter-rewriter,id=id,netdev=netdevid,queue=all|rx|tx,\[vnet\_hdr\_support\]\[,position=head|tail|id=<id>\]\[,insert=behind|before\]****

Filter-rewriter 是 COLO 项目的一部分。它将 tcp 数据包从 primary 重写到 secondary 以保持辅助 tcp 连接，并将 tcp 数据包从辅助重写到 primary 使 tcp 数据包可以由客户端处理。如果它具有 vnet\_hdr\_support 标志，我们可以解析带有 vnet 标头的数据包。

usage: colo secondary: -object filter-redirector,id=f1,netdev=hn0,queue=tx,indev=red0 -object filter-redirector,id=f2,netdev=hn0,queue=rx,outdev=red1 -object filter-rewriter,id=rew0,netdev=hn0,queue=all

****\-object filter-dump,id=id,netdev=dev\[,file=filename\]\[,maxlen=len\]\[,position=head|tail|id=<id>\]\[,insert=behind|before\]****

将 netdev dev 上的网络流量转储到 filename 指定的文件。 每个数据包最多存储 len 个字节（默认为 64k）。 文件格式为libpcap，因此可以使用tcpdump或Wireshark等工具进行分析。

****\-object colo-compare,id=id,primary\_in=chardevid,secondary\_in=chardevid,outdev=chardevid,iothread=id\[,vnet\_hdr\_support\]\[,notify\_dev=id\]\[,compare\_timeout=@var{ms}\]\[,expired\_scan\_cycle=@var{ms}\]\[,max\_queue\_size=@var{size}\]****

Colo-compare 从primary\_in chardevid 和secondary\_in 中获取数据包，然后比较primary packet 和secondary packet 的payload 是否相同。 如果相同，它会将primary packet输出到out\_dev，否则它会通知 COLO-framework 做checkpoint并将primary packet发送到out\_dev。 为了提高效率，我们需要将比较的任务放在另一个iothread中。 如果它有 vnet\_hdr\_support 标志，colo 比较将使用 vnet\_hdr\_len 发送/接收数据包。 _compare\_timeout=@var{ms_} 决定了 colo-compare 保持数据包的最长时间。 _expired\_scan\_cycle=@var{ms_} 是设置扫描过期主节点网络包的周期。 _max\_queue\_size=@var{size_} 是根据用户环境设置最大比较队列大小。 如果用户想使用 Xen COLO，需要添加 notify\_dev 来通知 Xen colo-frame 做检查点。

COLO-compare 必须在 filter-mirror, filter-redirector 和 filter-rewriter 的帮助下使用。

KVM COLO primary: -netdev tap,id=hn0,vhost=off,script=/etc/qemu-ifup,downscript=/etc/qemu-ifdown -device e1000,id=e0,netdev=hn0,mac=52:a4:00:12:78:66 -chardev socket,id=mirror0,host=3.3.3.3,port=9003,server=on,wait=off -chardev socket,id=compare1,host=3.3.3.3,port=9004,server=on,wait=off -chardev socket,id=compare0,host=3.3.3.3,port=9001,server=on,wait=off -chardev socket,id=compare0-0,host=3.3.3.3,port=9001 -chardev socket,id=compare\_out,host=3.3.3.3,port=9005,server=on,wait=off -chardev socket,id=compare\_out0,host=3.3.3.3,port=9005 -object iothread,id=iothread1 -object filter-mirror,id=m0,netdev=hn0,queue=tx,outdev=mirror0 -object filter-redirector,netdev=hn0,id=redire0,queue=rx,indev=compare\_out -object filter-redirector,netdev=hn0,id=redire1,queue=rx,outdev=compare0 -object colo-compare,id=comp0,primary\_in=compare0-0,secondary\_in=compare1,outdev=compare\_out0,iothread=iothread1 secondary: -netdev tap,id=hn0,vhost=off,script=/etc/qemu-ifup,down script=/etc/qemu-ifdown -device e1000,netdev=hn0,mac=52:a4:00:12:78:66 -chardev socket,id=red0,host=3.3.3.3,port=9003 -chardev socket,id=red1,host=3.3.3.3,port=9004 -object filter-redirector,id=f1,netdev=hn0,queue=tx,indev=red0 -object filter-redirector,id=f2,netdev=hn0,queue=rx,outdev=red1 Xen COLO primary: -netdev tap,id=hn0,vhost=off,script=/etc/qemu-ifup,downscript=/etc/qemu-ifdown -device e1000,id=e0,netdev=hn0,mac=52:a4:00:12:78:66 -chardev socket,id=mirror0,host=3.3.3.3,port=9003,server=on,wait=off -chardev socket,id=compare1,host=3.3.3.3,port=9004,server=on,wait=off -chardev socket,id=compare0,host=3.3.3.3,port=9001,server=on,wait=off -chardev socket,id=compare0-0,host=3.3.3.3,port=9001 -chardev socket,id=compare\_out,host=3.3.3.3,port=9005,server=on,wait=off -chardev socket,id=compare\_out0,host=3.3.3.3,port=9005 -chardev socket,id=notify\_way,host=3.3.3.3,port=9009,server=on,wait=off -object filter-mirror,id=m0,netdev=hn0,queue=tx,outdev=mirror0 -object filter-redirector,netdev=hn0,id=redire0,queue=rx,indev=compare\_out -object filter-redirector,netdev=hn0,id=redire1,queue=rx,outdev=compare0 -object iothread,id=iothread1 -object colo-compare,id=comp0,primary\_in=compare0-0,secondary\_in=compare1,outdev=compare\_out0,notify\_dev=nofity\_way,iothread=iothread1 secondary: -netdev tap,id=hn0,vhost=off,script=/etc/qemu-ifup,down script=/etc/qemu-ifdown -device e1000,netdev=hn0,mac=52:a4:00:12:78:66 -chardev socket,id=red0,host=3.3.3.3,port=9003 -chardev socket,id=red1,host=3.3.3.3,port=9004 -object filter-redirector,id=f1,netdev=hn0,queue=tx,indev=red0 -object filter-redirector,id=f2,netdev=hn0,queue=rx,outdev=red1 

-

-

如果您想了解上述命令行的详细信息，可以阅读 colo-compare git log。

****\-object cryptodev-backend-builtin,id=id\[,queues=queues\]****

创建一个 cryptodev 后端，该后端从 QEMU cipher APIS 执行加密操作。 id 参数是一个唯一的 ID，用于从 **virtio-crypto** 设备引用这个 cryptodev 后端。 queues 参数是可选的，它指定了cryptodev后端的队列号，队列的默认值为1。

\# qemu-system-x86\_64 \\ \[...\] \\ -object cryptodev-backend-builtin,id=cryptodev0 \\ -device virtio-crypto-pci,id=crypto0,cryptodev=cryptodev0 \\ \[...\] 

-

-

****\-object cryptodev-vhost-user,id=id,chardev=chardevid\[,queues=queues\]****

创建一个由 chardev chardevid 支持的 vhost-user 后端。 id 参数是一个唯一的 ID，用于从 **virtio-crypto** 设备引用这个 cryptodev 后端。 chardev 应该是一个支持 unix 域套接字的。 vhost-user 使用专门定义的协议将 vhost ioctl 替换消息传递给套接字另一端的应用程序。 queues 参数是可选的，它指定了多队列 vhost-user 的 cryptodev 后端的队列号，queues 默认为 1。

\# qemu-system-x86\_64 \\ \[...\] \\ -chardev socket,id=chardev0,path=/path/to/socket \\ -object cryptodev-vhost-user,id=cryptodev0,chardev=chardev0 \\ -device virtio-crypto-pci,id=crypto0,cryptodev=cryptodev0 \\ \[...\] 

-

-

****\-object secret,id=id,data=string,format=raw|base64\[,keyid=secretid,iv=string\]****

****\-object secret,id=id,file=filename,format=raw|base64\[,keyid=secretid,iv=string\]****

定义一个秘密来存储密码、加密密钥或一些其他敏感数据。 敏感数据可以通过 data 参数直接传递，也可以通过 file 参数间接传递。 除非敏感数据被加密，否则使用 data 参数是不安全的。

敏感数据可以以原始格式（默认）或 base64 格式提供。 当编码为 JSON 时，原始格式仅支持有效的 UTF-8 字符，因此建议使用 base64 发送二进制数据。 QEMU 将从提供的格式转换为内部需要的格式。 例如，可以以原始格式提供 RBD 密码，即使它在传递到 RBD 服务器时会进行 base64 编码。

为了增加保护，可以使用 AES-256-CBC 密码对与机密相关的数据进行加密。 通过提供 keyid 和 iv 参数来指示加密的使用。 keyid 参数提供了先前定义的包含 AES-256 解密密钥的密钥的 ID。 此密钥应为 32 字节长并采用 base64 编码。 iv 参数提供了用于加密此特定秘密的随机初始化向量，并且应该是 16 字节 IV 的 base64 加密字符串。

最简单（不安全）的用法是提供秘密内联

\# qemu-system-x86\_64 -object secret,id=sec0,data=letmein,format=raw 

-

-

最简单的安全用法是通过文件提供秘密

\# printf "letmein" > mypasswd.txt # QEMU\_SYSTEM\_MACRO -object secret,id=sec0,file=mypasswd.txt,format=raw

为了提高安全性，应使用 AES-256-CBC 。 为了说明用法，请考虑可以加密数据的 openssl 命令行工具。 请注意，加密时，必须使用标准 PKCS#5/6 兼容的填充算法将明文填充到密码块大小（32 字节）。

首先需要以 base64 编码创建主密钥：

\# openssl rand -base64 32 > key.b64 # KEY=$(base64 -d key.b64 | hexdump -v -e '/1 "%02X"') 

-

-

每个要加密的秘密都需要生成一个随机初始化向量。 这些不需要保密

\# openssl rand -base64 16 > iv.b64 # IV=$(base64 -d iv.b64 | hexdump -v -e '/1 "%02X"') 

-

-

现在可以对要定义的秘密进行加密，在这种情况下，我们告诉 openssl 对结果进行 base64 编码，但如果需要，它可以保留为原始字节。

\# SECRET=$(printf "letmein" | openssl enc -aes-256-cbc -a -K $KEY -iv $IV) 

-

-

启动 QEMU 时，创建一个指向 **key.b64** 的主密钥并指定用于解密用户密码。 将 **iv.b64** 的内容传给第二个secret

\# qemu-system-x86\_64 \\ -object secret,id=secmaster0,format=base64,file=key.b64 \\ -object secret,id=sec0,keyid=secmaster0,format=base64,\\ data=$SECRET,iv=$(<iv.b64) 

-

-

****\-object sev-guest,id=id,cbitpos=cbitpos,reduced-phys-bits=val,\[sev-device=string,policy=policy,handle=handle,dh-cert-file=file,session-file=file,kernel-hashes=on|off\]****

创建一个安全加密虚拟化 (SEV) 来宾对象，该对象可用于在 AMD 处理器上提供来宾内存加密支持。

当启用内存加密时，使用其中一个物理地址位(又称 C位)来标记内存页是否受到保护。 **cbitpos** 用于提供C位的位置。C位的位置依赖于主机族，因此用户必须提供这个值。

在EPYC上，这个值应该是47。

当启用内存加密时，我们会丢失物理地址空间中的某些位。 **reduced-phys-bits** 用于提供物理地址空间中丢失的比特数。 与c位类似，该值依赖于Host family。 在EPYC上，这个值应该是5。

**sev-device** 提供了设备文件，用于与运行在AMD安全处理器内的SEV固件进行通信。 默认设备为 '/dev/sev' 。 如果硬件支持内存加密，那么CCP驱动会创建 /dev/sev 设备。

该 **policy** 提供了由 SEV 固件强制执行的访客策略，并限制管理程序可以在该访客上执行哪些配置和操作命令。 该政策应由客人所有者提供，并受客人约束，并且在客人的整个生命周期内都不能更改。 默认值为 0。

如果访客 **policy** 允许与另一个 SEV 访客共享密钥，则 **handle** 可用于提供共享密钥的访客句柄。

**dh-cert-file** 和 **session-file** 提供了在 SEV 规范中定义的访客所有者的公共 Diffie-Hillman 密钥。 PDH 和会话参数用于与访客所有者建立加密会话以协商用于证明的密钥。 该文件必须以 base64 编码。

**kernel-hashes** 将给定 kernel/initrd/ cmdline 的哈希值添加到指定的客户机固件页面，用于使用 -kernel 进行测量的 Linux 引导。 默认为关闭。（从 6.2 开始）

例如启动 SEV 来宾

\# qemu-system-x86\_64 \\ ...... \\ -object sev-guest,id=sev0,cbitpos=47,reduced-phys-bits=5 \\ -machine ...,memory-encryption=sev0 \\ ..... 

-

-

****\-object authz-simple,id=id,identity=string****

创建一个授权对象来控制对网络服务的访问。

**identity** 参数用于标识用户，其格式取决于授权对象关联的网络服务。 对于基于 TLS x509 证书的授权，身份必须是 x509 专有名称。 请注意，必须注意对专有名称中的任何逗号进行转义。

验证 x509 专有名称的示例授权对象如下所示：

\# qemu-system-x86\_64 \\ ... \\ -object 'authz-simple,id=auth0,identity=CN=laptop.example.com,,O=Example Org,,L=London,,ST=London,,C=GB' \\ ... 

-

-

请注意引号的使用，因为 x509 专有名称包含空格，并转义了 ','。

****\-object authz-listfile,id=id,filename=path,refresh=on|off****

创建一个授权对象来控制对网络服务的访问。

**filename** 参数是包含 JSON 格式的访问控制列表规则的文件的完全限定路径。

与 SASL 用户名匹配的一组示例规则可能如下所示：

{ "rules": \[ { "match": "fred", "policy": "allow", "format": "exact" }, { "match": "bob", "policy": "allow", "format": "exact" }, { "match": "danb", "policy": "deny", "format": "glob" }, { "match": "dan\*", "policy": "allow", "format": "exact" }, \], "policy": "deny" } 

-

-

当检查访问时，该对象将遍历所有规则，第一个匹配的规则将返回其 **policy** 值作为结果。 如果没有匹配的规则，则返回默认的 **policy** 值。

这些规则可以是精确的字符串匹配，也可以使用简单的 UNIX glob 模式匹配来允许使用通配符。

如果 **refresh** 设置为 true，则文件将被监视并在其内容更改时自动重新加载。

与 **authz-simple** 对象一样，要匹配的身份字符串的格式取决于网络服务，但通常是 TLS x509 专有名称或 SASL 用户名。

验证 SASL 用户名的示例授权对象如下所示：

\# qemu-system-x86\_64 \\ ... \\ -object authz-simple,id=auth0,filename=/etc/qemu/vnc-sasl.acl,refresh=on \\ ... 

-

-

****\-object authz-pam,id=id,service=string****

创建一个授权对象来控制对网络服务的访问。

**service** 参数提供用于授权的 PAM 服务的名称。 它要求存在一个文件 **/etc/pam.d/service** 来为 **account** 子系统提供配置。

验证 TLS x509 专有名称的示例授权对象如下所示：

\# qemu-system-x86\_64 \\ ... \\ -object authz-pam,id=auth0,service=qemu-vnc \\ ... 

-

-

然后会有一个 **/etc/pam.d/qemu-vnc** 对应的 PAM 配置文件包含：

account requisite pam\_listfile.so item=user sense=allow \\ file=/etc/qemu/vnc.allow 

-

-

最后， **/etc/qemu/vnc.allow** 文件将包含允许访问的 x509 专有名称列表

CN=laptop.example.com,O=Example Home,L=London,ST=London,C=GB 

-

-

****\-object iothread,id=id,poll-max-ns=poll-max-ns,poll-grow=poll-grow,poll-shrink=poll-shrink,aio-max-batch=aio-max-batch****

创建专用的事件循环线程该设备可以分配到。 这称为 IOThread。 默认情况下，设备模拟发生在 vCPU 线程或主事件循环线程中。 这可能成为可扩展性瓶颈。 IOThreads 允许设备仿真和 I/O 在其他主机 CPU 上运行。

**id** 参数是一个唯一的 ID，将用于从 **\-device ...,iothread=id** 引用此 IOThread。 多个设备可以分配给一个 IOThread。 请注意，并非所有设备都支持 **iothread** 参数。

**query-iothreads** QMP 命令列出 IOThreads 并报告它们的线程 ID，以便用户可以配置主机 CPU 固定/亲和性。

IOThreads 使用自适应轮询算法来减少事件循环延迟。 轮询算法不是进入阻塞系统调用来监视文件描述符然后支付在事件发生时被唤醒的成本，而是轮询算法在短时间内等待事件。 该算法的默认参数适用于许多情况，但可以根据工作负载和/或主机设备延迟的知识进行调整。

**poll-max-ns** 参数是忙于等待事件的最大纳秒数。 可以通过将此值设置为 0 来禁用轮询。

**poll-grow** 参数是用于在算法检测到由于轮询时间不够长而丢失事件时增加轮询时间的乘数。

**poll-shrink** 参数是用于在算法检测到轮询时间过长而没有遇到事件时减少轮询时间的除数。

**aio-max-batch** 参数是 AIO 引擎一个批次的最大请求数，0 表示引擎将使用其默认值。

可以在运行时使用 **qom-set** 命令修改 IOThread 参数（其中 **iothread1** 是 IOThread 的 **id**):

(qemu) qom-set /objects/iothread1 poll-max-ns 100000 

-

-

-

-

在图形仿真期间，您可以使用特殊的组合键更改模式。 默认键映射如下所示，但如果使用 **\-alt-grab** 则修饰符是 Ctrl-Alt-Shift (而不是 Ctrl-Alt) ，如果使用 **\-ctrl-grab** 则修饰符是右 Ctrl 键 (而不是 Ctrl-Alt):

**Ctrl-Alt-f**

切换全屏

**Ctrl-Alt-+**

放大屏幕

**Ctrl-Alt--**

缩小屏幕

**Ctrl-Alt-u**

缩小屏幕

**Ctrl-Alt-n**

切换到虚拟控制台 'n' 。 标准控制台映射是：

**_1_**

目标系统显示器

**_2_**

显示器

**_3_**

串行端口

-

**Ctrl-Alt**

切换鼠标和键盘抓取。

-

在虚拟控制台中，您可以使用 Ctrl-Up, Ctrl-Down, Ctrl-PageUp 和 Ctrl-PageDown t来移动积压日志。

在仿真过程中，如果您使用字符后端多路复用器（如果您使用 **\-nographic** ，这是默认设置），则可以通过转义序列使用多个命令。 这些键序列都以转义字符开头，默认为 Ctrl-a ，但可以使用 **\-echr** 更改。 下面的列表假定您使用的是默认值。

**Ctrl-a h**

打印此帮助

**Ctrl-a x**

退出模拟器

**Ctrl-a s**

将磁盘数据保存回文件（如果 -snapshot)

**Ctrl-a t**

切换控制台时间戳

**Ctrl-a b**

发送中断（Linux 中的魔法 sysrq）

**Ctrl-a c**

在连接到多路复用器的前端之间旋转（通常在监视器和控制台之间切换）

**Ctrl-a Ctrl-a**

将转义字符发送到前端

-

[笔记](#__u7B14___u8BB0_)
=======================

除了使用模拟存储设备的普通文件图像外，QEMU 还可以使用网络资源，例如 iSCSI 设备。 这些是使用特殊的 URL 语法指定的。

****iSCSI****

iSCSI 支持允许 QEMU 直接访问 iSCSI 资源并用作来宾存储的映像。 支持磁盘和 cdrom 映像。

指定 iSCSI LUN 的语法是 "iscsi://<target-ip>\[:<port>\]/<target-iqn>/<lun>"

默认情况下 qemu 将使用 iSCSI 启动器名称 'iqn.2008-11.org.linux-kvm\[:<name>\]' 但也可以从命令行或配置文件中设置。

从 QEMU 2.4 版本开始，可以指定 iSCSI 请求超时来检测停滞的请求并强制重新建立会话。 超时以秒为单位指定。默认值为 0，表示没有超时。 此功能需要 Libiscsi 1.15.0 或更高版本。

示例（无身份验证）：

qemu-system-x86\_64 -iscsi initiator-name=iqn.2001-04.com.example:my-initiator \\ -cdrom iscsi://192.0.2.1/iqn.2001-04.com.example/2 \\ -drive file=iscsi://192.0.2.1/iqn.2001-04.com.example/1 

-

-

示例（通过 URL 的 CHAP 用户名/密码）：

qemu-system-x86\_64 -drive file=iscsi:_//user%password@192.0.2.1/iqn.2001-04.com.example/1_ 

-

-

示例（CHAP 用户名/密码通过环境变量）：

LIBISCSI\_CHAP\_USERNAME="user" \\ LIBISCSI\_CHAP\_PASSWORD="password" \\ qemu-system-x86\_64 -drive file=iscsi://192.0.2.1/iqn.2001-04.com.example/1 

-

-

****NBD****

QEMU 支持使用 TCP 协议和 Unix 的 NBD（网络块设备）域套接字。 使用 TCP，默认端口为 10809。

使用 TCP 指定 NBD 设备的语法，首选 URI 格式： "nbd://<server-ip>\[:<port>\]/\[<export>\]"

使用 Unix 域套接字的 NBD 设备；还记得吗 '?' i是一个 shell glob 字符，可能需要引用： "nbd+unix:///\[<export>\]?socket=<domain-socket>"

也可识别的旧语法： "nbd:<server-ip>:<port>\[:exportname=<export>\]"

使用 Unix 域套接字指定 NBD 设备的语法 "nbd:unix:<domain-socket>\[:exportname=<export>\]"

TCP 示例

qemu-system-x86\_64 --drive file=nbd:192.0.2.1:30000 

-

-

Unix 域套接字示例

qemu-system-x86\_64 --drive file=nbd:unix:/tmp/nbd-socket 

-

-

****SSH****

QEMU 支持对远程磁盘的 SSH（安全外壳）访问。

示例：

qemu-system-x86\_64 -drive file=ssh:_//user@host/path/to/disk.img_ qemu-system-x86\_64 -drive file.driver=ssh,file.user=user,file.host=host,file.port=22,file.path=/path/to/disk.img 

-

-

当前身份验证必须使用 ssh-agent 完成。 将来可能会支持其他身份验证方法。

****GlusterFS****

GlusterFS 是一个用户空间分布式文件系统。 QEMU 支持使用 GlusterFS 卷来托管使用 TCP、Unix 域套接字和 RDMA 传输协议的 VM 磁盘映像。

在 GlusterFS 卷上指定 VM 磁盘映像的语法是

URI: gluster\[+type\]://\[host\[:port\]\]/volume/path\[?socket=...\]\[,debug=N\]\[,logfile=...\] JSON: 'json:{"driver":"qcow2","file":{"driver":"gluster","volume":"testvol","path":"a.img","debug":N,"logfile":"...", "server":\[{"type":"tcp","host":"...","port":"..."}, {"type":"unix","socket":"..."}\]}}' 

-

-

Example

URI: qemu-system-x86\_64 --drive file=gluster://192.0.2.1/testvol/a.img, file.debug=9,file.logfile=/var/log/qemu-gluster.log JSON: qemu-system-x86\_64 'json:{"driver":"qcow2", "file":{"driver":"gluster", "volume":"testvol","path":"a.img", "debug":9,"logfile":"/var/log/qemu-gluster.log", "server":\[{"type":"tcp","host":"1.2.3.4","port":24007}, {"type":"unix","socket":"/var/run/glusterd.socket"}\]}}' qemu-system-x86\_64 -drive driver=qcow2,file.driver=gluster,file.volume=testvol,file.path=/path/a.img, file.debug=9,file.logfile=/var/log/qemu-gluster.log, file.server.0.type=tcp,file.server.0.host=1.2.3.4,file.server.0.port=24007, file.server.1.type=unix,file.server.1.socket=/var/run/glusterd.socket 

-

-

另见 _http://www.gluster.org_ 。

****HTTP/HTTPS/FTP/FTPS****

QEMU 支持对通过 http(s) 和 ftp(s) 访问的文件进行只读访问。

使用单个文件名的语法：

<protocol>://\[<username>\[:<password>\]@\]<host>/<path> 

-

-

其中：

****protocol****

'http', 'https', 'ftp', or 'ftps'.

****username****

可选用户名，用于向远程服务器进行身份验证。

****password****

用于对远程服务器进行身份验证的可选密码。

****host****

远程服务器的主机地址。

****path****

远程服务器上的路径，包括任何查询字符串。

-

还支持以下选项：

****url****

将选项显式传递给驱动程序时的完整 URL。

****readahead****

每次向远程服务器发出范围请求时要预读的数据量。 该值可以选择具有后缀 'T', 'G', 'M', 'K', 'k' 或 'b' 。 如果它没有后缀，它将被假定为以字节为单位。 该值必须是 512 字节的倍数。 它默认为 256k。

****sslverify****

是否验证远程服务器' 它的值可以是 'on' 或 'off' 。 它默认为 'on'。

****cookie****

与每个传出请求一起发送此 cookie（它也可以是由 ';') 分隔的 cookie 列表）。 仅在使用支持 cookie 的 HTTP 等协议时才支持，否则忽略。

****timeout****

以秒为单位设置 CURL 连接的超时时间。 此超时是 CURL 等待远程服务器响应以获取要下载的图像大小的时间。 如果未设置，则使用 5 秒的默认超时。

-

请注意，当显式将选项传递给 qemu 时， **driver** 是 <protocol> 的值。

示例：从远程 Fedora 20 live ISO 映像引导

qemu-system-x86\_64 --drive media=cdrom,file=https://archives.fedoraproject.org/pub/archive/fedora/linux/releases/20/Live/x86\_64/Fedora-Live-Desktop-x86\_64-20-1.iso,readonly qemu-system-x86\_64 --drive media=cdrom,file.driver=http,file.url=http://archives.fedoraproject.org/pub/fedora/linux/releases/20/Live/x86\_64/Fedora-Live-Desktop-x86\_64-20-1.iso,readonly 

-

-

示例：从远程 Fedora 20 云映像启动，使用本地覆盖进行写入、读取时复制和 64k 预读

qemu-img create -f qcow2 -o backing\_file='json:{"file.driver":"http",, "file.url":"_http://archives.fedoraproject.org/pub/archive/fedora/linux/releases/20/Images/x86\_64/Fedora-x86\_64-20-20131211.1-sda.qcow2_",, "file.readahead":"64k"}' /tmp/Fedora-x86\_64-20-20131211.1-sda.qcow2 qemu-system-x86\_64 -drive file=/tmp/Fedora-x86\_64-20-20131211.1-sda.qcow2,copy-on-read=on 

-

-

示例：从存储在 VMware vSphere 服务器上的映像引导，该映像具有自签名证书，使用本地覆盖进行写入、64k 预读和 10 秒超时。

qemu-img create -f qcow2 -o backing\_file='json:{"file.driver":"https",, "file.url":"_https://user:password@vsphere.example.com/folder/test/test-flat.vmdk?dcPath=Datacenter&dsName=datastore1_",, "file.sslverify":"off",, "file.readahead":"64k",, "file.timeout":10}' /tmp/test.qcow2 qemu-system-x86\_64 -drive file=/tmp/test.qcow2 

-

-

-

[参见](#__u53C2___u89C1_)
=======================

QEMU 的 HTML 文档以获取更精确的信息和 Linux 用户模式仿真器调用。

[作者](#__u4F5C___u8005_)
=======================

Fabrice Bellard

[版权](#__u7248___u6743_)
=======================

2021, QEMU 项目开发者

June 7, 2022

6.2.0