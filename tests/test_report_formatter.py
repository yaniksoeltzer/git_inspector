from tempfile import TemporaryDirectory
import pytest
from git import Repo
from git_inspector.report_formatter import format_git_reports
from git_inspector.reports import ReportType, GIT_REPORT_LEVEL_ALERT, Report, get_reports
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
        Report(working_dir, None, example_report)
    ]
    output = format_git_reports(reports, len(reports))
    assert working_dir in output


def test_clean_repo_output(repo: Repo):
    reports = get_reports([repo])
    output = format_git_reports(reports, len(reports))
    assert repo.working_dir in output


def test_dirty_repo_output(dirty_repo: Repo):
    reports = get_reports([dirty_repo])
    output = format_git_reports(reports, len(reports))
    assert dirty_repo.working_dir in output
