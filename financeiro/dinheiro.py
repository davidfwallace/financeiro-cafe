"""Dinheiro no sistema é sempre um int em centavos (R$ 12,50 -> 1250), nunca float."""


def para_centavos(texto: str) -> int:
    """Converte um valor no formato brasileiro em centavos.

    Aceita "12,50", "1.234,56", "R$ 7", "-60,00" e "12,5".
    Recusa o formato americano ("12.50"), pra não virar R$ 1.250 sem ninguém perceber.
    """
    limpo = texto.strip().replace("R$", "").replace(" ", "")
    negativo = limpo.startswith("-")
    limpo = limpo.removeprefix("-")

    reais, _, centavos = limpo.partition(",")
    grupos = reais.split(".")
    if len(grupos) > 1 and any(len(g) != 3 for g in grupos[1:]):
        raise ValueError(f"Valor inválido: {texto!r} (use vírgula nos centavos)")
    reais = "".join(grupos)

    if len(centavos) > 2:
        raise ValueError(f"Valor inválido: {texto!r} (mais de 2 casas decimais)")
    centavos = centavos.ljust(2, "0")

    if not reais.isdigit() or not centavos.isdigit():
        raise ValueError(f"Valor inválido: {texto!r}")

    valor = int(reais) * 100 + int(centavos)
    return -valor if negativo else valor


def formatar(centavos: int) -> str:
    """Formata centavos como dinheiro: 123456 -> "R$ 1.234,56"."""
    sinal = "-" if centavos < 0 else ""
    reais, resto = divmod(abs(centavos), 100)
    reais_txt = f"{reais:,}".replace(",", ".")
    return f"{sinal}R$ {reais_txt},{resto:02d}"