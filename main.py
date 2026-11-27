#!/usr/bin/env python3
"""news-image-20261127 v7 -- entry program.

The entry image is pre-rendered and shipped next to this file as
entry.png (45 stories, 10 regions, Friday 27 November 2026). This
program only copies that file to the location the scoring harness
asks for, always as entry.png. It uses the standard library only.
"""

import os
import shutil
import sys

IMAGE_NAME = "entry.png"


def resolve_destination():
    """Work out where entry.png should go.

    Priority: argv[1], then MAKEFUN_OUTPUT_DIR, then ./output.
    A directory argument gets entry.png placed inside it; a file
    argument is used as-is when it already names entry.png.
    """
    target = None
    if len(sys.argv) > 1 and sys.argv[1]:
        target = sys.argv[1]
    elif os.environ.get("MAKEFUN_OUTPUT_DIR"):
        target = os.environ["MAKEFUN_OUTPUT_DIR"]

    if target:
        if os.path.isdir(target) or not target.endswith(IMAGE_NAME):
            return os.path.join(target, IMAGE_NAME)
        return target
    return os.path.join("output", IMAGE_NAME)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, IMAGE_NAME)
    if not os.path.isfile(source):
        raise SystemExit("missing shipped image: %s" % source)
    dest = resolve_destination()
    parent = os.path.dirname(dest)
    if parent:
        os.makedirs(parent, exist_ok=True)
    shutil.copyfile(source, dest)
    # Integrity check: the delivered file must be the shipped image.
    if os.path.getsize(dest) != os.path.getsize(source):
        raise SystemExit("copy incomplete: %s" % dest)


if __name__ == "__main__":
    main()
