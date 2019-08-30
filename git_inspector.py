#!/usr/bin/env python3
import argparse
import os

from git_inspector import inspect_all

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('paths', metavar='paths', nargs='*', default='.',
                    help='directory paths in which to look for git modules')
args = vars(parser.parse_args())
absolute_paths = [os.path.abspath(x) for x in args['paths']]


inspect_all(paths=absolute_paths)
