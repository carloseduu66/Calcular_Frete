# Unit tests for calculator module

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.calculator import (
    calcular_peso_cubado_azul,
    calcular_frete,
    validar_entrada,
    formatar_resultado
)


def test_calcular_peso_cubado_azul():
    """Test cubed weight calculation."""
    result = calcular_peso_cubado_azul(100, 100, 100)
    expected = 1.0 * 300  # 1 m³ * 300 = 300 kg
    assert abs(result - expected) < 0.01, f"Expected {expected}, got {result}"
    print("✓ test_calcular_peso_cubado_azul passed")


def test_calcular_frete_com_desconto():
    """Test freight calculation with discount (weight <= 30kg)."""
    result = calcular_frete(100, 100, 100, 10)  # 10kg real, 300kg cubado = 300kg faturável
    # 300kg > 30kg limit, so: 30kg * 3.00 * 0.5 = 45 + (270kg * 3.00) = 45 + 810 = 855
    assert result['peso_faturavel'] == 300, f"Expected 300, got {result['peso_faturavel']}"
    print("✓ test_calcular_frete_com_desconto passed")


def test_calcular_frete_sem_desconto():
    """Test freight calculation without discount."""
    result = calcular_frete(10, 10, 10, 5)
    # Volume: 0.001 m³ * 300 = 0.3 kg, peso faturável = 5kg
    # 5kg <= 30kg: 5 * 3.00 * 0.5 = 7.50
    assert result['valor_total_frete'] == 7.50, f"Expected 7.50, got {result['valor_total_frete']}"
    print("✓ test_calcular_frete_sem_desconto passed")


def test_validar_entrada_valid():
    """Test input validation with valid data."""
    valid, value = validar_entrada("10.5")
    assert valid and float(value) == 10.5, "Should validate correct input"
    print("✓ test_validar_entrada_valid passed")


def test_validar_entrada_invalid():
    """Test input validation with invalid data."""
    valid, msg = validar_entrada("abc")
    assert not valid, "Should reject non-numeric input"
    print("✓ test_validar_entrada_invalid passed")


def test_formatar_resultado():
    """Test result formatting."""
    result = calcular_frete(100, 100, 100, 20)
    formatted = formatar_resultado(result)
    assert "VALOR TOTAL DO FRETE" in formatted, "Should contain total value"
    assert "kg" in formatted, "Should contain kg unit"
    print("✓ test_formatar_resultado passed")


if __name__ == "__main__":
    test_calcular_peso_cubado_azul()
    test_calcular_frete_com_desconto()
    test_calcular_frete_sem_desconto()
    test_validar_entrada_valid()
    test_validar_entrada_invalid()
    test_formatar_resultado()
    print("\n✓ All tests passed!")
