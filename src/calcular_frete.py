"""Calculadora de Frete Azul Cargo Express

Adiciona uma interface gráfica básica (Tkinter) e mantém funções
reutilizáveis para cálculo do frete para teste/import.
"""

def calcular_peso_cubado_azul(comprimento_cm, largura_cm, altura_cm, fator_cubagem=300):
    """Calcula o peso cubado com base nas dimensões em CM."""
    volume_m3 = (comprimento_cm / 100.0) * (largura_cm / 100.0) * (altura_cm / 100.0)
    peso_cubado_kg = volume_m3 * fator_cubagem
    return round(peso_cubado_kg, 2)


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


def iniciar_interface():
    """Cria e exibe a interface gráfica com Tkinter."""
    import tkinter as tk
    from tkinter import messagebox, ttk

    # ===== Janela Principal =====
    root = tk.Tk()
    root.title("Calculadora de Frete - Azul Cargo Express")
    root.geometry("900x500")
    ttk.Style().theme_use('clam')

    root._result_shown = False
    root.columnconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)

    # ===== Container Principal =====
    main_frame = tk.Frame(root, bg='#2b2b2b')
    main_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=2)
    main_frame.rowconfigure(1, weight=1)

    # ===== Painel de Entrada (Esquerda) =====
    input_frame = tk.LabelFrame(main_frame, text="Entrada de Dados", font=("Arial", 10, "bold"), 
                                 bg='#2b2b2b', fg='#f0f0f0', padx=10, pady=10)
    input_frame.grid(row=0, column=0, rowspan=3, sticky="nsew", padx=(0, 10))
    input_frame.columnconfigure(1, weight=1)
    
    labels = ["Comprimento (cm)", "Largura (cm)", "Altura (cm)", "Peso real (kg)"]
    entries = {}
    for i, text in enumerate(labels):
        tk.Label(input_frame, text=text, bg='#2b2b2b', fg='#f0f0f0').grid(row=i, column=0, padx=5, pady=6, sticky="w")
        ent = tk.Entry(input_frame, width=18, bg='#3a3a3a', fg='#f0f0f0', insertbackground='#f0f0f0')
        ent.grid(row=i, column=1, padx=5, pady=6, sticky="ew")
        entries[text] = ent
    entries[labels[0]].focus_set()

    # ===== Painel de Resultado (Direita) =====
    result_frame = tk.LabelFrame(main_frame, text="Resultado", font=("Arial", 10, "bold"),
                                  bg='#2b2b2b', fg='#f0f0f0', padx=10, pady=10)
    result_frame.grid(row=0, column=1, rowspan=3, sticky="nsew")
    result_frame.columnconfigure(0, weight=1)
    result_frame.rowconfigure(0, weight=1)
    
    scrollbar = tk.Scrollbar(result_frame)
    scrollbar.grid(row=0, column=1, sticky="ns")
    result_text = tk.Text(result_frame, yscrollcommand=scrollbar.set, font=("Consolas", 9),
                          bg='#1e1e1e', fg='#e6e6e6', insertbackground='#e6e6e6')
    result_text.grid(row=0, column=0, sticky="nsew")
    scrollbar.config(command=result_text.yview)

    # ===== Variáveis de Controle =====
    last_output = ""
    scheduled = False
    pending_text = None

    def on_calcular(event=None):
        """Calcula o frete com valores dos campos."""
        try:
            comp, larg, alt, peso = [float(entries[labels[i]].get()) for i in range(4)]
        except ValueError:
            messagebox.showerror("Entrada inválida", "Digite números válidos. Use ponto (.) como separador decimal.")
            return
        nonlocal last_output, scheduled, pending_text
        
        # Evita duplicação e debounce
        texto = formatar_resultado(calcular_frete(comp, larg, alt, peso))
        if texto == last_output or getattr(root, "_result_shown", False) or scheduled:
            return
        
        scheduled = True
        pending_text = texto
        def do_insert():
            nonlocal scheduled, pending_text, last_output
            btn_calc.config(state="disabled")
            root._result_shown = True
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, pending_text)
            last_output = pending_text
            scheduled = False
        root.after(10, do_insert)

    def on_limpar():
        """Limpa todos os campos e resultado."""
        for e in entries.values():
            e.delete(0, tk.END)
        result_text.delete("1.0", tk.END)
        nonlocal last_output
        last_output = ""
        root._result_shown = False
        btn_calc.config(state="normal")

    # ===== Painel de Botões =====
    btn_frame = tk.Frame(main_frame, bg='#2b2b2b')
    btn_frame.grid(row=3, column=0, columnspan=2, sticky="ew", pady=15)
    btn_frame.columnconfigure((0, 1, 2), weight=1)

    btn_style = {"width": 15, "font": ("Arial", 11, "bold"), "relief": tk.RAISED, "bd": 2, "cursor": "hand2"}
    
    btn_calc = tk.Button(btn_frame, text="Calcular", command=on_calcular, bg='#00aa00', fg='#ffffff',
                         activebackground='#00dd00', activeforeground='#ffffff', **btn_style)
    btn_calc.grid(row=0, column=0, padx=8)

    tk.Button(btn_frame, text="Limpar", command=on_limpar, bg='#ff6600', fg='#ffffff',
              activebackground='#ff8844', activeforeground='#ffffff', **btn_style).grid(row=0, column=1, padx=8)
    
    tk.Button(btn_frame, text="Exportar", bg='#0066cc', fg='#ffffff',
              activebackground='#0088ff', activeforeground='#ffffff', **btn_style).grid(row=0, column=2, padx=8)

    # Permite Enter para calcular
    root.bind('<Return>', on_calcular)
    root.bind('<KP_Enter>', on_calcular)

    root.mainloop()


if __name__ == "__main__":
    iniciar_interface()




