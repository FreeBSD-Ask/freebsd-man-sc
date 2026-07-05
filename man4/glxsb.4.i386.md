# glxsb.4.i386

`glxsb` — Geode LX Security Block 加密加速器

## 名称

`glxsb`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device crypto
> device glxsb

或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
glxsb_load="YES"
```

## 描述

`glxsb` 驱动支持 Geode LX 系列处理器的安全块。Geode LX 是 AMD Geode 系列 x86 集成系统芯片的一员。

通过定期检查生成器是否有可用数据，`glxsb` 为 [random(4)](random.4.md) 驱动提供熵，供通用用途使用。

`glxsb` 还支持为 [crypto(4)](crypto.4.md) 加速 AES-128-CBC 操作。它还注册自身以加速其他 HMAC 算法，尽管这些算法没有硬件加速。这只是为了使 `glxsb` 能与 [ipsec(4)](ipsec.4.md) 协同工作。

## 注意事项

如果 AES 密钥长度不等于 128 位，[crypto(9)](../man9/crypto.9.md) 框架将无法在设备上打开加密会话。这会阻止在 AES 密钥长度不等于 128 位时使用 `glxsb` 设备驱动。

## 参见

[crypto(4)](crypto.4.md), [intro(4)](intro.4.md), [ipsec(4)](ipsec.4.md), [pci(4)](pci.4.md), [random(4)](random.4.md), [crypto(7)](../man7/crypto.7.md), [crypto(9)](../man9/crypto.9.md)

## 历史

`glxsb` 设备驱动首次出现于 OpenBSD 4.1。`glxsb` 设备驱动被引入 FreeBSD 7.1。

## 作者

`glxsb` 设备驱动最初由 Tom Cosgrove 为 OpenBSD 编写。由 Patrick Lamaiziere <patfbsd@davenulle.org> 移植到 FreeBSD。
