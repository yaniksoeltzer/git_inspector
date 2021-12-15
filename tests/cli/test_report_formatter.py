from tempfile import TemporaryDirectory
import pytest
from git import Repo
from git_inspector.formatter.report_type_oriented_report_formatter import format_git_reports
from git_inspector.reports import ReportType, GIT_REPORT_LEVEL_ALERT, Report, REPORTS, get_dirty_report
from tests.testutils import create_repo


example_report = ReportType(
    'example',
    'example header',
    GIT_REPORT_LEVEL_ALERT
)


@pytest.fixture
def repo():
    with TemporaryDirectory() as directory:
        yield create_repo(directory)


def test_output_contains_working_directory():
    working_dir = "my_custom_directory"
    reports = [
        Report(working_dir, None, None, example_report)
    ]
    output = format_git_reports(reports, 10)
    assert working_dir in output


def test_clean_repo_output(repo: Repo):
    reports = []
    for f, report_type in REPORTS:
        report = f(repo)
        if report is not None:
            reports.append(report)
    output = format_git_reports(reports, 10)
    assert repo.working_dir in output


def test_dirty_repo_output(dirty_repo: Repo):
    report = get_dirty_report(dirty_repo)
    assert report is not None
    output = format_git_reports([report], 10)
    assert dirty_repo.working_dir in output
