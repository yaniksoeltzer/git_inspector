#!/usr/bin/env python3
from .cli.continuous_git_reporter import ContinuousGitReporter
from .cli.parse_arguments import parse_absolute_paths
from .generate_reports import generate_reports

absolute_paths = parse_absolute_paths()
reporter = ContinuousGitReporter()
exit_code = generate_reports(absolute_paths, reporter)

exit(exit_code)
