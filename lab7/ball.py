import pygame
pygame.init()

W = 600
H = 600

clock = pygame.time.Clock()
screen = pygame.display.set_mode((W,H))

pygame.display.set_caption("Ball")

def drawcircle(a = 0, b = 0):
    pygame.draw.circle(screen, (255, 0, 0), (a, b), 25)

x = 30
y = 30

done = True

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
            
    screen.fill((0, 0, 0))
   
    drawcircle(x, y)
    key = pygame.key.get_pressed()
    if key[pygame.K_a] and x > 25:  x -= 20
    if key[pygame.K_d] and x < 575:  x += 20
    if key[pygame.K_w] and y > 25:  y -= 20
    if key[pygame.K_s] and y < 575:  y += 20
    
    pygame.display.update()
    clock.tick(60)