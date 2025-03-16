import pygame
import os

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
            canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
            image = pygame.image.load(canonicalized_path)
            _image_library[path] = image
        return image
    
x = 30
y = 30 
    
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = True
clock = pygame.time.Clock()

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
            
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3    
    if pressed[pygame.K_DOWN]: y += 3  
    if pressed[pygame.K_LEFT]: x -= 3  
    if pressed[pygame.K_RIGHT]: x += 3    
    
      
            
    screen.fill((255, 255, 255))
    
    screen.blit(get_image('tutorial_2_3.png'), (x, y, 40, 40))
    
    pygame.display.flip()
    clock.tick(60)
