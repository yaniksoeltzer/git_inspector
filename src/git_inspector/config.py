EXCLUDED_DIR_SELECTORS = [
    "Trash",
    "/proc",
    ".cache",
    "node_modules",
    "~/.cargo",
    "/tmp",
]


COLOR_ALERT = "\033[1;31m"
COLOR_WARNING = "\033[0;33m"
COLOR_SUCCESS = "\033[0;32m"
COLOR_RESET = "\033[0m"
COLOR_BRANCH_TAG = "\033[0;34m"
COLOR_REMOTE_TAG = "\033[0;36m"
COLOR_HINT = COLOR_RESET
SUMMARY_COLOR_NOT_CLEAN = "\033[0;91m"

COLORS = {
    1: COLOR_ALERT,
    2: COLOR_WARNING,
    3: COLOR_HINT,
}
