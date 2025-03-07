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


def draw_cloud(screen, x,y):
    pygame.draw.circle(screen, config.WHITE, (x,y), 50)

    
    pygame.draw.circle(screen, config.WHITE, (50+x,y), 50)
    pygame.draw.circle(screen, config.WHITE, ((-50)+x,y), 50)
    pygame.draw.circle(screen, config.WHITE, (x,(-50)+y), 50)


def sun(screen, pos):
    pygame.draw.circle(screen, config.YELLOW, pos, 75)


#Add 50 to the START Numbers x/y to get the END X/Y
def guy(screen, start_x, start_y, end_x, end_y):
    pygame.draw.line(screen, config.BLACK, (start_x,start_y),(end_x,end_y),5)
    

    pygame.draw.line(screen,config.BLACK, (end_x,end_y), (80+start_x,50+start_y), 5)
    pygame.draw.line(screen,config.BLACK, (end_x,end_y), (45+start_x,80+start_y), 5)
    pygame.draw.line(screen,config.BLACK,((-10)+start_x,50+start_y) , (30+end_x,(-50)+end_y) ,5)
    pygame.draw.circle(screen, config.BLACK,(start_x,start_y) ,15)



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
        
        draw_cloud(screen, 200,300)
        draw_cloud(screen, 500,400)
        draw_cloud(screen, 600,130)
        sun(screen, (100,100))

        guy(screen,200,500,250,550)
        
       

        draw_text(screen,'sun',text_font1,config.PURPLE,80,75)
        draw_text(screen,'CLOUD',text_font1,config.PURPLE,460,380)
        
        pygame.display.flip()
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
