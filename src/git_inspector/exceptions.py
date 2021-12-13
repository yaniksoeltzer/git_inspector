from git import Repo

from .reports import ReportType


class FailedToGenerateReport(Exception):
    def __init__(self, repo: Repo, report_type: ReportType, error: Exception, trace):
        self.repo = repo
        self.report_type = report_type
        self.original_error = error
        self.trace = trace
