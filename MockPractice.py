#V2 basically task 1
#V3 basically task 2
from graphix import Window, Circle, Point

def draw_circle(win, centre, colour, radius):
    circle = Circle(centre, radius)
    circle.fill_colour = colour
    circle.draw(win)
    
def main():
    win = Window("Window", 500, 500)
    
    colour = "blue"
    radius = 20
    
    for i in range(10):
        centre = win.get_mouse()
        draw_circle(win, centre, colour, radius)
        
    win.get_mouse()
    win.close()
        
        
main()