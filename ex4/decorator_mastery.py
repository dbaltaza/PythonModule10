"""Master's Tower: Decorator Mastery and Class Methods"""

import functools
import time
from typing import Callable


def spell_timer(func: Callable) -> Callable:
    """Time execution decorator."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print(f"Spell completed in {elapsed_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    """Parameterized validation decorator."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get function signature to find 'power' parameter
            import inspect
            sig = inspect.signature(func)
            params = list(sig.parameters.keys())

            # Find power value
            power = None
            if 'power' in kwargs:
                power = kwargs['power']
            elif 'power' in params and len(args) > params.index('power'):
                power = args[params.index('power')]

            if power is not None and power < min_power:
                return "Insufficient power for this spell"

            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Retry decorator."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
                    else:
                        return (
                            "Spell casting failed after "
                            f"{max_attempts} attempts"
                        )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    """Mage Guild class demonstrating staticmethod."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Static method to validate mage names."""
        if len(name) < 3:
            return False
        # Check if contains only letters and spaces
        return all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Instance method to cast spells with power validation."""
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    # Testing spell timer
    print("Testing spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    # Testing power validator
    print("\nTesting power validator...")

    @power_validator(min_power=50)
    def powerful_spell(power: int):
        return f"Spell cast with {power} power"

    print(powerful_spell(75))
    print(powerful_spell(25))

    # Testing retry spell
    print("\nTesting retry spell...")

    attempt_count = 0

    @retry_spell(max_attempts=3)
    def unstable_spell():
        global attempt_count
        attempt_count += 1
        if attempt_count < 3:
            raise Exception("Spell fizzled")
        return "Spell succeeded!"

    result = unstable_spell()
    print(f"Result: {result}")

    # Testing MageGuild
    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("Al"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))
