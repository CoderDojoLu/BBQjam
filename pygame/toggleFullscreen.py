#!/usr/bin/env python3
import sys
from colors import *
from screen import *

def toggle_fullscreen():
    screen = pygame.display.get_surface()
    tmp = screen.convert()
    caption = pygame.display.get_caption()
    cursor = pygame.mouse.get_cursor()  # Duoas 16-04-2007

    w,h = screen.get_width(),screen.get_height()
    flags = screen.get_flags()
    bits = screen.get_bitsize()

    pygame.display.quit()
    pygame.display.init()

    screen = pygame.display.set_mode((w,h),flags^FULLSCREEN,bits)
    screen.blit(tmp,(0,0))
    pygame.display.set_caption(*caption)

    pygame.key.set_mods(0) #HACK: work-a-round for a SDL bug??

    pygame.mouse.set_cursor( *cursor )  # Duoas 16-04-2007

    return screen


def main():
    while True:
        for event in pygame.event.get():
            if (event.type is KEYDOWN and event.key == K_RETURN and (event.mod&(KMOD_LALT|KMOD_RALT)) != 0):
                toggle_fullscreen()
            if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
                exit()
                sys.exit()

        screen = pygame.display.get_surface()
        import random
        rr = random.randrange
        screen.fill((rr(0,256),rr(0,256),rr(0,256)),(rr(0,WIDTH),rr(0,HEIGHT),32,32))
        pygame.display.flip()

if __name__ == '__main__': main()
