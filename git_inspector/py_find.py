import os
import subprocess
from git_inspector.config import EXCLUDED_DIRS


def find_git_repository_paths(search_paths, excluded_dirs=EXCLUDED_DIRS):
    find_cmd = build_find_command(search_paths,excluded_dirs)
    git_paths = get_output_of_cmd(find_cmd)
    git_paths = filter(lambda x: x != "", git_paths)
    git_paths = list(set(git_paths))
    repo_paths = map(os.path.dirname, git_paths)
    return list(repo_paths)


def build_find_command(search_paths, excluded_dirs):
    find_cmd = \
        ["find"] \
        + search_paths \
        + ["-name", ".git",
           "-type", "d",
           ]
    for directory in excluded_dirs:
        find_cmd.extend(["-not", "-path", directory])
    return find_cmd


def get_output_of_cmd(cmd: list):
    find_ps = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = find_ps.communicate()
    output = out.decode("utf-8").split("\n")
    return output
