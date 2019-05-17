from tempfile import TemporaryDirectory
from git import Repo
from git_inspector.report_formatter import format_git_reports
from git_inspector.reports import GitReport, GIT_REPORT_LEVEL


def get_sample_output():
    repos = get_sample_repos()
    reports = get_sample_reports(repos)
    sample_output = format_git_reports(reports, repos)
    return sample_output


def get_sample_repos():
    names = ["repo_a", "repo_b"]
    dirs = [TemporaryDirectory(suffix=f"_{name}")
            for name in names]
    repos = [
        Repo.init(dir.name)
        for name, dir in zip(names, dirs)
    ]
    return repos


def get_sample_reports(repos):
    heads = [
        repo.head for repo in repos
    ]
    reports = [
        GitReport(
            f"test_alert_level_{alert_level}",
            f"test alert (level={alert_level})",
            alert_level,
            repos,
            heads,
        )
        for alert_level in GIT_REPORT_LEVEL
    ]
    return reports


if __name__ == '__main__':
    sample_output = get_sample_output()
    print(sample_output)
