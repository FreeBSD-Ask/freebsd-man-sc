# dtrace_cam.4

`dtrace_cam` — 用于跟踪 CAM 相关事件的 DTrace 提供者

## 名称

`dtrace_cam`

## 概要

`Fn cam::xpt:action union ccb *ccn Fn cam::xpt:done union ccb *ccb Fn cam::xpt:async-cb void *cbarg uint32_t async_code struct cam_path *path void *async_Arg`

## 描述

`cam` 提供者允许跟踪 CAM 事件。Fn cam::xpt_action 探测在 CAM 控制块（ccb）提交给 CAM SIM 驱动时触发。Fn cam::xpt:done 探测在该请求完成时触发。Fn cam::xpt:async-cb 探测在异步回调被调用之前触发。

## 参见

[dtrace(1)](../man1/dtrace.1.md), cam(4), [SDT(9)](../man9/SDT.9.md)

## 历史

`cam` 提供者首次出现于 FreeBSD 15.1 和 16.0。

## 作者

本手册页由 Warner Losh <imp@FreeBSD.org> 编写。
