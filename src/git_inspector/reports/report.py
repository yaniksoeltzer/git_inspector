from collections import namedtuple

Report = namedtuple('report', ['repo', 'branches', 'remotes', 'report_type'])


class ReportType:
    def __init__(self, tag_name, description, alert_level):
        self.tag_name = tag_name
        self.description = description
        self.alert_level = alert_level


GIT_REPORT_LEVEL_ALERT = 1
GIT_REPORT_LEVEL_WARNING = 2
GIT_REPORT_LEVEL_HINT = 3
GIT_REPORT_LEVEL = [
    GIT_REPORT_LEVEL_ALERT,
    GIT_REPORT_LEVEL_WARNING,
    GIT_REPORT_LEVEL_HINT
]
