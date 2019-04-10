"""
Instituto Tecnológico de Costa Rica
Ingeniería en Computadores
Taller de Programación
I Semestre, 2019

José Julián Camacho Hernández
2019201459

Proyecto #1: Rowser Castle

Python 3.7.2
Pygame 1.9.4
"""

#Importar módulos necesarios
import pygame
import time
import random

#Definir dimensiones de la ventana y frames por segundo de actualización de pantalla
displayWidth = 600
displayHeight = 600
FPS = 32

pygame.init() #Inicializar PyGame
pygame.mixer.init()
#Definir colores
transColor_mario = pygame.Color(149,83,125)
transColor_menu = pygame.Color(157,157,157)


###   ========== o ==========  Pantalla Principal ========= o ==========  ###

def Principal():
    displayFlag = True
    
    game_display = pygame.display.set_mode((displayWidth, displayHeight)) #Dar dimensiones que están definidas antes, es un solo argumento, una sola tupla
    pygame.display.set_caption("Rowser Castle") #Dar nombre a la ventana
    clock = pygame.time.Clock() #Reloj del juego, llevar el tiempo de todo, sobre todo con FPS

    princ_music = pygame.mixer.music.load("BowserBoss2.mp3")
    pygame.mixer.music.play(5, 0.0)
    pygame.mixer.music.rewind()

    #Diferentes pantallas
    gameScreen1 = PantallaJuego1(game_display)
    gameScreen2 = PantallaJuego2(game_display)
    gameScreen3 = PantallaJuego3(game_display)
    menuScreen = PantallaMenu(game_display, gameScreen1)
    scoreScreen = SalonFama(game_display, gameScreen1)
    settingScreen = Settings(game_display, gameScreen1)

    #Loop del juego
    
    while displayFlag:
        for event in pygame.event.get(): #Para un evento en PyGame
            if event.type == pygame.QUIT: #Para cerrar la ventana
                displayFlag = False #Para cerrar el ciclo

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #Salir al menú
                    gameScreen1.flag = False
                    gameScreen2.flag = False
                    gameScreen3.flag = False
                    menuScreen.flag = True
                    
                if event.key == pygame.K_p or event.key == pygame.K_1: #Ir al primer nivel
                    gameScreen1.flag = True
                    menuScreen.flag = False
                    
                if event.key == pygame.K_c or event.key == pygame.K_2: #Ir al segundo nivel
                    gameScreen1.flag = False
                    gameScreen2.flag = True
                    gameScreen3.flag = False
                    menuScreen.flag = False
                    
                if event.key == pygame.K_g or event.key == pygame.K_3: #Ir al tercer nivel
                    gameScreen1.flag = False
                    gameScreen2.flag = False
                    gameScreen3.flag = True
                    menuScreen.flag = False

                if event.key == pygame.K_t: #Ir a la configuración
                    settingScreen.flag = True
                    scoreScreen.flag = False
                    menuScreen.flag = False
                    
                if event.key == pygame.K_h: #Ir al salón de la fama
                    scoreScreen.flag = True
                    menuScreen.flag = False
                    settingScreen.flag = False
                    
                if event.key == pygame.K_m: #Pausar la música
                    pygame.mixer.music.pause()
                elif event.key == pygame.K_n: #Reanudar la música
                    pygame.mixer.music.unpause()
                    
        #Para cuando cada ventana esté activa
            if gameScreen1.flag:
                gameScreen1.events(event)
            if gameScreen2.flag:
                gameScreen2.events(event)
            if gameScreen3.flag:
                gameScreen3.events(event)
                
        if menuScreen.flag:
            menuScreen.__update__() 
            menuScreen.__draw__()
        elif gameScreen1.flag:
            gameScreen1.__update__()
            gameScreen1.__draw__()
        elif gameScreen2.flag:
            gameScreen2.__update__()
            gameScreen2.__draw__()
        elif gameScreen3.flag:
            gameScreen3.__update__()
            gameScreen3.__draw__()
        elif settingScreen.flag:
            settingScreen.__draw__()
        elif scoreScreen.flag:
            scoreScreen.__draw__()
        

        pygame.display.flip() #Actualizar todo 
        clock.tick(FPS) #FPS en que se va a ir actualizando

# Función de dibujar textos en la pantalla
font_name = pygame.font.match_font("arial")
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)



###  =========== o ==========  Pantalla de Menú  ========== o ===========   ###

class PantallaMenu: #Clase Menú
    def __init__(self, game_display, gameScreen1): #Atributos
        self.frame = game_display
        self.gameScreen = gameScreen1
        self.flag = True

        #Sprite del título
        self.spriteMenu = pygame.image.load("images/menutitle.png")
        self.spriteMenu.set_clip(8, 3, 416, 164)
        title1 = self.spriteMenu.subsurface(self.spriteMenu.get_clip()).convert()
        title1.set_colorkey((0, 0, 0))
        self.spriteMenu.set_clip(13, 174, 416, 164)
        title2 = self.spriteMenu.subsurface(self.spriteMenu.get_clip()).convert()
        title2.set_colorkey((0, 0, 0))
        self.spriteMenu.set_clip(13, 338, 416, 164)
        title3 = self.spriteMenu.subsurface(self.spriteMenu.get_clip()).convert()
        title3.set_colorkey((0, 0, 0))
        self.title = [title1, title2, title1, title3]

        self.sprite = self.title
        self.sprite_index = 0
        self.rect = pygame.Rect(100, 100, 142, 135) 
        
    def __update__(self): #Ir actualizando 
        self.sprite = self.title

    def __draw__(self): #Dibujar imágenes y texto en la pantalla
        imagenfondo_menu = pygame.image.load("images/CastleMenu.png")
        self.frame.blit(imagenfondo_menu, (0,0))

        draw_text(self.frame, ("Developed by José Julián Camacho Hernández"), 16, 450, 10)
        draw_text(self.frame, ("Hall of Fame"), 15, 40, 180)
        
        imagen_bow = pygame.image.load("images/Bowser (1).png")
        self.frame.blit(imagen_bow, (0,360))
        imagen_bow.set_colorkey((255, 255, 255))

        imagen_start = pygame.image.load("images/p.png")
        self.frame.blit(imagen_start, (298,460))
        imagen_start.set_colorkey((255, 255, 255))

        imagen_settings = pygame.image.load("images/settings1.png")
        self.frame.blit(imagen_settings, (10,10))
        imagen_start.set_colorkey((255, 255, 255))

        imagen_t = pygame.image.load("images/t.png")
        self.frame.blit(imagen_t, (-1,33))
        imagen_start.set_colorkey((255, 255, 255))

        imagen_hall = pygame.image.load("images/throne2.png")
        self.frame.blit(imagen_hall, (10,95))
        imagen_start.set_colorkey((255, 255, 255))

        imagen_h = pygame.image.load("images/h.png")
        self.frame.blit(imagen_h, (-1,130))
        imagen_start.set_colorkey((255, 255, 255))

        self.sprite = self.__get_sprite__(self.title)
        self.frame.blit(self.sprite, (100, 100))
        time.sleep(0.25)

    #Para recorrer la lista de los sprites   
    def __get_sprite__(self, sprites):
        self.sprite_index += 1
        if self.sprite_index >= (len(sprites)):
            self.sprite_index = 0
        return sprites[self.sprite_index]


###  ========== o =========  Configuración  ========== o ==========  ###

class Settings:
    def __init__(self, game_display, gameScreen1): #Atributos
        self.frame = game_display
        self.gameScreen = gameScreen1
        self.flag = True
            
    def __draw__(self):
        imagen_setti = pygame.image.load("images/SettingMenu.png")
        self.frame.blit(imagen_setti, (0,0))
        

###  ========== o =========  Salón de la Fama  ========== o ==========  ###

class SalonFama:
    def __init__(self, game_display, gameScreen1): #Atributos
        self.frame = game_display
        self.gameScreen = gameScreen1
        self.flag = True            

    def __draw__(self):
        imagenfondo_salon = pygame.image.load("images/salon4.png")
        self.frame.blit(imagenfondo_salon, (0,0))

        #Leer diferentes líneas en el archivo de texto
        with open("SalonFama.txt", "r") as f:
            n1 = f.readline()  
            n2 = f.readline()
            n3 = f.readline()
            n4 = f.readline()

        #Dibujar las líneas del archivo   
        draw_text(self.frame, ("Hall of Fame"), 70, 300, 90)
        draw_text(self.frame, (n1), 50, 300, 500)
        draw_text(self.frame, (n2), 50, 300, 400)
        draw_text(self.frame, (n3), 50, 300, 300)
        draw_text(self.frame, (n4), 50, 300, 200)


        
###   ========== o ==========  Player   ========== o ==========  ###
        
class Player:
    def __init__(self, x, y): #Atributos

        #Ubicacón de sprites
        self.spriteSheet = pygame.image.load("images/mario2.png")

        # Sprite Standing
        self.spriteSheet.set_clip(55, 34, 18, 30)
        self.standing = self.spriteSheet.subsurface(self.spriteSheet.get_clip()).convert()
        self.standing.set_colorkey(transColor_mario)

        #Sprite Walking
        self.spriteSheet.set_clip(55, 82, 18, 30)
        walking1 = self.spriteSheet.subsurface(self.spriteSheet.get_clip()).convert()
        walking1.set_colorkey(transColor_mario)
        self.spriteSheet.set_clip(82, 81, 26, 30)
        walking2 = self.spriteSheet.subsurface(self.spriteSheet.get_clip()).convert()
        walking2.set_colorkey(transColor_mario)
        self.spriteSheet.set_clip(117, 82, 20, 30)
        walking3 = self.spriteSheet.subsurface(self.spriteSheet.get_clip()).convert()
        walking3.set_colorkey(transColor_mario)
        self.spriteSheet.set_clip(152, 81, 17, 30)
        walking4 = self.spriteSheet.subsurface(self.spriteSheet.get_clip()).convert()
        walking4.set_colorkey(transColor_mario)
        self.spriteSheet.set_clip(179, 81, 25, 29)
        walking5 = self.spriteSheet.subsurface(self.spriteSheet.get_clip()).convert()
        walking5.set_colorkey(transColor_mario)
        self.spriteSheet.set_clip(215, 82, 19, 30)
        walking6 = self.spriteSheet.subsurface(self.spriteSheet.get_clip()).convert()
        walking6.set_colorkey(transColor_mario)
        self.walking = [walking1, walking2, walking3, walking4, walking5, walking6]

        self.sprite = self.standing
        self.sprite_index = 0
        self.rect = self.sprite.get_rect()
        self.rect.topleft = (x,y)
        self.action = 'standing' #Acción que realiza
        self.direction = 'right' #Dirección
        self.falling = True #Aplicación de gravedad
        self.jump = 0 #Salto 

    def __update__(self):
        if self.action == "standing":
            if self.direction == "left":
                sel = self.standing
                self.sprite = pygame.transform.flip(self.sprite, True, False)
            elif self.direction == "right":
                self.sprite = self.standing
             
        #Actualizarse dependiendo de la dirección del movimiento
        elif self.action == 'walking': 
            if self.direction == 'left': 
                self.rect.left -= 3
                self.sprite = self.__get_sprite__(self.walking)
                self.sprite = pygame.transform.flip(self.sprite, True, False)
            elif self.direction == 'right':
                self.rect.left += 3
                self.sprite = self.__get_sprite__(self.walking)      
            if self.direction == 'up': 
                self.rect.top -= 5
                self.sprite = self.__get_sprite__(self.walking)
                self.sprite = pygame.transform.flip(self.sprite, True, False)
            elif self.direction == 'down':
                self.rect.top += 1
                self.sprite = self.__get_sprite__(self.walking)
        
        #Actualizarse dependiendo del movimiento vertical (salto y gravedad)
        if self.falling and self.jump <= 0:
            self.rect.top += 3
        elif self.jump > 0:
            self.rect.top -= 3
            self.jump -= 3
            
    def __draw__(self, game_display): #Dinujar sprites según el movimiento
        if self.action == "standing":
            game_display.blit(self.sprite, (self.rect.left, self.rect.top))

        elif self.action == 'walking':
            if self.direction == 'left':
                game_display.blit(self.sprite, (self.rect.left, self.rect.top))
            elif self.direction == 'right':
                game_display.blit(self.sprite, (self.rect.left, self.rect.top))
            elif self.direction == 'up':
                game_display.blit(self.sprite, (self.rect.left, self.rect.top))
            elif self.direction == 'down':
                game_display.blit(self.sprite, (self.rect.left, self.rect.top))
                
    #Recorrer la lista de sprites           
    def __get_sprite__(self, sprites):
        self.sprite_index += 1
        if self.sprite_index >= (len(sprites)):
            self.sprite_index = 0
        return sprites[self.sprite_index]




###   ========== o ==========  Enemigo  =========== o ==========  ###
    
class Fuego:
    def __init__(self): #Atributos
        self.rect = pygame.Rect(30, 100, 17, 27) #Dimensiones del rectángulo
        self.speed = (random.randint(-5, 5), random.randint(-5, 5)) #Velocidad y dirección aleatoria de los enemigos

        #Sprite (imagen)
        self.spriteFire = pygame.image.load("images/fueguito.png")
        self.spriteFire.set_clip(1, 4, 17, 27)
        self.standing = self.spriteFire.subsurface(self.spriteFire.get_clip()).convert()
        self.standing.set_colorkey((255, 255, 255))
        
    def __update__(self): #Actualizar
        #Ir aumentando la cantidad de pixeles generados en la speed
        self.sprite = self.standing
        self.rect.left += self.speed[0]
        self.rect.top += self.speed[1]

        #Comportamiento del movimiento de los enemigos
        if self.rect.left < -40:
            self.rect.left = 600
        elif self.rect.left > 600:
            self.rect.left = 40
        if self.rect.top < -40:
            self.rect.top = 600
        elif self.rect.top > 600:
            self.rect.top = -40

    def __draw__(self, game_display):
        game_display.blit(self.sprite, self.rect)




###   ========== o ==========   Boss   ========== o ==========  ###

class Boss:
    def __init__(self):
        self.rect = pygame.Rect(30, 100, 74, 90)
        #Sprite (imagen)
        self.spriteBoss = pygame.image.load("images/Bowser (2).png")
        self.spriteBoss.set_clip(1, 0, 74, 90)
        self.boss = self.spriteBoss.subsurface(self.spriteBoss.get_clip()).convert()
        self.boss.set_colorkey((0, 0, 0))
    
    def __update__(self):
        self.sprite = self.boss

    def __draw__(self, game_display):
        game_display.blit(self.boss, self.rect)
        


###  ========== o ==========  Princess  ========== o ==========  ###

class Princess:
    def __init__(self):
        self.rect = pygame.Rect(130, 70, 19, 31)
        #Sprite (imagen)
        self.spritePrin = pygame.image.load("images/rosalina.png")
        self.spritePrin.set_clip(3, 1, 19, 31)
        self.prin = self.spritePrin.subsurface(self.spritePrin.get_clip()).convert()
        self.prin.set_colorkey((0, 136, 255))
    
    def __update__(self):
        self.sprite = self.prin

    def __draw__(self, game_display):
        game_display.blit(self.prin, self.rect)
        

###  ========== o ==========  Plant  ========== o ==========  ###

class Plant:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 21, 20)
        #Sprite (imagen)
        self.spritePlant = pygame.image.load("images/Planta.png")
        self.spritePlant.set_clip(0, 1, 23, 22)
        self.plant = self.spritePlant.subsurface(self.spritePlant.get_clip()).convert()
        self.plant.set_colorkey((0,164,0))
    
    def __update__(self):
        self.sprite = self.plant

    def __draw__(self, game_display):
        game_display.blit(self.plant, self.rect)
        
                    
        
###  ========== o ==========   Escaleras  ========== o ==========  ###

class Ladder:
    def __init__(self, x, y, height):
        self.rect = pygame.Rect(x, y, 20, height)

        self.spriteLadder = pygame.image.load("images/ladder2.png")
        self.spriteLadder.set_clip(0, 0, 20, 130)
        self.ladd = self.spriteLadder.subsurface(self.spriteLadder.get_clip()).convert()
        self.ladd.set_colorkey((0, 0,0))

    def __draw__(self, game_display):
        game_display.blit(self.ladd, self.rect)

        
        
###  ========== o ==========   Plataformas  ========== o ==========  ###

class Plataforma:
    def __init__(self, x, y): #Atributos
        self.rect = pygame.Rect(x, y, 50, 25)
        
        #Sprite (imagen)
        self.spritePlat = pygame.image.load("images/plat.png")
        self.spritePlat.set_clip(0, 0, 50, 25)
        self.brick = self.spritePlat.subsurface(self.spritePlat.get_clip()).convert()
        self.brick.set_colorkey((255, 255, 255))

    def __draw__(self, game_display):
        pygame.draw.rect(game_display, (0, 0, 0), self.rect)
        game_display.blit(self.brick, self.rect)

        
    
###  ========== o ==========  Nivel 1  ========== o ==========   ###
  
        
class PantallaJuego1:     
    def __init__(self, game_display): #Atributos
        self.frame = game_display
        self.player = Player(100, 460)
        self.platforms = [Plataforma(300, 174), Plataforma(460, 174), Plataforma(510, 174), Plataforma(0, 300), Plataforma(50, 300), Plataforma(100, 300), Plataforma(150, 300), Plataforma(183, 300), Plataforma(340, 300), Plataforma(439, 300), Plataforma(489, 300), Plataforma(500, 300), Plataforma(550, 300), Plataforma(120, 97), Plataforma(0, 181), Plataforma(50, 181), Plataforma(100, 181), Plataforma(150, 181), Plataforma(0, 424), Plataforma(50, 424), Plataforma(100, 424), Plataforma(138, 424), Plataforma(188, 424), Plataforma(238, 424), Plataforma(274, 424), Plataforma(413, 424), Plataforma(463, 424), Plataforma(513, 424), Plataforma(550, 424), Plataforma(0, 550), Plataforma(50, 550), Plataforma(100, 550), Plataforma(150, 550), Plataforma(200, 550), Plataforma(250, 550), Plataforma(300, 550), Plataforma(350, 550), Plataforma(400, 550), Plataforma(450, 550), Plataforma(500, 550), Plataforma(550, 550)]
        self.enemies = [Fuego(), Fuego(), Fuego(), Fuego(), Fuego(), Fuego()]
        self.ladders = [Ladder(570, 424, 124), Ladder(175, 300, 124), Ladder(500, 174, 124)]
        self.bosses = [Boss()]
        self.princesses = [Princess()]
        self.plants = [Plant(570, 580), Plant(350, 530), Plant(50, 402), Plant(175, 450), Plant(500, 327), Plant(25, 278), Plant(570, 330), Plant(175, 213), Plant(137, 213), Plant(100, 213), Plant(500, 80), Plant(410, 140), Plant(250, 140)]
        self.flag = False
        self.score = 0
        self.lives = 15
        self.win = 0
        self.load_data()

    def load_data(self):
        #Cargar el highscore
        with open ("HighScore.txt", "w") as g:
            try:
                self.highscore = init(g.read())
            except:
                self.highscore = 0
                
    def respawn(self):
        self.player = Player(100, 460)
    
    def __update__(self):
        # Gravedad en plataformas
        self.player.falling = True
        for platform in self.platforms:
            if self.player.rect.colliderect(platform.rect):
                self.player.falling = False
                break
        self.player.__update__()
        # Al colisionar contra enemigos
        for enemy in self.enemies:
            enemy.__update__()
            if self.player.rect.colliderect(enemy.rect):
                self.respawn()
                self.lives -= 1        
        # Al colisionar contra escaleras
        for ladder in self.ladders:
            if self.player.rect.colliderect(ladder.rect):
                self.player.direction == "none"
        self.player.__update__()
        #Al llegar a la princesa
        for princess in self.princesses:
            princess.__update__()
            if self.player.rect.colliderect(princess.rect):
                self.score += 1000
                self.win += 1
        #Al colisionar contra plantas enemigas       
        for plant in self.plants:
            plant.__update__()
            if self.player.rect.colliderect(plant.rect):
                self.respawn()
                self.lives -= 1
        #Al colisionar contra Rowser       
        for boss in self.bosses:
            boss.__update__()
            if self.player.rect.colliderect(boss.rect):
                self.respawn()
                self.lives -= 5
        #Puntaje
        if self.player.rect.top < 200:
            self.score = 1000
        elif self.player.rect.top < 300:
            self.score = 500
        elif self.player.rect.top < 424:
            self.score = 250

        #Para guardar un puntaje alto
        if self.score > self.highscore:
            self.highscore = self.score
            with open("HighScore.txt", "w") as g:
                g.write(str(self.score)) 
            with open ("SalonFama.txt", "a") as f:
                f.write("Mario: " + str(self.score) + "\n")
            
    def __draw__(self): #Dibujar imagen de fondo, textos de puntaje y vidas, y dibujar los obstáculos
        imagenfondo_juego = pygame.image.load("images/fondoCastle.png")
        self.frame.blit(imagenfondo_juego, (0,0))

        draw_text(self.frame, ("Score" + ":  " + str(self.score)), 24, 500, 10)
        draw_text(self.frame, ("Lives" + ":  " + str(self.lives)), 24, 500, 35)
        draw_text(self.frame, ("Highscore" + ":  " + str(self.highscore)), 24, 500, 60)    

        self.player.__draw__(self.frame)
        for platform in self.platforms:
            platform.__draw__(self.frame)
        self.player.__draw__(self.frame)
        for enemy in self.enemies:
            enemy.__draw__(self.frame)
        for ladder in self.ladders:
            ladder.__draw__(self.frame)
        for boss in self.bosses:
            boss.__draw__(self.frame)
        for princess in self.princesses:
            princess.__draw__(self.frame)
        self.player.__draw__(self.frame)
        for plant in self.plants:
            plant.__draw__(self.frame)

        #Imágenes que se presemtan si se gana o se pierde
        if self.lives < 0:
            imagen_over = pygame.image.load("images/gameover1.png")
            self.frame.blit(imagen_over, (0,0))
        if self.win >= 1:
            imagen_next = pygame.image.load("images/win1.png")
            self.frame.blit(imagen_next, (0,0))
        
    def events(self, event): #Teclas de funcionamiento
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.player.action = 'walking'
                self.player.direction = 'left'
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d: 
                self.player.action = 'walking'
                self.player.direction = 'right'
            elif event.key == pygame.K_SPACE and self.player.jump <= 0 and not self.player.falling:
                self.player.jump = 75
            elif event.key == pygame.K_r:
                self.respawn()
            if self.lives < 0 and event.key == pygame.K_y:
                self.respawn()
                self.lives = 15
                self.score = 0
            for ladder in self.ladders:
                if (event.key == pygame.K_UP or event.key == pygame.K_w) and self.player.rect.colliderect(ladder.rect) == True:
                    self.player.action = "walking"
                    self.player.direction = "up"
            for ladder in self.ladders:
                if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and self.player.rect.colliderect(ladder.rect)== True:
                    self.player.action = "walking"
                    self.player.direction = "down"                

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.player.action = 'standing'
                self.player.direction = 'left'
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.player.action = 'standing'
                self.player.direction = 'right'
            for ladder in self.ladders:
                if event.key == pygame.K_UP and self.player.rect.colliderect(ladder.rect) == True:
                    self.player.action = 'standing'
                    self.player.direction = "up"
            for ladder in self.ladders:
                if event.key == pygame.K_DOWN and self.player.rect.colliderect(ladder.rect) == True:
                    self.player.action = 'standing'
                    self.player.direction = "down"




###  ========== o ==========   Nivel 2   ========== o ==========   ###


class PantallaJuego2:
    def __init__(self, game_display): #Atributos
        self.frame = game_display
        self.player = Player(500, 500)
        self.platforms = [Plataforma(300, 174), Plataforma(425, 174), Plataforma(550, 174), Plataforma(0, 310), Plataforma(50, 310), Plataforma(100, 310), Plataforma(150, 310), Plataforma(200, 310), Plataforma(310, 310), Plataforma(390, 310), Plataforma(489, 310), Plataforma(500, 310), Plataforma(550, 310), Plataforma(120, 97), Plataforma(0, 181), Plataforma(50, 181), Plataforma(100, 181), Plataforma(150, 181), Plataforma(0, 444), Plataforma(50, 444), Plataforma(100, 444), Plataforma(238, 444), Plataforma(274, 444), Plataforma(450, 444), Plataforma(500, 444), Plataforma(550, 444), Plataforma(0, 570), Plataforma(50, 570), Plataforma(100, 570), Plataforma(150, 570), Plataforma(250, 570), Plataforma(300, 570), Plataforma(350, 570), Plataforma(450, 570), Plataforma(500, 570), Plataforma(550, 570)]
        self.enemies = [Fuego(),Fuego(), Fuego(), Fuego(), Fuego(), Fuego()]
        self.ladders = [Ladder(80, 444, 124), Ladder(175, 320, 124), Ladder(490, 320, 124), Ladder(570, 184, 124), Ladder(315, 184, 124)]
        self.bosses = [Boss()]
        self.princesses = [Princess()]
        self.plants = [Plant(80, 365), Plant(80, 573), Plant(350, 530), Plant(50, 422), Plant(175, 450), Plant(480, 474), Plant(555, 422), Plant(365, 400), Plant(20, 287),Plant(50, 287), Plant(230, 287), Plant(260, 287), Plant(170, 230), Plant(200, 287), Plant(80, 287), Plant(140, 287), Plant(110, 287), Plant(420, 287), Plant(390, 287), Plant(0, 287), Plant(490, 230), Plant(310, 320), Plant(570, 320), Plant(570, 93), Plant(310, 93), Plant(388, 140), Plant(388, 164), Plant(250, 140), Plant(250, 164)]
        self.flag = False
        self.score = 11750
        self.lives = 10
        self.win = 0
        self.load_data()

    #Cargar el highscore
    def load_data(self): 
        with open ("HighScore.txt", "w") as g:
            try:
                self.highscore = init(g.read())
            except:
                self.highscore = 0
        
    def respawn(self):
        self.player = Player(500, 500)
    
    def __update__(self):
        # Gravedad
        self.player.falling = True
        for platform in self.platforms:
            if self.player.rect.colliderect(platform.rect):
                self.player.falling = False
                break
        self.player.__update__() 
        # Enemigos
        for enemy in self.enemies:
            enemy.__update__()
            if self.player.rect.colliderect(enemy.rect):
                self.respawn()
                self.lives -= 1
        #Escaleras
        for ladder in self.ladders:
            if self.player.rect.colliderect(ladder.rect):
                self.player.direction == "none"
        self.player.__update__()
        #Princesa
        for princess in self.princesses:
            princess.__update__()
            if self.player.rect.colliderect(princess.rect):
                self.score += 10000
                self.win += 1  
        #Planta
        for plant in self.plants:
            plant.__update__()
            if self.player.rect.colliderect(plant.rect):
                self.respawn()
                self.lives -= 1
        #Jefe    
        for boss in self.bosses:
            boss.__update__()
            if self.player.rect.colliderect(boss.rect):
                self.respawn()
                self.lives -= 7
        #Puntaje
        if self.player.rect.top < 200:
            self.score = 20000
        elif self.player.rect.top < 300:
            self.score = 15000
        elif self.player.rect.top < 424:
            self.score = 11750
        #Guardar puntaje alto
        if self.score > self.highscore:
            self.highscore = self.score
            with open("HighScore.txt", "w") as g:
                g.write(str(self.score)) 
            with open ("SalonFama.txt", "a") as f:
                f.write("Mario: " + str(self.score) + "\n")
            
    def __draw__(self):
        imagenfondo_juego = pygame.image.load("images/fondoCastle.png")
        self.frame.blit(imagenfondo_juego, (0,0))

        draw_text(self.frame, ("Score" + ":  " + str(self.score)), 24, 500, 10)
        draw_text(self.frame, ("Lives" + ":  " + str(self.lives)), 24, 500, 35)
        draw_text(self.frame, ("Highscore" + ":  " + str(self.highscore)), 24, 500, 60)
        
        self.player.__draw__(self.frame)
        for platform in self.platforms:
            platform.__draw__(self.frame)
        self.player.__draw__(self.frame)
        for enemy in self.enemies:
            enemy.__draw__(self.frame)
        for ladder in self.ladders:
            ladder.__draw__(self.frame)
        for boss in self.bosses:
            boss.__draw__(self.frame)
        for princess in self.princesses:
            princess.__draw__(self.frame)
        self.player.__draw__(self.frame)
        for plant in self.plants:
            plant.__draw__(self.frame)
            
        #Imágenes que se presentan al ganar o perder
        if self.lives < 0:
            imagen_over = pygame.image.load("images/gameover1.png")
            self.frame.blit(imagen_over, (0,0))
        if self.win >= 1:
            imagen_next = pygame.image.load("images/win2.png")
            self.frame.blit(imagen_next, (0,0))

    def events(self, event): #Teclas de funcionamiento
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.player.action = 'walking'
                self.player.direction = 'left'
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.player.action = 'walking'
                self.player.direction = 'right'
            elif event.key == pygame.K_SPACE and self.player.jump <= 0 and not self.player.falling:
                self.player.jump = 75
            elif event.key == pygame.K_r:
                self.respawn()
            if self.lives < 0 and event.key == pygame.K_y:
                self.respawn()
                self.lives = 10
                self.score = 0
            for ladder in self.ladders:
                if (event.key == pygame.K_UP or event.key == pygame.K_w) and self.player.rect.colliderect(ladder.rect) == True:
                    self.player.action = "walking"
                    self.player.direction = "up"
            for ladder in self.ladders:
                if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and self.player.rect.colliderect(ladder.rect)== True:
                    self.player.action = "walking"
                    self.player.direction = "down"                

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.player.action = 'standing'
                self.player.direction = 'left'
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.player.action = 'standing'
                self.player.direction = 'right'
            for ladder in self.ladders:
                if event.key == pygame.K_UP and  self.player.rect.colliderect(ladder.rect) == True:
                    self.player.action = 'standing'
                    self.player.direction = "up"
            for ladder in self.ladders:
                if event.key == pygame.K_DOWN and self.player.rect.colliderect(ladder.rect) == True:
                    self.player.action = 'standing'
                    self.player.direction = "down"

                    
###   ========== o ==========  Nivel 3  ========== o ==========  ###

class PantallaJuego3:
    def __init__(self, game_display): #Atributos
        self.frame = game_display
        self.player = Player(30, 460)
        self.platforms = [Plataforma(385, 50), Plataforma(300, 174), Plataforma(460, 174), Plataforma(510, 174), Plataforma(0, 317), Plataforma(50, 317), Plataforma(250, 317),  Plataforma(485, 317), Plataforma(500, 317), Plataforma(550, 317), Plataforma(120, 97), Plataforma(0, 181), Plataforma(50, 181), Plataforma(100, 181), Plataforma(150, 181), Plataforma(50, 455), Plataforma(150, 455), Plataforma(275, 455), Plataforma(400, 455), Plataforma(500, 455), Plataforma(0, 590), Plataforma(100, 590), Plataforma(220, 590), Plataforma(330, 590), Plataforma(450, 590), Plataforma(550, 590)]
        self.enemies = [Fuego(),Fuego(), Fuego(), Fuego(), Fuego(), Fuego()]
        self.ladders = [Ladder(400, 50, 124), Ladder(175, 460, 124), Ladder(570, 445, 124), Ladder(25, 317, 124), Ladder(400, 354, 124), Ladder(300, 184, 124),  Ladder(570, 184, 124)]
        self.bosses = [Boss()]
        self.princesses = [Princess()]
        self.plants = [Plant(25, 430), Plant(570, 380), Plant(570, 575), Plant(350, 530), Plant(175, 450), Plant(500, 330), Plant(400, 480), Plant(330, 330), Plant(360, 330), Plant(390, 330), Plant(420, 330), Plant(419, -15), Plant(570, 330), Plant(10, 250), Plant(40, 230), Plant(70, 210), Plant(130, 210), Plant(100, 210), Plant(570, 100), Plant(400, 145), Plant(250, 140), Plant(250, 110), Plant(250, 80), Plant(303, 80), Plant(300, 325), Plant(350, 140), Plant(350, 110), Plant(350, 80), Plant(350, 50), Plant(222, 150), Plant(200, 160)]
        self.flag = False
        self.score = 30000
        self.lives = 5
        self.win = 0
        self.load_data()
    
    #Cargar el highscore
    def load_data(self):
        with open ("HighScore.txt", "w") as g:
            try:
                self.highscore = init(g.read())
            except:
                self.highscore = 0
        
    def respawn(self):
        self.player = Player(30, 460)
    
    def __update__(self):
        # Gravedad
        self.player.falling = True
        for platform in self.platforms:
            if self.player.rect.colliderect(platform.rect):
                self.player.falling = False
                break
        self.player.__update__()
        # Enemigo
        for enemy in self.enemies:
            enemy.__update__()
            if self.player.rect.colliderect(enemy.rect):
                self.respawn()
                self.lives -= 1
        #Escaleras
        for ladder in self.ladders:
            if self.player.rect.colliderect(ladder.rect):
                self.player.direction == "none"
        self.player.__update__()
        #Princesa
        for princess in self.princesses:
            princess.__update__()
            if self.player.rect.colliderect(princess.rect):
                self.score += 50000
                self.win += 1   
        #Plantas
        for plant in self.plants:
            plant.__update__()
            if self.player.rect.colliderect(plant.rect):
                self.respawn()
                self.lives -= 1
        #Jefe       
        for boss in self.bosses:
            boss.__update__()
            if self.player.rect.colliderect(boss.rect):
                self.respawn()
                self.lives -= 5
        #Puntaje
        if self.player.rect.top < 200:
            self.score = 50000
        elif self.player.rect.top < 300:
            self.score = 40000
        elif self.player.rect.top < 424:
            self.score = 30000

        # Guardar puntaje alto
        if self.score > self.highscore:
            self.highscore = self.score
            with open("HighScore.txt", "w") as g:
                g.write(str(self.score))  
            with open ("SalonFama.txt", "a") as f:
                f.write("Mario: " + str(self.score) + "\n")
            
    def __draw__(self):
        imagenfondo_juego = pygame.image.load("images/fondoCastle.png")
        self.frame.blit(imagenfondo_juego, (0,0))

        draw_text(self.frame, ("Score" + ":  " + str(self.score)), 24, 500, 10)
        draw_text(self.frame, ("Lives" + ":  " + str(self.lives)), 24, 500, 35)
        draw_text(self.frame, ("Highscore" + ":  " + str(self.highscore)), 24, 500, 60)
        draw_text(self.frame, ("Respawn: (r)"), 20, 500, 80)
            
        self.player.__draw__(self.frame)
        for platform in self.platforms:
            platform.__draw__(self.frame)
        self.player.__draw__(self.frame)
        for enemy in self.enemies:
            enemy.__draw__(self.frame)
        for ladder in self.ladders:
            ladder.__draw__(self.frame)
        for boss in self.bosses:
            boss.__draw__(self.frame)
        for princess in self.princesses:
            princess.__draw__(self.frame)
        self.player.__draw__(self.frame)
        for plant in self.plants:
            plant.__draw__(self.frame)

        #Imágenes que se presentan al ganar o perder
        if self.lives < 0:
            imagen_over = pygame.image.load("images/gameover1.png")
            self.frame.blit(imagen_over, (0,0))
        if self.win >= 1:
            imagen_next = pygame.image.load("images/totalwin.png")
            self.frame.blit(imagen_next, (0,0))

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.player.action = 'walking'
                self.player.direction = 'left'
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.player.action = 'walking'
                self.player.direction = 'right'
            elif event.key == pygame.K_SPACE and self.player.jump <= 0 and not self.player.falling:
                self.player.jump = 75
            elif event.key == pygame.K_r:
                self.respawn()
            if self.lives < 0 and event.key == pygame.K_y:
                self.respawn()
                self.lives = 5
                self.score = 0
            for ladder in self.ladders:
                if (event.key == pygame.K_UP or event.key == pygame.K_w) and self.player.rect.colliderect(ladder.rect) == True:
                    self.player.action = "walking"
                    self.player.direction = "up"
            for ladder in self.ladders:
                if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and self.player.rect.colliderect(ladder.rect)== True:
                    self.player.action = "walking"
                    self.player.direction = "down"                

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.player.action = 'standing'
                self.player.direction = 'left'
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.player.action = 'standing'
                self.player.direction = 'right'
            for ladder in self.ladders:
                if event.key == pygame.K_UP and  self.player.rect.colliderect(ladder.rect) == True:
                    self.player.action = 'standing'
                    self.player.direction = "up"
            for ladder in self.ladders:
                if event.key == pygame.K_DOWN and self.player.rect.colliderect(ladder.rect) == True:
                    self.player.action = 'standing'
                    self.player.direction = "down"
        
#Ejecutar la función de la principal
Principal()

#Cerrar PyGame
pygame.quit()
quit()
