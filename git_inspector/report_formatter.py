from git_inspector.reports.git_report import GitReport
from git import Head, Repo
from git_inspector.common import is_master_branch


def format_git_reports(git_reports: list):
    git_reports = sorted(git_reports, key=lambda report: report.alert_level)
    git_reports_repr = [
        format_git_report(report)
        for report in git_reports
    ]
    git_reports_repr_str = "\n".join(
        [r for r in git_reports_repr
         if r != ""]
    )
    return git_reports_repr_str


def format_git_report(git_report: GitReport):
    if git_report.is_empty():
        return ""

    indicator_line = f"{git_report.description}:"
    git_repo_repr_str = map(indent_string, map(git_repo_repr, git_report.repos))
    git_head_repr_str = map(indent_string, map(git_head_repr, git_report.heads))

    report_repr_str = \
        indicator_line + "\n" \
        + "\n".join(git_repo_repr_str) \
        + "\n".join(git_head_repr_str)

    return report_repr_str


def indent_string(string, indent=5):
    return " " * indent + string


def git_repo_repr(repo: Repo):
    return f"{repo.working_tree_dir}"


def git_head_repr(head: Head):
    return f"{head.repo.working_tree_dir}  {f'@{head}' if not is_master_branch(head) else ''}"
