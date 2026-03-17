"""Memory Depths: Lexical Scoping and Closures"""


def mage_counter() -> callable:
    """Create a counting closure that tracks call count."""
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:
    """Create a power accumulator closure."""
    total_power = initial_power

    def accumulate(amount: int):
        nonlocal total_power
        total_power += amount
        return total_power

    return accumulate


def enchantment_factory(enchantment_type: str) -> callable:
    """Create enchantment functions with specific types."""
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, callable]:
    """Create a memory management system with store and recall."""
    memories = {}

    def store(key: str, value):
        memories[key] = value

    def recall(key: str):
        return memories.get(key, "Memory not found")

    return {'store': store, 'recall': recall}


if __name__ == "__main__":
    # Testing mage counter
    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    # Testing spell accumulator
    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(100)
    print("Starting power: 100")
    print(f"After adding 50: {accumulator(50)}")
    print(f"After adding 25: {accumulator(25)}")
    print(f"After adding 10: {accumulator(10)}")

    # Testing enchantment factory
    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    # Testing memory vault
    print("\nTesting memory vault...")
    vault = memory_vault()
    vault['store']('secret', 'Dragon Location')
    vault['store']('spell', 'Ultimate Fireball')
    print(f"Recalled 'secret': {vault['recall']('secret')}")
    print(f"Recalled 'spell': {vault['recall']('spell')}")
    print(f"Recalled 'missing': {vault['recall']('missing')}")
