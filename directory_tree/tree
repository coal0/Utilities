#! /usr/bin/env python

import argparse
import os
import re
import sys


def tree(path="./", indentation=4, ignore_hidden=False, pattern=None):
    """Build a directory tree starting at `path`. See also
    https://en.wikipedia.org/wiki/File:Files11_directory_hierarchy.svg

    Arguments
    * path: A relative or absolute path to use as starting point
            for the tree. Defaults to "./". [type: str]

    * indentation: The amount of spaces to indent each level with.
                   Defaults to 4. [type: int]

    * ignore_hidden: Ignore hidden files (starting with a period).
                     Defaults to False. [type: boolean]

    * pattern: If set, only matching files will be shown.
               Set to None to show all files. Defaults to None.
               [type: str / None]

    Returns
    * A directory tree [type: str]

    Example
    Assuming we're in the 'home' directory:

        >>> import tree
        >>> t = tree.tree(path="./")
        >>> t

        ./images
            foo.jpg
            bar.jpg
            ./images/personal
                spam.png
        ./documents
            eggs.docx

        >>> t = tree.tree(path="./", ignore_hidden=False)
        >>> t

        .hidden.txt
        ./images
            foo.jpg
            bar.jpg
            .hidden.jpg
            ./images/personal
                spam.png
        ./documents
            eggs.docx

        >>> t = tree.tree("./", 8, regex="(.*\.png)")
        >>> t

        ./images
                ./images/personal
                        spam.png
        ./documents
    """
    structure = "\n"
    tab = " "*indentation
    if pattern is None:
        for root, directories, files in os.walk(path):
            try:
                depth = root.count(os.sep)
                offset = tab * depth
                structure += offset + root + "\n"
            except OSError:
                continue
            for f in files:
                if ignore_hidden and f.startswith("."):    
                    continue
                try:
                    depth = os.path.join(root, f).count(os.sep)
                    offset = tab * depth
                    structure += offset + f + "\n"
                except OSError:
                    continue
    else:
        restriction = re.compile(pattern)
        for root, directories, files in os.walk(path):
            try:
                depth = root.count(os.sep)
                offset = tab * depth
                structure += offset + root + "\n"
            except OSError:
                continue
            for f in files:
                if ignore_hidden and f.startswith("."):    
                    continue
                if not re.match(restriction, f):
                    continue
                try:
                    depth = os.path.join(root, f).count(os.sep)
                    offset = tab * depth
                    structure += offset + f + "\n"
                except OSError:
                    continue
    structure = structure.split("\n")
    dedented = list(map(lambda e: e.replace(tab, "", 1), structure))[1:]
    return "\n".join(dedented)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path",
        help="the starting path for building the directory tree",
        type=str,
        default="./"
        )
    parser.add_argument(
        "--indentation",
        help="the amount of spaces to indent each new level with",
        type=int,
        default=4
    )
    parser.add_argument(
        "--ignore_hidden",
        help="ignore hidden files (starting with a dot '.')",
        action="store_true",
        default=False
    )
    parser.add_argument(
        "--pattern",
        help="show only files matching this pattern",
        type=str,
        default=None
    )
    args = parser.parse_args()

    print(tree(
        path=args.path,
        indentation=args.indentation,
        ignore_hidden=args.ignore_hidden,
        pattern=args.pattern
    ))
    sys.exit(0)
