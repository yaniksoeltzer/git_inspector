import os
from contextlib import contextmanager
from tempfile import TemporaryDirectory
from git import Repo
from git_inspector import inspect


@contextmanager
def test_setup():
    with TemporaryDirectory(prefix="projects_") as outer_directory:
        middle_1 = os.path.join(outer_directory, 'middle_1')
        os.mkdir(middle_1)
        repo_a = os.path.join(middle_1, 'repo-a')
        Repo.init(repo_a)

        middle_2 = os.path.join(outer_directory, 'middle_2')
        os.mkdir(middle_2)
        repo_b = os.path.join(middle_2, 'repo-b')
        Repo.init(repo_b)
        repo_c = os.path.join(middle_2, 'repo-c')
        Repo.init(repo_c)

        middle_3 = os.path.join(outer_directory, 'middle_3')
        os.mkdir(middle_3)

        inner_1 = os.path.join(middle_3, 'inner_1')
        os.mkdir(inner_1)
        repo_d = os.path.join(inner_1, 'repo-d')
        Repo.init(repo_d)

        inner_2 = os.path.join(middle_3, 'inner_2')
        os.mkdir(inner_2)
        repo_e = os.path.join(inner_2, 'repo-e')
        Repo.init(repo_e)
        repo_f = os.path.join(inner_2, 'repo-f')
        Repo.init(repo_f)

        yield outer_directory


if __name__ == '__main__':
    with test_setup() as directory:
        print(inspect([directory]))
