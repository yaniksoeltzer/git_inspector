from time import sleep

from git_inspector.reports import Report, GIT_REPORT_LEVEL_HINT
from git_inspector.reports.dirty import dirty_report
from git_inspector.reports.merged import merged_report
from git_inspector.reports.unpushed import unpushed_report
from git_inspector.reports.untracked import untracked_report
from git_inspector.reports.broken_remote import broken_remote_report
from git_inspector.cli.continuous_git_reporter import ContinuousGitReporter

if __name__ == '__main__':
    reports = [
        Report("~/my_dirty_repo", {}, dirty_report),
        Report("~/my_dirty_repo_2", {}, dirty_report),
        Report("~/forgot_to_push", {"branch": "master"}, unpushed_report),
        Report("~/forgot_to_push", {"remote": "origin"}, broken_remote_report),
        Report("~/repo_with_old_branch", {"branch": "old_branch"}, merged_report),
        Report("~/repo_w_local_only_branch", {"branch": "local_only"}, untracked_report),
    ]
    with ContinuousGitReporter(report_level=GIT_REPORT_LEVEL_HINT) as reporter:
        for report in reports:
            sleep(0.5)
            reporter.add_repo(None)
            reporter.add_report(report)
    sleep(3)
