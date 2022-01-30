#!/usr/bin/env python3
import traceback
from typing import List
from git import Repo

from .exceptions import FailedToGenerateReport


def inspect_repos(git_repos: List[Repo], reporter, reports_functions):
    all_reports = []
    for repo in git_repos:
        reporter.add_repo(repo)
        for get_reports, report_type in reports_functions:
            try:
                reports = get_reports(repo)
                for report in reports:
                    reporter.add_report(report)
                all_reports.extend(reports)
            except Exception as e:
                error = FailedToGenerateReport(
                    repo, report_type, e, traceback.format_exc()
                )
                reporter.add_error(error)
