from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
import sys

# sonido del intro
pygame.mixer.init()
intro_juego = pygame.mixer.Sound("intro.ogg")
golpe_paleta = pygame.mixer.Sound("golpe paleta.ogg")
glope_bordes = pygame.mixer.Sound("choque_bordes.ogg")
partida_perdida = pygame.mixer.Sound("perdiste.ogg")
audio_terror = pygame.mixer.Sound("terror.ogg")

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
    intro_juego.stop()

def hardcore():
    intro_juego.stop()
    audio_terror.play()
    ventana.iconbitmap("logo_usc.ico")  # Establece el icono de la ventana
    pygame.init()  # Inicializa todos los módulos de Pygame
    screen_width = 1200
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))  # Configura el tamaño de la ventana
    pygame.display.set_caption("Ping Pong")  # Establece el título de la ventana

    # Carga y escala la imagen de fondo
    background_image = pygame.image.load("mesa negra.png")
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

    # Colores
    white = (255, 255, 255)
    black = (30, 100, 0)

    # Clase Raqueta que representa una paleta
    class Raqueta(pygame.sprite.Sprite):
        def __init__(self, paddel, paddle_width, paddle_height):
            super().__init__()
            self.paddle_width = paddle_width
            self.paddle_height = paddle_height
            # Carga la imagen de la paleta y la escala
            self.image = pygame.image.load("tablar.png").convert()
            self.image = pygame.transform.scale(self.image, (self.paddle_width, self.paddle_height))
            self.image.set_colorkey([0, 0, 0])  # Elimina el fondo negro
            self.rect = self.image.get_rect()
            self.rect.y = (screen_height - self.paddle_height) // 2  # Centra verticalmente la paleta
            self.rect.x = paddel  # Establece la posición horizontal

        def update(self):
            # Limita el movimiento de la paleta dentro de la pantalla
            if self.rect.y < 0:
                self.rect.y = 0
            if self.rect.y > (screen_height - self.paddle_height):
                self.rect.y = screen_height - self.paddle_height

    # Clase Pelota que representa la pelota del juego
    class Pelota(pygame.sprite.Sprite):
        def __init__(self, left_score, right_score):
            super().__init__()
            self.ballzc = 40
            self.speedx = 23  # Velocidad inicial en X
            self.speedy = 24  # Velocidad inicial en Y
            self.left_score = left_score
            self.right_score = right_score
            # Carga la imagen de la pelota y la escala
            self.image = pygame.image.load("rojo.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.ballzc, self.ballzc))
            self.image.set_colorkey([255, 255, 255])  # Elimina el fondo blanco
            self.rect = self.image.get_rect()
            self.rect.x = (screen_width - self.ballzc) // 2  # Centra horizontalmente la pelota
            self.rect.y = (screen_height - self.ballzc) // 2  # Centra verticalmente la pelota

        def update(self):
            # Actualiza la posición de la pelota
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            # Rebote en los bordes superior e inferior
            if self.rect.top <= 0 or self.rect.bottom >= screen_height:
                glope_bordes.play()
                self.speedy *= -1
            # Rebote en los bordes izquierdo y derecho
            if self.rect.left <= 0:
                self.speedx *= -1
                self.right_score += 1
                self.reset_position()
            if self.rect.right >= screen_width:
                self.speedx *= -1
                self.left_score += 1
                self.reset_position()

        def reset_position(self):
            self.rect.x = (screen_width - self.ballzc) // 2
            self.rect.y = (screen_height - self.ballzc) // 2

    left_score = 0  # Puntuación del jugador
    right_score = 0  # Puntuación del AI

    font = pygame.font.Font(None, 74)  # Fuente para mostrar la puntuación

    running = True
    clock = pygame.time.Clock()

    all_list_sprite = pygame.sprite.Group()
    raqt = pygame.sprite.Group()
    paddle_height = 190  # Altura de las paletas
    player = Raqueta(50, 50, paddle_height)  # Paleta del jugador
    ai = Raqueta(screen_width - 50 - player.paddle_width, 50, paddle_height)  # Paleta del AI
    ball = Pelota(left_score, right_score)  # Pelota del juego
    raqt.add(player)
    raqt.add(ai)
    all_list_sprite.add(ball)
    all_list_sprite.add(raqt)
    pygame.init()

    # Bucle principal del juego
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Termina el juego si se cierra la ventana

        # Control de la paleta del jugador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player.rect.y -= 16
        if keys[pygame.K_s]:
            player.rect.y += 16

        # Control de la paleta del AI
        if ai.rect.centery < ball.rect.centery:
            ai.rect.y += 20
        else:
            ai.rect.y -= 20

        # Detecta colisiones entre la pelota y las paletas
        if pygame.sprite.collide_mask(ball, player):
            golpe_paleta.play()
            ball.speedx *= -1
        if pygame.sprite.collide_mask(ball, ai):
            golpe_paleta.play()
            ball.speedx *= -1

        all_list_sprite.update()

        screen.blit(background_image, (0, 0))  # Dibuja el fondo
        all_list_sprite.draw(screen)  # Dibuja todos los sprites

        # Dibuja la línea central
        pygame.draw.aaline(screen, white, (screen_width // 2, 0), (screen_width // 2, screen_height))

        # Muestra la puntuación
        left_text = font.render("Tu = " + str(ball.left_score), True, white)
        screen.blit(left_text, (screen_width // 5, 20))
        right_text = font.render("PC = " + str(ball.right_score), True, white)
        screen.blit(right_text, (screen_width // 4 * 3, 20))

        pygame.display.update()
        clock.tick(60)  # Limita el juego a 60 FPS
    
    pygame.quit()  # Termina Pygame
    sys.exit()  # Cierra el programa


def juego_solo():
    intro_juego.stop()
    ventana.iconbitmap("logo_usc.ico")  # Establece el icono de la ventana
    pygame.init()  # Inicializa todos los módulos de Pygame
    screen_width = 1200
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))  # Configura el tamaño de la ventana
    pygame.display.set_caption("Ping Pong")  # Establece el título de la ventana

    # Carga y escala la imagen de fondo
    background_image = pygame.image.load("mesa azul.png")
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

    # Colores
    white = (255, 255, 255)
    black = (30, 100, 0)

    # Clase Raqueta que representa una paleta
    class Raqueta(pygame.sprite.Sprite):
        def __init__(self, paddel, paddle_width, paddle_height):
            super().__init__()
            self.paddle_width = paddle_width
            self.paddle_height = paddle_height
            # Carga la imagen de la paleta y la escala
            self.image = pygame.image.load("tablar.png").convert()
            self.image = pygame.transform.scale(self.image, (self.paddle_width, self.paddle_height))
            self.image.set_colorkey([0, 0, 0])  # Elimina el fondo negro
            self.rect = self.image.get_rect()
            self.rect.y = (screen_height - self.paddle_height) // 2  # Centra verticalmente la paleta
            self.rect.x = paddel  # Establece la posición horizontal

        def update(self):
            # Limita el movimiento de la paleta dentro de la pantalla
            if self.rect.y < 0:
                self.rect.y = 0
            if self.rect.y > (screen_height - self.paddle_height):
                self.rect.y = screen_height - self.paddle_height

    # Clase Pelota que representa la pelota del juego
    class Pelota(pygame.sprite.Sprite):
        def __init__(self, left_score, right_score):
            super().__init__()
            self.ballzc = 40
            self.speedx = 15  # Velocidad inicial en X
            self.speedy = 15  # Velocidad inicial en Y
            self.left_score = left_score
            self.right_score = right_score
            # Carga la imagen de la pelota y la escala
            self.image = pygame.image.load("pelota.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.ballzc, self.ballzc))
            self.image.set_colorkey([255, 255, 255])  # Elimina el fondo blanco
            self.rect = self.image.get_rect()
            self.rect.x = (screen_width - self.ballzc) // 2  # Centra horizontalmente la pelota
            self.rect.y = (screen_height - self.ballzc) // 2  # Centra verticalmente la pelota

        def update(self):
            # Actualiza la posición de la pelota
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            # Rebote en los bordes superior e inferior
            if self.rect.top <= 0 or self.rect.bottom >= screen_height:
                glope_bordes.play()
                self.speedy *= -1
            # Rebote en los bordes izquierdo y derecho
            if self.rect.left <= 0:
                self.speedx *= -1
                self.right_score += 1
                self.reset_position()
            if self.rect.right >= screen_width:
                self.speedx *= -1
                self.left_score += 1
                self.reset_position()

        def reset_position(self):
            self.rect.x = (screen_width - self.ballzc) // 2
            self.rect.y = (screen_height - self.ballzc) // 2

    left_score = 0  # Puntuación del jugador
    right_score = 0  # Puntuación del AI

    font = pygame.font.Font(None, 74)  # Fuente para mostrar la puntuación

    running = True
    clock = pygame.time.Clock()

    all_list_sprite = pygame.sprite.Group()
    raqt = pygame.sprite.Group()
    paddle_height = 190  # Altura de las paletas
    player = Raqueta(50, 50, paddle_height)  # Paleta del jugador
    ai = Raqueta(screen_width - 50 - player.paddle_width, 50, paddle_height)  # Paleta del AI
    ball = Pelota(left_score, right_score)  # Pelota del juego
    raqt.add(player)
    raqt.add(ai)
    all_list_sprite.add(ball)
    all_list_sprite.add(raqt)
    pygame.init()

    # Bucle principal del juego
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Termina el juego si se cierra la ventana

        # Control de la paleta del jugador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player.rect.y -= 14
        if keys[pygame.K_s]:
            player.rect.y += 14

        # Control de la paleta del AI
        if ai.rect.centery < ball.rect.centery:
            ai.rect.y += 12
        else:
            ai.rect.y -= 12

        # Detecta colisiones entre la pelota y las paletas
        if pygame.sprite.collide_mask(ball, player):
            golpe_paleta.play()
            ball.speedx *= -1
        if pygame.sprite.collide_mask(ball, ai):
            golpe_paleta.play()
            ball.speedx *= -1

        all_list_sprite.update()

        screen.blit(background_image, (0, 0))  # Dibuja el fondo
        all_list_sprite.draw(screen)  # Dibuja todos los sprites

        # Dibuja la línea central
        pygame.draw.aaline(screen, white, (screen_width // 2, 0), (screen_width // 2, screen_height))

        # Muestra la puntuación
        left_text = font.render("Tu = " + str(ball.left_score), True, white)
        screen.blit(left_text, (screen_width // 5, 20))
        right_text = font.render("PC = " + str(ball.right_score), True, white)
        screen.blit(right_text, (screen_width // 4 * 3, 20))

        pygame.display.update()
        clock.tick(60)  # Limita el juego a 60 FPS
        
    pygame.quit()  # Termina Pygame
    sys.exit()  # Cierra el programa


def A_vs_B():
    intro_juego.stop()

    class Raqueta(pygame.sprite.Sprite):
        def __init__(self, paddel, paddle_width, paddle_height):
            super().__init__()
            self.paddle_width = paddle_width
            self.paddle_height = paddle_height
            # Carga la imagen de la paleta y la escala
            self.image = pygame.image.load("tablar.png").convert()
            self.image = pygame.transform.scale(self.image, (self.paddle_width, self.paddle_height))
            self.image.set_colorkey([0, 0, 0])  # Elimina el fondo negro
            self.rect = self.image.get_rect()
            self.rect.y = (screen_height - self.paddle_height) // 2  # Centra verticalmente la paleta
            self.rect.x = paddel  # Establece la posición horizontal

        def update(self):
            # Limita el movimiento de la paleta dentro de la pantalla
            if self.rect.y < 0:
                self.rect.y = 0
            if self.rect.y > (screen_height - self.paddle_height):
                self.rect.y = screen_height - self.paddle_height

    class Pelota(pygame.sprite.Sprite):
        def __init__(self, left_score, right_score):
            super().__init__()
            self.ballzc = 40
            self.speedx = 14  # Velocidad inicial en X
            self.speedy = 14  # Velocidad inicial en Y
            self.left_score = left_score
            self.right_score = right_score
            # Carga la imagen de la pelota y la escala
            self.image = pygame.image.load("pelota.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.ballzc, self.ballzc))
            self.image.set_colorkey([255, 255, 255])  # Elimina el fondo blanco
            self.rect = self.image.get_rect()
            self.rect.x = (screen_width - self.ballzc) // 2  # Centra horizontalmente la pelota
            self.rect.y = (screen_height - self.ballzc) // 2  # Centra verticalmente la pelota

        def update(self):
            # Actualiza la posición de la pelota
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            # Rebote en los bordes superior e inferior
            if self.rect.top <= 0 or self.rect.bottom >= screen_height:
                self.speedy *= -1
            # Rebote en los bordes izquierdo y derecho
            if self.rect.left <= 0:
                self.speedx *= -1
                self.right_score += 1
                self.reset_position()
            if self.rect.right >= screen_width:
                self.speedx *= -1
                self.left_score += 1
                self.reset_position()

        def reset_position(self):
            self.rect.x = (screen_width - self.ballzc) // 2
            self.rect.y = (screen_height - self.ballzc) // 2

    a = usuario_1.get()
    b = usuario_2.get()
    if a == "" or b == "":
        messagebox.showerror("Campo Vacio", "Ingrese el nombre de los jugadores")
    else:
        pygame.init()  # Inicializa todos los módulos de Pygame
        screen_width = 1200
        screen_height = 800
        screen = pygame.display.set_mode((screen_width, screen_height))  # Configura el tamaño de la ventana
        pygame.display.set_caption("Ping Pong")  # Establece el título de la ventana

        # Carga y escala la imagen de fondo
        background_image = pygame.image.load("mesa azul.png")
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

        # Colores
        white = (255, 255, 255)
        black = (30, 100, 0)

        left_score = 0  # Puntuación del jugador
        right_score = 0  # Puntuación del AI

        font = pygame.font.Font(None, 74)  # Fuente para mostrar la puntuación

        running = True
        clock = pygame.time.Clock()

        all_list_sprite = pygame.sprite.Group()
        raqt = pygame.sprite.Group()
        paddle_height = 180  # Altura de las paletas
        player1 = Raqueta(50, 50, paddle_height)  # Paleta del jugador 1
        player2 = Raqueta(screen_width - 50 - player1.paddle_width, 50, paddle_height)  # Paleta del jugador 2
        ball = Pelota(left_score, right_score)  # Pelota del juego
        raqt.add(player1)
        raqt.add(player2)
        all_list_sprite.add(ball)
        all_list_sprite.add(raqt)
        pygame.init()

        # Bucle principal del juego
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  # Termina el juego si se cierra la ventana

            # Control de la paleta del jugador 1
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                player1.rect.y -= 15
            if keys[pygame.K_s]:
                player1.rect.y += 15

            # Control de la paleta del jugador 2
            if keys[pygame.K_UP]:
                player2.rect.y -= 15
            if keys[pygame.K_DOWN]:
                player2.rect.y += 15

            # Detecta colisiones entre la pelota y las paletas
            if pygame.sprite.collide_mask(ball, player1):
                ball.speedx *= -1
            if pygame.sprite.collide_mask(ball, player2):
                ball.speedx *= -1

            all_list_sprite.update()

            screen.blit(background_image, (0, 0))  # Dibuja el fondo
            all_list_sprite.draw(screen)  # Dibuja todos los sprites

            # Dibuja la línea central
            pygame.draw.aaline(screen, white, (screen_width // 2, 0), (screen_width // 2, screen_height))

            # Muestra la puntuación
            left_text = font.render("Tu = " + str(ball.left_score), True, white)
            screen.blit(left_text, (screen_width // 5, 20))
            right_text = font.render("PC = " + str(ball.right_score), True, white)
            screen.blit(right_text, (screen_width // 4 * 3, 20))

            pygame.display.update()
            clock.tick(60)  # Limita el juego a 60 FPS

        pygame.quit()  # Termina Pygame
        sys.exit()  # Cierra el programa


ventana = Tk()
ventana.iconbitmap("logo_usc.ico")
ventana.geometry("900x620")
ventana.resizable(False, False)
ventana.title("Pin Pon Game USC")
intro_juego.play()

imagen_original = Image.open("icono del juego.png")
imagen_redimensionada = imagen_original.resize((590, 580), Image.LANCZOS)
imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
mi_imagen = Label(ventana, image=imagen_tk)

mi_imagen = Label(ventana, image=imagen_tk)
mi_imagen.place(x=10, y=20)

etiqueta_aviso_1 = Label(ventana, text="JUGADOR A", font=("arial", 16, 'bold'))
etiqueta_aviso_1.place(x=610, y=40)
usuario_1 = Entry(ventana, width=14, font=("arial", 16, "bold"), border=2, fg="black")
usuario_1.place(x=610, y=100)

etiqueta_aviso_2 = Label(ventana, text="JUGADOR B", font=("arial", 16, 'bold'))
etiqueta_aviso_2.place(x=610, y=160)
usuario_2 = Entry(ventana, width=14, font=("arial", 16, "bold"), border=2, fg="black")
usuario_2.place(x=610, y=220)

boton_jugar_solo = Button(ventana, text="JUGAR SOLO", font=("arial black", 14, 'bold'), width=13, height=1, bg="#0093EE", border=3, command=juego_solo)
boton_jugar_solo.place(x=610, y=300)

boton_jugar = Button(ventana, text="A VS B", font=("arial black", 14, 'bold'), width=13, height=1, bg="SpringGreen2", border=3, command=A_vs_B)
boton_jugar.place(x=610, y=370)

boton_hard = Button(ventana, text="HARDCORE", font=("times new roman", 15, 'bold'), width=13, height=1, border=9, bg="black", fg="red", command=hardcore)
boton_hard.place(x=610, y=440)

boton_validar = Button(ventana, text="SALIR", font=("arial black", 14, 'bold'), width=13, height=1, bg="#FC6407", border=3, command=salir)
boton_validar.place(x=610, y=510)

imagen = PhotoImage(file="ajustes.png")
imagen = imagen.subsample(2, 2)
boton = Button(ventana, image=imagen, width=68, height=68, command=mostrar_menu_desplegable)
boton.place(x=5, y=2)

ventana.mainloop()

