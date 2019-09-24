"""
Write a function `cd(current_path, cd_argument)` that returns the new path after
using the cd argument. So cd('/some/path', '../anotherpath') would return
'/some/anotherpath'. This function must return the same as cd would place you
in. Assume any folder exists. (max 15 lines)
"""

from pathlib import Path


def cd(current_path, cd_argument):
    res = list(Path(current_path).parts)
    dst = Path(cd_argument)

    if dst.parts[0] == "/":
        return str(dst)

    for part in dst.parts:
        if part == "..":
            if len(res) > 1:
                res.pop()
        elif part in (".", "/"):
            pass
        else:
            res.append(part)

    return str(Path(*res))
