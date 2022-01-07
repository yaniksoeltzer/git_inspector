from git import Repo
from git_inspector.reports.unpushed import get_unpushed_reports
from tests.testutils import add_tracked_branch


def test_return_none_on_local_repo(repo: Repo):
    reports = get_unpushed_reports(repo)
    assert len(reports) == 0


def test_return_something_on_unpushed_repo(cloned_repo):
    cloned_repo.index.commit("local-only-commit")
    reports = get_unpushed_reports(cloned_repo)
    assert len(reports) > 0


def test_multiple_up_to_date_branches(remote_repo, cloned_repo):
    n_branches = 3
    for i in range(n_branches):
        add_tracked_branch(
            local_repo=cloned_repo,
            remote_repo=remote_repo,
            prefix=f"{i}"
        )
    reports = get_unpushed_reports(cloned_repo)
    assert len(reports) == 0


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
    reports = get_unpushed_reports(cloned_repo)
    assert len(reports) == n_branches
    assert reports[0].additional_info['branch'] is not None


def test_outdated_branches(remote_repo, cloned_repo):
    # commits on origin but not on local
    origin = cloned_repo.remotes.origin
    remote_repo.index.commit("remote only commit")
    origin.fetch()

    local = cloned_repo.heads[0]
    remote = local.tracking_branch()
    assert local.commit != remote.commit

    reports = get_unpushed_reports(cloned_repo)
    assert len(reports) == 0
