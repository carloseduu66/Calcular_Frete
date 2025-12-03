# Como Buildar o .exe (Calculadora de Frete)

## Pré-requisitos

1. **Python 3.10+** instalado
   - Baixar em: https://www.python.org/downloads/
   - Ao instalar, marcar "Add Python to PATH"

2. **PyInstaller** instalado
   ```bash
   pip install pyinstaller
   ```

## Método 1: Usando o arquivo build.bat (Recomendado - Windows)

### Passo 1: Abrir PowerShell
- Pressione `Win + X` e selecione "Windows PowerShell" ou "Terminal"
- Navegue até a pasta do projeto:
  ```powershell
  cd "C:\Users\carlo\Desktop\Progamas"
  ```

### Passo 2: Executar o script de build
```powershell
.\build.bat
```

O arquivo `.exe` será criado na pasta `dist/`

---

## Método 2: Buildar manualmente com PyInstaller

### Passo 1: Abrir PowerShell na pasta do projeto
```powershell
cd "C:\Users\carlo\Desktop\Progamas"
```

### Passo 2: Buildar o executável
```powershell
pyinstaller --onefile --windowed calcular_frete.py
```

**Opções explicadas:**
- `--onefile`: Cria um único arquivo `.exe` (mais fácil de distribuir)
- `--windowed`: Remove a janela de console preta
- `calcular_frete.py`: Nome do arquivo Python a converter

### Passo 3: Encontrar o arquivo
O `.exe` estará em: `dist/calcular_frete.exe`

---

## Método 3: Buildar com ícone personalizado

Se tiver um arquivo `icon.ico`:

```powershell
pyinstaller --onefile --windowed --icon=icon.ico calcular_frete.py
```

---

## Distributindo o .exe

### Opção 1: Arquivo único
- Copie apenas `dist/calcular_frete.exe`
- Funciona em qualquer Windows x64

### Opção 2: Com configuração
- Copie `dist/calcular_frete.exe`
- Copie `config.json` (se quiser valores customizados)
- Coloque os 2 arquivos na mesma pasta

---

## Limpando arquivos temporários

Se quiser deletar arquivos de build antigos:

```powershell
Remove-Item -Recurse build/
Remove-Item -Recurse dist/
Remove-Item calcular_frete.spec
```

---

## Solução de Problemas

### "PyInstaller não encontrado"
```powershell
pip install pyinstaller
```

### "Python não encontrado"
- Reinstale Python e marque "Add Python to PATH"
- Ou adicione Python ao PATH manualmente

### O .exe está muito grande (> 100MB)
É normal! Tkinter + Python embutidos deixam o arquivo pesado.

---

## Verificar o build

Para testar se o .exe funciona:
```powershell
.\dist\calcular_frete.exe
```

Se abrir a janela da calculadora = sucesso! ✓
