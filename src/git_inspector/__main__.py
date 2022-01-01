#!/usr/bin/env python3
from .cli.continuous_git_reporter import ContinuousGitReporter
from .cli.exit_code import calculate_exit_code
from .cli.parse_arguments import argument_parser
from .find_git_repo import find_repos
from .inspect_repos import inspect_repos
from .reports import REPORTS

arguments = argument_parser.parse_args()

git_repo_generator = find_repos(arguments.paths)

with ContinuousGitReporter(report_level=arguments.report_level) as reporter:
    inspect_repos(git_repo_generator, reporter, REPORTS)

exit_code = calculate_exit_code(reporter.all_reports)
exit(exit_code)
