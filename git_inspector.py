#!/usr/bin/env python3
import os
import argparse
from git_inspector import inspect_all
from git_inspector.report_formatter import format_git_reports, count_git_report_alert_level

# parse arguments
from git_inspector.reports import GIT_REPORT_LEVEL_ALERT, GIT_REPORT_LEVEL_WARNING

parser = argparse.ArgumentParser()
parser.add_argument('paths', metavar='path', nargs='*', default='.',
                    help='directory paths in which to look for git modules')
args = vars(parser.parse_args())
absolute_paths = [os.path.abspath(x) for x in args['paths']]


repos, reports = inspect_all(paths=absolute_paths)
formatted_str = format_git_reports(reports, repos)
print(formatted_str)

a_cnt = count_git_report_alert_level(git_reports=reports)
aw_cnt = a_cnt[GIT_REPORT_LEVEL_ALERT]+a_cnt[GIT_REPORT_LEVEL_WARNING]
exit_code = min(255, aw_cnt)
exit(exit_code)
