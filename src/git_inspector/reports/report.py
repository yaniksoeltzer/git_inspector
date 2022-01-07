from collections import namedtuple

Report = namedtuple('report', ['repo', 'additional_info', 'report_type'])


class ReportType:
    def __init__(self, tag_name, description, alert_level):
        self.tag_name = tag_name
        self.description = description
        self.alert_level = alert_level


GIT_REPORT_LEVEL_ALERT = 0
GIT_REPORT_LEVEL_WARNING = 1
GIT_REPORT_LEVEL_HINT = 2
GIT_REPORT_LEVEL = [
    GIT_REPORT_LEVEL_ALERT,
    GIT_REPORT_LEVEL_WARNING,
    GIT_REPORT_LEVEL_HINT
]
REPORT_LEVEL_NAMES = ['alert', 'warning', 'hint']
