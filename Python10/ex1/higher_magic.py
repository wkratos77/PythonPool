def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args, **kwargs) -> tuple:
        result1 = spell1(*args, **kwargs)
        result2 = spell2(*args, **kwargs)
        return (result1, result2)
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified(*args, **kwargs) -> int:
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster(*args, **kwargs) -> str:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(*args, **kwargs) -> list:
        return [spell(*args, **kwargs) for spell in spells]
    return sequence


if __name__ == "__main__":

    def fire(target):
        return f"Fireball hits {target}"

    def heal(target):
        return f"Heals {target}"

    def damage(target):
        return 10

    def strong(target):
        return target == "Dragon"

    print("Testing spell combiner...")
    combined = spell_combiner(fire, heal)
    print(*combined("Dragon"))

    print("\nTesting power amplifier...")
    mega = power_amplifier(damage, 3)
    print("Original:", damage("Dragon"))
    print("Amplified:", mega("Dragon"))
