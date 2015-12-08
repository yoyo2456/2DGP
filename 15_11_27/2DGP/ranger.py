__author__ = 'Administrator'

from pico2d import *
from Player import *
import random



class Ranger:

    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8



    def __init__(self):


       #Base Setting
        self.frame = random.randint(0, 1)
        self.frame_x = 0
        self.frame_y = 0
        self.total_frames = 0.0
        self.dir = 1
        self.image = load_image('resource\\attack.png')
        self.x=300
        self.y=400
        self.distance = 0





    def update(self, frame_time):
        self.distance = Ranger.RUN_SPEED_PPS * frame_time
        #self.total_frames += Ranger.FRAMES_PER_ACTION * Ranger.ACTION_PER_TIME * frame_time
        self.x += self.distance
        self.draw()




    def draw(self):

      self.image.draw(self.x, self.y)



    def get_bb(self):
        return self.x-5.5,self.y-5.5,self.x+5.5,self.y+5.5

    def draw_bb(self):
        draw_rectangle(*self.get_bb())



    def collide(a,b):
        left_a, bottom_a, right_a, top_a = a.get_bb()
        left_b, bottom_b, right_b, top_b = b.get_bb()
        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False
        return True


