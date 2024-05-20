from tkinter import *
from PIL import Image, ImageTk
import pygame
import sys

def salir():
    respuesta = messagebox.askquestion("Pregunta", "¿Seguro que desea salir del juego?")
    if respuesta == "yes":
        ventana.destroy()

    
def juego():
    ventana.iconbitmap("logo_usc.ico")
    campo_vacio_1 = usuario_1.get()
    campo_vacio_2 = usuario_2.get()
    if campo_vacio_1 == "" or campo_vacio_2 == "":
        messagebox.showerror("Campo Vacio", "Debes darle nombre a los jugadores.")
    else:
            
        # tamaño de la ventana del juego
        dimension_juego = (800, 600)
        color_juego_fondo = (0, 0, 0)
        screen = pygame.display.set_mode(dimension_juego)

        # titulo del juego
        pygame.display.set_caption("Pin Pon Game USC")

        # bucle principal del juego
        running = True
        while running:
            # Manejar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        # fodo del juego
        screen.fill(color_juego_fondo)  # Azul
        pygame.display.flip() # actualizar la pantalla

        # para salir dando en la x de la ventana
        pygame.quit()
        sys.exit()
    
pygame.init()
ventana = Tk()
ventana.iconbitmap("logo_usc.ico")
ventana.geometry("800x460")
ventana.resizable(False, False)
ventana.title("Pin Pon Game USC")

# imagen del niño jugando pinpon
imagen_original = Image.open("logo_pinpon.jpeg")
imagen_redimensionada = imagen_original.resize((450, 430), Image.LANCZOS)
imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
mi_imagen = Label(ventana, image=imagen_tk)
mi_imagen.place(x=380, y=10)

etiqueta = Label(ventana, text="Pin Pon USC", font=("arial black", 28, 'bold'))
etiqueta.place(x=30, y=10)

# entrada texto para los jugadores
etiqueta_aviso_1 = Label(ventana, text="Jugador 1", font=("arial", 16, 'bold'))
etiqueta_aviso_1.place(x=30, y=90)
usuario_1 = Entry(ventana, justify="center", width=17, font=("arial", 16, "bold"), border=2, fg="black")
usuario_1.place(x=30, y=140)

etiqueta_aviso_2 = Label(ventana, text="Jugador 2", font=("arial", 16, 'bold'))
etiqueta_aviso_2.place(x=30, y=190)
usuario_2 = Entry(ventana, justify="center", width=17, font=("arial", 16, "bold"), border=2, fg="black")
usuario_2.place(x=30, y=240)

# botones
boton_jugar = Button(ventana, text="JUGAR", font=("arial black", 14, 'bold'), width=16, height=1, bg="SpringGreen2", command=juego)
boton_jugar.place(x=30, y=300)

boton_validar = Button(ventana, text="SALIR", font=("arial black", 14, 'bold'), width=16, height=1, bg="#FC8907", command=salir)
boton_validar.place(x=30, y=370)
ventana.mainloop()
