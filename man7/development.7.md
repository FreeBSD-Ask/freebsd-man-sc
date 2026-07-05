# development.7

`development` — FreeBSD 开发流程简介

## 名称

`development` FreeBSD 开发流程

## 描述

FreeBSD 开发分为三个主要子项目：doc、ports 和 src。Doc 是文档，如 FreeBSD Handbook。更多信息参见：

Lk https://docs.FreeBSD.org/en/books/fdp-primer/

Ports 在 [ports(7)](ports.7.md) 中进一步描述，是构建、打包和安装第三方软件的方式。更多信息参见：

Lk https://docs.FreeBSD.org/en/books/porters-handbook/

最后一个 src，围绕基本系统的源代码，由内核以及通常称为 world 的库和实用程序组成。

Committer's Guide 描述了与所有 committer 相关的主题，可在以下位置找到：

Lk https://docs.freebsd.org/en/articles/committers-guide/

FreeBSD src 开发在项目托管的 Git 仓库中进行，位于：

Lk https://git.FreeBSD.org/src.git

推送 URL 为：

Lk ssh://git@gitrepo.FreeBSD.org/src.git

还有公共只读 Git 镜像列表：

Lk https://docs.FreeBSD.org/en/books/handbook/mirrors/#external-mirrors

`main` Git 分支代表 CURRENT；所有更改首先提交到 CURRENT，然后通常挑选回 STABLE，STABLE 指的是 `stable/14` 等 Git 分支。每隔几年从 CURRENT 分支出新的 STABLE，主版本号递增。然后从 STABLE 分支出版本，以连续的次版本号编号，如 `releng/14.3`

源代码树的布局在其 `README.md` 文件中描述。构建说明可在 [build(7)](build.7.md) 和 [release(7)](release.7.md) 中找到。内核编程接口（KPI）记录在第 9 节手册页中；使用 `apropos -s 9 .` 获取列表。回归测试套件在 [tests(7)](tests.7.md) 中描述。编码约定参见 [style(9)](../man9/style.9.md)。

要询问有关开发的问题，请使用邮件列表，如 freebsd-arch@ 和 freebsd-hackers@：

Lk https://lists.FreeBSD.org

要将补丁集成到 FreeBSD 主仓库，请使用 Phabricator；它是一个代码审查工具，允许其他开发者审查更改、提出改进建议，并最终允许他们选取更改并提交：

Lk https://reviews.FreeBSD.org

或 Github：

Lk https://github.com/freebsd

要检查 CURRENT 和 STABLE 分支的最新 FreeBSD 构建和测试状态，持续集成系统位于：

Lk https://ci.FreeBSD.org

## 文件

**`/usr/src/CONTRIBUTING.md`** FreeBSD 贡献指南
**`/usr/src/tools/tools/git/git-arc.sh`** Phabricator 审查工具
**`/usr/ports/devel/freebsd-git-arc`** 作为 port 的 Phabricator 审查工具

## 实例

使用 `devel/gh` 应用 Github pull #1234 的补丁：

```sh
gh pr checkout 1234
```

使用 git-arc(1) 应用 Phabricator 审查 D1234 的补丁：

```sh
git arc patch -c D1234
```

应用从 Bugzilla 或邮件手动下载的 git-format-patch(1) 补丁 `draft.patch`：

```sh
git am draft.patch
```

应用从 Bugzilla 或邮件手动下载的补丁 `draft.diff`：

```sh
git apply draft.diff
```

## 参见

git(1), git-arc(1), [witness(4)](../man4/witness.4.md), [build(7)](build.7.md), [hier(7)](hier.7.md), [ports(7)](ports.7.md), [release(7)](release.7.md), [tests(7)](tests.7.md), [locking(9)](../man9/locking.9.md), [style(9)](../man9/style.9.md)

## 历史

`development` 手册页最初由 Matthew Dillon <dillon@FreeBSD.org> 编写，首次出现于 FreeBSD 5.0，2002 年 12 月。此后由 Eitan Adler <eadler@FreeBSD.org> 大量修改，以反映仓库从 Lk https://www.nongnu.org/cvs/ CVS 到 Lk https://subversion.apache.org/ Subversion 的转换。由 Edward Tomasz Napierala <trasz@FreeBSD.org> 为 FreeBSD 12.0 从头重写。
