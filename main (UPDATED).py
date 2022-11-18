import pygame
from pygame import mixer


#items + window

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
START_SCREEN = None
TITLE_MUSIC = True

# music variables

remember_her = 'Remember her-MARI Title.mp3'

# main
pygame.init()
mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('MARI')
running = True


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


BackGround = Background('Screenshot 2022-11-17 203935.png', [0, 120])
screen.fill([255, 255, 255])
screen.blit(BackGround.image, BackGround.rect)

# music player
mixer.music.load(remember_her)
mixer.music.play()

# screen display

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    print(clock.get_fps())
    pygame.display.update()
    clock.tick(60)

pygame.quit()
