from collections import Counter
from typing import List
from git_inspector.config import *
from git import Head, Repo
from git_inspector.common import is_master_branch
from git_inspector.reports import *


def format_git_reports(git_reports: List[Report], repos):
    report_types: List[ReportType] = list(set(r.report_type for r in git_reports))
    report_types = sorted(report_types, key=lambda rt: rt.alert_level)
    output = []
    for report_type in report_types:
        output.append(report_type.description)
        reports = [r for r in git_reports if r.report_type == report_type]
        for report in reports:
            working_dir = report.repo.working_dir
            if report.branches is None:
                output.append(working_dir)
            else:
                for branch in report.branches:
                    output.append(working_dir + " @" + branch.name )

    output.append(summary_string(git_reports, repos))
    return "\n".join(output)


def format_git_report(git_report):
    if git_report.is_empty():
        return ""

    indicator_line = f"{COLORS[git_report.alert_level]}{git_report.description}:{COLOR_RESET}"
    git_repo_repr_str = map(indent_string, map(git_repo_repr, git_report.repos))
    git_head_repr_str = map(indent_string, map(git_head_repr, git_report.heads))

    lines = []
    lines.extend(git_repo_repr_str)
    lines.extend(git_head_repr_str)
    lines = sorted(lines, key=str.casefold)
    lines = [indicator_line]+lines
    report_repr_str = "\n".join(lines)

    return report_repr_str


def indent_string(string, indent=5):
    return " " * indent + string


def summary_string(git_reports: list, repos):
    alert_level: List[int] = [r.report_type.alert_level for r in git_reports]
    alert_level_occurrences = Counter(alert_level)
    a_cnt = alert_level_occurrences

    if a_cnt[GIT_REPORT_LEVEL_ALERT] == 0 \
            and a_cnt[GIT_REPORT_LEVEL_WARNING] == 0 \
            and a_cnt[GIT_REPORT_LEVEL_HINT] == 0:
        summary = f"{len(repos)} git repositories found. Everything looks fine :D"
        summary = COLOR_SUCCESS + summary + COLOR_RESET
        return summary

    summary = f"{SUMMARY_COLOR_NOT_CLEAN}{len(repos)} git repositories found {COLOR_RESET}"

    sss = []
    if a_cnt[GIT_REPORT_LEVEL_ALERT] > 0:
        sss.append(f"{COLOR_ALERT}{a_cnt[GIT_REPORT_LEVEL_ALERT]} alerts{COLOR_RESET}")
    if a_cnt[GIT_REPORT_LEVEL_WARNING] > 0:
        sss.append(f"{COLOR_WARNING}{a_cnt[GIT_REPORT_LEVEL_WARNING]} warnings{COLOR_RESET}")
    if a_cnt[GIT_REPORT_LEVEL_HINT] > 0:
        sss.append(f"{COLOR_HINT}{a_cnt[GIT_REPORT_LEVEL_HINT]} hints{COLOR_RESET}")
    if len(sss) == 1:
        summary += f"{SUMMARY_COLOR_NOT_CLEAN}with {sss[0]}{SUMMARY_COLOR_NOT_CLEAN}."
    if len(sss) == 2:
        summary += f"{SUMMARY_COLOR_NOT_CLEAN}with {sss[0]}{SUMMARY_COLOR_NOT_CLEAN} and {sss[1]}{SUMMARY_COLOR_NOT_CLEAN}."
    if len(sss) == 3:
        summary += f"{SUMMARY_COLOR_NOT_CLEAN}with {sss[0]}{SUMMARY_COLOR_NOT_CLEAN}{SUMMARY_COLOR_NOT_CLEAN}, {sss[1]}{SUMMARY_COLOR_NOT_CLEAN} and {sss[2]}{SUMMARY_COLOR_NOT_CLEAN}."

    return summary



def git_repo_repr(repo: Repo):
    return f"{repo.working_tree_dir}"


def git_head_repr(head: Head):
    return f"{head.repo.working_tree_dir}  {f'{COLOR_BRANCH_TAG}@{head}{COLOR_RESET}' if not is_master_branch(head) else ''}"
