from graphix import Window, Rectangle, Circle, Point, Line
import time

def draw_car():
    
    win = Window("Moving Car", 700, 400)
    
    tl = Point(100, 100)
    br = Point(200, 150)
    
    centre_top = Point(150, 100)
    radius_top = 40
    
    top = Circle(centre_top, radius_top)
    top.draw(win)
    top.fill_colour = "lightblue"
    
    car_body = Rectangle(tl,br)
    car_body.draw(win)
    car_body.fill_colour = "lightblue"
    
    centre1 = Point(120, 150)
    radius = 10
    
    wheel1 = Circle(centre1, radius)
    wheel1.draw(win)
    wheel1.fill_colour = "black"
    
    centre2 = Point(170, 150)
    
    wheel2 = Circle(centre2, radius)
    wheel2.draw(win)
    wheel2.fill_colour = "black"
    
    road_left = Point(10, 160)
    road_right = Point(300, 160)
    
    road = Line(road_left, road_right)
    road.draw(win)
    
    
    
    tl = Point(100, 200)
    br = Point(200, 350)
    
    centre_top = Point(150, 300)
    radius_top = 40
    
    top = Circle(centre_top, radius_top)
    top.draw(win)
    top.fill_colour = "lightblue"
    
    car_body = Rectangle(tl,br)
    car_body.draw(win)
    car_body.fill_colour = "lightblue"
    
    centre1 = Point(120, 350)
    radius = 10
    
    wheel1 = Circle(centre1, radius)
    wheel1.draw(win)
    wheel1.fill_colour = "black"
    
    centre2 = Point(170, 350)
    
    wheel2 = Circle(centre2, radius)
    wheel2.draw(win)
    wheel2.fill_colour = "black"
    
    road_left = Point(10, 360)
    road_right = Point(300, 360)
    
    road = Line(road_left, road_right)
    road.draw(win)
    
    car1 = [car_body, wheel1, wheel2, top]
    car2 = [car_body, wheel1, wheel2, top]
    
    for _ in range(200):
        #win.get_mouse()
        time.sleep(0.01)
        for part in car1:
            part.move(1,0)
            
    for _ in range(200):
    #win.get_mouse()
        time.sleep(0.01)
        for part in car2:
            part.move(2,0)
    
    
    
    
    win.get_mouse()
    win.close()
    
draw_car()