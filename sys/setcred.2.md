# setcred(2)

`setcred` — 以原子方式设置当前进程凭证

## 名称

`setcred`

## 库

Lb libc

## 概要

```c
#include <sys/ucred.h>

int
setcred(u_int flags, const struct setcred *wcred, size_t size);
```

## 描述

`setcred()` 系统调用可以以原子方式设置当前进程的任何用户可访问凭证组合。

此系统调用通常仅允许有效用户 ID 为超级用户 (0) ID 的进程调用；或者如果 [sysctl(8)](../man8/sysctl.8.md) 变量 `security.bsd.suser_enabled` 为零，或某些活动的 MAC 策略明确拒绝这些进程，则根本不允许调用。

某些 MAC 策略，如 [mac_do(4)](../man4/mac_do.4.md)，也可能允许非特权用户成功调用，这可能取决于所请求的确切凭证转换，但同样前提是没有任何活动的 MAC 策略明确拒绝。

`flags` 参数用于指示调用应更改哪些进程凭证。允许的标志有：

**`SETCREDF_UID`** 设置有效用户 ID。

**`SETCREDF_RUID`** 设置实际用户 ID。

**`SETCREDF_SVUID`** 设置保存的用户 ID。

**`SETCREDF_GID`** 设置有效组 ID。

**`SETCREDF_RGID`** 设置实际组 ID。

**`SETCREDF_SVGID`** 设置保存的组 ID。

**`SETCREDF_SUPP_GROUPS`** 设置补充组列表。

**`SETCREDF_MAC_LABEL`** 设置 MAC 标签。

`struct setcred` 结构当前定义为：

```c
struct setcred {
	uid_t	 sc_uid;		/* 有效用户 ID */
	uid_t	 sc_ruid;		/* 实际用户 ID */
	uid_t	 sc_svuid;		/* 保存的用户 ID */
	gid_t	 sc_gid;		/* 有效组 ID */
	gid_t	 sc_rgid;		/* 实际组 ID */
	gid_t	 sc_svgid;		/* 保存的组 ID */
	u_int	 sc_pad;		/* 填充，未使用 */
	u_int	 sc_supp_groups_nb;	/* 补充组数量 */
	gid_t	*sc_supp_groups;	/* 补充组 */
	struct mac *sc_label;		/* MAC 标签 */
};
```

其字段为：

**`sc_uid`** 如果指定了标志 `SETCREDF_UID`，要设置有效用户的目标 ID。

**`sc_ruid`** 如果指定了标志 `SETCREDF_RUID`，要设置实际用户的目标 ID。

**`sc_svuid`** 如果指定了标志 `SETCREDF_SVUID`，要设置保存用户的目标 ID。

**`sc_gid`** 如果指定了标志 `SETCREDF_GID`，要设置有效组的目标 ID。

**`sc_rgid`** 如果指定了标志 `SETCREDF_RGID`，要设置实际组的目标 ID。

**`sc_svgid`** 如果指定了标志 `SETCREDF_SVGID`，要设置保存组的目标 ID。

**`sc_supp_groups_nb`** 如果指定了标志 `SETCREDF_SUPP_GROUPS`，数组 `sc_supp_groups` 的大小。它必须小于或等于 `{NGROUPS_MAX}`。

**`sc_supp_groups`** 如果指定了标志 `SETCREDF_SUPP_GROUPS`，要设置补充组的目标 ID 数组。

**`sc_label`** 如果指定了标志 `SETCREDF_MAC_LABEL`，指向有效 MAC 标签结构的指针，例如使用 mac_from_text(3) 函数构建的结构。

出于向前兼容性和安全性的考虑，建议用户始终使用提供的初始化器 `SETCRED_INITIALIZER` 来初始化 `struct setcred` 类型的对象。

`size` 参数必须是所传递的 `wcred` 结构的大小。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`setcred()` 系统调用将失败，如果：

**[`EINVAL`]** `flags` 中传入了无法识别的标志，或 `size` 参数与 `struct setcred` 的大小不匹配，或字段 `sc_supp_group_nb` 的值严格大于 `{NGROUPS_MAX}`（如果提供了标志 `SETCREDF_SUPP_GROUPS`），或字段 `sc_label` 所指向的 MAC 标签无效（如果提供了标志 `SETCREDF_MAC_LABEL`）。

**[`EFAULT`]** `wcred` 指针，或字段 `sc_supp_groups`（如果提供了标志 `SETCREDF_SUPP_GROUPS`）或 `sc_label`（如果提供了标志 `SETCREDF_MAC_LABEL`）中的指针指向了无效的位置。

**[`EPERM`]** 用户不是超级用户，和/或所请求的凭证转换不被系统或 MAC 模块允许。

**[`EOPNOTSUPP`]** 某些所请求的凭证具有系统不支持的类型。当前这仅在内核编译时未包含 MAC 且传入了 `SETCREDF_MAC_LABEL` 时才会发生。

## 参见

[issetugid(2)](issetugid.2.md), [setregid(2)](setregid.2.md), [setreuid(2)](setreuid.2.md), [setuid(2)](setuid.2.md), [mac_text(3)](../posix1e/mac_text.3.md), [mac(4)](../man4/mac.4.md), [mac_do(4)](../man4/mac_do.4.md), [maclabel(7)](../man7/maclabel.7.md)

## 标准

`setcred()` 系统调用是 FreeBSD 特有的。

调用 `setcred()` 通常会更改 POSIX/SUS 标准所列出的进程凭证。更改后的值随后会相对于系统的其余部分产生这些标准中所描述的效果，就如同这些更改是通过调用标准或传统的凭证设置函数产生的。当前，除 `SETCREDF_MAC_LABEL` 外的所有标志都会导致修改标准凭证。

使用 `setcred()` 而非标准或传统函数来更改标准凭证的唯一区别在于：

- 所有请求的更改以原子方式执行。
- 只有超级用户或经某个 MAC 模块授权的非特权用户才能成功调用 `setcred()`，即使标准系统调用会授权任何非特权用户进行相同的更改。例如，seteuid(2) 允许任何非特权用户将有效用户 ID 更改为实际或保存的用户 ID，而以标志 `SETCREDF_UID` 调用 `setcred()` 则不允许。

## 历史

`setcred()` 系统调用出现于 FreeBSD 14.3。

传统上，在 UNIX 中，除有效、实际和保存 ID 的调换之外的所有凭证更改，都是由 setuid 二进制文件按特定顺序依次调用多个凭证设置系统调用来完成的。例如，要将所有用户 ID 更改为某个非特权用户的 ID，`setuid()` 必须最后调用，以便所有其他凭证更改调用能在此前成功执行，因为它们需要超级用户特权。

这种分步方式导致此类进程会暂时持有既非原始也非必然为最终期望值的高特权凭证。这不仅打开了一个转换窗口，其中潜在的漏洞可能产生灾难性后果，还使内核无法强制执行仅允许特定的凭证转换。

在扩展 [mac_do(4)](../man4/mac_do.4.md) 以允许规则仅授权主组或补充组的特定更改时，对原子、全局的凭证更改方式的需求变得明显，这促成了 `setcred()` 的引入。

## 作者

`setcred()` 系统调用及本手册页由 Olivier Certner <olce.freebsd@certner.fr> 编写。

## 安全考虑

标准或传统凭证设置系统调用的注意事项同样适用于 `setcred()`，但连续此类调用缺乏原子性的情况除外。

特别地，关于更改标准凭证对已打开文件没有效果的问题，请参阅 [setuid(2)](setuid.2.md) 手册页中的**安全考虑**章节。
