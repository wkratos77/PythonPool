def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sort_artifacts = sorted(artifacts, key=lambda x: x['power'], reverse=True)
    return sort_artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    powerful_mages = list(filter(lambda x: x['power'] >= min_power, mages))
    return powerful_mages


def spell_transformer(spells: list[str]) -> list[str]:
    transformed_spells = list(map(lambda x: f"* {x} *", spells))
    return transformed_spells


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {
            'max_power': None,
            'min_power': None,
            'avg_power': 0
        }
    max_mage = max(mages, key=lambda x: x['power'])
    max_power = max_mage['power']
    min_mage = min(mages, key=lambda x: x['power'])
    min_power = min_mage['power']
    sum_power = sum(map(lambda m: m["power"], mages))
    average_power = sum_power / len(mages)
    avg = round(average_power, 2)
    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg
    }


if __name__ == "__main__":
    artifacts = [
        {'name': 'Fire Staff', 'power': 63, 'type': 'relic'},
        {'name': 'Ice Wand', 'power': 66, 'type': 'armor'},
        {'name': 'Crystal Orb', 'power': 116, 'type': 'accessory'},
        {'name': 'Shadow Blade', 'power': 86, 'type': 'armor'}
    ]

    mages = [
        {'name': 'Luna', 'power': 53, 'element': 'ice'},
        {'name': 'Storm', 'power': 98, 'element': 'water'},
        {'name': 'Luna', 'power': 74, 'element': 'light'},
        {'name': 'Storm', 'power': 69, 'element': 'shadow'},
        {'name': 'Riley', 'power': 51, 'element': 'lightning'}
    ]

    spells = ['darkness', 'tsunami', 'meteor', 'freeze']

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    for artifact in sorted_artifacts:
        print(f"{artifact['name']} ({artifact['power']} power)")
    print()

    print("Testing power filter (min_power=70)...")
    strong_mages = power_filter(mages, 70)
    for mage in strong_mages:
        print(f"{mage['name']} ({mage['power']} power)")
    print()

    print("Testing spell transformer...")
    print(*spell_transformer(spells))
    print()

    print("Testing mage stats...")
    stats = mage_stats(mages)
    print(stats)
