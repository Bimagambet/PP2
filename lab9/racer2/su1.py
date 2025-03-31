import pygame as pg 
import random
import time

pg.init()
pg.mixer.init() # for sounds

width = 400
height = 600
screen = pg.display.set_mode((width,height)) # display koiu

pg.mixer.music.load('background.wav') # back music
pg.mixer.music.set_volume(0.5)  # valume to 50%
# infinite loop music
pg.mixer.music.play(-1) 

clock = pg.time.Clock()
FPS = 60 # frequency 60fps

pg.display.set_caption("RACER!")

image_back = pg.image.load('AnimatedStreet.png')
image_player = pg.image.load('Player.png')
image_enemy = pg.image.load('Enemy.png')
image_coin = [(pg.transform.scale(pg.image.load('coin.png'), (30, 30))),
              (pg.transform.scale(pg.image.load('yellow.jpg'), (30, 30))),
              (pg.transform.scale(pg.image.load('red.png'), (30, 30)))] # коин размерин 30х30 писксел етіп жасау

back_y = 0 # фонның жылжу кординатасы

sound_crash = pg.mixer.Sound('crash.wav') 


# Set up font for text rendering
font = pg.font.SysFont("Verdana", 60)  # Verdana шрифтін 60 пиксель өлшемінде орнату
game_over = font.render("Game Over", True, (0,0,0)) # render для гаме овер
game_over_rect = game_over.get_rect(center = (width // 2, height // 2)) # "Game Over" мәтінін экранның ортасына орналастыру

# score render
def drawscore(score):
    score_text = font.render(f"Score: {score}" , True, (255, 255, 255)) # ақ түсті мәтін жасау
    screen.blit(score_text, (10, 10)) # экранның жоғарғы сол жағына орналастыру

# Player class
class Player(pg.sprite.Sprite):
    def __init__(self): 
        super().__init__() # Вызываем конструктор Sprite
        self.image = image_player 
        self.rect = self.image.get_rect() 
        self.rect.centerx = width // 2 # экранның ортасына қою
        self.rect.bottom = height # төменгі бөлікке орналастыру
        self.speed = 5
        
    def move(self):
        key = pg.key.get_pressed()
        
        if key[pg.K_d]:
            self.rect.move_ip(self.speed, 0)
        if key[pg.K_a]:
            self.rect.move_ip(-self.speed, 0)
            
        # Prevent player from going out of bounds
        if self.rect.left < 0: # prevent Сол жақ шектен шықпауды
            self.rect.left = 0
        if self.rect.right > width: # prevent Оң жақ шектен шықпауды
            self.rect.right = width
    
  
# Enemy class
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = image_enemy.get_rect()
        self.speed = 10
        
    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > height:
            self.generate_rect()    
    
    def generate_rect(self):
        self.rect.left = random.randint(0, width - self.rect.w) # кездейсоқ орынға қою
        self.rect.bottom = 0 # enemy экранның жоғарғы шетіне қою
  
# coin class
class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.type = 0
        self.image = image_coin[self.type]
        self.rect = self.image.get_rect()
        self.speed = 6
        self.score = 0
        
    def generate_coin(self):
        self.rect.left = random.randint(0, width - self.rect.w)
        self.rect.bottom = 0
        self.type = random.randint(0, 2)
        self.image = image_coin[self.type]
        
    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > height:  
            self.generate_coin()
        elif self.rect.colliderect(playerr.rect):
            self.score += (self.type + 1) * 10
            self.generate_coin()
        else:
            screen.blit(self.image, self.rect) 
            
        if self.score > 100:
            enemy.speed = 30
        elif self.score > 50:
            enemy.speed = 15

running = True


playerr = Player()
enemy = Enemy()
coin = Coin()


# create sprite groups
all_sprites = pg.sprite.Group()
enemy_sprites = pg.sprite.Group()

# add player and enemy to sprite groups
all_sprites.add(playerr, enemy)
enemy_sprites.add(enemy)

# main body
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
    # background effect
    screen.blit(image_back, (0, back_y))
    screen.blit(image_back, (0, back_y - height))
    back_y += 5
    if back_y == height:
        back_y = 0
    
    # move and draw all cars (obj)
    for cars in all_sprites:
        cars.move()
        screen.blit(cars.image, cars.rect)  
        
    coin.move()
    
    drawscore(coin.score)
        
    if pg.sprite.spritecollideany(playerr,enemy_sprites):
        sound_crash.play()
        time.sleep(1)
        
        running = False
        screen.fill("red")
        screen.blit(game_over, game_over_rect)
        pg.display.flip()
        
        time.sleep(3)    
        
             
            
    pg.display.update()
    clock.tick(FPS)