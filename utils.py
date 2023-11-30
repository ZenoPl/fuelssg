"""_summary_

Returns:
    _type_: _description_
"""

import os
from typing import Optional


def get_list_of_files_from_dir(
    dirname: str, ext: Optional[list[str]] = None
) -> tuple[list[str], list[str]]:
    """Returns tuple of lists: files and subdirectories. Starting at dirname and going recursively.

    Modified from stackoverflow answer:
    https://stackoverflow.com/questions/18394147/how-to-do-a-recursive-sub-folder-search-and-return-files-in-a-list#59803793

    Args:
        dirname (str): path do directory we want a file list of, recursively
        ext (Optional[list[str]], optional): List of file extensions we're looking for.
            Extensions should be provided without leading '.', i.e ["json"] NOT [".json"].
            Defaults to None.

    Returns:
        tuple[list[str], list[str]]: touple of: list of all files with full paths that were
        found in and under dirname (recursively).
        If ext list is set list contains only files with extensions provided
        AND
        list of all subfolders that were found under dirname (not including dirname)
    """
    subdirectories: list[str] = []
    files: list[str] = []

    for f in os.scandir(path=dirname):
        if f.is_dir():
            subdirectories.append(f.path)

        if f.is_file():
            if not ext:
                files.append(f.path)
            elif os.path.splitext(p=f.name)[1].lower()[1:] in ext:
                files.append(f.path)

    for d in subdirectories:
        f, sd = get_list_of_files_from_dir(dirname=d, ext=ext)
        subdirectories.extend(sd)
        files.extend(f)
    return files, subdirectories
