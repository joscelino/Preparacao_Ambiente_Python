from .start import soma


def test_soma():
    result = soma(2, 4)
    concat = soma("ca", "sa")
    assert result == 6
    assert concat == "casa"
