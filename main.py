import sys


def main() -> None:
    data = sys.stdin.read()
    # Input contains a single natural number; echo it verbatim.
    if data:
        sys.stdout.write(data)


if __name__ == "__main__":
    main()
