from graphix import Window, Point, Rectangle, Circle, Polygon, Text

def main():
    
    MAX = 500
    win = Window("New Window", MAX, MAX)
    
    for y0 in range(50, MAX, 100):
        for x0 in range(50, MAX, 100):
            
            p0 = Point(x0,y0)
    
            p = win.get_mouse()
            x = p.x
            y = p.y

            cir = Circle(p0, 50)

            if x > 250 and y > 250:
                cir.fill_colour = "red"
            elif x > 250 and y < 250:
                cir.fill_colour = "blue"
            elif x < 250 and y > 250:
                cir.fill_colour = "green"
            else:
                cir.fill_colour = "yellow"

            cir.draw(win)


main()
