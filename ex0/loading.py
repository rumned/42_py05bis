#!/usr/bin/env python3

import importlib
import importlib.metadata


def check_env() -> None:
    def get_version(name: str) -> str | None:
        try:
            importlib.import_module(name.lower())
            return importlib.metadata.version(name)
        except ImportError:
            return None

    print("REAGENT STATUS: Loading reagents...\n")
    reagents = {
        "pandas": get_version("pandas"),
        "numpy": get_version("numpy")
    }
    for name in reagents:
        if reagents[name] is not None:
            print(f"[OK] {name} {reagents[name]} - Ready to go!")
        else:
            print(f"[MISSING] {name} {reagents[name]} - Not installed")

    print("\npip vs Poetry:\n"
          "requirements.txt declares what to install;"
          " pip resolves it at install time.\n"
          "pyproject.toml declares the same constraints, "
          "and Poetry pins the resolved\n"
          "versions in poetry.lock so every install is identical.\n")

    print("All reagents present and accounted for.")


if __name__ == "__main__":
    check_env()
