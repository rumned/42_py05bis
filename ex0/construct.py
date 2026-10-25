import sys

in_venv = sys.prefix != sys.base_prefix
print(in_venv)