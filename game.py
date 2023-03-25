import pygame as pg

from tilemap import Tilemap
from settings import Settings


class Game():
    def __init__(self):
        self.screen = None
        self.playing = True
        self.settings = Settings()

        self._initialise()

        self.map = Tilemap(self)

    def _initialise(self):
        pg.init()
        self.screen = pg.display.set_mode((1024, 768), 0, 32)
        pg.display.set_caption("Chicken Farm")

    def run(self):
        while self.playing:
            self.handle_event()
            self.draw()
            self.update(30)

    def handle_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False

            self.map.handle_event(event)



    def update(self, dt):
        self.map.update(dt)

        pg.display.update()

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.map.draw()

