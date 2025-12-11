import sys


def main() -> None:
    data = sys.stdin.read().strip()
    if not data:
        return
    token = data.split()[0]
    sys.stdout.write(token)


if __name__ == "__main__":
    main()
