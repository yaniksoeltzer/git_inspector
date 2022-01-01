#!/usr/bin/env python3
import traceback

from .exceptions import FailedToGenerateReport


def inspect_repos(git_repos, reporter, reports):
    all_reports = []
    for repo in git_repos:
        reporter.add_repo(repo)
        for get_report, report_type in reports:
            try:
                report = get_report(repo)
                if report is not None:
                    reporter.add_report(report)
                    all_reports.append(report)
            except Exception as e:
                error = FailedToGenerateReport(repo, report_type, e, traceback.format_exc())
                reporter.add_error(error)
