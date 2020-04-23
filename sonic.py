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

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom = SCREENRECT.midbottom)
        self.origtop = self.rect.top
        self.facing = -1

    def move(self, direction):
        if direction:
            self.facing = direction

        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp(SCREENRECT)
        if direction > 0:
            self.image = self.images[0]
        elif direction < 0:
            self.image = self.images[1]

def main():
    # Initialize pygame
    pygame.init()

    winstyle = 0
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    # Load images for player
    img = loadImage('Sonic.png')
    Player.images = [img, pygame.transform.flip(img, 1, 0)]

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

    all = pygame.sprite.RenderUpdates()
    Player.containers = all

    player = Player()
    clock = pygame.time.Clock()

    # Main loop
    while True:
        # Get input
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return

        keystate = pygame.key.get_pressed()

        # Clear the last drawn sprites
        all.clear(screen, background)

        # Update all the sprites
        all.update()

        # Handle player input
        direction = keystate[K_RIGHT] - keystate[K_LEFT]
        player.move(direction)

        # Draw the scene
        dirty = all.draw(screen)
        pygame.display.update(dirty)

        # Cap the framerate
        clock.tick(40)

    pygame.time.wait(1000)
    pygame.quit()


if __name__ == '__main__': 
    main()
