"""
Write a function that recursively walks through a directory, printing its
contents. Indent with spaces based on recursion depth. (max 10 lines)
"""

from pathlib import Path


def show_path(path, level=0):
    if not path.is_dir():
        return
    for p in path.iterdir():
        print("{}{}".format("  " * level, p.name))
        if p.is_dir():
            show_path(p, level + 1)


if __name__ == "__main__":
    show_path(Path("/usr/local/lib"))
