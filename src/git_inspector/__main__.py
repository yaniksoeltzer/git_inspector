#!/usr/bin/env python3
import os
import argparse
from collections import Counter
from typing import List

from git import Repo

from .find_git_repo import find_git_directories
from .report_formatter import format_git_reports
from .reports import GIT_REPORT_LEVEL_ALERT, GIT_REPORT_LEVEL_WARNING, get_reports

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('paths', metavar='path', nargs='*', default='.',
                    help='directory paths in which to look for git modules')
args = vars(parser.parse_args())
absolute_paths = [os.path.abspath(x) for x in args['paths']]


repo_file_names = find_git_directories(search_paths=absolute_paths)
repos = list(map(Repo, repo_file_names))
reports = get_reports(repos)
output = format_git_reports(reports, repos)
print(output)

alert_level: List[int] = [r.report_type.alert_level for r in reports]
a_cnt = Counter(alert_level)
aw_cnt = a_cnt[GIT_REPORT_LEVEL_ALERT]+a_cnt[GIT_REPORT_LEVEL_WARNING]
exit_code = min(255, aw_cnt)
exit(exit_code)
