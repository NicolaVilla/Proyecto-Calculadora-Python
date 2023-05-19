
import customtkinter
#Ventana principal tkinter
ventana = customtkinter.CTk()
ventana.geometry("600x250")
ventana.title("Calculadora")
#Texto donde se va a mostrar el resultado
text_resultado = customtkinter.CTkEntry(ventana,height=2,width=300,)
text_resultado.grid(row=0,column=0,columnspan=4,sticky="nsew")
#Variables de layout
padding_x=5
padding_y=5





resultado = ""
def agregar_digito(digito):
    global resultado
    resultado += str(digito)
    text_resultado.delete(0,"end")
    text_resultado.insert(0,resultado)

def evaluar_resultado():
    global resultado
    try:
        resultado = str(eval(resultado))
        text_resultado.delete(0,"end")
        text_resultado.insert(0,resultado)
    except:
        limpiar_texto()
        text_resultado.insert(0,"Error")

def limpiar_texto():
    global resultado
    resultado=""
    text_resultado.delete(0,"end")
    text_resultado.insert(0,resultado)

#botones fila 1
btn_1 = customtkinter.CTkButton(ventana,text="1",command=lambda: agregar_digito(1))
btn_1.grid(row=1,column=0, padx=padding_x, pady=padding_y, sticky="ew")
btn_2 = customtkinter.CTkButton(ventana,text="2",command=lambda: agregar_digito(2))
btn_2.grid(row=1,column=1, padx=padding_x, pady=padding_y, sticky="ew")
btn_3 = customtkinter.CTkButton(ventana,text="3",command=lambda: agregar_digito(3))
btn_3.grid(row=1,column=2, padx=padding_x, pady=padding_y, sticky="ew")

#botones fila 2
btn_4 = customtkinter.CTkButton(ventana,text="4",command=lambda: agregar_digito(4))
btn_4.grid(row=2,column=0, padx=padding_x, pady=padding_y, sticky="ew")
btn_5 = customtkinter.CTkButton(ventana,text="5",command=lambda: agregar_digito(5))
btn_5.grid(row=2,column=1, padx=padding_x, pady=padding_y, sticky="ew")
btn_6 = customtkinter.CTkButton(ventana,text="6",command=lambda: agregar_digito(6))
btn_6.grid(row=2,column=2, padx=padding_x, pady=padding_y, sticky="ew")

#botones fila 3
btn_7 = customtkinter.CTkButton(ventana,text="7",command=lambda: agregar_digito(7))
btn_7.grid(row=3,column=0, padx=padding_x, pady=padding_y, sticky="ew")
btn_8 = customtkinter.CTkButton(ventana,text="8",command=lambda: agregar_digito(8))
btn_8.grid(row=3,column=1, padx=padding_x, pady=padding_y, sticky="ew")
btn_9 = customtkinter.CTkButton(ventana,text="9",command=lambda: agregar_digito(9))
btn_9.grid(row=3,column=2, padx=padding_x, pady=padding_y, sticky="ew")

#botones fila 4
btn_abrir = customtkinter.CTkButton(ventana,text="(",command=lambda: agregar_digito("("))
btn_abrir.grid(row=4,column=0, padx=padding_x, pady=padding_y, sticky="ew")
btn_0 = customtkinter.CTkButton(ventana,text="0",command=lambda: agregar_digito(0))
btn_0.grid(row=4,column=1, padx=padding_x, pady=padding_y, sticky="ew")
btn_cerrar = customtkinter.CTkButton(ventana,text=")",command=lambda: agregar_digito(")"))
btn_cerrar.grid(row=4,column=2, padx=padding_x, pady=padding_y, sticky="ew")

#botones operaciones numericas
btn_mas = customtkinter.CTkButton(ventana,text="+",command=lambda: agregar_digito("+"))
btn_mas.grid(row=1,column=3, padx=padding_x, pady=padding_y, sticky="ew")
btn_menos = customtkinter.CTkButton(ventana,text="-",command=lambda: agregar_digito("-"))
btn_menos.grid(row=2,column=3, padx=padding_x, pady=padding_y, sticky="ew")
btn_por = customtkinter.CTkButton(ventana,text="*",command=lambda: agregar_digito("*"))
btn_por.grid(row=3,column=3, padx=padding_x, pady=padding_y, sticky="ew")
btn_div = customtkinter.CTkButton(ventana,text="/",command=lambda: agregar_digito("/"))
btn_div.grid(row=4,column=3, padx=padding_x, pady=padding_y, sticky="ew")

#botones AC y igual
btn_AC = customtkinter.CTkButton(ventana,text="AC",command=limpiar_texto)
btn_AC.grid(row=5,column=0,columnspan=2,sticky="ew", padx=padding_x, pady=padding_y)
btn_igual = customtkinter.CTkButton(ventana,text="=",command=evaluar_resultado)
btn_igual.grid(row=5,column=2,columnspan=2,sticky="ew", padx=padding_x, pady=padding_y)
ventana.mainloop()

