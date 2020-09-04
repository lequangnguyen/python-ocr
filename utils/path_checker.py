import os


def check_file_path(path):
    """Check file path."""
    return bool(os.path.exists(path))
