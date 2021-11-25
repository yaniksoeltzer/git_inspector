from .dynamic_terminal_output import DynamicTerminalOutput
from .report_formatter import format_git_reports


class ContinuousGitReporter:
    all_reports = []
    n_repos = 0

    def __init__(self):
        terminal = DynamicTerminalOutput("searching . . .")
        self.terminal = terminal

    def add_repo(self, _):
        self.n_repos += 1
        self.update_view()

    def add_report(self, report):
        self.all_reports.append(report)
        self.update_view()

    def finish(self):
        self.update_view()

    def update_view(self):
        output = format_git_reports(self.all_reports, self.n_repos)
        self.terminal.update(output)
