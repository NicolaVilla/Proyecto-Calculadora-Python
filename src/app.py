import tkinter
#Ventana principal tkinter
ventana = tkinter.Tk()
ventana.geometry("300x300")
#Texto donde se va a mostrar el resultado
text_resultado = tkinter.Text(ventana,height="2",width="16")
text_resultado.grid(columnspan=5)

resultado = ""
def agregar_digito(digito):
    global resultado
    resultado += str(digito)
    text_resultado.delete(1.0,"end")
    text_resultado.insert(1.0,resultado)

def evaluar_resultado():
    global resultado
    try:
        resultado = str(eval(resultado))
        text_resultado.delete(1.0,"end")
        text_resultado.insert(1.0,resultado)
    except:
        limpiar_texto()
        text_resultado.insert(1.0,"Error")

def limpiar_texto():
    global resultado
    resultado=""
    text_resultado.delete(1.0,"end")
    text_resultado.insert(1.0,resultado)

#botones fila 1
btn_1 = tkinter.Button(ventana,text="1",command=lambda: agregar_digito(1))
btn_1.grid(row=1,column=0)
btn_2 = tkinter.Button(ventana,text="2",command=lambda: agregar_digito(2))
btn_2.grid(row=1,column=1)
btn_3 = tkinter.Button(ventana,text="3",command=lambda: agregar_digito(3))
btn_3.grid(row=1,column=2)

#botones fila 2
btn_4 = tkinter.Button(ventana,text="4",command=lambda: agregar_digito(4))
btn_4.grid(row=2,column=0)
btn_5 = tkinter.Button(ventana,text="5",command=lambda: agregar_digito(5))
btn_5.grid(row=2,column=1)
btn_6 = tkinter.Button(ventana,text="6",command=lambda: agregar_digito(6))
btn_6.grid(row=2,column=2)

#botones fila 3
btn_7 = tkinter.Button(ventana,text="7",command=lambda: agregar_digito(7))
btn_7.grid(row=3,column=0)
btn_8 = tkinter.Button(ventana,text="8",command=lambda: agregar_digito(8))
btn_8.grid(row=3,column=1)
btn_9 = tkinter.Button(ventana,text="9",command=lambda: agregar_digito(9))
btn_9.grid(row=3,column=2)

#botones fila 4
btn_abrir = tkinter.Button(ventana,text="(",command=lambda: agregar_digito("("))
btn_abrir.grid(row=4,column=0)
btn_0 = tkinter.Button(ventana,text="0",command=lambda: agregar_digito(0))
btn_0.grid(row=4,column=1)
btn_cerrar = tkinter.Button(ventana,text=")",command=lambda: agregar_digito(")"))
btn_cerrar.grid(row=4,column=2)

#botones operaciones numericas
btn_mas = tkinter.Button(ventana,text="+",command=lambda: agregar_digito("+"))
btn_mas.grid(row=1,column=3)
btn_menos = tkinter.Button(ventana,text="-",command=lambda: agregar_digito("-"))
btn_menos.grid(row=2,column=3)
btn_por = tkinter.Button(ventana,text="*",command=lambda: agregar_digito("*"))
btn_por.grid(row=3,column=3)
btn_div = tkinter.Button(ventana,text="/",command=lambda: agregar_digito("/"))
btn_div.grid(row=4,column=3)

#botones AC y igual
btn_AC = tkinter.Button(ventana,text="AC",command=limpiar_texto)
btn_AC.grid(row=5,column=0,columnspan=2)
btn_igual = tkinter.Button(ventana,text="=",command=evaluar_resultado)
btn_igual.grid(row=5,column=2,columnspan=3)
ventana.mainloop()

