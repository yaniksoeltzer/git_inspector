import sys


class ActiveTerminalText:
    def __init__(self, start_output):
        self.last_output = start_output
        print(start_output)

    def update(self, new_output: str):
        self._clear_previous()
        print(new_output)
        self.last_output = new_output

    def _clear_previous(self):
        n_new_lines = self.last_output.count("\n") + 1
        for _ in range(n_new_lines):
            sys.stdout.write("\033[F")  # Cursor up one line
            sys.stdout.write("\033[K")  # Clear to the end of line
