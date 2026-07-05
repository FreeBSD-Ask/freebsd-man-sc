# hv_vss.4

`hv_vss` — Hyper-V 卷影复制服务 API

## 名称

`hv_vss`

## 概要

`#include <dev/hyperv/hv_snapshot.h>`

```sh
#define VSS_SUCCESS		0x00000000
#define VSS_FAIL		0x00000001
enum hv_vss_op_t {
	HV_VSS_NONE = 0,
	HV_VSS_CHECK,
	HV_VSS_FREEZE,
	HV_VSS_THAW,
	HV_VSS_COUNT
};
struct hv_vss_opt_msg {
	uint32_t	opt;		/* 操作 */
	uint32_t	status;		/* 0 表示成功，1 表示错误 */
	uint64_t	msgid;		/* 用于标识事务的 ID */
	uint8_t		reserved[48];	/* 保留值全为零 */
};
```

## 描述

应用程序的冻结或解冻功能对于保证应用程序一致性备份非常重要。在 Windows 平台上，VSS 用于执行实时备份。但对于运行于 Hyper-V 上的虚拟机客户机，尚未定义相应的 VSS。例如，一个正在运行的数据库服务器实例知道应用程序的冻结/解冻应何时开始或结束，但它无法感知来自 Hyper-V 主机的冻结/解冻通知。`hv_vss` 旨在通知应用程序冻结/解冻请求。因此，它扮演中介角色，将来自 Hyper-V 主机的冻结/解冻命令转发给在 FreeBSD 虚拟机上注册了 VSS 服务的用户态应用程序，并将结果发送回 Hyper-V 主机。

通常，hv_vss_daemon(8) 负责冻结/解冻 UFS 文件系统，并在系统启动后自动启动。当 Hyper-V 主机想要对 FreeBSD 虚拟机创建快照时，会先向 FreeBSD 虚拟机发送 VSS 能力检查。`hv_vss` 接收到请求后，如果应用程序已注册，则将请求转发给用户态应用程序。只有当 `hv_vss` 收到来自应用程序的 VSS_SUCCESS 响应后，才会通知 hv_vss_daemon(8) 检查是否支持文件系统冻结/解冻。在此期间发生任何错误，`hv_vss` 将通知 Hyper-V 主机不支持 VSS。此外，在向 Hyper-V 主机发送响应前有一个默认超时限制。如果应用程序和 hv_vss_daemon(8) 的总响应时间超过此值，将发生超时，并向 Hyper-V 主机响应不支持 VSS。

Hyper-V 主机确认 FreeBSD 虚拟机支持 VSS 后，会向虚拟机发送冻结请求，`hv_vss` 会首先将其转发给应用程序。应用程序完成冻结后，应通知 `hv_vss`，然后由 hv_vss_daemon(8) 触发文件系统级冻结。当应用程序和 hv_vss_daemon(8) 两端的冻结都完成后，`hv_vss` 将通知 Hyper-V 主机冻结完成。当然，与 VSS 能力检查相同，也设置了一个超时限制，以确保 FreeBSD 虚拟机上的冻结不会挂起。如果发生任何错误或超时，Hyper-V 端的冻结将失败。

Hyper-V 主机在创建快照后会发送解冻请求，通常此时间段非常短，以免阻塞正在运行的应用程序。`hv_vss` 首先通过通知 hv_vss_daemon(8) 解冻文件系统，然后通知用户注册的应用程序。在向 Hyper-V 主机发送响应前也有超时检查。

VSS 能力检查、冻结或解冻中使用的所有默认超时限制相同。目前为 15 秒。

## 注释

`hv_vss` 目前仅支持 UFS。如果任何文件系统分区不是 UFS，VSS 能力检查将失败。如果应用程序未注册 VSS，`hv_vss` 仅支持文件系统级一致性备份。设备在再次打开之前应先关闭。如果要同时打开 "/dev/hv_appvss_dev" 两次或更多次，将返回错误（-1），并设置 errno。

如果 hv_vss_daemon(8) 在系统启动后被终止，VSS 功能将无法工作。

## 实例

以下是一个完整示例，在收到来自 `hv_vss` 的这些通知时除了等待 2 秒外什么都不做：

```sh
#include <string.h>
#include <stdio.h>
#include <sys/ioctl.h>
#include <sys/param.h>
#include <sys/ucred.h>
#include <sys/mount.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <poll.h>
#include <stdint.h>
#include <syslog.h>
#include <errno.h>
#include <err.h>
#include <fcntl.h>
#include <ufs/ffs/fs.h>
#include <paths.h>
#include <sys/ioccom.h>
#include <dev/hyperv/hv_snapshot.h>
#define UNDEF_FREEZE_THAW	(0)
#define FREEZE			(1)
#define THAW			(2)
#define CHECK			(3)
#define	VSS_LOG(priority, format, args...) do	{				\
		if (is_debugging == 1) {					\
			if (is_daemon == 1)					\
				syslog(priority, format, ## args);		\
			else							\
				printf(format, ## args);			\
		} else {							\
			if (priority < LOG_DEBUG) {				\
				if (is_daemon == 1)				\
					syslog(priority, format, ## args);	\
				else						\
					printf(format, ## args);		\
			}							\
		}								\
	} while(0)
#define CHECK_TIMEOUT		1
#define CHECK_FAIL		2
#define FREEZE_TIMEOUT		1
#define FREEZE_FAIL		2
#define THAW_TIMEOUT		1
#define THAW_FAIL		2
static int is_daemon        = 1;
static int is_debugging     = 0;
static int simu_opt_waiting = 2; // 秒
#define GENERIC_OPT(TIMEOUT, FAIL)						\
	do {									\
		sleep(simu_opt_waiting);					\
		if (opt == CHECK_TIMEOUT) {					\
			sleep(simu_opt_waiting * 10);				\
			VSS_LOG(LOG_INFO, "%s timeout simulationn",		\
			    __func__);						\
			return (0);						\
		} else if (opt == CHECK_FAIL) {					\
			VSS_LOG(LOG_INFO, "%s failure simulationn",		\
			    __func__);						\
			return (CHECK_FAIL);					\
		} else {							\
			VSS_LOG(LOG_INFO, "%s success simulationn",		\
			    __func__);						\
			return (0);						\
		}								\
	} while (0)
static int
check(int opt)
{
	GENERIC_OPT(CHECK_TIMEOUT, CHECK_FAIL);
}
static int
freeze(int opt)
{
	GENERIC_OPT(FREEZE_TIMEOUT, FREEZE_FAIL);
}
static int
thaw(int opt)
{
	GENERIC_OPT(THAW_TIMEOUT, THAW_FAIL);
}
static void usage(const char* cmd) {
	fprintf(stderr,
	    "%s -f <0|1|2>: simulate app freeze."
	    " 0: successful, 1: freeze timeout, 2: freeze failedn"
	    " -c <0|1|2>: simulate vss feature check"
	    " -t <0|1|2>: simulate app thaw."
	    " 0: successful, 1: freeze timeout, 2: freeze failedn"
	    " -d : enable debug moden"
	    " -n : run this tool under non-daemon moden", cmd);
}
int
main(int argc, char* argv[]) {
	int ch, freezesimuop = 0, thawsimuop = 0, checksimuop = 0, fd, r, error;
	uint32_t op;
	struct pollfd app_vss_fd[1];
	struct hv_vss_opt_msg  userdata;
	while ((ch = getopt(argc, argv, "f:c:t:dnh")) != -1) {
		switch (ch) {
		case 'f':
			/* 以常规进程运行以便调试 */
			freezesimuop = (int)strtol(optarg, NULL, 10);
			break;
		case 't':
			thawsimuop = (int)strtol(optarg, NULL, 10);
			break;
		case 'c':
			checksimuop = (int)strtol(optarg, NULL, 10);
			break;
		case 'd':
			is_debugging = 1;
			break;
		case 'n':
			is_daemon = 0;
			break;
		case 'h':
		default:
			usage(argv[0]);
			exit(0);
		}
	}
	openlog("APPVSS", 0, LOG_USER);
	/* 首先成为守护进程 */
	if (is_daemon == 1)
		daemon(1, 0);
	else
		VSS_LOG(LOG_DEBUG, "Run as regular process.n");
	VSS_LOG(LOG_INFO, "HV_VSS starting; pid is: %dn", getpid());
	fd = open(VSS_DEV(APP_VSS_DEV_NAME), O_RDWR);
	if (fd < 0) {
		VSS_LOG(LOG_ERR, "Fail to open %s, error: %d %sn",
		    VSS_DEV(APP_VSS_DEV_NAME), errno, strerror(errno));
		exit(EXIT_FAILURE);
	}
	app_vss_fd[0].fd     = fd;
	app_vss_fd[0].events = POLLIN | POLLRDNORM;
	while (1) {
		r = poll(app_vss_fd, 1, INFTIM);
		VSS_LOG(LOG_DEBUG, "poll returned r = %d, revent = 0x%xn",
		    r, app_vss_fd[0].revents);
		if (r == 0 || (r < 0 && errno == EAGAIN) ||
		    (r < 0 && errno == EINTR)) {
			/* 无可读内容 */
			continue;
		}
		if (r < 0) {
			/*
			 * 对于 EAGAIN 以外的 poll 返回失败，
			 * 我们选择退出。
			 */
			VSS_LOG(LOG_ERR, "Poll failed.n");
			perror("poll");
			exit(EIO);
		}
		/* 从字符设备读取 */
		error = ioctl(fd, IOCHVVSSREAD, &userdata);
		if (error < 0) {
			VSS_LOG(LOG_ERR, "Read failed.n");
			perror("pread");
			exit(EIO);
		}
		if (userdata.status != 0) {
			VSS_LOG(LOG_ERR, "data read errorn");
			continue;
		}
		op = userdata.opt;
		switch (op) {
		case HV_VSS_CHECK:
			error = check(checksimuop);
			break;
		case HV_VSS_FREEZE:
			error = freeze(freezesimuop);
			break;
		case HV_VSS_THAW:
			error = thaw(thawsimuop);
			break;
		default:
			VSS_LOG(LOG_ERR, "Illegal operation: %dn", op);
			error = VSS_FAIL;
		}
		if (error)
			userdata.status = VSS_FAIL;
		else
			userdata.status = VSS_SUCCESS;
		error = ioctl(fd, IOCHVVSSWRITE, &userdata);
		if (error != 0) {
			VSS_LOG(LOG_ERR, "Fail to write to devicen");
			exit(EXIT_FAILURE);
		} else {
			VSS_LOG(LOG_INFO, "Send response %d for %s to kerneln",
			    userdata.status, op == HV_VSS_FREEZE ? "Freeze" :
			    (op == HV_VSS_THAW ? "Thaw" : "Check"));
		}
	}
	return 0;
}
```

## 参见

[hv_utils(4)](hv_utils.4.md), hv_vss_daemon(8)

## 历史

该守护进程于 2016 年 10 月引入，由 Microsoft Corp. 开发。

## 作者

`hv_vss` 的 FreeBSD 支持最早由 Microsoft BSD Integration Services Team <bsdic@microsoft.com> 添加。
