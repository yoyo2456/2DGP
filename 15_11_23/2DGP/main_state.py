import random
import json
import os

from pico2d import *
from maze import *
from Player import *
from AI import *
from Jewelry import *


import game_framework
from pico2d import *
import title_state


name = "MainState"
count = None
font = None



def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time



def enter():
    global player,background #player
    global out_tile,in_tile #tile
    global blue_jewelry,red_jewelry, green_jewelry, yellow_jewelry #jewelry
    global out_tiles, in_tiles, blue_jewelrys, red_jewelrys, green_jewelrys, yellow_jewelrys # -s
    global font # font
    global ai_1,ai_2,ai_3,ai_4 # ai

    font = load_font('Font\\2DGP.TTF')


    player = Player()
    ai_1 = AI_1()
    ai_2 = AI_2()
    ai_3 = AI_3()
    ai_4 = AI_4()
    background = Background()
    out_tile = Out_Tile()
    in_tile = In_Tile()

    red_jewelry = red_Jewelry()
    blue_jewelry = blue_Jewelry()
    green_jewelry = green_Jewelry()
    yellow_jewelry = yellow_Jewelry()

    in_tiles = in_tile.create_in_tile()

    blue_jewelrys = blue_jewelry.create_blue_jewelry()
    red_jewelrys = red_jewelry.create_red_jewelry()
    green_jewelrys = green_jewelry.create_green_jewelry()
    yellow_jewelrys =  yellow_jewelry.create_yellow_jewelry()



def exit():
    pass


def pause():
    pass


def resume():
    pass

# a : Player, b : Obstacle
def collide(a,b):
     left_a, bottom_a, right_a, top_a = a.get_bb()
     left_b, bottom_b, right_b, top_b = b.get_bb()

     if left_a > right_b:
     #    a.setPosX(a.getDistance())
         return False
     if right_a < left_b:
     #    a.setPosX(a.getDistance())
         return False
     if top_a < bottom_b:
     #    a.setPosY(a.getDistance())
         return False
     if bottom_a > top_b:
     #    a.setPosY(a.getDistance())
         return False

     return True



def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            player.handle_event(event)

current_time = 0.0



def update(frame_time):
    global out_tile,out_tiles,in_tile,in_tiles,road,roads
    global count

    out_tiles = out_tile.create_out_tile() #Character Frame 조절을 위해 여기둠

    for blue_jewelry in blue_jewelrys:
        if collide(player, blue_jewelry):
           blue_jewelrys.remove(blue_jewelry)
           player.get_BJ()

    for yellow_jewelry in yellow_jewelrys:
        if collide(player, yellow_jewelry):
           yellow_jewelrys.remove(yellow_jewelry)
           player.get_YJ()

    for red_jewelry in red_jewelrys:
        if collide(player, red_jewelry):
           red_jewelrys.remove(red_jewelry)
           player.get_RJ()

    for green_jewelry in green_jewelrys:
        if collide(player, green_jewelry):
           green_jewelrys.remove(green_jewelry)
           player.get_GJ()




    for in_tile in in_tiles:
       if collide(player,in_tile):
           if player.state == player.LEFT_MOVE and (player.bf_state != player.DOWN_MOVE or player.bf_state != player.UP_MOVE): #Collison 보정
               if player.x > in_tile.x:
                   player.leftCollide_Player()
                   player.bf_state = player.LEFT_MOVE

           if player.state == player.RIGHT_MOVE and (player.bf_state != player.DOWN_MOVE or player.bf_state != player.UP_MOVE): #Collison 보정
               if player.x < in_tile.x:
                   player.rightCollide_Player()
                   player.bf_state = player.RIGHT_MOVE

           if player.state == player.UP_MOVE and (player.bf_state != player.LEFT_MOVE or player.bf_state != player.RIGHT_MOVE): #Collison 보정
               if player.y < in_tile.y:
                   player.upCollide_Player()
                   player.bf_state = player.UP_MOVE

           if player.state == player.DOWN_MOVE and (player.bf_state != player.LEFT_MOVE or player.bf_state != player.RIGHT_MOVE): #Collison 보정
               if player.y > in_tile.y:
                   player.downCollide_Player()
                   player.bf_state = player.DOWN_MOVE


       if collide(ai_1,in_tile):
              if (ai_1.state == ai_1.RIGHT_MOVE):
                  if ai_1.x < in_tile.x:
                      ai_1.x-=5
                      ai_1.state=random.randint(1,4)
              elif (ai_1.state == ai_1.UP_MOVE):
                  if ai_1.y < in_tile.y:
                      ai_1.y-=5
                      ai_1.state=random.randint(1,4)
                  while 1:
                    if(ai_1.state == ai_1.UP_MOVE):
                        ai_1.state=random.randint(1,4)
                    else:
                        break;
              elif (ai_1.state == ai_1.LEFT_MOVE):
                  if ai_1.x > in_tile.x:
                      ai_1.x+=5
                      ai_1.state=random.randint(1,4)
                  while 1:
                     if(ai_1.state == ai_1.LEFT_MOVE):
                         ai_1.state=random.randint(1,4)
                     else:
                        break;
              elif (ai_1.state == ai_1.DOWN_MOVE):
                   if ai_1.y > in_tile.y:
                       ai_1.y+=5
                       ai_1.state=random.randint(1,4)


       if collide(ai_2,in_tile):
              if (ai_2.state == ai_2.RIGHT_MOVE):
                  if ai_2.x < in_tile.x:
                      ai_2.x-=5
                      ai_2.state=random.randint(1,4)
              elif (ai_2.state == ai_2.UP_MOVE):
                  if ai_2.y < in_tile.y:
                      ai_2.y-=5
                      ai_2.state=random.randint(1,4)
                  while 1:
                    if(ai_2.state == ai_2.UP_MOVE):
                        ai_2.state=random.randint(1,4)
                    else:
                        break;
              elif (ai_2.state == ai_2.LEFT_MOVE):
                  if ai_2.x > in_tile.x:
                      ai_2.x+=5
                      ai_2.state=random.randint(1,4)
                  while 1:
                     if(ai_2.state == ai_1.LEFT_MOVE):
                         ai_2.state=random.randint(1,4)
                     else:
                        break;
              elif (ai_2.state == ai_2.DOWN_MOVE):
                   if ai_2.y > in_tile.y:
                       ai_2.y+=5

                       ai_2.state=random.randint(1,4)

       if collide(ai_3,in_tile):
              if (ai_3.state == ai_3.RIGHT_MOVE):
                  if ai_3.x < in_tile.x:
                      ai_3.x-=5
                      ai_3.state=random.randint(1,4)
              elif (ai_3.state == ai_3.UP_MOVE):
                  if ai_3.y < in_tile.y:
                      ai_3.y-=5
                      ai_3.state=random.randint(1,4)
                  while 1:
                    if(ai_3.state == ai_3.UP_MOVE):
                        ai_3.state=random.randint(1,4)
                    else:
                        break;
              elif (ai_3.state == ai_3.LEFT_MOVE):
                  if ai_3.x > in_tile.x:
                      ai_3.x+=5
                      ai_3.state=random.randint(1,4)
                  while 1:
                     if(ai_3.state == ai_3.LEFT_MOVE):
                         ai_3.state=random.randint(1,4)
                     else:
                        break;
              elif (ai_3.state == ai_3.DOWN_MOVE):
                   if ai_3.y > in_tile.y:
                       ai_3.y+=5
                       ai_3.state=random.randint(1,4)


       if collide(ai_4,in_tile):
              if (ai_4.state == ai_4.RIGHT_MOVE):
                  if ai_4.x < in_tile.x:
                      ai_4.x-=5
                      ai_4.state=random.randint(1,4)
              elif (ai_4.state == ai_4.UP_MOVE):
                  if ai_4.y < in_tile.y:
                      ai_4.y-=5
                      ai_4.state=random.randint(1,4)
                  while 1:
                    if(ai_4.state == ai_4.UP_MOVE):
                        ai_4.state=random.randint(1,4)
                    else:
                        break;
              elif (ai_4.state == ai_4.LEFT_MOVE):
                  if ai_4.x > in_tile.x:
                      ai_4.x+=5
                      ai_4.state=random.randint(1,4)
                  while 1:
                     if(ai_4.state == ai_4.LEFT_MOVE):
                         ai_4.state=random.randint(1,4)
                     else:
                        break;
              elif (ai_4.state == ai_4.DOWN_MOVE):
                   if ai_4.y > in_tile.y:
                       ai_4.y+=5
                       ai_4.state=random.randint(1,4)







    player.update(frame_time)
    ai_1.update(frame_time)
    ai_2.update(frame_time)
    ai_3.update(frame_time)
    ai_4.update(frame_time)



def draw(frame_time):
    clear_canvas()
    background.draw()




    for out_tile in out_tiles:
        out_tile.draw()

    for in_tile in in_tiles:
        in_tile.draw()
        #in_tile.draw_bb()



    for red_jewelry in red_jewelrys:
        red_jewelry.draw()
        #red_jewelry.draw_bb()

    for green_jewelry in green_jewelrys:
        green_jewelry.draw()
        #green_jewelry.draw_bb()

    for yellow_jewelry in yellow_jewelrys:
        yellow_jewelry.draw()
        #yellow_jewelry.draw_bb()

    for blue_jewelry in blue_jewelrys:
        blue_jewelry.draw()


    font.draw(25,590, 'Blue : %d' % (player.BJ_count),(0,0,255))
    font.draw(100,590, 'Red : %d' % (player.RJ_count),(255,0,0))
    font.draw(160,590, 'Yellow : %d' % (player.YJ_count),(255,255,0))
    font.draw(245,590, 'Green : %d' % (player.GJ_count),(0,255,0))



        #blue_jewelry.draw_bb()



    player.draw()
    #player.draw_bb()
    ai_1.draw()
    ai_2.draw()
    ai_3.draw()
    ai_4.draw()







   # print("main Draw -> self.x[5][4] = %d, self.y[5][4] = %d " %(tile.x[5][4],tile.y[5][4]))


    update_canvas()












