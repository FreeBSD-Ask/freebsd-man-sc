# ibv_ud_pingpong.1

`ibv_ud_pingpong` — 简单的 InfiniBand UD 传输测试

## 名称

`ibv_ud_pingpong`

## 概要

`ibv_ud_pingpong [-p port] [-d device] [-i ib port] [-s size] [-r rx depth] [-n iters] [-l sl] [-e] [-g gid index] HOSTNAME`

`ibv_ud_pingpong [-p port] [-d device] [-i ib port] [-s size] [-r rx depth] [-n iters] [-l sl] [-e] [-g gid index]`

## 描述

通过不可靠数据报（UD）传输在 InfiniBand 上运行简单的 ping-pong 测试。

## 选项

**`-p`**, `--port`=`PORT` 使用 TCP 端口 `PORT` 进行初始同步（默认 18515）

**`-d`**, `--ib-dev`=`DEVICE` 使用 IB 设备 `DEVICE`（默认为找到的第一个设备）

**`-i`**, `--ib-port`=`PORT` 使用 IB 端口 `PORT`（默认端口 1）

**`-s`**, `--size`=`SIZE` 大小为 `SIZE` 的 ping-pong 消息（默认 2048）

**`-r`**, `--rx-depth`=`DEPTH` 每次投递 `DEPTH` 个接收请求（默认 500）

**`-n`**, `--iters`=`ITERS` 执行 `ITERS` 次消息交换（默认 1000）

**`-l`**, `--sl`=`SL` 以服务级别 `SL` 发送消息（默认 0）

**`-e`**, `--events` 等待工作完成事件时休眠（默认为轮询完成）

**`-g`**, `--gid-idx`=`GIDINDEX` 本地端口 GID 索引 `GIDINDEX`

## 参见

ibv_rc_pingpong(1), ibv_uc_pingpong(1), ibv_srq_pingpong(1), ibv_xsrq_pingpong(1)

## 作者

Roland Dreier <rolandd@cisco.com>

## 缺陷

客户端和服务器实例之间的网络同步较弱，无法防止两个实例使用不兼容的选项。检索工作完成的方法并不严格正确，竞争条件可能在某些系统上导致失败。
