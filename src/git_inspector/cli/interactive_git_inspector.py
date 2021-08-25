#!/usr/bin/env python3
from collections import Counter
from typing import List

from git import Repo

from .active_terminal_text import ActiveTerminalText
from ..find_git_repo import find_git_directories
from ..report_formatter import format_git_reports
from ..reports import GIT_REPORT_LEVEL_ALERT, GIT_REPORT_LEVEL_WARNING, get_reports


def interactively_present_reports(absolute_paths: List[str]):
    terminal = ActiveTerminalText("searching ...")
    git_path_generator = find_git_directories(search_paths=absolute_paths)
    git_repo_generator = map(Repo, git_path_generator)

    all_reports = []
    for n_repos, repo in enumerate(git_repo_generator, 1):
        reports = get_reports(repo)
        for report in reports:
            all_reports.append(report)
            output = format_git_reports(all_reports, n_repos)
            terminal.update(output)

    alert_level: List[int] = [r.report_type.alert_level for r in all_reports]
    a_cnt = Counter(alert_level)
    aw_cnt = a_cnt[GIT_REPORT_LEVEL_ALERT] + a_cnt[GIT_REPORT_LEVEL_WARNING]
    exit_code = min(255, aw_cnt)
    return exit_code
