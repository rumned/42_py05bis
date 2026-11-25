def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    from .dark_validator import dark_validate_ingredients
    validation = dark_validate_ingredients(ingredients)

    if "INVALID" in validation:
        print (f"Spell rejected: {spell_name.capitalize()} {validation}")
    print (f"Spell recorded: {spell_name.capitalize()} {validation}")
