  PWM(8)  

PWM(8)

FreeBSD System Manager's Manual

PWM(8)

[名称](#__u540D___u79F0_)
=======================

`pwm` —

配置 PWM（脉冲宽度调制）硬件

[概要](#__u6982___u8981_)
=======================

`pwm` \[`-f` device\] `-C` `pwm` \[`-f` device\] \[`-D` | `-E`\] \[`-p` period\] \[`-d` duty\]

[描述](#__u63CF___u8FF0_)
=======================

`pwm` 实用程序可用于配置 pwm 硬件。 `pwm` 使用 pwmc(4) 设备与硬件进行通信。一些 PWM 硬件支持单个控制器模块内的多个输出通道；每个 pwmc(4) 实例控制一个 PWM 通道。

pwmc(4) 设备被命名为 /dev/pwm/pwmcX.Y, 其中 X 是控制器单元号， Y 是该单元内的通道号。

选项如下：

[`-f`](#f) device

要操作的设备。 如果未指定，则使用 /dev/pwm/pwmc0.0 。 如果提供了非限定名称，则 /dev/pwm 会自动添加到前面。

[`-C`](#C)

显示 PWM 通道的配置。

[`-D`](#D)

禁用 PWM 通道。

[`-d`](#d) duty

配置 PWM 通道的占空比（以纳秒或百分比为单位）。 占空比是断言信号的 period 部分。

[`-E`](#E)

启用 PWM 通道。

[`-p`](#p) period

配置 PWM 通道的周期（以纳秒为单位）。

[实例](#__u5B9E___u4F8B_)
=======================

*   显示 PWM 通道的配置：
    
    pwm -f /dev/pwm/pwmc0.1 -C 
    
*   配置 50000 ns 周期和 25000 ns 占空比并启用通道：
    
    pwm -f pwmc1.1 -E -p 50000 -d 25000 
    
*   在 pwmc(4) 中配置为具有 backlight 的设备和通道上配置 50% 的占空比：
    
    pwm -f backlight -d 50% 
    

[参见](#__u53C2___u89C1_)
=======================

pwm(9), pwmbus(9)

[历史](#__u5386___u53F2_)
=======================

`pwm` 实用程序出现在 FreeBSD 13.0 中。

[作者](#__u4F5C___u8005_)
=======================

`pwm` 实用程序和本手册页由 Emmanuel Vadot <[manu@FreeBSD.org](mailto:manu@FreeBSD.org)\> 编写。

June 17, 2019

FreeBSD 13.1-RELEASE