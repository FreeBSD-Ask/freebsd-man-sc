  GPIOCTL(8)  

GPIOCTL(8)

FreeBSD System Manager's Manual

GPIOCTL(8)

[名称](#__u540D___u79F0_)
=======================

`gpioctl` —

GPIO 控制实用程序

[概要](#__u6982___u8981_)
=======================

`gpioctl` \[`-f` ctldev\] `-l` \[`-v`\] `gpioctl` \[`-f` ctldev\] \[`-pN`\] `-t` pin `gpioctl` \[`-f` ctldev\] \[`-pN`\] `-c` pin flag \[flag ...\] `gpioctl` \[`-f` ctldev\] \[`-pN`\] `-n` pin pin-name `gpioctl` \[`-f` ctldev\] \[`-pN`\] pin \[0|1\]

[描述](#__u63CF___u8FF0_)
=======================

`gpioctl` 实用程序可用于管理来自用户空间的 GPIO 引脚并列出可用引脚。

pin 参数可以是 pin-number 或 pin-name 。 如果它是一个数字并且一个 pin 以这个数字作为它的名称并且您没有使用 `-N` 或 `-p` , 则 `gpioctl` 退出。

选项如下：

[`-c`](#c) pin flag \[flag ...\]

通过设置提供的标志来配置 pin。当前定义了以下标志：

[`IN`](#IN)

输入引脚

[`OUT`](#OUT)

输出引脚

[`OD`](#OD)

Open drain pin

[`PP`](#PP)

Push pull pin

[`TS`](#TS)

Tristate pin

[`PU`](#PU)

Pull-up pin

[`PD`](#PD)

Pull-down pin

[`II`](#II)

Inverted input pin

[`IO`](#IO)

Inverted output pin

[`-f`](#f) ctldev

要使用的 GPIO 控制器设备 如果未指定，默认为 /dev/gpioc0

[`-l`](#l)

列出可用的引脚

[`-n`](#n) pin pin-name

设置用于描述引脚的名称

[`-t`](#t) pin

提供引脚的切换值

[`-v`](#v)

详细：为每个列出的引脚打印当前配置

[`-p`](#p)

强制将 pin 解释为 pin 号

[`-N`](#N)

强制将 pin 解释为 pin 名称

[实例](#__u5B9E___u4F8B_)
=======================

*   列出设备 /dev/gpioc0 定义的 GPIO 控制器上可用的引脚
    
    gpioctl -f /dev/gpioc0 -l
    
*   将引脚 12 的值设置为 1
    
    gpioctl -f /dev/gpioc0 12 1
    
*   将引脚 12 配置为输入引脚
    
    gpioctl -f /dev/gpioc0 -c 12 IN
    
*   设置引脚 12 的名称进行测试
    
    gpioctl -f /dev/gpioc0 -n 12 test
    
*   切换名为 test 的引脚的值
    
    gpioctl -f /dev/gpioc0 -t test
    
*   切换引脚编号 12 的值，即使另一个引脚的名称为 12
    
    gpioctl -f /dev/gpioc0 -pt 12
    

[参见](#__u53C2___u89C1_)
=======================

gpio(4), gpioiic(4), gpioled(4)

[历史](#__u5386___u53F2_)
=======================

`gpioctl` 实用程序出现在 FreeBSD 9.0 中。

[作者](#__u4F5C___u8005_)
=======================

`gpioctl` 实用程序和本手册页由 Oleksandr Tymoshenko <[gonzo@freebsd.org](mailto:gonzo@freebsd.org)\> 编写。

June 6, 2018

FreeBSD 13.1-RELEASE