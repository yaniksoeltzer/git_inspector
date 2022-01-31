from git import Repo

from git_inspector.reports.local import get_local_report, local_report


def test_return_none_on_cloned_repo(cloned_repo: Repo):
    report = get_local_report(cloned_repo)
    assert report is None


def test_return_report_on_local_repo(repo: Repo):
    report = get_local_report(repo)
    assert report is not None
    assert report.repo == repo
    assert report.report_type == local_report
