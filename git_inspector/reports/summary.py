
class SummaryReport:

    def __init__(self, repos, reports):
        self.repo_cnt = len(repos)
        self.alerts = 0
        self.warnings = 0
        for report in reports:
            self.alerts += report.number_of_alerts()
            self.warnings += report.number_of_warnings()

    def __str__(self):
        summary_message = \
            f"{self.repo_cnt} git repositories found: " \
            f"{self.alerts} alerts, {self.warnings} warnings"

        if self.alerts > 0:
            summary_message = "\033[1;31m" + summary_message
        else:
            summary_message = "\033[0;32m" + summary_message
        summary_message += "\033[0m"
        return summary_message
