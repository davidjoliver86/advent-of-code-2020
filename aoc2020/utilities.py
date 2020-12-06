"""
General helper functions
"""
import pathlib


def lines_from_file(filename: str):
    """
    Read a file relative to the fixtures folder and yield its lines.
    """
    for line in pathlib.Path(f"fixtures/{filename}").read_text().splitlines():
        yield line
