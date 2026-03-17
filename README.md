# FuncMage Chronicles: Master the Ancient Arts of Functional Programming

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│    ███████╗██╗   ██╗███╗   ██╗ ██████╗███╗   ███╗ █████╗   │
│    ██╔════╝██║   ██║████╗  ██║██╔════╝████╗ ████║██╔══██╗  │
│    █████╗  ██║   ██║██╔██╗ ██║██║     ██╔████╔██║███████║  │
│    ██╔══╝  ██║   ██║██║╚██╗██║██║     ██║╚██╔╝██║██╔══██║  │
│    ██║     ╚██████╔╝██║ ╚████║╚██████╗██║ ╚═╝ ██║██║  ██║  │
│    ╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚═╝     ╚═╝╚═╝  ╚═╝  │
│                                                             │
│              Master the Ancient Arts of                     │
│           Functional Programming in Python                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 📚 Table of Contents

- [About](#about)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Exercises](#exercises)
  - [Exercise 0: Lambda Sanctum](#exercise-0-lambda-sanctum)
  - [Exercise 1: Higher Realm](#exercise-1-higher-realm)
  - [Exercise 2: Memory Depths](#exercise-2-memory-depths)
  - [Exercise 3: Ancient Library](#exercise-3-ancient-library)
  - [Exercise 4: Master's Tower](#exercise-4-masters-tower)
- [Installation & Testing](#installation--testing)
- [Learning Objectives](#learning-objectives)
- [Author](#author)

---

## 🎯 About

Welcome to **FuncMage Chronicles**, an epic journey through the mystical realms of functional programming in Python! This project explores five powerful paradigms that will transform how you think about code.

You've mastered Python fundamentals, conquered object-oriented programming, and learned exception handling. Now it's time to discover the elegant art of functional programming through an engaging fantasy-themed adventure.

---

## ⚡ Prerequisites

- **Python 3.10+** installed
- Solid understanding of:
  - Python functions and classes
  - Exception handling
  - Basic data structures (lists, dictionaries)
  - Type hints
- **flake8** for code style checking

**Important**: Focus on understanding **WHY** functional programming patterns are powerful, not just **HOW** to implement them.

---

## 📂 Project Structure

```
PythonModule10/
│
├── ex0/
│   └── lambda_spells.py          # Lambda expressions & anonymous functions
│
├── ex1/
│   └── higher_magic.py            # Higher-order functions
│
├── ex2/
│   └── scope_mysteries.py         # Lexical scoping & closures
│
├── ex3/
│   └── functools_artifacts.py     # functools module mastery
│
├── ex4/
│   └── decorator_mastery.py       # Decorators & class methods
│
└── README.md
```

---

## 🧙 Exercises

### Exercise 0: Lambda Sanctum
**Master anonymous functions and lambda expressions**

**Location:** `ex0/lambda_spells.py`

**Functions:**
- `artifact_sorter(artifacts)` - Sort artifacts by power using lambda
- `power_filter(mages, min_power)` - Filter mages by minimum power
- `spell_transformer(spells)` - Transform spell names with map()
- `mage_stats(mages)` - Calculate max, min, avg power statistics

**Key Concepts:**
- Lambda syntax: `lambda args: expression`
- Using `map()`, `filter()`, `sorted()` with lambdas
- When to use lambda vs. named functions

**Test:**
```bash
python3 ex0/lambda_spells.py
```

---

### Exercise 1: Higher Realm
**Discover the power of higher-order functions**

**Location:** `ex1/higher_magic.py`

**Functions:**
- `spell_combiner(spell1, spell2)` - Combine two functions into one
- `power_amplifier(base_spell, multiplier)` - Amplify function results
- `conditional_caster(condition, spell)` - Conditional function execution
- `spell_sequence(spells)` - Execute functions in sequence

**Key Concepts:**
- Functions as first-class citizens
- Passing functions as arguments
- Returning functions from functions
- Function composition

**Test:**
```bash
python3 ex1/higher_magic.py
```

---

### Exercise 2: Memory Depths
**Understand lexical scoping and closures**

**Location:** `ex2/scope_mysteries.py`

**Functions:**
- `mage_counter()` - Closure-based counter
- `spell_accumulator(initial_power)` - Power accumulation with state
- `enchantment_factory(enchantment_type)` - Function factory pattern
- `memory_vault()` - Private data encapsulation

**Key Concepts:**
- Lexical scoping
- Closures and captured variables
- `nonlocal` keyword
- State preservation without global variables
- Factory pattern

**Test:**
```bash
python3 ex2/scope_mysteries.py
```

---

### Exercise 3: Ancient Library
**Explore the functools module's treasures**

**Location:** `ex3/functools_artifacts.py`

**Functions:**
- `spell_reducer(spells, operation)` - Reduce with operator module
- `partial_enchanter(base_enchantment)` - Partial application
- `memoized_fibonacci(n)` - Cached fibonacci with lru_cache
- `spell_dispatcher()` - Single dispatch by type

**Key Concepts:**
- `functools.reduce()` for data aggregation
- `functools.partial()` for argument pre-filling
- `functools.lru_cache()` for memoization
- `functools.singledispatch()` for type-based dispatch
- `operator` module functions

**Test:**
```bash
python3 ex3/functools_artifacts.py
```

---

### Exercise 4: Master's Tower
**Create powerful decorators and class methods**

**Location:** `ex4/decorator_mastery.py`

**Functions:**
- `spell_timer(func)` - Execution timing decorator
- `power_validator(min_power)` - Parameterized validation decorator
- `retry_spell(max_attempts)` - Retry logic decorator
- `MageGuild` class - Demonstrates `@staticmethod`

**Key Concepts:**
- Decorator syntax and patterns
- `functools.wraps()` for metadata preservation
- Parameterized decorators (decorator factories)
- `@staticmethod` vs instance methods
- Separation of concerns

**Test:**
```bash
python3 ex4/decorator_mastery.py
```

---

## 🚀 Installation & Testing

### Setup
```bash
# Clone the repository
git clone <your-repo-url>
cd PythonModule10

# Verify Python version
python3 --version  # Should be 3.10+
```

### Running Individual Exercises
```bash
# Exercise 0 - Lambda Sanctum
python3 ex0/lambda_spells.py

# Exercise 1 - Higher Realm
python3 ex1/higher_magic.py

# Exercise 2 - Memory Depths
python3 ex2/scope_mysteries.py

# Exercise 3 - Ancient Library
python3 ex3/functools_artifacts.py

# Exercise 4 - Master's Tower
python3 ex4/decorator_mastery.py
```

### Code Style Check
```bash
# Check all files
flake8 ex0/ ex1/ ex2/ ex3/ ex4/

# Check specific exercise
flake8 ex0/lambda_spells.py
```

---

## 🎓 Learning Objectives

By completing this project, you will master:

1. **Lambda Expressions**
   - Anonymous function syntax
   - Functional transformations with map/filter/sorted
   - When to use lambda vs. named functions

2. **Higher-Order Functions**
   - Functions as first-class citizens
   - Function composition and combination
   - Building modular, reusable code

3. **Closures & Scope**
   - Lexical scoping rules
   - Capturing variables in closures
   - State encapsulation without classes
   - Factory patterns

4. **Functools Mastery**
   - Data reduction and aggregation
   - Partial application for specialization
   - Memoization for performance
   - Single dispatch for polymorphism

5. **Decorators**
   - Wrapping functions to modify behavior
   - Parameterized decorators
   - Cross-cutting concerns (logging, timing, validation)
   - Class method decorators

---

## 💡 Key Takeaways

### When to Use Each Pattern

| Pattern | Use Case | Example |
|---------|----------|---------|
| **Lambda** | Simple, one-time transformations | `sorted(items, key=lambda x: x['value'])` |
| **Higher-Order** | Function composition, callbacks | Middleware, event handlers |
| **Closures** | Private state, factories | Configuration builders, counters |
| **Functools** | Data processing, optimization | reduce(), partial(), caching |
| **Decorators** | Cross-cutting concerns | Logging, authentication, timing |

### Functional Programming Principles

1. **Immutability** - Avoid modifying data in place
2. **Pure Functions** - Same input → same output, no side effects
3. **Function Composition** - Build complex functions from simple ones
4. **Higher Abstraction** - Think in terms of transformations, not loops

---

## 📖 Common Instructions

### General Rules
- Python 3.10 or later
- Follow flake8 coding standard
- Use type hints for all functions
- Handle exceptions gracefully
- Write clean, readable code
- Focus on demonstrating functional patterns clearly

### Authorized Imports
- `functools` - Essential for this project
- `typing` - For type hints
- `operator` - For functional operations
- `itertools` - For advanced iteration
- Standard library modules as needed
- **NO external libraries** (no pip install)

### Forbidden
- External libraries (no pip install)
- File I/O operations
- `eval()` or `exec()`
- Global variables (embrace functional purity)
- Complex algorithms (focus on functional patterns)

---

## 🎮 Philosophy

> *"A great Function Mage understands the philosophy behind the magic."*

This project isn't just about learning syntax—it's about understanding:
- **Why** functional patterns make code more maintainable
- **How** immutability prevents bugs
- **When** to choose functional vs. object-oriented approaches
- **What** makes code elegant and reusable

---

## 🏆 Evaluation

During peer-review, you may be asked to:
- Explain functional programming concepts
- Demonstrate how closures capture variables
- Show how decorators transform functions
- Discuss advantages of functional patterns
- Live-code simple functional transformations

**Focus:** Understanding concepts over memorizing syntax!

---

## ✨ Author

- 42 Intra: `dbaltaza`

---

## 📜 License

This project is part of the 42 School curriculum.

---

```
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║  "With great functions comes great responsibility."       ║
║                                        - Uncle Lambda      ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
```

**Congratulations, Function Mage! May your code be pure and your closures be tight! 🧙‍♂️✨**
