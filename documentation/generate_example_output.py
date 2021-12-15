from time import sleep

from git_inspector.reports import Report
from git_inspector.reports.dirty import dirty_report
from git_inspector.reports.merged import merged_report
from git_inspector.reports.unpushed import unpushed_report
from git_inspector.reports.untracked import untracked_report
from git_inspector.cli.continuous_git_reporter import ContinuousGitReporter

if __name__ == '__main__':
    reports = [
        Report("~/my_dirty_repo", None, None, dirty_report),
        Report("~/my_dirty_repo_2", None, None, dirty_report),
        Report("~/my_dirty_repo_3", None, None, dirty_report),
        Report("~/forgot_to_push", None, ["origin"], unpushed_report),
        Report("~/repo_with_old_branch", ["old_branch"], None, merged_report),
        Report("~/repo_w_local_only_branch", ["local_only"], None, untracked_report),
    ]
    with ContinuousGitReporter() as reporter:
        for report in reports:
            sleep(0.5)
            reporter.add_repo(None)
            reporter.add_report(report)
    sleep(3)
