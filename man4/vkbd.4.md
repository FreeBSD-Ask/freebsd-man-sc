# vkbd(4)

`vkbd` — 虚拟 AT 键盘接口

## 名称

`vkbd`

## 概要

`device vkbd`

## 描述

`vkbd` 接口是一种软件回环机制，可粗略地描述为 [pty(4)](pty.4.md) 的虚拟 AT 键盘对应物，即 `vkbd` 之于虚拟 AT 键盘，如同 [pty(4)](pty.4.md) 驱动之于终端。

`vkbd` 驱动与 [pty(4)](pty.4.md) 驱动一样，提供两个接口：一个类似于其模拟的常规设施（`vkbd` 为虚拟 AT 键盘，[pty(4)](pty.4.md) 为终端）的键盘接口，以及一个字符特殊设备“控制”接口。

虚拟 AT 键盘命名为 `vkbd0 , vkbd1` 等，每个对应一个已打开的控制设备。

`vkbd` 接口允许打开特殊控制设备 **/dev/vkbdctl**。当此设备被打开时，`vkbd` 将返回最低未使用的 `vkbdctl` 设备的句柄（使用 devname(3) 来确定是哪一个）。

每个虚拟 AT 键盘支持常规的键盘接口 ioctl(2)，因此可像任何其他键盘一样与 kbdcontrol(1) 一起使用。控制设备支持与虚拟 AT 键盘设备完全相同的 ioctl(2)。向控制设备写入 AT 扫描码会生成虚拟 AT 键盘上的输入，就像（不存在的）硬件刚刚接收到它一样。

虚拟 AT 键盘控制设备通常为 **/dev/vkbdctl**<`N`>，是独占打开的（如果已打开则无法再次打开），且仅限超级用户使用。read(2) 调用将返回虚拟 AT 键盘状态结构（定义于

`#include <dev/vkbd/vkbd_var.h>`

如果有可用的话；否则将阻塞直到有可用结构，或返回 Er EWOULDBLOCK，取决于是否启用了非阻塞 I/O。

write(2) 调用传递要由虚拟 AT 键盘“接收”的 AT 扫描码。每个 AT 扫描码必须以 `unsigned int` 传递。虽然 AT 扫描码必须以 `unsigned int` 传递，但传递给 write(2) 的缓冲区大小仍应以字节为单位，即：

```sh
static unsigned int     codes[] =
{
/*      Make    Break */
        0x1e,   0x9e
};
int
main(void)
{
        int     fd, len;
        fd = open("/dev/vkbdctl0", O_RDWR);
        if (fd < 0)
                err(1, "open");
        /* 注意是 sizeof(codes) - 不是 2！ */
        len = write(fd, codes, sizeof(codes));
        if (len < 0)
                err(1, "write");
        close(fd);
        return (0);
}
```

如果输入队列没有足够空间，写入将阻塞。

控制设备还支持 select(2) 用于读和写。

在控制设备最后一次关闭时，虚拟 AT 键盘将被移除。所有排队的扫描码都将被丢弃。

## 参见

kbdcontrol(1), [atkbdc(4)](atkbdc.4.md), [psm(4)](psm.4.md), [syscons(4)](syscons.4.md), [vt(4)](vt.4.md)

## 历史

`vkbd` 模块在 FreeBSD 6.0 中实现。

## 作者

Maksim Yevmenkin <m_evmenkin@yahoo.com>

## 注意事项

`vkbd` 接口是一种软件回环机制，因此 [ddb(4)](ddb.4.md) 无法与其配合使用。[syscons(4)](syscons.4.md) 驱动的当前实现只能接受来自一个键盘的输入，即使它是虚拟的。因此，无法同时使有线键盘和虚拟键盘处于活动状态。但是，原则上可以从不同来源获取 AT 扫描码并将其写入同一虚拟键盘。虚拟键盘状态同步由用户负责。
