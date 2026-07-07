# rndtest(4)

`rndtest` — FIPS 140-2 随机数生成器测试监视器

## 名称

`rndtest`

## 概要

`device rndtest`

## 描述

`rndtest` 驱动"挂接"到硬件加密设备上，监视传递给 [random(4)](random.4.md) 子系统的熵数据。此数据会定期接受 FIPS 140-2 合规性测试并收集统计信息。如果采集到的熵未通过任何 FIPS 测试套件，则该数据将被丢弃，并持续进行测试直至从设备收到"良好数据"。失败情况可选择性地在控制台上报告。

## 参见

[crypto(4)](crypto.4.md), [random(4)](random.4.md), [safe(4)](safe.4.md), [crypto(9)](../man9/crypto.9.md)

## 历史

此想法及原始代码来自 Jason L. Wright。`rndtest` 设备驱动最早出现在 FreeBSD 5.0 中。

## 缺陷

加密设备驱动必须经过特殊编译才能使用此驱动；这本不应必要。此特性最好集成到 [random(4)](random.4.md) 子系统中，以便可应用于声称提供"纯熵"的设备。
