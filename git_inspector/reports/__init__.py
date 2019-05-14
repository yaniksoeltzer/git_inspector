from git_inspector.reports.dirty import DirtyReposReporter, get_dirt_repo_report
from git_inspector.reports.merged_branches import MergedBranchesReporter, get_merged_branches_report
from git_inspector.reports.git_report import Reporter
from git_inspector.reports.summary import SummaryReport
from git_inspector.reports.unpushed import UnpushedRemotesReporter, get_unpushed_branches_report


class GitInspectorReporter(Reporter):

    def __init__(self, repos):
        self.reports = []
        self.reports.append(DirtyReposReporter(repos))
        self.reports.append(UnpushedRemotesReporter(repos))
        self.reports.append(MergedBranchesReporter(repos))

        self.summary_report = SummaryReport(repos, self.reports)
        self.reports.append(self.summary_report)

    def number_of_alerts(self):
        return self.summary_report.alerts

    def number_of_warnings(self):
        return self.summary_report.warnings

    def __str__(self):
        return "\n".join(
            filter(lambda s: s != "", map(str, self.reports)))



def get_git_reports(repos):
    reports = []
    reports.append(get_dirt_repo_report(repos))
    reports.append(get_merged_branches_report(repos))
    reports.append(get_unpushed_branches_report(repos))
    return reports