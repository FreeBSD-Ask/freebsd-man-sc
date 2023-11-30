  MOUSED(8)  

MOUSED(8)

FreeBSD System Manager's Manual

MOUSED(8)

[名称](#__u540D___u79F0_)
=======================

`moused` —

将鼠标数据传递给控制台驱动程序

[概要](#__u6982___u8981_)
=======================

`moused` \[`-DPRacdfs`\] \[`-I` file\] \[`-F` rate\] \[`-r` resolution\] \[`-S` baudrate\] \[`-VH` \[`-U` distance `-L` distance\]\] \[`-A` exp\[,offset\]\] \[`-a` X\[,Y\]\] \[`-C` threshold\] \[`-m` N=M\] \[`-w` N\] \[`-z` target\] \[`-t` mousetype\] \[`-l` level\] \[`-3` \[`-E` timeout\]\] \[`-T` distance\[,time\[,after\]\]\] `-p` port

`moused` \[`-Pd`\] `-p` port `-i` info

[描述](#__u63CF___u8FF0_)
=======================

`moused` 实用程序和控制台驱动程序协同工作以支持文本控制台和用户程序中的鼠标操作。 它们虚拟化鼠标并为用户程序提供标准格式的鼠标数据（参见 sysmouse(4) ）。

鼠标守护程序侦听鼠标数据的指定端口，对其进行解释，然后通过 ioctls 将其传递给控制台驱动程序。 鼠标守护程序报告平移移动、按钮按下/释放事件以及滚轮或滚轮的移动（如果可用）。 滚子/车轮运动报告为 “Z” 轴运动。

如果通过 vidcontrol(1) 在虚拟控制台中启用了鼠标指针，控制台驱动程序将在屏幕上显示鼠标指针并提供剪切和粘贴功能。 如果用户程序打开了 sysmouse(4) ，控制台驱动程序也会将鼠标数据传递给设备，以便用户程序可以看到它。

如果鼠标守护程序收到信号 `SIGHUP` ，它将重新打开鼠标端口并重新初始化自己。 如果在系统挂起时连接/分离鼠标，则很有用。

如果鼠标守护进程收到信号 `SIGUSR1` ，它将停止传递鼠标事件。 再次发送信号 `SIGUSR1` 将恢复传递鼠标事件。 如果您在笔记本电脑上的打字因意外触摸鼠标垫而中断，这很有用。

可以使用以下选项：

[`-3`](#3)

模拟 2 键鼠标的第三个（中间）按钮。 它是通过同时按下左右物理按钮来模拟的。

[`-C`](#C) threshold

将双击速度设置为按钮单击之间的最大间隔（毫秒）。 如果没有此选项，将假定默认值 500 毫秒。 此选项仅对文本模式控制台中的剪切和粘贴操作有效。 通过 sysmouse(4) 读取鼠标数据的用户程序不会受到影响。

[`-D`](#D)

降低串行端口上的 DTR。 此选项仅在协议类型选择为 mousesystems 时有效。 可能需要删除 DTR 线才能使 3 键鼠标在 mousesystems 模式下运行。

[`-E`](#E) timeout

当启用第三个按钮模拟时（见上文）， `moused`-
实用程序最多等待 timeout 毫秒，然后再决定是否同时按下两个按钮。 默认超时为 100 毫秒。

[`-F`](#F) rate

如果支持，设置设备的报告速率（报告/秒）。

[`-L`](#L) distance

当启用 “Virtual Scrolling” 时， `-L` 选项可用于设置在生成滚动事件之前鼠标必须移动的 distance （以像素为单位）。 这有效地控制了滚动速度。 默认 distance 为 2 像素。

[`-H`](#H)

启用 “Horizontal Virtual Scrolling” 。 设置此选项后，按住鼠标中键将导致运动被解释为水平滚动。 使用 `-U` 选项设置在激活滚动模式之前鼠标必须移动的距离，使用 `-L` 选项设置滚动速度。 此选项可以与 `-V` 选项一起使用，也可以不与 `-V` 选项一起使用。

[`-I`](#I) file

在指定文件中写入 `moused` 实用程序的进程 ID。 如果没有这个选项，进程 ID 将存储在 /var/run/moused.pid 中。

[`-P`](#P)

识别串行鼠标时不要启动即插即用 COM 设备枚举过程。 如果此选项与 `-i` 选项一起提供，则 `moused` 实用程序将无法打印串行鼠标的有用信息。

[`-R`](#R)

降低串行端口上的 RTS。 仅当以下 `-t` 选项选择 mousesystems 作为协议类型时，此选项才有效。 它通常与上面的 `-D` 选项一起使用。 可能需要同时删除 RTS 和 DTR 线才能使 3 键鼠标在 mousesystems 模式下运行。

[`-S`](#S) baudrate

选择串行端口的波特率（1200 到 9600）。 并非所有串行鼠标都支持此选项。

[`-T`](#T) distance\[,time\[,after\]\]

终止漂移。 如果鼠标不移动时鼠标指针缓慢移动，请使用此选项。 在 time 毫秒（默认 500）内移动到 distance （例如 4）像素 (X+Y) 的移动将被忽略，除非在自上次真正的鼠标移动 after 的毫秒（默认 4000）之后。

[`-V`](#V)

启用 “Virtual Scrolling” 。 设置此选项后，按住鼠标中键将导致运动被解释为滚动。 使用 `-U` 选项设置在激活滚动模式之前鼠标必须移动的距离，使用 `-L` 选项设置滚动速度。

[`-U`](#U) distance

当启用 “Virtual Scrolling” 时， `-U` 选项可用于设置鼠标在滚动模式激活之前必须移动的 distance （以像素为单位）。 默认 distance 为 3 像素。

[`-A`](#A) exp\[,offset\]

对鼠标移动应用指数（动态）加速度：移动鼠标的速度越快，它的加速度就越大。 这意味着鼠标的小移动不会加速，因此它们仍然非常准确，而更快的移动将推动指针快速穿过屏幕。

exp 值指定指数，它基本上是加速度的量。 有用的值在 1.1 到 2.0 的范围内，但这取决于您的鼠标硬件和您的个人喜好。 值 1.0 表示没有指数加速。 值 2.0 表示平方加速度（即，如果您以两倍的速度移动鼠标，则指针在屏幕上的移动速度将是四倍）。 超过 2.0 的值是可能的，但不推荐。 一个好的开始值可能是 1.5。

可选的 offset 值指定加速开始的距离。 默认值为 1.0，这意味着将加速度应用于大于一个单位的运动。 如果您指定一个较大的值，则加速开始需要更多的速度，即小而准确的运动的速度范围更广。 通常默认值就足够了，但如果您对行为不满意，请尝试使用 2.0 的值。

请注意， `-A` 选项与 X 服务器自身的加速交互不良，无论如何它都不能很好地工作。 因此，如有必要，建议将其关闭： “xset m 1” 。

[`-a`](#a) X\[,Y\]

加速或减速鼠标输入。 这只是线性加速度。 小于 1.0 的值会减慢移动速度，大于 1.0 的值会加快速度。 仅指定一个值会设置两个轴的加速度。

您可以同时使用 `-a` 和 `-A` 选项以获得线性和指数加速的组合效果。

[`-c`](#c)

一些鼠标报告中间按钮按下事件，就像按下左右按钮一样。 此选项处理此问题。

[`-d`](#d)

启用调试消息。

[`-f`](#f)

不要成为守护进程，而是作为前台进程运行。 对测试和调试很有用。

[`-i`](#i) info

打印指定信息并退出。 可用的信息有：

port

端口（设备文件）名称，即 /dev/cuau0 和 /dev/psm0 。

if

接口类型：串行、总线、输入端口或 ps/2。

type

协议类型。 如果驱动程序支持 sysmouse 数据格式标准，则它是下面 `-t` 选项或 sysmouse 下列出的类型之一。

model

鼠标模型。 `moused` 实用程序可能并不总是能够识别模型。

all

以上所有项目。 在一行中按此顺序打印端口、接口、类型和型号。

如果 `moused` 实用程序无法确定请求的信息，则会打印 “`unknown`” 或 “`generic`” 。

[`-l`](#l) level

指定 `moused` 应该在哪个级别操作鼠标驱动程序。 有关这方面的更多信息，请参阅 psm(4) 中的 [Operation Levels](#Operation_Levels) 。

[`-m`](#m) N=M

将物理按钮 M 分配给逻辑按钮 N 。您可以指定任意数量的此选项实例。 一个以上的物理按钮可以同时分配给一个逻辑按钮。 在这种情况下，如果任一分配的物理按钮被按住，则逻辑按钮将被按下。 不要在 ‘`=`’ 周围放置空格。

[`-p`](#p) port

使用 port 与鼠标通信。

[`-r`](#r) resolution

设置设备的分辨率；以每英寸点数为单位， low, medium-low, medium-high 或 high 。 并非所有设备都支持此选项。

[`-s`](#s)

为串行线选择波特率 9600。 并非所有串行鼠标都支持此选项。

[`-t`](#t) type

指定连接到端口的鼠标的协议类型。 您可以明确指定下面列出的类型，或使用 auto 让 `moused` 实用程序自动为给定鼠标选择适当的协议。 如果您在命令行中完全省略此选项，则假定为 `-t` auto 。 在正常情况下，只有当 `moused` 实用程序无法自动检测协议时，才需要使用此选项（请参阅 [配置鼠标守护程序](#__u914D___u7F6E___u9F20___u6807___u5B88___u62A4___u7A0B___u5E8F_) )。

请注意，如果使用此选项指定协议类型，则隐含上面的 `-P` 选项，并且将禁用即插即用 COM 设备枚举过程。

另请注意，如果您的鼠标连接到 PS/2 鼠标端口，则无论鼠标的品牌和型号如何，都应始终选择 auto 或 ps/2 。 同样，如果您的鼠标连接到总线鼠标端口，请选择 auto 或 busmouse 。 串行鼠标协议不适用于这些鼠标。

对于 USB 鼠标，协议必须是 auto 。 没有其他协议适用于 USB 鼠标。

下面列出了此选项的有效类型。

对于串行鼠标：

microsoft

Microsoft 串行鼠标协议。 大多数 2 键串行鼠标使用此协议。

intellimouse

Microsoft IntelliMouse 协议。 Genius NetMouse, ASCII Mie Mouse, Logitech MouseMan+ 和 FirstMouse+ 也使用此协议。 其他带有滚轮/滚轮的鼠标可能与此协议兼容。

mousesystems

MouseSystems 5 字节协议。 三键鼠标可以使用此协议。

mmseries

MM 系列鼠标协议。

logitech

罗技鼠标协议。 请注意，这适用于旧的 Logitech 型号。 应为较新的模型指定 mouseman 或 intellimouse 。

mouseman

罗技 MouseMan 和 TrackMan 协议。 某些 3 键鼠标可能与此协议兼容。 注意 MouseMan+ 和 FirstMouse+ 使用 intellimouse 协议而不是这个协议。

glidepoint

ALPS GlidePoint 协议。

thinkingmouse

Kensington ThinkingMouse 协议。

mmhitab

日立平板电脑协议。

x10mouseremote

X10 鼠标遥控器。

kidspad

Genius Kidspad 和 Easypad 协议。

versapad

Interlink VersaPad 协议。

gtco\_digipad

GTCO Digipad 协议。

对于总线和 InPort 鼠标：

busmouse

这是总线和 InPort 鼠标唯一可用的协议类型，应为任何总线鼠标和 InPort 鼠标指定，无论品牌如何。

对于 PS/2 鼠标：

ps/2

这是 PS/2 鼠标唯一可用的协议类型，应该为任何 PS/2 鼠标指定，无论品牌如何。

对于 USB 鼠标， auto-
是唯一可用于 USB 鼠标的协议类型，应为任何 USB 鼠标指定，无论品牌如何。

[`-w`](#w) N

使实体按键 N 充当滚轮模式按键。 按下此按钮时，X 和 Y 轴运动报告为零，Y 轴运动映射到 Z 轴。 您可以通过下面的 `-z` 选项进一步将 Z 轴运动映射到虚拟按钮。

[`-z`](#z) target

将 Z 轴（滚轮/滚轮）运动映射到另一个轴或虚拟按钮。有效的 target 可能是：

x

y

当检测到 Z 轴移动时，将报告 X 或 Y 轴移动。

N

当检测到负和正 Z 轴运动时，分别报告虚拟按钮 N 和 N+1 的向下事件。 不需要有物理按钮 N 和 N+1 。 请注意，在完成从 Z 轴移动到虚拟按钮的映射之后，执行到逻辑按钮的映射。

N1 N2

当检测到负和正 Z 轴运动时，分别报告虚拟按钮 N1 和 N2 的向下事件。

N1 N2 N3 N4

这对于具有两个轮子（其中第二个轮子用于产生水平滚动动作）的鼠标，以及具有可以检测用户施加的水平力的旋钮或杆的鼠标很有用。

第二个轮子的运动将映射到按钮 N3 （负方向）和 N4 （正方向）。 如果此鼠标中确实存在 N3 和 N4 按钮，则不会检测到它们的动作。

请注意，水平运动或第二个滚轮/滚轮运动可能并不总是被检测到，因为似乎没有关于如何编码的公认标准。

另请注意，有些老鼠认为左是负水平方向；其他人可能不这么认为。 此外，有些鼠标的两个轮子都是垂直安装的，第二个垂直轮的方向与第一个不匹配。

[配置鼠标守护程序](#__u914D___u7F6E___u9F20___u6807___u5B88___u62A4___u7A0B___u5E8F_)
-----------------------------------------------------------------------------

您需要知道的第一件事是您要使用的鼠标的接口类型。 可以通过查看鼠标的连接器来确定。 串行鼠标有一个 D-Sub 母头 9 或 25 针连接器。 总线和 InPort 鼠标具有 D-Sub 公 9 针连接器或圆形 DIN 9 针连接器。 PS/2 鼠标配备一个小型圆形 DIN 6 针连接器。 一些鼠标带有适配器，可以将连接器转换为另一个。 如果您要使用这样的适配器，请记住鼠标/适配器对最末端的连接器很重要。 USB 鼠标有一个扁平的矩形连接器。

接下来要决定的是用于给定接口的端口。 PS/2 鼠标始终位于 /dev/psm0 。 串行鼠标可以连接到多个串行端口。 许多人经常将第一个内置串行端口 /dev/cuau0 分配给鼠标。 您可以将多个 USB 鼠标连接到您的系统或 USB 集线器。 它们可作为 /dev/ums0, /dev/ums1 等访问。

您可能希望创建一个符号链接 /dev/mouse 指向鼠标连接的真实端口，以便稍后您可以轻松区分哪个是您的 “mouse” 端口。

下一步是猜测鼠标的适当协议类型。 `moused` 实用程序可能能够自动确定协议类型。 使用 `-i` 选项运行 `moused` 实用程序并查看它的内容。 如果该命令可以识别协议类型，则您无需进一步调查。 您可以在不明确指定协议类型的情况下启动守护程序（请参阅 [实例](#__u5B9E___u4F8B_) ) 。

如果鼠标驱动程序支持此协议类型，该命令可能会打印 sysmouse 。

请注意，由 `-i` 选项打印的 `type` 和 `model` 不一定与所讨论的指针设备的产品名称匹配，但它们可能会给出与之兼容的设备的名称。

如果 `-i` 选项没有产生任何结果，则需要通过 `-t` 选项为 `moused` 实用程序指定协议类型。 你必须做出猜测并尝试。有经验法则：

1.  无论鼠标的品牌如何，总线鼠标和 InPort 鼠标始终使用 busmouse 协议。
2.  无论鼠标的品牌如何，都应始终为 PS/2 鼠标指定 ps/2 协议。
3.  您必须为 USB 鼠标指定 auto 协议。
4.  大多数 2 键串行鼠标支持 microsoft 协议。
5.  3 键串行鼠标可以使用 mousesystems-
    协议。 如果没有，它可能与 microsoft 协议一起使用，尽管第三个（中间）按钮不起作用。 三键串行鼠标也可以使用 mouseman 协议，在该协议下，第三个按钮可以按预期工作。
6.  三键串行鼠标可能有一个小开关，可以在 “MS” 和 “PC” 或 “2” 和 “3” 之间进行选择。 “MS” 或 “2” 通常表示 microsoft 协议。 “PC” 或 “3” 将选择 mousesystems 协议。
7.  如果鼠标有滚轮或滚轮，它可能与 intellimouse 协议兼容。

要测试所选协议类型对于给定鼠标是否正确，请在当前虚拟控制台中启用鼠标指针，

`vidcontrol -m on`

在前台模式下启动鼠标守护程序，

`moused -f -p <selected_port> -t <selected_protocol>`

并查看鼠标指针是否根据鼠标移动正确移动。 然后通过单击左、右和中间按钮尝试剪切和粘贴功能。 键入 ^C 停止命令。

[多只老鼠](#__u591A___u53EA___u8001___u9F20_)
-----------------------------------------

可以同时运行与连接到系统的鼠标数量一样多的鼠标守护程序实例；每只鼠标一个实例。 如果用户想在路上使用笔记本电脑的内置 PS/2 指针设备，但在将系统连接到办公室的扩展坞时想使用串行鼠标，这将非常有用。 运行两个鼠标守护程序并告诉应用程序（例如 X Window System ）使用 sysmouse(4), 然后应用程序将始终从任一鼠标中看到鼠标数据。 当串行鼠标未连接时，相应的鼠标守护程序不会检测到任何移动或按钮状态变化，应用程序只会看到来自 PS/2 鼠标守护程序的鼠标数据。 相反，在此配置中，当两个鼠标都连接并同时移动时，鼠标指针将在屏幕上移动，就像鼠标的移动结合在一起一样。

[文件](#__u6587___u4EF6_)
=======================

/dev/consolectl

控制控制台的设备

/dev/psm%d

PS/2 鼠标驱动

/dev/sysmouse

虚拟鼠标驱动

/dev/ttyv%d

虚拟控制台

/dev/ums%d

USB鼠标驱动

/var/run/moused.pid

当前运行的 `moused` 实用程序的进程 ID

/var/run/MouseRemote

X10 MouseRemote 事件的 UNIX 域流套接字

[实例](#__u5B9E___u4F8B_)
=======================

`moused -p /dev/cuau0 -i type`

让 `moused` 实用程序在串行端口 /dev/cuau0 确定鼠标的协议类型。 如果成功，该命令将打印类型，否则将显示 “`unknown`” 。

moused -p /dev/cuau0 vidcontrol -m on 

如果 `moused` 实用程序能够在指定端口自动识别鼠标的协议类型，您可以在没有 `-t` 选项的情况下启动守护程序并在文本控制台中启用鼠标指针，如上。

moused -p /dev/mouse -t microsoft vidcontrol -m on 

在串行端口 /dev/mouse 上启动鼠标守护程序。 协议类型 microsoft 由 `-t` 选项明确指定。

`moused -p /dev/mouse -m 1=3 -m 3=1`

将物理按钮 3（右键）分配给逻辑按钮 1（逻辑左），将物理按钮 1（左）分配给逻辑按钮 3（逻辑右）。 这将有效地交换左右按钮。

`moused -p /dev/mouse -t intellimouse -z 4`

按下按钮 4 时报告负 Z 轴运动（即鼠标滚轮），按下按钮 5 时报告正 Z 轴运动（即鼠标滚轮）

如果你添加

`ALL ALL = NOPASSWD: /usr/bin/killall -USR1 moused`

到 /usr/local/etc/sudoers 文件，然后绑定

`killall -USR1 moused`

到窗口管理器中的一个键，如果您在键入时继续刷鼠标垫，则可以暂停笔记本电脑上的鼠标事件。

[参见](#__u53C2___u89C1_)
=======================

kill(1), vidcontrol(1), xset(1), keyboard(4), psm(4), screen(4), sysmouse(4), ums(4)

[标准](#__u6807___u51C6_)
=======================

`moused` 实用程序部分支持 “即插即用外部 COM 设备规范” ，以支持 PnP 串行鼠标。 但是，由于现有的串行鼠标对规范的符合程度不同，它并没有严格遵循标准的 1.0 版本。 即使采用这种不太严格的方法，它也可能并不总是为给定的串行鼠标确定适当的协议类型。

[历史](#__u5386___u53F2_)
=======================

`moused` 实用程序首次出现在 FreeBSD 2.2 中。

[作者](#__u4F5C___u8005_)
=======================

`moused` 实用程序由 Michael Smith <[msmith@FreeBSD.org](mailto:msmith@FreeBSD.org)\> 编写。 本手册页由 Mike Pritchard <[mpp@FreeBSD.org](mailto:mpp@FreeBSD.org)\> 编写。 该命令和手册页已由 Kazutaka Yokota <[yokota@FreeBSD.org](mailto:yokota@FreeBSD.org)\> 更新。

[注意事项](#__u6CE8___u610F___u4E8B___u9879_)
=========================================

如果用户 “taps” pad 的表面，许多pad设备的行为就好像按下了第一个（左）按钮。 相比之下，一些 ALPS GlidePoint 和 Interlink VersaPad 模型将敲击动作视为第四个按钮事件。 对这些模型使用选项 “`-m` `1=4`” 可以获得与其他焊盘设备相同的效果。

虚拟控制台中的剪切和粘贴功能假定鼠标上有三个按钮。 逻辑按钮 1（逻辑左侧）选择控制台中的文本区域并将其复制到剪切缓冲区。 逻辑按钮 3（逻辑右侧）扩展所选区域。 逻辑按钮 2（逻辑中间）将所选文本粘贴到文本光标位置。 如果鼠标只有两个按钮，则中间的“粘贴”按钮不可用。 要获得粘贴功能，使用 `-3` 选项模拟中间按钮，或者使用 `-m` 选项将物理右键分配给逻辑中间按钮: “`-m` `2=3`” 。

May 15, 2008

FreeBSD 13.1-RELEASE