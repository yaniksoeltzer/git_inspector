from git_inspector.report_formatter import format_git_reports
from git_inspector.reports import Report
from git_inspector.reports.dirty import dirty_report
from git_inspector.reports.merged import merged_report
from git_inspector.reports.unpushed import unpushed_report
from git_inspector.reports.untracked import untracked_report
from ansi2html import Ansi2HTMLConverter
from html2image import Html2Image

PNG_FILE = "example_output.png"
BASH_PROMPT = "user@device:~$ git_inspector\n"

if __name__ == '__main__':
    reports = [
        Report("~/my_dirty_repo", None, dirty_report),
        Report("~/forgot_to_push", ["master"], unpushed_report),
        Report("~/repo_with_old_branch", ["old_branch"], merged_report),
        Report("~/repo_w_local_only_branch", ["local_only"], untracked_report),
    ]
    output = format_git_reports(reports, 10)

    conv = Ansi2HTMLConverter(dark_bg=False)
    output = BASH_PROMPT + output
    print(output)
    html = conv.convert(output)
    hti = Html2Image()
    size = 3.5
    hti.screenshot(
        html_str=html,
        save_as=PNG_FILE,
        size=(int(170 * size), int(50 * size)),
    )
