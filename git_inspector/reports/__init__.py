from git_inspector.reports.dirty import DirtyReposReport
from git_inspector.reports.merged_branches import MergedBranchesReport
from git_inspector.reports.report import Report
from git_inspector.reports.summary import SummaryReport
from git_inspector.reports.unpushed import UnpushedRemotesReport


class GitInspectorReport(Report):

    def __init__(self, repos):
        self.reports = []
        self.reports.append(DirtyReposReport(repos))
        self.reports.append(UnpushedRemotesReport(repos))
        self.reports.append(MergedBranchesReport(repos))

        self.summary_report = SummaryReport(repos, self.reports)
        self.reports.append(self.summary_report)

    def number_of_alerts(self):
        return self.summary_report.alerts

    def number_of_warnings(self):
        return self.summary_report.warnings

    def __str__(self):
        return "\n".join(
            filter(lambda s: s != "", map(str, self.reports)))
