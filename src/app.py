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




ventana.mainloop()

