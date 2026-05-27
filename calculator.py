import customtkinter as ctk

ctk.set_appearance_mode("System")  

janela = ctk.CTk()

janela.geometry("400x470") 
janela.title("Calculator")
janela.iconbitmap("icon.ico")
janela.resizable(False, False)


janela.grid_rowconfigure(0, weight=0)
janela.grid_rowconfigure(1, weight=1)
janela.grid_columnconfigure(0, weight=1)

expressao = ""

def cliques(caractere):
    global expressao
    expressao = expressao + str(caractere)
    label_Visor.configure(text=expressao)

def limpa_tudo():
    global expressao
    expressao = ""
    label_Visor.configure(text="0")

def apagar_ultimo():
    global expressao
    expressao = expressao[:-1]   

    if expressao == "":
        label_Visor.configure(text="0")
    else:
        label_Visor.configure(text=expressao) 

def calcular():
    global expressao
    try:
        resultado = eval(expressao)
        label_Visor.configure(text=str(resultado))
        expressao = str(resultado)
    except:
        label_Visor.configure(text="Erro")
        expressao = ""

frame_visor = ctk.CTkFrame(janela, width=400, height=100, fg_color="#000000", corner_radius=0)
frame_visor.grid(row=0, column=0, sticky="ew")
frame_visor.grid_propagate(False) 

frame_but = ctk.CTkFrame(janela, width=400, height=375, fg_color="#000000", corner_radius=0)
frame_but.grid(row=1, column=0, sticky="nsew")
frame_but.grid_propagate(False)

label_Visor = ctk.CTkLabel(
    frame_visor, 
    text="0", 
    font=("Arial", 42, "bold"),  
    text_color="#ffffff",        
    fg_color="transparent"
)
label_Visor.pack(side="right", padx=20, fill="y")

b_apaga = ctk.CTkButton(frame_but, font=("Arial", 20, "bold"), command=apagar_ultimo, text="C", height=75, width=100, fg_color="#808080")
b_apaga.place(x=0, y=0) 

b_apagaTudo = ctk.CTkButton(frame_but, font=("Arial", 20, "bold"), command=limpa_tudo, text="AC", height=75, width=100, fg_color="#808080")
b_apagaTudo.place(x=100, y=0)

b_porcent = ctk.CTkButton(frame_but, font=("Arial", 20, "bold"), command=lambda: cliques("/100"), text="%", height=75, width=100, fg_color="#808080")
b_porcent.place(x=200, y=0)

b_div = ctk.CTkButton(frame_but, font=("Arial", 20, "bold"), command=lambda: cliques("/"), text="/", height=75, width=100, fg_color="#ff7d10")
b_div.place(x=300, y=0)

b_7 = ctk.CTkButton(frame_but, font=("Arial", 20, "bold"), command=lambda: cliques("7"), text="7", height=75, width=100, fg_color="#000000")
b_7.place(x=0, y=75) 

b_8 = ctk.CTkButton(frame_but, font=("Arial", 20, "bold"), command=lambda: cliques("8"), text="8", height=75, width=100, fg_color="#000000")
b_8.place(x=100, y=75)

b_9 = ctk.CTkButton(frame_but, font=("Arial", 20, "bold"), command=lambda: cliques("9"), text="9", height=75, width=100, fg_color="#000000")
b_9.place(x=200, y=75)

b_mult = ctk.CTkButton(frame_but, font=("Arial", 20, "bold"), command=lambda: cliques("*"), text="*", height=75, width=100, fg_color="#ff7d10")
b_mult.place(x=300, y=75)

b_4 = ctk.CTkButton(frame_but, font=("Arial", 20, "bold"), command=lambda: cliques("4"), text="4", height=75, width=100, fg_color="#000000")
b_4.place(x=0, y=150) 

b_5 = ctk.CTkButton(frame_but, font=("Arial", 20, "bold"), command=lambda: cliques("5"), text="5", height=75, width=100, fg_color="#000000")
b_5.place(x=100, y=150)

b_6 = ctk.CTkButton(frame_but, font=("Arial", 20, "bold"), command=lambda: cliques("6"), text="6", height=75, width=100, fg_color="#000000")
b_6.place(x=200, y=150)

b_sub = ctk.CTkButton(frame_but, font=("Arial", 20, "bold"), command=lambda: cliques("-"), text="-", height=75, width=100, fg_color="#ff7d10")
b_sub.place(x=300, y=150)

b_1 = ctk.CTkButton(frame_but, font=("Arial", 20, "bold"), command=lambda: cliques("1"), text="1", height=75, width=100, fg_color="#000000")
b_1.place(x=0, y=225) 

b_2 = ctk.CTkButton(frame_but, font=("Arial", 20, "bold"), command=lambda: cliques("2"), text="2", height=75, width=100, fg_color="#000000")
b_2.place(x=100, y=225)

b_3 = ctk.CTkButton(frame_but, font=("Arial", 20, "bold"), command=lambda: cliques("3"), text="3", height=75, width=100, fg_color="#000000")
b_3.place(x=200, y=225)

b_plus = ctk.CTkButton(frame_but, font=("Arial", 20, "bold"), command=lambda: cliques("+"), text="+", height=75, width=100, fg_color="#ff7d10")
b_plus.place(x=300, y=225)

b_0 = ctk.CTkButton(frame_but, font=("Arial", 20, "bold"), command=lambda: cliques("0"), text="0", height=75, width=100, fg_color="#000000")
b_0.place(x=0, y=300)

b_quadrado = ctk.CTkButton(frame_but, font=("Arial", 20, "bold"), command=lambda: cliques("**2"), text="x²", height=75, width=100, fg_color="#000000")
b_quadrado.place(x=100, y=300)

b_ponto = ctk.CTkButton(frame_but, font=("Arial", 20, "bold"), command=lambda: cliques("."), text=".", height=75, width=100, fg_color="#000000")
b_ponto.place(x=200, y=300)

b_igual = ctk.CTkButton(frame_but, font=("Arial", 20, "bold"), command=calcular, text="=", height=75, width=100, fg_color="#ff7d10")
b_igual.place(x=300, y=300)

janela.mainloop()