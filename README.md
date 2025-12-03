# 📦 Calculadora de Frete - Azul Cargo Express

Uma aplicação profissional para cálculo de frete com interface gráfica, lógica de negócio modular e distribuição como executável Windows.

## ✨ Características

- ✅ **Interface Gráfica Moderna**: Tkinter com tema escuro profissional
- ✅ **Cálculo Preciso**: Sistema de peso cubado + desconto progressivo
- ✅ **Modular e Reutilizável**: Separação clara entre lógica e UI
- ✅ **Testado**: Suite de testes unitários automatizados
- ✅ **Distribuível**: Executável Windows standalone (10.93 MB)
- ✅ **Profissional**: Estrutura de pastas adequada para produção

## 🎯 O Que a Calculadora Faz

### Cálculo de Frete com Desconto Progressivo
- **Peso Cubado**: Calcula automaticamente com fator 300
- **Peso Faturável**: Máximo entre peso real e peso cubado
- **Desconto até 30kg**: 50% de desconto (R$ 1,50/kg)
- **Excedente**: Sem desconto (R$ 3,00/kg)

### Exemplo de Cálculo
```
Caixa: 100cm × 100cm × 100cm | Peso Real: 20kg

Peso Cubado: 300kg
Peso Faturável: 300kg (máximo entre 20kg e 300kg)

Primeiros 30kg com desconto: 30kg × R$ 1,50 = R$ 45,00
Excedente sem desconto: 270kg × R$ 3,00 = R$ 810,00
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VALOR TOTAL DO FRETE: R$ 855,00
```

## 📁 Estrutura do Projeto

```
Calculadora_Frete/
│
├─ 📁 src/                           # Código fonte modular
│  ├─ __init__.py                   # Pacote Python
│  ├─ __main__.py                   # 🎯 Ponto de entrada
│  ├─ constants.py                  # 🎨 Constantes e tema
│  ├─ calculator.py                 # 🧮 Lógica de cálculo (pura)
│  └─ gui.py                        # 🖥️ Interface Tkinter
│
├─ 📁 tests/                         # Testes unitários
│  └─ test_calculator.py            # ✓ Testes da lógica
│
├─ 📁 docs/                          # Documentação
│  ├─ README.md                     # Este arquivo
│  ├─ COMO_BUILDAR.md               # Instruções de build
│  ├─ BUILD_INFO.md                 # Info de compilação
│  └─ PROJECT_STRUCTURE.md          # Arquitetura do projeto
│
├─ 📁 build_scripts/                 # Automação
│  └─ build.bat                     # 🔨 Script PyInstaller
│
├─ 📁 dist/                          # 📦 Saída do build
│  └─ Calculadora de Frete.exe      # ✅ Executável final
│
├─ 📁 .venv/                         # Ambiente virtual Python
│
└─ 📄 calcular_frete.py             # Versão monolítica (legacy)
```

## 🚀 Como Usar

### Desenvolvimento Local

#### Pré-requisitos
- Python 3.10+ instalado
- Git (opcional)

#### Instalação

```powershell
# Clone ou extraia o projeto
cd "C:\Users\seu_usuario\Desktop\Calculadora_Frete"

# Crie ambiente virtual (recomendado)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Instale dependências (Tkinter já vem com Python)
pip install pytest
```

#### Executar em Desenvolvimento
```powershell
# Rodar a aplicação
python -m src

# Rodar testes
python tests/test_calculator.py
```

### Distribuição

#### Usar o Executável Pronto
```
dist/Calculadora de Frete.exe
```
Clique 2x para rodar. Não precisa instalar Python!

#### Compilar Novo Executável
```powershell
cd build_scripts
.\build.bat
```

O novo `.exe` será criado em `dist/`.

## 🔧 Tecnologias

| Componente | Tecnologia | Versão |
|-----------|-----------|--------|
| **Linguagem** | Python | 3.14.1 |
| **GUI Desktop** | Tkinter | Built-in |
| **Build** | PyInstaller | 6.17.0 |
| **Testes** | Pytest (nativo) | - |
| **Sistema** | Windows | 10+ |

## 📊 Arquitetura

### Camadas de Separação

```
┌─────────────────────────────────────┐
│   Interface (gui.py)                │  Tkinter UI
├─────────────────────────────────────┤
│   Lógica de Negócio (calculator.py) │  Cálculos puros
├─────────────────────────────────────┤
│   Configuração (constants.py)       │  Temas e constantes
└─────────────────────────────────────┘
```

**Benefícios:**
- Lógica testável sem UI
- Fácil reutilizar em outros projetos
- Simples migrar para web/mobile
- Manutenção simplificada

## ✅ Testes

### Cobertura
```
✓ test_calcular_peso_cubado_azul     - Cálculo de volume
✓ test_calcular_frete_com_desconto   - Frete com desconto
✓ test_calcular_frete_sem_desconto   - Frete sem desconto
✓ test_validar_entrada_valid         - Validação positiva
✓ test_validar_entrada_invalid       - Validação negativa
✓ test_formatar_resultado            - Formatação de output
```

### Executar Testes
```powershell
python tests/test_calculator.py
```

Todos os testes devem passar com:
```
✓ All tests passed!
```

## 🔄 Fluxo de Comunicação Entre Módulos

```
main (__main__.py)
    ↓
GUI (gui.py)
    ├→ constants.py (THEME, window config)
    └→ calculator.py (funções de cálculo)
        └→ constants.py (MULTIPLICADOR, preços)

Tests (test_calculator.py)
    └→ calculator.py
```

## 📋 Constantes Configuráveis

**`src/constants.py`**

```python
# Cálculo de Frete
FATOR_CUBAGEM = 300                 # Fator volume → kg
VALOR_FRETE_POR_KG_CHEIO = 3.00    # R$/kg sem desconto
PERCENTUAL_DESCONTO_KG = 0.50      # 50% de desconto
LIMITE_PESO_DESCONTO = 30.0        # até 30kg com desconto

# Tema
THEME = {
    'bg_main': '#2b2b2b',           # Fundo principal
    'bg_text': '#1e1e1e',           # Fundo de texto
    'fg_text': '#f0f0f0',           # Cor do texto
    'btn_calc': '#00aa00',          # Botão calcular
    'btn_clear': '#ff6600',         # Botão limpar
    'btn_copy': '#0066cc',          # Botão copiar
}

# Janela
WINDOW_WIDTH = 900                  # Largura
WINDOW_HEIGHT = 550                 # Altura
```

## 🎨 Interface

### Layout Principal

```
┌─────────────────────────────────────────────┐
│     Calculadora de Frete                    │
├──────────────┬──────────────────────────────┤
│ Entrada de   │  Resultado                   │
│ Dados        │  ═════════════════════════   │
│              │  Peso cubado:      300 kg    │
│ Comprimento: │  Peso real:        20 kg    │
│ │ 100        │  Peso faturável:   300 kg   │
│              │  ─────────────────────────   │
│ Largura:     │  Até 30kg (c/desc): ...     │
│ │ 100        │  Excedente (s/desc): ...    │
│              │  ─────────────────────────   │
│ Altura:      │  VALOR TOTAL: R$ 855,00    │
│ │ 100        │                              │
│              │                              │
│ Peso Real:   │                              │
│ │ 20         │                              │
├──────────────┴──────────────────────────────┤
│ [Calcular] [Limpar] [Copiar]                │
└──────────────────────────────────────────────┘
```

### Cores
- **Fundo**: Cinza escuro (#2b2b2b)
- **Texto**: Branco (#f0f0f0)
- **Botões**: Verde (calc), Laranja (limpar), Azul (copiar)
- **Resultado**: Fonte fixa Consolas

## 🔄 Funcionalidades

### Calcular
- Captura valores dos 4 campos
- Valida entradas numéricas
- Executa cálculo completo
- Exibe resultado formatado

### Limpar
- Limpa todos os campos
- Reseta resultado
- Coloca foco no primeiro campo

### Copiar
- Copia resultado completo para área de transferência
- Mostra mensagem de sucesso

### Enter
- Pressionar Enter nos campos calcula automaticamente
- Suporta teclado numérico (KP_Enter)

## 🛠️ Troubleshooting

### Erro: "Python não encontrado"
```powershell
# Reinstale Python e marque "Add Python to PATH"
# Ou use:
python --version
```

### Erro ao rodar testes
```powershell
# Certifique-se de estar na pasta raiz:
cd "C:\...\Calculadora_Frete"
python tests/test_calculator.py
```

### O .exe não funciona
```powershell
# Recompile:
.\build_scripts\build.bat

# Se ainda não funcionar, revise build.bat
# ou reinstale PyInstaller:
pip install --upgrade PyInstaller
```

## 📈 Histórico de Desenvolvimento

### v1.0 - Desktop App
- ✅ Interface Tkinter com tema escuro
- ✅ Cálculo com desconto progressivo
- ✅ Estrutura modular (src/)
- ✅ Suite de testes
- ✅ Build automático com PyInstaller
- ✅ Executável Windows distribuível

## 📝 Licença

Este projeto é de uso livre. Sinta-se à vontade para modificar e distribuir.

## 👤 Autor

**Carlo Eduardo**  
Criada: Dezembro 2025  
Projeto: Calcular_Frete

---

## 📞 Suporte

Para dúvidas ou sugestões sobre:
- Modificar cálculos → Edite `src/calculator.py`
- Mudar UI → Edite `src/gui.py`
- Compilar → Use `build_scripts/build.bat`
- Testar → Execute `python tests/test_calculator.py`

**Pronto para usar e expandir!** 🚀
