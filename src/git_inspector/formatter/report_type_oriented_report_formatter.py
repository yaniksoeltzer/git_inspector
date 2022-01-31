from collections import Counter
from typing import List, Iterator
from termcolor import colored
from ..reports import *
from ..config import *

INTENTS = 4
REPORT_TYPE_COLOR = {
    GIT_REPORT_LEVEL_ALERT: "red",
    GIT_REPORT_LEVEL_WARNING: "yellow",
    GIT_REPORT_LEVEL_HINT: None,
}

BRANCH_COLOR = "blue"
REMOTE_COLOR = "magenta"


def format_git_reports(git_reports: Iterator[Report], n_repos: int, report_level=100):
    git_reports = [g for g in git_reports]
    output = git_report_list_format(
        [r for r in git_reports if r.report_type.alert_level <= report_level]
    )
    if output != "":
        output += "\n"
    output += summary_string(git_reports, n_repos)
    return output


def git_report_list_format(git_reports: Iterator[Report]):
    report_types: List[ReportType] = list(set(r.report_type for r in git_reports))
    report_types = sorted(report_types, key=lambda rt: rt.alert_level)
    output = []
    for report_type in report_types:
        header = colored(
            report_type.description, REPORT_TYPE_COLOR[report_type.alert_level]
        )
        output.append(header)
        reports = [r for r in git_reports if r.report_type == report_type]
        for report in reports:
            working_dir = report.repo
            report_string = " " * INTENTS + working_dir
            if "branch" in report.additional_info:
                branch = report.additional_info["branch"]
                report_string += colored(" @" + branch, BRANCH_COLOR)
            if "remote" in report.additional_info:
                remote = report.additional_info["remote"]
                report_string += colored(" @" + remote, REMOTE_COLOR)
            output.append(report_string)
    return "\n".join(output)


def summary_string(git_reports: list, n_repos: int):
    alert_level: List[int] = [r.report_type.alert_level for r in git_reports]
    alert_level_occurrences = Counter(alert_level)
    a_cnt = alert_level_occurrences

    if (
        a_cnt[GIT_REPORT_LEVEL_ALERT] == 0
        and a_cnt[GIT_REPORT_LEVEL_WARNING] == 0
        and a_cnt[GIT_REPORT_LEVEL_HINT] == 0
    ):
        summary = f"{n_repos} git repositories found. Everything looks fine :D"
        summary = COLOR_SUCCESS + summary + COLOR_RESET
        return summary

    if a_cnt[GIT_REPORT_LEVEL_ALERT] == 0 and a_cnt[GIT_REPORT_LEVEL_WARNING] == 0:
        summary_color = COLOR_SUCCESS
    else:
        summary_color = SUMMARY_COLOR_NOT_CLEAN

    summary = f"{summary_color}{n_repos} git repositories found {COLOR_RESET}"

    sss = []
    if a_cnt[GIT_REPORT_LEVEL_ALERT] > 0:
        sss.append(f"{COLOR_ALERT}{a_cnt[GIT_REPORT_LEVEL_ALERT]} alerts{COLOR_RESET}")
    if a_cnt[GIT_REPORT_LEVEL_WARNING] > 0:
        sss.append(
            f"{COLOR_WARNING}{a_cnt[GIT_REPORT_LEVEL_WARNING]} warnings{COLOR_RESET}"
        )
    if a_cnt[GIT_REPORT_LEVEL_HINT] > 0:
        sss.append(f"{COLOR_HINT}{a_cnt[GIT_REPORT_LEVEL_HINT]} hints{COLOR_RESET}")
    if len(sss) == 1:
        summary += f"{summary_color}with {sss[0]}{summary_color}."
    if len(sss) == 2:
        summary += (
            f"{summary_color}with {sss[0]}{summary_color} and {sss[1]}{summary_color}."
        )
    if len(sss) == 3:
        summary += f"{summary_color}with {sss[0]}{summary_color}{summary_color}, {sss[1]}{summary_color} and {sss[2]}{summary_color}."

    return summary + colored("", None)
