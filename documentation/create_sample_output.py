from test_setup import test_setup
from git_inspector import inspect


if __name__ == '__main__':
    with test_setup() as directory:
        print(inspect([directory]))
