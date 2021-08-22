from tempfile import NamedTemporaryFile

import pdfkit

from test_setup import test_setup
from git_inspector import inspect
from ansi2html import Ansi2HTMLConverter

PDF_FILE = "example_output.pdf"
options = {
    'page-height': '5cm',
    'page-width': '15cm',
    'margin-top': '0',
    'margin-right': '0',
    'margin-bottom': '0',
    'margin-left': '0',
}

if __name__ == '__main__':
    conv = Ansi2HTMLConverter()
    with test_setup() as directory:
        output = inspect([directory])
        print(output)
        html = conv.convert(output)
        pdfkit.from_string(html, PDF_FILE, options=options)

