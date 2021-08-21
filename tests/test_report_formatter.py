from tempfile import TemporaryDirectory
import pytest
from git import Repo
from git_inspector.report_formatter import format_git_reports
from git_inspector.reports import ReportType, GIT_REPORT_LEVEL_ALERT, Report
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


def test_output_contains_repo(repo: Repo):
    reports = [
        Report(repo, None, example_report)
    ]
    output = format_git_reports(reports, [repo])
    assert repo.working_dir in output