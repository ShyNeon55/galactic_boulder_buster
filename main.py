import pygame
from constants import *
from player import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        #This keeps the game running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            #This allows you to exit the game by hitting the exit button
        dt = clock.tick(60) / 1000
        #This sets the fps to 60 and sets the miliseconds to the delta
        screen.fill((0, 0, 0))
        #Makes the screen black
        player.draw(screen)
        #Redraws player each frame
        pygame.display.flip()
        


if __name__ == "__main__":
    main()
