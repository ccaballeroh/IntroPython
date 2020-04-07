"""
Script to generate Markdown files with solutions
"""
from pathlib import Path

SOLUTIONS: Path = Path(r"../Solutions/")
MD: Path = Path(r"../md/")


def read_script(*, filename: Path) -> str:
    assert filename.is_file(), "File does not exist"
    with filename.open(mode="r") as f:
        return f.read()


def write_md(*, filename: Path, content: str) -> None:
    assert len(content) > 0, "File empty"
    with open(MD / (script.stem + ".md"), mode="w") as f:
        f.write("```python\n")
        f.write(content)
        f.write("```")
    return None


if __name__ == "__main__":
    try:
        for script in SOLUTIONS.iterdir():
            if script.suffix == ".py":
                content: str = read_script(filename=script)
                write_md(filename=script, content=content)
                print(f"{script} converted")
        input()
    except AssertionError as e:
        print(script, e)
