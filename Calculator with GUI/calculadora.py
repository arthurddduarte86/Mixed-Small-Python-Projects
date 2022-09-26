import tkinter as tk


calculation=""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except: 
        clear_field()
        text_result.insert(1.0, "Deu erro")   

def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0, "end")

# parametros da GUI
janela = tk.Tk()
janela.geometry("450x270")
#
text_result = tk.Text(janela, height=2, width=30, font=("Arial", 18))
text_result.grid(columnspan=5)
#botões
btn_1 = tk.Button(janela, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 16))
btn_1.grid(row=2, column=1)
#
btn_2 = tk.Button(janela, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 16))
btn_2.grid(row=2, column=2)
#
btn_3 = tk.Button(janela, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 16))
btn_3.grid(row=2, column=3)
#
btn_4 = tk.Button(janela, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 16))
btn_4.grid(row=3, column=1)
#
btn_5 = tk.Button(janela, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 16))
btn_5.grid(row=3, column=2)
#
btn_6 = tk.Button(janela, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 16))
btn_6.grid(row=3, column=3)
#
btn_7 = tk.Button(janela, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 16))
btn_7.grid(row=4, column=1)
#
btn_8 = tk.Button(janela, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 16))
btn_8.grid(row=4, column=2)
#
btn_9 = tk.Button(janela, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 16))
btn_9.grid(row=4, column=3)
#
btn_0 = tk.Button(janela, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 16))
btn_0.grid(row=5, column=2)
#
btn_plus = tk.Button(janela, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 16))
btn_plus.grid(row=2, column=4)
#
btn_minus = tk.Button(janela, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 16))
btn_minus.grid(row=3, column=4)
#
btn_mul = tk.Button(janela, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 16))
btn_mul.grid(row=4, column=4)
#
btn_div = tk.Button(janela, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 16))
btn_div.grid(row=5, column=4)
#
btn_open = tk.Button(janela, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 16))
btn_open.grid(row=5, column=1)
#
btn_close = tk.Button(janela, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 16))
btn_close.grid(row=5, column=3)
#
btn_CE = tk.Button(janela, text="CE", command=clear_field, width=13, font=("Arial", 16))
btn_CE.grid(row=6, column=1, columnspan=2)
#
btn_equals = tk.Button(janela, text="=", command=evaluate_calculation, width=12, font=("Arial", 16))
btn_equals.grid(row=6, column=3, columnspan=2)




















janela.mainloop()




