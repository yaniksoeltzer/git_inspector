#!/usr/bin/env python3
from .cli.interactive_git_inspector import interactively_present_reports
from .cli.parse_arguments import parse_absolute_paths

absolute_paths = parse_absolute_paths()
exit_code = interactively_present_reports(absolute_paths)

exit(exit_code)
