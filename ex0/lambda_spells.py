"""Lambda Sanctum: Mastering Anonymous Functions"""


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort magical artifacts by power level (descending)."""
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Filter mages by minimum power level."""
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Transform spell names with prefix and suffix."""
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Calculate statistics for mages' power levels."""
    powers = list(map(lambda mage: mage['power'], mages))
    return {
        'max_power': max(powers, key=lambda x: x),
        'min_power': min(powers, key=lambda x: x),
        'avg_power': round(sum(powers, 0) / len(powers), 2)
    }


if __name__ == "__main__":
    # Testing artifact sorter
    print("Testing artifact sorter...")
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'staff'},
        {'name': 'Ice Wand', 'power': 78, 'type': 'wand'}
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]['name']} "
        f"({sorted_artifacts[0]['power']} power) "
        f"comes before {sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
    )

    # Testing spell transformer
    print("\nTesting spell transformer...")
    spells = ['fireball', 'heal', 'shield']
    transformed = spell_transformer(spells)
    print(' '.join(transformed))
