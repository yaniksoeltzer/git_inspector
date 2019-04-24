import os
import subprocess

from git_inspector.config import EXCLUDED_DIRS


class FindCommandBuilder:
    search_dir = None
    excluded_dirs = []

    def __init__(self, search_dir, excluded_dirs=None):
        self.search_dir = search_dir
        if excluded_dirs:
            self.excluded_dirs = excluded_dirs

    def build(self):
        find_cmd = [
            "find",
            self.search_dir,
            "-name", ".git",
            "-type", "d",
        ]
        find_cmd.extend(self.build_exclude_dir_cmd())
        return find_cmd

    def build_exclude_dir_cmd(self):
        cmd = []
        for directory in self.excluded_dirs:
            cmd.extend(["-not", "-path", directory])
        return cmd


def find_git_repository_paths(search_dir, excluded_dirs=EXCLUDED_DIRS):
    find_git_repos_cmd = FindCommandBuilder(
        search_dir=search_dir,
        excluded_dirs=excluded_dirs,
    ).build()

    git_paths = get_output_of_cmd(find_git_repos_cmd)
    git_paths = filter(lambda x: x != "", git_paths)
    repo_paths = map(os.path.dirname, git_paths)
    return list(repo_paths)


def get_output_of_cmd(cmd:list):
    find_ps = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = find_ps.communicate()
    output = out.decode("utf-8").split("\n")
    return output
