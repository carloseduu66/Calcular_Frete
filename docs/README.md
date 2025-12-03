# Calculadora de Frete - Azul Cargo Express

## 📦 O que é?

Uma aplicação desktop simples e responsiva para calcular fretes com desconto progressivo.

**Versão:** 1.2 (Atualizada: Dezembro 2025)

---

## 🎯 Funcionalidades

- ✅ Interface escura moderna com Tkinter
- ✅ Cálculo automático de peso cubado
- ✅ Desconto progressivo até 30kg
- ✅ Layout responsivo (se expande com a janela)
- ✅ Validação de entrada
- ✅ Botões coloridos e funcionais
- ✅ Resultado bem formatado

---

## 🚀 Como Usar

### Opção 1: Executável (.exe)
1. Baixe `calcular_frete.exe`
2. Clique 2x para abrir
3. Preencha os 4 campos (Comprimento, Largura, Altura, Peso)
4. Clique em "Calcular"

### Opção 2: Código Python
```bash
python calcular_frete.py
```

---

## 📊 Como Funciona o Cálculo

**Fórmula:**
- Peso cubado = (C × L × A) / 100³ / 300
- Peso faturável = MAX(peso cubado, peso real)

**Desconto:**
- Até 30kg: 50% de desconto (R$ 1.50/kg)
- Acima de 30kg: Valor cheio na parte excedente (R$ 3.00/kg)

**Exemplo:**
- Caixa 50×40×30cm, peso real 25kg
- Peso cubado: 20kg
- Peso faturável: 25kg (todo com desconto)
- Valor: 25kg × R$ 1.50 = **R$ 37.50**

---

## ⚙️ Configuração Personalizada

Crie um arquivo `config.json` na mesma pasta do .exe:

```json
{
  "VALOR_FRETE_POR_KG_CHEIO": 3.50,
  "PERCENTUAL_DESCONTO_KG": 0.45,
  "LIMITE_PESO_DESCONTO": 40.0
}
```

---

## 🛠️ Como Buildar o .exe

Veja o arquivo `COMO_BUILDAR.md` para instruções detalhadas.

**TL;DR:**
```powershell
python -m PyInstaller --onefile --windowed calcular_frete.py
```

---

## 📁 Estrutura de Arquivos

```
calcular_frete.py          # Código principal
dist/
  └─ calcular_frete.exe    # Executável (use este!)
config.json                # Configuração (opcional)
COMO_BUILDAR.md           # Instruções de build
README.md                 # Este arquivo
```

---

## 💻 Requisitos

- **Windows 7+** (x64)
- **Nenhuma dependência adicional** (tudo embutido no .exe)

---

## 📝 Notas

- O arquivo `.exe` é grande (~50-100MB) porque inclui Python + Tkinter embutidos
- Funciona offline, não precisa internet
- Pode ser copiado para pendrive e usar em outro PC

---

## 🤝 Suporte

Se encontrar problemas:
1. Verifique se tem Windows x64
2. Tente deletar arquivos de cache do Windows
3. Reinstale o .exe se tiver problemas de permissão

---

**Made with ❤️ para Azul Cargo Express**
