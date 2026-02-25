def mage_counter() -> callable:
    mage_count = 0

    def counter() -> int:
        nonlocal mage_count
        mage_count += 1
        return mage_count
    return counter


def spell_accumulator(initial_power: int) -> callable:
    total_power = initial_power

    def accumulator(spell_power: int) -> int:
        nonlocal total_power
        total_power += spell_power
        return total_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:

    def create_enchantment(item_name) -> str:
        return f"{enchantment_type} {item_name}"
    return create_enchantment


def memory_vault() -> dict[str, callable]:
    vault = {}

    def store_spell(spell_name: str, spell_function: callable) -> None:
        vault[spell_name] = spell_function

    def recall_spell(spell_name: str) -> callable:
        return vault.get(spell_name, "Memory not found")
    return {
        'store': store_spell,
        'recall': recall_spell
    }
