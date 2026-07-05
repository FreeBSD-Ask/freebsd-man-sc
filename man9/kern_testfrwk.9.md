# kern_testfrwk.9

`kern_testfrwk` — 内核测试框架

## 名称

`kern_testfrwk`

## 概要

```sh
kldload kern_testfrwk
```

## 描述

那么内核中的这个 sys/tests 目录到底是做什么的？

你是否曾想以某种方式测试 FreeBSD 内核的某个部分，却无法从用户态触发你期望发生的事情？比如某个错误路径，或者某种以特定方式发生锁定的情形，而这种情形极少出现？

如果是这样，那么内核测试框架正是你需要的。它旨在帮助你创建你想要的场景。

该系统有两个组件：测试框架和你的测试。本文档将描述这两个组件，并使用随此代码首次提交的测试来讨论测试（callout_test）。所有测试都成为内核可加载模块。你编写的测试应该依赖于测试框架。这样它将随你的测试一起自动加载。例如，你可以在 `sys/tests/callout_test/callout_test.c` 中 callout_test.c 的底部看到如何做到这一点。

框架本身位于 `sys/tests/framework/kern_testfrwk.c`。它的工作是管理已加载的测试。（可以加载多个测试。）思路很简单；你加载测试框架，然后加载你的测试。

当你的测试加载时，你向内核测试框架注册你的测试。你通过调用 `kern_testframework_register` 来完成此操作。通常这在模块加载事件时完成，如下所示：

```c
	switch (type) {
	case MOD_LOAD:
		err = kern_testframework_register("callout_test",
		    run_callout_test);
```

这里测试名为 "callout_test"，注册为运行函数 `run_callout_test`，并向其传递一个 `struct kern_test *ptr`。`kern_test` 结构定义在 `kern_testfrwk.h` 中。

```c
struct kern_test {
	char name[TEST_NAME_LEN];
	int num_threads;  /* 填入你想要的线程数量 */
	int tot_threads_running;       /* 框架私有 */
	uint8_t test_options[TEST_OPTION_SPACE];
};
```

用户通过 sysctl 将此结构下发以启动你的测试。他或她在 `name` 字段中放置你注册的相同名称（在我们的示例中为 "callout_test"）。用户还可以使用 `num_threads` 设置要运行的线程数。

框架将启动所请求数量的内核线程，所有线程同时运行你的测试。用户不在 `tot_threads_running` 中指定任何内容；它是框架私有的。当框架调用你的每个测试时，它将把 `tot_threads_running` 设置为你的调用所在线程的索引。例如，如果用户将 `num_threads` 设置为 2，那么函数 `run_callout_test` 将被调用一次，`tot_threads_running` 为 0，第二次调用时 `tot_threads_running` 设置为 1。

`test_options` 字段是测试特定的信息集，是一个不透明的数据块。它从用户空间传入，最大大小为 256 字节。你可以在此空间中传递任意测试输入。在 callout_test 的情况下，我们将其重塑为：

```c
struct callout_test {
	int number_of_callouts;
	int test_number;
};
```

因此 `run_callout_test` 的前几行执行以下操作以获取用户特定数据：

```c
	struct callout_test *u;
	size_t sz;
	int i;
	struct callout_run *rn;
	int index = test->tot_threads_running;
	u = (struct callout_test *)test->test_options;
```

这样它就可以访问：`u->test_number`（此测试提供了两种类型的测试）和 `u->number_of_callouts`（要运行多少个并发 callout）。

你的测试可以用这些字节做任何事情。因此所讨论的 callout_test 希望创建一个多个 callout 全部运行的场景，即 `number_of_callouts`，并尝试使用新的 `callout_async_drain` 取消 callout。线程通过获取所讨论的锁，然后启动每个 callout 来做到这一点。它等待所有 callout 触发（执行器忙等待）。这迫使 callout 已过期并都在等待执行器持有的锁的情况。在所有 callout 都被阻塞后，执行器对每个 callout 调用 `callout_async_drain` 并释放锁。

在所有 callout 完成后，通过 [printf(9)](printf.9.md) 打印显示结果的总状态。人工测试人员可以运行 [dmesg(8)](../man8/dmesg.8.md) 查看结果。在这种情况下，如果你运行的是测试 0，预期所有 callout 在同一 CPU 上过期，因此只会调用一个 callout_drain 函数。zero_returns 的数量应该匹配被调用的 callout_drain 的数量，即 1。one_returns 应该是 callout 的剩余数量。如果测试编号为 1，callout 会分散到所有 CPU。zero_returns 的数量将再次匹配进行的 drain 调用数，后者匹配投入使用的 CPU 数量。

此测试可以使用多个线程，尽管在示例情况下可能并不必要。

你不应需要更改框架。只需添加测试并在加载后注册它们。

## 作者

内核测试框架由 Randall Stewart <rrs@FreeBSD.org> 在 John Mark Gurney <jmg@FreeBSD.org> 的帮助下编写。
