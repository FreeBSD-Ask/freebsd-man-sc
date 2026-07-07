# periodic.conf(5)

`periodic.conf` — 周期性作业配置信息

## 名称

`periodic.conf`

## 描述

文件 `periodic.conf` 包含了关于每日、每周和每月系统维护作业应如何运行的描述。它位于 **/etc/defaults** 目录中，部分内容可被 **/etc** 中同名文件覆盖，而后者本身又可被 **/etc/periodic.conf.local** 文件覆盖。

`periodic.conf` 文件实际上是从每个 periodic 脚本作为 shell 脚本 sourced 的，旨在简单地提供默认配置变量。

以下变量由 [periodic(8)](../man8/periodic.8.md) 本身使用：

**`local_periodic`** （`str`）搜索 periodic 脚本的目录列表。此列表始终以 **/etc/periodic** 为前缀，并且仅当 [periodic(8)](../man8/periodic.8.md) 的参数不是绝对目录名时才使用。

**<`dir`** >`_output`> （`path` 或 `list`）如何处理从目录 `dir` 执行的脚本的输出。如果此变量设置为绝对路径名，输出将记录到该文件中；否则将其视为一个或多个以空格分隔的电子邮件地址，并发送给这些用户。如果此变量未设置或为空，输出发送到标准输出。对于无人值守的机器，`daily_output`、`weekly_output` 和 `monthly_output` 的合适值可能分别是 “`/var/log/daily.log`”、“`/var/log/weekly.log`” 和 “`/var/log/monthly.log`”，因为 newsyslog(8) 会在适当的时候轮转这些文件（如果它们存在）。

**<`dir`** >`_show_success`>

**<`dir`** >`_show_info`>

**<`dir`** >`_show_badconfig`> （`bool`）这些变量控制 [periodic(8)](../man8/periodic.8.md) 是否根据执行脚本的返回码来屏蔽其输出（其中 `dir` 是每个脚本所在的基础目录名）。如果脚本的返回码为 ‘0’ 且 <`dir` >`_show_success`> 设置为 “`NO`”，[periodic(8)](../man8/periodic.8.md) 将屏蔽该脚本的输出。如果脚本的返回码为 ‘1’ 且 <`dir` >`_show_info`> 设置为 “`NO`”，[periodic(8)](../man8/periodic.8.md) 将屏蔽该脚本的输出。如果脚本的返回码为 ‘2’ 且 <`dir` >`_show_badconfig`> 设置为 “`NO`”，[periodic(8)](../man8/periodic.8.md) 将屏蔽该脚本的输出。如果这些变量既未设置为 “`YES`” 也未设置为 “`NO`”，则分别默认为 “`YES`”、“`YES`” 和 “`NO`”。关于如何解释脚本返回码，请参阅 [periodic(8)](../man8/periodic.8.md) 手册页。

**`anticongestion_sleeptime`** （`int`）为平滑共享资源（如下载镜像）上的突发负载而随机睡眠的最大秒数。

以下变量由位于 **/etc/periodic/daily** 中的标准脚本使用：

**`daily_clean_disks_enable`** （`bool`）如果你想要每日删除所有匹配 `daily_clean_disks_files` 的文件，设置为 “`YES`”。

**`daily_clean_disks_files`** （`str`）设置为要匹配的文件名列表。允许使用通配符。

**`daily_clean_disks_days`** （`num`）当 `daily_clean_disks_enable` 设置为 “`YES`” 时，还必须将其设置为文件的访问和修改时间必须达到多少天才能被删除。

**`daily_clean_disks_verbose`** （`bool`）如果你希望在每日输出中报告被删除的文件，设置为 “`YES`”。

**`daily_clean_tmps_enable`** （`bool`）如果你想要每日清理临时目录，设置为 “`YES`”。

**`daily_clean_tmps_dirs`** （`str`）当 `daily_clean_tmps_enable` 设置为 “`YES`” 时，设置为要清理的目录列表。

**`daily_clean_tmps_days`** （`num`）当 `daily_clean_tmps_enable` 设置后，还必须将其设置为文件的访问和修改时间必须达到多少天才能被删除。

**`daily_clean_tmps_ignore`** （`str`）当 `daily_clean_tmps_enable` 设置为 “`YES`” 时，设置为不应删除的文件列表。允许使用通配符。

**`daily_clean_tmps_verbose`** （`bool`）如果你希望在每日输出中报告被删除的文件，设置为 “`YES`”。

**`daily_clean_preserve_enable`** （`bool`）如果你希望从 **/var/preserve** 中删除旧文件，设置为 “`YES`”。

**`daily_clean_preserve_days`** （`num`）设置为文件在删除前必须未修改的天数。

**`daily_clean_preserve_verbose`** （`bool`）如果你希望在每日输出中报告被删除的文件，设置为 “`YES`”。

**`daily_clean_msgs_enable`** （`bool`）如果你希望清理旧系统消息，设置为 “`YES`”。

**`daily_clean_msgs_days`** （`num`）设置为文件在删除前必须未修改的天数。如果此变量留空，则使用 msgs(1) 的默认值。

**`daily_clean_rwho_enable`** （`bool`）如果你希望清理 **/var/who** 中的旧文件，设置为 “`YES`”。

**`daily_clean_rwho_days`** （`num`）设置为文件在删除前必须未修改的天数。

**`daily_clean_rwho_verbose`** （`bool`）如果你希望在每日输出中报告被删除的文件，设置为 “`YES`”。

**`daily_clean_hoststat_enable`** （`bool`）设置为 “`YES`” 以运行 `sendmail` `-bH`，自动从 sendmail(8) 的主机状态缓存中清理过期条目。文件将使用与 sendmail(8) 在确定是否相信缓存信息时通常使用的相同标准来删除，如在 **/etc/mail/sendmail.cf** 中配置的那样。

**`daily_backup_efi_enable`** （`bool`）设置为 “`YES`” 以创建 EFI 系统分区（ESP）的备份。

**`daily_backup_gmirror_enable`** （`bool`）设置为 “`YES`” 以创建 gmirror 信息的备份（即 `gmirror` `list` 的输出），参见 gmirror(8)。

**`daily_backup_gmirror_verbose`** （`bool`）设置为 “`YES`” 以在每日输出中报告新备份与现有备份之间的差异。

**`daily_backup_gpart_enable`** （`bool`）设置为 “`YES`” 以创建分区表和 bootcode 分区内容的备份。

**`daily_backup_gpart_verbose`** （`bool`）设置为 “`YES`”，以便在 kern.geom.conftxt 或分区表的现有备份与新备份不同时显示详细信息。

**`daily_backup_passwd_enable`** （`bool`）如果你希望备份 **/etc/master.passwd** 和 **/etc/group** 文件并报告，设置为 “`YES`”。报告包括检查这两个文件的修改以及对 `group` 文件运行 chkgrp(8)。

**`daily_backup_aliases_enable`** （`bool`）如果你希望备份 **/etc/mail/aliases** 文件并在每日输出中显示修改，设置为 “`YES`”。

**`daily_backup_zfs_enable`** （`bool`）设置为 “`YES`” 以创建 zfs-list(8) 和 zpool-list(8) 实用程序生成的输出备份。

**`daily_backup_zfs_list_flags`** （`str`）设置为 zfs-list(8) 实用程序的参数。默认为标准行为。

**`daily_backup_zpool_list_flags`** （`str`）设置为 zpool-list(8) 实用程序的参数。默认为 `-v`。

**`daily_backup_zfs_props_enable`** （`bool`）设置为 “`YES`” 以创建 zfs-get(8) 和 zpool-get(8) 实用程序生成的输出备份。

**`daily_backup_zfs_get_flags`** （`str`）设置为 zfs-get(8) 实用程序的参数。默认为 `all`。

**`daily_backup_zpool_get_flags`** （`str`）设置为 zpool-get(8) 实用程序的参数。默认为 `all`。

**`daily_backup_zfs_verbose`** （`bool`）设置为 “`YES`” 以在每日输出中报告新备份与现有备份之间的差异。

**`daily_calendar_enable`** （`bool`）如果你希望每日运行 `calendar` `-a`，设置为 “`YES`”。

**`daily_accounting_enable`** （`bool`）如果你希望轮转每日进程记账文件，设置为 “`YES`”。除非在 [rc.conf(5)](rc.conf.5.md) 中启用了 `accounting_enable`，否则无需轮转。

**`daily_accounting_compress`** （`bool`）如果你希望使用 [gzip(1)](../man1/gzip.1.md) 压缩每日记账文件，设置为 “`YES`”。

**`daily_accounting_save`** （`num`）当 `daily_accounting_enable` 设置后，可将其设置为要保存的每日记账文件数量。默认为 “`3`”。

**`daily_accounting_flags`** （`str`）当 `daily_accounting_enable` 设置为 “`YES`” 时，设置为传递给 sa(8) 实用程序的参数（除 `-s` 之外）。默认为 `-q`。

**`daily_status_disks_enable`** （`bool`）如果你希望运行 [df(1)](../man1/df.1.md)（使用 `daily_status_disks_df_flags` 中提供的参数）和 `dump` `-W`，设置为 “`YES`”。

**`daily_status_disks_df_flags`** （`str`）当 `daily_status_disks_enable` 设置为 “`YES`” 时，设置为 [df(1)](../man1/df.1.md) 实用程序的参数。默认为 `-l` `-h`。

**`daily_status_zfs_enable`** （`bool`）如果你希望在 [zfs(8)](../man8/zfs.8.md) 池上运行 `zpool` `status`，设置为 “`YES`”。

**`daily_status_zfs_zpool_list_enable`** （`bool`）如果你希望在 [zfs(8)](../man8/zfs.8.md) 池上运行 `zpool` `list`，设置为 “`YES`”。需要将 `daily_status_zfs_enable` 设置为 `YES`。

**`daily_status_gmirror_enable`** （`bool`）如果你希望在 gmirror(8) 设备上运行 `gmirror` `status`，设置为 “`YES`”。

**`daily_status_graid3_enable`** （`bool`）如果你希望在 graid3(8) 设备上运行 `graid3` `status`，设置为 “`YES`”。

**`daily_status_gstripe_enable`** （`bool`）如果你希望在 gstripe(8) 设备上运行 `gstripe` `status`，设置为 “`YES`”。

**`daily_status_gconcat_enable`** （`bool`）如果你希望在 gconcat(8) 设备上运行 `gconcat` `status`，设置为 “`YES`”。

**`daily_status_mfi_enable`** （`bool`）如果你希望在 [mfi(4)](../man4/mfi.4.md) 设备上运行 `mfiutil` `status`，设置为 “`YES`”。

**`daily_status_network_enable`** （`bool`）如果你希望运行 `netstat` `-i`，设置为 “`YES`”。

**`daily_status_network_netstat_flags`** （`str`）当 `daily_status_network_enable` 设置为 “`YES`” 时，设置为 [netstat(1)](../man1/netstat.1.md) 实用程序的附加参数。默认为 `-d -W`。

**`daily_status_network_usedns`** （`bool`）如果你希望在不带 `-n` 选项的情况下运行 [netstat(1)](../man1/netstat.1.md)（以进行 DNS 查找），设置为 “`YES`”。

**`daily_status_uptime_enable`** （`bool`）如果你希望运行 [uptime(1)](../man1/uptime.1.md)（如果 `/etc/rc.conf` 中 `rwhod_enable` 设置为 “`YES`”，则运行 [ruptime(1)](../man1/ruptime.1.md)），设置为 “`YES`”。

**`daily_status_mailq_enable`** （`bool`）如果你希望运行 mailq(1)，设置为 “`YES`”。

**`daily_status_mailq_shorten`** （`bool`）如果你希望在 `daily_status_mailq_enable` 设置为 “`YES`” 时缩短 mailq(1) 输出，设置为 “`YES`”。

**`daily_status_include_submit_mailq`** （`bool`）如果你还希望在 `daily_status_mailq_enable` 设置为 “`YES`” 时对提交邮件队列运行 mailq(1)，设置为 “`YES`”。这对于 sendmail(8) 之外的 MTA 可能无效。

**`daily_status_security_enable`** （`bool`）如果你希望运行安全检查，设置为 “`YES`”。安全检查是另一组 [periodic(8)](../man8/periodic.8.md) 脚本。系统默认值位于 **/etc/periodic/security**。本地脚本应放在 **/usr/local/etc/periodic/security**。更多信息请参见 [periodic(8)](../man8/periodic.8.md) 手册页。

**`daily_status_security_inline`** （`bool`）如果你希望安全检查输出内联显示，设置为 “`YES`”。默认是根据 `daily_status_security_output` 的值将输出邮寄或记录。

**`daily_status_security_output`** （`str`）当 `daily_status_security_inline` 设置为 “`NO`” 时，安全检查输出发送的位置。此变量的行为与上述 `*_output` 变量相同，即可设置为一个或多个电子邮件地址或绝对文件名。

**`daily_status_mail_rejects_enable`** （`bool`）如果你希望总结前一天记录到 **/var/log/maillog** 的邮件拒绝信息，设置为 “`YES`”。

**`daily_status_mail_rejects_logs`** （`num`）设置为应检查昨天邮件拒绝信息的 maillog 文件数量。

**`daily_status_ntpd_enable`** （`bool`）如果你希望启用 NTP 状态检查，设置为 “`YES`”。

**`daily_status_world_kernel`** （`bool`）设置为 “`YES`” 以检查运行中的用户态和内核是否同步。

**`daily_queuerun_enable`** （`bool`）如果你希望每天至少手动运行一次邮件队列，设置为 “`YES`”。

**`daily_submit_queuerun`** （`bool`）如果你还希望在 `daily_queuerun_enable` 设置为 “`YES`” 时每天至少手动运行一次提交邮件队列，设置为 “`YES`”。

**`daily_scrub_zfs_enable`** （`bool`）如果你希望定期运行 zfs scrub，设置为 “`YES`”。

**`daily_scrub_zfs_pools`** （`str`）以空格分隔的要进行 scrub 的 zfs 池名称列表。如果列表为空或未设置，则对所有 zfs 池进行 scrub。

**`daily_scrub_zfs_default_threshold`** （`int`）如果未设置特定池的阈值，两次 scrub 之间的天数。如果未设置，默认值为 35，对应 5 周。

**`daily_scrub_zfs_`** <`poolname` >`_threshold`> （`int`）与 `daily_scrub_zfs_default_threshold` 相同，但特定于池 <`poolname` >。

**`daily_trim_zfs_enable`** （`bool`）如果你希望每日运行 zfs trim，设置为 “`YES`”。

**`daily_trim_zfs_pools`** （`str`）以空格分隔的要进行 trim 的 zfs 池名称列表。如果列表为空或未设置，则对所有 zfs 池进行 trim。

**`daily_local`** （`str`）设置为在所有其他每日脚本之后运行的额外脚本列表。所有脚本必须是绝对路径名。

**`daily_diff_flags`** （`str`）设置为生成差异时传递给 [diff(1)](../man1/diff.1.md) 实用程序的参数。默认为 `-b` `-U` `0`。

以下变量由位于 **/etc/periodic/weekly** 中的标准脚本使用：

**`weekly_locate_enable`** （`bool`）如果你希望运行 **/usr/libexec/locate.updatedb**，设置为 “`YES`”。此脚本使用 `nice` `-5` 以用户 “`nobody`” 身份运行，并生成 [locate(1)](../man1/locate.1.md) 命令使用的表。

**`weekly_whatis_enable`** （`bool`）如果你希望运行 **/usr/libexec/makewhatis.local**，设置为 “`YES`”。此脚本重新生成 [apropos(1)](../man1/apropos.1.md) 命令使用的数据库。

**`weekly_noid_enable`** （`bool`）如果你希望定位系统上的孤立文件，设置为 “`YES`”。孤立文件是指具有无效所有者或组的文件。

**`weekly_noid_dirs`** （`str`）搜索孤立文件的目录列表。通常设置为 **/**。

**`weekly_status_security_enable`** （`bool`）`daily_status_security_enable` 的每周对应项。

**`weekly_status_security_inline`** （`bool`）`daily_status_security_inline` 的每周对应项。

**`weekly_status_security_output`** （`str`）`daily_status_security_output` 的每周对应项。

**`weekly_status_pkg_enable`** （`bool`）如果你希望使用 pkg-version(8) 列出已过时的已安装软件包，设置为 “`YES`”。

**`pkg_version`** （`str`）当 `weekly_status_pkg_enable` 设置为 “`YES`” 时，此变量指定用于确定过时软件包的程序。如果未设置，则使用 pkg-version(8) 程序。例如，如果安装了 `ports/sysutils/portupgrade` port，则可将此变量设置为 “`portversion`”。

**`pkg_version_index`** （`str`）此变量指定 **/usr/ports** 中应由 pkg-version(8) 使用的 `INDEX` 文件。由于不同 FreeBSD 版本之间的依赖树可能大不相同，**/usr/ports** 中可能有多个 `INDEX` 文件。注意，如果 `pkg_version` 变量设置为 “`portversion`”，还需要安排使用环境变量指定正确的 `INDEX` 文件，并在 **/etc/periodic.conf** 中清除 `pkg_version_index`（“`pkg_version_index=`”）。

**`weekly_local`** （`str`）设置为在所有其他每周脚本之后运行的额外脚本列表。所有脚本必须是绝对路径名。

以下变量由位于 **/etc/periodic/monthly** 中的标准脚本使用：

**`monthly_accounting_enable`** （`bool`）如果你希望使用 ac(8) 命令进行登录记账，设置为 “`YES`”。

**`monthly_status_security_enable`** （`bool`）`daily_status_security_enable` 的每月对应项。

**`monthly_status_security_inline`** （`bool`）`daily_status_security_inline` 的每月对应项。

**`monthly_status_security_output`** （`str`）`daily_status_security_output` 的每月对应项。

**`monthly_local`** （`str`）设置为在所有其他每月脚本之后运行的额外脚本列表。所有脚本必须是绝对路径名。

以下变量由位于 **/etc/periodic/security** 中的标准脚本使用。这些脚本通常从每日（`daily_status_security_enable`）、每周（`weekly_status_security_enable`）和每月（`monthly_status_security_enable`）periodic 钩子运行。每个脚本的 `..._period` 可配置为 “daily”、“weekly”、“monthly” 或 “NO”。注意，当 periodic 安全脚本从 crontab(5) 运行时，除非其 `..._enable` 或 `..._period` 变量设置为 “NO”，否则它们始终会运行。

**`security_status_diff_flags`** （`str`）设置为生成差异时传递给 [diff(1)](../man1/diff.1.md) 实用程序的参数。默认为 `-b` `-U` `0`。

**`security_status_chksetuid_enable`** （`bool`）设置为 “`YES`” 以将 setuid 可执行文件的模式和修改时间与前一天的值进行比较。

**`security_status_chksetuid_period`** （`str`）设置为 “`daily`”、“`weekly`”、“`monthly`” 或 “`NO`”。

**`security_status_chkportsum_enable`** （`bool`）设置为 “`YES`” 以根据 **/var/db/pkg** 中已知校验和验证所有已安装软件包的校验和。

**`security_status_chkportsum_period`** （`str`）设置为 “`daily`”、“`weekly`”、“`monthly`” 或 “`NO`”。

**`security_status_neggrpperm_enable`** （`bool`）设置为 “`YES`” 以检查文件组权限小于全局权限的文件。当用户属于超过 14 个补充组时，这些否定权限可能不会通过 NFS 共享强制执行。

**`security_status_neggrpperm_period`** （`str`）设置为 “`daily`”、“`weekly`”、“`monthly`” 或 “`NO`”。

**`security_status_chkmounts_enable`** （`bool`）设置为 “`YES`” 以检查已挂载文件系统与前一天的值相比的更改。

**`security_status_chkmounts_period`** （`str`）设置为 “`daily`”、“`weekly`”、“`monthly`” 或 “`NO`”。

**`security_status_noamd`** （`bool`）如果你希望在 `security_status_chkmounts_enable` 检查中与昨天的文件系统挂载比较时忽略 amd(8) 挂载，设置为 “`YES`”。

**`security_status_chkuid0_enable`** （`bool`）设置为 “`YES`” 以检查 **/etc/master.passwd** 中 UID 为 0 的账户。

**`security_status_chkuid0_period`** （`str`）设置为 “`daily`”、“`weekly`”、“`monthly`” 或 “`NO`”。

**`security_status_passwdless_enable`** （`bool`）设置为 “`YES`” 以检查 **/etc/master.passwd** 中密码为空的账户。

**`security_status_passwdless_period`** （`str`）设置为 “`daily`”、“`weekly`”、“`monthly`” 或 “`NO`”。

**`security_status_logincheck_enable`** （`bool`）设置为 “`YES`” 以检查 **/etc/login.conf** 的所有权，更多信息请参见 login.conf(5)。

**`security_status_logincheck_period`** （`str`）设置为 “`daily`”、“`weekly`”、“`monthly`” 或 “`NO`”。

**`security_status_ipfwdenied_enable`** （`bool`）设置为 “`YES`” 以显示自昨天检查以来被 [ipfw(8)](../man8/ipfw.8.md) 拒绝的数据包日志条目。

**`security_status_ipfwdenied_period`** （`str`）设置为 “`daily`”、“`weekly`”、“`monthly`” 或 “`NO`”。

**`security_status_ipfdenied_enable`** （`bool`）设置为 “`YES`” 以显示自昨天检查以来被 ipf(8) 拒绝的数据包日志条目。

**`security_status_ipfdenied_period`** （`str`）设置为 “`daily`”、“`weekly`”、“`monthly`” 或 “`NO`”。

**`security_status_pfdenied_enable`** （`bool`）设置为 “`YES`” 以显示自昨天检查以来被 [pf(4)](../man4/pf.4.md) 拒绝的数据包日志条目。

**`security_status_pfdenied_additionalanchors`** （`str`）以空格分隔的附加锚点列表，显示其拒绝数据包日志条目。主规则集（即空字符串锚点）和任何 blocklistd(8) 锚点（如果存在）始终显示。

**`security_status_pfdenied_period`** （`str`）设置为 “`daily`”、“`weekly`”、“`monthly`” 或 “`NO`”。

**`security_status_ipfwlimit_enable`** （`bool`）设置为 “`YES`” 以显示已达到其详细级别限制的 [ipfw(8)](../man8/ipfw.8.md) 规则。

**`security_status_ipfwlimit_period`** （`str`）设置为 “`daily`”、“`weekly`”、“`monthly`” 或 “`NO`”。

**`security_status_kernelmsg_enable`** （`bool`）设置为 “`YES`” 以显示自昨天检查以来新的 [dmesg(8)](../man8/dmesg.8.md) 条目。

**`security_status_kernelmsg_period`** （`str`）设置为 “`daily`”、“`weekly`”、“`monthly`” 或 “`NO`”。

**`security_status_loginfail_enable`** （`bool`）设置为 “`YES`” 以显示前一天 **/var/log/messages** 中的失败登录。

**`security_status_loginfail_period`** （`str`）设置为 “`daily`”、“`weekly`”、“`monthly`” 或 “`NO`”。

**`security_status_loginfail_ignore`** （`str`）设置为扩展正则表达式以过滤掉不需要的消息。默认情况下，不过滤任何消息。

**`security_status_tcpwrap_enable`** （`bool`）设置为 “`YES`” 以显示前一天 **/var/log/messages** 中被 tcpwrappers 拒绝的连接（参见 hosts_access(5)）。

**`security_status_tcpwrap_period`** （`str`）设置为 “`daily`”、“`weekly`”、“`monthly`” 或 “`NO`”。

## 文件

**/etc/defaults/periodic.conf** 默认配置文件。此文件包含所有默认变量和值。

**/etc/periodic.conf** 通常的系统特定变量覆盖文件。

**/etc/periodic.conf.local** 附加覆盖文件，在 **/etc/periodic.conf** 被共享或分发时很有用。

## 参见

[apropos(1)](../man1/apropos.1.md), calendar(1), [df(1)](../man1/df.1.md), [diff(1)](../man1/diff.1.md), [gzip(1)](../man1/gzip.1.md), [locate(1)](../man1/locate.1.md), [man(1)](../man1/man.1.md), msgs(1), [netstat(1)](../man1/netstat.1.md), [nice(1)](../man1/nice.1.md), login.conf(5), [rc.conf(5)](rc.conf.5.md), ac(8), chkgrp(8), dump(8), newsyslog(8), [periodic(8)](../man8/periodic.8.md), pkg-version(8), sendmail(8)

## 历史

`nice` 文件首次出现在 FreeBSD 4.1 中。

## 作者

Brian Somers <brian@Awfulhak.org>
