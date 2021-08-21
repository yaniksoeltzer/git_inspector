from git import Repo
from git_inspector.reports.unpushed import get_unpushed_report


def test_return_none_on_local_repo(repo: Repo):
    report = get_unpushed_report(repo)
    assert report is None


def test_return_something_on_unpushed_repo(cloned_repo):
    cloned_repo.index.commit("local-only-commit")
    report = get_unpushed_report(cloned_repo)
    assert report is not None


def test_multiple_up_to_date_branches(remote_repo, cloned_repo):
    #
    # master -> origin/master
    # branch_1 -> origin/remote_1
    n_branches = 3
    origin = cloned_repo.remotes.origin
    for i in range(n_branches):
        # create emote ranches
        remote_branch_name = f'remote_{i}'
        remote_repo.create_head(remote_branch_name)
        origin.fetch()
        # create local branches
        local_branch_name = f'branch_{i}'
        lb = cloned_repo.create_head(local_branch_name)
        lb.set_tracking_branch(origin.refs[remote_branch_name])

    report = get_unpushed_report(cloned_repo)
    assert report is None


def test_multiple_branches(remote_repo, cloned_repo):
    # master -> origin/master (up to date)
    # branch_{i} -> origin/remote_{i} (unpushed)
    n_branches = 3
    origin = cloned_repo.remotes.origin

    for i in range(n_branches):
        # create emote ranches
        remote_branch_name = f'remote_{i}'
        remote_repo.create_head(remote_branch_name)
        origin.fetch()
        # create local branches
        local_branch_name = f'branch_{i}'
        lb = cloned_repo.create_head(local_branch_name)
        lb.set_tracking_branch(origin.refs[remote_branch_name])

        # commit to local_branch
        lb.checkout()
        cloned_repo.index.commit(f"local only commit on {local_branch_name}")

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
