"""Higher Realm: Functions Operating on Functions"""


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    """Combine two spells into one that calls both."""
    def combined(*args, **kwargs):
        result1 = spell1(*args, **kwargs)
        result2 = spell2(*args, **kwargs)
        return (result1, result2)
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    """Amplify a spell's power by multiplying its result."""
    def amplified(*args, **kwargs):
        result = base_spell(*args, **kwargs)
        return result * multiplier
    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    """Cast a spell only if condition is met."""
    def conditional(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[callable]) -> callable:
    """Create a function that casts all spells in order."""
    def sequenced(*args, **kwargs):
        results = []
        for spell in spells:
            results.append(spell(*args, **kwargs))
        return results
    return sequenced


if __name__ == "__main__":
    # Define some example spells
    def fireball(target):
        return f"Fireball hits {target}"

    def heal(target):
        return f"Heals {target}"

    def damage_spell(target):
        return 10

    # Testing spell combiner
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon")
    print(f"Combined spell result: {result[0]}, {result[1]}")

    # Testing power amplifier
    print("\nTesting power amplifier...")
    mega_damage = power_amplifier(damage_spell, 3)
    original = damage_spell("Enemy")
    amplified = mega_damage("Enemy")
    print(f"Original: {original}, Amplified: {amplified}")
