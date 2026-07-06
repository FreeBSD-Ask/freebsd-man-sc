#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
man_tools.py - FreeBSD man 手册中文翻译项目综合工具

整合所有比较、检查、分析功能于一体。

子命令:
    report      生成综合比较报告（en/ vs SUMMARY.md + 翻译行数 + 问题检测）
    compare     比较 en/ 与 SUMMARY.md，查漏补缺
    linecount   比较中文翻译与英文原文行数
    issues      检测所有问题（损坏的 en2/、占位符、缺失翻译）
    fix-en2     重新转换损坏的 en2/ 文件（.TH 格式 → mdoc 格式）
    aliases     列出 SUMMARY.md 中的别名条目
    stats       显示按章节的统计信息

用法:
    python man_tools.py report
    python man_tools.py compare
    python man_tools.py linecount
    python man_tools.py issues
    python man_tools.py fix-en2 [--dry-run]
    python man_tools.py aliases
    python man_tools.py stats

输出写入 script/man_tools_output.txt（report 模式）。
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional

# ---------------------------------------------------------------------------
# 常量
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent
EN_DIR = PROJECT_ROOT / "en"
EN2_DIR = PROJECT_ROOT / "en2"
SUMMARY_FILE = PROJECT_ROOT / "SUMMARY.md"
OUTPUT_FILE = PROJECT_ROOT / "script" / "man_tools_output.txt"

MAN_SECTIONS = [
    "man1", "man2", "man3", "man3lua",
    "man4", "man5", "man6", "man7", "man8", "man9",
]

# mdoc 章节标题中文映射
SECTION_TITLES = {
    "NAME": "名称", "SYNOPSIS": "概要", "DESCRIPTION": "描述",
    "OPTIONS": "选项", "EXIT STATUS": "退出状态", "EXAMPLES": "实例",
    "SEE ALSO": "参见", "STANDARDS": "标准", "HISTORY": "历史",
    "AUTHORS": "作者", "BUGS": "缺陷", "CAVEATS": "注意事项",
    "CAVEAT": "注意事项", "DIAGNOSTICS": "诊断", "ERRORS": "错误",
    "ENVIRONMENT": "环境变量", "FILES": "文件", "LEGAL": "法律条款",
    "WARNING": "警告", "NOTES": "注释", "RETURN VALUES": "返回值",
    "LIBRARY": "库",
}

OUTPUT_LINES: List[str] = []


# ---------------------------------------------------------------------------
# 辅助函数
# ---------------------------------------------------------------------------

def log(msg: str = "") -> None:
    """输出到控制台并记录到 OUTPUT_LINES。"""
    print(msg)
    OUTPUT_LINES.append(str(msg))


def count_lines(filepath: Path) -> int:
    """统计文件行数。"""
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            return sum(1 for _ in f)
    except Exception:
        return 0


def read_text(filepath: Path) -> str:
    """读取文件内容。"""
    try:
        return filepath.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""


# ---------------------------------------------------------------------------
# 数据收集函数
# ---------------------------------------------------------------------------

def get_en_files() -> Dict[str, Dict[str, Path]]:
    """获取 en/ 目录下所有 man 文件，按章节分组。
    返回 {section: {filename: Path}}。
    """
    result: Dict[str, Dict[str, Path]] = {}
    for section in MAN_SECTIONS:
        section_dir = EN_DIR / section
        if not section_dir.exists():
            continue
        files: Dict[str, Path] = {}
        for entry in sorted(section_dir.iterdir()):
            if entry.name.startswith("Makefile"):
                continue
            if entry.is_file():
                files[entry.name] = entry
        result[section] = files
    return result


def get_en2_files() -> Dict[str, Dict[str, Path]]:
    """获取 en2/ 目录下所有 man .md 文件，按章节分组。"""
    result: Dict[str, Dict[str, Path]] = {}
    for section in MAN_SECTIONS:
        section_dir = EN2_DIR / section
        if not section_dir.exists():
            continue
        files: Dict[str, Path] = {}
        for entry in sorted(section_dir.iterdir()):
            if entry.name.startswith("Makefile"):
                continue
            if entry.is_file() and entry.suffix == ".md":
                files[entry.name] = entry
        result[section] = files
    return result


def get_cn_files() -> Dict[str, Dict[str, Path]]:
    """获取中文翻译目录下所有 .md 文件，按章节分组。"""
    result: Dict[str, Dict[str, Path]] = {}
    for section in MAN_SECTIONS:
        section_dir = PROJECT_ROOT / section
        if not section_dir.exists():
            continue
        files: Dict[str, Path] = {}
        for entry in sorted(section_dir.iterdir()):
            if entry.is_file() and entry.suffix == ".md":
                files[entry.name] = entry
        result[section] = files
    return result


def get_summary_entries() -> Tuple[Dict[str, Set[str]], Dict[str, Set[str]]]:
    """解析 SUMMARY.md。
    返回:
        entries: {section: set of link_text}（链接文本，即别名）
        targets: {section: set of filename}（实际指向的文件名）
    """
    if not SUMMARY_FILE.exists():
        log(f"错误：SUMMARY.md 不存在: {SUMMARY_FILE}")
        sys.exit(1)

    content = SUMMARY_FILE.read_text(encoding="utf-8", errors="replace")
    pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

    entries: Dict[str, Set[str]] = {}
    targets: Dict[str, Set[str]] = {}

    for match in pattern.finditer(content):
        text = match.group(1)
        path = match.group(2)
        path_clean = path.lstrip("./")
        parts = path_clean.split("/")

        if len(parts) < 2:
            continue

        section = parts[0]
        filename = parts[1]

        if section not in MAN_SECTIONS:
            continue

        if section not in entries:
            entries[section] = set()
            targets[section] = set()

        # 链接文本（去除 markdown 转义的反斜杠）
        clean_text = text.replace("\\", "")
        entries[section].add(clean_text)
        targets[section].add(filename)

    return entries, targets


def is_th_format(filepath: Path) -> bool:
    """检测 mdoc 文件是否使用 .TH（man-db 格式）而非 .Dt（mdoc 格式）。"""
    content = read_text(filepath)
    # 查找 .TH 行（man-db 格式）
    if re.search(r'^\.TH\s+', content, re.MULTILINE):
        return True
    return False


def is_mdoc_format(filepath: Path) -> bool:
    """检测是否为 mdoc 格式（包含 .Dt 或 .Dd）。"""
    content = read_text(filepath)
    if re.search(r'^\.(Dt|Dd|Os)\s+', content, re.MULTILINE):
        return True
    return False


# ---------------------------------------------------------------------------
# 子命令实现
# ---------------------------------------------------------------------------

def cmd_stats(args: argparse.Namespace) -> None:
    """显示按章节的统计信息。"""
    log("=" * 80)
    log("按章节统计")
    log("=" * 80)

    en_files = get_en_files()
    en2_files = get_en2_files()
    cn_files = get_cn_files()
    summary_entries, summary_targets = get_summary_entries()

    log(f"\n{'章节':<12} {'en/':<10} {'en2/':<10} {'中文翻译':<12} {'SUMMARY链接':<15} {'SUMMARY实际':<15}")
    log("-" * 79)
    for section in MAN_SECTIONS:
        en_count = len(en_files.get(section, {}))
        en2_count = len(en2_files.get(section, {}))
        cn_count = len(cn_files.get(section, {}))
        entry_count = len(summary_entries.get(section, set()))
        target_count = len(summary_targets.get(section, set()))
        log(f"{section:<12} {en_count:<10} {en2_count:<10} {cn_count:<12} {entry_count:<15} {target_count:<15}")

    total_en = sum(len(f) for f in en_files.values())
    total_en2 = sum(len(f) for f in en2_files.values())
    total_cn = sum(len(f) for f in cn_files.values())
    total_entries = sum(len(f) for f in summary_entries.values())
    total_targets = sum(len(f) for f in summary_targets.values())
    log("-" * 79)
    log(f"{'合计':<12} {total_en:<10} {total_en2:<10} {total_cn:<12} {total_entries:<15} {total_targets:<15}")


def cmd_compare(args: argparse.Namespace) -> None:
    """比较 en/ 与 SUMMARY.md，查漏补缺。"""
    log("=" * 80)
    log("比较 en/ 目录和 SUMMARY.md，查漏补缺")
    log("=" * 80)

    en_files = get_en_files()
    summary_entries, summary_targets = get_summary_entries()

    # 查漏：en/ 中有但 SUMMARY.md 既未作为链接文本也未作为目标引用的文件
    log("\n【查漏：en/ 中有但 SUMMARY.md 完全未引用的文件】")
    missing_total = 0
    for section in MAN_SECTIONS:
        en_set = set(en_files.get(section, {}).keys())
        # 构建小写映射
        en_lower_map = {f.lower(): f for f in en_set}
        en_lower_set = set(en_lower_map.keys())

        # SUMMARY.md 链接文本（去掉 .md 后缀，小写）
        entry_lower_set = set()
        for text in summary_entries.get(section, set()):
            # 链接文本可能带 .N 后缀（如 addr2line.1）
            entry_lower_set.add(text.lower())

        # SUMMARY.md 实际目标（去掉 .md 后缀，小写）
        target_lower_set = set()
        for fname in summary_targets.get(section, set()):
            if fname.endswith(".md"):
                target_lower_set.add(fname[:-3].lower())
            else:
                target_lower_set.add(fname.lower())

        # en 中既不在链接文本也不在实际目标中的文件
        combined = entry_lower_set | target_lower_set
        missing_lower = en_lower_set - combined
        if missing_lower:
            log(f"\n  {section} (缺失 {len(missing_lower)} 个):")
            for fname_lower in sorted(missing_lower):
                original_name = en_lower_map[fname_lower]
                log(f"    - {original_name}")
                missing_total += 1

    if missing_total == 0:
        log("  无缺失文件，SUMMARY.md 引用与 en/ 目录完全一致。")
    else:
        log(f"\n  总计缺失: {missing_total} 个文件")

    # 查缺：SUMMARY.md 引用但 en/ 中不存在的文件（基于实际引用目标）
    log("\n【查缺：SUMMARY.md 引用但 en/ 中不存在的文件（基于实际引用目标）】")
    extra_total = 0
    for section in MAN_SECTIONS:
        en_set = set(en_files.get(section, {}).keys())
        en_lower_set = set(f.lower() for f in en_set)

        target_set = set()
        target_original = {}
        for fname in summary_targets.get(section, set()):
            if fname.endswith(".md"):
                key = fname[:-3].lower()
                target_set.add(key)
                target_original[key] = fname
            else:
                key = fname.lower()
                target_set.add(key)
                target_original[key] = fname

        extra = target_set - en_lower_set
        if extra:
            log(f"\n  {section} (多出 {len(extra)} 个):")
            for fname_lower in sorted(extra):
                original = target_original[fname_lower]
                log(f"    - {original}")
                extra_total += 1

    if extra_total == 0:
        log("  无多余引用。")
    else:
        log(f"\n  总计多出: {extra_total} 个文件")

    # 别名统计
    log("\n【SUMMARY.md 中的别名条目统计】")
    for section in MAN_SECTIONS:
        entries = summary_entries.get(section, set())
        targets = summary_targets.get(section, set())
        alias_count = len(entries) - len(targets)
        if alias_count > 0:
            log(f"  {section}: {alias_count} 个别名（{len(entries)} 个链接 → {len(targets)} 个文件）")


def cmd_linecount(args: argparse.Namespace) -> None:
    """比较中文翻译与英文原文行数。"""
    log("=" * 80)
    log("翻译行数比较：中文翻译 vs 英文原文（en2/）")
    log("=" * 80)

    cn_files = get_cn_files()
    en2_files = get_en2_files()

    threshold = args.threshold if hasattr(args, "threshold") else 20

    for section in MAN_SECTIONS:
        cn_section = cn_files.get(section, {})
        en2_section = en2_files.get(section, {})

        if not cn_section and not en2_section:
            continue

        log(f"\n  --- {section} ---")

        missing_en: List[str] = []
        missing_cn: List[str] = []
        big_diff_files: List[Tuple[str, int, int, int, float]] = []
        placeholder_files: List[str] = []

        for filename, cn_path in cn_section.items():
            en_path = en2_section.get(filename)
            if en_path is None or not en_path.exists():
                missing_en.append(filename)
                continue

            cn_lines = count_lines(cn_path)
            en_lines = count_lines(en_path)
            diff = cn_lines - en_lines
            diff_pct = (diff / en_lines * 100) if en_lines > 0 else 0

            # 检测占位符（1-2 行）
            if cn_lines <= 2 and en_lines > 10:
                placeholder_files.append(filename)
            elif abs(diff_pct) > threshold:
                big_diff_files.append((filename, cn_lines, en_lines, diff, diff_pct))

        for filename, en_path in en2_section.items():
            if filename not in cn_section:
                missing_cn.append(filename)

        if big_diff_files:
            log(f"  行数差异大于 {threshold}% 的文件（{len(big_diff_files)} 个）:")
            for filename, cn_lines, en_lines, diff, diff_pct in big_diff_files:
                log(f"    {filename:<40} 中文:{cn_lines:<8} 英文:{en_lines:<8} 差异:{diff:<+8} ({diff_pct:<+.1f}%)")

        if placeholder_files:
            log(f"  占位符文件（中文 1-2 行，英文 >10 行）（{len(placeholder_files)} 个）:")
            for f in placeholder_files[:50]:
                log(f"    - {f}")
            if len(placeholder_files) > 50:
                log(f"    ... 还有 {len(placeholder_files) - 50} 个")

        if missing_en:
            log(f"  有中文翻译但缺少英文原文 en2/ 的文件（{len(missing_en)} 个）:")
            for f in missing_en[:30]:
                log(f"    - {f}")
            if len(missing_en) > 30:
                log(f"    ... 还有 {len(missing_en) - 30} 个")

        if missing_cn:
            log(f"  有英文原文但缺少中文翻译的文件（{len(missing_cn)} 个）:")
            for f in missing_cn[:30]:
                log(f"    - {f}")
            if len(missing_cn) > 30:
                log(f"    ... 还有 {len(missing_cn) - 30} 个")

        if not big_diff_files and not placeholder_files and not missing_en and not missing_cn:
            log(f"  本章节所有文件行数差异在 {threshold}% 以内，且中英文文件齐全。")


def cmd_issues(args: argparse.Namespace) -> None:
    """检测所有问题。"""
    log("=" * 80)
    log("问题检测报告")
    log("=" * 80)

    en_files = get_en_files()
    en2_files = get_en2_files()
    cn_files = get_cn_files()

    # 1. 检测损坏的 en2/ 文件（3 行以下）
    log("\n【1. 损坏的 en2/ 文件（3 行以下，转换失败）】")
    broken_en2: List[Tuple[str, str]] = []
    for section in MAN_SECTIONS:
        for filename, path in en2_files.get(section, {}).items():
            lines = count_lines(path)
            if lines <= 3:
                broken_en2.append((section, filename))
                # 检查 en/ 源文件格式
                en_filename = filename.replace(".md", "")
                en_path = EN_DIR / section / en_filename
                if en_path.exists():
                    if is_th_format(en_path):
                        log(f"  [{section}] {filename} ({lines} 行) - 源文件为 .TH 格式（非 mdoc）")
                    else:
                        log(f"  [{section}] {filename} ({lines} 行) - 源文件格式未知")
                else:
                    log(f"  [{section}] {filename} ({lines} 行) - en/ 源文件不存在")
    log(f"  总计: {len(broken_en2)} 个损坏文件")

    # 2. 检测占位符中文文件
    log("\n【2. 占位符中文文件（1-2 行，未翻译）】")
    placeholder_cn: List[Tuple[str, str]] = []
    for section in MAN_SECTIONS:
        for filename, path in cn_files.get(section, {}).items():
            lines = count_lines(path)
            if lines <= 2:
                placeholder_cn.append((section, filename))
    log(f"  总计: {len(placeholder_cn)} 个占位符文件")
    for section in MAN_SECTIONS:
        section_placeholders = [f for s, f in placeholder_cn if s == section]
        if section_placeholders:
            log(f"    {section}: {len(section_placeholders)} 个")

    # 3. 检测完全缺失中文翻译的文件
    log("\n【3. 完全缺失中文翻译的文件（en2/ 有但中文目录无）】")
    missing_cn: List[Tuple[str, str]] = []
    for section in MAN_SECTIONS:
        cn_section = cn_files.get(section, {})
        for filename in en2_files.get(section, {}):
            if filename not in cn_section:
                missing_cn.append((section, filename))
    log(f"  总计: {len(missing_cn)} 个缺失文件")
    for section, filename in missing_cn:
        log(f"    [{section}] {filename}")

    # 4. 检测 .TH 格式的 en/ 文件
    log("\n【4. .TH 格式（非 mdoc）的 en/ 文件】")
    th_files: List[Tuple[str, str]] = []
    for section in MAN_SECTIONS:
        for filename, path in en_files.get(section, {}).items():
            if is_th_format(path):
                th_files.append((section, filename))
    log(f"  总计: {len(th_files)} 个 .TH 格式文件")
    for section, filename in th_files:
        log(f"    [{section}] {filename}")


def cmd_aliases(args: argparse.Namespace) -> None:
    """列出 SUMMARY.md 中的别名条目。"""
    log("=" * 80)
    log("SUMMARY.md 别名条目列表")
    log("=" * 80)

    summary_entries, summary_targets = get_summary_entries()

    for section in MAN_SECTIONS:
        entries = summary_entries.get(section, set())
        targets = summary_targets.get(section, set())
        if len(entries) == len(targets):
            continue

        log(f"\n--- {section} ---")
        # 构建目标 → 链接文本列表的映射
        content = SUMMARY_FILE.read_text(encoding="utf-8", errors="replace")
        pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
        target_to_entries: Dict[str, List[str]] = {}

        for match in pattern.finditer(content):
            text = match.group(1).replace("\\", "")
            path = match.group(2).lstrip("./")
            parts = path.split("/")
            if len(parts) < 2 or parts[0] != section:
                continue
            target = parts[1]
            if target not in target_to_entries:
                target_to_entries[target] = []
            target_to_entries[target].append(text)

        # 只显示有多个链接文本指向同一目标的条目
        for target, texts in sorted(target_to_entries.items()):
            if len(texts) > 1:
                log(f"  {target}:")
                for t in texts:
                    marker = " ← 主条目" if t + ".md" == target else ""
                    log(f"    - {t}{marker}")


def cmd_fix_en2(args: argparse.Namespace) -> None:
    """重新转换损坏的 en2/ 文件。"""
    log("=" * 80)
    log("修复损坏的 en2/ 文件")
    log("=" * 80)

    en_files = get_en_files()
    en2_files = get_en2_files()

    dry_run = args.dry_run if hasattr(args, "dry_run") else False

    fixed = 0
    failed = 0

    for section in MAN_SECTIONS:
        for filename, en2_path in en2_files.get(section, {}).items():
            lines = count_lines(en2_path)
            if lines > 3:
                continue

            en_filename = filename.replace(".md", "")
            en_path = EN_DIR / section / en_filename

            if not en_path.exists():
                log(f"  [跳过] {section}/{filename} - en/ 源文件不存在")
                failed += 1
                continue

            if not is_th_format(en_path):
                log(f"  [跳过] {section}/{filename} - 非 .TH 格式，需手动检查")
                failed += 1
                continue

            if dry_run:
                log(f"  [DRY-RUN] 将转换 {section}/{filename}")
                fixed += 1
                continue

            # 读取 .TH 格式文件并转换为简易 Markdown
            content = read_text(en_path)
            md_content = convert_th_to_markdown(content, en_filename)

            if md_content:
                en2_path.write_text(md_content, encoding="utf-8")
                new_lines = count_lines(en2_path)
                log(f"  [成功] {section}/{filename} - 转换为 {new_lines} 行")
                fixed += 1
            else:
                log(f"  [失败] {section}/{filename} - 转换失败")
                failed += 1

    log(f"\n总计: 成功 {fixed} 个, 失败/跳过 {failed} 个")


def convert_th_to_markdown(content: str, filename: str) -> str:
    """将 .TH 格式的 man 页面转换为简易 Markdown。

    .TH 格式使用 .SH 而非 .Sh，.B/.I 而非 .Sy/.Em 等。
    本函数做基本转换，生成可读的 Markdown。
    """
    lines = content.split("\n")
    output: List[str] = []

    # 提取标题
    title_match = re.match(r'\.TH\s+"([^"]+)"\s+"(\d+)"', lines[0] if lines else "")
    if title_match:
        name = title_match.group(1).lower()
        section_num = title_match.group(2)
        output.append(f"# `{name}({section_num})`")
        output.append("")

    # 处理 .SH 章节标题
    current_section = ""
    in_preformatted = False

    for line in lines[1:]:
        stripped = line.strip()

        # 跳过注释
        if stripped.startswith('.\\"'):
            continue

        # .SH 章节标题
        sh_match = re.match(r'^\.SH\s+"?([^"]+)"?', stripped)
        if sh_match:
            section_name = sh_match.group(1).strip()
            # 映射为中文标题
            cn_title = SECTION_TITLES.get(section_name.upper(), section_name)
            current_section = section_name.upper()
            output.append(f"## {cn_title}")
            output.append("")
            continue

        # .B 加粗
        b_match = re.match(r'^\.B\s+(.+)', stripped)
        if b_match:
            text = b_match.group(1).strip()
            # 去掉嵌套的 .B/.I
            text = re.sub(r'\\f[BI]', '', text)
            output.append(f"**{text}**")
            continue

        # .I 斜体
        i_match = re.match(r'^\.I\s+(.+)', stripped)
        if i_match:
            text = i_match.group(1).strip()
            output.append(f"*{text}*")
            continue

        # .TP 标签段落
        if stripped == ".TP":
            continue

        # .PP 段落
        if stripped in (".PP", ".P"):
            output.append("")
            continue

        # .RS/.RE 缩进块
        if stripped == ".RS":
            continue
        if stripped == ".RE":
            output.append("")
            continue

        # .br 换行
        if stripped == ".br":
            output.append("")
            continue

        # 跳过空行和未处理的宏
        if stripped.startswith(".") and not stripped.startswith(".."):
            # 尝试提取宏后的文本
            macro_match = re.match(r'^\.\w+\s+(.+)', stripped)
            if macro_match:
                text = macro_match.group(1).strip()
                # 清理 troff 字体控制
                text = re.sub(r'\\f[BI]', '', text)
                text = re.sub(r'\\f[R]', '', text)
                if text:
                    output.append(text)
            continue

        # 普通文本行
        if stripped:
            # 清理 troff 转义
            text = stripped
            text = re.sub(r'\\f[BI]', '', text)
            text = re.sub(r'\\f[R]', '', text)
            text = text.replace(r'\-', '-')
            text = text.replace(r'\\', '\\')
            output.append(text)

    return "\n".join(output)


def cmd_report(args: argparse.Namespace) -> None:
    """生成综合报告。"""
    log("=" * 80)
    log("FreeBSD man 手册翻译项目 - 综合报告")
    log("=" * 80)

    log(f"\n生成时间: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log(f"项目根目录: {PROJECT_ROOT}")

    # 统计
    log("\n" + "=" * 80)
    log("一、统计概览")
    log("=" * 80)
    cmd_stats(args)

    # 比较
    log("\n" + "=" * 80)
    log("二、en/ 与 SUMMARY.md 比较")
    log("=" * 80)
    cmd_compare(args)

    # 行数比较
    log("\n" + "=" * 80)
    log("三、翻译行数比较")
    log("=" * 80)
    cmd_linecount(args)

    # 问题检测
    log("\n" + "=" * 80)
    log("四、问题检测")
    log("=" * 80)
    cmd_issues(args)

    log("\n" + "=" * 80)
    log("报告结束")
    log("=" * 80)

    # 写入文件
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(OUTPUT_LINES))
    log(f"\n完整输出已写入: {OUTPUT_FILE}")


# ---------------------------------------------------------------------------
# 主入口
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="FreeBSD man 手册翻译项目综合工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", help="子命令")

    # report
    p_report = subparsers.add_parser("report", help="生成综合报告")
    p_report.set_defaults(func=cmd_report)

    # compare
    p_compare = subparsers.add_parser("compare", help="比较 en/ 与 SUMMARY.md")
    p_compare.set_defaults(func=cmd_compare)

    # linecount
    p_linecount = subparsers.add_parser("linecount", help="比较翻译行数")
    p_linecount.add_argument("--threshold", type=int, default=20, help="行数差异阈值百分比（默认 20）")
    p_linecount.set_defaults(func=cmd_linecount)

    # issues
    p_issues = subparsers.add_parser("issues", help="检测所有问题")
    p_issues.set_defaults(func=cmd_issues)

    # fix-en2
    p_fix = subparsers.add_parser("fix-en2", help="重新转换损坏的 en2/ 文件")
    p_fix.add_argument("--dry-run", action="store_true", help="仅显示将执行的操作，不实际修改")
    p_fix.set_defaults(func=cmd_fix_en2)

    # aliases
    p_aliases = subparsers.add_parser("aliases", help="列出 SUMMARY.md 中的别名")
    p_aliases.set_defaults(func=cmd_aliases)

    # stats
    p_stats = subparsers.add_parser("stats", help="显示统计信息")
    p_stats.set_defaults(func=cmd_stats)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    args.func(args)


if __name__ == "__main__":
    main()
