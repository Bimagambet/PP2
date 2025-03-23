import pygame as pg
import random

pg.init()

W = 800
H = 800

clock = pg.time.Clock()
screen = pg.display.set_mode((W, H))

pg.display.set_caption("Snake!")

cell = 50


FPS = 10

font = pg.font.SysFont('Verdana',30)
int_font = pg.font.SysFont('Verdana',30)

def drawField():
    for i in range(0, W, cell):
        for j in range(0, H, cell):
            rect = pg.Rect(i, j, cell, cell)
            pg.draw.rect(screen, (21, 27, 35), rect, 1)


def drawtext(score, level):
    score_text = font.render(f"Score: {score}  Level: {level}", True, "WHITE")
    screen.blit(score_text, (10, 10))

class Snake:
    def __init__(self):
        self.x, self.y = cell, cell
        self.xdir = 1
        self.ydir = 0
        self.head = pg.Rect(self.x, self.y, cell, cell)
        self.body = [pg.Rect(self.x - cell, self.y, cell, cell)]
        self.dead = False
        self.score = 0
        self.level = 1

    def move(self):
        for i in self.body:
            if self.head.x not in range(0, W) or self.head.y not in range(0, H):
                self.dead = True
            if self.head.x == i.x and self.head.y == i.y:
                self.dead = True
        
        if self.dead:
            self.score = 0
            self.level = 1
            self.x, self.y = cell, cell
            self.xdir = 1
            self.ydir = 0
            self.head = pg.Rect(self.x, self.y, cell, cell)
            self.body = [pg.Rect(self.x - cell, self.y, cell, cell)]
            self.dead = False

        self.body.append(self.head)
        for i in range(len(self.body)-1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        self.head.x += self.xdir * cell
        self.head.y += self.ydir * cell
        self.body.remove(self.head)
    

    

    def draw(self, surf, side = [0, 0, 0, 0]):
        pg.draw.rect(surf, (0, 0, 255), (self.head.x, self.head.y, cell, cell), 0, 0)

        for i in self.body:
            pg.draw.rect(surf, "green", i)


class Apple:
    def __init__(self):
        self.x = random.randint(0, W)// cell * cell
        self.y = random.randint(0, H)// cell * cell
    
    def draw(self, screen):
        pg.draw.circle(screen, "red", (self.x+25, self.y+25), 25)

snake = Snake()
apple = Apple()


sides = [0, 25, 0, 25]

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                snake.xdir = -1
                snake.ydir = 0
                sides = [25, 0, 25, 0]
            elif event.key == pg.K_s:
                snake.xdir = 0
                snake.ydir = 1
                sides = [0, 0, 25, 25]
            elif event.key == pg.K_d:
                snake.xdir = 1
                snake.ydir = 0
                sides = [0, 25, 0, 25]
            elif event.key == pg.K_w:
                snake.xdir = 0
                snake.ydir = -1
                sides = [25, 25, 0, 0]
    

    screen.fill((13, 17, 23))
    

    
    apple.draw(screen)
    snake.move()
    snake.draw(screen, sides)

    key = pg.key.get_pressed()

    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.body.append(pg.Rect(snake.body[-1].x, snake.body[-1].y, cell, cell))
        apple = Apple()
        snake.score += 1
        snake.level = snake.score // 5 + 1
    

    drawField()
    drawtext(snake.score, snake.level)
    
    pg.display.update()
    clock.tick(FPS + snake.level - 1)
pg.quit()
exit()