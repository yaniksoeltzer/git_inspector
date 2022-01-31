from git import Repo

from ..common import is_local_repo
from ..reports import ReportType, GIT_REPORT_LEVEL_HINT, Report

local_report = ReportType("local", "local repository", GIT_REPORT_LEVEL_HINT)


def get_local_report(repo: Repo):
    if is_local_repo(repo):
        return Report(repo, None, local_report)
