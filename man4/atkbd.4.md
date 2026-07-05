# atkbd.4

`atkbd` — AT 键盘接口

## 名称

`atkbd`

## 概要

`options ATKBD_DFLT_KEYMAP makeoptions ATKBD_DFLT_KEYMAP=_keymap_name_ options KBD_DISABLE_KEYMAP_LOAD device atkbd`

在 **/boot/device.hints** 中：

```ini
hint.atkbd.0.at="atkbdc"
hint.atkbd.0.irq="1"
```

## 描述

`atkbd` 驱动与 `atkbdc` 驱动一起，提供对连接到 AT 键盘控制器的 AT 84 键盘或 AT 增强型键盘的访问。

控制台驱动 [syscons(4)](syscons.4.md) 或 [vt(4)](vt.4.md) 需要此驱动。

内核配置文件中只能定义一个 `atkbdc` 设备。此设备还要求存在 `atkbdc` 键盘控制器。*irq* 号必须始终为 1；无法更改此号码。

### 功能键

AT 键盘有若干功能键。它们的编号如下，并可通过 kbdcontrol(1) 命令关联到字符串。可使用键盘映射文件（参见 kbdmap(5)）将它们映射到任意按键，尤其是默认未使用的 65 到 96 范围内的功能键。

| 功能键编号 | 功能键 |
| --- | --- |
| 1, 2,...12 | F1, F2,... F12 |
| 13, 14,...24 | Shift+F1, Shift+F2,... Shift+F12 |
| 25, 26,...36 | Ctl+F1, Ctl+F2,... Ctl+F12 |
| 37, 38,...48 | Shift+Ctl+F1, Shift+Ctl+F2,... Shift+Ctl+F12 |
| 49 | Home 和小键盘 7（不按 NumLock） |
| 50 | 上箭头和小键盘 8（不按 NumLock） |
| 51 | Page Up 和小键盘 9（不按 NumLock） |
| 52 | 小键盘 - |
| 53 | 左箭头和小键盘 4（不按 NumLock） |
| 54 | 小键盘 5（不按 NumLock） |
| 55 | 右箭头和小键盘 6（不按 NumLock） |
| 56 | 小键盘 + |
| 57 | End 和小键盘 1（不按 NumLock） |
| 58 | 下箭头和小键盘 2（不按 NumLock） |
| 59 | Page Down 和小键盘 3（不按 NumLock） |
| 60 | Ins 和小键盘 0（不按 NumLock） |
| 61 | Del |
| 62 | 左 GUI 键 |
| 63 | 右 GUI 键 |
| 64 | Menu |
| 65, 66,...96 | 空闲（默认未使用） |

有关如何为功能键分配字符串，请参见 kbdcontrol(1) 命令的手册页。

## 驱动配置

### 内核配置选项

以下内核配置选项控制 `atkbdc` 驱动。

***ATKBD_DFLT_KEYMAP*** 此选项将 `atkbdc` 驱动的默认内置键盘映射设为指定名称的键盘映射。参见下文实例。

***KBD_DISABLE_KEYMAP_LOAD*** 键盘映射可由 kbdcontrol(1) 命令修改。此选项将禁用此功能，防止用户更改按键分配。

### 驱动标志

`atkbdc` 驱动接受以下驱动标志。可在 **/boot/device.hints** 中设置，也可在引导加载器中设置（参见 [loader(8)](../man8/loader.8.md)）。

**bit** 0（FAIL_IF_NO_KBD）默认情况下，即使系统未实际连接键盘，`atkbdc` 驱动也会安装。此选项可在这种情况下阻止驱动安装。

**bit** 1（NO_RESET）给出此选项时，`atkbdc` 驱动在初始化时不会重置键盘。对于功能键具有特殊功能且重置键盘会丢失这些功能的笔记本电脑可能有用。

**bit** 2（ALT_SCANCODESET）某些键盘（如某些 ThinkPad 型号上的键盘）行为类似旧式 XT 键盘，需要此选项。

**bit** 3（NO_PROBE_TEST）给出此选项时，`atkbdc` 驱动在探测例程中不会测试键盘端口。某些机器在执行此测试时会在引导过程中挂起。

## 实例

`atkbdc` 驱动需要键盘控制器 `atkbdc`。因此，内核配置文件应包含以下行。

```sh
device atkbdc
```

```sh
device atkbd
```

以下示例展示如何将默认内置键盘映射设为 `jp.106.kbd`。

```sh
device atkbdc
```

```sh
options ATKBD_DFLT_KEYMAP
```

```sh
makeoptions ATKBD_DFLT_KEYMAP=jp.106
```

```sh
device atkbd
```

两种情况下，都需要在 **/boot/device.hints** 中加入以下行。

```sh
hint.atkbdc.0.at="isa"
```

```sh
hint.atkbdc.0.port="0x060"
```

```sh
hint.atkbd.0.at="atkbdc"
```

```sh
hint.atkbd.0.irq="1"
```

## 参见

kbdcontrol(1), [atkbdc(4)](atkbdc.4.md), [psm(4)](psm.4.md), [syscons(4)](syscons.4.md), [vt(4)](vt.4.md), kbdmap(5), [loader(8)](../man8/loader.8.md)

## 历史

`atkbdc` 驱动首次出现于 FreeBSD 3.1。

## 作者

`atkbdc` 驱动由 Søren Schmidt <sos@FreeBSD.org> 和 Kazutaka Yokota <yokota@FreeBSD.org> 编写。本手册页由 Kazutaka Yokota 编写。
