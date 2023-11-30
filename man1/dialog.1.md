  DIALOG(1)  

DIALOG(1)

FreeBSD General Commands Manual

DIALOG(1)

[名称](#__u540D___u79F0_)
=======================

dialog - 显示来自 shell 脚本的对话框

[概要](#__u6982___u8981_)
=======================

**dialog --clear**-
**dialog --create-rc** _file_-
**dialog --print-maxsize**-
**dialog** _common-options_ _box-options_

[描述](#__u63CF___u8FF0_)
=======================

**Dialog** 是一个程序，可让您使用 shell 脚本中的对话框提出各种问题或显示消息。实现了这些类型的对话框（尽管并非所有都必须编译成 **dialog**):

**buildlist**, **calendar**, **checklist**, **dselect**, **editbox**, **form**, **fselect**, **gauge**, **infobox**, **inputbox**, **inputmenu**, **menu**, **mixedform**, **mixedgauge**, **msgbox** (message), **passwordbox**, **passwordform**, **pause**, **prgbox**, **programbox**, **progressbox**, **radiolist**, **rangebox**, **tailbox**, **tailboxbg**, **textbox**, **timebox**, **treeview** 和 **yesno** (yes/no)。

您可以将多个对话框放入脚本中：

*   使用 "**\--and-widget**" 标记强制 **dialog** 进入下一个对话框，除非您已按 ESC 取消，或者
*   只需为下一个对话框添加标记，形成一个链。当 Dialog 的返回码不为零时，对话框停止链接，例如，Cancel 或 No（请参阅 DIAGNOSTICS）。

一些小部件，例如清单，会将文本写入对话框的输出。通常这是标准错误，但有一些选项可以改变它： "**\--output-fd**"、 "**\--stderr**" 和 "**\--stdout**"。 如果按下取消按钮（或 ESC），则不会写入任何文本；在这种情况下， **dialog** 会立即退出。

[选项](#__u9009___u9879_)
=======================

所有选项都以 "**\--**" 开头（两个 ASCII 连字符，为了那些使用具有混乱语言环境支持的系统的人的利益）。

"**\--**" 本身用作转义，即命令行上的下一个标记不被视为选项。

**dialog --title -- --Not an option**

"**\--args**" 选项告诉 **dialog** 列出标准错误的命令行参数。这在使用 "**\--**" 和 "**\--file**" 调试复杂脚本时很有用，因为命令行可能会随着它们的扩展而被重写。

"**\--file**" 选项告诉对 **dialog** 从命名为它的值的文件中读取参数。

**dialog --file _parameterfile_**

不在双引号内的空格将被丢弃（使用反斜杠引用单个字符）。结果被插入命令行，替换 "**\--file**" 及其选项值。命令行的解释从那时开始。如果 _parameterfile_ 以 "&" 开头， **dialog** 将以下文本解释为文件描述符编号而不是文件名。

大多数小部件接受 _height_ 和 _width_ 参数，可用于自动调整小部件的大小以适应多行消息 _prompt_ 值：

*   如果参数为负， **dialog** 使用屏幕的大小。
*   如果参数为零，则 **dialog** 使用小部件的最小尺寸来显示 _prompt_ 和数据。
*   否则， **dialog** 使用小部件的给定大小。

[**常用选项**](#_fB__u5E38___u7528___u9009___u9879__fP)
---------------------------------------------------

大多数常用选项在处理每个小部件之前都会被重置。

**\--ascii-lines**

与其在框周围绘制图形线，不如在同一位置绘制 ASCII "+" 和 "-" i。参见 "**\--no-lines**"。

**\--aspect** _ratio_

这使您可以在使用自动调整大小时对框尺寸进行一些控制（将高度和宽度指定为 0）。它代表宽度/高度。默认值为 9，这意味着每 1 行高 9 个字符宽。

**\--backtitle** _backtitle_

指定要在屏幕顶部的背景上显示的 _backtitle_ 。

**\--begin** _y x_

指定对话框左上角在屏幕上的位置。

**\--cancel-label** _string_

覆盖用于 “Cancel” 按钮的标签。

**\--clear**

清除小部件屏幕，仅保留 screen\_color 背景。当您将小部件与 "**\--and-widget**" 结合使用时，可以使用它来擦除屏幕上前一个小部件的内容，这样就不会在下一个小部件的内容下看到它。将此理解为 "**\--keep-window**" 的补充。要比较效果，请使用这些：

所有三个小部件都可见，层叠效果，按 1、2、3 排序：

dialog \\  --begin 2 2 --yesno "" 0 0 \\  --and-widget --begin 4 4 --yesno "" 0 0 \\  --and-widget --begin 6 6 --yesno "" 0 0 

只有最后一个小部件是可见的：

dialog \\  --clear --begin 2 2 --yesno "" 0 0 \\  --and-widget --clear --begin 4 4 --yesno "" 0 0 \\  --and-widget --begin 6 6 --yesno "" 0 0 

所有三个小部件都可见，楼梯效果，顺序 3、2、1：

dialog \\  --keep-window --begin 2 2 --yesno "" 0 0 \\  --and-widget --keep-window --begin 4 4 --yesno "" 0 0 \\  --and-widget --begin 6 6 --yesno "" 0 0 

第一个和第三个小部件可见，楼梯效果，顺序 3,1：

dialog \\  --keep-window --begin 2 2 --yesno "" 0 0 \\  --and-widget --clear --begin 4 4 --yesno "" 0 0 \\  --and-widget --begin 6 6 --yesno "" 0 0 

请注意，如果您想在对话框程序退出后恢复原始控制台颜色并将光标返回原处，请使用 **clear** (1) 命令。

**\--colors**

通过以下字符解释对话框文本中嵌入的 "\\Z" 序列，它告诉 **dialog** 设置颜色或视频属性：

*   0 到 7 是 curses 中使用的 ANSI 颜色编号：分别为黑色、红色、绿色、黄色、蓝色、洋红色、青色和白色。
*   粗体由“b”设置，由“B”重置。
*   反向由'r'设置，由'R'重置。
*   下划线由'u'设置，由'U'重置。
*   设置是累积的，例如， "\\Zb\\Z1" 使以下文本变为粗体（可能是明亮的）红色。
*   使用 "\\Zn" 恢复正常设置。

**\--column-separator** _string_

告诉 **dialog** 在出现给定字符串时拆分单选框/复选框和菜单的数据，并将拆分的数据对齐到列中。

**\--cr-wrap**

将对话框文本中嵌入的换行符解释为屏幕上的换行符。否则， **dialog** 只会在需要适合文本框的地方换行。

即使您可以使用它来控制换行符， **Dialog** 仍然会换行任何对于框的宽度来说太长的行。如果没有 cr-wrap，您的文本布局可能会被格式化为在脚本的源代码中看起来不错，而不会影响它在对话框中的外观。

_cr-wrap_ 功能在以下条件下实施：

*   字符串包含 “\\n” 并且未使用 **\--no-nl-expand** 选项，或者
*   使用 **\--trim** 选项。

有关详细信息，请参阅 **Whitespace 选项**。

**\--create-rc** _file_

当 **dialog** 支持运行时配置时，这可用于将示例配置文件转储到 _file_ 指定的文件中。

**\--date-format** _format_

如果主机提供 **strftime**, 则此选项允许您为 **\--calendar** 小部件指定打印日期的格式。一天中的时间（小时、分钟、秒）是当前本地时间。

**\--defaultno**

将 **yes/no** 框的默认值设为 **No** 。 同样，将提供 “OK” 和 “Cancel” 的小部件的默认按钮设为 _Cancel_。 如果给定了 "**\--nocancel**" 或 "**\--visit-items**" ，这些选项将覆盖此选项，使默认按钮始终为 “Yes” (内部与 “OK” 相同)。

**\--default-button** _string_

在小部件中设置默认（预选）按钮。通过预先选择一个按钮，脚本使用户可以简单地按 _Enter_ 以通过最少的交互来继续对话框。

选项的值是按钮的名称： _ok_, _yes_, _cancel_, _no_, _help_ 或 _extra_。

通常每个小部件中的第一个按钮是默认按钮。显示的第一个按钮由小部件与 "**\--nook**" 和 "**\--nocancel** " 选项一起确定。如果未给出此选项，则没有分配默认按钮。

**\--default-item** _string_

在清单、表单或菜单框中设置默认项目。通常，框中的第一项是默认值。

**\--exit-label** _string_

覆盖用于 “EXIT” 按钮的标签。

**\--extra-button**

在 “OK” 和 “Cancel” 按钮之间显示一个额外的按钮。

**\--extra-label** _string_

覆盖用于 “Extra” 按钮的标签。注意：对于输入菜单小部件，默认为 “Rename”。

**\--help**

将帮助消息打印到标准输出并退出。如果没有给出选项，或者给出了无法识别的选项，也会打印帮助消息。

**\--help-button**

在 “OK” 和 “Cancel” 按钮之后显示帮助按钮，例如，在清单、单选列表和菜单框以及其他具有 “OK” 按钮的小部件中，无论是否使用 “Cancel” 按钮。

退出时，返回状态将指示已按下帮助按钮。 **Dialog** 还会在令牌 “HELP” 之后向其输出写入一条消息：

*   如果还给出了 "**\--item-help**" ，则将写入项目帮助文本。
*   否则，将写入项目的标签（第一个字段）。

您可以使用 **\--help-tags** 选项和/或设置 DIALOG\_ITEM\_HELP 环境变量来修改这些消息和退出状态。

**\--help-label** _string_

覆盖用于 “Help” 按钮的标签。

**\--help-status**

如果选择了帮助按钮，则在项目帮助 “HELP” 信息之后写入清单、单选列表或表单信息。这可用于在处理帮助请求后重建检查表的状态。

**\--help-tags**

修改退出时为 **\--help-button** 编写的消息，使它们始终只是项目的标签。这不会影响退出状态代码。

**\--hfile** _filename_

当用户按下 F1 时，使用文本框显示给定的文件。

**\--hline** _string_

显示在小部件底部居中的给定字符串。

**\--ignore**

忽略 **dialog** 无法识别的选项。无论如何都会忽略一些众所周知的，例如 "**\--icon**" ，但这是与其他实现兼容的更好选择。

**\--input-fd** _fd_

从给定的文件描述符中读取键盘输入。大多数 **dialog** 脚本从标准输入读取，但仪表小部件读取管道（始终是标准输入）。当 **dialog** 尝试重新打开终端时，某些配置无法正常工作。如果您的脚本必须在该类型的环境中工作，请使用此选项（适当地处理文件描述符）。

**\--insecure**

通过为每个字符回显星号，使密码小部件更友好但更不安全。

**\--iso-week**

根据 ISO-8601 设置 "**\--calendar**" 选项中显示的周数的起始点，从第一周开始编号，包括一月的星期四。

**\--item-help**

解释清单、单选清单和菜单框的标签数据，为当前选定的项目添加一个显示在屏幕底部的列。

**\--keep-tite**

当使用 **ncurses** 构建时， **dialog** 通常会检查它是否在 **xterm** 中运行，并且在这种情况下会尝试抑制使其切换到备用屏幕的初始化字符串。在多次运行 **dialog** 的脚本中，在正常屏幕和备用屏幕之间切换会在视觉上分散注意力。使用此选项允许 **dialog** 使用这些初始化字符串。

**\--keep-window**

通常，当 **dialog** 执行通过 "**\--and-widget**" 连接的几个 **tailboxbg** 小部件时，它会通过在旧小部件上绘画来清除屏幕上的旧小部件。使用此选项来禁止重新绘制。

在退出时， **dialog** 会重新绘制所有标记为 "**\--keep-window**" 的小部件，即使它们不是 **tailboxbg** 小部件。这会导致它们以相反的顺序重新绘制。有关示例，请参见 "**\--clear**" 选项的讨论。

**\--last-key**

在退出时，报告用户输入的最后一个键。这是 curses 键码，而不是符号或文字字符。脚本可以使用它来区分绑定到同一操作的两个键。

**\--max-input** _size_

将输入字符串限制为给定大小。如果未指定，则限制为 2048。

**\--no-cancel**

**\--nocancel**

在清单、输入框和菜单框模式下抑制 “Cancel” 按钮。如果用户按下 ESC 键取消退出，脚本仍然可以测试。

**\--no-collapse**

通常， **dialog** 将制表符转换为空格，并将多个空格减少为单个空格，用于显示在消息框等中的文本。使用此选项可禁用该功能。请注意， **dialog** 仍将换行文本，这取决于 "**\--cr-wrap**" 和 "**\--trim**" 选项。

The _no-collapse_ 功能的实施取决于以下条件：

*   字符串包含 “\\n” 并且未使用 **\--no-nl-expand** 选项，或者
*   不使用 **\--trim** 选项。

有关详细信息，请参阅 **Whitespace 选项**。

**\--no-items**

一些小部件 (checklist, inputmenu, radiolist, menu) 显示一个包含两列（ “tag” 和 “item”, 即 “description”)的列表。此选项告诉 **dialog** 读取较短的行，省略列表的 “item” 部分。这有时很有用，例如，如果标签提供了足够的信息。

另请参阅 **\--no-tags** 。如果两个选项都给出，则忽略此选项。

**\--no-kill**

告诉 **dialog** 将 **tailboxbg** 框放在后台，将其进程 ID 打印到 **dialog** 的输出。SIGHUP 对后台进程禁用。

**\--no-label** _string_

覆盖用于 “No” 按钮的标签。

**\--no-lines**

与其在盒子周围画线，不如在同一个地方画空间。另见 "**\--ascii-lines**" 。

**\--no-mouse**

不要启用鼠标。

**\--no-nl-expand**

不要将 message/prompt 文本的 "\\n" 子字符串转换为文字换行符。

仅当字符串包含 “\\n” 时才使用 _no-nl-expand_ 功能，以便有一些东西可以转换。

有关详细信息，请参阅 **Whitespace 选项**。

**\--no-ok**

**\--nook**

在清单、输入框和菜单框模式下抑制 “OK” 按钮。脚本仍然可以测试用户是否按下 “Enter” 键来接受数据。

**\--no-shadow**

抑制将在每个对话框的右侧和底部绘制的阴影。

**\--no-tags**

一些小部件（清单、输入菜单、单选列表、菜单）显示一个包含两列（“ “tag” 和 “description”)的列表。该标签对脚本很有用，但可能对用户没有帮助。 **\--no-tags** 选项（来自 Xdialog）可用于抑制显示中的标签列。与 **\--no-items** 选项不同，这不会影响从脚本中读取的数据。

Xdialog 不显示类似的构建列表和树视图小部件的标签列； **dialog** 也是如此。

通常， **dialog** 允许您通过将单个字符与标记的第一个字符匹配来快速移动到显示列表中的条目。 当给出 **\--no-tags** 选项时， **dialog** 与描述的第一个字符匹配。 在任何一种情况下，可匹配的字符都会突出显示。

**\--ok-label** _string_

覆盖用于 “OK” 按钮的标签。

**\--output-fd** _fd_

直接输出到给定的文件描述符。 大多数 **dialog** 本都会写入标准错误，但也可能会在那里写入错误消息，具体取决于您的脚本。

**\--separator** _string_

**\--output-separator** _string_

指定一个字符串，它将 **dialog** 输出上的输出与清单分开，而不是换行符（用于 **\--separate-output** ）或空格。 这适用于通常使用换行符的其他小部件，例如表单和编辑框。

**\--print-maxsize**

将对话框的最大尺寸（即屏幕尺寸）打印到 **dialog** 的输出。 这可以单独使用，没有其他选项。

**\--print-size**

初始化对话框时，将每个对话框的大小打印到 **dialog** 的输出。

**\--print-text-only** _string \[ height \[ width \] \]_

打印字符串，因为它将被包装在 **dialog** 输出的消息框中。

因为可选的 _height_ 和 _width_ 默认为零，如果省略它们， **dialog** 会根据屏幕尺寸自动调整大小。

**\--print-text-size** _string \[ height \[ width \] \]_

将字符串的大小打印到 **dialog** 的输出中，就像它包装在消息框中一样

height width 

因为可选的 _height_ 和 _width_ 参数默认为零，如果省略它们， **dialog** 会根据屏幕尺寸自动调整大小。

**\--print-version**

将 **dialog** 的版本打印到 **dialog** 的输出。 这可以单独使用，没有其他选项。 它不会导致 **dialog** 自行退出。

**\--quoted**

通常 **dialog** 引用检查表返回的字符串以及项目帮助文本。 使用此选项引用所有字符串结果。

**\--reorder**

默认情况下，构建列表小部件对输出（右）列表使用与输入（左）相同的顺序。 使用此选项告诉 **dialog** 使用用户将选择添加到输出列表的顺序。

**\--scrollbar**

对于拥有一组可滚动数据的小部件，在其右边距上绘制一个滚动条。 这不会响应鼠标。

**\--separate-output**

对于某些小部件（buildlist、checklist、treeview），一次输出一行，不带引号。这有利于另一个程序的解析。

**\--separate-widget** _string_

指定一个字符串，它将对话框的输出与每个小部件分开。这用于简化解析具有多个小部件的对话框的结果。如果未给出此选项，则默认分隔符字符串是制表符。

**\--shadow**

在每个对话框的右侧和底部绘制阴影。

**\--single-quoted**

根据需要使用单引号（如果不需要，则不要使用引号）作为清单和项目帮助文本的输出。如果未设置此选项，则 **dialog** 在每个项目周围使用双引号。 在任何一种情况下， **dialog** 都会添加反斜杠以使输出在 shell 脚本中有用。

**\--size-err**

在尝试使用之前检查对话框的结果大小，如果结果大小大于屏幕，则打印结果大小。（此选项已过时，因为检查了所有新窗口调用）。

**\--sleep** _secs_

处理对话框后休眠（延迟）给定的秒数。

**\--stderr**

直接输出到标准错误。这是默认设置，因为 curses 通常会将屏幕更新写入标准输出。

**\--stdout**

直接输出到标准输出。提供此选项是为了与 Xdialog 兼容，但不建议在可移植脚本中使用它，因为 curses 通常会将其屏幕更新写入标准输出。如果您使用此选项， **dialog** 会尝试重新打开终端，以便它可以写入显示器。 根据平台和您的环境，这可能会失败。

**\--tab-correct**

将每个制表符转换为一个或多个空格（对于 **textbox** 小部件；否则转换为单个空格）。 否则，选项卡将根据 curses 库的解释呈现。 **\--no-collapse** 选项禁用选项卡扩展。

**\--tab-len** _n_

如果给出 "**\--tab-correct**" 选项，则指定制表符占用的空格数。 默认值为 8。此选项仅对 **textbox** 小部件有效。

**\--time-format** _format_

如果主机提供 **strftime**, 则此选项允许您指定为 **\--timebox** 小部件打印的时间格式。 在这种情况下，日、月、年值是针对当前本地时间的。

**\--timeout** _secs_

如果在给定的秒数内没有用户响应，则超时（退出并显示错误代码）。 忽略零秒超时。

"**\--pause**" 小部件忽略此选项。如果后台 "**\--tailboxbg**" 选项用于设置多个并发小部件，它也会被覆盖。

**\--title** _title_

指定要在对话框顶部显示的 _title_ 字符串。

**\--trace** _filename_

将命令行参数、击键和其他信息记录到给定文件中。 如果 **dialog** 读取配置文件，它也会被记录下来。记录到 _gauge_ 小部件的管道输入。使用 control/T 记录当前对话窗口的图片。

**dialog** 程序专门处理一些命令行参数，并在处理它们时将它们从参数列表中删除。例如，如果第一个选项是 **\--trace**, 则在 **dialog** 初始化显示之前对其进行处理（并删除）。

**\--week-start** _day_

设置一周的开始日期，在 "**\--calendar**" 选项中使用。 _day_ 参数可以是

*   一个数字（0 到 6，周日到周六，使用 POSIX）或
*   特殊值 “locale” 这适用于使用 glibc 的系统，为 **locale** 命令提供扩展，即 **first\_weekday** 值）。
*   与 **calendar** 小部件中显示的星期几的缩写之一匹配的字符串，例如， “Mo” 表示 “Monday”。

**\--trim**

消除前导空格，修剪文字换行符和消息文本中的重复空格。

_trim_ 功能在以下条件下实施：

*   字符串不包含 “\\n” 或
*   使用 **\--no-nl-expand** 选项。

有关详细信息，请参阅 **Whitespace 选项**。

另请参阅 "**\--cr-wrap**" 和 "**\--no-collapse**" 选项。

**\--version**

将 **dialog** 的版本打印到标准输出，然后退出。另见 "**\--print-version**"。

**\--visit-items**

修改 checklist、radiolist、menubox 和 inputmenu 的 tab-traversal 以包含项目列表作为状态之一。这作为视觉辅助很有用，即光标位置可以帮助某些用户。

给出此选项时，光标最初放置在列表上。缩写（标签的第一个字母）适用于列表项。如果您选择按钮行，则缩写适用于按钮。

**\--yes-label** _string_

覆盖用于 “Yes” 按钮的标签。

[对话框选项](#__u5BF9___u8BDD___u6846___u9009___u9879_)
--------------------------------------------------

所有对话框都至少有三个参数：

_text_

方框的标题或内容。

_height_

对话框的高度。

_width_

对话框的宽度。

其他参数取决于盒子类型。

**\--buildlist** _text height width list-height_ \[ _tag item status_ \] _..._

**buildlist** 对话框并排显示两个列表。左侧的列表显示未选择的项目。右侧的列表显示所选项目。选择或取消选择项目时，它们会在列表之间移动。

使用回车或 “OK” 按钮接受所选窗口中的当前值并退出。 使用所选窗口中显示的顺序写入结果。

每个条目的初始开/关状态由 _status_ 指定。

该对话框的行为类似于 **menu** ，使用 **\--visit-items** 来控制是否允许光标直接访问列表。

*   如果 **\--visit-items** 没有给出，tab-traversal 使用两种状态（OK/Cancel）。
*   如果给出 **\--visit-items** ，则tab-traversal 使用四种状态（左/右/确定/取消）。

无论是否给出 **\--visit-items** ，都可以使用默认的 "^" （左列）和 "$" （右列）键在两个列表之间移动突出显示。

退出时，打开的那些条目的 _tag_ 字符串列表将打印在 **dialog** 的输出中。

如果未给出 "**\--separate-output**" 选项，则将根据需要引用字符串，以使脚本可以简单地分隔它们。默认情况下，这使用双引号。请参阅修改引用行为的 "**\--single-quoted**" 选项。

**\--calendar** _text height width day month year_

**calendar** 框在可单独调节的窗口中显示月、日和年。如果日、月或年的值缺失或为负，则使用当前日期的对应值。您可以使用左箭头、上箭头、右箭头和下箭头来增加或减少其中的任何一个。使用 vi 风格的 h、j、k 和 l 来移动一个月中的天数数组。使用 tab 或 backtab 在窗口之间移动。如果年份为零，则使用当前日期作为初始值。

退出时，日期以日/月/年的形式打印。 可以使用 **\--date-format** 选项覆盖格式。

**\--checklist** _text height width list-height_ \[ _tag item status_ \] _..._

**checklist** 框类似于 **menu** 框。有多个条目以菜单的形式呈现。另一个区别是您可以通过将其 _status_ 设置为 _on_ 来指示当前选择了哪个条目。用户可以打开或关闭每个条目，而不是从条目中选择一个条目。每个条目的初始开/关状态由 _status_ 指定。

退出时，打开的那些条目的 _tag_ 字符串列表将打印在 **dialog** 的输出中。

如果未给出 "**\--separate-output**" 选项，则将根据需要引用字符串，以使脚本可以简单地分隔它们。默认情况下，这使用双引号。 请参阅修改引用行为的 "**\--single-quoted**" 选项。

**\--dselect** _filepath height width_

目录选择对话框显示一个文本输入窗口，您可以在其中键入一个目录，在该窗口上方还有一个带有目录名称的窗口。

这里的 **filepath** 可以是一个文件路径，在这种情况下，目录窗口将显示路径的内容，而文本输入窗口将包含预选的目录。

使用制表键或箭头键在窗口之间移动。在目录窗口中，使用向上/向下箭头键滚动当前选择。使用空格键将当前选择复制到文本输入窗口中。

键入任何可打印字符会将焦点切换到文本输入窗口，输入该字符并将目录窗口滚动到最接近的匹配项。

使用回车或 “OK” 按钮接受文本输入窗口中的当前值并退出。

退出时，文本输入窗口的内容被写入 **dialog** 的输出。

**\--editbox** _filepath height width_

编辑框对话框显示文件的副本。您可以使用 _backspace_、 _delete_ 和光标键对其进行编辑，以纠正打字错误。它还可以识别 pageup/pagedown。与 **\--inputbox** 不同，您必须按 Tab 键选择 “OK” 或 “Cancel” 按钮才能关闭对话框。在框中按 “Enter” 键将拆分相应的行。

退出时，编辑窗口的内容被写入 **dialog** 的输出。

**\--form** _text height width formheight_ \[ _label y x item y x flen ilen_ \] _..._

**form** 对话框显示由标签和字段组成的表单，这些标签和字段通过脚本中给定的坐标定位在可滚动窗口上。字段长度 _flen_ 和输入长度 _ilen_ 表示字段可以有多长。前者定义了为选定字段显示的长度，而后者定义了在该字段中输入的数据的允许长度。

*   如果 _flen_ 为零，则不能更改相应的字段。字段的内容决定了显示的长度。
*   如果 _flen_ 为负数，则对应的字段不能改变，取 _flen_ 的负值作为显示长度。
*   如果 _ilen_ 为零，则设置为 _flen_。

使用向上/向下箭头（或 control/N、control/P）在字段之间移动。使用选项卡在窗口之间移动。

退出时，表单字段的内容被写入 **dialog** 的输出，每个字段由换行符分隔。 用于填充不可编辑字段（ _flen_ 为零或负数）的文本不会被写出。

**\--fselect** _filepath height width_

The **fselect** （文件选择）对话框显示一个文本输入窗口，您可以在其中键入文件名（或目录），在这两个窗口上方有目录名和文件名。

这里的 **filepath** 可以是一个文件路径，在这种情况下，文件和目录窗口将显示路径的内容，而文本输入窗口将包含预选的文件名。

使用制表键或箭头键在窗口之间移动。在目录或文件名窗口中，使用向上/向下箭头键滚动当前选择。使用空格键将当前选择复制到文本输入窗口中。

键入任何可打印字符会将焦点切换到文本输入窗口，输入该字符并将目录和文件名窗口滚动到最接近的匹配。

键入空格字符会强制 **dialog** 完成当前名称（直到可能与多个条目匹配）。

使用回车或 “OK” 按钮接受文本输入窗口中的当前值并退出。

退出时，文本输入窗口的内容被写入 **dialog** 的输出。

**\--gauge** _text height width \[percent\]_

**gauge** 框在框的底部显示一个仪表。仪表显示百分比。从标准输入读取新的百分比，每行一个整数。仪表会更新以反映每个新的百分比。如果标准输入读取字符串 “XXX” ，那么后面的第一行作为一个整数百分比，然后到另一个 “XXX” 的后续行用于新的提示。当标准输入达到 EOF 时，仪表退出。

_percent_ 值表示仪表中显示的初始百分比。如果未指定，则为零。

退出时，不会将任何文本写 **dialog** 的输出。 小部件不接受任何输入，因此退出状态始终为 OK。

**\--infobox** _text height width_

**info** 框基本上是一个 **message** 框。 但是，在这种情况下， **dialog** 将在向用户显示消息后立即退出。 **dialog** 退出时屏幕不会被清除，因此消息将一直保留在屏幕上，直到稍后调用 shell 脚本将其清除。当您想要通知用户正在进行的某些操作可能需要一些时间才能完成时，这很有用。

退出时，不会将任何文本写入 **dialog** 的输出。返回 OK 退出状态。

**\--inputbox** _text height width \[init\]_

当您要提出要求用户输入字符串作为答案的问题时， **input** 很有用。 如果提供了 init，则它用于初始化输入字符串。 输入字符串时，可以使用 _backspace_、 _delete_ 和光标键来纠正输入错误。如果输入字符串的长度超出了对话框可以容纳的长度，则输入字段将被滚动。

退出时，输入字符串将打印在 **dialog** 的输出中。

**\--inputmenu** _text height width menu-height_ \[ _tag item_ \] _..._

**inputmenu** 框与普通 **menu** 框非常相似。它们之间只有几个区别：

1.

条目不会自动居中，而是会进行左调整。

2.

一个额外的按钮（称为 _Rename_) 暗示在按下时重命名当前项目。

3.

可以通过按 _Rename_ 按钮来重命名当前条目。然后 **dialog** 将在 **dialog** 的输出中写入以下内容。

RENAMED <tag> <item>

**\--menu** _text height width menu-height_ \[ _tag item_ \] _..._

顾名思义， **menu** 框就是一个对话框，可以用来以菜单的形式呈现一个选项列表供用户选择。 选项按给定顺序显示。每个菜单条目由一个 _tag_ 字符串和一个 _item_ 字符串组成。 该 _tag_ 为条目提供了一个名称，以将其与菜单中的其他条目区分开来。该 _item_ 是该条目所代表的选项的简短描述。 用户可以通过按光标键、 _tag_ 的第一个字母作为热键或数字键 _1_ 到 _9_ 在菜单条目之间移动。 菜单中一次显示 _menu-height_ 条目，但如果条目多于该条目，菜单将滚动。

退出时，所选菜单条目的 _tag_ 将打印在 **dialog** 的输出中。 如果给出 "**\--help-button**" 选项，如果用户选择帮助按钮，将打印相应的帮助文本。

**\--mixedform** _text height width formheight_ \[ _label y x item y x flen ilen itype_ \] _..._

**mixedform** 对话框显示一个由标签和字段组成的表单，很像 **\--form** 对话框。它的不同之处在于在每个字段的描述中添加了一个字段类型参数。类型中的每个位表示字段的一个属性：

1

隐藏，例如密码字段。

2

只读，例如标签。

**\--mixedgauge** _text height width percent_ \[ _tag1 item1_ \] _..._

**mixedgauge** 框在框的底部显示一个仪表。仪表显示百分比。

它还在框的顶部显示 _tag_\- 和 _item_\-值的列表。 有关标签值，请参见 dialog(3) 。

_text_ 显示为列表和仪表之间的标题。 _percent_ 值表示仪表中显示的初始百分比。

没有像 **\--gauge** 那样从标准输入读取数据。

退出时，不会将任何文本写入 **dialog** 的输出。小部件不接受任何输入，因此退出状态始终为 OK。

**\--msgbox** _text height width_

**message** 框与 **yes/no** 框非常相似。 **message** 框和 **yes/no** 框之间的唯一区别是 **message** 框只有一个 **OK** 按钮。 您可以使用此对话框显示您喜欢的任何消息。阅读完消息后，用户可以按 _ENTER_ 键，这样 **dialog** 就会退出，调用的 shell 脚本可以继续运行。

如果消息对于空间来说太大， **dialog** 可能允许您滚动它，前提是底层的 curses 实现足够强大。在这种情况下，百分比显示在小部件的底部。

退出时，不会将任何文本写入 **dialog** 的输出。仅提供 “OK” 按钮用于输入，但可能返回ESC退出状态。

**\--pause** _text height width seconds_

**pause** 框在框的底部显示一个仪表。仪表指示距离暂停结束还剩多少秒。当达到超时或用户按下 OK 按钮（状态 OK）或用户按下 CANCEL 按钮或 Esc 键时，暂停退出。

**\--passwordbox** _text height width \[init\]_

**password** 框类似于输入框，只是不显示用户输入的文本。这在提示输入密码或其他敏感信息时很有用。请注意，如果在 “init” 中传递了任何内容，它将在系统的进程表中对临时窥探者可见。此外，为用户提供他们看不到的默认密码也会让用户感到非常困惑。由于这些原因，强烈建议不要使用 “init” 。 如果您不关心密码，请参阅 "**\--insecure**" 。

退出时，输入字符串将打印在对话框的输出中。

**\--passwordform** _text height width formheight_ \[ _label y x item y x flen ilen_ \] _..._

这与 **\--form** 相同，只是所有文本字段都被视为 **password** 小部件而不是 **inputbox** 小部件。

**\--prgbox** _text command height width_

**\--prgbox** _command height width_

**prgbox** 与 **programbox** 框非常相似。

此对话框用于显示指定为 **prgbox** 参数的命令的输出。

命令完成后，用户可以按 _ENTER_ 键，这样 **dialog** 就会退出，调用的 shell 脚本可以继续运行。

如果给出三个参数，它会在标题下显示文本，从滚动文件的内容中划定。如果仅给出两个参数，则省略此文本。

**\--programbox** _text height width_

**\--programbox** _height width_

**programbox** 框与 **progressbox** 框非常相似。 **program** 框和 **progress** 框的唯一区别是 **program** 框显示一个 **OK** 按钮（但仅在命令完成后）。

此对话框用于显示命令的管道输出。命令完成后，用户可以按 _ENTER_ 键，这样 **dialog** 就会退出，调用的 shell 脚本可以继续运行。

如果给出三个参数，它会在标题下显示文本，从滚动文件的内容中划定。 如果仅给出两个参数，则省略此文本。

**\--progressbox** _text height width_

**\--progressbox** _height width_

**progressbox** 框类似于 **tailbox** 框，不同之处在于

a) 而不是显示文件的内容，它显示命令的管道输出和

b) 到达文件末尾时将退出（没有 “OK” 按钮）。

如果给出三个参数，它会在标题下显示文本，从滚动文件的内容中划定。如果仅给出两个参数，则省略此文本。

**\--radiolist** _text height width list-height_ \[ _tag item status_ \] _..._

**radiolist** 框类似于 **menu** 框。 唯一的区别是您可以通过将其 _status_ 设置为 _on_ 来指示当前选择了哪个条目。

退出时，所选项目的标签将写入 **dialog** 的输出。

**\--tailbox** _file height width_

在对话框中显示文件中的文本，如 "tail -f" 命令。使用 vi 风格的“h”和“l”或箭头键向左/向右滚动。'0' 重置滚动。

退出时，不会将任何文本写入 **dialog** 的输出。 仅提供 “OK” 按钮用于输入，但可能返回ESC退出状态。

**\--rangebox** _text height width min-value max-value default-value_

允许用户从一系列值中进行选择，例如，使用滑块。该对话框将当前值显示为条形（如仪表对话框）。制表符或箭头键在按钮和值之间移动光标。当光标位于该值上时，您可以通过以下方式对其进行编辑：

左/右光标移动以选择要修改的数字

+/-

将数字递增/递减一位的字符

0 到 9

将数字设置为给定值

在所有光标位置也可以识别一些键：

home/end

将值设置为其最大值或最小值

pageup/pagedown

增加值，使滑块移动一列

**\--tailboxbg** _file height width_

在对话框中显示文件中的文本作为后台任务，如 "tail -f &" 命令。使用 vi 风格的“h”和“l”或箭头键向左/向右滚动。'0' 重置滚动。

Dialog 如果屏幕上同时存在其他小部件 (**\--and-widget**) ，则 Dialog 会特别处理后台任务。 直到这些小部件关闭（例如， “OK”), **dialog** 将在同一进程中执行所有 tailboxbg 小部件，轮询更新。 您可以使用选项卡在屏幕上的小部件之间遍历，并单独关闭它们，例如，按 _ENTER_ 。 关闭非 tailboxbg 小部件后， **dialog** 会将自身的副本分叉到后台，如果给出 "**\--no-kill**" 选项，则打印其进程ID。

退出时，不会将任何文本写入 **dialog** 的输出。仅提供 “EXIT” 按钮用于输入，但可能返回ESC退出状态。

注意：旧版本的 **dialog** 立即分叉并尝试单独更新屏幕。除了不利于性能之外，它是行不通的。一些较旧的脚本可能无法与轮询方案一起正常工作。

**\--textbox** _file height width_

**text** 框允许您在对话框中显示文本文件的内容。它就像一个简单的文本文件查看器。用户可以使用大多数键盘上可用的光标、向上翻页、向下翻页和 _HOME/END_ 键在文件中移动。如果行太长而无法显示在框中，可以使用 _LEFT/RIGHT_ 键水平滚动文本区域。您也可以使用 vi 风格的键 h、j、k 和 l 代替光标键，并使用 B 或 N 代替上翻页和下翻页键。使用 vi 风格的 “k” 和 “j” 或箭头键向上/向下滚动。 使用 vi 风格的 “h” 和 “l” 或箭头键向左/向右滚动。

退出时，不会将任何文本写入 **dialog** 的输出。 仅提供 “EXIT” 按钮用于输入，但可能返回ESC退出状态。

**\--timebox** _text height \[width hour minute second\]_

将显示一个对话框，允许您选择小时、分钟和秒。如果小时、分钟或秒的值缺失或为负，则使用当前日期的对应值。您可以使用左箭头、上箭头、右箭头和下箭头增加或减少其中的任何一个。使用 tab 或 backtab 在窗口之间移动。

退出时，结果以小时：分钟：秒的形式打印。可以使用 **\--time-format** 选项覆盖格式。

**\--treeview** _text height width list-height_ \[ _tag item status depth_ \] _..._

显示组织为树的数据。每组数据包含一个标签、要为项目显示的文本、其状态 (“on” 或 “off”) 以及项目在树中的深度。

只能选择一项（如 **radiolist**)。 不显示标签。

退出时，所选项目的标签将写入 **dialog** 的输出。

**\--yesno** _text height width_

将显示大小 _height_ 行按 _width_ 列的 **yes/no** 对话框。 _text_ 指定的字符串显示在对话框内。如果这个字符串太长而不能放在一行中，它会在适当的地方自动分成多行。 _text_ 字符串还可以包含子字符串 "_\\n_" 或换行符 \`_\\n_' 以显式控制换行。 此对话框对于询问需要用户回答是或否的问题很有用。该对话框有一个 **Yes** 按钮和一个 **No** 按钮，用户可以通过按 _TAB_ 键在其中切换。

退出时，不会将任何文本写入 **dialog** 的输出。除了 “Yes” 和 “No” 退出代码（参见诊断）之外，还可能返回 ESC 退出状态。

用于 “Yes” 和 “No” 的代码与用于 “OK” 和 “Cancel” 的代码相匹配，内部没有区别。

[过时选项](#__u8FC7___u65F6___u9009___u9879_)
-----------------------------------------

**\--beep**

这用于告诉原始 cdialog 当 tailboxbg 小部件的单独进程重新绘制屏幕时它应该发出哔声。

**\--beep-after**

在用户通过按下其中一个按钮完成小部件后发出哔声。

[空白选项](#__u7A7A___u767D___u9009___u9879_)
-----------------------------------------

这些选项可用于在对话框读取脚本时转换空格（空格、制表符、换行符）：

**\--cr-wrap**, **\--no-collapse**, **\--no-nl-expand**, and **\--trim**

选项不是独立的：

*   **Dialog** 检查脚本是否包含至少一个 “\\n” 并且（除非设置了 **\--no-nl-expand** ）将忽略 **\--no-collapse** 和 **\--trim** 选项。
*   在检查 “\\n” 和 **\--no-nl-expand** 选项后， **dialog** 处理 **\--trim** 选项。

如果 **\--trim** 选项生效，则对话框忽略 **dialog** ignores **\--no-collapse** 。 它将制表符、空格（和换行符，除非设置了 **\-cr-wrap** ）的序列更改为单个空格。

•

如果 “\\n” 或 **\--trim** 情况都不适用， **dialog** 会检查 **\--no-collapse** 以决定是否将制表符和空格的序列减少到单个空格。

在这种情况下， **dialog** 会忽略 **\-cr-wrap** 并且不会修改换行符。

考虑到这些依赖关系，下表总结了各种选项组合的行为。 该表假定当未设置 **\--no-nl-expand** 选项时脚本至少包含一个 “\\n” 。

cr-

no-

no-

trim

Result

wrap

collapse

nl-expand

no

no

no

no

将制表符转换为空格。将换行符转换为空格。将 “\\n” 转换为换行符。

no

no

no

yes

将制表符转换为空格。将换行符转换为空格。将 “\\n” 转换为换行符。

no

no

yes

no

将制表符转换为空格。不要将换行符转换为空格。将多空间转换为单空间。按字面意思显示 “\\n” 。

no

no

yes

yes

将制表符转换为空格。将多空间转换为单空间。将换行符转换为空格。按字面意思显示 “\\n” 。

no

yes

no

no

将换行符转换为空格。将 “\\n” 转换为换行符。

no

yes

no

yes

将换行符转换为空格。将 “\\n” 转换为换行符。

no

yes

yes

no

不要将换行符转换为空格。不要减少多个空白。按字面意思显示 “\\n” 。

no

yes

yes

yes

将多个空格转换为单个空格。将换行符转换为空格。按字面意思显示 “\\n” 。

yes

no

no

no

将制表符转换为空格。换行。将 “\\n” 转换为换行符。

yes

no

no

yes

将制表符转换为空格。换行。将 “\\n” 转换为换行符。

yes

no

yes

no

将制表符转换为空格。不要将换行符转换为空格。将多空间转换为单空间。按字面意思显示 “\\n” 。

yes

no

yes

yes

将制表符转换为空格。将多空间转换为单空间。换行。按字面意思显示 “\\n” 。

yes

yes

no

no

换行换行。将 “\\n” 转换为换行符。

yes

yes

no

yes

换行符换行。将 “\\n” 转换为换行符。

yes

yes

yes

no

不要将换行符转换为空格。不要减少多个空白。按字面意思显示 “\\n” 。

yes

yes

yes

yes

将多个空格转换为单个空格。换行。按字面意思显示 “\\n” 。

[运行时配置](#__u8FD0___u884C___u65F6___u914D___u7F6E_)
==================================================

1.

通过键入以下内容创建示例配置文件：

dialog --create-rc _file_ 

2.

开始时， **dialog** 确定要使用的设置，如下所示：

a)

如果设置了环境变量 **DIALOGRC** ，它的值决定了配置文件的名称。

b)

如果没有找到 (a) 中的文件，则使用文件 _$HOME/.dialogrc_ 作为配置文件。

c)

如果没有找到 (b) 中的文件，请尝试使用在编译时确定的 GLOBALRC 文件，即 _/etc/dialogrc_。

d)

如果 (c) 中的文件未找到，则使用默认编译。

3.

编辑示例配置文件并将其复制到 **dialog** 可以找到的某个位置，如上面的步骤 2 所述。

[关键绑定](#__u5173___u952E___u7ED1___u5B9A_)
=========================================

您可以通过添加到配置文件来覆盖或添加到 **dialog** 中的键绑定。 **Dialog** 的 **bindkey** 命令将单个键映射到其内部编码。

bindkey _widget_ _curses\_key_ _dialog\_key_ 

_widget_ 名称可以是 "\*" （所有小部件）或特定小部件，例如 **textbox** 。 特定的小部件绑定会覆盖 "\*" 绑定。 用户定义的绑定会覆盖内置绑定。

_curses\_key_ 可以是从 **curses.h** 派生的任何名称，例如 “HELP” 中的 “KEY\_HELP”。 **Dialog** 还可以识别 ANSI 控制字符，例如 "^A", "^?", 以及 C1 控件，例如 "~A" 和 "~?"。 最后，它允许使用反斜杠转义任何单个字符。

**Dialog** 的内部键码名称对应于 **dlg\_keys.h** 中的 **DLG\_KEYS\_ENUM** 类型，例如 “DLGK\_HELP” 中的 “HELP” 。

[小部件名称](#__u5C0F___u90E8___u4EF6___u540D___u79F0_)
--------------------------------------------------

一些小部件（例如表单框）有一个可以编辑字段的区域。这些在小部件的子窗口中进行管理，并且可能具有与主小部件不同的键绑定，因为子窗口使用不同的名称注册。

小部件

窗口名称

子窗口名称

calendar

calendar

checklist

checklist

editbox

editbox

editbox2

form

formbox

formfield

fselect

fselect

fselect2

inputbox

inputbox

inputbox2

menu

menubox

menu

msgbox

msgbox

pause

pause

progressbox

progressbox

radiolist

radiolist

tailbox

tailbox

textbox

textbox

searchbox

timebox

timebox

yesno

yesno

一些小部件实际上是其他小部件，使用内部设置来修改行为。那些使用与实际小部件相同的小部件名称：

Widget

Actual Widget

dselect

fselect

infobox

msgbox

inputmenu

menu

mixedform

form

passwordbox

inputbox

passwordform

form

prgbox

progressbox

programbox

progressbox

tailboxbg

tailbox

[内置绑定](#__u5185___u7F6E___u7ED1___u5B9A_)
-----------------------------------------

本手册页没有列出每个小部件的键绑定，因为可以通过运行 **dialog** 获得详细信息。 如果您设置了 **\--trace** 选项， **dialog** 会在注册时为每个小部件写入键绑定信息。

[实例](#__u5B9E___u4F8B_)
-----------------------

通常， **dialog** 使用不同的键在按钮和对话框的编辑部分之间导航，而不是在编辑部分中导航。也就是说，标签（和后退标签）遍历按钮（或按钮和编辑部分之间），而箭头键遍历编辑部分内的字段。选项卡也被认为是在小部件之间遍历的一种特殊情况，例如，当使用多个 tailboxbg 小部件时。

一些用户可能希望使用相同的键在编辑部分中遍历与在按钮之间遍历。 通过在 **dlgk\_keys.h** 中为 “form” （左/右/下一个/上一个）添加一个特殊组，表单小部件被编写为支持这种键的重新定义。这是一个示例绑定，演示了如何执行此操作：

bindkey formfield TAB form\_NEXT bindkey formbox TAB form\_NEXT bindkey formfield BTAB form\_prev bindkey formbox BTAB form\_prev 

由于潜在的大量字段要遍历，这种类型的重新定义在其他小部件（例如日历）中不会有用。

[环境](#__u73AF___u5883_)
=======================

**DIALOGOPTS**

定义此变量以将任何常用选项应用于每个小部件。大多数常用选项在处理每个小部件之前都会被重置。如果您在此环境变量中设置选项，它们将在重置后应用于 **dialog** 的状态。 与 "**\--file**" 选项一样，双引号和反斜杠被解释。

"**\--file**" 选项不被视为常用选项（因此您不能将其嵌入此环境变量中）。

**DIALOGRC**

如果要指定要使用的配置文件的名称，请定义此变量。

**DIALOG\_CANCEL**

**DIALOG\_ERROR**

**DIALOG\_ESC**

**DIALOG\_EXTRA**

**DIALOG\_HELP**

**DIALOG\_ITEM\_HELP**

**DIALOG\_OK**

定义这些变量中的任何一个以更改退出代码 Cancel (1), error (-1), ESC (255), Extra (3), Help (2), Help with **\--item-help** (2), 或 OK (0)。 通常 shell 脚本无法区分 -1 和 255 。

**DIALOG\_TTY**

将此变量设置为 “1” 以提供与旧版本 **dialog** 的兼容性，该版本假定如果脚本重定向标准输出，则给出 "**\--stdout**" 选项。

[文件](#__u6587___u4EF6_)
=======================

_$HOME/.dialogrc_

默认配置文件

[实例](#__u5B9E___u4F8B__2)
=========================

**dialog** 源包含几个示例，说明如何使用不同的框选项以及它们的外观。 只需查看源的目录 **samples/** 即可。

[诊断](#__u8BCA___u65AD_)
=======================

退出状态会被环境变量覆盖。可以覆盖它们的默认值和相应的环境变量是：

0

如果按下 **YES** 或 **OK** 按钮 (DIALOG\_OK)。

1

如果按下 **No** 或 **Cancel** 按钮 (DIALOG\_CANCEL)。

2

如果按下 **Help** 按钮 (DIALOG\_HELP)，-
除了下面关于 DIALOG\_ITEM\_HELP 的说明。

3

如果按下 **Extra** 按钮 (DIALOG\_EXTRA)。

4

如果按下 **Help** 按钮，并设置了-
**\--item-help** 选项-
并且 DIALOG\_ITEM\_HELP 环境变量设置为 4。

虽然可以使用环境变量覆盖任何退出代码，但这种特殊情况是在 2004 年引入的，以简化兼容性。 **Dialog** 在内部使用 DIALOG\_ITEM\_HELP(4)，但除非还设置了环境变量，否则它会在退出时将其更改为 DIALOG\_HELP(2)。

\-1

如果 **dialog** 内部发生错误 (DIALOG\_ERROR) 或 **dialog** 因按下 _ESC_ 键 (DIALOG\_ESC) 而退出。

[可移植性](#__u53EF___u79FB___u690D___u6027_)
=========================================

**Dialog** 适用于 X/Open 诅咒。但是，一些实现存在不足：

*   HPUX 诅咒（可能还有其他诅咒）无法为 _newterm_ 功能正确打开终端。 通过阻止光标键和类似的转义序列被识别，这会干扰 **dialog** 的 **\--input-fd** 选项。
*   NetBSD 5.1 curses 对宽字符的支持不完全。 **dialog** 将生成，但并非所有示例都正确显示。

[兼容性](#__u517C___u5BB9___u6027_)
================================

您可能想要编写与其他 **dialog** “clones” 一起运行的脚本。

[原始对话框](#__u539F___u59CB___u5BF9___u8BDD___u6846_)
--------------------------------------------------

首先，要考虑 “original” **dialog** 程序（版本 0.3 到 0.9）。 它有一些拼写错误（或不一致）的选项。 **dialog** 程序将那些不推荐使用的选项映射到首选选项。它们包括：

选项

处理

**\--beep-after**

ignored

**\--guage**

mapped to **\--gauge**

[Xdialog](#Xdialog)
-------------------

这是一个 X 应用程序，而不是一个终端程序。稍加注意，就可以编写与 **Xdialog** 和 **dialog** 一起使用的有用脚本。

**dialog** 程序会忽略 **Xdialog** 识别的这些选项：

选项

处理

**\--allow-close**

ignored

**\--auto-placement**

ignored

**\--fixed-font**

ignored

**\--icon**

ignored

**\--keep-colors**

ignored

**\--no-close**

ignored

**\--no-cr-wrap**

ignored

**\--screen-center**

ignored

**\--separator**

mapped to **\--separate-output**

**\--smooth**

ignored

**\--under-mouse**

ignored

**\--wmclass**

ignored

**Xdialog** 的手册页有一节讨论它与 **dialog** 的兼容性。手册页中未显示一些差异。例如，html 文档状态

注意：以前的 Xdialog 版本使用 "\\n" （换行符）作为清单小部件的结果分隔符；这已在 Xdialog v1.5.0 中更改为 "/" 以使其与 (c)dialog 兼容。 在您使用 Xdialog 清单的旧脚本中，您必须在 **\--separate-output** 之一之前添加 **\--checklist** 选项。

**Dialog** 没有使用不同的分隔符；差异可能是由于对某些脚本的混淆。

[Whiptail](#Whiptail)
---------------------

然后是 **whiptail** 。 出于实际目的，它由 Debian 维护（其上游开发人员完成的工作很少）。 它的文档（README.whiptail）声称

Whittail(1) 是 dialog(1), 的轻量级替代品，为 shell 脚本提供对话框。 它建立在 newt 窗口库而不是 ncurses 库，允许它在嵌入式环境中更小，例如安装程序，救援盘等 Whiptail 被设计为与对话兼容，但是功能较少：一些对话框没有实现，例如 如tailbox、timebox、calendarbox等。 

比较实际大小（Debian 测试，2007/1/10）： **whiptail**、 newt、 popt and slang 库的总大小为 757 KB。 **dialog** 的可比数字（计算 ncurses）为 520 KB。无视第一段。

第二段具有误导性，因为 **whiptail** 也不适用于 **dialog** 的常见选项，例如 gauge 框。 与 1990 年代中期最初的 dialog 0.4 程序相比， **whiptail** 与 **dialog** 的兼容性较差。

**whiptail** 的手册页借鉴了 **dialog** 的功能，例如，但奇怪的是仅引用了 0.4（1994）以下的 **dialog** 版本作为来源。也就是说，它的手册页指的是从较新版本的 **dialog** 中借用的功能，例如，

*   **\--gauge** (从 0.5 开始)
*   **\--passwordbox** (来自 Debian 1999 年的更改),
*   **\--default-item** (来自 **dialog** 2000/02/22),
*   **\--output-fd** (来自 **dialog** 2002/08/14)。

有点幽默的是，有人可能会注意到使用 "--" 作为转义符的 **popt** 功能（未在其联机帮助页中记录）在 **dialog** 的联机帮助页中记录了大约一年，然后才在 **whiptail** 的联机帮助页中被提及。 **whiptail** 的联机帮助页错误地将其归因于 **getopt** 并且无论如何都不准确）。

Debian 使用 **whiptail** 作为官方 **dialog** 变体。

**dialog** 程序会忽略或映射这些被 **whiptail** 识别的选项：

选项

处理

**\--cancel-button**

映射到 **\--cancel-label**

**\--fb**

忽略

**\--fullbutton**

忽略

**\--no-button**

映射到 **\--no-label**

**\--nocancel**

映射到 **\--no-cancel**

**\--noitem**

映射到 **\--no-items**

**\--notags**

映射到 **\--no-tags**

**\--ok-button**

映射到 **\--ok-label**

**\--scrolltext**

映射到 **\--scrollbar**

**\--topleft**

映射到 **\--begin 0 0**

**\--yes-button**

映射到 **\--yes-label**

存在命令行选项未解决的视觉差异：

*   窗口内的 **dialog** 中心列表。 **whiptail** 通常将列表放在左边距。
*   **whiptail** 使用尖括号 ("<" 和 ">") 来标记按钮。 **dialog** 框使用方括号。
*   **whiptail** 用竖线标记了字幕的限制。 **dialog** 不标记限制。
*   **whiptail** 尝试使用向上/向下箭头标记滚动条的顶部/底部单元格。 当它无法做到这一点时，它会用滚动条的背景颜色填充这些单元格并让用户感到困惑。 **dialog** 使用整个滚动条空间，从而获得更好的分辨率。

[缺陷](#__u7F3A___u9677_)
=======================

也许。

[作者](#__u4F5C___u8005_)
=======================

Thomas E. Dickey (0.9b 及更高版本的更新)

[贡献者](#__u8D21___u732E___u8005_)
================================

Kiran Cherupally – 混合形式和混合仪表小部件。

Tobias C. Rittweiler

Valery Reznic – 表单和进度框小部件。

Yura Kalinichenko 将仪表小部件改编为 “pause”。

这是 **dialog 0.9a** 早期版本的重写（除非需要提供兼容性），其中列出了作者：

*   Savio Lam – 0.3 版， “dialog”
*   Stuart Herbert – 0.4 版补丁
*   Marc Ewing – 仪表小部件。
*   Pasquale De Marco “Pako” – 0.9a 版， “cdialog”

$Date: 2018/06/19 00:26:13 $