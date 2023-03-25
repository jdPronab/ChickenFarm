import pygame as pg
import random

class Tile():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = None

        self.set_rect()

    def set_rect(self):
        self.rect =  pg.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        pass

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)

class Tilemap():

    def __init__(self, game):
        self.map = []
        self.tiles = []

        self.screen = game.screen
        self.settings = game.settings

        # used in draging the map
        self.drag = False
        self.tiles_ofset_coords = []

        self.prepare_tilemap()
        self.generate_tiles()


    def prepare_tilemap(self):
        for i in range(self.settings.world_width):
            row = []
            for j in range(self.settings.world_height):
                row.append(random.choice(self.settings.tile_styles))
            self.map.append(row)

    def generate_tiles(self):
        self.tiles = [[None for tile in row] for row in self.map ]
        for row in range(len(self.map)):
            for col in range(len(self.map[0])):
                tile_x = col * self.settings.tile_size
                tile_y = row * self.settings.tile_size
                if self.map[row][col] == 0:
                    self.tiles[row][col] = Tile(tile_x, tile_y,
                                                self.settings.tile_size,
                                                self.settings.tile_size,
                                                self.settings.tile_colors[0])
                elif self.map[row][col] == 1:
                    self.tiles[row][col] = Tile(tile_x, tile_y,
                                                self.settings.tile_size,
                                                self.settings.tile_size,
                                                self.settings.tile_colors[1])
                elif self.map[row][col] == 2:
                    self.tiles[row][col] = Tile(tile_x, tile_y,
                                                self.settings.tile_size,
                                                self.settings.tile_size,
                                                self.settings.tile_colors[2])
                elif self.map[row][col] == 3:
                    self.tiles[row][col] = Tile(tile_x, tile_y,
                                                self.settings.tile_size,
                                                self.settings.tile_size,
                                                self.settings.tile_colors[3])
                elif self.map[row][col] == 4:
                    self.tiles[row][col] = Tile(tile_x, tile_y,
                                                self.settings.tile_size,
                                                self.settings.tile_size,
                                                self.settings.tile_colors[4])



    '''
    ofset for every single tile
    to find the ofset
    ofset_x = tile.x - mouse_x
    ofset_y = tile.y - mouse_y
    '''

    def handle_event(self, event):
        self.tiles_ofset_coords = [[None for tile in row] for row in self.map]
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                for row in range(len(self.tiles_ofset_coords)):
                    for col in range(len(self.tiles_ofset_coords[0])):
                        ofset_x = self.tiles[row][col].x - mouse_x
                        ofset_y = self.tiles[row][col].y - mouse_y
                        self.tiles_ofset_coords[row][col] = (ofset_x, ofset_y)
                print(self.tiles_ofset_coords)
                self.drag = True

        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                    self.drag = False

        elif event.type == pg.MOUSEMOTION:
            if self.drag:
                print(self.tiles_ofset_coords)
                mouse_x, mouse_y = event.pos
                for row in range(len(self.map)):
                    for col in range(len(self.map[0])):
                        self.tiles[row][col].x = \
                                self.tiles_ofset_coords[row][col][0] + mouse_x
                        self.tiles[row][col].y = \
                                self.tiles_ofset_coords[row][col][1] + mouse_y


    def update(self, dt):
        if self.drag:

            print(self.tiles_ofset_coords)

    def draw(self):
        for row in self.tiles:
            for tile in row:
                tile.draw(self.screen)


if __name__ == "__main__":
    pass
