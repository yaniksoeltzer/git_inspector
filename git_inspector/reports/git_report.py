from abc import abstractmethod
from collections import namedtuple

GIT_REPORT_LEVEL_ALERT = 1
GIT_REPORT_LEVEL_WARNING = 2
GIT_REPORT_LEVEL_INFO = 3


# GitReport = namedtuple("git_repo_report", ['tag_name', 'description', 'alert_level', 'repos', 'heads'])


class GitReport:
    def __init__(self, tag_name, description, alert_level, repos, heads):
        self.tag_name = tag_name
        self.description = description
        self.alert_level = alert_level
        self.repos = repos
        self.heads = heads

    def is_empty(self):
        return len(self.heads) + len(self.repos) == 0


class Reporter:

    @abstractmethod
    def number_of_alerts(self):
        pass

    @abstractmethod
    def number_of_warnings(self):
        pass
