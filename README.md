# 🐍 PythonPool (Modules 00 → 10)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Code Style](https://img.shields.io/badge/Style-flake8-informational)
![Focus](https://img.shields.io/badge/Focus-Software%20Engineering-success)
![Paradigms](https://img.shields.io/badge/Paradigms-OOP%20%7C%20FP%20%7C%20Architecture-purple)

> A structured, progressively advanced collection of Python modules (00 → 10) demonstrating strong foundations in **software engineering**, **object-oriented design**, **functional programming**, and **production-minded tooling**.

This repository contains my implementations for each module in the curriculum.  
Each module is built as a standalone learning unit and targets one major concept area (fundamentals → OOP → robustness → architecture → tooling → abstractions → FP).

---

## 📁 Repository Structure

```text
PythonPool/
├── Module00
├── Module01
├── Module02
├── Module03
├── Module04
├── Module05
├── Module06
├── Module07
├── Module08
├── Module09
└── Module10
```
---
## 🧭 Modules Roadmap (00 → 10)

| Module | Subject / Theme | What it demonstrates | Code |
|------:|------------------|----------------------|------|
| 00 | **Growing Code — Python Fundamentals Through Garden Data** | Variables, functions, control flow, type annotations | `Module00/` |
| 01 | **CodeCultivation — Object-Oriented Garden Systems** | Classes, methods, encapsulation, modeling | `Module01/` |
| 02 | **Garden Guardian — Data Engineering for Smart Agriculture** | Exceptions, custom errors, cleanup (`finally`), resilient logic | `Module02/` |
| 03 | **The Codex — Mastering Python’s Import Mysteries** | Packages, `__init__.py`, absolute vs relative imports, circular dependencies | `Module03/` |
| 04 | **Cyber Archives — File & Stream Operations (from repo code)** | File I/O, stream handling, safe resource management | `Module04/` |
| 05 | **Data Quest — Mastering Python Collections for Data Engineering** | Lists, tuples, sets, dictionaries, comprehensions, generators, pipelines | `Module05/` |
| 06 | **The Matrix — Real-World Data Engineering Setup** | Virtual environments, packaging, configuration mindset | `Module06/` |
| 07 | **DataDeck — Abstract Card Architecture** | Abstract Base Classes, interfaces, multiple inheritance, Strategy & Abstract Factory patterns | `Module07/` |
| 08 | **Code Nexus — Polymorphic Data Streams** | Inheritance, method overriding, subtype polymorphism, unified interfaces | `Module08/` |
| 09 | **Cosmic Data — Pydantic Models & Validation** | Pydantic v2 models, Field constraints, `model_validator`, nested models | `Module09/` |
| 10 | **FuncMage — Functional Programming Mastery** | Lambdas, higher-order functions, closures, `functools`, decorators | `Module10/` |

---

## ⭐ Highlights (Recruiter-Relevant Engineering Skills)

### ✅ Software Design & Architecture

- Abstract Base Classes (`abc`) and enforceable contracts  
- Interface segregation and composition  
- Multiple inheritance (clean and controlled)  
- Strategy Pattern & Abstract Factory Pattern *(DataDeck Engine)*

### ✅ Robustness & Maintainability

- Defensive programming and exception design  
- Clean module boundaries and package organization  
- Practical project structuring *(execution from module root, import hygiene)*

### ✅ Data Engineering Mindset

- Efficient collection usage and generator-based pipelines  
- Typed, validated data models *(Pydantic v2)*  
- Environment and dependency setup *(virtual environments, configuration)*

### ✅ Functional Programming

- Closures for private state  
- Higher-order functions for composition  
- Decorators for separation of concerns *(timing, validation, retry)*

---

## ▶️ How to Run

### General Rule

Most modules can be run by executing scripts inside the module exercises:

```bash
python3 Module00/ex0/...
python3 Module05/ex3/...
python3 Module10/ex4/...
```
### Module07 (DataDeck) — Important

DataDeck is structured as a Python package with required __init__.py files and must be executed using module mode:
```bash
cd Module07

python3 -m ex0.main
python3 -m ex1.main
python3 -m ex2.main
python3 -m ex3.main
python3 -m ex4.main
Module09 (Pydantic)
```
### Module09 uses Pydantic v2. Recommended setup:
```bash
python3 -m venv .venv
source .venv/bin/activate

pip install pydantic

python3 Module09/ex0/space_station.py
```
## 📌 Module Details (What each one teaches)
### Module00 — Growing Code

- Focus: Python fundamentals through practical exercises

- Expressions, variables, and control flow

-Functions and basic problem-solving

- Introduction to type annotations

### Module01 — CodeCultivation

- Focus: Object-oriented modeling

- Building class-based systems

- Encapsulation, methods, and constructors

- Scalable data modeling mindset

### Module02 — Garden Guardian

- Focus: Resilient programming

- try / except / finally patterns

- Custom exception types

- Raising errors intentionally

- Reliable resource cleanup

### Module03 — The Codex

- Focus: Python import system mastery

- Package initialization (__init__.py)

- Import pathways and module resolution

- Absolute vs relative import decisions

- Breaking circular dependency chains

### Module04 — Cyber Archives

- Focus: File and stream operations

- Reading and writing files

- Stream management

- Safe file access using with open(...)

- Handling missing files and corrupted states safely

### Module05 — Data Quest

- Focus: Collections and efficiency

- Lists, tuples, sets, and dictionaries

- Comprehensions and generator expressions

- Practical data transformations and pipelines

### Module06 — The Matrix

- Focus: Professional Python environments

- Virtual environments

- Dependency management mindset

- Configuration patterns and isolation

### Module07 — DataDeck

- Focus: Abstract architecture and system design

- Abstract Base Class foundations (Card)

- Polymorphic concrete implementations

- Interface composition (Combatable, Magical)

- Design patterns: Strategy + Abstract Factory

- Clean package execution (python3 -m exN.main)

### Module08 — Code Nexus

- Focus: Polymorphism

- Overriding behavior while keeping a unified interface

- Designing inheritance hierarchies

- Building systems that scale with new types

### Module09 — Cosmic Data

- Focus: Typed data validation (Pydantic v2)

- BaseModel with Field constraints

- Custom validation via @model_validator(mode="after")

- Nested models and structured relationships

- Clean error reporting for invalid data

### Module10 — FuncMage

- Focus: Functional programming patterns

- Lambda expressions

- Higher-order functions and function composition

- Closures and lexical scoping

- functools utilities (reduce, partial, lru_cache, singledispatch)

- Decorators and @staticmethod patterns

## 🛠 Tech Stack

- Python 3.10+

- flake8 style compliance (where required)

- Python Standard Library (functools, operator, abc, typing, etc.)

- Pydantic v2 (Module09)

##👤 Author

Walid Krati
Software Engineering Student — Python • Backend • Architecture
