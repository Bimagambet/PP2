import pygame as pg

pg.init()

width, height = 800 , 600
screen = pg.display.set_mode((width, height)) # окно орнату
pg.display.set_caption("paint sultan")

white, green, red, blue, black = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 255), (0, 0, 0)

curent_color = black

drawing = False
mode = "pen"

running = True
screen.fill(white) # Экранды ақ түспен бояу (таза күйде бастау)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT: # Егер қолданушы Quit батырмасын басса
            running = False
        
        elif event.type == pg.KEYDOWN: # Пернетақтадағы батырмаларға жауап беру
            if event.key == pg.K_r:
                mode = "rect"
            if event.key == pg.K_c:
                mode = "circle"
            if event.key == pg.K_e:
                mode = "eraser" 
            if event.key == pg.K_p:
                mode = "pen"
            if event.key == pg.K_1:
                curent_color = black
            if event.key == pg.K_2:
                curent_color = red
            if event.key == pg.K_3:
                curent_color = blue
            if event.key == pg.K_4:
                curent_color = green
        
        elif event.type == pg.MOUSEBUTTONDOWN:  # Егер тінтуірдің сол жақ батырмасы басылса – сурет сала бастаймыз
            if event.button == 1:
                drawing = True
                basu_pos = event.pos
        
        elif event.type == pg.MOUSEMOTION: # Егер mouse қозғалып жатса
            if drawing:
                if mode == "pen":
                    pg.draw.line(screen, curent_color, basu_pos, event.pos, 5)
                    basu_pos = event.pos # Соңғы координатаны жаңарту
                if mode == "eraser":
                    pg.draw.circle(screen, white, event.pos, 10)
                    
        
                    
        elif event.type == pg.MOUSEBUTTONUP: # Егер тінтуір батырмасы жіберілсе – сызуды аяқтаймыз
            if event.button == 1:
                drawing = False  
                last_pos = event.pos # мышка жібергеннен кейінгі кордината
                
                if mode == "rect":
                    pos_dim = pg.Rect(basu_pos, ((last_pos[0] - basu_pos[0]), (last_pos[1] - basu_pos[1])))
                    pg.draw.rect(screen, curent_color, pos_dim, 2)
                
                if mode == "circle":
                    radius = ((last_pos[0] - basu_pos[0])**2 + (last_pos[1] - basu_pos[1])**2 ) ** 0.5
                    pg.draw.circle(screen, curent_color, basu_pos, radius, 2)
                    
                                  
                     
    pg.display.flip() # Экранды жаңарту барлық өзгерістерді көрсету
pg.quit()