import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('paths', metavar='path', nargs='*', default='.',
                    help='directory paths in which to look for git modules')


def parse_absolute_search_paths():
    args = vars(parser.parse_args())
    absolute_paths = [os.path.abspath(x) for x in args['paths']]
    return absolute_paths
