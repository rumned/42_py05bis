from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    splitted = ingredients.lower().replace(",", " ").split()
    for i in splitted:
        if i.strip() in allowed:
            return f"({ingredients} - VALID)"
    return f"({ingredients} - INVALID)"
