# sndstat(4)

`sndstat` — 基于 nvlist 的 PCM 音频设备枚举接口

## 名称

`sndstat`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device sound

## 描述

由 `/dev/sndstat` 设备提供的 ioctl 接口允许调用者枚举可用于使用的 PCM 音频设备。换言之，它提供了获取系统中所有可用音频设备列表的手段。

## IOCTL

对于带参数的 ioctl 调用，使用以下结构：

```sh
struct sndstioc_nv_arg {
	size_t nbytes;
	void *buf;
};
```

下面是一个 nvlist 对象的示例，并附有常见字段的解释：

```sh
dsps (NVLIST ARRAY): 1
	from_user (BOOL): FALSE
	nameunit (STRING): [pcm0]
	devnode (STRING): [dsp0]
	desc (STRING): [Generic (0x8086) (Analog Line-out)]
	pchan (NUMBER): 1
	rchan (NUMBER): 0
	info_play (NVLIST):
		min_rate (NUMBER): 48000
		max_rate (NUMBER): 48000
		formats (NUMBER): 16
		min_chn (NUMBER): 2
		max_chn (NUMBER): 2
	provider_info (NVLIST):
		unit (NUMBER): 0
		status (STRING): on hdaa0
		bitperfect (BOOL): FALSE
		pvchan (BOOL): TRUE
		pvchanrate (NUMBER): 48000
		pvchanformat (NUMBER): 0x00000010
		rvchan (BOOL): TRUE
		rvchanrate (NUMBER): 48000
		rvchanformat (NUMBER): 0x00000010
		channel_info (NVLIST_ARRAY): 1
			name (STRING): dsp0.virtual_play.0
			parentchan (STRING): dsp0.play.0
			unit (NUMBER): 1
			caps (NUMBER): 0x073200
			latency (NUMBER): 2
			rate (NUMBER): 48000
			format (NUMBER): 0x201000
			pid (NUMBER): 1234
			comm (STRING): mpv
			interrupts (NUMBER): 0
			feedcount (NUMBER): 0
			xruns (NUMBER): 0
			left_volume (NUMBER): 45
			right_volume (NUMBER): 45
			hwbuf_fmt (NUMBER): 0x200010
			hwbuf_rate (NUMBER): 48000
			hwbuf_size (NUMBER): 0
			hwbuf_blksz (NUMBER): 0
			hwbuf_blkcnt (NUMBER): 0
			hwbuf_free (NUMBER): 0
			hwbuf_ready (NUMBER): 0
			swbuf_fmt (NUMBER): 0x201000
			swbuf_rate (NUMBER): 48000
			swbuf_size (NUMBER): 16384
			swbuf_blksz (NUMBER): 2048
			swbuf_blkcnt (NUMBER): 8
			swbuf_free (NUMBER): 16384
			swbuf_ready (NUMBER): 0
			feederchain (STRING):
				[userland ->
				feeder_root(0x00201000) ->
				feeder_format(0x00201000 -> 0x00200010) ->
				feeder_volume(0x00200010) -> hardware]
	provider (STRING): [sound(4)]
```

**`min_rate`** 支持的最低采样率。

**`max_rate`** 支持的最高采样率。

**`formats`** 支持的样本格式。

**`min_chn`** 声道布局中支持的最小声道数。

**`max_chn`** 声道布局中支持的最大声道数。

**`min_rate`** 支持的最低采样率。

**`max_rate`** 支持的最高采样率。

**`formats`** 支持的样本格式。

**`min_chn`** 声道布局中支持的最小声道数。

**`max_chn`** 声道布局中支持的最大声道数。

**`name`** 声道名称。

**`parentchan`** 父声道名称（例如虚拟声道的情况）。

**`unit`** 声道单元。

**`caps`** OSS 能力。

**`latency`** 延迟。

**`rate`** 采样率。

**`format`** 采样格式。

**`pid`** 占用该声道的进程的 PID。

**`comm`** 占用该声道的进程的名称。

**`interrupts`** 自声道打开以来的中断次数。

**`xruns`** 溢出/欠载次数，具体取决于声道方向。

**`feedcount`** 自声道打开以来读/写的字节数。

**`left_volume`** 左侧音量。

**`right_volume`** 右侧音量。

**`hwbuf_format`** 硬件缓冲区格式。

**`hwbuf_rate`** 硬件缓冲区采样率；

**`hwbuf_size`** 硬件缓冲区大小。

**`hwbuf_blksz`** 硬件缓冲区块大小。

**`hwbuf_blkcnt`** 硬件缓冲区块数。

**`hwbuf_free`** 硬件缓冲区中的可用空间（以字节为单位）。

**`hwbuf_ready`** 可从硬件缓冲区读/写的字节数。

**`swbuf_format`** 软件缓冲区格式。

**`swbuf_rate`** 软件缓冲区采样率；

**`swbuf_size`** 软件缓冲区大小。

**`swbuf_blksz`** 软件缓冲区块大小。

**`swbuf_blkcnt`** 软件缓冲区块数。

**`swbuf_free`** 软件缓冲区中的可用空间（以字节为单位）。

**`swbuf_ready`** 可从软件缓冲区读/写的字节数。

**`feederchain`** 声道 feeder 链。

**`unit`** 声卡单元。

**`status`** 状态字符串。通常报告设备所附加到的驱动。

**`bitperfect`** 声卡是否启用了 bit-perfect 模式。

**`pvchan`** 是否启用播放虚拟声道。

**`pvchanrate`** 播放虚拟声道采样率。

**`pvchanformat`** 播放虚拟声道格式。

**`rvchan`** 是否启用录制虚拟声道。

**`rvchanrate`** 录制虚拟声道采样率。

**`rvchanformat`** 录制虚拟声道格式。

**`channel_info`** 声道信息。此字段内包含若干名/值对：

**`from_user`** PCM 音频设备节点是由内核内音频子系统还是由用户空间提供者创建。

**`nameunit`** 设备标识，形式为子系统加上单元号。

**`devnode`** devfs 中 PCM 音频设备节点的相对路径。

**`desc`** PCM 音频设备的描述。

**`pchan`** 硬件支持的播放声道数。如果此 PCM 音频设备完全不支持播放，则可为 0。

**`rchan`** 硬件支持的录制声道数。如果此 PCM 音频设备完全不支持录制，则可为 0。

**`info_play`** 播放方向所支持的配置。仅当此 PCM 音频设备支持播放时才存在。此字段内包含若干名/值对：

**`info_rec`** 录制方向所支持的配置。仅当此 PCM 音频设备支持录制时才存在。此字段内包含若干名/值对：

**`provider_info`** 提供者特定的字段。如果 PCM 音频设备并非由内核内接口提供，则此字段可能不存在。如果 provider 字段为空字符串，则此字段不存在。对于 sound(4) 提供者，此字段内包含若干名/值对：

**`provider`** 指定 PCM 音频设备提供者的字符串。

提供以下 ioctl 供使用：

**`SNDSTIOC_REFRESH_DEVS`** 丢弃之前获取的任何 PCM 音频设备列表快照。此 ioctl 不接受参数。

**`SNDSTIOC_GET_DEVS`** 生成和/或向调用者返回 PCM 音频设备列表快照。此 ioctl 接受指向 `struct sndstioc_nv_arg` 的指针作为第一个也是唯一的参数。调用者需要提供足够大的缓冲区来容纳序列化的 nvlist。如果所打开的 sndstat `fd` 的内部结构中没有现成的 PCM 音频设备列表快照，将自动生成一份新的 PCM 音频设备列表快照。调用者必须将 `nbytes` 设为 0 或所提供缓冲区的大小。如果 `nbytes` 为 0，则在 `nbytes` 中返回容纳当前快照的序列化 nvlist 流所需的缓冲区大小，并忽略 `buf`。否则，如果缓冲区不够大，ioctl 返回成功，并将 `nbytes` 设为 0。如果所提供缓冲区足够大，则将 `nbytes` 设为写入所提供缓冲区的序列化 nvlist 的大小。一旦 PCM 音频设备列表快照成功返回到用户空间，给定 `fd` 的子系统内部结构中所存储的快照将被释放。

**`SNDSTIOC_ADD_USER_DEVS`** 将调用者提供的 PCM 音频设备列表添加到 `/dev/sndstat` 设备。此 ioctl 接受指向 `struct sndstioc_nv_arg` 的指针作为第一个也是唯一的参数。调用者必须提供容纳序列化 nvlist 的缓冲区。`nbytes` 应设为序列化 nvlist 的字节长度。`buf` 应指向存储序列化 nvlist 的缓冲区。用户空间支撑的 PCM 音频设备节点应列在序列化 nvlist 之内。

**`SNDSTIOC_FLUSH_USER_DEVS`** 清除之前由调用者添加的任何 PCM 音频设备。此 ioctl 不接受参数。

## 文件

**`/dev/sndstat`**

## 实例

以下代码枚举所有可用的 PCM 音频设备：

```sh
#include <sys/types.h>
#include <err.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/nv.h>
#include <sys/sndstat.h>
#include <sysexits.h>
#include <unistd.h>
int
main()
{
	int fd;
	struct sndstioc_nv_arg arg;
	const nvlist_t * const *di;
	size_t i, nitems;
	nvlist_t *nvl;
	/* 首先以只读方式打开 sndstat 节点 */
	fd = open("/dev/sndstat", O_RDONLY);
	if (ioctl(fd, SNDSTIOC_REFRESH_DEVS, NULL))
		err(1, "ioctl(fd, SNDSTIOC_REFRESH_DEVS, NULL)");
	/* 当 nbytes = 0 时获取快照大小 */
	arg.nbytes = 0;
	arg.buf = NULL;
	if (ioctl(fd, SNDSTIOC_GET_DEVS, &arg))
		err(1, "ioctl(fd, SNDSTIOC_GET_DEVS, &arg)");
	/* 获取快照数据 */
	arg.buf = malloc(arg.nbytes);
	if (arg.buf == NULL)
		err(EX_OSERR, "malloc");
	if (ioctl(fd, SNDSTIOC_GET_DEVS, &arg))
		err(1, "ioctl(fd, SNDSTIOC_GET_DEVS, &arg)");
	/* 反序列化 nvlist 流 */
	nvl = nvlist_unpack(arg.buf, arg.nbytes, 0);
	free(arg.buf);
	/* 获取 DSPs 数组 */
	di = nvlist_get_nvlist_array(nvl, SNDST_DSPS, &nitems);
	for (i = 0; i < nitems; i++) {
		const char *nameunit, *devnode, *desc;
		/*
		 * 检查每个设备的 nvlist 项
		 */
		nameunit = nvlist_get_string(di[i], SNDST_DSPS_NAMEUNIT);
		devnode = nvlist_get_string(di[i], SNDST_DSPS_DEVNODE);
		desc = nvlist_get_string(di[i], SNDST_DSPS_DESC);
		printf("Name unit: `%s`, Device node: `%s`, Description: `%s`n",
		    nameunit, devnode, desc);
	}
	nvlist_destroy(nvl);
	return (0);
}
```

## 参见

sound(4), [nv(9)](../man9/nv.9.md)

## 历史

`sndstat` 设备的基于 nvlist 的 ioctl 支持首次出现于 FreeBSD 13.0。

## 作者

本手册页由 Ka Ho Ng <khng@FreeBSD.org> 编写。
