import math
from graphix import Window, Circle

def draw_brown_eye(win, centre, radius):
    draw_circle(win, centre, radius, "white")
    draw_circle(win, centre, int(radius * 0.5), "brown")
    draw_circle(win, centre, int(radius * 0.25), "black")
    
def draw_circle(win, centre, radius, colour):
    circle = Circle(centre, int(radius))
    circle.fill_colour = colour
    circle.outline_width = 2
    circle.draw(win)

def distance_between_points(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    return math.sqrt(dx**2 + dy**2)

def distance_calculator(p1, p2):
    # Just compute and return the distance
    return distance_between_points(p1, p2)

def draw_four_pairs_of_brown_eyes():
    MAX = 500
    win = Window("4 pairs of eyes", MAX, MAX)
    
    for _ in range(4):
        left_eye_centre = win.get_mouse()
        p2 = win.get_mouse()
        
        radius = distance_calculator(left_eye_centre, p2)
        draw_brown_eye(win, left_eye_centre, radius)
        
    win.get_mouse()
    win.close()
    
draw_four_pairs_of_brown_eyes()