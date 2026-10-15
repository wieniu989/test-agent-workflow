"""Wypisuje powitanie dla imienia podanego jako argument wiersza poleceń.

Użycie:
    python hello.py <imie>
"""

import sys


def main(argv):
    if len(argv) < 2 or not argv[1].strip():
        print("Użycie: python hello.py <imie>", file=sys.stderr)
        return 1
    print(f"Witaj, {argv[1].strip()}!")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
