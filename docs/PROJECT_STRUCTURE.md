# Project Structure
```
Calcular_Frete/
├── src/                          # Source code
│   ├── __main__.py              # Entry point (main)
│   ├── constants.py             # Shared constants and theme
│   ├── calculator.py            # Business logic (pure functions)
│   └── gui.py                   # GUI components
│
├── tests/                        # Unit tests
│   └── test_calculator.py       # Tests for calculator module
│
├── docs/                         # Documentation
│   ├── README.md                # User guide
│   ├── COMO_BUILDAR.md          # Build instructions (PT)
│   └── BUILD_INFO.md            # Build information
│
├── build_scripts/                # Build automation
│   └── build.bat                # PyInstaller build script
│
└── .venv/                        # Python virtual environment

## Module Communication Flow

```
__main__.py (entry point)
    ↓
gui.py (FreteCalculatorUI)
    ├→ imports constants.py (THEME, window config)
    └→ imports calculator.py (calculation functions)

calculator.py (business logic)
    └→ imports constants.py (AZUL_WEIGHT_MULTIPLIER, prices)

tests/test_calculator.py (unit tests)
    └→ imports calculator.py (functions to test)
```

## How to Run

### Development
```powershell
# Run directly
python -m src

# Run tests
cd tests
python test_calculator.py
```

### Build for Distribution
```powershell
# Windows batch file
.\build_scripts\build.bat
```

## Module Responsibilities

| Module | Responsibility |
|--------|-----------------|
| `__main__.py` | Application initialization |
| `constants.py` | Shared configuration and theme |
| `calculator.py` | Pure calculation functions (no UI) |
| `gui.py` | Tkinter interface and user interaction |
| `test_calculator.py` | Unit tests for business logic |
