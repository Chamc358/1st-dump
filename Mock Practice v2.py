#V2 basically task 1
#V3 basically task 2
from graphix import Window, Circle, Point

def draw_circle(win, centre, colour, radius):
    circle = Circle(centre, radius)
    circle.fill_colour = colour
    circle.draw(win)
    
def colour_selector1(x, y):
    if y < 200:
        return "blue"
    elif y < 400:
        return "red"
    else:
        return "yellow"
    
    
def colour_selector2(x, y):
    if x < 200:
        return "blue"
    elif x < 400:
        return "red"
    else:
        return "yellow"
    

def colour_selector3(x, y):
    if x > 250 and y > 250:
        return "red"

    elif x > 250 and y < 250:
        return "blue"
    
    elif x < 250 and y > 250:
        return "green"
    else:
        return "yellow"
    
    


    
def main():
    win = Window("Window", 600, 600)
    
    radius = 20
    
    for i in range(10):
        centre = win.get_mouse()
        x = centre.x
        y = centre.y
        
        colour = colour_selector1(x, y)
        
        draw_circle(win, centre, colour, radius)
        
    win.get_mouse()
    win.close()
        
        
main()
