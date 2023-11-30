  LOADER(8)  

LOADER(8)

FreeBSD System Manager's Manual

LOADER(8)

[名称](#__u540D___u79F0_)
=======================

`loader` —

内核引导的最后阶段

[描述](#__u63CF___u8FF0_)
=======================

名为 `loader` 的程序是 FreeBSD 内核引导过程的最后阶段。 在 IA32 (i386) 架构上，它是一个 BTX 客户端。 它静态链接到 libstand(3) ，通常位于目录 /boot 。

它提供了一种脚本语言，可用于自动执行任务、进行预配置或协助恢复过程。 这种脚本语言大致分为两个主要部分。 较小的一个是为临时用户直接使用而设计的一组命令，由于历史原因称为“内置命令”。 这些命令背后的主要驱动力是用户友好性。 更大的组件是 John Sadler 的基于 FICL 的 ANS 兼容 Forth 解释器。

在初始化期间， `loader` 将探测控制台并设置 console 变量，或者如果之前的引导阶段使用了串行控制台 (“`comconsole`”) ，则将其设置为串行控制台（“comconsole”）。 如果选择了多个控制台，它们将以空格分隔列出。 然后，探测设备，设置 currdev 和 loaddev ，并将 LINES 设置为 24。 接下来， FICL 被初始化，内置词被添加到它的词汇表中，如果 /boot/boot.4th 存在则处理它。 读取该文件时无法进行磁盘切换。 然后将与 FICL 一起使用的内部解释器 `loader` 设置为 `interpret` ，这是 FICL 的默认值。 之后，如果可用，将处理 /boot/loader.rc 。 这些文件通过 `include` 命令进行处理，该命令在处理它们之前将它们全部读入内存，从而使磁盘更改成为可能。

此时，如果尚未尝试 `autoboot` ，并且 autoboot\_delay 未设置为 “`NO`” （不区分大小写），则将尝试 `autoboot` 。 如果系统超过这一点，将设置 prompt 并且 `loader` 将进入交互模式。 请注意，从历史上看，即使 autoboot\_delay 设置为 “`0`” ，用户也可以在加载内核和模块时通过按控制台上的某个键来中断自动引导过程。 在某些情况下，这种行为可能是不可取的，以防止将 autoboot\_delay 设置为 “`-1`” ，在这种情况下， `loader` 仅在 `autoboot` 失败时才会进入交互模式。

[内置命令](#__u5185___u7F6E___u547D___u4EE4_)
=========================================

在 `loader` 中，内置命令从命令行获取参数。 目前，从脚本调用它们的唯一方法是在字符串上使用 evaluate 。 如果出现错误情况，就会产生异常，可以使用 ANS Forth 异常处理词进行拦截。 如果没有被拦截，则会显示错误消息并重置解释器的状态，清空堆栈并恢复解释模式。

可用的内置命令有：

[`autoboot`](#autoboot) \[seconds \[prompt\]\]

如果没有被用户中断，几秒钟后继续引导系统。 显示倒计时提示，警告用户系统即将启动，除非被按键中断。 如有必要，将首先加载内核。 默认为 10 秒。

[`bcachestat`](#bcachestat)

显示有关磁盘缓存使用情况的统计信息。仅用于调试。

[`boot`](#boot)

[`boot`](#boot_2) kernelname \[`...`\]

[`boot`](#boot_3) `-flag` `...`

立即开始引导系统，必要时加载内核。 任何标志或参数都会传递给内核，但如果提供了内核名称，它们必须在内核名称之前。

_警告：_ 如果加载了 loader.4th(8) ，则此内置函数的行为会发生变化。

[`echo`](#echo) \[`-n`\] \[⟨message⟩\]

在屏幕上显示文本。 除非指定了 `-n` ，否则将打印一个新行。

[`heap`](#heap)

显示内存使用统计信息。 仅用于调试目的。

[`help`](#help) \[topic \[subtopic\]\]

显示从 /boot/loader.help 读取的帮助消息。 专题 _index_ 将列出可用的主题。

[`include`](#include) file \[file ...\]

处理脚本文件。 反过来，每个文件都被完全读入内存，然后它的每一行都被传递给命令行解释器。 如果解释器返回任何错误，include 命令会立即中止，而不读取任何其他文件，并返回错误本身（请参阅 [ERRORS](#ERRORS) )。

[`load`](#load) \[`-t` type\] file `...`

加载内核、内核可加载模块 (kld)、磁盘映像或标记为 type 类型的不透明内容的文件。 内核和模块可以是 a.out 或 ELF 格式。 在要加载的文件名之后传递的任何参数都将作为参数传递给该文件。 使用 `md_image` 类型使内核创建一个文件支持的 md(4) 磁盘。 这对于从临时 rootfs 引导很有用。 目前，参数传递不适用于内核。

[`load_geli`](#load_geli) \[`-n` keyno\] prov file

为给定的提供者名称加载一个 geli(8) 加密密钥文件。 键索引可以通过 keyno 指定或默认为零。

[`ls`](#ls) \[`-l`\] \[path\]

显示目录 path 中的文件列表，如果未指定 path ，则显示根目录。 如果指定了 `-l` ，也会显示文件大小。

[`lsdev`](#lsdev) \[`-v`\]

列出可以从中加载模块的所有设备以及 ZFS 池。 如果指定了 `-v` ，则会打印更多详细信息，包括采用类似于 `zpool` `status` 输出格式的 ZFS 池信息。

[`lsmod`](#lsmod) \[`-v`\]

显示加载的模块。 如果指定了 `-v` ，则会显示更多详细信息。

[`lszfs`](#lszfs) filesystem

一个 ZFS 扩展命令，可用于探索池中的 ZFS 文件系统层次结构。 列出 filesystem 的直接子级。 文件系统层次结构植根于与池同名的文件系统。

[`more`](#more) file \[file ...\]

显示指定的文件，并在显示的每个 LINES 处暂停。

[`pnpscan`](#pnpscan) \[`-v`\]

扫描即插即用设备。 目前这不起作用。

[`read`](#read) \[`-t` seconds\] \[`-p` prompt\] \[variable\]

从终端读取一行输入，如果指定，将其存储在 variable 中。 可以用 `-t` 指定超时，尽管它会在第一个按键被按下时被取消。 也可以通过 `-p` 标志显示提示。

[`reboot`](#reboot)

立即重新启动系统。

[`set`](#set) variable

[`set`](#set_2) variable\=value

设置加载器的环境变量。

[`show`](#show) \[variable\]

显示指定变量的值，如果未指定 variable ，则显示所有变量及其值。

[`unload`](#unload)

从内存中删除所有模块。

[`unset`](#unset) variable

从环境中删除 variable 。

[`?`](#?)

列出可用的命令。

[内置环境变量](#__u5185___u7F6E___u73AF___u5883___u53D8___u91CF_)
-----------------------------------------------------------

`loader` 实际上有两种不同的 ‘environment’ 变量。 有 ANS Forth 的 _environmental queries_ ，以及内置函数使用的单独的环境变量空间，这些对于 Forth 单词是不直接可用的。 本节介绍的是后一种类型。

环境变量可以通过 `set` 和 `unset`-
内置函数设置和取消设置，并且可以通过使用 `show` 内置函数交互式检查它们的值。 也可以按照 [BUILTIN PARSER](#BUILTIN_PARSER) 中的描述访问它们的值。

请注意，这些环境变量在系统启动后不会被任何 shell 继承。

`loader` 会自动设置一些变量。 其他可能会影响 `loader` 或内核在引导时的行为。 一些选项可能需要一个值，而其他选项仅通过设置来定义行为。 下面描述了这两种类型的内置变量。

autoboot\_delay

启动前 `autoboot` 将等待的秒数。 如果未定义此变量， `autoboot` 将默认为 10 秒。

如果设置为 “`NO`” ，则在处理 /boot/loader.rc 后不会自动尝试 `autoboot` ，但会正常处理显式 `autoboot` ，默认为 10 秒延迟。

如果设置为 “`0`” ，则不会插入延迟，但用户仍然可以在加载内核和模块时通过按控制台上的某个键来中断 `autoboot` 过程并进入交互模式。

如果设置为 “`-1`” ，则不会插入延迟，并且只有在 `autoboot` 由于某种原因失败时 `loader` 才会进入交互模式。

boot\_askname

指示内核在引导内核时提示用户输入根设备的名称。

boot\_cdrom

指示内核尝试从 CD-ROM 挂载根文件系统。

boot\_ddb

指示内核在 DDB 调试器中启动，而不是在启动时进行初始化。

boot\_dfltroot

指示内核挂载静态编译的根文件系统。

boot\_gdb

默认情况下为内核调试器选择 gdb-remote 模式。

boot\_multicons

在启动早期启用内核中的多控制台支持。 在正在运行的系统中，控制台配置可以通过 conscontrol(8) 实用程序进行操作。

boot\_mute

当控制台静音时，所有内核控制台输出都会被抑制。 在正在运行的系统中，控制台静音的状态可以通过 conscontrol(8) 实用程序进行操作。

boot\_pause

在设备探测期间，在打印每一行后暂停。

boot\_serial

即使存在内部控制台，也强制使用串行控制台。

boot\_single

防止内核启动多用户启动；相反，当内核完成设备探测时将进入单用户模式。

boot\_verbose

设置此变量会导致内核在引导阶段打印额外的调试信息。

bootfile

可引导内核的分号分隔搜索路径列表。 默认为 “`kernel`” 。

comconsole\_speed

定义串行控制台的速度（仅限 i386 和 amd64）。 如果前一个引导阶段表明正在使用串行控制台，则此变量将初始化为控制台串行端口的当前速度。 否则设置为 9600，除非在编译 `loader` 时使用 BOOT\_COMCONSOLE\_SPEED 变量覆盖。 对 comconsole\_speed 变量的更改会立即生效。

comconsole\_port

定义用于访问控制台 UART 的基本 i/o 端口（仅限 i386 和 amd64）。 如果未设置该变量，则其假定值为 0x3F8，对应 PC 端口 COM1，除非在 `loader` 编译期间被 BOOT\_COMCONSOLE\_PORT 变量覆盖。 设置 comconsole\_port 变量会自动设置 hw.uart.console 环境变量，以向内核提供控制台位置的提示。 设置变量 comconsole\_port 后立即更改加载程序控制台。

comconsole\_pcidev

定义用作串行控制台 UART 的“简单通信”类 PCI 设备的位置（仅限 i386 和 amd64）。 变量的语法是 `'bus:device:function[:bar]'` ，其中所有成员必须是数字，可能带有 `0x` 前缀以指示十六进制值。 bar 成员是可选的，如果省略，则假定为 0x10。 条形必须解码 i/o 空间。 设置变量 comconsole\_pcidev 会自动将变量 comconsole\_port 设置为所选柱的底部，并提示 hw.uart.console 。 设置变量 comconsole\_pcidev 后立即更改加载程序控制台。

console

定义当前控制台或控制台。 可以指定多个控制台。 在这种情况下，第一个列出的控制台将成为用户态输出的默认控制台（例如来自 init(8) )。

currdev

选择要从中加载内核的默认设备。语法是：

``` `loader_device:` ```

或

``` `zfs:dataset:` ```

实例:

``` `disk0p2:` ```

``` `zfs:zroot/ROOT/default:` ```

dumpdev

为内核转储设置设备。 这可用于确保在处理来自 rc.conf(5) 的相应 dumpdev 指令之前配置设备，从而允许捕获在引导早期阶段发生的内核恐慌。

init\_chroot

请参见 init(8) 。

init\_exec

请参见 init(8) 。

init\_path

设置内核将尝试作为初始进程运行的二进制文件列表。 使用第一个匹配的二进制文件。 默认列表是 “`/sbin/init:/sbin/oinit:/sbin/init.bak:/rescue/init`” 。

init\_script

请参见 init(8)

init\_shell

请参见 init(8) 。

interpret

如果 Forth 的当前状态是解释，则值为 “`OK`” 。

LINES

定义屏幕上的行数，以供寻呼机使用

module\_path

设置目录列表，将搜索在加载命令中命名的模块或依赖项隐式需要的模块。 此变量的默认值为 “`/boot/kernel;/boot/modules`” 。

num\_ide\_disks

设置 IDE 磁盘的数量作为在引导时查找根磁盘时出现的一些问题的解决方法。 这已被弃用，取而代之的是 root\_disk\_unit 。

prompt

`loader` 提示的值。 默认为 “`${interpret}`” 。 如果未设置变量 prompt ，则默认提示为 ‘`>`’ 。

root\_disk\_unit

如果检测根磁盘的磁盘单元号的代码混淆了，例如混合了 SCSI 和 IDE 磁盘，或者 IDE 磁盘在序列中有间隙（例如，没有主从），可以通过设置这个来强制单元号多变的。

rootdev

默认情况下， currdev 的值用于设置内核启动时的根文件系统。 这可以通过显式设置 rootdev 来覆盖。

其他变量用于覆盖内核可调参数。 可以使用以下可调参数：

efi.rt.disabled

如果适用，请在内核中禁用 UEFI 运行时服务。 只有在 UEFI 环境中引导内核时，运行时服务才可用和使用。

hw.physmem

限制系统将使用的物理内存量。 默认情况下，大小以字节为单位，但也接受 `k`, `K`, `m`, `M`, `g` 和 `G` 后缀，分别表示千字节、兆字节和千兆字节。 无效的后缀将导致该变量被内核忽略。

hw.pci.host\_start\_mem, hw.acpi.host\_start\_mem

如果没有其他约束，这会限制内存起始地址。 默认值为 0x80000000，应设置为至少内存大小且不与其他资源冲突。 通常，只有没有 PCI 桥接器的系统需要设置此变量，因为 PCI 桥接器通常会限制内存起始地址（并且该变量仅在桥接器不限制此地址时使用）。

hw.pci.enable\_io\_modes

启用某些 BIOS 遗漏或设备驱动程序未正确启用的 PCI 资源。 可调值默认设置为 ON (1)，但这可能会导致某些外围设备出现问题。

kern.maxusers

设置一些静态分配的系统表的大小；有关如何为此可调参数选择适当值的说明，请参见 tuning(7) 。 设置后，此可调参数将替换内核编译时配置文件中声明的值。

kern.ipc.nmbclusters

设置要分配的 mbuf 簇的数量。 该值不能设置为低于编译内核时确定的默认值。

kern.ipc.nsfbufs

设置要分配的 sendfile(2) 缓冲区的数量。覆盖 `NSFBUFS` 。 并非所有架构都使用此类缓冲区；有关详细信息，请参阅 sendfile(2) 。

kern.maxswzone

限制用于保存交换元数据的 KVM 数量，这直接控制系统可以支持的最大交换量，每 1 MB 元数据大约需要 200 MB 交换空间。 此值以 KVA 空间的字节数指定。 如果未提供任何值，系统将分配足够的内存来处理相当于系统中存在的物理内存量的八倍的交换量。

请注意，交换元数据可能会被碎片化，这意味着系统可能会在达到理论限制之前耗尽空间。 因此，应注意配置的交换量不要超过理论最大值的大约一半。

交换元数据空间不足会使系统处于不可恢复的状态。 因此，仅当您需要为其他资源（例如缓冲区缓存或 kern.ipc.nmbclusters ）大幅扩展 KVM 预留时，才应更改此参数。 修改内核选项 `VM_SWZONE_SIZE_MAX` 。

kern.maxbcache

限制为缓冲区高速缓存保留的 KVM 数量，以字节为单位。 i386 上的默认最大值为 200MB，amd64 上为 400MB。 该参数用于防止缓冲区缓存在大内存机器配置中吃掉过多的 KVM。 如果您需要为其他资源（例如交换区或 kern.ipc.nmbclusters ）大幅扩展 KVM 预留，请仅使用此参数。 请注意，NBUF 参数将覆盖此限制。 修改 `VM_BCACHE_SIZE_MAX` 。

kern.msgbufsize

设置内核消息缓冲区的大小。 96KB 的默认限制通常就足够了，除非需要在检查缓冲区或将其转储到文件的机会之间收集大量跟踪数据。 覆盖内核选项 `MSGBUF_SIZE` 。

machdep.disable\_mtrrs

禁用 i686 MTRR（仅限 x86）。

net.inet.tcp.tcbhashsize

覆盖 `TCBHASHSIZE` 的编译时设置值或预设的默认值 512。 必须是 2 的幂。

twiddle\_divisor

限制加载内核和模块时显示的 ‘twiddle’ I/O 进度指示器的输出。 这在慢速串行控制台上很有用，在这些控制台上等待这些字符被写入所花费的时间可能会增加很多秒。 默认值为 1（全速）；值 2 旋转速度减半，依此类推。

vm.kmem\_size

设置内核内存的大小（字节）。 这会覆盖编译内核时确定的值。 修改 `VM_KMEM_SIZE` 。

vm.kmem\_size\_min

vm.kmem\_size\_max

设置将由内核自动分配的最小和最大（分别）内核内存量。 这些会覆盖内核编译时确定的值。 修改 `VM_KMEM_SIZE_MIN` 和 `VM_KMEM_SIZE_MAX` 。

[ZFS 特点](#ZFS___u7279___u70B9_)
-------------------------------

`loader` 支持以下格式来指定 ZFS 文件系统，只要 loader(8) 引用设备规范，就可以使用这些格式：

zfs:pool/filesystem:

其中 pool/filesystem 是 zfs(8) 中描述的 ZFS 文件系统名称。

如果 /etc/fstab 没有根文件系统的条目并且未设置 vfs.root.mountfrom ，但 currdev 引用 ZFS 文件系统，则 `loader` 将指示内核将该文件系统用作根文件系统。

[内置解析器](#__u5185___u7F6E___u89E3___u6790___u5668_)
--------------------------------------------------

当执行一个内置命令时，该行的其余部分被它作为参数，并由一个不用于常规 Forth 命令的特殊解析器处理。

此特殊解析器将以下规则应用于已解析的文本：

1.  所有反斜杠字符都经过预处理。
    *   \\b , \\f , \\r , \\n 和 \\t 在 C 中处理。
    *   \\s 转换为空格。
    *   \\v 被转换为 ASCII 11。
    *   \\z 只是被跳过。对诸如 “\\0xf\\z\\0xf” 之类的东西很有用。
    *   \\0xN 和 \\0xNN 替换为十六进制 N 或 NN。
    *   \\NNN 替换为八进制 NNN ASCII 字符。
    *   \\" , \\' 和 \\$ 将转义这些字符，防止它们在步骤 2 中接受特殊处理，如下所述。
    *   \\\\ 将替换为单个 \\ 。
    *   在任何其他情况下，反斜杠将被删除。
2.  出于剩余步骤的目的，非转义引号或双引号之间的每个字符串都将被视为一个单词。
3.  将任何 `$VARIABLE` 或 `${VARIABLE}` 替换为环境变量 VARIABLE 。
4.  空格分隔的参数被传递给被调用的内置命令。 空格也可以通过使用 \\\\ 。

此解析规则存在一个例外，并在 [BUILTINS AND FORTH](#BUILTINS_AND_FORTH) 。

[BUILTINS AND FORTH](#BUILTINS_AND_FORTH)
-----------------------------------------

所有内置词都是状态智能的直接词。如果被解释，它们的行为与前面描述的完全一样。 但是，如果它们被编译，它们会从堆栈而不是命令行中提取参数。

如果编译，内置词期望在执行时在堆栈上找到以下参数：

addrN lenN ... addr2 len2 addr1 len1 N

其中 addrX lenX 是字符串，它将组成将被解析为内置参数的命令行。 在内部，这些字符串从 1 到 N 连接在一起，每个字符串之间都有一个空格。

如果没有传递参数，则 _must_ 传递 0，即使内置函数不接受任何参数。

虽然这种行为有好处，但也有其权衡。 如果获取了内置函数的执行令牌（通过 `'` 或 `[']`), 然后传递给 `catch` 或 `execute`, 则内置行为将取决于系统状态

内建的行为将取决于系统状态 `catch` 或 `execute` 被处理的时间!

这对于想要或需要处理异常的程序来说尤其烦人。 在这种情况下，建议使用代理。例如：

`: (boot) boot;`

[FICL](#FICL)
=============

FICL 是一个用 C 语言编写的 Forth 解释器，以第四个虚拟机库的形式出现，可以被 C 函数调用，反之亦然。

在 `loader` 中，交互读取的每一行然后被馈送到 FICL ，FICL 可能会回调 `loader` 以执行内置字。 内置的 `include` 也将提供 FICL, 一次一行。

FICL 可用的词可分为四组。 ANS Forth 标准词、额外的 FICL 词、额外的 FreeBSD 词和内置命令；后者已被描述。 ANS 标准字列在 [STANDARDS](#STANDARDS) 部分。 属于其他两组的单词将在以下小节中描述。

[FICL 额外词](#FICL___u989D___u5916___u8BCD_)
------------------------------------------

[`.env`](#.env)

[`.ver`](#.ver)

[`-roll`](#-roll)

[`2constant`](#2constant)

[`>name`](#_name)

[`body>`](#body_)

[`compare`](#compare)

这是 STRING 字集的 `compare` 。

[`compile-only`](#compile-only)

[`endif`](#endif)

[`forget-wid`](#forget-wid)

[`parse-word`](#parse-word)

[`sliteral`](#sliteral)

这是 STRING 字集的 `sliteral` 。

[`wid-set-super`](#wid-set-super)

[`w@`](#w@)

[`w!`](#w!)

[`x.`](#x.)

[`empty`](#empty)

[`cell-`](#cell-)

[`-rot`](#-rot)

[FREEBSD 额外词](#FREEBSD___u989D___u5916___u8BCD_)
------------------------------------------------

[`$`](#$) (--)

先打印输入缓冲区的剩余部分，然后对其进行评估。

[`%`](#_) (--)

在 `catch` 异常保护下评估输入缓冲区的剩余部分。

[`.#`](#._)

像 . 但不输出尾随空格。

[`fclose`](#fclose) (fd --)

关闭文件。

[`fkey`](#fkey) (fd -- char)

从文件中读取单个字符。

[`fload`](#fload) (fd --)

处理文件 _fd_ 。

[`fopen`](#fopen) (addr len mode `--` fd)

打开一个文件。返回文件描述符，如果失败则返回 -1 。 mode 参数选择是否打开文件以进行读访问、写访问或两者兼而有之。 /boot/support.4th 中定义了常量 `O_RDONLY`, `O_WRONLY`, 和 `O_RDWR` ，分别表示只读、只写和读写访问。

[`fread`](#fread) (fd addr len -- len')

尝试将文件 _fd_ 中的 _len_ 个字节读入缓冲区 _addr_ 。 返回实际读取的字节数，如果出现错误或文件结束，则返回 -1。

[`heap?`](#heap?) (-- cells)

返回字典堆中剩余的空间，以单元格为单位。 这与动态内存分配字使用的堆无关。

[`inb`](#inb) (port -- char)

从端口读取一个字节。

[`key`](#key) (-- char)

从控制台读取单个字符。

[`key?`](#key?) (-- flag)

如果有一个字符可以从控制台读取，则返回 `true` 。

[`ms`](#ms) (u --)

等待 _u_ 微秒。

[`outb`](#outb) (port char --)

向端口写入一个字节。

[`seconds`](#seconds) (-- u)

返回自午夜以来的秒数。

[`tib>`](#tib_) (-- addr len)

将输入缓冲区的剩余部分作为堆栈上的字符串返回。

[`trace!`](#trace!) (flag --)

激活或停用跟踪。不适用于 `catch` 。

[FREEBSD 定义的环境查询](#FREEBSD___u5B9A___u4E49___u7684___u73AF___u5883___u67E5___u8BE2_)
------------------------------------------------------------------------------------

arch-i386

如果架构是 IA32，则为 `TRUE` 。

FreeBSD\_version

编译时的 FreeBSD 版本。

loader\_version

`loader` 版本。

[安全](#__u5B89___u5168_)
=======================

访问 `loader` 命令行提供了几种危及系统安全性的方法，包括但不限于:

*   从可移动存储引导，通过设置 currdev 或 loaddev 变量
*   执行选择的二进制文件，通过设置 init\_path 或 init\_script 变量
*   覆盖 ACPI DSDT将任意代码注入 ACPI 子系统

可以通过设置 password 或将 autoboot\_delay 设置为 -1 来防止对 `loader` 来防止对加载程序命令行的未经授权的访问。 有关详细信息，请参阅 loader.conf(5) 。 为了使其有效，还应配置固件（BIOS 或 UEFI）以防止从未经授权的设备启动。

[文件](#__u6587___u4EF6_)
=======================

/boot/loader

`loader` 本身。

/boot/boot.4th

附加 FICL 初始化。

/boot/defaults/loader.conf

/boot/loader.4th

额外的内置词。

/boot/loader.conf

/boot/loader.conf.local

`loader` 配置文件，如 loader.conf(5) 中所述。

/boot/loader.rc

`loader` 加载程序引导脚本。

/boot/loader.help

通过 `help` 加载。包含帮助消息。

/boot/support.4th

loader.conf-
处理的话。

/usr/share/examples/bootforth/

各种实例。

[实例](#__u5B9E___u4F8B_)
=======================

在单用户模式下引导：

`boot -s`

加载内核、启动屏幕，然后在五秒内自动引导。 请注意，必须在尝试任何其他 `load` 命令之前加载内核。

load kernel load splash\_bmp load -t splash\_image\_data /boot/chuckrulez.bmp autoboot 5 

设置根设备的磁盘单元为2，然后启动。 这在具有两个 IDE 磁盘的系统中是需要的，第二个 IDE 磁盘硬连线到 ada2 而不是 ada1。

set root\_disk\_unit=2 boot /boot/kernel/kernel 

设置用于从 ZFS 文件系统加载内核的默认设备：

set currdev=zfs:tank/ROOT/knowngood: 

[错误](#__u9519___u8BEF_)
=======================

`loader` 抛出以下值：

100

处理内置函数的任何类型的错误。

\-1

[`Abort`](#Abort) 执行。

\-2

[`Abort"`](#Abort_) 执行。

\-56

[`Quit`](#Quit) 执行。

\-256

解释文本。 -

\-257

需要更多文本才能成功——将在下次运行时完成。

\-258

[`Bye`](#Bye) 执行。

\-259

未指定错误。

[参见](#__u53C2___u89C1_)
=======================

libstand(3), loader.conf(5), tuning(7), boot(8), btxld(8)

[标准](#__u6807___u51C6_)
=======================

出于 ANS Forth 合规性的目的，loader 是具有环境限制的 ANS Forth 系统，提供

.(, :noname, ?do, parse, pick, roll, refill, to, value, \\, false, true, <>, 0<>, compile, , erase, nip, tuck

_and_ `marker`

from the Core Extensions word set, Providing the Exception Extensions word set, Providing the Locals Extensions word set, Providing the Memory-Allocation Extensions word set, Providing

.s, bye, forget, see, words, \[if\], \[else\]

_and_ `[then]`

from the Programming-Tools extension word set, Providing the Search-Order extensions word set.

[历史](#__u5386___u53F2_)
=======================

`loader` 首次出现在 FreeBSD 3.1

[作者](#__u4F5C___u8005_)
=======================

`loader` 由 Michael Smith ⟨msmith@FreeBSD.org⟩ 编写

FICL 由 John Sadler ⟨john\_sadler@alum.mit.edu⟩ 编写

[缺陷](#__u7F3A___u9677_)
=======================

`expect` 和 `accept` 词将从输入缓冲区而不是控制台读取。 后者将被修复，但前者不会。

October 2, 2020

FreeBSD 13.1-RELEASE