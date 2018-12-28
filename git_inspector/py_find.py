import subprocess


grep_permission_denied_cmd = [
    "grep",
    "-v","Permission denied"
]

class FindCommandBuilder:
    search_dir = None
    execluded_dirs = []

    def build_command(self):
        find_cmd = [
            "find",
            self.search_dir,
            "-name",".git",
            "-type", "d",
        ]
        find_cmd.extend(self.execlude_dir_cmd())
        return find_cmd

    def execlude_dir_cmd(self):
        cmd = []
        for dir in self.execluded_dirs:
            cmd.extend(["-not","-path",dir])
        return cmd



EXECLUDED_DIRS = [
    "*/Trash/*",
    "/proc"
]


def get_git_repository_paths(search_dir, execluded_dirs=EXECLUDED_DIRS):
    builder = FindCommandBuilder()
    builder.search_dir = search_dir
    builder.execluded_dirs = execluded_dirs
    find_cmd = builder.build_command()

    find_ps = subprocess.Popen(find_cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    grep_ps = subprocess.Popen(find_cmd,stdin=find_ps.stdout,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out, err = grep_ps.communicate()
    repos = out.decode("utf-8").split("\n")
    repos = [repo for repo in repos if repo != ""]
    return repos
