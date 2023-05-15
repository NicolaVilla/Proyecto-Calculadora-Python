import tkinter
#Ventana principal tkinter
ventana = tkinter.Tk()
ventana.geometry("300x300")
#Texto donde se va a mostrar el resultado
text_resultado = tkinter.Text(ventana,height="2",width="16")
text_resultado.grid(columnspan=5)






ventana.mainloop()

