

from test_setup import test_setup
from src.git_inspector import inspect
from ansi2html import Ansi2HTMLConverter
from html2image import Html2Image

PNG_FILE = "example_output.png"
BASH_PROMPT = "user@device:~$ git_inspector\n"

if __name__ == '__main__':
    conv = Ansi2HTMLConverter(dark_bg=False,)
    with test_setup() as directory:
        output = inspect([directory])
        output = BASH_PROMPT + output
        print(output)
        html = conv.convert(output)
        hti = Html2Image()
        size = 3.5
        hti.screenshot(
            html_str=html,
            save_as=PNG_FILE,
            size=(int(170*size), int(50*size)),
        )

