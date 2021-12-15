import logging

from .dynamic_terminal_output import DynamicTerminalOutput
from ..formatter.report_type_oriented_report_formatter import format_git_reports
from ..exceptions import FailedToGenerateReport


class ContinuousGitReporter:
    all_reports = []
    n_repos = 0
    errors = []

    def __init__(self):
        terminal = DynamicTerminalOutput("searching . . .")
        self.terminal = terminal

    def __enter__(self):
        return self

    def add_repo(self, _):
        self.n_repos += 1
        self.update_view()

    def add_report(self, report):
        self.all_reports.append(report)
        self.update_view()

    def add_error(self, error: FailedToGenerateReport):
        self.errors.append(error)

    def __exit__(self, type, value, traceback):
        self.update_view()
        # print errors when finished to not disturb terminal output
        if len(self.errors) > 0:
            logging.error(generate_error_message(self.errors))

    def update_view(self):
        output = format_git_reports(self.all_reports, self.n_repos)
        self.terminal.update(output)


def generate_error_message(errors):
    if len(errors) == 0:
        return ""

    output = f"\nEncountered {len(errors)} error{'s' if len(errors) > 1 else ''}:"
    for error in errors:
        output += f"Failed to generate {error.report_type.tag_name} report for {error.repo.working_dir}\n"
        output += error.trace
    return output
