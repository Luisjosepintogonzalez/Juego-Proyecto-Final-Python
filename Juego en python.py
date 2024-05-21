from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
import sys

def salir():
    respuesta = messagebox.askquestion("Pregunta", "¿Seguro que desea salir del juego?")
    if respuesta == "yes":
        ventana.destroy()

def juego_solo():
    ventana.iconbitmap("logo_usc.ico")
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
    ai_speed = 7

    # Variables de la pelota
    ball_size = 20
    ball_x = (screen_width - ball_size) // 2
    ball_y = (screen_height - ball_size) // 2
    ball_speed_x = 5
    ball_speed_y = 5
    choques=0
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

       # ...

# Control de la paleta de la máquina (derecha)
        if right_paddle_y + paddle_height // 2 < ball_y and right_paddle_y < screen_height - paddle_height:
    # Suaviza el movimiento hacia la posición de la pelota
         target_y = ball_y - paddle_height // 2
         right_paddle_y += (target_y - right_paddle_y) * 0.4  # Ajusta el factor de suavizado

        if right_paddle_y + paddle_height // 2 > ball_y and right_paddle_y > 0:
    # Suaviza el movimiento hacia la posición de la pelota
         target_y = ball_y - paddle_height // 2
         right_paddle_y += (target_y - right_paddle_y) * 0.4  # Ajusta el factor de suavizado

# ...

        # Movimiento de la pelota
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Colisión con los bordes superior e inferior
        if ball_y <= 0 or ball_y >= screen_height - ball_size:
            ball_speed_y *= -1

   
        # Colisión con los bordes izquierdo y derecho
        if ball_x <= 0:
            right_score += 1
            ball_x = (screen_width - ball_size) // 2
            ball_y = (screen_height - ball_size) // 2
            ball_speed_x *= -1
            ball_speed_x=5
            choques=0
        if ball_x >= screen_width - ball_size:
            left_score += 1
            ball_x = (screen_width - ball_size) // 2
            ball_y = (screen_height - ball_size) // 2
            ball_speed_x *= -1
            ball_speed_x=5
            choques=0
        # Dibujar todo
        screen.fill(black)
        player1=pygame.draw.rect(screen, white, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
        ai=pygame.draw.rect(screen, white, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))
        ball=pygame.draw.ellipse(screen, white, (ball_x, ball_y, ball_size, ball_size))

        #colision de la pelota con los jugadores
        if ball.colliderect(ai) or ball.colliderect(player1):
         ball_speed_x *= -1
         ball_speed_x+=choques
         choques+=1 
         ball_speed_y=5
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
            colision=0
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
                '''
                # Colisión con las paletas
                if (left_paddle_x < ball_x < left_paddle_x + paddle_width and
                        left_paddle_y < ball_y < left_paddle_y + paddle_height):
                    ball_speed_x *= -1
                if (right_paddle_x < ball_x < right_paddle_x + paddle_width and
                        right_paddle_y < ball_y < right_paddle_y + paddle_height):
                    ball_speed_x *= -1
'''
                # Colisión con los bordes izquierdo y derecho
                if ball_x <= 0:
                    right_score += 1
                    ball_x = (screen_width - ball_size) // 2
                    ball_y = (screen_height - ball_size) // 2
                    ball_speed_x=5 
                    ball_speed_x *= -1
                    colision=0
                  
                if ball_x >= screen_width - ball_size:
                    left_score += 1
                    ball_x = (screen_width - ball_size) // 2
                    ball_y = (screen_height - ball_size) // 2
                    ball_speed_x=5
                    ball_speed_x *= -1
                    colision=0
                  
                # Dibujar todo
                screen.fill(black)
                jugador1= pygame.draw.rect(screen, white, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
                jugador2=pygame.draw.rect(screen, white, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))
                pelota=pygame.draw.ellipse(screen, white, (ball_x, ball_y, ball_size, ball_size))
                pygame.draw.aaline(screen, white, (screen_width // 2, 0), (screen_width // 2, screen_height))
            
                if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
                    ball_speed_x *= -1
                    colision+=1
                    ball_speed_x+=colision
                    ball_speed_y=5
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
ventana.geometry("800x520")
ventana.resizable(False, False)
ventana.title("Pin Pon Game USC")

# imagen del niño jugando pinpon
imagen_original = Image.open("logo_pinpon.jpeg")
imagen_redimensionada = imagen_original.resize((500, 490), Image.LANCZOS)
imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
mi_imagen = Label(ventana, image=imagen_tk)
mi_imagen.place(x=320, y=10)

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
boton_jugar_solo = Button(ventana, text="JUGAR SOLO", font=("arial black", 14, 'bold'), width=16, height=1, bg="SpringGreen2", command=juego_solo)
boton_jugar_solo.place(x=30, y=300)

boton_jugar = Button(ventana, text="A VS B", font=("arial black", 14, 'bold'), width=16, height=1, bg="#FCC807", command=A_vs_B)
boton_jugar.place(x=30, y=370)

boton_validar = Button(ventana, text="SALIR", font=("arial black", 14, 'bold'), width=16, height=1, bg="#FC6407", command=salir)
boton_validar.place(x=30, y=440)
ventana.mainloop()

