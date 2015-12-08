__author__ = 'incipe'

from pico2d import *
import random
import viewport

out_tile = None
out_tiles = None






class Background:
    def __init__(self):
        self.image = load_image('resource\\road3.png')

    def draw(self):
        self.image.draw(400,300)

class Out_Tile:
    image = None

    def __init__(self):
        self.create=random.randint(0,1)
        self.x =0
        self.y =0

        self.left = 0
        self.bottom = 0

        if self.image==None:
            self.image=load_image('resource\\tile.png')

    def get_bb(self):
         return self.x-12.5,self.y-12.5,self.x+12.5,self.y+12.5

    def create_out_tile(self):
        tile_data_file = open('text\\Out_tile.txt', 'r')
        tile_data = json.load(tile_data_file)
        tile_data_file.close()

        out_tiles = []

        for name in tile_data:
            out_tile = Out_Tile()
            out_tile.name = name
            out_tile.x = tile_data[name]['x']
            out_tile.y = tile_data[name]['y']
            out_tiles.append(out_tile)
        return out_tiles



    def draw(self):
        self.image.draw(self.x-12.5, self.y-12.5)


class In_Tile:
    image = None

    def __init__(self):
        self.create=random.randint(0,1)
        self.x =0
        self.y =0

        if self.image==None:
            self.image=load_image('resource\\tile.png')

    def set_center_object(self, player):
        self.center_object = player


    def get_bb(self):
       return (self.x - 25.5) , (self.y - 25.5) , (self.x)  , (self.y)
       #return (self.x - 12.5 , self.y - 12.5 , self.x + 12.5  , self.y + 12.5)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def create_in_tile(self):
        tile_data_file = open('text\\In_tile.txt', 'r')
        tile_data = json.load(tile_data_file)
        tile_data_file.close()

        in_tiles = []

        for name in tile_data:
            in_tile = In_Tile()
            in_tile.name = name
            in_tile.x = tile_data[name]['x']
            in_tile.y = tile_data[name]['y']
            in_tiles.append(in_tile)
        return in_tiles

    def draw(self):
        self.image.draw(self.x-12.5, self.y-12.5)



