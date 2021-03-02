from typing import Union


def soma(
    valor_1: Union[str, int, float], valor_2: Union[str, int, float]
) -> Union[str, int, float]:
    """Sum two values
    :param - valor_1: first value
           - valor_2: second value
    :return - Sum of valor_1 and valor_2 only
    """
    soma_dois_valores = valor_1 + valor_2
    return soma_dois_valores


SOMA_DOIS_NUMEROS = soma(1, 2)
SOMA_DUAS_STRINGS = soma("mar", "ia")
