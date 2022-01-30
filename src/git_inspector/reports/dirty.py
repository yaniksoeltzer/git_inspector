from git import Repo

from .report import Report, ReportType, GIT_REPORT_LEVEL_ALERT


dirty_report = ReportType("dirty", "dirty repositories", GIT_REPORT_LEVEL_ALERT)


def get_dirty_reports(repo: Repo):
    report = get_dirty_report(repo)
    return [get_dirty_report(repo)] if report is not None else []


def get_dirty_report(repo: Repo):
    if repo.is_dirty():
        return Report(repo.working_dir, {}, dirty_report)
    else:
        return None
