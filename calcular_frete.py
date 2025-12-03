"""Calculadora de Frete Azul Cargo Express

Adiciona uma interface gráfica básica (Tkinter) e mantém funções
reutilizáveis para cálculo do frete para teste/import.
"""

def calcular_peso_cubado_azul(comprimento_cm, largura_cm, altura_cm, fator_cubagem=300):
    """Calcula o peso cubado com base nas dimensões em CM."""
    volume_m3 = (comprimento_cm / 100.0) * (largura_cm / 100.0) * (altura_cm / 100.0)
    peso_cubado_kg = volume_m3 * fator_cubagem
    return round(peso_cubado_kg, 2)


# Constantes de negócio
VALOR_FRETE_POR_KG_CHEIO = 3.00
PERCENTUAL_DESCONTO_KG = 0.50  # 50% de desconto
LIMITE_PESO_DESCONTO = 30.0  # kg


def calcular_frete(comprimento_cm, largura_cm, altura_cm, peso_real_kg):
    """Calcula o frete e retorna um dicionário com todos os detalhes.

    Entradas: medidas em cm e peso real em kg.
    Retorna: dict com chaves: peso_cub, peso_faturavel, peso_parte_descontada,
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


def iniciar_interface():
    try:
        import tkinter as tk
        from tkinter import messagebox
    except Exception:
        raise

    root = tk.Tk()
    root.title("Calculadora de Frete - Azul Cargo Express")

    # Flag para indicar se o resultado já foi exibido (evita múltiplas execuções)
    root._result_shown = False

    # Inputs
    labels = ["Comprimento (cm)", "Largura (cm)", "Altura (cm)", "Peso real (kg)"]
    entries = {}

    for i, text in enumerate(labels):
        lbl = tk.Label(root, text=text)
        lbl.grid(row=i, column=0, padx=8, pady=6, sticky="w")
        ent = tk.Entry(root, width=18)
        ent.grid(row=i, column=1, padx=8, pady=6)
        entries[text] = ent

    # Define foco inicial no primeiro campo
    entries[labels[0]].focus_set()

    # Resultado: usar um Text para exibir todo o conteúdo (como versão original)
    result_text = tk.Text(root, width=60, height=12)
    result_text.grid(row=0, column=2, rowspan=6, padx=8, pady=6, sticky="nsew")

    # Guarda o último texto exibido para evitar duplicação acidental
    last_output = ""
    # Guard para agendamento (debounce) e texto pendente
    scheduled = False
    pending_text = None

    def on_calcular(event=None):
        try:
            comprimento = float(entries[labels[0]].get())
            largura = float(entries[labels[1]].get())
            altura = float(entries[labels[2]].get())
            peso_real = float(entries[labels[3]].get())
        except ValueError:
            messagebox.showerror("Entrada inválida", "Digite números válidos. Use ponto (.) como separador decimal.")
            return
        nonlocal last_output
        nonlocal scheduled, pending_text

        resp = calcular_frete(comprimento, largura, altura, peso_real)
        texto = formatar_resultado(resp)

        # Se já mostramos resultado, não reapresenta
        if texto == last_output or getattr(root, "_result_shown", False):
            return

        # Se já agendado, ignora chamadas subsequentes (debounce)
        if scheduled:
            return

        # Marca agendado e guarda texto pendente
        scheduled = True
        pending_text = texto

        # Agenda a inserção para o loop principal (evita reentrância múltipla)
        def do_insert():
            nonlocal scheduled, pending_text, last_output
            # Desabilita o botão imediatamente para evitar reentrância adicional
            btn_calc.config(state="disabled")
            root._result_shown = True

            # Insere o texto pendente na UI
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, pending_text)
            last_output = pending_text

            # limpa estado de agendamento (a flag _result_shown mantém bloqueio até Limpar)
            scheduled = False

        root.after(10, do_insert)

    def on_limpar():
        for e in entries.values():
            e.delete(0, tk.END)
        result_text.delete("1.0", tk.END)
        nonlocal last_output
        last_output = ""
        root._result_shown = False
        btn_calc.config(state="normal")

    btn_calc = tk.Button(root, text="Calcular", command=on_calcular, width=12)
    btn_calc.grid(row=5, column=0, pady=6)

    btn_clear = tk.Button(root, text="Limpar", command=on_limpar, width=12)
    btn_clear.grid(row=5, column=1, pady=6)

    # Permitir que a tecla Enter (Return) dispare o cálculo — inclusive em campos Entry
    root.bind('<Return>', on_calcular)
    root.bind('<KP_Enter>', on_calcular)

    root.mainloop()


if __name__ == "__main__":
    # Abre a interface gráfica
    iniciar_interface()




