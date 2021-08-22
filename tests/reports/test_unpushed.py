from git import Repo
from src.git_inspector.reports.unpushed import get_unpushed_report
from tests.testutils import add_tracked_branch


def test_return_none_on_local_repo(repo: Repo):
    report = get_unpushed_report(repo)
    assert report is None


def test_return_something_on_unpushed_repo(cloned_repo):
    cloned_repo.index.commit("local-only-commit")
    report = get_unpushed_report(cloned_repo)
    assert report is not None


def test_multiple_up_to_date_branches(remote_repo, cloned_repo):
    n_branches = 3
    for i in range(n_branches):
        add_tracked_branch(
            local_repo=cloned_repo,
            remote_repo=remote_repo,
            prefix=f"{i}"
        )
    report = get_unpushed_report(cloned_repo)
    assert report is None


def test_multiple_branches(remote_repo, cloned_repo):
    n_branches = 3
    for i in range(n_branches):
        lb, _ = add_tracked_branch(
            local_repo=cloned_repo,
            remote_repo=remote_repo,
            prefix=f"{i}"
        )
        lb.checkout()
        cloned_repo.index.commit(f"local only commit on {lb}")
    report = get_unpushed_report(cloned_repo)
    assert report is not None
    assert report.branches is not None
    assert len(report.branches) == n_branches


def test_outdated_branches(remote_repo, cloned_repo):
    # commits on origin but not on local
    origin = cloned_repo.remotes.origin
    remote_repo.index.commit("remote only commit")
    origin.fetch()

    local = cloned_repo.heads.master
    remote = local.tracking_branch()
    assert local.commit != remote.commit

    report = get_unpushed_report(cloned_repo)

    assert report is None
