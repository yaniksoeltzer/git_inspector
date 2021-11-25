#!/usr/bin/env python3
from collections import Counter
from typing import List
from git import Repo

from .find_git_repo import find_git_directories
from .reports import GIT_REPORT_LEVEL_ALERT, get_reports, GIT_REPORT_LEVEL_WARNING


def generate_reports(absolute_paths: List[str], reporter):
    git_path_generator = find_git_directories(search_paths=absolute_paths)
    git_repo_generator = map(Repo, git_path_generator)

    all_reports = []
    for repo in git_repo_generator:
        reporter.add_repo(repo)
        reports = get_reports(repo)
        for report in reports:
            reporter.add_report(report)
            all_reports.append(report)

    reporter.finish()

    alert_level: List[int] = [r.report_type.alert_level for r in all_reports]
    a_cnt = Counter(alert_level)
    aw_cnt = a_cnt[GIT_REPORT_LEVEL_ALERT] + a_cnt[GIT_REPORT_LEVEL_WARNING]
    exit_code = min(255, aw_cnt)
    return exit_code
