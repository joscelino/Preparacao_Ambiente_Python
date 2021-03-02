from .start import soma


def test_soma():
    """ Testing soma """

    result = soma(2, 4)
    concat = soma("ca", "lo")
    assert result == 6
    assert concat == "calo"
