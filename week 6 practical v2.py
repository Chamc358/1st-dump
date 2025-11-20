from graphix import Window, Point, Rectangle, Circle, Polygon, Text

def draw_circle(win, centre, colour, radius):
    cir = Circle(centre, radius)
    cir.fill_colour = colour
    cir.draw(win)

def main():
    
    MAX = 500
    win = Window("New Window", MAX, MAX)
    
    for i in range(10):
    
        p = win.get_mouse()
        
        x = p.x
        y = p.y
        
        if x > 250 and y > 250:
            draw_circle(win, p, "red", 50)
        elif x > 250 and y < 250:
            draw_circle(win, p, "blue", 50)

        elif x < 250 and y > 250:
            draw_circle(win, p, "green", 50)
        else:
            draw_circle(win, p, "yellow", 50)


    win.get_mouse()
    win.close()



main()