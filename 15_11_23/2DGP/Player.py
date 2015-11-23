from pico2d import *
from maze import *
from Jewelry import *
import random
import json
import os




class Player:

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
        global blue_jewelry

        self.frame = random.randint(0, 7)
        self.total_frames = 0.0
        self.dir = 1
        self.image = load_image('resource\\player.png')

        self.frame_y = 0
        self.frame_x = 0
        self.state = self.STANDING # 기본 상태
        self.bf_state = self.STANDING # 이전 상태
        self.x=400
        self.y=300
        self.distance = 0
        self.hp=5 #Player Hp
        self.reverseMove = 0


        #collide
        self.left_collid = False
        self.right_collid = False
        self.up_collid = False
        self.down_collid = False

        #Jewelry count
        self.BJ_count = 0
        self.RJ_count = 0
        self.YJ_count = 0
        self.GJ_count = 0




    def handle_event(self, event):
          if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state==self.SKILL:
                self.old_state=self.LEFT_MOVE
            else:
                self.state=self.LEFT_MOVE
          elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state==self.SKILL:
                self.old_state=self.RIGHT_MOVE
            else:
                self.state=self.RIGHT_MOVE
          elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            if self.state==self.SKILL:
                self.old_state=self.UP_MOVE
            else:
                self.state=self.UP_MOVE
          elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if self.state==self.SKILL:
                self.old_state=self.DOWN_MOVE
            else:
                self.state=self .DOWN_MOVE
          elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state==self.LEFT_MOVE:
                self.state=self .STANDING
            elif self.state==self.SKILL:
                self.old_state=self.STANDING
          elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state==self.RIGHT_MOVE:
                self.state=self.STANDING
            elif self.state==self.SKILL:
                self.old_state=self.STANDING
          elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            if self.state==self.UP_MOVE:
                self.state=self.STANDING
            elif self.state==self.SKILL:
                self.old_state=self.STANDING
          elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            if self.state==self.DOWN_MOVE:
                self.state=self.STANDING
            elif self.state==self.SKILL:
                self.old_state=self.STANDING


    def MovingPlayer(self):
        if self.state == self.RIGHT_MOVE:
            if self.x > 775:
                pass
            else:

                self.x += (self.dir * self.distance/2)
        elif self.state == self.LEFT_MOVE:
            if self.x < 30:
                pass
            else:

                self.x -= (self.dir * self.distance/2)
        elif self.state == self.UP_MOVE:
            if self.y > 575:
                pass
            else:

                self.y += (self.dir * self.distance/2)
        elif self.state == self.DOWN_MOVE:
            if self.y < 43:
                pass
            else:

                self.y -= (self.dir * self.distance/2)


    def leftCollide_Player(self):
        self.x += (self.dir * self.distance/2) + 5.5

    def rightCollide_Player(self):
        self.x -= (self.dir * self.distance/2) + 5.5

    def upCollide_Player(self):
        self.y -= (self.dir * self.distance/2) + 5.5

    def downCollide_Player(self):
        self.y += (self.dir * self.distance/2) + 5.5


    def get_BJ(self):
         global BJ_count
         self.BJ_count +=1

    def get_RJ(self):
         global RJ_count
         self.RJ_count +=1

    def get_GJ(self):
         global GJ_count
         self.GJ_count +=1

    def get_YJ(self):
         global YJ_count
         self.YJ_count +=1




    def update(self, frame_time):
        self.distance = Player.RUN_SPEED_PPS * frame_time
        self.total_frames += Player.FRAMES_PER_ACTION * Player.ACTION_PER_TIME * frame_time
        self.frame = (self.frame + 1) % 6
        self.frame_x = (self.frame_x + 1) % 8
        self.MovingPlayer()



    def draw(self):
        self.image.clip_draw(self.frame * 40, self.state * 30, 40, 30, self.x, self.y)



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





