class Settings():
    def __init__(self):
        self.tile_size = 32
        self.world_width = 40
        self.world_height = 40

        self.tile_styles = [x for x in range(5)]
        self.tile_colors = [(255, 0, 55),
                            (222, 12, 255),
                            (233, 30, 10),
                            (10, 20, 200),
                            (20, 50, 80)]
