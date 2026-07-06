# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 仓库概览

这是 FreeBSD man 手册的中文翻译项目。基于 GitBook 格式，发布在 <https://man.bsdcn.org/>。

源内容为 Markdown 文件，由 GitBook 平台自动构建和部署，无需本地构建步骤。

**翻译基准：** 以 FreeBSD 源码树中的英文 mdoc/mandoc 原文为准，当前基准提交号为 `bcb471cfb499f61d98abdc7bfd48bee0e229b02b`。

## 内容架构

### 核心文件

- **`SUMMARY.md`** — 全书唯一数据源，定义完整目录结构和导航树。GitBook 用它来生成侧边栏。**第一行 `# Table of contents` 绝对不能变更**，否则 GitBook 同步失效。
- **`mu-lu.md`** — 由 `mulu.yml` CI 工作流从 `SUMMARY.md` 自动复制生成，**不要手动编辑**。
- **`README.md`** — 项目说明，译者信息。
- **`en2/`** — 由 `script/man-to-markdown.py` 从 `en/` mdoc 原文转换生成的 Markdown 格式英文原文（`en2/manN/命令.N.md`），作为逐句审校的**英文权威源**。架构专属文件加后缀（如 `en2/man4/glxsb.4.i386.md`）。

### 目录结构

- 章节按 man 手册分节组织：`man1/`（用户命令）、`man4/`（设备驱动）、`man5/`（文件格式）、`man7/`（杂项）、`man8/`（系统管理）
- 每个 man 页面为独立 `.md` 文件，命名为 `命令.N.md`（如 `cat.1.md`、`jail.8.md`）
- `en/` — 英文 mdoc/mandoc 原文归档（`en/manN/命令.N`），用于翻译对照参考；不要修改或翻译其中的内容
- `en/` 中的英文原文来自 FreeBSD 源码树（**share/man** 文件夹），按提交号 `bcb471cfb499f61d98abdc7bfd48bee0e229b02b` 拉取
- `en2/` — Markdown 格式英文原文（由转换器从 `en/` 生成），按 man 章节分文件夹（man1/man2/man3/man3lua/man4/man5/man6/man7/man8/man9），架构专属文件加后缀

### 标题管理（关键约束）

`sync-headers.yml` 工作流会在每次 push 时自动将 `SUMMARY.md` 中的标题同步到对应 `.md` 文件的第一行（H1）。**这意味着直接编辑 `.md` 文件的第一行标题会被 CI 覆盖。** 修改 man 页面标题时，只改 `SUMMARY.md` 中对应的 `* [标题](路径)` 条目即可。

### mdoc→Markdown 转换器

- **位置**：`script/man-to-markdown.py`（单文件，仅依赖标准库）
- **用法**：
  - `python script/man-to-markdown.py` — 全量转换 `en/` → `en2/`
  - `python script/man-to-markdown.py --sample` — 随机转换 6 个示例文件
  - 也可通过 `python man_tools.py convert` / `python man_tools.py convert-sample` 调用（见下方综合工具节）
- **功能**：
  - 自动遍历 `en/` 下所有 `man*` 子目录（man1-man9, man3lua）
  - 处理架构专属子目录（man4.aarch64/man4.arm/man4.i386/man4.powerpc），输出加架构后缀
  - mdoc macro 解析与 Markdown 映射（`.Sh` → H2 中文标题、`.Nm` → 反引号、`.Fl` → 反引号、`.Ar` → 反引号、`.Xr` → markdown 链接、`.Bd -literal` → 代码块等）
  - 交叉引用链接化：`.Xr cat 1` → `[cat(1)](cat.1.md)`（同章节）或 `[fcntl(2)](../man2/fcntl.2.md)`（跨章节），目标不存在降级为纯文本
  - SYNOPSIS 章节整行单反引号包裹（如 `` `cat [-belnstuv] [file]` ``）
  - 两遍处理：第一遍转换+记录文件清单，第二遍修正交叉引用链接
  - 幂等性：重复运行覆盖已有文件
  - UTF-8 编码（无 BOM）、LF 换行符
- **输出**：`en2/manN/命令.N.md`（通用版本）、`en2/manN/命令.N.<arch>.md`（架构版本）

### 综合工具 man_tools.py

- **位置**：`man_tools.py`（项目根目录，单文件，仅依赖标准库 + 动态加载 `script/man-to-markdown.py`）
- **用途**：整合 mdoc→Markdown 转换、en/SUMMARY 比较、翻译行数检查、问题检测等功能于一体
- **子命令**：

  | 子命令 | 功能 |
  | ------ | ---- |
  | `report` | 生成综合报告（统计 + 比较 + 行数 + 问题检测），输出到 `script/man_tools_output.txt` |
  | `compare` | 比较 `en/` 与 `SUMMARY.md`，查漏补缺（大小写不敏感，识别 MLINKS 别名） |
  | `linecount` | 比较中文翻译与英文原文（en2/）行数，可选 `--threshold N`（默认 20%） |
  | `issues` | 检测所有问题：损坏的 en2/、占位符、缺失翻译、.TH 格式文件 |
  | `fix-en2` | 重新转换损坏的 en2/ 文件（.TH 格式用简易转换器，mdoc 格式调用 `man-to-markdown.py`） |
  | `convert` | 全量转换 `en/` → `en2/`（整合 `man-to-markdown.py` 的 `run_full`） |
  | `convert-sample` | 转换示例文件（整合 `man-to-markdown.py --sample`） |
  | `aliases` | 列出 SUMMARY.md 中的别名条目（多链接指向同一文件） |
  | `stats` | 显示按章节的统计信息（en/、en2/、中文翻译、SUMMARY 链接数） |

- **用法示例**：
  - `python man_tools.py report` — 生成完整报告
  - `python man_tools.py compare` — 检查 SUMMARY.md 与 en/ 目录一致性
  - `python man_tools.py issues` — 检测占位符、损坏文件、缺失翻译
  - `python man_tools.py fix-en2 --dry-run` — 预览将修复的 en2/ 文件
  - `python man_tools.py convert` — 全量重新转换 en/ → en2/
- **日志**：`script/man_tools.log`
- **特性**：
  - 动态加载 `script/man-to-markdown.py` 作为模块，复用其 mdoc 转换逻辑
  - 对 .TH 格式（非 mdoc）文件提供简易转换器（`convert_th_to_markdown`）
  - 大小写不敏感比较（en/ 使用大写文件名如 `BUF_UNLOCK.9`，SUMMARY.md 使用小写如 `buf_unlock.9.md`）
  - 识别 MLINKS 别名（SUMMARY.md 中多个链接文本指向同一目标文件）
  - 识别架构专属文件（en/man4/man4.<arch>/ 下的文件）

## CI/CD 工作流

所有工作流位于 `.github/workflows/`，脚本位于 `.github/scripts/`：

| 工作流 | 触发条件 | 说明 |
| ------ | -------- | ---- |
| `sync-headers.yml` | push | 从 SUMMARY.md 同步标题到各 .md 文件第一行 |
| `mulu.yml` | SUMMARY.md 变更时 push | 复制 SUMMARY.md → mu-lu.md |
| `markdown-lint2.yml` | workflow_dispatch | markdownlint 检查，规则见 `.github/.markdownlint.json` |
| `md-padding.yml` | workflow_dispatch | 自动在 CJK 与英文/数字间添加空格 |
| `AutoCorrect.yml` | --- | 自动修正常见中文笔误与格式问题 |
| `links.yml` | 定时 + workflow_dispatch | lychee 死链检查，配置见 `.github/lychee.toml` |
| `file-name-check.yml` | push | 检查 SUMMARY.md 中引用的文件是否存在 |
| `create-pdf.yml` | --- | 导出 PDF |

## mdoc/mandoc 语法参考

英文原文使用 mdoc/mandoc（troff）格式，非 AsciiDoc。翻译时需理解以下 macro：

### 文档头

| Macro | 含义 | 示例 |
| ----- | ---- | ---- |
| `.Dd` | 日期（Date） | `.Dd July 20, 2015` |
| `.Dt` | 文档标题（Document Title） | `.Dt OW 4` |
| `.Os` | 操作系统（OS） | `.Os` |

### 章节标题（`.Sh`）

| mdoc Section | 中文翻译 |
| ------------ | -------- |
| `.Sh NAME` | 名称 |
| `.Sh SYNOPSIS` | 概要 |
| `.Sh DESCRIPTION` | 描述 |
| `.Sh OPTIONS` | 选项 |
| `.Sh EXIT STATUS` | 退出状态 |
| `.Sh EXAMPLES` | 实例 |
| `.Sh SEE ALSO` | 参见 |
| `.Sh STANDARDS` | 标准 |
| `.Sh HISTORY` | 历史 |
| `.Sh AUTHORS` | 作者 |
| `.Sh BUGS` | 缺陷 |
| `.Sh CAVEATS` | 注意事项 |
| `.Sh DIAGNOSTICS` | 诊断 |
| `.Sh ERRORS` | 错误 |
| `.Sh ENVIRONMENT` | 环境变量 |
| `.Sh FILES` | 文件 |
| `.Sh LEGAL` | 法律条款 |
| `.Sh WARNING` | 警告 |

子章节用 `.Ss`（如 `.Ss Commands`）。

### 内容 Macro

| Macro | 含义 | 翻译处理 |
| ----- | ---- | -------- |
| `.Nm` | 名称（命令名） | 用反引号包裹，如 `` `cat` `` |
| `.Nd` | 名称描述 | 翻译为中文 |
| `.Op` | 可选参数 | 用方括号 `[]` 包裹 |
| `.Fl` | 选项标志 | 用反引号包裹，如 `` `-v` `` |
| `.Ar` | 参数 | 用反引号包裹 |
| `.Xr` | 交叉引用 | 保留为 `命令(N)` 格式 |
| `.Cd` | 内核配置声明 | 用反引号包裹 |
| `.An` | 作者名 | 保留英文原名 |
| `.Fx` | FreeBSD 版本 | 保留为 `FreeBSD X.X` |
| `.Tn` | 商标名 | 保留英文 |
| `.Va` | 变量名 | 用反引号包裹 |
| `.Vt` | 变量类型 | 用反引号包裹 |
| `.Fa` | 函数参数 | 用反引号包裹 |
| `.Ic` | 内部命令（shell 内建） | 用反引号包裹 |
| `.Li` | 字面量 | 用反引号包裹 |
| `.Em` | 强调 | 翻译为中文 |
| `.Sy` | 符号（加粗） | 保留原文 |
| `.D1` | 单行缩进显示 | 用缩进或代码块 |
| `.Dl` | 单行字面量显示 | 用代码块 |
| `.Bd`/`.Ed` | 显示块开始/结束 | 用代码块（`.Bd -literal`） |
| `.Bl`/`.El` | 列表开始/结束 | 用 markdown 列表 |
| `.It` | 列表项 | 用 `-` 或 `1.` |
| `.Pp` | 段落分隔 | 空行 |
| `.Ql` | 引用字面量 | 用反引号包裹 |
| `.Dq` | 双引号 | 用中文引号"" |
| `.Sq` | 单引号 | 用中文引号'' |

### 列表类型

- `.Bl -column` — 列表（表格样式），用 markdown 表格
- `.Bl -tag` — 标签列表（定义列表），用 `**标签**` + 描述
- `.Bl -item` — 项目列表，用 `-` 无序列表
- `.Bl -compact` — 紧凑列表（无额外间距）
- `.Ta` — 列表中的制表符分隔（用于 `-column` 列表）

### mdoc 到 Markdown 翻译映射

| mdoc | Markdown 翻译 |
| ---- | ------------- |
| `.Sh NAME` + `.Nm` + `.Nd` | `[名称](#anchor)` + `===` 标题，`` `命令` `` — 中文描述 |
| `.Sh SYNOPSIS` | `[概要](#anchor)` + `===` 标题 |
| `.Fl v` | `` `-v` `` |
| `.Ar file` | `` `file` `` |
| `.Op Ar file` | `[`file`]` |
| `.Xr cat 1` | `cat(1)` |
| `.Cd device ow` | `` `device ow` `` |
| `.Bd -literal` ... `.Ed` | ` ```sh ` ... ` ``` ` |
| `.Bl -tag` + `.It Fl v` | `` `-v` `` + 描述 |
| `.Fx 11.0` | `FreeBSD 11.0` |

## 编写规范

### 格式

- **命令行前缀：** `#` 表示 root 权限，`$` 表示普通用户。不要使用 `sudo`。
- **提示块：** tip/important/note/warning/caution 使用 `>` 缩进引用，关键词 **加粗**。
- **代码块：** 无法判断的，再使用 `/`/`/`sh ` 兜底，禁止使用 text 作为代码块标记，不窜改既有的 ` ```ini ` 标记。
- **表格：** 一律居中。
- **禁止 HTML：** 本项目不支持任何 HTML 语法。
- **文件命名：** 使用 `命令.N.md` 格式，文件名中不得包含空格、中文字符或英文冒号 `:`，必须兼容 Windows 操作系统对文件名的要求。
- **路径与 IP：** 全书正文中的路径（带 `/` 或 `\` 的，如 `/etc/rc.conf`、`/usr/local/etc/`）和 IP 地址一律使用 **加粗**，不使用反引号 `` ` `` 包裹；不要混合使用 `*` 和 `` ` ``（如 `*`path`*` 是错误的）。
- **命令、选项、参数：** 命令、选项、可调选项、可调参数等格式使用 `行间代码`（反引号）包裹。注意：不带选项和参数的裸命令，如 mv cp 等，一般不加反引号，不进行包裹。
- **转义字符：** 除非是命令、选项和参数，否则含转义字符 `\` 的元素一律使用 **加粗** 包裹整个元素，不在正文中直接使用转义字符。逐个手动修改，禁止批量替换。
- **避免滥用"已"字：** 如"XX 已新增"应改为"新增 XX"；"已修复"应改为"修复完成"。禁止机械替换。
- **禁止篡改：** 不要篡改软件版本号、用户名、带圈数字（如 ①②③ 等），确保其位置、数量和英语原文一致。
- **代码块注释翻译：** 代码块（` ``` ` 围栏）内的英文注释必须翻译为中文（如 shell 注释 `# This is a comment` → `# 这是一个注释`）。只翻译注释部分，不修改实际命令或代码。保持代码结构和格式不变。
- **fstab 不翻译：** fstab 文件表头（如 `# Device Mountpoint FStype Options Dump Pass#`）及其相关内容保持英文原样，不翻译。

### 术语

- `Ports` 保持英文不翻译，且保持首字母大写（注意区分真正的"端口"）禁止机械替换。
- "Jail" 保持英文（不翻译为"监狱"、"监牢"）禁止机械替换。
- "拷贝" → "复制"，"壳/外壳" → "shell"。禁止机械替换。
- 第二人称一律使用"你"而非"您"
- man 手册中的技术术语（如 socket、daemon、filesystem、partition 等）保留英文或按惯例翻译，保持全书一致

### CJK 空格

中英文、中文与数字之间必须加半角空格。文件和命令名用 `` ` `` 括起来。`md-padding.yml` 和 `AutoCorrect.yml` 工作流会自动检测修复。

### 标点符号

全书正文标点符号需统一使用全角，包括""及括号、引号等，避免半角混用。

### 图片

在正文中插入图片，使用 markdown 格式。

## 翻译流程

1. 参考英文 Markdown 原文（`en2/manN/` 下对应文件）进行人工校对
2. 提交 PR 到 main 分支

### 翻译校对工作流程（Claude Code）

对已翻译 man 页面进行质量审校时，参考以下步骤：

1. **获取原文**：优先从 `en2/manN/命令.N.md` 读取英文 Markdown 原文。如果 `en2/` 中没有该文件，通过 `WebFetch` 抓取 `https://man.freebsd.org/cgi/man.cgi?query=命令&sektion=N` 获取英文内容。

2. **逐句对照**：将中文翻译与英文 Markdown 原文逐句比对，重点检查以下问题类别：

   | 问题类型 | 示例 |
   | -------- | ---- |
   | 漏译 | 英文原版有但中文缺失的句子/段落 |
   | 未翻译的英文残留 | 如整段英文未译（cat.1.md 退出状态整段英文） |
   | 事实性错误/窜改原意 | 中文与英文原意不符 |
   | 机翻腔/表达生硬 | "在阅读本章后，你将会收获" → "通过阅读本章，你将了解" |
   | 用词不当 | "独家优势"应为"主要优势" |
   | 术语不一致 | "您的 shell"应为"你的 shell"（第二人称用"你"） |
   | 版本过时 | FreeBSD 版本号与英文原文不一致 |
   | 语法/文字错误 | 重复字词、"非常地"应为"非常" |
   | 欧化汉语 | 倒装句、后置句、偷换主语、不必要的被动句、滥用"一个 xx" |

3. **提交修改**：
   - 基于 `main` 创建分支 `fix/manN-translation`
   - 仅提交修改的 `.md` 文件，不要包含无关文件
   - 提交信息格式：`fix: 修正 manN 翻译错误及同步英文原版更新`
   - 用 `gh pr create` 创建 PR，目标分支为 `main`
   - PR 描述中列出每处修改及原因

4. **注意事项**：
   - 不要修改 `.md` 文件的第一行标题——会被 `sync-headers.yml` CI 覆盖
   - 保持术语一致性
   - 英文原文可能比翻译版本更新，版本号差异应以英文原版为准
   - 添加新内容时，确保翻译风格与上下文一致
   - 禁止篡改带圈数字、代码块（shell 命令、配置文件内容）、用户名、邮箱、URL、IP 地址、软件版本号
   - 以英文 Markdown 原文（`en2/`）为唯一权威源；禁止以中文版已有翻译作为修改依据，避免错误沿袭
   - 允许意译，但不得扭曲原意

5. **逐句校对递归工作流**（核心约束）：
   - **逐行逐句子**遍历内容，检查逻辑一致性，联网复核后修改
   - **三轮 + 一轮复查**：完整执行三轮逐句校对，然后严格、完整地复查一轮；若仍有问题，继续执行三轮，递归直至无问题
   - **逐个修改**：修改时禁止机械修改、禁止批量；必须逐个手动修改，禁止使用软件工具批量替换或批量逐个复核
   - **修改前后复核**：每次修改前确认问题真实存在、修改后确认改动准确且未引入新错误
   - **不复查旧错**：不得复查以前已经完成三轮的错误；每轮查询内容必须是新的
   - **联网复查**：对于不存在的实际访问查询（如失效链接、版本号、API 端点），需联网复查三次后修改
   - **禁止绕过审查**：不得以任何方式搜索、批量、绕过逐句子审查流程

## 结构化 AI 更新方法

本节提供便于 AI 理解的日后更新流程，用于将翻译同步到新版 FreeBSD man 页面。

### 当前英文原文基准

- **FreeBSD 源码仓库**：`https://gitlab.freebsd.org/freebsd/freebsd-src`（或 GitHub 镜像 `https://github.com/freebsd/freebsd-src`）
- **当前基准提交号**：`c9d98c0134864d8bc69006b92d34a3b22c940870`
- **英文原文位置**：`en/manN/命令.N`（mdoc/mandoc 格式，无 `.md` 扩展名）
- **Markdown 原文位置**：`en2/manN/命令.N.md`（由 `script/man-to-markdown.py` 从 `en/` 转换生成，逐句审校权威源）

### 如何获取新版英文原文

1. **克隆 FreeBSD 源码仓库**：

   ```sh
   git clone --filter=blob:none https://gitlab.freebsd.org/freebsd/freebsd-src.git
   cd freebsd-src
   git checkout <新提交号>
   ```

2. **提取 man 页面到 en/**：
   - `share/man/manN/` 下的文件直接复制到 `en/manN/`
   - 命令 man 页面分散在源码树中，按以下路径查找：
     - `bin/<cmd>/<cmd>.1` — 基本命令（cat, ls, cp 等）
     - `sbin/<cmd>/<cmd>.8` — 系统命令（mount, ifconfig 等）
     - `usr.bin/<cmd>/<cmd>.1` — 用户命令（grep, find, less 等）
     - `usr.sbin/<cmd>/<cmd>.8` — 系统管理命令（jail, bhyve 等）
     - `libexec/<cmd>/<cmd>.8` — 库可执行文件（ftpd 等）
     - `stand/<cmd>/<cmd>.8` — 引导加载器
     - `gnu/usr.bin/<cmd>/<cmd>.1` — GNU 工具
     - `cddl/usr.sbin/<cmd>/<cmd>.8` — CDDL 工具（dtrace 等）
   - MLINKS 别名（如 sha256.1 → md5.1）：使用主文件内容

3. **拉取单个文件**（无需克隆整个仓库）：

   ```sh
   # GitLab raw
   curl -o en/man1/cat.1 https://gitlab.freebsd.org/freebsd/freebsd-src/-/raw/<commit>/bin/cat/cat.1
   # GitHub 镜像（备用）
   curl -o en/man1/cat.1 https://raw.githubusercontent.com/freebsd/freebsd-src/<commit>/bin/cat/cat.1
   ```

4. **Shell 内建命令**（alias, break, case, cd, echo, eval, exec, exit, export, for, if, jobs, kill, read, set, shift, source, unset, wait 等）：
   - 无独立 `.1` 源文件
   - 文档统一收录在 `builtin.1`、`csh.1`、`sh.1` 中
   - 翻译时参考这些父文件

### 如何检测变更

```sh
# 对比两个提交之间的 man 页面变更
git diff <旧提交号> <新提交号> -- '*.1' '*.4' '*.5' '*.7' '*.8' '*.9'

# 仅列出变更的文件
git diff --name-only <旧提交号> <新提交号> -- '*.1' '*.4' '*.5' '*.7' '*.8' '*.9'
```

### 如何增量更新翻译

1. 检测到 man 页面变更后，更新 `en/manN/` 中对应的英文原文文件
2. 重新生成 en2/：运行 `python script/man-to-markdown.py` 从更新后的 `en/` 重新生成 `en2/` Markdown 原文
3. 对有变更的 man 页面，按"翻译校对工作流程"执行逐句审校
4. 更新 CLAUDE.md 中的"当前基准提交号"
5. 未变更的 man 页面无需重新审校

### mdoc → Markdown 映射规则速查

| mdoc 语法 | Markdown 翻译 |
| --------- | ------------- |
| `.Sh SECTION` | `[中文标题](#anchor)` + `===`（H1 风格） |
| `.Ss Subsection` | `[中文子标题](#anchor)` + `---`（H2 风格） |
| `.Nm cmd` | `` `cmd` `` |
| `.Nd 描述` | `—` 中文描述 |
| `.Fl v` | `` `-v` `` |
| `.Ar file` | `` `file` `` |
| `.Op Ar file` | `[`file`]` |
| `.Xr cat 1` | `cat(1)` |
| `.Cd device ow` | `` `device ow` `` |
| `.Bd -literal` ... `.Ed` | ` ```sh ` ... ` ``` ` |
| `.Bl -tag` + `.It Fl v` | `` `-v` `` + 描述 |
| `.Bl -item` + `.It` | `-` 列表项 |
| `.Bl -column` | markdown 表格 |
| `.Pp` | 空行 |
| `.Fx 11.0` | `FreeBSD 11.0` |
| `.An 名字` | 保留英文原名 |
| `.Tn 商标` | 保留英文 |
| `.Ql text` | `` `text` `` |
| `.Dq text` | "text"（中文引号） |

## Lint 配置

- **markdownlint**（`.github/.markdownlint.json`）：本地已安装 `markdownlint-cli2 v0.22.1`（基于 `markdownlint v0.40.0`），可在本地直接运行检查与修复
  - **本地运行命令**（在仓库根目录执行）：

    ```sh
    # 检查全部中文 .md（排除 en/、en2/、.github/、.gitbook/、node_modules/、script/）
    markdownlint-cli2 "**/*.md" "!en/**" "!en2/**" "!.github/**" "!.gitbook/**" "!node_modules/**" "!script/**" --config .github/.markdownlint.json

    # 自动修复可修复的问题（MD012 多余空行、MD047 末尾换行、MD034 裸 URL 等）
    markdownlint-cli2 "**/*.md" "!en/**" "!en2/**" "!.github/**" "!.gitbook/**" "!node_modules/**" "!script/**" --config .github/.markdownlint.json --fix
    ```

  - **MD060 表格列风格规则（重要）**：配置为 `"style": "compact"` + `"aligned_delimiter": true`
    - **compact 风格**：管道符两侧各保留**单个空格**，例如 `| cell1 | cell2 |`；空单元格写作 `| |`（不是 `||` 或 `|  |`）
    - **aligned_delimiter**：分隔行 `|---|` 的管道符位置必须与表头行的管道符位置对齐
    - **CJK 显示宽度**：markdownlint 按**显示宽度**计算列位置，**每个中文字符按 2 宽度**计算（与英文 1 宽度不同）。因此含 CJK 的列宽 = CJK 字符数 × 2 + ASCII 字符数 × 1
    - **分隔行 dash 数量公式**：若某列内容显示宽度为 W，则分隔行该列总宽（含两侧空格）也应为 W，dash 数量 = W − 4（减去前后各 1 空格 + 前后各 1 冒号）。例如列内容 `FreeBSD 版本` 显示宽度 = 7+1+4 = 12，分隔行应为 ` :--------: `（8 个 dash）
    - **常见错误修复**：当 markdownlint 报 `MD060/table-column-style [Table pipe does not align with header for option "aligned_delimiter"]` 时，需手动扩展分隔行 dash 数量，使管道符位置与表头按显示宽度对齐；`--fix` 无法自动修复此类问题
  - **MD056 表格列数规则**：表头声明几列，所有数据行都必须有几列；末尾缺空单元格时需补 `| |`，而非省略管道符
- **textlint**（`.textlintrc`）：仅启用 `ja-space-between-half-and-full-width` 规则，用于 CJK/英文空格检查
- **lychee**（`.github/lychee.toml`）：6 线程、30 并发、30 秒超时、最多 3 次重试、Chrome UA、排除私有 IP 和 `ftp.freebsd.org`

## AutoCorrect 与 md-padding 最终清理流程

**执行时机**：所有翻译工作完成后，作为最终清理步骤执行。

**工具**：

- `AutoCorrect`（`.github/AutoCorrect.yml` 工作流）：自动修正常见中文笔误与格式问题
- `md-padding`（`.github/md-padding.yml` 工作流）：自动在 CJK 与英文/数字间添加空格

**核心约束（必须严格遵守）**：

1. **禁止批量接受**：不得使用 `--fix` 或类似选项直接批量应用所有修改建议
2. **禁止默认接受**：不得默认接受工具输出，必须逐条人工审核
3. **逐个结合上下文综合复核**：对每一条修改建议，必须结合所在段落的上下文综合判断是否采纳
4. **修改前后各复核一次**：
   - **修改前复核**：确认问题真实存在，修改建议准确且不引入新错误
   - **修改后复核**：确认改动准确，未破坏原有格式、链接、代码块、表格等
5. **最后总复核一次**：全部修改完成后，对全书进行一次总复核，确认无遗漏、无新引入的错误

**执行步骤**：

1. **生成工具输出**：分别运行 AutoCorrect 和 md-padding，**仅生成差异报告，不直接应用修改**

   ```sh
   # AutoCorrect 检查（不修改文件）
   autocorrect --lint "**/*.md" "!en/**" "!en2/**" "!.github/**" "!script/**"

   # md-padding 检查（不修改文件，仅输出差异）
   md-padding --check "**/*.md" "!en/**" "!en2/**" "!.github/**" "!script/**"
   ```

2. **逐条审核**：对每一条修改建议：
   - 阅读修改点所在段落完整上下文
   - 判断修改是否正确（如 CJK 空格、标点规范、术语一致）
   - 判断修改是否会破坏代码块、链接、表格、路径加粗等格式
   - 仅在确认无误后手动应用该修改（使用 Edit 工具逐个修改，禁止批量替换）

3. **修改前复核**：每次修改前，确认问题真实存在且修改建议准确

4. **修改后复核**：每次修改后，重新读取修改区域，确认改动准确且未引入新错误

5. **总复核**：全部修改完成后，重新运行工具检查，确认无遗漏问题；对全书进行一次抽查，确认格式一致性

**禁止事项**：

- 禁止使用 `--fix` 或 `-i` 选项批量应用修改
- 禁止使用脚本批量替换
- 禁止跳过上下文审核直接接受工具建议
- 禁止修改代码块内部内容（代码块内注释除外，但需单独审核）
- 禁止修改路径加粗格式（`**/path**` 不得改为反引号或其他格式）
- 禁止修改交叉引用链接格式
