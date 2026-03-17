"""Ancient Library: Functools Treasures"""

import functools
import operator
from typing import Callable


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


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
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


def spell_dispatcher() -> Callable:
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
    print(f"Spells: {spells}")
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    print(f"Min: {spell_reducer(spells, 'min')}")

    # Testing partial enchanter
    print("\nTesting partial enchanter...")

    def enchant(power: int, element: str, target: str):
        return (
            f"{element.capitalize()} enchantment "
            f"({power} power) on {target}"
        )

    enchants = partial_enchanter(enchant)
    print(enchants['fire_enchant'](target='Sword'))
    print(enchants['ice_enchant'](target='Shield'))
    print(enchants['lightning_enchant'](target='Staff'))

    # Testing memoized fibonacci
    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Fib(20): {memoized_fibonacci(20)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    # Testing spell dispatcher
    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(50))
    print(dispatcher("Lightning Strike"))
    print(dispatcher(["Fireball", "Ice Blast", "Heal"]))
