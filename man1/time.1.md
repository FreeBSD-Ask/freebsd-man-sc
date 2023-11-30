  TIME(1)  

TIME(1)

FreeBSD General Commands Manual

TIME(1)

[名称](#__u540D___u79F0_)
=======================

`time` —

计算命令执行的时间

[概要](#__u6982___u8981_)
=======================

`time` \[`-al`\] \[`-h` | `-p`\] \[`-o` file\] utility \[argument ...\]

[描述](#__u63CF___u8FF0_)
=======================

`time` 实用程序执行指定的 utility 并对其计时。 utility 完成后， `time` 写入标准错误流，（以秒为单位）：已用的总时间、执行 utility 进程所用的时间和系统开销消耗的时间。

可以使用以下选项：

[`-a`](#a)

如果使用了 `-o` 标志，则追加到指定的文件而不是覆盖它。 否则，此选项无效。

[`-h`](#h)

以人性化的格式打印时间。 时间以分钟、小时等适当打印。

[`-l`](#l)

_rusage_ 结构的内容也被打印出来。

[`-o`](#o) file

将输出写入 file 而不是标准错误。 如果 file 存在且未指定 `-a` 标志，则该文件将被覆盖。

[`-p`](#p)

使 `time` 输出符合 POSIX.2（每次都打印在自己的行上）。

某些 shell 可能提供与此实用程序类似或相同的内置 `time` 命令。 请参阅 builtin(1) 手册页。

如果 `time` 收到 `SIGINFO` （参见 stty(1) 的状态参数）信号，则给定命令运行的当前时间将被写入标准输出。

[环境](#__u73AF___u5883_)
=======================

如果名称不包含 ‘`/`’ 字符，则 `PATH` 环境变量用于定位请求的 utility 。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

如果 utility 可以成功计时，则返回其退出状态。如果 utility 异常终止，则会向 stderr 输出一条警告消息。 如果找到该 utility 但无法运行，则退出状态为 126。 如果根本找不到 utility ，则退出状态为 127。 如果 `time` 遇到任何其他错误，则退出状态介于 1 到 125 之间。

[实例](#__u5B9E___u4F8B_)
=======================

在空目录上执行 ls(1) 的时间：

$ /usr/bin/time ls 0.00 real 0.00 user 0.00 sys 

计算 cp(1) 命令的执行时间并将结果存储在 times.txt 文件中。 然后再次执行命令以制作新副本并将结果添加到同一文件中：

$ /usr/bin/time -o times.txt cp FreeBSD-12.1-RELEASE-amd64-bootonly.iso copy1.iso $ /usr/bin/time -a -o times.txt cp FreeBSD-12.1-RELEASE-amd64-bootonly.iso copy2.iso 

times.txt 文件将包含两个命令的时间：

$ cat times.txt 0.68 real 0.00 user 0.22 sys 0.67 real 0.00 user 0.21 sys 

计时 sleep(1) 命令并以人类友好的格式显示结果。也显示 _rusage_ 结构的内容：

$ /usr/bin/time -l -h -p sleep 5 real 5.01 user 0.00 sys 0.00 0 maximum resident set size 0 average shared memory size 0 average unshared data size 0 average unshared stack size 80 page reclaims 0 page faults 0 swaps 1 block input operations 0 block output operations 0 messages sent 0 messages received 0 signals received 3 voluntary context switches 0 involuntary context switches 

[参见](#__u53C2___u89C1_)
=======================

builtin(1), csh(1), getrusage(2), wait(2)

[标准](#__u6807___u51C6_)
=======================

`time` 实用程序应符合 ISO/IEC 9945-2:1993 (\`\`POSIX'')。

[历史](#__u5386___u53F2_)
=======================

`time` 实用程序出现在 Version 3 AT&T UNIX 中。

July 7, 2020

FreeBSD 13.1-RELEASE