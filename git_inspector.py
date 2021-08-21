#!/usr/bin/env python3
import os
import argparse
from collections import Counter
from typing import List

from git_inspector import inspect

# parse arguments
from git_inspector.reports import GIT_REPORT_LEVEL_ALERT, GIT_REPORT_LEVEL_WARNING

parser = argparse.ArgumentParser()
parser.add_argument('paths', metavar='path', nargs='*', default='.',
                    help='directory paths in which to look for git modules')
args = vars(parser.parse_args())
absolute_paths = [os.path.abspath(x) for x in args['paths']]

output = inspect(paths=absolute_paths)
print(output)

alert_level: List[int] = [r.report_type.alert_level for r in git_reports]
a_cnt = Counter(alert_level)
aw_cnt = a_cnt[GIT_REPORT_LEVEL_ALERT]+a_cnt[GIT_REPORT_LEVEL_WARNING]
exit_code = min(255, aw_cnt)
exit(exit_code)
