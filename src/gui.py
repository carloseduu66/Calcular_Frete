# GUI components and interface
# Module responsible for UI rendering and interaction

import tkinter as tk
from tkinter import messagebox
from src.constants import THEME, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT
from src.calculator import (
    calcular_peso_cubado_azul,
    calcular_frete,
    validar_entrada,
    formatar_resultado
)


class FreteCalculatorUI:
    """Main GUI application for freight calculation."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Frete - Azul Cargo Express")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.minsize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)
        self.root.configure(bg=THEME['bg_main'])
        
        self.last_output = ""
        self.scheduled = False
        
        self.setup_ui()
        self.setup_bindings()
        self.apply_theme()
    
    def setup_ui(self):
        """Create and layout all UI elements."""
        # Configure grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        
        # Main container
        main_frame = tk.Frame(self.root, bg=THEME['bg_main'])
        main_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=2)
        main_frame.rowconfigure(1, weight=1)
        
        # ===== INPUT FRAME (LEFT) =====
        input_frame = tk.LabelFrame(
            main_frame,
            text="Entrada de Dados",
            font=THEME['font_normal'],
            bg=THEME['bg_main'],
            fg=THEME['fg_text'],
            padx=10,
            pady=10
        )
        input_frame.grid(row=0, column=0, rowspan=3, sticky="nsew", padx=(0, 10))
        input_frame.columnconfigure(1, weight=1)
        
        labels_text = ["Comprimento (cm)", "Largura (cm)", "Altura (cm)", "Peso real (kg)"]
        self.entries = {}
        
        for i, text in enumerate(labels_text):
            tk.Label(
                input_frame,
                text=text,
                bg=THEME['bg_main'],
                fg=THEME['fg_text'],
                font=THEME['font_normal']
            ).grid(row=i, column=0, padx=5, pady=6, sticky="w")
            
            entry = tk.Entry(
                input_frame,
                width=18,
                bg=THEME['bg_text'],
                fg=THEME['fg_text'],
                font=THEME['font_normal'],
                insertbackground=THEME['fg_text']
            )
            entry.grid(row=i, column=1, padx=5, pady=6, sticky="ew")
            self.entries[text] = entry
        
        self.entries[labels_text[0]].focus_set()
        
        # ===== RESULT FRAME (RIGHT) =====
        result_frame = tk.LabelFrame(
            main_frame,
            text="Resultado",
            font=THEME['font_normal'],
            bg=THEME['bg_main'],
            fg=THEME['fg_text'],
            padx=10,
            pady=10
        )
        result_frame.grid(row=0, column=1, rowspan=3, sticky="nsew")
        result_frame.columnconfigure(0, weight=1)
        result_frame.rowconfigure(0, weight=1)
        
        # Text widget with scrollbar
        scrollbar = tk.Scrollbar(result_frame)
        scrollbar.grid(row=0, column=1, sticky="ns")
        
        self.result_text = tk.Text(
            result_frame,
            yscrollcommand=scrollbar.set,
            font=("Consolas", 9),
            bg=THEME['bg_text'],
            fg='#e6e6e6',
            insertbackground='#e6e6e6'
        )
        self.result_text.grid(row=0, column=0, sticky="nsew")
        scrollbar.config(command=self.result_text.yview)
        
        # ===== BUTTON FRAME =====
        btn_frame = tk.Frame(main_frame, bg=THEME['bg_main'])
        btn_frame.grid(row=3, column=0, columnspan=2, sticky="ew", pady=15)
        btn_frame.columnconfigure((0, 1, 2), weight=1)
        
        btn_style = {
            "width": 15,
            "font": THEME['font_normal'],
            "relief": tk.RAISED,
            "bd": 2,
            "cursor": "hand2"
        }
        
        self.btn_calc = tk.Button(
            btn_frame,
            text="Calcular",
            command=self.on_calcular,
            bg=THEME['btn_calc'],
            fg='#ffffff',
            activebackground='#00dd00',
            activeforeground='#ffffff',
            **btn_style
        )
        self.btn_calc.grid(row=0, column=0, padx=8)
        
        tk.Button(
            btn_frame,
            text="Limpar",
            command=self.on_limpar,
            bg=THEME['btn_clear'],
            fg='#ffffff',
            activebackground='#ff8844',
            activeforeground='#ffffff',
            **btn_style
        ).grid(row=0, column=1, padx=8)
        
        tk.Button(
            btn_frame,
            text="Copiar",
            command=self.on_copiar,
            bg=THEME['btn_copy'],
            fg='#ffffff',
            activebackground='#0088ff',
            activeforeground='#ffffff',
            **btn_style
        ).grid(row=0, column=2, padx=8)
    
    def setup_bindings(self):
        """Setup keyboard bindings."""
        for entry in self.entries.values():
            entry.bind('<Return>', lambda e: self.on_calcular())
            entry.bind('<KP_Enter>', lambda e: self.on_calcular())
            entry.bind('<KeyRelease>', lambda e: self.schedule_calculation())
    
    def schedule_calculation(self):
        """Debounce calculation on input change."""
        if self.scheduled:
            return
        self.scheduled = True
        self.root.after(100, self.on_calcular_silent)
    
    def on_calcular(self):
        """Handle calculate button press."""
        self.scheduled = False
        self.do_calculate()
    
    def on_calcular_silent(self):
        """Silent calculation for live updates."""
        self.scheduled = False
        try:
            self.do_calculate()
        except:
            pass
    
    def do_calculate(self):
        """Perform the actual calculation."""
        try:
            comp = float(self.entries["Comprimento (cm)"].get())
            larg = float(self.entries["Largura (cm)"].get())
            alt = float(self.entries["Altura (cm)"].get())
            peso = float(self.entries["Peso real (kg)"].get())
        except ValueError:
            self.result_text.delete("1.0", tk.END)
            return
        
        resultado = calcular_frete(comp, larg, alt, peso)
        texto = formatar_resultado(resultado)
        
        if texto != self.last_output:
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, texto)
            self.last_output = texto
    
    def on_limpar(self):
        """Clear all inputs and results."""
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.result_text.delete("1.0", tk.END)
        self.last_output = ""
        self.entries["Comprimento (cm)"].focus_set()
    
    def on_copiar(self):
        """Copy result to clipboard."""
        if self.last_output:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.last_output)
            messagebox.showinfo("Sucesso", "Resultado copiado para área de transferência!")
        else:
            messagebox.showwarning("Aviso", "Calcule um valor primeiro")
    
    def apply_theme(self):
        """Apply dark theme to the application."""
        self.root.configure(bg=THEME['bg_main'])
