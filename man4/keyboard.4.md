# keyboard.4

`keyboard` — PC 键盘接口

## 名称

`keyboard`

## 描述

PC 键盘用作控制台字符输入设备。键盘由当前虚拟控制台拥有。要在虚拟控制台之间切换，使用组合键 `ALT+Fn`，即按住 ALT 并按下一个功能键。与功能键编号相同的虚拟控制台随即被选为当前虚拟控制台，并独占使用键盘和显示器。

控制台允许通过特殊按键序列输入键盘上实际不存在的值。要使用此功能，按住 ALT，然后通过数字小键盘输入 0-255 的十进制数，然后释放 ALT。输入的值随后用作一个字符的 ASCII 值。这样就可以输入键盘上不存在的任何 ASCII 值。控制台驱动程序还包括历史记录功能。通过按下 scroll-lock 键激活。这会保持显示，并启用光标箭头在最后滚出的行中上下滚动。

键盘可配置以适应个人用户和不同的国家布局。

键盘上的按键可具有以下任何功能：

**Normal** 键 输入与该键关联的 ASCII 值。

**Function** 键 输入一串 ASCII 值。

**Switch** 键 切换虚拟控制台。

**Modifier** 键 更改另一个键的含义。

键盘被视为从 1 到 n 编号的多个键。此编号通常被称为给定键的“scancode”。按键时，键的编号以 8 位字符形式传输，位 7 为 0；释放时，编号的位 7 为 1。这使得按键的映射完全可配置。

每个键的含义可通过 PIO_KEYMAP ioctl 调用编程，该调用以 keymap_t 结构为参数。此结构的布局如下：

```sh
		struct keymap {
			u_short	n_keys;
			struct key_t {
				u_char map[NUM_STATES];
				u_char spcl;
				u_char flgs;
			} key[NUM_KEYS];
		};
```

字段 n_keys 告诉系统有多少个键定义（扫描码）跟随。然后每个扫描码在 key_t 子结构中指定。

每个扫描码可转换为 8 个不同的值之一，具体取决于 shift、control 和 alt 状态。这八种可能性由 map 数组表示，如下所示：

```sh
                                                            alt
 scan                          cntrl          alt    alt   cntrl
 code     base   shift  cntrl  shift   alt   shift  cntrl  shift
 map[n]      0       1      2      3     4       5      6      7
 ----     ------------------------------------------------------
 0x1E      'a'     'A'   0x01   0x01    'a'    'A'   0x01   0x01
```

这是标记为“A”的键的默认映射，其扫描码通常为 0x1E。八个状态如上所示，赋予“A”键正常行为。spcl 字段用于对键进行“特殊”处理，解释如下。每个位对应于上述状态之一。如果该位为 0，则键发出相应 map[] 条目中定义的数字。如果该位为 1，则键为“特殊”。这意味着它不发出任何内容；而是更改“状态”。即它是 shift、control、alt、lock、切换屏幕、功能键或无操作键。位图是反向的，即 7 为 base，6 为 shift 等。

flgs 字段定义键是否应对 caps-lock（1）、num-lock（2）、两者（3）或忽略两者（0）作出反应。

kbdcontrol(1) 工具用于在运行时将此类描述加载到内核或从中读取。这使得在运行时更改按键分配成为可能，更重要的是从内核获取（GIO_KEYMAP ioctl）确切的键含义（例如由 X 服务器使用）。

功能键可使用 SETFKEY ioctl 调用编程。

此 ioctl 接受 fkeyarg_t 类型的参数：

```sh
		struct fkeyarg {
			u_short	keynum;
			char	keydef[MAXFK];
			char	flen;
		};
```

字段 keynum 定义要编程的功能键。数组 keydef 应包含要使用的新字符串（MAXFK 长），长度应输入 flen。

GETFKEY ioctl 调用以类似方式工作，但它返回 keynum 的当前设置。

功能键编号如下：

```sh
	F1-F12 			键 1 - 12
	Shift F1-F12		键 13 - 24
	Ctrl F1-F12		键 25 - 36
	Ctrl+shift F1-F12	键 37 - 48
	Home			键 49
	Up arrow		键 50
	Page Up			键 51
	(小键盘) -		键 52
	Left arrow		键 53
	(小键盘) 5              键 54
	Right arrow		键 55
	(小键盘) +		键 56
	End			键 57
	Down arrow		键 58
	Page down		键 59
	Insert 			键 60
	Delete			键 61
	Left window		键 62
	Right window		键 63
	Menu			键 64
```

kbdcontrol(1) 工具还允许在运行时更改这些值。

## 作者

Søren Schmidt <sos@FreeBSD.org>
