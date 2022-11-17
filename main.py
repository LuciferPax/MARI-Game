import pygame


#items + window

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
START_SCREEN = NULL

#main 
pygame.init()
clock = pygame.time.Clock()  
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
pygame.display.set_caption('MARI')
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    print(clock.get_fps())
    pygame.display.update()
    clock.tick(60)
  
pygame.quit()

  
