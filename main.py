import pygame
from pygame_phyics import *

SCREEN_SIZE = (1200, 800)
TITLE = "title"

Game.init(SCREEN_SIZE, TITLE)

Game.import_objects("objects/", debug="log")

@game.world("scene/main.json")
def main():

    def start(cls: Game):
        pass

    def event(cls: Game, event: pygame.event.Event):
        pass

    def update(cls: Game):
        pass
    return start, event, update

main()

