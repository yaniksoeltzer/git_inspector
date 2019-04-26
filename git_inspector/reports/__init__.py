from git_inspector.reports.dirty import DirtyReposReport
from git_inspector.reports.merged_branches import MergedBranchesReport
from git_inspector.reports.summary import SummaryReport
from git_inspector.reports.unpushed import UnpushedRemotesReport


class GitInspectorReport:
    def __init__(self, repos):
        self.dirty_report = DirtyReposReport(repos)
        self.unpushed_report = UnpushedRemotesReport(repos)
        self.summary_report = SummaryReport(repos)
        self.merged_branches_report = MergedBranchesReport(repos)

    def __str__(self):
        return "\n".join(
            filter(lambda s: s != "", [
                str(self.dirty_report),
                str(self.unpushed_report),
                str(self.merged_branches_report),
                str(self.summary_report),
            ]))
