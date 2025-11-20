from graphix import Window, Circle, Point

def draw_circle(win, centre, colour, outline, radius):
    circle = Circle(centre, radius)
    circle.fill_colour = colour
    circle.outline_colour = outline
    circle.draw(win)
    

def colour_selector3(x, y):
    if x > 300 and y > 300:
        return "pink"

    elif x > 300 and y < 300:
        return "blue"
    
    else:
        return "white"
    
def outline_selector(x, y):
    if x < 300 and y < 300:
        return "blue"
    
    elif x < 300 and y > 300:
        return "pink"
    
    else:
        return "black"
    
    
def draw_circles():
    win = Window("Window", 600, 600)
    
    radius = 30
    
    for i in range(12):
        centre = win.get_mouse()
        x = centre.x
        y = centre.y
        
        colour = colour_selector3(x, y)
        outline = outline_selector(x, y)
        
        draw_circle(win, centre, colour, outline, radius)
        
    win.get_mouse()
    win.close()
    
draw_circles()    
        
def draw_circles2():
    win = Window("Window", 600, 600)
    
    radius = 30
    
    for y in range(450, 600, 60):
        for x in range(30, 600, 60):
            p = win.get_mouse()
            colour = colour_selector3(p.x, p.y)
            outline = outline_selector(p.x, p.y)
            centre = Point(x, y)
        
            draw_circle(win, centre, colour, outline, radius)
        
    win.get_mouse()
    win.close()
        
        
