__author__ = 'Administrator'

from pico2d import *
import random




class blue_Jewelry:
    image = None

    def __init__(self):

        self.create=random.randint(0,1)
        self.x =0
        self.y =0


        if self.image==None:
            self.image=load_image('resource\\blue_jewelry.png')


    def get_bb(self):
        return (self.x - 25) , (self.y - 25) , (self.x)  , (self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def create_blue_jewelry(self):
        blue_jewelry_data_file = open('text\\blue_jewelry.txt', 'r')
        blue_jewelry_data = json.load(blue_jewelry_data_file)
        blue_jewelry_data_file.close()

        blue_jewelrys = []

        for name in blue_jewelry_data:
            blue_jewelry = blue_Jewelry()
            blue_jewelry.name = name
            blue_jewelry.x = blue_jewelry_data[name]['x']
            blue_jewelry.y = blue_jewelry_data[name]['y']
            blue_jewelrys.append(blue_jewelry)
        return blue_jewelrys

    def draw(self):
        self.image.draw(self.x-12.5, self.y-12.5)









class red_Jewelry:
    image = None

    def __init__(self):
        self.create=random.randint(0,1)
        self.x =0
        self.y =0

        if self.image==None:
            self.image=load_image('resource\\red_jewelry.png')

    def get_bb(self):
        return (self.x - 25) , (self.y - 25) , (self.x)  , (self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def create_red_jewelry(self):
        red_jewelry_data_file = open('text\\red_jewelry.txt', 'r')
        red_jewelry_data = json.load(red_jewelry_data_file)
        red_jewelry_data_file.close()

        red_jewelrys = []

        for name in red_jewelry_data:
            red_jewelry = red_Jewelry()
            red_jewelry.name = name
            red_jewelry.x = red_jewelry_data[name]['x']
            red_jewelry.y = red_jewelry_data[name]['y']
            red_jewelrys.append(red_jewelry)
        return red_jewelrys

    def draw(self):
        self.image.draw(self.x-12.5, self.y-12.5)


class green_Jewelry:
    image = None

    def __init__(self):
        self.create=random.randint(0,1)
        self.x =0
        self.y =0

        if self.image==None:
            self.image=load_image('resource\\green_jewelry.png')

    def get_bb(self):
        return (self.x - 25) , (self.y - 25) , (self.x)  , (self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def create_green_jewelry(self):
        green_jewelry_data_file = open('text\\green_jewelry.txt', 'r')
        green_jewelry_data = json.load(green_jewelry_data_file)
        green_jewelry_data_file.close()

        green_jewelrys = []

        for name in green_jewelry_data:
            green_jewelry = green_Jewelry()
            green_jewelry.name = name
            green_jewelry.x = green_jewelry_data[name]['x']
            green_jewelry.y = green_jewelry_data[name]['y']
            green_jewelrys.append(green_jewelry)
        return green_jewelrys

    def draw(self):
        self.image.draw(self.x-12.5, self.y-12.5)


class yellow_Jewelry:
    image = None

    def __init__(self):
        self.create=random.randint(0,1)
        self.x =0
        self.y =0

        if self.image==None:
            self.image=load_image('resource\\yellow_jewelry.png')



    def get_bb(self):
        return (self.x - 25) , (self.y - 25) , (self.x)  , (self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def create_yellow_jewelry(self):
        yellow_jewelry_data_file = open('text\\yellow_jewelry.txt', 'r')
        yellow_jewelry_data = json.load(yellow_jewelry_data_file)
        yellow_jewelry_data_file.close()

        yellow_jewelrys = []

        for name in yellow_jewelry_data:
            yellow_jewelry = yellow_Jewelry()
            yellow_jewelry.name = name
            yellow_jewelry.x = yellow_jewelry_data[name]['x']
            yellow_jewelry.y = yellow_jewelry_data[name]['y']
            yellow_jewelrys.append(yellow_jewelry)
        return yellow_jewelrys

    def draw(self):
        self.image.draw(self.x-12.5, self.y-12.5)
