import pytest

from financeiro.dinheiro import formatar, para_centavos


@pytest.mark.parametrize(
    "texto, esperado",
    [
        ("12,50", 1250),
        ("12,5", 1250),
        ("7", 700),
        ("R$ 7", 700),
        ("1.234,56", 123456),
        ("-60,00", -6000),
        ("0,01", 1),
    ],
)
def test_para_centavos(texto, esperado):
    assert para_centavos(texto) == esperado


@pytest.mark.parametrize("texto", ["12.50", "abc", "", "1,234", "1.23,00"])
def test_para_centavos_recusa_valores_invalidos(texto):
    with pytest.raises(ValueError):
        para_centavos(texto)


@pytest.mark.parametrize(
    "centavos, esperado",
    [
        (1250, "R$ 12,50"),
        (123456, "R$ 1.234,56"),
        (1, "R$ 0,01"),
        (-6000, "-R$ 60,00"),
        (0, "R$ 0,00"),
    ],
)
def test_formatar(centavos, esperado):
    assert formatar(centavos) == esperado


def test_ida_e_volta():
    assert para_centavos(formatar(389514).removeprefix("R$ ")) == 389514