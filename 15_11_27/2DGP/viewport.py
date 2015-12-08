__author__ = 'Administrator'

from pico2d import *

center_object = None
background = None
left, bottom, width, height = None, None, None, None

#step 3

def set_center_object(co):
    global center_object
    center_object = co

def set_background(bg):
    global background
    background = bg

def update(t):
    global left,bottom,width,height
    width = get_canvas_width()
    height = get_canvas_height()
    left = clamp (0,int(center_object.x) - width/2, background.width - width)
    bottom = clamp ( 0,int(center_object.y) - height/2,background.height - height)

def draw() :
    debug_print('l = %d, b= %d,w = %d, h = %d' %(left,bottom,width,height))
