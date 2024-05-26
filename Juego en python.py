from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
import sys

# para cambiar en ajustes el idioma
def cambiar_idioma(idioma):
    global boton_jugar_solo, boton_jugar, boton_hard, boton_validar, ventana
    if idioma == "Español":
        etiqueta_aviso_1.config(text="JUGADOR A")
        etiqueta_aviso_2.config(text="JUGADOR B")
        boton_jugar_solo.config(text="JUGAR SOLO")
        boton_jugar.config(text="A VS B")
        boton_hard.config(text="HARDCORE")
        boton_validar.config(text="SALIR")
        ventana.title("Pin Pon Game USC")
    elif idioma == "English":
        etiqueta_aviso_1.config(text="PLAYER A")
        etiqueta_aviso_2.config(text="PLAYER B")
        boton_jugar_solo.config(text="ONLY PLAYER")
        boton_jugar.config(text="A VS B")
        boton_hard.config(text="HARDCORE")
        boton_validar.config(text="EXIT")
        ventana.title("Pin Pon Game USC")
    elif idioma == "Русский":
        etiqueta_aviso_1.config(text="ИГРОК А")
        etiqueta_aviso_2.config(text="ИГРОК Б")
        boton_jugar_solo.config(text="ИГРАТЬ ОДИН")
        boton_jugar.config(text="А ПРОТИВ Б")
        boton_hard.config(text="СЛОЖНО")
        boton_validar.config(text="ВЫХОД")
        ventana.title("Игра в пинг-понг")
    elif idioma == "Italiano":
        etiqueta_aviso_1.config(text="GIOCATORE A")
        etiqueta_aviso_2.config(text="GIOCATORE B")
        boton_jugar_solo.config(text="GIOCA SOLO")
        boton_jugar.config(text="A VS B")
        boton_hard.config(text="DIFFICILE")
        boton_validar.config(text="ESCI")
        ventana.title("Gioco del Ping Pong")
    elif idioma == "Portugués":
        etiqueta_aviso_1.config(text="JOGADOR A")
        etiqueta_aviso_2.config(text="JOGADOR B")
        boton_jugar_solo.config(text="JOGAR SOZINHO")
        boton_jugar.config(text="A VS B")
        boton_hard.config(text="DIFÍCIL")
        boton_validar.config(text="SAIR")
        ventana.title("Jogo de Ping Pong")
    elif idioma == "українська":
        etiqueta_aviso_1.config(text="ГРАВЕЦЬ А")
        etiqueta_aviso_2.config(text="ГРАВЕЦЬ Б")
        boton_jugar_solo.config(text="ГРАТИ САМ")
        boton_jugar.config(text="А ПРОТИ Б")
        boton_hard.config(text="СКЛАДНО")
        boton_validar.config(text="ВИХІД")
        ventana.title("Гра в пінг-понг")
    elif idioma == "عرب":
        etiqueta_aviso_1.config(text="اللاعب الأول")
        etiqueta_aviso_2.config(text="اللاعب الثاني")
        boton_jugar_solo.config(text="العب بمفردك")
        boton_jugar.config(text="أ-ب")
        boton_hard.config(text="صعب")
        boton_validar.config(text="الخروج")
        ventana.title("لعبة البينغ بونغ")
    elif idioma == "हिंदी":
        etiqueta_aviso_1.config(text="खिलाड़ी ए")
        etiqueta_aviso_2.config(text="खिलाड़ी बी")
        boton_jugar_solo.config(text="एकल खेलो")
        boton_jugar.config(text="ए बी खेलें")
        boton_hard.config(text="कठिन")
        boton_validar.config(text="निकास")
        ventana.title("पिंग पोंग खेल")


def mostrar_menu_desplegable():
    ventana_menu = Toplevel(ventana)  # Crear una nueva ventana
    ventana_menu.title("Menú Desplegable")

    ### crear un menú desplegable en la nueva ventana
    menu_desplegable = Menu(ventana_menu)
    menu_idioma = Menu(menu_desplegable, tearoff=0)
    menu_idioma.add_command(label="Español", command=lambda: cambiar_idioma("Español"))
    menu_idioma.add_command(label="Inglés", command=lambda: cambiar_idioma("English"))
    menu_idioma.add_command(label="Русский", command=lambda: cambiar_idioma("Русский"))
    menu_idioma.add_command(label="Italiano", command=lambda: cambiar_idioma("Italiano"))
    menu_idioma.add_command(label="عرب", command=lambda: cambiar_idioma("عرب"))
    menu_idioma.add_command(label="हिंदी", command=lambda: cambiar_idioma("हिंदी"))
    menu_idioma.add_command(label="Portugués", command=lambda: cambiar_idioma("Portugués"))
    menu_idioma.add_command(label="українська", command=lambda: cambiar_idioma("українська"))
    menu_desplegable.add_cascade(label="Idioma", menu=menu_idioma)

    # configurar el menú desplegable en la nueva ventana
    ventana_menu.config(menu=menu_desplegable)

def salir():
    respuesta = messagebox.askquestion("Pregunta", "¿Seguro que desea salir del juego?")
    if respuesta == "yes":
        ventana.destroy()

def hardcore():
    print("hardcore")
    
def juego_solo():
    ventana.iconbitmap("logo_usc.ico")
    # Inicialización de pygame
    pygame.init()
    # Configuración de la pantalla
    screen_width = 1200
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Ping Pong")

    # Cargar la imagen de fondo
    background_image = pygame.image.load("mesa azul.png")
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

    # Colores
    white = (255, 255, 255)
    black = (30, 100, 0)

    # Variables de las paletas
    paddle_width = 10
    paddle_height = 100
    left_paddle_x = 50
    right_paddle_x = screen_width - 50 - paddle_width
    left_paddle_y = (screen_height - paddle_height) // 2
    right_paddle_y = (screen_height - paddle_height) // 2
    paddle_speed = 10
    ai_speed = 9

    # Variables de la pelota
    ball_size = 40
    ball_x = (screen_width - ball_size) // 2
    ball_y = (screen_height - ball_size) // 2
    ball_speed_x = 9
    ball_speed_y = 9

    # Puntajes
    left_score = 0
    right_score = 0

    # Fuente
    font = pygame.font.Font(None, 74)

    # Bucle principal del juego
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Controles de la paleta del jugador (izquierda)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and left_paddle_y > 0:
            left_paddle_y -= paddle_speed
        if keys[pygame.K_s] and left_paddle_y < screen_height - paddle_height:
            left_paddle_y += paddle_speed

        # Control de la paleta de la máquina (derecha)
        if right_paddle_y + paddle_height // 2 < ball_y and right_paddle_y < screen_height - paddle_height:
            right_paddle_y += ai_speed
        if right_paddle_y + paddle_height // 2 > ball_y and right_paddle_y > 0:
            right_paddle_y -= ai_speed

        # Movimiento de la pelota
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Colisión con los bordes superior e inferior
        if ball_y <= 0 or ball_y >= screen_height - ball_size:
            ball_speed_y *= -1

        # Colisión con las paletas
        if (left_paddle_x < ball_x < left_paddle_x + paddle_width and
            left_paddle_y < ball_y < left_paddle_y + paddle_height):
            ball_speed_x *= -1
        if (right_paddle_x < ball_x < right_paddle_x + paddle_width and
                right_paddle_y < ball_y < right_paddle_y + paddle_height):
            ball_speed_x *= -1

        # Colisión con los bordes izquierdo y derecho
        if ball_x <= 0:
            right_score += 1
            ball_x = (screen_width - ball_size) // 2
            ball_y = (screen_height - ball_size) // 2
            ball_speed_x *= -1
        if ball_x >= screen_width - ball_size:
            left_score += 1
            ball_x = (screen_width - ball_size) // 2
            ball_y = (screen_height - ball_size) // 2
            ball_speed_x *= -1

        # Dibujar todo
        screen.blit(background_image, (0, 0))
        pygame.draw.rect(screen, white, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
        pygame.draw.rect(screen, white, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))
        pygame.draw.ellipse(screen, white, (ball_x, ball_y, ball_size, ball_size))
        pygame.draw.aaline(screen, white, (screen_width // 2, 0), (screen_width // 2, screen_height))

        left_text = font.render("Tu = " + str(left_score), True, white)
        screen.blit(left_text, (screen_width // 5, 20))
        right_text = font.render("PC = " + str(right_score), True, white)
        screen.blit(right_text, (screen_width // 4 * 3, 20))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


def A_vs_B():
    a = usuario_1.get()
    b = usuario_2.get()
    if a == "" or b == "":
        messagebox.showerror("Campo Vacio", "Ingrese el nombre de los jugadores")
    else:
            # Inicialización de pygame
            pygame.init()

            # Configuración de la pantalla
            screen_width = 800
            screen_height = 600
            screen = pygame.display.set_mode((screen_width, screen_height))
            pygame.display.set_caption("Ping Pong")

            # Colores
            white = (255, 255, 255)
            black = (30, 100, 0)

            # Variables de las paletas
            paddle_width = 10
            paddle_height = 100
            left_paddle_x = 50
            right_paddle_x = screen_width - 50 - paddle_width
            left_paddle_y = (screen_height - paddle_height) // 2
            right_paddle_y = (screen_height - paddle_height) // 2
            paddle_speed = 10

            # Variables de la pelota
            ball_size = 20
            ball_x = (screen_width - ball_size) // 2
            ball_y = (screen_height - ball_size) // 2
            ball_speed_x = 5
            ball_speed_y = 5

            # Puntajes
            left_score = 0
            right_score = 0

            # Fuente
            font = pygame.font.Font(None, 74)

            # Bucle principal del juego
            running = True
            clock = pygame.time.Clock()

            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                # Controles de las paletas
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w] and left_paddle_y > 0:
                    left_paddle_y -= paddle_speed
                if keys[pygame.K_s] and left_paddle_y < screen_height - paddle_height:
                    left_paddle_y += paddle_speed
                if keys[pygame.K_UP] and right_paddle_y > 0:
                    right_paddle_y -= paddle_speed
                if keys[pygame.K_DOWN] and right_paddle_y < screen_height - paddle_height:
                    right_paddle_y += paddle_speed

                # Movimiento de la pelota
                ball_x += ball_speed_x
                ball_y += ball_speed_y

                # Colisión con los bordes superior e inferior
                if ball_y <= 0 or ball_y >= screen_height - ball_size:
                    ball_speed_y *= -1

                # Colisión con las paletas
                if (left_paddle_x < ball_x < left_paddle_x + paddle_width and
                        left_paddle_y < ball_y < left_paddle_y + paddle_height):
                    ball_speed_x *= -1
                if (right_paddle_x < ball_x < right_paddle_x + paddle_width and
                        right_paddle_y < ball_y < right_paddle_y + paddle_height):
                    ball_speed_x *= -1

                # Colisión con los bordes izquierdo y derecho
                if ball_x <= 0:
                    right_score += 1
                    ball_x = (screen_width - ball_size) // 2
                    ball_y = (screen_height - ball_size) // 2
                    ball_speed_x *= -1
                if ball_x >= screen_width - ball_size:
                    left_score += 1
                    ball_x = (screen_width - ball_size) // 2
                    ball_y = (screen_height - ball_size) // 2
                    ball_speed_x *= -1

                # Dibujar todo
                screen.fill(black)
                pygame.draw.rect(screen, white, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
                pygame.draw.rect(screen, white, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))
                pygame.draw.ellipse(screen, white, (ball_x, ball_y, ball_size, ball_size))
                pygame.draw.aaline(screen, white, (screen_width // 2, 0), (screen_width // 2, screen_height))
            
                # anotar los puntos
                nombre_1 = usuario_1.get()
                nombre_2 = usuario_2.get()
                left_text = font.render(str(left_score), True, white)
                screen.blit(left_text, (screen_width // 4, 20))
                right_text = font.render(str(right_score), True, white)
                screen.blit(right_text, (screen_width // 4 * 3, 20))
        
                # los nombres
                nombre_1_text = font.render(nombre_1, True, white)
                screen.blit(nombre_1_text, (screen_width // 7, 530)) 
                nombre_2_text = font.render(nombre_2, True, white)
                screen.blit(nombre_2_text, (screen_width // 5 * 3, 530))
        
                pygame.display.flip()
                clock.tick(60)

            pygame.quit()
            sys.exit()


ventana = Tk()
ventana.iconbitmap("logo_usc.ico")
ventana.geometry("900x620")
ventana.resizable(False, False)
ventana.title("Pin Pon Game USC")

# imagen del niño jugando pinpon
imagen_original = Image.open("icono del juego.png")
imagen_redimensionada = imagen_original.resize((590, 580), Image.LANCZOS)
imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
mi_imagen = Label(ventana, image=imagen_tk)

# Mostrar la imagen en la ventana
mi_imagen = Label(ventana, image=imagen_tk)
mi_imagen.place(x=10, y=20)

# entrada texto para los jugadores
etiqueta_aviso_1 = Label(ventana, text="JUGADOR A", font=("arial", 16, 'bold'))
etiqueta_aviso_1.place(x=610, y=40)
usuario_1 = Entry(ventana, width=14, font=("arial", 16, "bold"), border=2, fg="black")
usuario_1.place(x=610, y=100)

etiqueta_aviso_2 = Label(ventana, text="JUGADOR B", font=("arial", 16, 'bold'))
etiqueta_aviso_2.place(x=610, y=160)
usuario_2 = Entry(ventana, width=14, font=("arial", 16, "bold"), border=2, fg="black")
usuario_2.place(x=610, y=220)

# botones
boton_jugar_solo = Button(ventana, text="JUGAR SOLO", font=("arial black", 14, 'bold'), width=13, height=1, bg="#0093EE",border=3, command=juego_solo)
boton_jugar_solo.place(x=610, y=300)

boton_jugar = Button(ventana, text="A VS B", font=("arial black", 14, 'bold'), width=13, height=1, bg="SpringGreen2",border=3, command=A_vs_B)
boton_jugar.place(x=610, y=370)

boton_hard = Button(ventana, text="HARDCORE", font=("times new roman", 15, 'bold'), width=13, height=1,border=9, bg="black", fg="red")
boton_hard.place(x=610, y=440)

boton_validar = Button(ventana, text="SALIR", font=("arial black", 14, 'bold'), width=13, height=1, bg="#FC6407",border=3, command=salir)
boton_validar.place(x=610, y=510)

# ajustes
imagen = PhotoImage(file="ajustes.png")
imagen = imagen.subsample(2, 2) 
boton = Button(ventana, image=imagen, width=68, height=68, command=mostrar_menu_desplegable)
boton.place(x=5, y=2)

ventana.mainloop()


