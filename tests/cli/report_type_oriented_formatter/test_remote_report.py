from git import Repo
from git_inspector.formatter.report_type_oriented_report_formatter import format_git_reports
from git_inspector.reports import ReportType, GIT_REPORT_LEVEL_ALERT, Report

example_report = ReportType(
    'has_remote',
    'Repos with remotes',
    GIT_REPORT_LEVEL_ALERT
)


def test_output_contains_remote_name(cloned_repo: Repo):
    working_dir = "my_custom_directory"
    remotes = ['some_remote', 'some_other_remote']
    reports = [
        Report(working_dir, {'remote': remote}, example_report)
        for remote in remotes
    ]
    output = format_git_reports(reports, 10)
    for remote in remotes:
        assert remote in output
