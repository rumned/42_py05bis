import sys

is_global = sys.prefix == sys.base_prefix
if (is_global):
    print("\nLABORATORY STATUS: You are working in the open\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You are in the global environment!")
    print("Every reagent you install here leaks into the whole system.\n")
    print("To seal the laboratory, run:\n"
          "python3 -m venv lab_env\n"
          "source lab_env/bin/activate # On Unix\n"
          "lab_env\\Scripts\\activate # On Windows\n\n"
          "Then run this program again.")
else:
    print("LABORATORY STATUS: The laboratory is sealed")
