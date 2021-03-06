from collections import defaultdict
from git_inspector.config import *
from git_inspector.reports.git_report import GitReport
from git import Head, Repo
from git_inspector.common import is_master_branch
from git_inspector.reports import GIT_REPORT_LEVEL_ALERT, GIT_REPORT_LEVEL_WARNING, GIT_REPORT_LEVEL_HINT


def format_git_reports(git_reports: list, repos: list):
    git_reports = sorted(git_reports, key=lambda report: report.alert_level)
    git_reports_repr = [
        format_git_report(report)
        for report in git_reports
    ] + [
        summary_string(git_reports, repos)
    ]
    git_reports_repr_str = "\n".join(
        [f for f in git_reports_repr
         if f != ""]
    )
    return git_reports_repr_str


def format_git_report(git_report: GitReport):
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


def summary_string(git_reports: list, repos: list):
    a_cnt = count_git_report_alert_level(git_reports)

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


def count_git_report_alert_level(git_reports):
    a_cnt = defaultdict(int)
    for git_report in git_reports:
        git_report: GitReport = git_report
        a_cnt[git_report.alert_level] += len(git_report)
    return a_cnt


def git_repo_repr(repo: Repo):
    return f"{repo.working_tree_dir}"


def git_head_repr(head: Head):
    return f"{head.repo.working_tree_dir}  {f'{COLOR_BRANCH_TAG}@{head}{COLOR_RESET}' if not is_master_branch(head) else ''}"
