# time(1)

`time` — 为命令执行计时

## 名称

`time`

## 概要

`time [-al] [-h -| -p] [-o file] utility [argument ...]`

## 描述

`time` 实用程序执行并为指定的 `utility` 计时。`utility` 完成后，`time` 向标准错误流写入（以秒为单位）：总经过时间、执行 `utility` 进程所用的时间以及系统开销消耗的时间。

以下选项可用：

**`-a`** 如果使用了 `-o` 标志，则追加到指定文件而不是覆盖它。否则，此选项无效。

**`-h`** 以人类友好的格式打印时间。时间以分钟、小时等适当单位打印。

**`-l`** 同时打印 *rusage* 结构的内容。

**`-o`** `file` 将输出写入 `file` 而不是 stderr。如果 `file` 存在且未指定 `-a` 标志，文件将被覆盖。

**`-p`** 使 `time` 输出符合 POSIX.2（每个时间单独打印在一行上）。

某些 shell 可能提供与此实用程序类似或相同的内建 `time` 命令。参见 [builtin(1)](builtin.1.md) 手册页。

如果 `time` 收到 `SIGINFO` 信号（参见 stty(1) 的 status 参数），当前给定命令运行的时间将写入标准输出。

## 环境变量

如果名称不包含 `/` 字符，`PATH` 环境变量用于定位请求的 `utility`。

## 退出状态

如果 `utility` 成功计时，返回其退出状态。如果 `utility` 异常终止，向 stderr 输出警告消息。如果找到了 `utility` 但无法运行，退出状态为 126。如果完全找不到 `utility`，退出状态为 127。如果 `time` 遇到任何其他错误，退出状态在 1 到 125 之间（含）。

## 实例

为空目录上 [ls(1)](ls.1.md) 的执行计时：

```sh
$ /usr/bin/time ls
        0.00 real         0.00 user         0.00 sys
```

为 [cp(1)](cp.1.md) 命令的执行计时并将结果存储在 `times.txt` 文件中。然后再次执行命令以创建新副本并将结果添加到同一文件：

```sh
$ /usr/bin/time -o times.txt cp source.iso copy1.iso
$ /usr/bin/time -a -o times.txt cp source.iso copy2.iso
```

`times.txt` 文件将包含两个命令的时间：

```sh
$ cat times.txt
        0.68 real         0.00 user         0.22 sys
        0.67 real         0.00 user         0.21 sys
```

为 [sleep(1)](sleep.1.md) 命令计时并以人类友好的格式显示结果。同时显示 *rusage* 结构的内容：

```sh
$ /usr/bin/time -l -h -p sleep 5
real 5.01
user 0.00
sys 0.00
         0  maximum resident set size
         0  average shared memory size
         0  average unshared data size
         0  average unshared stack size
        80  page reclaims
         0  page faults
         0  swaps
         1  block input operations
         0  block output operations
         0  messages sent
         0  messages received
         0  signals received
         3  voluntary context switches
         0  involuntary context switches
```

## 参见

[builtin(1)](builtin.1.md), [csh(1)](csh.1.md), [getrusage(2)](../man2/getrusage.2.md), [wait(2)](../man2/wait.2.md)

## 标准

`time` 实用程序预期符合 ISO/IEC 9945-2:1993。

## 历史

`time` 实用程序出现在 Version 3 AT&T UNIX 中。
