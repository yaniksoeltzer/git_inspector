import pytest

from src.git_inspector.cli.continuous_git_reporter import ContinuousGitReporter


class MockTerminal:
    is_cleared = False

    def update(self, _: str):
        self.is_cleared = False

    def clear(self):
        self.is_cleared = True


@pytest.fixture
def mock_terminal():
    return MockTerminal()


def test_empty_output_on_empty_reports(mock_terminal):
    reporter = ContinuousGitReporter()
    reporter.terminal = mock_terminal
    reporter.finish()
