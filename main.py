"""make.fun entry for news-image-20261119: one image that sums up the
world news of Thursday 19 November 2026.

The picture lives beside this program as entry.png: a front page whose
masthead names the day, whose lead panel shows GTA VI's worldwide launch,
and whose smaller panels cover the Strait of Hormuz tanker fires, the
Beijing summit of the Chinese, US and Russian leaders, the World Court's
Myanmar judgment, Voyager 1 reaching one light-day from Earth and the
record $190.4M Van Gogh sale, with a ticker of the day's other stories.

The program's whole job is to deliver those exact bytes to the grader:
read entry.png from this repository and write it, unchanged, as
entry.png in the output directory. Copying a fixed file keeps the two
scoring runs byte-identical, as the rules require.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    # The gate scores the exact bytes in the output file, so prove the
    # copy landed whole before exiting: same length, same content.
    with open(SOURCE, "rb") as fh:
        expected = fh.read()
    with open(target, "rb") as fh:
        written = fh.read()
    if written != expected:
        raise SystemExit("entry.png copy mismatch: output is not the entry image")


if __name__ == "__main__":
    main()
