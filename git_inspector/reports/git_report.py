
GIT_REPORT_LEVEL_ALERT = 1
GIT_REPORT_LEVEL_WARNING = 2
GIT_REPORT_LEVEL_HINT = 3
GIT_REPORT_LEVEL = [
    GIT_REPORT_LEVEL_ALERT,
    GIT_REPORT_LEVEL_WARNING,
    GIT_REPORT_LEVEL_HINT
]


class GitReport:
    def __init__(self, tag_name, description, alert_level, repos, heads):
        self.tag_name = tag_name
        self.description = description
        self.alert_level = alert_level
        self.repos = repos
        self.heads = heads

    def is_empty(self):
        return len(self.heads) + len(self.repos) == 0

    def __len__(self):
        return len(self.heads) + len(self.repos)
