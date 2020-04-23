#!/usr/bin/env python

import pygame
import os.path
from pygame.locals import *

# Constants
SCREENRECT = Rect(0, 0, 640, 480)

gCurrentDirectory = os.path.split(os.path.abspath(__file__))[0]

def loadImage(name):
    file = os.path.join(gCurrentDirectory, 'data', name)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(name, pygame.get_error()))

    return surface.convert()

class Player(pygame.sprite.Sprite):
    speed = 10
    images = []

def main():
    # Initialize pygame
    pygame.init()

    winstyle = 0
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    # Load images for player


    # Decorate window
    pygame.display.set_caption('Pygame Sonic Run')
    pygame.mouse.set_visible(0)

    # Create the background
    img = loadImage('SonicWorld.png')
    background = pygame.Surface(SCREENRECT.size)
    for x in range(0, SCREENRECT.width, img.get_width()):
        background.blit(img, (x, 0))

    screen.blit(background, (0, 0))
    pygame.display.flip()

    pygame.time.wait(1000)
    pygame.quit()


if __name__ == '__main__': 
    main()
