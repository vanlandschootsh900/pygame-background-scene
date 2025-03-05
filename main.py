#Shay VanLandschoot
#--DATE--#
# Pygame game template

import pygame
import sys
import config # Import the config module

def init_game ():

    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) 
   
    
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def draw_text(screen, text, font, text_color, x,y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x,y))

def draw_cloud(screen, pos, pos1, pos2, pos3):
    pygame.draw.circle(screen, config.WHITE, pos, 50)

    
    pygame.draw.circle(screen, config.WHITE, pos1, 50)
    pygame.draw.circle(screen, config.WHITE, pos2, 50)
    pygame.draw.circle(screen, config.WHITE, pos3, 50)

def sun(screen, pos):
    pygame.draw.circle(screen, config.YELLOW, pos, 75)


def guy(screen,start, end,right,left, arms,arme):
    pygame.draw.line(screen, config.BLACK, start,end,5)
    
    pygame.draw.line(screen,config.BLACK,end, left,5)
    pygame.draw.line(screen,config.BLACK,end,right,5)
    pygame.draw.line(screen,config.BLACK,arms,arme,5)
    pygame.draw.circle(screen, config.BLACK, start ,15)



def main():
    
    screen = init_game()
    clock = pygame.time.Clock()
    text_font = pygame.font.SysFont('Arial', 50)
    text_font1 = pygame.font.SysFont('Arial', 30)
    

    running = True
    while running:
        running = handle_events()
        screen.fill(config.SKY_BLUE) # Use color from config
        
        # Add code to draw stuff (for example) below this comment

        draw_text(screen,'THE SKY', text_font, config.PURPLE,300,100)
        draw_text(screen,'Guy Falling',text_font,config.PURPLE,150, 400)
        

        draw_cloud(screen, (200,300), (250,300),(150,300),(200,250))
        draw_cloud(screen, (500,400),(450,400),(550,400),(500,350))
        draw_cloud(screen, (600,130),(550,130),(650,130),(600,80))
        sun(screen, (100,100))
        guy(screen,(200,500),(250,550),(245,580),(280,550),(190,550),(240,500))
        draw_text(screen,'sun',text_font1,config.PURPLE,80,75)
        draw_text(screen,'CLOUD',text_font1,config.PURPLE,460,380)
        
        pygame.display.flip()
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
