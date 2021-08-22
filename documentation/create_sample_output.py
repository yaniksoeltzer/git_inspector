from test_setup import test_setup
from git_inspector import inspect
from ansi2html import Ansi2HTMLConverter

HTML_FILE = "example_output.html"

if __name__ == '__main__':
    conv = Ansi2HTMLConverter()
    with test_setup() as directory:
        output = inspect([directory])
        print(output)
        html = conv.convert(output)
        with open(HTML_FILE, "w+") as f:
            f.write(html)

