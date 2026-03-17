"""Ancient Library: Functools Treasures"""

import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce spell powers using specified operation."""
    operations = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': lambda a, b: a if operator.gt(a, b) else b,
        'min': lambda a, b: a if operator.lt(a, b) else b
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")

    return functools.reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    """Create partial applications of base enchantment."""
    return {
        'fire_enchant': functools.partial(
            base_enchantment, power=50, element='fire'
        ),
        'ice_enchant': functools.partial(
            base_enchantment, power=50, element='ice'
        ),
        'lightning_enchant': functools.partial(
            base_enchantment, power=50, element='lightning'
        ),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Calculate fibonacci with memoization."""
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    """Create single dispatch system for different spell types."""
    @functools.singledispatch
    def cast_spell(spell):
        return f"Unknown spell type: {type(spell)}"

    @cast_spell.register(int)
    def _(spell):
        return f"Damage spell: {spell} points of damage"

    @cast_spell.register(str)
    def _(spell):
        return f"Enchantment: {spell}"

    @cast_spell.register(list)
    def _(spell):
        spell_list = ', '.join(map(str, spell))
        return f"Multi-cast: {len(spell)} spells ({spell_list})"

    return cast_spell


if __name__ == "__main__":
    # Testing spell reducer
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    # Testing memoized fibonacci
    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
