# gpioctl.8

`gpioctl` — GPIO 控制工具

## 名称

`gpioctl`

## 概要

`gpioctl [-f ctldev] -l [-v]`

`gpioctl [-f ctldev] [-pN] -t pin`

`gpioctl [-f ctldev] [-pN] -c pin flag [flag ...]`

`gpioctl [-f ctldev] [-pN] -n pin pin-name`

`gpioctl [-f ctldev] [-pN] pin [0|1]`

## 描述

`gpioctl` 工具可用于从用户态管理 GPIO 引脚，并列出可用引脚。

`pin` 参数可以是 `pin-number` 或 `pin-name`。如果它是一个数字，并且某个引脚以此数字作为名称，而你没有使用 `-N` 或 `-p`，则 `gpioctl` 会退出。

可用选项如下：

**`-c`** `pin` `flag` [flag ...] 通过设置所提供的标志来配置引脚。当前定义了以下标志：

**`IN`** 输入引脚

**`OUT`** 输出引脚

**`OD`** 开漏引脚

**`PP`** 推挽引脚

**`TS`** 三态引脚

**`PU`** 上拉引脚

**`PD`** 下拉引脚

**`II`** 反相输入引脚

**`IO`** 反相输出引脚

**`-f`** `ctldev` 要使用的 GPIO 控制器设备。如果未指定，默认为 **/dev/gpioc0**。

**`-l`** 列出可用引脚

**`-n`** `pin` `pin-name` 设置用于描述该引脚的名称

**`-t`** `pin` 切换所提供引脚的值

**`-v`** 详细模式：为列出的每个引脚打印当前配置

**`-p`** 强制将 `pin` 解释为引脚编号

**`-N`** 强制将 `pin` 解释为引脚名称

## 实例

- 列出由设备 **/dev/gpioc0** 定义的 GPIO 控制器上的可用引脚

```sh
gpioctl -f /dev/gpioc0 -l
```

- 将引脚 12 的值设置为 1

```sh
gpioctl -f /dev/gpioc0 12 1
```

- 将引脚 12 配置为输入引脚

```sh
gpioctl -f /dev/gpioc0 -c 12 IN
```

- 将引脚 12 的名称设置为 test

```sh
gpioctl -f /dev/gpioc0 -n 12 test
```

- 切换名为 test 的引脚的值

```sh
gpioctl -f /dev/gpioc0 -t test
```

- 切换引脚编号 12 的值，即使另一个引脚的名称为 12

```sh
gpioctl -f /dev/gpioc0 -pt 12
```

## 参见

[gpio(4)](../man4/gpio.4.md), [gpioiic(4)](../man4/gpioiic.4.md), [gpioled(4)](../man4/gpioled.4.md)

## 历史

`gpioctl` 工具出现于 FreeBSD 9.0。

## 作者

`gpioctl` 工具及本手册页由 Oleksandr Tymoshenko <gonzo@freebsd.org> 编写。
