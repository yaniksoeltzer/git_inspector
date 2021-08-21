from tests.testutils import *
import os
from contextlib import contextmanager
from tempfile import TemporaryDirectory


@contextmanager
def test_setup():
    with TemporaryDirectory(prefix="projects_") as outer_directory:
        local_only_repo_dir = os.path.join(outer_directory, 'local_only_repo')
        local_only_repo = create_repo(local_only_repo_dir)
        add_n_commits(local_only_repo, 3)

        def fd(name):
            repo_dir = os.path.join(outer_directory, name)
            return create_cloned_repo(repo_dir, local_only_repo)

        fd("clean_repo")

        dirty_repo = fd("dirty_repo")
        make_repo_dirty(dirty_repo)

        merged_repo = fd("merged_branch_repo")
        add_merged_branch(merged_repo)

        unpushed_repo = fd("unpushed_repo")
        add_n_commits(unpushed_repo, 1)

        yield outer_directory
