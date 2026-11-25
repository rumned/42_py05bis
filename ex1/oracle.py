#!/usr/bin/env python3

import dotenv
import os
import sys


def load_config() -> dict[str, str | None]:
    env: dict[str, str | None] = {
        "Mode": os.environ.get("MATRIX_MODE"),
        "Database": os.environ.get("DATABASE_URL"),
        "Api Access": os.environ.get("API_KEY"),
        "Log Level": os.environ.get("LOG_LEVEL"),
        "Remote Network": os.environ.get("ZION_ENDPOINT")
    }
    return env


def check_config_development(env: dict[str, str | None]) -> None:
    if env["Database"]:
        print("Database: Connected to local instance")
    else:
        print("Database: Cannot connect to database, please check url",
              file=sys.stderr)

    if env["Api Access"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Unauthenticated", file=sys.stderr)

    if env["Log Level"]:
        print(f"Log Level: {env['Log Level']}")
    else:
        print("Log Level: DEBUG", file=sys.stderr)

    if env["Remote Network"]:
        print("Remote Network: Online")
    else:
        print("Remote Network: Undetected", file=sys.stderr)


def check_config_production(env: dict[str, str | None]) -> None:
    if env["Database"]:
        print("Database: Connected to database")
    else:
        print("Database: Cannot connect to database, program stop",
              file=sys.stderr)
        sys.exit(1)

    if env["Api Access"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Unauthenticated, program stop", file=sys.stderr)
        sys.exit(1)

    if env["Log Level"]:
        print(f"Log Level: {env['Log Level']}")
    else:
        print("Log Level: PRODUCTION", file=sys.stderr)

    if env["Remote Network"]:
        print("Remote Network: Online")
    else:
        print("Remote Network: Offline", file=sys.stderr)


def is_hardcode_secret(env: dict[str, str | None]) -> bool:
    try:
        with open(os.path.abspath(__file__), "r") as f:
            content = f.read()
    except OSError:
        return False

    for key in ("Database", "Api Access"):
        value = env[key]
        if value and value in content:
            return True
    return False


def env_is_ignored() -> bool:
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, ".gitignore")

    try:
        with open(path, "r") as f:
            lines = [line.strip() for line in f]
    except OSError:
        return False
    return ".env" in lines


def env_is_overrided(ori_env: dict[str, str | None]) -> bool:
    for key, value in ori_env.items():
        if value is None:
            continue
        after_value = os.environ.get(key)
        if after_value != value:
            return False
    return True


def security_check(
        env: dict[str, str | None], ori_env: dict[str, str | None]) -> None:
    if is_hardcode_secret(env):
        print("[WARNING] Hardcoded secrets detected")
    else:
        print("[OK] No hardcoded secrets detected")

    if env_is_ignored():
        print("[OK] .env file properly ignored by git")
    else:
        print("[WARNING] .env is not ignored by git")

    if env_is_overrided(ori_env):
        print("[OK] Production overrides available")
    else:
        print("[WARNING] Production overrides unavailable")


def dotenv_check() -> None:
    print("\nORACLE STATUS: Consulting the configuration...\n")
    ori_env_key = ("MATRIX_MODE", "DATABASE_URL", "API_KEY",
                   "LOG_LEVEL", "ZION_ENDPOINT")
    ori_env = {key: os.environ.get(key) for key in ori_env_key}
    dotenv.load_dotenv()
    env = load_config()
    print("Configuration loaded:")
    if env["Mode"] == "development":
        print("Mode: development")
        check_config_development(env)
    elif env["Mode"] == "production":
        print("Mode: production")
        check_config_production(env)
    elif env["Mode"] is None:
        print("[WARNING] Mode is blank, default 'development'")
        env["Mode"] = "development"
        check_config_development(env)
    else:
        print("[ERROR] Mode error", file=sys.stderr)

    print("")
    security_check(env, ori_env)

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    dotenv_check()
