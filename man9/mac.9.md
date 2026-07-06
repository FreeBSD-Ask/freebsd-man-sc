# mac.9

`mac` — TrustedBSD 强制访问控制框架

## 名称

`mac`

## 概要

`#include <sys/types.h>`

`#include <sys/mac.h>`

在内核配置文件中：`options MAC` `options MAC_DEBUG`

## 描述

### 简介

TrustedBSD 强制访问控制框架允许动态引入的系统安全模块修改系统安全功能。这可用于支持各种新的安全服务，包括传统的带标签强制访问控制模型。该框架提供了一系列入口点，支持各种内核服务的代码必须调用这些入口点，特别是在访问控制点和对象创建方面。然后，框架会调用安全模块，为它们提供在这些 MAC API 入口点修改安全行为的机会。API 的使用者（普通内核服务）和安全模块都必须了解 API 调用的语义，特别是关于同步原语（如锁定）的语义。

### 框架支持的内核对象

MAC 框架管理多种内核内对象上的标签，包括进程凭证、vnode、devfs_dirent、挂载点、套接字、mbuf、bpf 描述符、网络接口、IP 分片队列和管道。内核对象上的标签数据由 `struct label` 表示，与策略无关，可由策略模块按其认为合适的方式使用。

### 使用者 API

MAC API 提供了大量的入口点，过于宽泛，无法在此一一记录。通常，这些入口点表示访问控制检查或其他 MAC 相关操作，接受授权该活动的一个或多个主体（凭证）、要对其进行操作的一组对象，以及提供所请求操作类型信息的一组操作参数。

### 使用者的锁定

MAC API 的使用者必须了解每个 API 入口点的锁定要求：通常，必须对传递给调用的每个主体或对象持有适当的锁，以便 MAC 模块可以将对象的各个方面用于访问控制目的。例如，通常需要 vnode 锁，以便 MAC 框架和模块可以从 vnode 中检索安全标签和属性以进行访问控制。类似地，调用者必须了解传递给 MAC API 的任何主体或对象的引用计数语义：所有调用都要求在（可能冗长的）MAC API 调用期间持有对对象的有效引用。在某些情况下，必须以共享或独占方式持有对象。

### 模块编写者 API

每个模块导出一个结构，描述该模块选择实现的 MAC API 操作，包括初始化和销毁 API 入口点、各种对象创建和销毁调用，以及大量的访问控制检查点。未来还将出现额外的审计入口点。模块作者可以选择只实现入口点的一个子集，将描述结构中的 API 函数指针设置为 `NULL`，允许框架避免调用该模块。

### 模块编写者的锁定

模块编写者必须了解他们实现的入口点的锁定语义：MAC API 入口点对每个参数都有特定的锁定或引用计数语义，模块必须遵循锁定和引用计数协议，否则会出现各种故障模式（包括竞态条件、不当的指针解引用等）。

MAC 模块编写者还必须注意，MAC API 入口点经常从内核栈深处被调用，因此必须小心避免违反更全局的锁定要求，例如全局锁顺序要求。例如，锁定策略模块未专门维护和排序的其他对象可能是不合适的，或者策略模块可能违反与这些其他对象相关的全局排序要求。

最后，MAC API 模块实现者必须小心避免不当地回调到 MAC 框架：框架利用锁定来防止策略模块附加和分离期间的不一致。MAC API 模块应避免产生可能发生死锁或不一致的场景。

### 添加新的 MAC 入口点

MAC API 旨在随着内核中新服务的添加而轻松扩展。为了确保策略有机会无处不在地保护系统主体和对象，内核开发者必须保持对新编写或修改的内核代码中何时发生安全检查或相关主体或对象操作的意识。必须仔细记录新的入口点，以防止有关锁顺序和语义的任何混淆。引入新的入口点需要四个不同的工作部分：引入反映操作参数的新 MAC API 条目，将这些 MAC API 入口点散布到新的或修改的内核服务中，扩展 MAC API 框架的前端实现，以及修改适当的模块以利用新的入口点，使它们能够一致地执行其策略。

## 入口点

系统服务和模块作者应参考 FreeBSD 架构手册，了解 MAC 框架 API 的信息。

## 参见

acl(3), mac(3), posix1e(3), [mac(4)](../man4/mac.4.md), [ucred(9)](ucred.9.md), [vaccess(9)](vaccess.9.md), [vaccess_acl_posix1e(9)](vaccess_acl_posix1e.9.md), [VFS(9)](vfs.9.md), [VOP_SETLABEL(9)](vop_setlabel.9.md)

> “FreeBSD 架构手册”。

## 历史

TrustedBSD MAC 框架首次出现于 FreeBSD 5.0。

## 作者

本手册页由 Robert Watson 编写。此软件由 Network Associates Laboratories（Network Associates Inc. 的安全研究部门）在 DARPA/SPAWAR 合同 N66001-01-C-8035（“CBOSS”）下贡献给 FreeBSD 项目，作为 DARPA CHATS 研究计划的一部分。

TrustedBSD MAC 框架由 Robert Watson 设计，由 Network Associates Laboratories 的网络安全（NETSEC）、安全执行环境（SEE）和自适应网络防御研究小组实现。参与 CBOSS 项目的 Network Associates Laboratory 员工包括（按字母顺序排列）：Lee Badger、Brian Feldman、Hrishikesh Dandekar、Tim Fraser、Doug Kilpatrick、Suresh Krishnaswamy、Adam Migus、Wayne Morrison、Andrew Reisse、Chris Vance 和 Robert Watson。

子合同员工包括：Chris Costello、Poul-Henning Kamp、Jonathan Lemon、Kirk McKusick、Dag-Erling Smørgrav。

其他贡献者包括：Pawel Dawidek、Chris Faulhaber、Ilmar Habibulin、Mike Halderman、Bosko Milekic、Thomas Moestl、Andrew Reiter 和 Tim Robbins。

## 缺陷

虽然 MAC 框架的设计旨在支持对 root 用户的限制，但并非所有攻击渠道目前都受到入口点检查的保护。因此，不应单独依赖 MAC 框架策略来防御恶意的特权用户。
