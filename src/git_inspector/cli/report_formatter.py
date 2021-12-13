from collections import Counter
from typing import List, Iterator
from git import Head
from termcolor import colored
from ..reports import *
from ..config import *
from ..common import is_master_branch


INTENTS = 4
REPORT_TYPE_COLOR = {
    GIT_REPORT_LEVEL_ALERT: "red",
    GIT_REPORT_LEVEL_WARNING: "yellow",
    GIT_REPORT_LEVEL_HINT: None,
}

BRANCH_COLOR = "blue"


def format_git_reports(git_reports: Iterator[Report], n_repos: int):
    git_reports = [g for g in git_reports]
    report_types: List[ReportType] = list(set(r.report_type for r in git_reports))
    report_types = sorted(report_types, key=lambda rt: rt.alert_level)
    output = []
    for report_type in report_types:
        header = colored(report_type.description, REPORT_TYPE_COLOR[report_type.alert_level])
        output.append(header)
        reports = [r for r in git_reports if r.report_type == report_type]
        for report in reports:
            working_dir = report.repo
            if report.branches is None:
                output.append(" " * INTENTS + working_dir)
            else:
                for branch in report.branches:
                    output.append(" " * INTENTS + working_dir + colored(" @" + branch, BRANCH_COLOR))

    output.append(summary_string(git_reports, n_repos))
    return "\n".join(output) + colored("", None)


def summary_string(git_reports: list, n_repos: int):
    alert_level: List[int] = [r.report_type.alert_level for r in git_reports]
    alert_level_occurrences = Counter(alert_level)
    a_cnt = alert_level_occurrences

    if a_cnt[GIT_REPORT_LEVEL_ALERT] == 0 \
            and a_cnt[GIT_REPORT_LEVEL_WARNING] == 0 \
            and a_cnt[GIT_REPORT_LEVEL_HINT] == 0:
        summary = f"{n_repos} git repositories found. Everything looks fine :D"
        summary = COLOR_SUCCESS + summary + COLOR_RESET
        return summary

    summary = f"{SUMMARY_COLOR_NOT_CLEAN}{n_repos} git repositories found {COLOR_RESET}"

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
