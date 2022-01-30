from git_inspector.cli.parse_arguments import argument_parser


def test_parse_no_args():
    argument_parser.parse_args([])


def test_parse_report_level():
    arguments = argument_parser.parse_args(["--report-level", "warning"])
    assert arguments.report_level == 1
