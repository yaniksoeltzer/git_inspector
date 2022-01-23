import time
from tempfile import TemporaryDirectory

from git_inspector.common import is_ancestors_of, is_ahead_of
from tests.testutils import create_repo, add_n_big_commits


def test_is_ahead_vs_is_ancestor_of():
    print()
    n_commits = 1000
    with TemporaryDirectory() as directory:
        repo = create_repo(directory)
        add_n_big_commits(repo, n_commits + 1)
        ancestor_commit = repo.commit(f"HEAD~{n_commits}")
        commit = repo.commit("HEAD")

        elapsed_time_is_ahead_of = measure_is_ahead_of(repo=repo,
                                                       ancestor=ancestor_commit,
                                                       commit=commit)
        print(f"Elapsed time for 'is_ahead_of' {elapsed_time_is_ahead_of * 1000} ms")

        elapsed_time_is_ancestor_of = measure_is_ancestor_of(ancestor=ancestor_commit,
                                                             commit=commit)
        print(f"Elapsed time for 'is_ancestors_of' {elapsed_time_is_ancestor_of * 1000} ms")


def measure_is_ancestor_of(ancestor, commit):
    start_is_ancestor_of = time.time()
    is_ancestor = is_ancestors_of(ancestor=ancestor, commit=commit)
    stop_is_ancestor_of = time.time()
    assert is_ancestor
    elapsed_time_is_ancestor_of = stop_is_ancestor_of - start_is_ancestor_of
    return elapsed_time_is_ancestor_of


def measure_is_ahead_of(repo, ancestor, commit):
    start_is_ahead_of = time.time()
    is_ahead = is_ahead_of(repo=repo, ancestor=ancestor, commit=commit)
    stop_is_ahead_of = time.time()
    assert is_ahead
    elapsed_time_is_ahead_of = stop_is_ahead_of - start_is_ahead_of
    return elapsed_time_is_ahead_of
