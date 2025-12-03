# ✅ Build Concluído com Sucesso!

## 📊 Resumo do Build

- **Data:** Dezembro 3, 2025
- **Versão:** 1.2
- **Arquivo:** `dist/calcular_frete.exe`
- **Tamanho:** 10.95 MB
- **Python:** 3.14.1
- **Status:** ✅ Pronto para uso

---

## 🎯 Como Usar o .exe

### Opção 1: Clicar 2x
Simplesmente abra `dist/calcular_frete.exe` clicando 2x

### Opção 2: Linha de comando
```powershell
.\dist\calcular_frete.exe
```

---

## 📦 Como Distribuir

### Para um PC específico:
```
1. Copie dist/calcular_frete.exe
2. Cole em qualquer pasta do PC destino
3. Clique 2x para executar
```

### Para pendrive (USB):
```
1. Copie dist/calcular_frete.exe
2. Cole no pendrive
3. Use em qualquer Windows (x64) sem instalar nada
```

### Para enviar por email:
```
1. Copie dist/calcular_frete.exe
2. Comprima em ZIP se desejar
3. Envie normalmente
4. Destinatário só precisa clicar 2x
```

---

## 🔄 Como Fazer um Novo Build

### Método 1: Clique no arquivo (Mais fácil)
```
1. Abra a pasta do projeto
2. Clique 2x em build.bat
3. Espere aparecer a mensagem de sucesso
```

### Método 2: PowerShell
```powershell
cd "C:\Users\carlo\Desktop\Progamas"
.\build.bat
```

### Método 3: Manual (Se build.bat não funcionar)
```powershell
cd "C:\Users\carlo\Desktop\Progamas"
python -m PyInstaller --onefile --windowed calcular_frete.py
```

---

## ⚙️ Se Precisar Customizar o .exe

### Adicionar ícone:
1. Coloque um arquivo `icon.ico` na pasta
2. Execute: `python -m PyInstaller --onefile --windowed --icon=icon.ico calcular_frete.py`

### Alterar valores de frete:
Crie `config.json` ao lado do .exe:
```json
{
  "VALOR_FRETE_POR_KG_CHEIO": 3.50,
  "PERCENTUAL_DESCONTO_KG": 0.45,
  "LIMITE_PESO_DESCONTO": 40.0
}
```

---

## ⚠️ Requisitos do PC

- **Sistema Operacional:** Windows 7+ (x64)
- **Memória:** Mínimo 512MB RAM
- **Espaço:** ~50MB para instalar
- **Dependências:** NENHUMA (Python já está embutido!)

---

## 🐛 Solução de Problemas

### "Windows protegeu seu PC"
- Clique em "Informações adicionais"
- Clique em "Executar assim mesmo"

### "Arquivo está corrompido"
- Faça um novo build
- Verifique se calcular_frete.py não foi modificado

### "Abriu uma janela preta e fechou"
- Pode ser um erro de entrada
- Verifique os valores digitados
- Use números com ponto (.) não vírgula (,)

---

## 📝 Histórico de Builds

- **v1.2** (Dez 2025) - Tema escuro fixo, código otimizado, comentários reduzidos
- **v1.1** (Dez 2025) - Interface responsiva, botões coloridos
- **v1.0** (Dez 2025) - Versão inicial

---

**O .exe está pronto para usar! 🎉**
