import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return functools.reduce(operator.add, spells, 0)
    elif operation == "multiply":
        return functools.reduce(operator.mul, spells, 1)
    elif operation == "max":
        return functools.reduce(operator.max, spells)
    elif operation == "min":
        return functools.reduce(operator.min, spells)
    else:
        raise ValueError(
            "Invalid operation. Use 'add', 'multiply', 'max', or 'min'.")


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    fire = functools.partial(base_enchantment, 50, "fire")
    ice = functools.partial(base_enchantment, 50, "ice")
    lightning = functools.partial(base_enchantment, 50, "lightning")
    return {
        'fire_enchant': fire,
        'ice_enchant': ice,
        'lightning_enchant': lightning
    }


def memoized_fibonacci(n: int) -> int:
    @functools.lru_cache(maxsize=None)
    def fib(n):
        if n <= 1:
            return n
        return fib(n-1) + fib(n-2)
    return fib(n)


def spell_dispatcher() -> callable:

    @functools.singledispatch
    def dispatch(arg):
        return "Unknown spell"

    @dispatch.register(int)
    def _(arg: int):
        return f"Damage spell: {arg}"

    @dispatch.register(str)
    def _(arg: str):
        return f"Enchantment: {arg}"

    @dispatch.register(list)
    def _(arg: list):
        return f"Multi-cast: {', '.join(map(str, arg))}"

    return dispatch
