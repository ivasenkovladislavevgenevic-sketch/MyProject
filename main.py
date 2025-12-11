import sys


def main() -> None:
    data = sys.stdin.read().strip()
    if data:
        sys.stdout.write(data)


if __name__ == '__main__':
    main()
