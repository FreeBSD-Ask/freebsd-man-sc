# dialog(1)

`dialog` — 从 shell 脚本显示对话框

## 名称

`dialog`

## 概要

`dialog --clear`

`dialog --create-rc file`

`dialog --print-maxsize`

`dialog` `common-options` `box-options`

## 描述

`dialog` 是一个程序，允许你从 shell 脚本中使用对话框呈现各种问题或显示消息。这些类型的对话框已实现（尽管不一定全部编译进 `dialog`）：

`buildlist`, `calendar`, `checklist`, `dselect`, `editbox`, `form`, `fselect`, `gauge`, `infobox`, `inputbox`, `inputmenu`, `menu`, `mixedform`, `mixedgauge`, `msgbox`（message）, `passwordbox`, `passwordform`, `pause`, `prgbox`, `programbox`, `progressbox`, `radiolist`, `rangebox`, `tailbox`, `tailboxbg`, `textbox`, `timebox`, `treeview` 和 `yesno`（yes/no）。

你可以在一个脚本中放置多个对话框：

- 使用 “`--and-widget`” 标记强制 `dialog` 进入下一个对话框，除非你已按 ESC 取消，或者
- 直接添加下一个对话框的标记，形成链式。

当对话框的返回码非零时（例如 Cancel 或 No，参见诊断），`dialog` 停止链接。

某些小部件（例如 checklist）会将文本写入 `dialog` 的输出。通常是标准错误，但有选项可以更改：`--output-fd`、`--stderr` 和 `--stdout`。如果按 Cancel 按钮（或 ESC），不写入任何文本；`dialog` 在这种情况下立即退出。

## 选项

所有选项都以 “`--`”（两个 ASCII 连字符，为了方便那些使用 locale 支持失常的系统的人）开头。

单独的 “`--`” 用作转义，即命令行上的下一个标记不被视为选项。

```
--title -- --Not an option
```

当通用（非小部件）选项重复时，使用最后找到的选项。布尔选项有特殊处理，可以通过在前导 “`--`” 之后添加（或省略） “`no`” 修饰符来取消。例如，此处记录的是 `--no-shadow`，但 `--shadow` 也可接受。

`--args` 选项告诉 `dialog` 将命令行参数列表输出到标准错误。在使用 “`--`” 和 “`--file`” 调试复杂脚本时非常有用，因为命令行在展开这些标记时可能被重写。

`--file` 选项告诉 `dialog` 从以其值命名的文件中读取参数。

```
--file parameterfile
```

不在双引号内的空白将被丢弃（使用反斜杠引用单个字符）。结果插入命令行，替换 “`--file`” 及其选项值。命令行的解释从该点恢复。如果 `parameterfile` 以 “`&`” 开头，`dialog` 将后续文本解释为文件描述符编号而非文件名。

大多数小部件接受高度和宽度参数，可用于自动调整小部件大小以适应多行消息提示值：

- 如果参数为负数，`dialog` 使用屏幕大小。
- 如果参数为零，`dialog` 使用小部件显示提示和数据的最小尺寸。
- 否则，`dialog` 使用给定的小部件尺寸。

### 通用选项

大多数通用选项在处理每个小部件之前重置。

**`--ascii-lines`** 不在框周围绘制图形线条，而是在相同位置绘制 ASCII “`+`” 和 “`-`”。另请参见 “`--no-lines`”。

**`--aspect ratio`** 在使用自动调整大小（高度和宽度指定为 0）时，让你控制框尺寸。它表示宽/高。默认值为 9，意味着每 1 行高对应 9 个字符宽。

**`--backtitle backtitle`** 指定在屏幕顶部背景上显示的 backtitle 字符串。

**`--begin y x`** 指定对话框在屏幕上的左上角位置。

**`--cancel-label string`** 覆盖 “`Cancel`” 按钮使用的标签。

**`--clear`** 清除小部件屏幕，仅保留 `screen_color` 背景。在将小部件与 “`--and-widget`” 组合使用时，用此选项擦除屏幕上先前小部件的内容，使其不会出现在后续小部件的内容下方。可理解为 “`--keep-window`” 的补集。要比较效果，可使用以下命令：

```sh
# 三个小部件都可见，阶梯效果，顺序 1,2,3：
dialog --begin 2 2 --yesno "" 0 0 \
  --and-widget --begin 4 4 --yesno "" 0 0 \
  --and-widget --begin 6 6 --yesno "" 0 0
```

```sh
# 只剩最后一个小部件可见：
dialog --clear --begin 2 2 --yesno "" 0 0 \
  --and-widget --clear --begin 4 4 --yesno "" 0 0 \
  --and-widget --begin 6 6 --yesno "" 0 0
```

```sh
# 三个小部件都可见，阶梯效果，顺序 3,2,1：
dialog --keep-window --begin 2 2 --yesno "" 0 0 \
  --and-widget --keep-window --begin 4 4 --yesno "" 0 0 \
  --and-widget --begin 6 6 --yesno "" 0 0
```

```sh
# 第一个和第三个小部件可见，阶梯效果，顺序 3,1：
dialog --keep-window --begin 2 2 --yesno "" 0 0 \
  --and-widget --clear --begin 4 4 --yesno "" 0 0 \
  --and-widget --begin 6 6 --yesno "" 0 0
```

注意，如果要在 dialog 程序退出后恢复原始控制台颜色并将光标归位，请使用 clear(1) 命令。反之，如果要在程序退出后清除屏幕并将光标置于左下角，请使用 `--erase-on-exit` 选项。

**`--colors`** 解释对话框文本中嵌入的 “`\Z`” 序列，按以下字符指示 `dialog` 设置颜色或视频属性：

- 0 到 7 是 curses 中使用的 ANSI 颜色编号：黑、红、绿、黄、蓝、品红、青和白。
- 加粗由 “`b`” 设置，由 “`B`” 重置。
- 反转由 “`r`” 设置，由 “`R`” 重置。
- 下划线由 “`u`” 设置，由 “`U`” 重置。
- 设置是累积的，例如 “`\Zb\Z1`” 使后续文本加粗（可能更亮）红色。
- 使用 “`\Zn`” 恢复正常设置。

**`--column-separator string`** 告诉 `dialog` 在出现给定字符串时拆分单选/复选框和菜单的数据，并将拆分的数据对齐到列中。

**`--cr-wrap`** 将对话框文本中嵌入的换行符解释为屏幕上的换行。否则，`dialog` 仅在需要适应文本框时换行。

即使你可以用此选项控制换行，`dialog` 仍会换行任何对于框宽度过长的行。不使用 `cr-wrap` 时，文本的布局可以在脚本源代码中格式化得很好看，而不会影响在对话框中的显示方式。

`cr-wrap` 功能在以下条件下实现：

- 字符串包含 “`\n`” 且未使用 `--no-nl-expand` 选项，或者
- 使用了 `--trim` 选项。

更多信息请参见空格选项。

**`--create-rc file`** 当 `dialog` 支持运行时配置时，这可用于将示例配置文件转储到 `file` 指定的文件中。

**`--cursor-off-label`** 将终端光标置于按钮末尾而非按钮标签的第一个字符上。这在光标颜色与按钮标签文本颜色交互不良时有助于减少视觉混乱。

**`--date-format format`** 如果主机提供 strftime，此选项允许你为 `--calendar` 小部件打印的日期指定格式。时间（小时、分钟、秒）为当前本地时间。

**`--defaultno`** 使 yes/no 框的默认值为 **No**。同样，将提供 “`OK`” 和 “`Cancel`” 的小部件的默认按钮视为 Cancel。如果给出了 `--no-cancel` 或 `--visit-items`，这些选项会覆盖此设置，使默认按钮始终为 “`Yes`”（内部与 “`OK`” 相同）。

**`--default-button string`** 设置小部件中的默认（预选）按钮。通过预选按钮，脚本使用户能够简单按 Enter 以最少交互通过对话框。

此选项的值是按钮的名称：`ok`、`yes`、`cancel`、`no`、`help` 或 `extra`。

通常，每个小部件中的第一个按钮是默认值。显示的第一个按钮由小部件以及 `--no-ok` 和 `--no-cancel` 选项共同确定。如果未给出此选项，则不分配默认按钮。

**`--default-item string`** 在 checklist、form 或 menu 框中设置默认项。通常框中的第一项是默认值。

**`--erase-on-exit`** 当 `dialog` 退出时，移除对话框小部件，将整个屏幕擦除为其原生背景色，并将终端光标置于左下角。

**`--exit-label string`** 覆盖 “`EXIT`” 按钮使用的标签。

**`--extra-button`** 在 “`OK`” 和 “`Cancel`” 按钮之间显示一个额外按钮。

**`--extra-label string`** 覆盖 “`Extra`” 按钮使用的标签。注意：对于 inputmenu 小部件，默认为 “`Rename`”。

**`--help`** 将帮助信息打印到标准输出并退出。如果未给出选项或给出了无法识别的选项，也会打印帮助信息。

**`--help-button`** 在具有标记项列表的框（即 checklist、radiolist、menu 和 treeview 框）中，在 “`OK`” 和 “`Cancel`” 按钮之后显示帮助按钮。

退出时，返回状态指示按下了 Help 按钮。`dialog` 还会在 “`HELP`” 标记之后向其输出写入消息：

- 如果同时给出了 “`--item-help`”，则写入 item-help 文本。
- 否则，写入项的标记（第一个字段）。

你可以使用 `--help-tags` 选项和/或设置 `DIALOG_ITEM_HELP` 环境变量来修改这些消息和退出状态。

此选项可应用于其他具有 “`OK`” 按钮的小部件，无论是否使用 “`Cancel`” 按钮。其他小部件的返回状态和输出不做特殊处理；help-button 只是一个额外按钮。

**`--help-label string`** 覆盖 “`Help`” 按钮使用的标签。

**`--help-status`** 如果选择了 help-button，则在 item-help “`HELP`” 信息之后写入 checklist、radiolist 或 form 信息。这可用于在处理帮助请求后重构 checklist 的状态。

**`--help-tags`** 修改 `--help-button` 退出时写入的消息，使其始终仅为项的标记。这不影响退出状态码。

**`--hfile filename`** 当用户按 F1 时使用 textbox 显示给定文件。

**`--hline string`** 在小部件底部居中显示给定字符串。

**`--ignore`** 忽略 `dialog` 不识别的选项。一些已知的选项如 “`--icon`” 无论如何都会被忽略，但为了与其他实现兼容，这是更好的选择。

**`--input-fd fd`** 从给定文件描述符读取键盘输入。大多数脚本从标准输入读取，但 gauge 小部件读取管道（始终为标准输入）。某些配置在 `dialog` 尝试重新打开终端时无法正常工作。如果你的脚本必须在该类型环境中工作，请使用此选项（适当调整文件描述符）。

**`--insecure`** 通过为每个字符回显星号，使 password 小部件更友好但安全性较低。

**`--iso-week`** 根据 ISO-8601 设置 `--calendar` 选项中显示的周编号的起始点，从包含一月份星期四的第一周开始编号。

**`--item-help`** 解释 checklist、radiolist 和 menu 框的标记数据，添加一列显示在屏幕底部，用于当前选定项。

**`--keep-tite`** 当使用 ncurses 构建时，`dialog` 通常会检查它是否在 xterm 中运行，在这种情况下尝试抑制会使其切换到备用屏幕的初始化字符串。在多次运行的脚本中，在正常和备用屏幕之间切换在视觉上会令人分心。使用此选项允许 `dialog` 使用这些初始化字符串。

**`--keep-window`** 通常，当 `dialog` 执行由 “`--and-widget`” 连接的多个 `tailboxbg` 小部件时，它会通过重绘来清除屏幕上的旧小部件。使用此选项抑制该重绘。

退出时，`dialog` 重绘所有标记了 “`--keep-window`” 的小部件，即使它们不是 `tailboxbg` 小部件。这导致它们以相反顺序重绘。示例参见 “`--clear`” 选项的讨论。

**`--last-key`** 退出时，报告用户输入的最后一个键。这是 curses 键码而非符号或字面字符，且仅报告绑定到操作的键。脚本可用它区分绑定到同一操作的两个键。

**`--max-input size`** 将输入字符串限制为给定大小。如果未指定，限制为 2048。

**`--no-cancel`** 在 checklist、inputbox 和 menu 框模式中抑制 “`Cancel`” 按钮。脚本仍可测试用户是否按 ESC 键取消退出。

**`--no-collapse`** 通常，`dialog` 将制表符转换为空格，并将多个空格减少为单个空格，用于消息框等中显示的文本。使用此选项禁用该功能。注意，`dialog` 仍会换行文本，受 `--cr-wrap` 和 `--trim` 选项约束。

`no-collapse` 功能在以下条件下实现：

- 字符串包含 “`\n`” 且未使用 `--no-nl-expand` 选项，或者
- 未使用 `--trim` 选项。

更多信息请参见空格选项。

**`--no-hot-list`** 告诉 `dialog` 抑制列表的热键功能，例如 checkbox、menus。

通常，列表条目的第一个大写字符将高亮显示，键入该字符会将焦点移至该条目。此选项抑制高亮和移动。

按钮的热键（“`OK`”、“`Cancel`” 等）不受影响。

**`--no-items`** 某些小部件（checklist、inputmenu、radiolist、menu）显示两列列表（“`tag`” 和 “`item`”，即 “`description`”）。此选项告诉 `dialog` 读取较短的行，省略列表的 “`item`” 部分。这偶尔有用，例如标记提供足够信息时。

另请参见 `--no-tags`。如果同时给出这两个选项，此选项被忽略。

**`--no-kill`** 告诉 `dialog` 将 `tailboxbg` 框置于后台，将其进程 ID 打印到 `dialog` 的输出。后台进程禁用 SIGHUP。

**`--no-label string`** 覆盖 “`No`” 按钮使用的标签。

**`--no-lines`** 不在框周围绘制线条，而是在相同位置绘制空格。另请参见 “`--ascii-lines`”。

**`--no-mouse`** 不启用鼠标。

**`--no-nl-expand`** 不将消息/提示文本的 “`\n`” 子字符串转换为字面换行符。

`no-nl-expand` 功能仅在字符串包含 “`\n`” 时使用，以便有内容可转换。

更多信息请参见空格选项。

**`--no-ok`** 抑制 “`OK`” 按钮，使其不显示。脚本仍可测试用户是否按 “`Enter`” 键接受数据：

- 使用 `--no-ok` 选项时，“`Enter`” 键始终作为 “`OK`” 按钮处理。即默认绑定到 LEAVE 虚拟键。
- 不使用 `--no-ok` 时，你可以使用 Tab 键在小部件的字段和按钮之间移动光标。在这种情况下，如果光标位于按钮上，“`Enter`” 键激活当前按钮。
- 为处理使用 `--no-ok` 时要激活按钮的情况，还有另一个虚拟键 LEAVE，激活当前按钮。默认情况下，`^D`（EOF）绑定到该键。

**`--no-shadow`** 抑制每个对话框右下方绘制的阴影。

**`--no-tags`** 某些小部件（checklist、inputmenu、radiolist、menu）显示两列列表（“`tag`” 和 “`description`”）。标记对脚本编写有用，但可能对用户无帮助。`--no-tags` 选项（来自 Xdialog）可用于从显示中抑制标记列。与 `--no-items` 选项不同，这不影响从脚本读取的数据。

Xdialog 不为类似的 buildlist 和 treeview 小部件显示标记列；`dialog` 也这样做。

通常，`dialog` 允许你通过将单个字符匹配到标记的第一个字符来快速移动到显示列表中的条目。给出 `--no-tags` 选项时，`dialog` 匹配描述的第一个字符。无论哪种情况，可匹配的字符都会高亮显示。

**`--ok-label string`** 覆盖 “`OK`” 按钮使用的标签。

**`--output-fd fd`** 将输出定向到给定文件描述符。大多数脚本写入标准错误，但根据脚本，错误消息也可能写入那里。

**`--separator string`** **`--output-separator string`** 指定一个字符串，用于分隔 `dialog` 输出中 checklists 的输出，而非换行符（用于 `--separate-output`）或空格。这适用于通常使用换行符的其他小部件，如 forms 和 editboxes。

**`--print-maxsize`** 将对话框的最大尺寸（即屏幕尺寸）打印到 `dialog` 的输出。可单独使用，无需其他选项。

**`--print-size`** 在框初始化时将每个对话框的尺寸打印到 `dialog` 的输出。

**`--print-text-only string`** `[` `height` `[` `width` `]` `]` 将字符串按其在消息框中换行的方式打印到 `dialog` 的输出。

由于可选的高度和宽度默认为零，如果省略它们，`dialog` 会根据屏幕尺寸自动调整大小。

**`--print-text-size string`** `[` `height` `[` `width` `]` `]` 将字符串按其在消息框中换行后的尺寸打印到 `dialog` 的输出，形式为：

```
height width
```

由于可选的高度和宽度参数默认为零，如果省略它们，`dialog` 会根据屏幕尺寸自动调整大小。

**`--print-version`** 将 `dialog` 的版本打印到 `dialog` 的输出。可单独使用，无需其他选项。它本身不会导致 `dialog` 退出。

**`--quoted`** 通常，`dialog` 引用 checklist 返回的字符串以及 item-help 文本。使用此选项按需引用所有字符串结果（即如果字符串包含空白或单引号或双引号字符）。

**`--reorder`** 默认情况下，buildlist 小部件对输出（右）列表使用与输入（左）相同的顺序。使用此选项告诉 `dialog` 使用用户向输出列表添加选择的顺序。

**`--scrollbar`** 对于持有可滚动数据集的小部件，在其右边缘绘制滚动条。这不响应鼠标。

**`--separate-output`** 对于某些小部件（buildlist、checklist、treeview），每次输出一行结果，不带引用。这便于另一个程序解析。

**`--separate-widget string`** 指定一个字符串，用于分隔 `dialog` 输出中每个小部件的输出。这用于简化解析具有多个小部件的对话框的结果。如果未给出此选项，默认分隔字符串为制表符。

**`--single-quoted`** 对 checklist 的输出以及 item-help 文本按需使用单引号（不需要时不引用）。

如果未设置此选项，`dialog` 可能在每个项周围使用双引号。无论哪种情况，`dialog` 都添加反斜杠以使输出在 shell 脚本中有用。

如果字符串包含空白或单引号或双引号字符，则需要单引号。

**`--size-err`** 在尝试使用对话框之前检查其结果大小，如果大于屏幕则打印结果大小。（此选项已过时，因为所有 new-window 调用都会被检查）。

**`--sleep secs`** 处理对话框后休眠（延迟）给定秒数。

**`--stderr`** 将输出定向到标准错误。这是默认值，因为 curses 通常将屏幕更新写入标准输出。

**`--stdout`** 将输出定向到标准输出。此选项为与 Xdialog 兼容而提供，但不建议在可移植脚本中使用，因为 curses 通常将其屏幕更新写入标准输出。如果使用此选项，`dialog` 尝试重新打开终端以便写入显示。根据平台和环境，这可能失败。

**`--tab-correct`** 将每个制表符转换为一个或多个空格（对于 textbox 小部件；否则为单个空格）。否则，制表符根据 curses 库的解释进行渲染。`--no-collapse` 选项禁用制表符展开。

**`--tab-len n`** 指定如果给出 `--tab-correct` 选项时制表符占用的空格数。默认为 8。此选项仅对 textbox 小部件有效。

**`--time-format format`** 如果主机提供 strftime，此选项允许你为 `--timebox` 小部件打印的时间指定格式。在这种情况下，日、月、年值为当前本地时间。

**`--timeout secs`** 如果在给定秒数内无用户响应则超时。零秒超时被忽略。

通常，超时会导致在当前小部件中输入 ESC 字符，取消它。其他小部件可能仍在屏幕上；这些不被取消。设置 `DIALOG_TIMEOUT` 环境变量告诉 `dialog` 直接退出，即取消屏幕上的所有小部件。

此选项被 `--pause` 小部件忽略。如果后台 `--tailboxbg` 选项用于设置多个并发小部件，它也被覆盖。

**`--title title`** 指定在对话框顶部显示的标题字符串。

**`--trace filename`** 将命令行参数、按键和其他信息记录到给定文件。如果 `dialog` 读取配置文件，也会记录。gauge 小部件的管道输入会被记录。使用 control/T 记录当前对话窗口的图片。

程序专门处理某些命令行参数，并在处理时从参数列表中移除。例如，如果第一个选项是 `--trace`，则在 `dialog` 初始化显示之前处理（并移除）它。

**`--week-start day`** 设置 `--calendar` 选项中使用的周的起始日。`day` 参数可以是：

- 数字（0 到 6，使用 POSIX 表示星期日到星期六），或者
- 特殊值 “`locale`”（适用于使用 glibc 的系统，提供 locale 命令的扩展，即 `first_weekday` 值）。
- 匹配日历小部件中显示的星期几缩写之一的字符串，例如 “`Mo`” 表示 “`Monday`”。

**`--trim`** 从消息文本中消除前导空白、修剪字面换行符和重复空白。

`trim` 功能在以下条件下实现：

- 字符串不包含 “`\n`”，或者
- 使用了 `--no-nl-expand` 选项。

更多信息请参见空格选项。

另请参见 `--cr-wrap` 和 `--no-collapse` 选项。

**`--version`** 将 `dialog` 的版本打印到标准输出并退出。另请参见 `--print-version`。

**`--visit-items`** 修改 checklist、radiolist、menubox 和 inputmenu 的制表符遍历，将项列表作为状态之一。这作为视觉辅助很有用，即光标位置对某些用户有帮助。

给出此选项时，光标最初位于列表上。缩写（标记的第一个字母）应用于列表项。如果按 Tab 键到按钮行，缩写应用于按钮。

**`--yes-label string`** 覆盖 “`Yes`” 按钮使用的标签。

### 盒子选项

所有对话框都至少有三个参数：

- `text` — 框的标题或内容。
- `height` — 对话框的高度。
- `width` — 对话框的宽度。

其他参数取决于框类型。

**`--buildlist text height width list-height [ tag item status ] ...`**

buildlist 对话框并排显示两个列表。左侧列表显示未选中的项。右侧列表显示已选中的项。随着项被选中或取消选中，它们在列表之间移动。

使用回车或 “`OK`” 按钮接受选中窗口中的当前值并退出。结果按选中窗口中显示的顺序写入。

每个条目的初始开/关状态由 `status` 指定。

对话框的行为类似于菜单，使用 `--visit-items` 控制是否允许光标直接访问列表。

- 如果未给出 `--visit-items`，制表符遍历使用两个状态（OK/Cancel）。
- 如果给出了 `--visit-items`，制表符遍历使用四个状态（Left/Right/OK/Cancel）。

无论是否给出 `--visit-items`，都可以使用默认的 “`^`”（左列）和 “`$`”（右列）键在两个列表之间移动高亮。

退出时，打开的条目的标记字符串列表将打印到 `dialog` 的输出。

如果未给出 “`--separate-output`” 选项，字符串将按需引用，使脚本易于分隔它们。默认情况下，按需使用双引号。参见 `--single-quoted` 选项，它修改引用行为。

**`--calendar text height width day month year`**

日历框在单独可调整的窗口中显示月、日和年。如果日、月或年的值缺失或为负，使用当前日期的相应值。你可以使用左、上、右和下箭头增减任何值。使用 vi 风格的 `h`、`j`、`k` 和 `l` 在一个月的日数组中移动。使用 tab 或 backtab 在窗口之间移动。如果年给定为零，使用当前日期作为初始值。

退出时，日期以 `day/month/year` 形式打印。可以使用 `--date-format` 选项覆盖格式。

**`--checklist text height width list-height [ tag item status ] ...`**

checklist 框类似于 menu 框；以菜单形式呈现多个条目。另一个区别是你可以通过将条目的 `status` 设置为 `on` 来指示当前选中的条目。不是在条目中选择一个，每个条目都可由用户打开或关闭。每个条目的初始开/关状态由 `status` 指定。

退出时，打开的条目的标记字符串列表将打印到 `dialog` 的输出。

如果未给出 `--separate-output` 选项，字符串将按需引用，使脚本易于分隔它们。默认情况下，按需使用双引号。参见 `--single-quoted` 选项，它修改引用行为。

**`--dselect filepath height width`**

目录选择对话框显示一个文本输入窗口，你可在其中输入目录，上方是一个带有目录名的窗口。

此处 `filepath` 可以是文件路径，在这种情况下目录窗口将显示路径的内容，文本输入窗口将包含预选目录。

使用 tab 或箭头键在窗口之间移动。在目录窗口中，使用上/下箭头键滚动当前选择。使用空格键将当前选择复制到文本输入窗口。

键入任何可打印字符将焦点切换到文本输入窗口，输入该字符并滚动目录窗口到最接近的匹配。

使用回车或 “`OK`” 按钮接受文本输入窗口中的当前值并退出。

退出时，文本输入窗口的内容写入 `dialog` 的输出。

**`--editbox filepath height width`**

编辑框对话框显示文件副本。你可以使用退格、删除和光标键来纠正键入错误。它还识别 pageup/pagedown。与 `--inputbox` 不同，你必须按 tab 到 “`OK`” 或 “`Cancel`” 按钮关闭对话框。在框内按 “`Enter`” 键将拆分相应行。

退出时，编辑窗口的内容写入 `dialog` 的输出。

**`--form text height width formheight [ label y x item y x flen ilen ] ...`**

form 对话框显示由标签和字段组成的表单，通过脚本中给出的坐标定位在可滚动窗口上。字段长度 `flen` 和输入长度 `ilen` 告诉字段可以有多长。前者定义选中字段的显示长度，后者定义字段中输入数据的允许长度。

- 如果 `flen` 为零，相应字段不能更改，且字段内容决定显示长度。
- 如果 `flen` 为负，相应字段不能更改，且 `flen` 的否定值用作显示长度。
- 如果 `ilen` 为零，将其设置为 `flen`。

使用上/下箭头（或 control/N、control/P）在字段之间移动。使用 tab 在窗口之间移动。

退出时，表单字段的内容写入 `dialog` 的输出，每个字段以换行符分隔。用于填充不可编辑字段（`flen` 为零或负）的文本不写出。

**`--fselect filepath height width`**

fselect（文件选择）对话框显示一个文本输入窗口，你可在其中输入文件名（或目录），上方是带有目录名和文件名的两个窗口。

此处 `filepath` 可以是文件路径，在这种情况下文件和目录窗口将显示路径的内容，文本输入窗口将包含预选文件名。

使用 tab 或箭头键在窗口之间移动。在目录或文件名窗口中，使用上/下箭头键滚动当前选择。使用空格键将当前选择复制到文本输入窗口。

键入任何可打印字符将焦点切换到文本输入窗口，输入该字符并滚动目录和文件名窗口到最接近的匹配。

键入空格字符强制 `dialog` 完成当前名称（直到可能有多个匹配的点）。

使用回车或 “`OK`” 按钮接受文本输入窗口中的当前值并退出。

退出时，文本输入窗口的内容写入 `dialog` 的输出。

**`--gauge text height width [percent]`**

gauge 框沿框底部显示一个仪表。仪表指示百分比。新百分比从标准输入读取，每行一个整数。仪表更新以反映每个新百分比。如果标准输入读取字符串 “`XXX`”，则后续第一行作为整数百分比，然后直到另一个 “`XXX`” 的行用于新提示。在标准输入上达到 EOF 时，gauge 退出。

`percent` 值表示仪表中显示的初始百分比。如果未指定，为零。

退出时，不向 `dialog` 的输出写入文本。小部件不接受输入，因此退出状态始终为 OK。

**`--infobox text height width`**

info 框基本上是 message 框。但是，在这种情况下，`dialog` 在向用户显示消息后立即退出。`dialog` 退出时不清除屏幕，因此消息将保留在屏幕上，直到调用 shell 脚本稍后清除它。当你想通知用户某些操作正在进行可能需要一些时间才能完成时，这很有用。

退出时，不向 `dialog` 的输出写入文本。返回 OK 退出状态。

**`--inputbox text height width [init]`**

当你想问需要用户输入字符串作为答案的问题时，input 框很有用。如果提供了 `init`，它用于初始化输入字符串。输入字符串时，可使用退格、删除和光标键纠正键入错误。如果输入字符串长于对话框可容纳的长度，输入字段将滚动。

退出时，输入字符串将打印到 `dialog` 的输出。

**`--inputmenu text height width menu-height [ tag item ] ...`**

inputmenu 框非常类似于普通 menu 框。它们之间只有几个区别：

1. 条目不自动居中而是左对齐。
2. 隐含一个额外按钮（称为 Rename），按下时重命名当前项。
3. 可以通过按 Rename 按钮重命名当前条目。然后 `dialog` 将在 `dialog` 的输出上写入以下内容：

```
RENAMED <tag> <item>
```

**`--menu text height width menu-height [ tag item ] ...`**

顾名思义，menu 框是一个对话框，可用于以菜单形式呈现选择列表供用户选择。选择按给定顺序显示。每个菜单条目由标记字符串和项字符串组成。标记给条目一个名称以将其与菜单中的其他条目区分开来。项是条目表示的选项的简短描述。用户可以通过按光标键、标记的第一个字母作为热键或数字键 1 到 9 在菜单条目之间移动。菜单中一次显示 `menu-height` 个条目，但如果条目多于该数，菜单将滚动。

退出时，所选菜单条目的标记将打印到 `dialog` 的输出。如果给出了 `--help-button` 选项，当用户选择帮助按钮时将打印相应的帮助文本。

**`--mixedform text height width formheight [ label y x item y x flen ilen itype ] ...`**

mixedform 对话框显示由标签和字段组成的表单，与 `--form` 对话框非常相似。区别在于为每个字段的描述添加了字段类型参数。类型中的每一位表示字段的一个属性：

1. hidden，例如密码字段。
2. readonly，例如标签。

**`--mixedgauge text height width percent [ tag1 item1 ] ...`**

mixedgauge 框沿框底部显示一个仪表。仪表指示百分比。

它还在框顶部显示标记值和项值的列表。标记值参见 (3)。

文本显示为列表和仪表之间的标题。`percent` 值表示仪表中显示的初始百分比。

不像 `--gauge` 那样提供从标准输入读取数据的规定。

退出时，不向 `dialog` 的输出写入文本。小部件不接受输入，因此退出状态始终为 OK。

**`--msgbox text height width`**

message 框非常类似于 yes/no 框。message 框和 yes/no 框之间唯一的区别是 message 框只有一个 OK 按钮。你可以使用此对话框显示你喜欢的任何消息。阅读消息后，用户可以按 ENTER 键以便 `dialog` 退出，调用 shell 脚本可以继续其操作。

如果消息对于空间太大，`dialog` 可能允许你滚动它，前提是底层 curses 实现足够强大。在这种情况下，小部件底部显示百分比。

退出时，不向 `dialog` 的输出写入文本。仅提供 “`OK`” 按钮用于输入，但可能返回 ESC 退出状态。

**`--pause text height width seconds`**

pause 框沿框底部显示一个仪表。仪表指示暂停结束前剩余的秒数。当达到超时或用户按 OK 按钮（状态 OK）或用户按 CANCEL 按钮或 Esc 键时，pause 退出。

**`--passwordbox text height width [init]`**

password 框类似于 input 框，区别在于用户输入的文本不显示。这在提示输入密码或其他敏感信息时很有用。请注意，如果在 “`init`” 中传递任何内容，它将在系统进程表中可见，便于随意窥探。此外，向用户提供他们看不到的默认密码令人困惑。由于这些原因，强烈不建议使用 “`init`”。如果你不在乎密码，请参见 `--insecure`。

退出时，输入字符串将打印到 `dialog` 的输出。

**`--passwordform text height width formheight [ label y x item y x flen ilen ] ...`**

这与 `--form` 相同，区别在于所有文本字段都被视为 password 小部件而非 inputbox 小部件。

**`--prgbox text command height width`**

**`--prgbox command height width`**

prgbox 非常类似于 programbox。

此对话框用于显示作为 prgbox 参数指定的命令的输出。

命令完成后，用户可以按 ENTER 键以便 `dialog` 退出，调用 shell 脚本可以继续其操作。

如果给出四个参数，它在标题下显示文本，与滚动文件内容分开。如果仅给出三个参数，则省略此文本。

**`--programbox text height width`**

**`--programbox height width`**

programbox 非常类似于 progressbox。program 框和 progress 框之间唯一的区别是 program 框显示 OK 按钮（但仅在命令完成后）。

此对话框用于显示命令的管道输出。命令完成后，用户可以按 ENTER 键以便 `dialog` 退出，调用 shell 脚本可以继续其操作。

如果给出三个参数，它在标题下显示文本，与滚动文件内容分开。如果仅给出两个参数，则省略此文本。

**`--progressbox text height width`**

**`--progressbox height width`**

progressbox 类似于 tailbox，区别在于：

a) 它显示命令的管道输出而非文件内容，并且

b) 它在达到文件末尾时退出（没有 “`OK`” 按钮）。

如果给出三个参数，它在标题下显示文本，与滚动文件内容分开。如果仅给出两个参数，则省略此文本。

**`--radiolist text height width list-height [ tag item status ] ...`**

radiolist 框类似于 menu 框。唯一的区别是你可以通过将条目的 `status` 设置为 `on` 来指示当前选中的条目。

退出时，选中项的标记写入 `dialog` 的输出。

**`--rangebox text height width min-value max-value default-value`**

允许用户从值范围中选择，例如使用滑块。对话框将当前值显示为条（类似 gauge 对话框）。Tab 或箭头键在按钮和值之间移动光标。当光标位于值上时，你可以通过以下方式编辑：

- 左/右光标移动选择要修改的数字
- `+`/`-` 字符将数字增减一
- `0` 到 `9` 将数字设置为给定值

某些键在所有光标位置也被识别：

- home/end 将值设置为其最大或最小值
- pageup/pagedown 增加值使滑块移动一列

**`--tailbox file height width`**

在对话框中显示文件中的文本，如 “`tail -f`” 命令。使用 vi 风格的 “`h`” 和 “`l`” 或箭头键左右滚动。“`0`” 重置滚动。

退出时，不向 `dialog` 的输出写入文本。仅提供 “`OK`” 按钮用于输入，但可能返回 ESC 退出状态。

**`--tailboxbg file height width`**

作为后台任务在对话框中显示文件中的文本，如 “`tail -f &`” 命令。使用 vi 风格的 “`h`” 和 “`l`” 或箭头键左右滚动。“`0`” 重置滚动。

如果屏幕上同时有其他小部件（`--and-widget`），`dialog` 会特殊处理后台任务。在这些小部件关闭（例如 “`OK`”）之前，`dialog` 将在同一进程中执行所有 `tailboxbg` 小部件，轮询更新。你可以使用 tab 在屏幕上的小部件之间遍历，并单独关闭它们，例如按 ENTER。一旦非 `tailboxbg` 小部件关闭，`dialog` 将自身的一个副本分叉到后台，如果给出了 `--no-kill` 选项，则打印其进程 ID。

退出时，不向 `dialog` 的输出写入文本。仅提供 “`EXIT`” 按钮用于输入，但可能返回 ESC 退出状态。

注意：旧版本的 `dialog` 立即分叉并尝试单独更新屏幕。除了性能不佳外，这还不可行。某些旧脚本可能无法与轮询方案一起正常工作。

**`--textbox file height width`**

文本框让你在对话框中显示文本文件的内容。它像一个简单的文本文件查看器。用户可以通过使用大多数键盘上可用的光标、page-up、page-down 和 HOME/END 键在文件中移动。如果行太长而无法在框中显示，可以使用 LEFT/RIGHT 键水平滚动文本区域。你也可以使用 vi 风格键 `h`、`j`、`k` 和 `l` 代替光标键，`B` 或 `N` 代替 page-up 和 page-down 键。使用 vi 风格的 “`k`” 和 “`j`” 或箭头键上下滚动。使用 vi 风格的 “`h`” 和 “`l`” 或箭头键左右滚动。“`0`” 重置左/右滚动。为更方便，还提供了 vi 风格的前向和后向搜索功能。

退出时，不向 `dialog` 的输出写入文本。仅提供 “`EXIT`” 按钮用于输入，但可能返回 ESC 退出状态。

**`--timebox text height [width hour minute second]`**

显示一个对话框，允许你选择小时、分钟和秒。如果小时、分钟或秒的值缺失或为负，使用当前日期的相应值。你可以使用左、上、右和下箭头增减任何值。使用 tab 或 backtab 在窗口之间移动。

退出时，结果以 `hour:minute:second` 形式打印。可以使用 `--time-format` 选项覆盖格式。

**`--treeview text height width list-height [ tag item status depth ] ...`**

显示组织为树的数据。每组数据包含一个标记、为项显示的文本、其状态（“`on`” 或 “`off`”）以及项在树中的深度。

只能选择一个项（类似 radiolist）。标记不显示。

退出时，选中项的标记写入 `dialog` 的输出。

**`--yesno text height width`**

将显示大小为 `height` 行 `width` 列的 yes/no 对话框。`text` 指定的字符串显示在对话框内。如果此字符串太长而无法在一行中容纳，将在适当位置自动分成多行。文本字符串还可以包含子字符串 “`\n`” 或换行符 “`\n`” 以显式控制换行。此对话框对于需要用户回答是或否的问题很有用。对话框有 Yes 按钮和 No 按钮，用户可以通过按 TAB 键在它们之间切换。

退出时，不向 `dialog` 的输出写入文本。除了 “`Yes`” 和 “`No`” 退出码（参见诊断）外，可能返回 ESC 退出状态。

“`Yes`” 和 “`No`” 使用的代码与 “`OK`” 和 “`Cancel`” 使用的代码匹配，内部不做区分。

### 过时选项

**`--beep`** 这曾用于告诉原始 cdialog 在 `tailboxbg` 小部件的单独进程重绘屏幕时应发出蜂鸣声。

**`--beep-after`** 用户通过按其中一个按钮完成小部件后蜂鸣。

### 空格选项

这些选项可用于在 `dialog` 读取脚本时转换空白（空格、制表符、换行符）：

`--cr-wrap`、`--no-collapse`、`--no-nl-expand` 和 `--trim`

这些选项不是独立的：

- `dialog` 检查脚本是否包含至少一个 “`\n`”，并且（除非设置了 `--no-nl-expand`）将忽略 `--no-collapse` 和 `--trim` 选项。
- 检查 “`\n`” 和 `--no-nl-expand` 选项后，`dialog` 处理 `--trim` 选项。

  如果 `--trim` 选项生效，则 `dialog` 忽略 `--no-collapse`。它将制表符、空格（以及换行符，除非设置了 `-cr-wrap`）序列更改为单个空格。

- 如果 “`\n`” 或 `--trim` 情况都不适用，`dialog` 检查 `--no-collapse` 以决定是否将制表符和空格序列减少为单个空格。

  在这种情况下，`dialog` 忽略 `--cr-wrap` 且不修改换行符。

考虑这些依赖关系，这里有一个表格总结了各种选项组合的行为。该表假设未设置 `--no-nl-expand` 选项时脚本包含至少一个 “`\n`”。

| cr-wrap | no-collapse | no-nl-expand | trim | 结果 |
| --- | --- | --- | --- | --- |
| no | no | no | no | 将制表符转换为空格。将换行符转换为空格。将 “`\n`” 转换为换行符。 |
| no | no | no | yes | 将制表符转换为空格。将换行符转换为空格。将 “`\n`” 转换为换行符。 |
| no | no | yes | no | 将制表符转换为空格。不将换行符转换为空格。将多个空格转换为单个。字面显示 “`\n`”。 |
| no | no | yes | yes | 将制表符转换为空格。将多个空格转换为单个。将换行符转换为空格。字面显示 “`\n`”。 |
| no | yes | no | no | 将换行符转换为空格。将 “`\n`” 转换为换行符。 |
| no | yes | no | yes | 将换行符转换为空格。将 “`\n`” 转换为换行符。 |
| no | yes | yes | no | 不将换行符转换为空格。不减少多个空白。字面显示 “`\n`”。 |
| no | yes | yes | yes | 将多个空格转换为单个。将换行符转换为空格。字面显示 “`\n`”。 |
| yes | no | no | no | 将制表符转换为空格。在换行符处换行。将 “`\n`” 转换为换行符。 |
| yes | no | no | yes | 将制表符转换为空格。在换行符处换行。将 “`\n`” 转换为换行符。 |
| yes | no | yes | no | 将制表符转换为空格。不将换行符转换为空格。将多个空格转换为单个。字面显示 “`\n`”。 |
| yes | no | yes | yes | 将制表符转换为空格。将多个空格转换为单个。在换行符处换行。字面显示 “`\n`”。 |
| yes | yes | no | no | 在换行符处换行。将 “`\n`” 转换为换行符。 |
| yes | yes | no | yes | 在换行符处换行。将 “`\n`” 转换为换行符。 |
| yes | yes | yes | no | 不将换行符转换为空格。不减少多个空白。字面显示 “`\n`”。 |
| yes | yes | yes | yes | 将多个空格转换为单个。在换行符处换行。字面显示 “`\n`”。 |

## 运行时配置

1. 通过键入以下命令创建示例配置文件：

```
dialog --create-rc file
```

2. 启动时，`dialog` 按以下方式确定要使用的设置：

   a) 如果设置了环境变量 `DIALOGRC`，其值确定配置文件的名称。

   b) 如果未找到 (a) 中的文件，使用文件 **$HOME/.dialogrc** 作为配置文件。

   c) 如果未找到 (b) 中的文件，尝试使用编译时确定的 GLOBALRC 文件，即 **/etc/dialogrc**。

   d) 如果未找到 (c) 中的文件，使用编译默认值。

3. 编辑示例配置文件并将其复制到 `dialog` 可以找到的位置，如上文步骤 2 所述。

## 键绑定

你可以通过添加到配置文件来覆盖或添加 `dialog` 中的键绑定。`dialog` 的 `bindkey` 命令将单个键映射到其内部编码。

```
bindkey widget curses_key dialog_key
```

小部件名称可以是 “`*`”（所有小部件），或特定小部件如 `textbox`。特定小部件绑定覆盖 “`*`” 绑定。用户定义的绑定覆盖内置绑定。

`curses_key` 可以用不同形式表示：

- 它可以是从 `curses.h` 派生的任何名称，例如 “`HELP`” 来自 `KEY_HELP`。
- `dialog` 还识别 ANSI 控制字符如 “`^A`”、“`^?`”，以及 C1 控制字符如 “`~A`” 和 “`~?`”。
- 最后，`dialog` 允许像 C 中一样的反斜杠转义。这些可以是八进制字符值如 “`\033`”（ASCII 转义字符），或下表中列出的字符：

| 转义 | 实际 |
| --- | --- |
| `\b` | 退格 |
| `\f` | 换页 |
| `\n` | 换行（line feed） |
| `\r` | 回车 |
| `\s` | 空格 |
| `\t` | 制表符 |
| `\^` | “`^`”（插入符号） |
| `\?` | “`?`”（问号） |
| `\\` | “`\`”（反斜杠） |

`dialog` 的内部键码名称对应于 `dlg_keys.h` 中的 `DLG_KEYS_ENUM` 类型，例如 “`HELP`” 来自 `DLGK_HELP`。

### 小部件名称

某些小部件（如 formbox）有一个可编辑字段的区域。这些在小部件的子窗口中管理，并且可能有与主小部件分开的键绑定，因为子窗口使用不同名称注册。

| 小部件 | 窗口名称 | 子窗口名称 |
| --- | --- | --- |
| calendar | calendar | |
| checklist | checklist | |
| editbox | editbox | editbox2 |
| form | formbox | formfield |
| fselect | fselect | fselect2 |
| inputbox | inputbox | inputbox2 |
| menu | menubox | menu |
| msgbox | msgbox | |
| pause | pause | |
| progressbox | progressbox | |
| radiolist | radiolist | |
| tailbox | tailbox | |
| textbox | textbox | searchbox |
| timebox | timebox | |
| yesno | yesno | |

某些小部件实际上是其他小部件，使用内部设置修改行为。这些使用与实际小部件相同的小部件名称：

| 小部件 | 实际小部件 |
| --- | --- |
| dselect | fselect |
| infobox | msgbox |
| inputmenu | menu |
| mixedform | form |
| passwordbox | inputbox |
| passwordform | form |
| prgbox | progressbox |
| programbox | progressbox |
| tailboxbg | tailbox |

### 内置绑定

此手册页未列出每个小部件的键绑定，因为可以通过运行 `dialog` 获取该详细信息。如果设置了 `--trace` 选项，`dialog` 在注册每个小部件时写入其键绑定信息。

### 示例

通常，`dialog` 使用不同的键在按钮之间导航和编辑对话框的一部分，与在编辑部分内导航相比。即，tab（和 back-tab）遍历按钮（或在按钮和编辑部分之间），而箭头键遍历编辑部分内的字段。Tab 还被识别为在小部件之间遍历的特殊情况，例如使用多个 `tailboxbg` 小部件时。

某些用户可能希望使用相同的键在编辑部分内遍历和在按钮之间遍历。form 小部件被编写为通过在 `dlgk_keys.h` 中为 “`form`”（左/右/下一个/上一个）添加特殊组来支持这种键的重新定义。以下是演示如何执行此操作的示例绑定：

```
bindkey formfield TAB form_NEXT
bindkey formbox TAB form_NEXT
bindkey formfield BTAB form_prev
bindkey formbox BTAB form_prev
```

这种重新定义在其他小部件中（例如 calendar）不会有用，因为可能有大量字段要遍历。

## 环境变量

**`DIALOGOPTS`** 定义此变量以将任何通用选项应用于每个小部件。大多数通用选项在处理每个小部件之前重置。如果在此环境变量中设置选项，它们将在重置后应用于 `dialog` 的状态。与 “`--file`” 选项一样，双引号和反斜杠被解释。

“`--file`” 选项不被视为通用选项（因此不能嵌入此环境变量中）。

**`DIALOGRC`** 如果要指定要使用的配置文件的名称，定义此变量。

**`DIALOG_CANCEL`** **`DIALOG_ERROR`** **`DIALOG_ESC`** **`DIALOG_EXTRA`** **`DIALOG_HELP`** **`DIALOG_ITEM_HELP`** **`DIALOG_TIMEOUT`** **`DIALOG_OK`** 定义这些变量中的任何一个以更改退出代码：

- Cancel (1),
- error (-1),
- ESC (255),
- Extra (3),
- Help (2),
- Help with --item-help (2),
- Timeout (5), 或
- OK (0).

通常 shell 脚本无法区分 -1 和 255。

**`DIALOG_TTY`** 将此变量设置为 “`1`” 以提供与旧版本 `dialog` 的兼容性，旧版本假定如果脚本重定向标准输出，则给出了 “`--stdout`” 选项。

## 文件

**$HOME/.dialogrc** 默认配置文件

## 实例

源代码包含几个示例，说明如何使用不同的盒子选项及其外观。只需查看源代码的 `samples/` 目录。

## 诊断

退出状态可能被环境变量覆盖。默认值和可覆盖它们的相应环境变量为：

**`0`** 如果按 YES 或 OK 按钮（`DIALOG_OK`）。

**`1`** 如果按 NO 或 Cancel 按钮（`DIALOG_CANCEL`）。

**`2`** 如果按 **Help** 按钮（`DIALOG_HELP`），除下文关于 `DIALOG_ITEM_HELP` 的说明外。

**`3`** 如果按 **Extra** 按钮（`DIALOG_EXTRA`）。

**`4`** 如果按 **Help** 按钮，并且设置了 `--item-help` 选项，并且 `DIALOG_ITEM_HELP` 环境变量设置为 4。

虽然任何退出代码都可以使用环境变量覆盖，但此特殊情况于 2004 年引入以简化兼容性。`dialog` 内部使用 `DIALOG_ITEM_HELP`(4)，但除非也设置了环境变量，否则它在退出时将其更改为 `DIALOG_HELP`(2)。

**`5`** 如果超时到期且 `DIALOG_TIMEOUT` 变量设置为 5。

**`-1`** 如果 `dialog` 内部发生错误（`DIALOG_ERROR`）或因按 ESC 键（`DIALOG_ESC`）退出。

## 可移植性

`dialog` 与 X/Open curses 一起工作。但是，某些实现有缺陷：

- HPUX curses（可能还有其他）未正确为 `newterm` 函数打开终端。这会干扰 `dialog` 的 `--input-fd` 选项，阻止光标键和类似转义序列被识别。
- NetBSD 5.1 curses 对宽字符的支持不完整。`dialog` 会构建，但并非所有示例都正确显示。

## 兼容性

你可能希望编写与其他 “`clones`” 一起运行的脚本。

### 原始 Dialog

首先，要考虑 “`original`” 程序（版本 0.3 到 0.9）。它有一些拼写错误（或不一致）的选项。该程序将这些已弃用的选项映射到首选选项。它们包括：

| 选项 | 处理 |
| --- | --- |
| `--beep-after` | ignored |
| `--guage` | mapped to `--gauge` |

### Xdialog

这是一个 X 应用程序，而非终端程序。稍加注意，可以编写与 Xdialog 和 `dialog` 都能工作的有用脚本。

`dialog` 程序忽略 Xdialog 识别的这些选项：

| 选项 | 处理 |
| --- | --- |
| `--allow-close` | ignored |
| `--auto-placement` | ignored |
| `--fixed-font` | ignored |
| `--icon` | ignored |
| `--keep-colors` | ignored |
| `--no-close` | ignored |
| `--no-cr-wrap` | ignored |
| `--screen-center` | ignored |
| `--separator` | mapped to `--separate-output` |
| `--smooth` | ignored |
| `--under-mouse` | ignored |
| `--wmclass` | ignored |

Xdialog 的手册页有一节讨论其与 `dialog` 的兼容性。手册页中未显示一些差异。例如，html 文档指出：

注意：以前的 Xdialog 版本使用 “`\n`”（换行符）作为 checklist 小部件的结果分隔符；这在 Xdialog v1.5.0 中已更改为 “`/`” 以使其与 (c)dialog 兼容。在使用 Xdialog checklist 的旧脚本中，你必须在 `--checklist` 之前添加 `--separate-output` 选项。

`dialog` 未使用不同的分隔符；差异可能是由于对某些脚本的混淆。

### Whiptail

然后是 whiptail。出于实用目的，它由 Debian 维护（其上游开发者做的工作很少）。其文档（README.whiptail）声称

```
whiptail(1) is a lightweight replacement for dialog(1), to provide dialog boxes for shell scripts. It is built on the newt windowing library rather than the ncurses library, allowing it to be smaller in embedded environments such as installers, rescue disks, etc. whiptail is designed to be drop-in compatible with dialog, but has less features: some dialog boxes are not implemented, such as tailbox, timebox, calendarbox, etc.
```

比较实际大小（Debian testing，2007/1/10）：whiptail、newt、popt 和 slang 库的总大小为 757 KB。`dialog` 的可比数字（包括 ncurses）为 520 KB。忽略第一段。

第二段具有误导性，因为 whiptail 也不适用于 `dialog` 的通用选项，例如 gauge 框。whiptail 与 `dialog` 的兼容性不如 1990 年代中期的原始 dialog 0.4 程序。

whiptail 的手册页从 `dialog` 借用功能，但奇怪地仅引用到 0.4（1994）版本作为来源。即其手册页指的是从 `dialog` 的更新版本借用的功能，例如：

- `--gauge`（来自 0.5）
- `--passwordbox`（来自 1999 年 Debian 更改）
- `--default-item`（来自 2000/02/22）
- `--output-fd`（来自 2002/08/14）

有点幽默的是，可以注意到使用 “`--`” 作为转义的 popt 功能（在其手册页中未记录）在 `dialog` 的手册页中记录了大约一年后才在 whiptail 的手册页中提到。whiptail 的手册页错误地将其归因于 getopt（并且无论如何都不准确）。

Debian 使用 whiptail 作为官方变体。

`dialog` 程序忽略或映射 whiptail 识别的这些选项：

| 选项 | 处理 |
| --- | --- |
| `--cancel-button` | mapped to `--cancel-label` |
| `--fb` | ignored |
| `--fullbutton` | ignored |
| `--no-button` | mapped to `--no-label` |
| `--nocancel` | mapped to `--no-cancel` |
| `--noitem` | mapped to `--no-items` |
| `--notags` | mapped to `--no-tags` |
| `--ok-button` | mapped to `--ok-label` |
| `--scrolltext` | mapped to `--scrollbar` |
| `--topleft` | mapped to `--begin 0 0` |
| `--yes-button` | mapped to `--yes-label` |

命令行选项未解决的视觉差异：

- `dialog` 将列表在窗口内居中。whiptail 通常将列表置于左边距。
- whiptail 使用尖括号（“`<`” 和 “`>`”）标记按钮。`dialog` 使用方括号。
- whiptail 用竖线标记字幕的限制。`dialog` 不标记限制。
- whiptail 尝试用上/下箭头标记滚动条的顶部/底部单元格。当无法做到这一点时，它用滚动条的背景色填充这些单元格，使用户困惑。`dialog` 使用整个滚动条空间，从而获得更好的分辨率。

## 缺陷

也许。

## 作者

Thomas E. Dickey（0.9b 及更高版本的更新）

## 贡献者

Kiran Cherupally — mixed form 和 mixed gauge 小部件。

Tobias C. Rittweiler

Valery Reznic — form 和 progressbox 小部件。

Yura Kalinichenko 将 gauge 小部件改编为 “`pause`”。

这是早期版本 0.9a 的重写（除了需要提供兼容性外），0.9a 列出的作者为：

- Savio Lam — version 0.3, “`dialog`”
- Stuart Herbert — patch for version 0.4
- Marc Ewing — the gauge widget.
- Pasquale De Marco “`Pako`” — version 0.9a, “`cdialog`”
