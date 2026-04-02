import customtkinter as ctk
from core.calculos import add, subtract, multiply, divide
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("360x480")
        self.resizable(False, False)
        self._build_ui()
    def _build_ui(self):
        ctk.CTkLabel(self, text="Calculadora", font=("Arial", 22, "bold")).pack(pady=20)
        ctk.CTkLabel(self,text="Número 1").pack()
        self.entry1 = ctk.CTkEntry(self, placeholder_text="Ex: 10")
        self.entry1.pack(pady=5)
        ctk.CTkLabel(self, text="Número 2").pack()
        self.entry2 = ctk.CTkEntry(self, placeholder_text="Ex: 5")
        self.entry2.pack(pady=5)
        ctk.CTkLabel(self, text="Operação").pack(pady=(10, 0))
        self.operacao = ctk.CTkOptionMenu(self, values=["Add","Subtract", "Multiply", "Divide"])
        self.operacao.pack(pady=5)
        ctk.CTkButton(self, text="Calcular", command=self._calcular).pack(pady=20)
        self.result_label = ctk.CTkLabel(self, text="Result will appear here.", font=("Arial", 16, "bold"), text_color="gray")
        self.result_label.pack(pady=10)
    def _calcular(self):
        try:
            n1 = float(self.entry1.get())
            n2 = float(self.entry2.get())
        except ValueError:
            self._mostrar_resultado("Digite Números Validos!", erro = True)
            return
        op = self.operacao.get()
        operacoes = {
            "Add": lambda: add(n1,n2),
            "Subtract": lambda: subtract(n1,n2),
            "Multiply": lambda: multiply(n1,n2),
            "Divide": lambda: divide(n1,n2),
        }   
        resultado = operacoes[op]()
        if isinstance(resultado, str):
            self._mostrar_resultado(f"⚠ {resultado}", erro=True)
        else:
            self._mostrar_resultado(f"= {resultado:.4f}")
    def _mostrar_resultado(self, texto, erro=False):
        cor = "#FF6B6B" if erro else "#4FC3F7"
        self.result_label.configure(text= texto, text_color=cor)