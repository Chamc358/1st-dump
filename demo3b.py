from graphix import Window, Point, Rectangle, Line, Circle

def grid():
    MAX = 600
    STEP = 100
    
    win = Window("New Window", MAX, MAX)
    
    for y in range(0, MAX, STEP):
        for x in range(0, MAX, STEP):
            print(x, " ",y)
            
            top_left = Point(x,y)
            bottom_right = Point(x+STEP, y+STEP)
            top_right = Point(x+STEP, y)
            bottom_left = Point(x, y+STEP)
            centre = Point(x+STEP//2, y+STEP//2)
            radius = STEP//2
            
            rec = Rectangle(top_left, bottom_right)
            rec.draw(win)
            rec.fill_colour = "orange"
            
            lin = Line(top_left, bottom_right)
            lin.draw(win)
            
            lin2 = Line(top_right, bottom_left)
            lin2.draw(win)
            
            cir = Circle(centre, radius)
            cir.draw(win)
            cir.fill_colour = "blue"
            
            
    win.get_mouse()
    win.close()


grid()