from pathlib import Path
import sys


def main():
    # Resolve entry.txt next to this file, so the script works from any cwd.
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    sys.stdout.write(entry_path.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
