from .light_spellbook import light_spell_allowed_ingredients
def validate_ingredients(ingredients: str) -> str:
    

    allowed = light_spell_allowed_ingredients()
    splitted = ingredients.lower().replace(",", " ").split()
    for i in splitted:
        if i.strip() in allowed:
            return f"({ingredients} - VALID)"
    return f"({ingredients} - INVALID)"
