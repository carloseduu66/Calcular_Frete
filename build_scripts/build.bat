@echo off
REM Build script for Calcular Frete application
REM Creates standalone .exe using PyInstaller

setlocal enabledelayedexpansion

echo.
echo ================================================
echo  Construtor - Calcular Frete
echo ================================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python nao encontrado!
    pause
    exit /b 1
)

echo [OK] Python encontrado
echo.

REM Install/Update dependencies
echo Instalando dependencias...
pip install PyInstaller pillow -q
if errorlevel 1 (
    echo [ERRO] Falha ao instalar dependencias
    pause
    exit /b 1
)

echo [OK] Dependencias instaladas
echo.

REM Clean old builds
echo Limpando builds antigos...
if exist build rmdir /s /q build >nul 2>&1
if exist dist rmdir /s /q dist >nul 2>&1
if exist calcular_frete.spec del calcular_frete.spec >nul 2>&1
echo [OK] Limpeza concluida
echo.

REM Build with PyInstaller
echo Compilando aplicacao...
python -m PyInstaller --onefile --windowed src/__main__.py --name "Calculadora de Frete" -y >nul 2>&1

if errorlevel 1 (
    echo [ERRO] Falha na compilacao!
    pause
    exit /b 1
)

echo [OK] Compilacao concluida!
echo.

REM Show result
if exist "dist\Calculadora de Frete.exe" (
    echo ================================================
    echo [SUCESSO] Aplicacao compilada!
    echo.
    echo Arquivo: dist\Calculadora de Frete.exe
    for %%F in ("dist\Calculadora de Frete.exe") do echo Tamanho: %%~zF bytes
    echo.
    echo Proximos passos:
    echo - Clique 2x em "Calculadora de Frete.exe" para rodar
    echo - Distribuir o arquivo .exe para usuarios
    echo ================================================
) else (
    echo [ERRO] Arquivo .exe nao foi criado!
    pause
    exit /b 1
)

pause
