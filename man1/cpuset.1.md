# cpuset(1)

`cpuset` — 配置处理器集合

## 名称

`cpuset`

## 概要

`cpuset [-l cpu-list] [-n policy:domain-list] [-s setid] cmd ... cpuset [-l cpu-list] [-n policy:domain-list] [-s setid] -p pid cpuset [-c] [-l cpu-list] [-n policy:domain-list] -C -p pid cpuset [-c] [-l cpu-list] [-n policy:domain-list] [-j jail | -p pid | -t tid | -s setid | -x irq] cpuset -g [-cir] [-d domain | -j jail | -p pid | -t tid | -s setid | -x irq]`

## 描述

`cpuset` 命令可用于为进程分配处理器集合、运行受限于指定处理器集合或处理器与内存域列表的命令，以及查询系统中有关处理器绑定、内存绑定与策略、集合，以及可用处理器与内存域的信息。

`cpuset` 需要一个修改或查询目标。目标可以指定为命令、进程 ID、线程 ID、cpuset ID、IRQ、Jail 或 NUMA 域。使用 `-g` 可查询目标的集合 ID 或掩码。使用 `-l` 或 `-s` 可设置目标的 CPU 掩码或集合 ID。如果未指定目标，`cpuset` 将对自身进行操作。并非所有操作与目标的组合都受支持。例如，不能设置现有集合的 ID，也不能同时查询并启动命令。

每个进程关联两个集合，每个线程有一个私有掩码。系统中的每个进程都属于一个 cpuset。默认情况下，进程在集合 1 中启动。可使用 `-c` 查询掩码或 ID。每个线程还有一个其允许运行的 CPU 私有掩码，该掩码必须是指定集合的子集。最后，还有一个编号为 0 的根集合，它是不可变的。最后一个集合是系统中所有可能 CPU 的列表，使用 `-r` 查询。

大多数集合包含 NUMA 内存域与策略信息。可使用 `-g` 检查，使用 `-n` 设置。这将指定哪些 NUMA 域对进程可见，并影响首次访问时匿名内存与文件页的存储位置。被其他进程首次访问的文件可能指定冲突的策略。

运行命令时，可加入用 `-s` 指定的集合，否则将创建新集合。此外，可使用 `-l` 为命令指定掩码。与 `-c` 一起使用时，该掩码修改所提供或创建的集合，而非线程的私有掩码。

选项如下：

**`-C`** 创建新 cpuset 并将目标进程分配到该集合。

**`-c`** 所请求操作应引用通过目标说明符可访问的 cpuset。

**`-d`** `domain` 将 NUMA 域 ID 指定为操作目标。这仅可用于查询每个编号域中可见的 CPU。

**`-g`** 使 `cpuset` 打印有效 CPU 列表，或使用 `-i` 打印目标 ID。

**`-i`** 与 `-g` 选项一起使用时，打印目标 ID 而非有效掩码。

**`-j`** `jail` 将 Jail ID 或名称指定为操作目标。

**`-l`** `cpu-list` 指定要应用于目标的 CPU 列表。指定方式可包括用 '-' 分隔的数字范围和用逗号分隔的单个数字。可指定特殊列表 “all”，此时列表包含根集合中的所有 CPU。

**`-n`** `policy:domain-list` 指定要应用于目标的域列表和分配策略。范围可按 `-l` 的方式指定。有效策略包括 first-touch (ft)、round-robin (rr)、prefer 和 interleave (il)。first-touch 在内存可用时在本地域上分配。round-robin 在每个可能的域页面之间交替。prefer 策略在集合中仅接受单个域。如果首选域不可用，则查询集合的父集合。interleave 的作用类似于 round-robin，但具有实现定义的条带宽度。有关策略的更多细节，参见 [domainset(9)](../man9/domainset.9.md)。

**`-p`** `pid` 将 pid 指定为操作目标。

**`-s`** `setid` 将集合 ID 指定为操作目标。

**`-r`** 所请求操作应引用通过目标说明符可访问的根集合。

**`-t`** `tid` 将线程 ID 指定为操作目标。

**`-x`** `irq` 将 IRQ 指定为操作目标。

## 退出状态

`cpuset` 实用程序成功时退出值为 0，发生错误时大于 0。

## 实例

创建包含 CPU 0-4 的新组并在其上运行 **/bin/sh**：

```sh
cpuset -c -l 0-4 /bin/sh
```

查询 `<sh pid>` 允许运行的 CPU 掩码：

```sh
cpuset -g -p <sh pid>
```

将 **/bin/sh** 限制为在 CPU 0 和 2 上运行，而其所在组仍允许在 CPU 0-4 上运行：

```sh
cpuset -l 0,2 -p <sh pid>
```

修改 **/bin/sh** 所属的 cpuset，将其限制为 CPU 0 和 2：

```sh
cpuset -l 0,2 -c -p <sh pid>
```

修改所有线程默认所在的 cpuset，使其仅包含前 4 个 CPU，其余保持空闲：

```sh
cpuset -l 0-3 -s 1
```

打印 **/bin/sh** 所在的 cpuset 的 ID：

```sh
cpuset -g -i -p <sh pid>
```

将 `pid` 移入指定 cpuset `setid`，以便与该集合中的其他 pid 一起管理：

```sh
cpuset -s <setid> -p <pid>
```

创建限制为 CPU 0 和 2 的新 cpuset，并将 `pid` 移入新集合：

```sh
cpuset -C -c -l 0,2 -p <pid>
```

## 参见

nproc(1), [cpuset(2)](../sys/cpuset.2.md), [rctl(8)](../man8/rctl.8.md)

## 历史

`cpuset` 命令首次出现于 FreeBSD 7.1。

## 作者

Jeffrey Roberson <jeff@FreeBSD.org>
