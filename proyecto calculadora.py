##################interfaz

import tkinter as tk
ventana= tk.Tk()

ventana.title("calculadora")
ventana.geometry("300x450")
ventana.configure(bg="gray21")
ventana.resizable(False,False)

###pantalla:

valores= tk.StringVar()
 
pantalla = tk.Label(ventana, textvariable=valores, font=("Impact", 15,), bg="white", anchor="e")
pantalla.place(x=1, y=20, width=300, height=60)


#######:funciones:

def agg(valor):
    actual = valores.get()
    valores.set(actual + valor)

def borrar():
    valores.set("")

def calcular():
    try:
        valor=valores.get()
        if "/0" in valor:
           valores.set("No es posible divir entre 0")
        else:
            result= float(eval(valor))
            valores.set(result)
    except:
        valores.set("ERROR")

def raiz():
    try:
        from math import sqrt
        valor= int(valores.get())
        res_raiz=sqrt(valor)
        valores.set(str(res_raiz))
    except:
        valores.set("ERROR")

def abrir():
    ventana.geometry("950x450")


######funciones distancias:

panx= tk.Label(ventana, text="Valores de X:", font=("Impact",10), bg="white", anchor="e")
panx.place(x=350, y=103, width=80, height=30)
x1=tk.Entry(ventana)
x1.place(x=350,y=130)

x2=tk.Entry(ventana)
x2.place(x=350,y=160)

pany= tk.Label(ventana, text="Valores de Y:", font=("Impact",10), bg="white", anchor="e")
pany.place(x=350, y=190, width=80, height=30)

y1=tk.Entry(ventana)
y1.place(x=350,y=220)

y2=tk.Entry(ventana)
y2.place(x=350,y=250)


def dis_manh():
    xa=int(x1.get())
    xb=int(x2.get())
    dx=abs(xa-xb)
    ya=int(y1.get())
    yb=int(y2.get())
    dy=abs(ya-yb)
    dmanh=dx+dy
    resultado_dismanh.config(text=str(dmanh))


def dis_euc():
    from math import sqrt
    xa=int(x1.get())
    xb=int(x2.get())
    dx=abs(xa-xb)
    px= abs(dx**2)
    ya=int(y1.get())
    yb=int(y2.get())
    dy=abs(ya-yb)
    py=abs(dy**2)
    deuc=sqrt(px+py)
    resultado_dismanh.config(text=str(deuc))

resultado_dismanh= tk.Label(ventana, text="resultado: ", font=("Impact",12), bg="white", anchor="w")
resultado_dismanh.place(x=350, y=300, width=150, height=50)

def borrardis():
    resultado_dismanh.config(text="resultado: ")


borr = tk.Button(ventana, text="borrar",font=("Impact", 16), bg="red", command=lambda: borrardis())
borr.place(x=350, y=360, width=100, height=30)


#######grafica
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
### Frame para la gráfica
ancho_px = 400
alto_px = 300

frame_grafica = tk.Frame(ventana, width=ancho_px, height=alto_px, bg="white")
frame_grafica.place(x=530, y=110)
### Función para graficar
def graficar():
    try:
        xa = float(x1.get())
        ya = float(y1.get())
# Limpiar gráfica anterior
        for widget in frame_grafica.winfo_children():
            widget.destroy()
# Convertir tamaño del frame de píxeles a pulgadas (100 dpi por defecto)
        dpi = 100
        ancho_pulg = ancho_px / dpi
        alto_pulg = alto_px / dpi
 # Crear figura con tamaño ajustado
        fig = plt.figure(figsize=(ancho_pulg, alto_pulg), dpi=dpi)
        plt.plot([0, xa], [0, ya], marker='o')
        plt.title("Punto ingresado")
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
# Mostrar figura en Frame
        canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
        canvas.draw()
        canvas.get_tk_widget().place(x=0, y=0, width=ancho_px, height=alto_px)

    except ValueError:
        print("Ingresa solo números.")







    

##numeros:
bot1 = tk.Button(ventana, text="1",font=("Impact", 16), bg="light gray",command=lambda: agg("1"))
bot1.place(x=50, y=100, width=50, height=50)

bot2 = tk.Button(ventana, text="2", font=("Impact", 16), bg="light gray",command=lambda: agg("2"))
bot2.place(x=100, y=100, width=50, height=50)

bot3 = tk.Button(ventana, text="3", font=("Impact", 16), bg="light gray",command=lambda: agg("3"))
bot3.place(x=150, y=100, width=50, height=50)

bot4 = tk.Button(ventana, text="4", font=("Impact", 16), bg="light gray",command=lambda: agg("4"))
bot4.place(x=50, y=150, width=50, height=50)

bot5 = tk.Button(ventana, text="5", font=("Impact", 16), bg="light gray",command=lambda: agg("5"))
bot5.place(x=100, y=150, width=50, height=50)

bot6 = tk.Button(ventana, text="6", font=("Impact", 16), bg="light gray",command=lambda: agg("6"))
bot6.place(x=150, y=150, width=50, height=50)

bot7 = tk.Button(ventana, text="7", font=("Impact", 16), bg="light gray",command=lambda: agg("7"))
bot7.place(x=50, y=200, width=50, height=50)

bot8 = tk.Button(ventana, text="8", font=("Impact", 16), bg="light gray",command=lambda: agg("8"))
bot8.place(x=100, y=200, width=50, height=50)

bot9 = tk.Button(ventana, text="9", font=("Impact", 16), bg="light gray",command=lambda: agg("9"))
bot9.place(x=150, y=200, width=50, height=50)

bot0 = tk.Button(ventana, text="0", font=("Impact", 16), bg="light gray",command=lambda: agg("0"))
bot0.place(x=100, y=250, width=50, height=50)



##signos:
botsum = tk.Button(ventana, text="+", font=("Impact", 16), bg="steel blue", command=lambda: agg("+"))
botsum.place(x=200, y=100, width=50, height=50)

botrest = tk.Button(ventana, text="-", font=("Impact", 16), bg="steel blue",command=lambda: agg("-"))
botrest.place(x=200, y=150, width=50, height=50)

botmulp = tk.Button(ventana, text="x", font=("Impact", 16), bg="steel blue",command=lambda: agg("*"))
botmulp.place(x=200, y=200, width=50, height=50)

botdiv = tk.Button(ventana, text="/", font=("Impact", 16), bg="steel blue",command=lambda: agg("/"))
botdiv.place(x=50, y=250, width=50, height=50)

botraiz = tk.Button(ventana, text="√", font=("Impact", 16), bg="steel blue",command=lambda: raiz())
botraiz.place(x=150, y=250, width=50, height=50)

botpot = tk.Button(ventana, text="^", font=("Impact", 16), bg="steel blue",command=lambda: agg("**"))
botpot.place(x=200, y=250, width=50, height=50)

bot_igual = tk.Button(ventana, text="=", font=("Impact", 16), bg="medium sea green",command=lambda: calcular())
bot_igual.place(x=200, y=300, width=50, height=50)

bot_c = tk.Button(ventana, text="C", font=("Impact", 16), bg="red", command=lambda: borrar())
bot_c.place(x=50, y=300, width=50, height=50)


##extencion

abrir_ext= tk.Button(ventana, text="EXTENCION", font=("Impact", 16), bg="steel blue", command=abrir)
abrir_ext.place(x=100, y=300, width=100, height=50)


dic_euc= tk.Button(ventana, text="Distancia Euciliana", font=("Impact", 10), bg="medium sea green",command=lambda: dis_euc())
dic_euc.place(x=350, y=50, width=150, height=50)

dic_man= tk.Button(ventana, text="Distancia Manhattan", font=("Impact", 10), bg="medium sea green", command=dis_manh)
dic_man.place(x=550, y=50, width=150, height=50)

graf= tk.Button(ventana, text="Graficar", font=("Impact", 10), bg="medium sea green", command=lambda: graficar())
graf.place(x=750, y=50, width=150, height=50)




ventana.mainloop()





