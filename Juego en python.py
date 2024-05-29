from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
import time
import sys

# sonido del intro
pygame.mixer.init()
intro_juego = pygame.mixer.Sound("intro.ogg")
golpe_paleta = pygame.mixer.Sound("golpe paleta.ogg")
glope_bordes = pygame.mixer.Sound("choque_bordes.ogg")
partida_perdida = pygame.mixer.Sound("perdiste.ogg")
audio_terror = pygame.mixer.Sound("terror.ogg")
perdiste= pygame.mixer.Sound("perdiste.ogg")
ganaste=pygame.mixer.Sound("ganaste.mp3")

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
    ventana_menu = Toplevel(ventana)  # para la ventana
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
    class Juego(object):
        def __init__(self,screen,screen_width,screen_height,background_image):
             self.game_over=False

             self.background_image=background_image
             self.white = (255, 255, 255)
             self.black = (30, 100, 0)
             self.screen=screen
             self.screen_width=screen_width
             self.screen_heigth=screen_height
             self.font = pygame.font.Font(None, 74)
             ventana.iconbitmap("logo_usc.ico")  #  icono de la ventana
            
             self.left_score = 0  # Puntuación del jugador
             self.right_score = 0  # Puntuación del pc

             self.all_list_sprite = pygame.sprite.Group()
             self.raqt = pygame.sprite.Group()
             self.paddle_height = 190  # atura de las paletas
             self.player = Raqueta(50, 50, self.paddle_height,screen_height)  # Paleta del jugador
             self.ai = Raqueta(self.screen_width - 50 - self.player.paddle_width, 50, self.paddle_height,screen_height)  #  paleta del pc
             self.ball = Pelota(self.left_score, self.right_score,screen_height,screen_width)  # Pelota del juego
             self.raqt.add(self.player)
             self.raqt.add(self.ai)
             self.all_list_sprite.add(self.ball)
             self.all_list_sprite.add(self.raqt)

        def eventos_proceso(self):
          for event in pygame.event.get(): 
           if event.type == pygame.QUIT:
            return False 
          
           if self.game_over:
            game_over_text = self.font.render("Game Over", True, (220,20,60))
            self.screen.blit(game_over_text, (self.screen_width // 2 - 100, self.screen_heigth // 2))
            pygame.display.update()
           
            if self.ball.left_score==3:
               winer_text = "player 1 win"
               l=1
            else:
              winer_text = "PC win"
              l=2
            winner_surf=self.font.render(winer_text, True, (220,20,60))
            self.screen.blit(winner_surf, (self.screen_width // 2 - 100, self.screen_heigth // 2 + 45))
            if l==2:
             perdiste.play()
            else:
               ganaste.play()
            winner_surf=self.font.render("Presiona espacio para repetir", True, (220,20,60))
            self.screen.blit(winner_surf, (self.screen_width // 2 - 300, self.screen_heigth // 2 + 70))
            pygame.display.update()
            # Espera a que se presione una tecla
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    perdiste.stop()
                    ganaste.stop()
                    self.game_over = False  ## restablece la condición de game over
                    self.ball.left_score = 0  # restablece las puntuaciones
                    self.ball.right_score = 0
                    self.ball.reset_position()  # asume que tienes un método para restablecer la posición de la pelota
                    
          return True

        
        def logica(self):
             # control de la paleta del jugador
         
        # detecta colisiones entre la pelota y las paletas
        
         keys = pygame.key.get_pressed()
         if not self.game_over:
           if keys[pygame.K_w]:
              self.player.rect.y -= 14
           if keys[pygame.K_s]:
              self.player.rect.y += 14
          
        # control de la paleta de la pc
           if self.ai.rect.centery < self.ball.rect.centery:
               self.ai.rect.y += 18 #velocidad
           else:
                self.ai.rect.y -= 18
        
           if pygame.sprite.collide_mask(self.ball, self.player):
            if self.ball.rect.top>= self.player.rect.top and self.ball.rect.bottom<= self.player.rect.bottom:
             golpe_paleta.play()
             self.ball.speedx *= -1
           if pygame.sprite.collide_mask(self.ball, self.ai):
            if self.ball.rect.top>= self.ai.rect.top and self.ball.rect.bottom<= self.ai.rect.bottom:
             golpe_paleta.play()
             self.ball.speedx *= -1
            
           if self.ball.left_score==3 or self.ball.right_score==3:
              self.game_over=True
           self.all_list_sprite.update() 
          
        def display_frame(self):
            self.screen.blit(self.background_image, (0, 0))  # Dibuja el fondo
            self.all_list_sprite.draw(self.screen)  # Dibuja todos los sprites
            
        # dibuja la línea central
            pygame.draw.aaline(self.screen, self.white, (self.screen_width // 2, 0), (self.screen_width // 2, self.screen_heigth))
            pygame.display.update()
            self.left_text = self.font.render("Tu = " + str(self.ball.left_score), True, self.white)
            self.screen.blit(self.left_text, (self.screen_width // 5, 20))
            right_text = self.font.render("PC = " + str(self.ball.right_score), True, self.white)
            self.screen.blit(right_text, (self.screen_width // 4 * 3, 20))
            pygame.display.update()
    class Raqueta(pygame.sprite.Sprite):
        def __init__(self, paddel, paddle_width, paddle_height,screen_height):
            super().__init__()
            self.screen_height=screen_height
            self.paddle_width = paddle_width
            self.paddle_height = paddle_height
            # carga la imagen de la paleta y la escala
            self.image = pygame.image.load("tablar.png").convert()
            self.image = pygame.transform.scale(self.image, (self.paddle_width, self.paddle_height))
            self.image.set_colorkey([0, 0, 0])  # Elimina el fondo negro
            self.rect = self.image.get_rect()
            self.rect.y = (screen_height - self.paddle_height) // 2  # Centra verticalmente la paleta
            self.rect.x = paddel  #### establece la posición horizontal
      
        def update(self):
            #/ limitar el movimiento de la paleta dentro de la pantalla
            if self.rect.y < 0:
                self.rect.y = 0
            if self.rect.y > (self.screen_height - self.paddle_height):
                self.rect.y = self.screen_height - self.paddle_height
          
    # clase Pelota que representa la pelota del juego
    class Pelota(pygame.sprite.Sprite):
        def __init__(self, left_score, right_score,screen_height,screen_width):
            super().__init__()
            self.screen_height=screen_height
            self.screen_width=screen_width
            self.ballzc = 40
            self.speedx = 24 # velocidad inicial en X
            self.speedy = 23  # velocidad inicial en Y
            self.left_score = left_score
            self.right_score = right_score
            # carga la imagen de la pelota y la escala
            self.image = pygame.image.load("rojo.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.ballzc, self.ballzc))
            self.image.set_colorkey([255, 255, 255])  # Elimina el fondo blanco
            self.rect = self.image.get_rect()
            self.rect.x = (self.screen_width - self.ballzc) // 2  # Centra horizontalmente la pelota
            self.rect.y = (self.screen_height - self.ballzc) // 2  # Centra verticalmente la pelota

        def update(self):
            # actualiza la posición de la pelota
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            # rebote en los bordes superior e inferior
            if self.rect.top <= 0 or self.rect.bottom >= self.screen_height:
                glope_bordes.play()
                self.speedy *= -1
            # rebote en los bordes izquierdo y derecho
            if self.rect.left <= 0:
                self.speedx *= -1
                self.right_score += 1
                self.reset_position()
            if self.rect.right >= self.screen_width:
                self.speedx *= -1
                self.left_score += 1
                self.reset_position()

        def reset_position(self):
            self.rect.x = (self.screen_width - self.ballzc) // 2
            self.rect.y = (self.screen_height - self.ballzc) // 2

        def update(self):
            # actualiza la posición de la pelota
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            # rebote en los bordes superior e inferior
            if self.rect.top <= 0 or self.rect.bottom >= self.screen_height:
                glope_bordes.play()
                self.speedy *= -1
            # rebote en los bordes izquierdo y derecho
            if self.rect.left <= 0:
                self.speedx *= -1
                self.right_score += 1
                self.reset_position()
            if self.rect.right >= self.screen_width:
                self.speedx *= -1
                self.left_score += 1
                self.reset_position()

        def reset_position(self):
            self.rect.x = (self.screen_width - self.ballzc) // 2
            self.rect.y = (self.screen_height - self.ballzc) // 2
   
    def main():
         pygame.init()  # inicializa todos los módulos de Pygame
         intro_juego.stop()
         audio_terror.play()
         ventana.iconbitmap("logo_usc.ico")  # icono de la ventana
         pygame.init()
         screen_width = 1200
         screen_height = 800
         screen = pygame.display.set_mode((screen_width, screen_height))  # configura el tamaño de la ventana
         pygame.display.set_caption("Ping Pong")

    # Carga y escala la imagen de fondo
         background_image = pygame.image.load("mesa negra.png")
         background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

    # Colores
         running = True
         clock = pygame.time.Clock()
         game=Juego(screen,screen_width,screen_height,background_image)
         while running:
             running= game.eventos_proceso()
             game.logica()
             game.display_frame()
             clock.tick(60)  # imitar el juego a 60 FPS
         pygame.quit()  # terminar el juego
         sys.exit()  #
    if __name__=="__main__":
        main()
  
def juego_solo():
    intro_juego.stop()

    class Boton:
        def __init__(self, x, y, text, font, color, screen):
            # Inicializar propiedades del botón
            self.x = x
            self.y = y
            self.text = text
            self.font = font
            self.color = color
            self.screen = screen
            self.image = self.font.render(self.text, True, self.color)
            self.rect = self.image.get_rect(center=(self.x, self.y))

        def draw(self):
            # dibujar el botón en la pantalla
            self.screen.blit(self.image, self.rect)

        def is_clicked(self, pos):
            # verificar si el botón ha sido clicado
            return self.rect.collidepoint(pos)

    #cClase Juego para manejar la lógica y la interfaz del juego
    class Juego(object):
        def __init__(self, screen, screen_width, screen_height, background_image):
            # inicializar propiedades del juego
            self.game_over = False
            self.background_image = background_image
            self.white = (255, 255, 255)
            self.black = (30, 100, 0)
            self.screen = screen
            self.screen_width = screen_width
            self.screen_height = screen_height
            self.font = pygame.font.Font(None, 74)
            self.button_font = pygame.font.Font(None, 36)
            self.left_score = 0  # puntuación del jugador
            self.right_score = 0  # puntuación del pc

            # grupos de sprites para manejar múltiples sprites a la vez
            self.all_list_sprite = pygame.sprite.Group()
            self.raqt = pygame.sprite.Group()
            self.paddle_height = 190  # altura de las paletas
            self.player = Raqueta(50, 50, self.paddle_height, screen_height)  # paleta del jugador
            self.ai = Raqueta(self.screen_width - 50 - self.player.paddle_width, 50, self.paddle_height, screen_height)  # Paleta del del pc
            self.ball = Pelota(self.left_score, self.right_score, screen_height, screen_width)  # pelota del juego
            self.raqt.add(self.player)
            self.raqt.add(self.ai)
            self.all_list_sprite.add(self.ball)
            self.all_list_sprite.add(self.raqt)

            # crear botón de reinicio
            self.restart_button = Boton(self.screen_width // 3, self.screen_height // 2 + 100, "Reiniciar", self.button_font, self.white, self.screen)

        def eventos_proceso(self):
            # manejar eventos del juego
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False  # salir del juego
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # verificar si se ha clicado el botón de reinicio
                    if self.game_over and self.restart_button.is_clicked(event.pos):
                        self.reset_game()
            return True

        def logica(self):
            # lógica del juego
            if not self.game_over:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                    self.player.rect.y -= 14  # mover paleta del jugador hacia arriba
                if keys[pygame.K_s]:
                    self.player.rect.y += 14  # mover paleta del jugador hacia abajo

                # movimiento automático de la paleta del pc
                if self.ai.rect.centery < self.ball.rect.centery:
                    self.ai.rect.y += 13
                else:
                    self.ai.rect.y -= 13

                # colisión con las paletas
                if pygame.sprite.collide_mask(self.ball, self.player) or pygame.sprite.collide_mask(self.ball, self.ai):
                    golpe_paleta.play()
                    self.ball.speedx *= -1  # invertir dirección de la pelota

                # verificar si alguien ha ganado
                if self.ball.left_score == 3 or self.ball.right_score == 3:
                    self.game_over = True
                    if self.ball.left_score == 3:
                        ganaste.play()
                        self.mostrar_imagen("¡Ganaste!")
                    else:
                        perdiste.play()
                        self.mostrar_imagen("Perdiste")

            self.all_list_sprite.update()

        def mostrar_imagen(self, mensaje):
            # mostrar mensaje en pantalla
            text_surface = self.font.render(mensaje, True, self.white)
            text_rect = text_surface.get_rect(center=(self.screen_width // 3, self.screen_height // 2 - 50))
            self.screen.blit(text_surface, text_rect)
            self.restart_button.draw()
            pygame.display.update()

        def reset_game(self):
            # meiniciar el juego
            ganaste.stop()
            perdiste.stop()
            self.game_over = False
            self.ball.left_score = 0
            self.ball.right_score = 0
            self.ball.reset_position()

        def display_frame(self):
            # mostrar los elementos del juego en cada frame
            if not self.game_over:
                self.screen.blit(self.background_image, (0, 0))  # Dibuja el fondo
                self.all_list_sprite.draw(self.screen)  # Dibuja todos los sprites

                # dibujar línea divisoria
                pygame.draw.aaline(self.screen, self.white, (self.screen_width // 2, 0), (self.screen_width // 2, self.screen_height))

                # mostrar puntuaciones
                left_text = self.font.render("Tu = " + str(self.ball.left_score), True, self.white)
                self.screen.blit(left_text, (self.screen_width // 5, 20))
                right_text = self.font.render("PC = " + str(self.ball.right_score), True, self.white)
                self.screen.blit(right_text, (self.screen_width // 4 * 3, 20))
                pygame.display.update()

    # clase Raqueta para manejar las paletas
    class Raqueta(pygame.sprite.Sprite):
        def __init__(self, paddel, paddle_width, paddle_height, screen_height):
            super().__init__()
            self.screen_height = screen_height
            self.paddle_width = paddle_width
            self.paddle_height = paddle_height
            self.image = pygame.image.load("tablar.png").convert()
            self.image = pygame.transform.scale(self.image, (self.paddle_width, self.paddle_height))
            self.image.set_colorkey([0, 0, 0])
            self.rect = self.image.get_rect()
            self.rect.y = (self.screen_height - self.paddle_height) // 2
            self.rect.x = paddel

        def update(self):
            # limitar el movimiento de las paletas dentro de los bordes de la pantalla
            if self.rect.y < 0:
                self.rect.y = 0
            if self.rect.y > (self.screen_height - self.paddle_height):
                self.rect.y = self.screen_height - self.paddle_height

    # clase Pelota para manejar la lógica de la pelota
    class Pelota(pygame.sprite.Sprite):
        def __init__(self, left_score, right_score, screen_height, screen_width):
            super().__init__()
            self.screen_height = screen_height
            self.screen_width = screen_width
            self.ballzc = 45
            self.speedx = 17
            self.speedy = 16
            self.left_score = left_score
            self.right_score = right_score
            self.image = pygame.image.load("pelota.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.ballzc, self.ballzc))
            self.image.set_colorkey([255, 255, 255])
            self.rect = self.image.get_rect()
            self.rect.x = (self.screen_width - self.ballzc) // 2
            self.rect.y = (self.screen_height - self.ballzc) // 2

        def update(self):
            # actualizar la posición de la pelota
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            # Colisión con los bordes superior e inferior
            if self.rect.top <= 0 or self.rect.bottom >= self.screen_height:
                glope_bordes.play()
                self.speedy *= -1
            # colisión con los bordes izquierdo y derecho
            if self.rect.left <= 0:
                self.speedx *= -1
                self.right_score += 1
                self.reset_position()
            if self.rect.right >= self.screen_width:
                self.speedx *= -1
                self.left_score += 1
                self.reset_position()

        def reset_position(self):
            # reiniciar la posición de la pelota
            self.rect.x = (self.screen_width - self.ballzc) // 2
            self.rect.y = (self.screen_height - self.ballzc) // 2

    # función principal para iniciar el juego
    def main():
        pygame.init()
        screen_width = 1200
        screen_height = 800
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Ping Pong")
        background_image = pygame.image.load("mesa verde.png")
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
        running = True
        clock = pygame.time.Clock()
        game = Juego(screen, screen_width, screen_height, background_image)
        while running:
            running = game.eventos_proceso()
            game.logica()
            game.display_frame()
            clock.tick(60)
        pygame.quit()
        sys.exit()

    if __name__ == "__main__":
        main()

  
def A_vs_B():
       # clase principal para manejar la lógica y la interfaz del juego
    class Juego(object):
        def __init__(self, screen, screen_width, screen_height, background_image, a, b):
            # inicialización de propiedades del juego
            self.screen = screen
            self.screen_width = screen_width
            self.screen_height = screen_height
            self.background_image = background_image
            self.a = a # jugador a 
            self.b = b # jugador b
            self.font = pygame.font.Font(None, 74)
            self.white = (255, 255, 255)

            # iniciarlizar el juego
            self.init_game()

        def init_game(self):
            # estado inicial del juego
            self.game_over = False
            self.left_score = 0 # pundos de a
            self.right_score = 0 # puntos del jugador b

            #grupos de sprites
            self.all_list_sprite = pygame.sprite.Group()
            self.raqt = pygame.sprite.Group()
            self.paddle_height = 190
            self.player1 = Raqueta(50, 50, self.paddle_height, self.screen_height)
            self.player2 = Raqueta(self.screen_width - 50 - self.player1.paddle_width, 50, self.paddle_height, self.screen_height)
            self.ball = Pelota(self.left_score, self.right_score, self.screen_height, self.screen_width)
            self.raqt.add(self.player1)
            self.raqt.add(self.player2)
            self.all_list_sprite.add(self.ball)
            self.all_list_sprite.add(self.raqt)

        def eventos_proceso(self):
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    return False  # salir del juego si se cierra la ventana
                if event.type == pygame.KEYDOWN and self.game_over:
                    if event.key == pygame.K_SPACE:
                        self.init_game()
            return True

        def mostrar_ventana_ganador(self, winner):
            #  ventana para el ganador
            ganaste.play()
            ventana_ganador = Toplevel()
            ventana_ganador.title("Ganaste")

            # Cargar la imagen
            imagen_ganaste = PhotoImage(file="ganaste.png")

            # Crear un widget de etiqueta para mostrar la imagen
            etiqueta_imagen = Label(ventana_ganador, image=imagen_ganaste)
            etiqueta_imagen.pack()

            # Crear un widget de etiqueta para mostrar el texto del ganador
            etiqueta_texto = Label(ventana_ganador, text=winner, font=("Arial", 24))
            etiqueta_texto.pack()

            # Botón de reinicio
            boton_reiniciar = Button(ventana_ganador, text="Reiniciar", command=lambda: self.reiniciar_juego(ventana_ganador))
            boton_reiniciar.pack()

            # Mantener una referencia a la imagen para evitar que se recoja basura
            etiqueta_imagen.image = imagen_ganaste

            ventana_ganador.wait_window()

        def reiniciar_juego(self, ventana_ganador):
            ganaste.stop()
            ventana_ganador.destroy()
            self.init_game()

        def logica(self):
            # logica basica del juego
            if not self.game_over:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                    self.player1.rect.y -= 14
                if keys[pygame.K_s]:
                    self.player1.rect.y += 14
                if keys[pygame.K_UP]:
                    self.player2.rect.y -= 15
                if keys[pygame.K_DOWN]:
                    self.player2.rect.y += 15
                #colisiones de la de la pelota y la paleta
                if pygame.sprite.collide_mask(self.ball, self.player1):
                    self.ball.speedx += 2
                    self.ball.speedx *= -1
                    golpe_paleta.play()
                if pygame.sprite.collide_mask(self.ball, self.player2):
                    self.ball.speedx += 2
                    self.ball.speedx *= -1
                    golpe_paleta.play()

                self.all_list_sprite.update()
                
                # para verificar quien gana
                if self.ball.left_score == 3 or self.ball.right_score == 3:
                    self.game_over = True
                    winner = self.a if self.ball.left_score == 3 else self.b
                    self.mostrar_ventana_ganador(f"{winner} Gana")

        def display_frame(self):
            # pa mostrar los elementos en los frame
            self.screen.blit(self.background_image, (0, 0))
            self.all_list_sprite.draw(self.screen)
            
            pygame.draw.aaline(self.screen, self.white, (self.screen_width // 2, 0), (self.screen_width // 2, self.screen_height))

            left_text = self.font.render(f"{self.a} = " + str(self.ball.left_score), True, self.white)
            self.screen.blit(left_text, (self.screen_width // 5, 20))
            right_text = self.font.render(f"{self.b} = " + str(self.ball.right_score), True, self.white)
            self.screen.blit(right_text, (self.screen_width // 4 * 3, 20))
            pygame.display.update()

    class Raqueta(pygame.sprite.Sprite):
        def __init__(self, paddel, paddle_width, paddle_height, screen_height):
            super().__init__()
            self.screen_height = screen_height
            self.paddle_width = paddle_width
            self.paddle_height = paddle_height
            self.image = pygame.image.load("tablar.png").convert()
            self.image = pygame.transform.scale(self.image, (self.paddle_width, self.paddle_height))
            self.image.set_colorkey([0, 0, 0])
            self.rect = self.image.get_rect()
            self.rect.y = (self.screen_height - self.paddle_height) // 2
            self.rect.x = paddel

        def update(self):
            if self.rect.y < 0:
                self.rect.y = 0
            if self.rect.y > (self.screen_height - self.paddle_height):
                self.rect.y = self.screen_height - self.paddle_height

    class Pelota(pygame.sprite.Sprite):
        def __init__(self, left_score, right_score, screen_height, screen_width):
            super().__init__()
            self.screen_height = screen_height
            self.screen_width = screen_width
            self.ballzc = 50
            self.speedx = 20
            self.speedy = 20
            self.left_score = left_score
            self.right_score = right_score
            self.image = pygame.image.load("pelota.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.ballzc, self.ballzc))
            self.image.set_colorkey([255, 255, 255])
            self.rect = self.image.get_rect()
            self.rect.x = (self.screen_width - self.ballzc) // 2
            self.rect.y = (self.screen_height - self.ballzc) // 2

        def update(self):
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            if self.rect.top <= 0 or self.rect.bottom >= self.screen_height:
                glope_bordes.play()
                self.speedy *= -1
            if self.rect.left <= 0:
                self.speedx *= -1
                self.right_score += 1
                self.reset_position()
            if self.rect.right >= self.screen_width:
                self.speedx *= -1
                self.left_score += 1
                self.reset_position()

        def reset_position(self):
            self.rect.x = (self.screen_width - self.ballzc) // 2
            self.rect.y = (self.screen_height - self.ballzc) // 2

    def main():
        a = usuario_1.get()
        b = usuario_2.get()
        if a == "" or b == "":
            messagebox.showerror("Campo Vacio", "Ingrese el nombre de los jugadores")
        else:
            pygame.init()
            intro_juego.stop()
            screen_width = 1200
            screen_height = 800
            screen = pygame.display.set_mode((screen_width, screen_height))
            pygame.display.set_caption("Ping Pong")

            background_image = pygame.image.load("mesa azul.png")
            background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

            running = True
            clock = pygame.time.Clock()
            game = Juego(screen, screen_width, screen_height, background_image, a, b)
            while running:
                running = game.eventos_proceso()
                game.logica()
                game.display_frame()
                clock.tick(60)
            pygame.quit()
            sys.exit()

    if __name__ == "__main__":
        root = Tk()
        root.withdraw()
        main()


### la interfaz grafica principal
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
sys.exit()
intro.stop()
