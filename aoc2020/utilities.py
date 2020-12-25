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


def line_chunks_from_file(filename: str):
    """
    Yields a list of all lines containing text, separated by newline characters.
    """
    chunk = []
    for line in lines_from_file(filename):
        if not line:
            yield chunk
            chunk = []
        else:
            chunk.append(line)
    yield chunk
