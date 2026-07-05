# ibv_devinfo.1

`ibv_devinfo` — 查询 RDMA 设备

## 名称

`ibv_devinfo`

## 概要

`ibv_devinfo [-d device] [-i port] [-l] [-v]`

## 描述

打印可从用户空间使用的 RDMA 设备信息。

## 选项

**`-d`**, `--ib-dev`=`DEVICE` 使用 IB 设备 `DEVICE`（默认为找到的第一个设备）

**`-i`**, `--ib-port`=`PORT` 查询端口 `PORT`（默认所有端口）

**`-l`**, `--list` 仅列出 RDMA 设备的名称

**`-v`**, `--verbose` 打印 RDMA 设备的所有可用信息

## 参见

[ibv_devices(1)](ibv_devices.1.md)

## 作者

Dotan Barak <dotanba@gmail.com>

Roland Dreier <rolandd@cisco.com>
