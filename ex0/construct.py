#!/usr/bin/env python3

import os
import sys
import site


def virtual_enviroment_check() -> None:
    def in_venv() -> bool:
        return (sys.prefix != sys.base_prefix)

    if in_venv():
        print("LABORATORY STATUS: The laboratory is sealed\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You are working in an isolated environment!\n"
              "Safe to install reagents without affecting\n"
              "the global system\n")
        print("Reagent installation path:")
        print(f"{site.getsitepackages()[0]}")
    else:
        print("LABORATORY STATUS: You are working in the open\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You are in the global environment!"
              "Every reagent you install here leaks into the whole system\n")
        print("To seal the laboratory, run:\n"
              "python3 -m venv lab_env\n"
              "source lab_env/bin/activate # On Unix\n"
              "lab_env\\Scripts\\activate # On Windows\n\n"
              "Then run this program again.")


if __name__ == "__main__":
    virtual_enviroment_check()
