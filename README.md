# Python Module 10 - Functional Programming

<div align="center">

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![42 School](https://img.shields.io/badge/42-School-000000?logo=42)
![License](https://img.shields.io/badge/license-MIT-green.svg)

*Master the art of functional programming in Python*

[Installation](#installation) • [Exercises](#exercises) • [Usage](#usage) • [Resources](#resources)

</div>

---

## 📋 Table of Contents

- [About](#about)
- [Installation](#installation)
- [Exercises](#exercises)
  - [Exercise 00: Lambda Expressions](#exercise-00-lambda-expressions)
  - [Exercise 01: Higher-Order Functions](#exercise-01-higher-order-functions)
  - [Exercise 02: Closures and Scoping](#exercise-02-closures-and-scoping)
  - [Exercise 03: Functools Module](#exercise-03-functools-module)
  - [Exercise 04: Decorators](#exercise-04-decorators)
- [Usage](#usage)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Resources](#resources)
- [Author](#author)

---

## About

This project is part of the **42 School** curriculum, focusing on functional programming paradigms in Python. Through five comprehensive exercises, you'll explore lambda expressions, higher-order functions, closures, the functools module, and decorators.

### Key Topics

- **Lambda Expressions** - Anonymous functions and functional transformations
- **Higher-Order Functions** - Functions as first-class citizens
- **Closures & Scoping** - Lexical scoping and state encapsulation
- **Functools Module** - Reduce, partial, memoization, and dispatch
- **Decorators** - Function wrapping and metaprogramming

---

## Installation

```bash
# Clone the repository
git clone https://github.com/dbaltaza/PythonModule10.git

# Navigate to project directory
cd PythonModule10

# Verify Python version (3.10+ required)
python3 --version
```

---

## Exercises

### Exercise 00: Lambda Expressions

**File:** `ex0/lambda_spells.py`

Master anonymous functions and lambda expressions through practical implementations.

**Functions:**
- `artifact_sorter(artifacts)` - Sort using lambda expressions
- `power_filter(mages, min_power)` - Filter data with lambda
- `spell_transformer(spells)` - Transform data using map()
- `mage_stats(mages)` - Calculate statistics with functional operations

**Concepts:**
- Lambda syntax and usage
- `map()`, `filter()`, `sorted()` with lambdas
- Functional data transformations

```bash
python3 ex0/lambda_spells.py
```

---

### Exercise 01: Higher-Order Functions

**File:** `ex1/higher_magic.py`

Explore functions as first-class citizens and function composition.

**Functions:**
- `spell_combiner(spell1, spell2)` - Function composition
- `power_amplifier(base_spell, multiplier)` - Function transformers
- `conditional_caster(condition, spell)` - Conditional execution
- `spell_sequence(spells)` - Sequential function execution

**Concepts:**
- Functions as arguments and return values
- Function composition patterns
- Building modular, reusable code

```bash
python3 ex1/higher_magic.py
```

---

### Exercise 02: Closures and Scoping

**File:** `ex2/scope_mysteries.py`

Understand lexical scoping, closures, and state encapsulation.

**Functions:**
- `mage_counter()` - Closure-based counter implementation
- `spell_accumulator(initial_power)` - State preservation with closures
- `enchantment_factory(enchantment_type)` - Factory pattern
- `memory_vault()` - Private data encapsulation

**Concepts:**
- Lexical scoping rules
- Closure mechanics and variable capture
- `nonlocal` keyword usage
- Factory patterns

```bash
python3 ex2/scope_mysteries.py
```

---

### Exercise 03: Functools Module

**File:** `ex3/functools_artifacts.py`

Explore Python's functools module for advanced functional programming.

**Functions:**
- `spell_reducer(spells, operation)` - Data reduction with reduce()
- `partial_enchanter(base_enchantment)` - Partial function application
- `memoized_fibonacci(n)` - Memoization with lru_cache
- `spell_dispatcher()` - Type-based dispatch with singledispatch

**Concepts:**
- `functools.reduce()` for aggregation
- `functools.partial()` for argument pre-filling
- `functools.lru_cache()` for performance optimization
- `functools.singledispatch()` for polymorphism

```bash
python3 ex3/functools_artifacts.py
```

---

### Exercise 04: Decorators

**File:** `ex4/decorator_mastery.py`

Master decorator patterns and function wrapping techniques.

**Functions:**
- `spell_timer(func)` - Execution timing decorator
- `power_validator(min_power)` - Parameterized decorators
- `retry_spell(max_attempts)` - Retry logic implementation
- `MageGuild` class - Static methods and class decorators

**Concepts:**
- Decorator syntax and patterns
- `functools.wraps()` for metadata preservation
- Decorator factories (parameterized decorators)
- `@staticmethod` decorator usage

```bash
python3 ex4/decorator_mastery.py
```

---

## Usage

### Running Tests

Execute individual exercises:

```bash
# Exercise 00
python3 ex0/lambda_spells.py

# Exercise 01
python3 ex1/higher_magic.py

# Exercise 02
python3 ex2/scope_mysteries.py

# Exercise 03
python3 ex3/functools_artifacts.py

# Exercise 04
python3 ex4/decorator_mastery.py
```

### Code Style Check

```bash
# Check all exercises
flake8 ex0/ ex1/ ex2/ ex3/ ex4/

# Check specific file
flake8 ex0/lambda_spells.py
```

---

## Learning Objectives

After completing this module, you will understand:

- ✅ Lambda expressions and anonymous functions
- ✅ Higher-order functions and function composition
- ✅ Closures and lexical scoping
- ✅ The functools module (reduce, partial, lru_cache, singledispatch)
- ✅ Decorator patterns and metaprogramming
- ✅ Functional programming principles in Python
- ✅ When to use functional vs object-oriented approaches

---

## Requirements

### Technical Requirements

- **Python:** 3.10 or higher
- **Code Style:** flake8 compliant
- **Type Hints:** Required for all functions
- **Documentation:** Clear and concise

### Allowed Imports

- `functools` - Core module for this project
- `typing` - Type hints
- `operator` - Functional operations
- `itertools` - Advanced iteration
- Standard library modules

### Restrictions

- ❌ No external libraries (no pip install)
- ❌ No file I/O operations
- ❌ No `eval()` or `exec()`
- ❌ Minimize global variables

---

## Resources

### Official Documentation

- [Python Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)
- [functools — Higher-order functions](https://docs.python.org/3/library/functools.html)
- [PEP 318 — Decorators](https://www.python.org/dev/peps/pep-0318/)

### Recommended Reading

- [Real Python - Functional Programming](https://realpython.com/python-functional-programming/)
- [Python Closures](https://realpython.com/inner-functions-what-are-they-good-for/)
- [Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/)

---

## Author

**dbaltaza** - [42 Intra Profile](https://profile.intra.42.fr/users/dbaltaza)

---

## License

This project is part of the 42 School curriculum.

---

<div align="center">

**[⬆ back to top](#python-module-10---functional-programming)**

Made with ☕ at 42 School

</div>
