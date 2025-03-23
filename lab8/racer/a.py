import pygame 
import random
import time

pygame.init()
pygame.mixer.init()

width = 400
height = 600
screen = pygame.display.set_mode((width,height))

pygame.mixer.music.load('background.wav')
pygame.mixer.music.set_volume(0.5) 
# infinite loop music
pygame.mixer.music.play(-1) 

clock = pygame.time.Clock()
FPS = 60

pygame.display.set_caption("RACER!")

image_back = pygame.image.load('AnimatedStreet.png')
image_player = pygame.image.load('Player.png')
image_enemy = pygame.image.load('Enemy.png')
image_coin = pygame.transform.scale(pygame.image.load('coin.png'), (30, 30))

back_y = 0

sound_crash = pygame.mixer.Sound('crash.wav')


# Set up font for text rendering
font = pygame.font.SysFont("Verdana", 60)
game_over = font.render("Game Over", True, "black")
game_over_rect = game_over.get_rect(center = (width // 2, height // 2))


# score render
def drawscore(score):
    score_text = font.render(f"Score: {score}" , True, "WHITE")
    screen.blit(score_text, (10, 10))

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect()
        self.rect.centerx = width // 2
        self.rect.bottom = height 
        self.speed = 5
        
    def move(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if key[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
            
        # Prevent player from going out of bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
    
  
# Enemy class
class Enemy(pygame.sprite.Sprite):
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
        self.rect.left = random.randint(0, width - self.rect.w)        
        self.rect.bottom = 0
  
# coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_coin
        self.rect = self.image.get_rect()
        self.speed = 6
        self.score = 0
        
    def generate_coin(self):
        self.rect.left = random.randint(0, width - self.rect.w)
        self.rect.bottom = 0
        
    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > height:
            self.generate_coin()
        elif self.rect.colliderect(player.rect):
            self.score += 1
            self.generate_coin()
        else:
            screen.blit(self.image, self.rect) 

running = True


player = Player()
enemy = Enemy()
coin = Coin()


# create sprite groups
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()

# add player and enemy to sprite groups
all_sprites.add(player, enemy)
enemy_sprites.add(enemy)

# main body
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # background effect
    screen.blit(image_back, (0, back_y))
    screen.blit(image_back, (0, back_y - height))
    back_y += 5
    if back_y == height:
        back_y = 0
        
    player.move() 
    
    # move and draw all cars (obj)
    for cars in all_sprites:
        cars.move()
        screen.blit(cars.image, cars.rect)  
        
    coin.move()
    
    drawscore(coin.score)
        
    if pygame.sprite.spritecollideany(player,enemy_sprites):
        sound_crash.play()
        time.sleep(1)
        
        running = False
        screen.fill("red")
        screen.blit(game_over, game_over_rect)
        pygame.display.flip()
        
        time.sleep(3)    
        
             
            
    pygame.display.update()
    clock.tick(FPS)
        
