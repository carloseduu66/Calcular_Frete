# Constants for Calcular Frete application
# Shared configuration used across modules

# Theme configuration
THEME = {
    'bg_main': '#2b2b2b',
    'bg_text': '#1e1e1e',
    'fg_text': '#f0f0f0',
    'btn_calc': '#00aa00',
    'btn_clear': '#ff6600',
    'btn_copy': '#0066cc',
    'font_title': ('Arial', 14, 'bold'),
    'font_normal': ('Arial', 11),
    'font_small': ('Arial', 9),
}

# Calculation constants - Azul Cargo Express
FATOR_CUBAGEM = 300  # fator padrão para volume em kg
VALOR_FRETE_POR_KG_CHEIO = 3.00
PERCENTUAL_DESCONTO_KG = 0.50  # 50% de desconto
LIMITE_PESO_DESCONTO = 30.0  # kg

# Window configuration
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 550
WINDOW_MIN_WIDTH = 700
WINDOW_MIN_HEIGHT = 400
