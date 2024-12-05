from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Retourne une fonction qui multiplie un flottant par le multiplicateur donné."""
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
