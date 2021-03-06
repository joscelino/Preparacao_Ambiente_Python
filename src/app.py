from functools import lru_cache
from typing import Union


@lru_cache
def soma(
    valor_1: Union[str, int, float], valor_2: Union[str, int, float]
) -> Union[str, int, float]:
    """Sum two values.
    :param - valor_1: first value
           - valor_2: second value
    :return - Sum of valor_1 and valor_2 only
    """
    soma_dois_valores = valor_1 + valor_2
    return soma_dois_valores


SOMA_DOIS_NUMEROS = soma(1, 2.0524899927999035)
SOMA_DUAS_STRINGS = soma("Mar", "ia")

print(SOMA_DOIS_NUMEROS)
print(SOMA_DUAS_STRINGS)
