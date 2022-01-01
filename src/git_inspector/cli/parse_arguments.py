import argparse
import pathlib

from ..reports import REPORT_LEVEL_NAMES


def parse_log_level(log_level_name):
    if log_level_name not in REPORT_LEVEL_NAMES:
        raise argparse.ArgumentTypeError(f"log_level must be one of {REPORT_LEVEL_NAMES}")
    return REPORT_LEVEL_NAMES.index(log_level_name)


argument_parser = argparse.ArgumentParser(
    description='Inspect best practice for git repositories.')

argument_parser.add_argument(
    '-l',
    '--report-level',
    default='warning',
    metavar='level',
    type=parse_log_level,
    help="Set the report level.\n"
         "Allowed values are: " + (", ".join(f"'{l}'" for l in REPORT_LEVEL_NAMES)) + ".\n" +
         "Only reports with the same or a higher report level are shown."
)
argument_parser.add_argument(
    'paths',
    metavar='path',
    nargs='*',
    type=pathlib.Path,
    default='.',
    help='Directory paths that are searched for git modules.'
)
