import pyautogui as pg
import mouse
import math
import time

radius = 400 
        
def DrawCircle():
    time.sleep(5)
    print('Five seconds left!')
    time.sleep(5)
    print('Drawing...')
    px = 961
    py = 516
    pg.mouseDown(px, py - radius, button='left')
    angle = 360
    
    while angle >= 0:
        x, y = GetXY(angle)
        mouse.move((px + x), (py - y), duration = 0.005)
        angle -= 1
    pg.mouseUp()
    print('Thank LilyLambda!')
           
def GetXY(angle):
    x = radius * math.sin(math.pi * 2 * angle / 360)
    y = radius * math.cos(math.pi * 2 * angle / 360)
    return (x, y)
   
DrawCircle()