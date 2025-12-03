# Business logic for freight calculation
# Module responsible for calculations only

from src.constants import (
    FATOR_CUBAGEM,
    VALOR_FRETE_POR_KG_CHEIO,
    PERCENTUAL_DESCONTO_KG,
    LIMITE_PESO_DESCONTO
)


def calcular_peso_cubado_azul(comprimento_cm, largura_cm, altura_cm):
    """Calcula o peso cubado com base nas dimensões em CM."""
    volume_m3 = (comprimento_cm / 100.0) * (largura_cm / 100.0) * (altura_cm / 100.0)
    peso_cubado_kg = volume_m3 * FATOR_CUBAGEM
    return round(peso_cubado_kg, 2)


def calcular_frete(comprimento_cm, largura_cm, altura_cm, peso_real_kg):
    """Calcula o frete e retorna um dicionário com todos os detalhes.

    Entradas: medidas em cm e peso real em kg.
    Retorna: dict com chaves: peso_cub, peso_real, peso_faturavel, peso_parte_descontada,
    peso_parte_cheia, valor_parte_descontada, valor_parte_cheia, valor_total_frete
    """
    peso_cub = calcular_peso_cubado_azul(comprimento_cm, largura_cm, altura_cm)
    peso_faturavel = max(peso_cub, peso_real_kg)

    if peso_faturavel <= LIMITE_PESO_DESCONTO:
        peso_parte_descontada = peso_faturavel
        peso_parte_cheia = 0.0
        valor_parte_descontada = peso_parte_descontada * VALOR_FRETE_POR_KG_CHEIO * PERCENTUAL_DESCONTO_KG
        valor_parte_cheia = 0.0
        valor_total_frete = valor_parte_descontada
    else:
        peso_parte_descontada = LIMITE_PESO_DESCONTO
        peso_parte_cheia = peso_faturavel - LIMITE_PESO_DESCONTO
        valor_parte_descontada = peso_parte_descontada * VALOR_FRETE_POR_KG_CHEIO * PERCENTUAL_DESCONTO_KG
        valor_parte_cheia = peso_parte_cheia * VALOR_FRETE_POR_KG_CHEIO
        valor_total_frete = valor_parte_descontada + valor_parte_cheia

    return {
        "peso_cub": round(peso_cub, 2),
        "peso_real": round(peso_real_kg, 2),
        "peso_faturavel": round(peso_faturavel, 2),
        "peso_parte_descontada": round(peso_parte_descontada, 2),
        "peso_parte_cheia": round(peso_parte_cheia, 2),
        "valor_parte_descontada": round(valor_parte_descontada, 2),
        "valor_parte_cheia": round(valor_parte_cheia, 2),
        "valor_total_frete": round(valor_total_frete, 2),
    }


def formatar_resultado(resp):
    """Formata o resultado do cálculo em string para exibição."""
    sep_eq = "=" * 55
    sep_dash = "-" * 55
    return (
        f"{sep_eq}\n"
        f"Peso cubado:      {resp['peso_cub']} kg\n"
        f"Peso real:        {resp['peso_real']} kg\n"
        f"**Peso faturável:   {resp['peso_faturavel']} kg** (Base da cobrança)\n"
        f"{sep_dash}\n"
        f"Até {LIMITE_PESO_DESCONTO}kg (c/ desc): {resp['peso_parte_descontada']} kg -> R$ {resp['valor_parte_descontada']:.2f}\n"
        f"Excedente (s/ desc): {resp['peso_parte_cheia']} kg -> R$ {resp['valor_parte_cheia']:.2f}\n"
        f"{sep_dash}\n"
        f"**VALOR TOTAL DO FRETE: R$ {resp['valor_total_frete']:.2f}**\n"
        f"{sep_eq}"
    )


def validar_entrada(valor: str, campo: str = "valor") -> tuple[bool, str]:
    """Validate and convert input to float."""
    if not valor or not valor.replace('.', '', 1).replace(',', '', 1).isdigit():
        return False, f"{campo} inválido"
    
    try:
        num = float(valor.replace(',', '.'))
        if num <= 0:
            return False, f"{campo} deve ser maior que 0"
        return True, str(num)
    except:
        return False, f"Erro ao processar {campo}"
