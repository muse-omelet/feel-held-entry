import os

TEXT = 'Somewhere, a kettle has just clicked off, and nobody is in a hurry to pour it. The window is warm with late light. Your cup is already full. There is nothing after this on the list — the list is done, the house is quiet, and the evening is keeping the rest for you.'


def main() -> None:
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
