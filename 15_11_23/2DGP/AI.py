__author__ = 'Administrator'

import random
from pico2d import *

class AI_1:


    STANDING,RIGHT_MOVE,DOWN_MOVE,LEFT_MOVE,UP_MOVE=0,1,2,3,4
    ATTACK,SKILL=5,6

    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8


    def __init__(self):

        self.image = load_image('resource\\ai.png')
        self.frame = random.randint(0, 7)
        self.total_frames = 0.0
        self.dir = 1


        self.frame_y = 0
        self.frame_x = 0
        self.state = random.randint(1,4)
        self.bf_state = self.STANDING # 이전 상태
        self.x=150
        self.y=525
        self.dir = 1
        self.distance = 0
        self.hp=5 #Player Hp
        #self.direction=random.randint(0,3)






    def update(self, frame_time):
        self.distance = AI_1.RUN_SPEED_PPS * frame_time
        self.total_frames += AI_1.FRAMES_PER_ACTION * AI_1.ACTION_PER_TIME * frame_time
        self.frame = (self.frame + 1) % 6
        self.frame_x = (self.frame_x + 1) % 8


        if self.state == self.RIGHT_MOVE:
            self.x +=5
            if self.x>=775:
                self.x -=5
                self.state=random.randint(1,4)

        elif self.state == self.UP_MOVE:
            self.y +=5
            if self.y>=575:
                self.y -=5
                self.state=random.randint(1,4)
                if self.state == self.LEFT_MOVE:
                     self.state=random.randint(1,4)

        elif self.state == self.LEFT_MOVE:
            self.x -=5
            if self.x<=30:
                 self.x +=5
                 self.state=random.randint(1,4)
                 if self.state == self.LEFT_MOVE:
                     self.state=random.randint(1,4)


        elif self.state == self.DOWN_MOVE:
            self.y -=5
            if self.y<=43:
                 self.y +=5
                 self.state=random.randint(1,4)


    def draw(self):
        self.image.clip_draw(self.frame * 40, self.state * 30, 40, 30, self.x, self.y)

    def get_bb(self):
        return self.x-5,self.y-5,self.x+5,self.y+5

    def draw_bb(self):
        draw_rectangle(*self.get_bb())




class AI_2:


    STANDING,RIGHT_MOVE,DOWN_MOVE,LEFT_MOVE,UP_MOVE=0,1,2,3,4
    ATTACK,SKILL=5,6

    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8


    def __init__(self):

        self.image = load_image('resource\\ai.png')
        self.frame = random.randint(0, 7)
        self.total_frames = 0.0
        self.dir = 1


        self.frame_y = 0
        self.frame_x = 0
        self.state = random.randint(1,4)
        self.bf_state = self.STANDING # 이전 상태
        self.x=700
        self.y=575
        self.dir = 1
        self.distance = 0
        self.hp=5 #Player Hp
        #self.direction=random.randint(0,3)






    def update(self, frame_time):
        self.distance = AI_2.RUN_SPEED_PPS * frame_time
        self.total_frames += AI_2.FRAMES_PER_ACTION * AI_2.ACTION_PER_TIME * frame_time
        self.frame = (self.frame + 1) % 6
        self.frame_x = (self.frame_x + 1) % 8


        if self.state == self.RIGHT_MOVE:
            self.x +=5
            if self.x>=775:
                self.x -=5
                self.state=random.randint(1,4)

        elif self.state == self.UP_MOVE:
            self.y +=5
            if self.y>=575:
                self.y -=5
                self.state=random.randint(1,4)
                if self.state == self.LEFT_MOVE:
                     self.state=random.randint(1,4)

        elif self.state == self.LEFT_MOVE:
            self.x -=5
            if self.x<=30:
                 self.x +=5
                 self.state=random.randint(1,4)
                 if self.state == self.LEFT_MOVE:
                     self.state=random.randint(1,4)


        elif self.state == self.DOWN_MOVE:
            self.y -=5
            if self.y<=43:
                 self.y +=5
                 self.state=random.randint(1,4)


    def draw(self):
        self.image.clip_draw(self.frame * 40, self.state * 30, 40, 30, self.x, self.y)

    def get_bb(self):
        return self.x-5,self.y-5,self.x+5,self.y+5

    def draw_bb(self):
        draw_rectangle(*self.get_bb())



class AI_3:


    STANDING,RIGHT_MOVE,DOWN_MOVE,LEFT_MOVE,UP_MOVE=0,1,2,3,4
    ATTACK,SKILL=5,6

    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8


    def __init__(self):

        self.image = load_image('resource\\ai.png')
        self.frame = random.randint(0, 7)
        self.total_frames = 0.0
        self.dir = 1


        self.frame_y = 0
        self.frame_x = 0
        self.state = random.randint(1,4)
        self.bf_state = self.STANDING # 이전 상태
        self.x=150
        self.y=200
        self.dir = 1
        self.distance = 0
        self.hp=5 #Player Hp
        #self.direction=random.randint(0,3)






    def update(self, frame_time):
        self.distance = AI_3.RUN_SPEED_PPS * frame_time
        self.total_frames += AI_3.FRAMES_PER_ACTION * AI_3.ACTION_PER_TIME * frame_time
        self.frame = (self.frame + 1) % 6
        self.frame_x = (self.frame_x + 1) % 8


        if self.state == self.RIGHT_MOVE:
            self.x +=5
            if self.x>=775:
                self.x -=5
                self.state=random.randint(1,4)

        elif self.state == self.UP_MOVE:
            self.y +=5
            if self.y>=575:
                self.y -=5
                self.state=random.randint(1,4)
                if self.state == self.LEFT_MOVE:
                     self.state=random.randint(1,4)

        elif self.state == self.LEFT_MOVE:
            self.x -=5
            if self.x<=30:
                 self.x +=5
                 self.state=random.randint(1,4)
                 if self.state == self.LEFT_MOVE:
                     self.state=random.randint(1,4)


        elif self.state == self.DOWN_MOVE:
            self.y -=5
            if self.y<=43:
                 self.y +=5
                 self.state=random.randint(1,4)


    def draw(self):
        self.image.clip_draw(self.frame * 40, self.state * 30, 40, 30, self.x, self.y)

    def get_bb(self):
        return self.x-5,self.y-5,self.x+5,self.y+5

    def draw_bb(self):
        draw_rectangle(*self.get_bb())



class AI_4:


    STANDING,RIGHT_MOVE,DOWN_MOVE,LEFT_MOVE,UP_MOVE=0,1,2,3,4
    ATTACK,SKILL=5,6

    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8


    def __init__(self):

        self.image = load_image('resource\\ai.png')
        self.frame = random.randint(0, 7)
        self.total_frames = 0.0
        self.dir = 1


        self.frame_y = 0
        self.frame_x = 0
        self.state = random.randint(1,4)
        self.bf_state = self.STANDING # 이전 상태
        self.x=700
        self.y=150
        self.dir = 1
        self.distance = 0
        self.hp=5 #Player Hp
        #self.direction=random.randint(0,3)






    def update(self, frame_time):
        self.distance = AI_4.RUN_SPEED_PPS * frame_time
        self.total_frames += AI_4.FRAMES_PER_ACTION * AI_4.ACTION_PER_TIME * frame_time
        self.frame = (self.frame + 1) % 6
        self.frame_x = (self.frame_x + 1) % 8


        if self.state == self.RIGHT_MOVE:
            self.x +=5
            if self.x>=775:
                self.x -=5
                self.state=random.randint(1,4)

        elif self.state == self.UP_MOVE:
            self.y +=5
            if self.y>=575:
                self.y -=5
                self.state=random.randint(1,4)
                if self.state == self.LEFT_MOVE:
                     self.state=random.randint(1,4)

        elif self.state == self.LEFT_MOVE:
            self.x -=5
            if self.x<=30:
                 self.x +=5
                 self.state=random.randint(1,4)
                 if self.state == self.LEFT_MOVE:
                     self.state=random.randint(1,4)


        elif self.state == self.DOWN_MOVE:
            self.y -=5
            if self.y<=43:
                 self.y +=5
                 self.state=random.randint(1,4)


    def draw(self):
        self.image.clip_draw(self.frame * 40, self.state * 30, 40, 30, self.x, self.y)

    def get_bb(self):
        return self.x-5,self.y-5,self.x+5,self.y+5

    def draw_bb(self):
        draw_rectangle(*self.get_bb())