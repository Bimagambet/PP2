import pygame
import time

pygame.mixer.init()
pygame.init()

w = 500
h = 500

clock = pygame.time.Clock()
screen = pygame.display.set_mode((w, h))

pygame.display.set_caption("music")

imgs = [
    pygame.transform.scale(pygame.image.load("md.jpg"), (w, h)),
    pygame.transform.scale(pygame.image.load("litvin.jpg"), (w, h))
]

musics = [
    (r"C:\Users\Юзер\OneDrive\Рабочий стол\python\PP2\lab7\md.mp3"),
    (r"C:\Users\Юзер\OneDrive\Рабочий стол\python\PP2\lab7\navai.mp3")
]

play = 0
playing = False
lenght = len(musics)

def play_music():
    global playing
    pygame.mixer.music.load(musics[play])
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.5)
    playing = True
    
def stop_music(): 
    global playing
    pygame.mixer.music.stop()
    playing = False
    
def play_next():
    global play
    play = (play + 1) % lenght
    play_music()
    
def play_prev():
    global play
    if play - 1 < 0:
        play = 2
    else:
        play = (play - 1) % lenght
        
    play_music()
    
play_music()

done = True

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    
    screen.fill((0,0,0))
    screen.blit(imgs[play], (0,0))
    
    key = pygame.key.get_pressed()
    
    if(key[pygame.K_LEFT]) :
        play_prev()
        time.sleep(0.5)
    elif(key[pygame.K_RIGHT]) :
        play_next()
        time.sleep(0.5)   
    elif(key[pygame.K_SPACE]) :
        if playing:
            pygame.mixer.music.pause()
            playing = False
        else:
            pygame.mixer.music.unpause()
            playing = True
        time.sleep(0.5)
    elif key[pygame.K_s]:
        stop_music()
        
    pygame.display.update()
    
pygame.quit()   
    
