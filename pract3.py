from graphix import Window, Circle, Point, Line, Rectangle, \
                    Text, Entry

def draw_stick_figure():
    win = Window()
    head = Circle(Point(200, 120), 40)
    head.draw(win)
    body = Line(Point(200, 160), Point(200, 240))
    body.draw(win)
    leg1 = Line(Point(200, 240), Point(250, 320))
    leg1.draw(win)
    leg2 = Line(Point(200, 240), Point(150, 320))
    leg2.draw(win)
    arms = Line(Point(130, 200), Point(270, 200))
    arms.draw(win)
    
    
    
    win.get_mouse()
    win.close()
    
    
def draw_circle():
    radius = int(input("Enter radius: "))
    
    MAX = 400
    win = Window("New Window", MAX, MAX)
    centre = Point(MAX//2, MAX//2)
    
    cir = Circle(centre, radius)
    cir.draw(win)
    
    win.get_mouse()
    win.close()
    
    
def draw_archery_target():
    yellow_radius = 100
    red_radius = 200
    blue_radius = 300
    
    MAX = 620
    
    win = Window("New Window", MAX, MAX)
    centre = Point(MAX // 2, MAX // 2)
    
    cir1 = Circle(centre, blue_radius)
    cir1.draw(win)
    cir1.fill_colour = "blue"
    
    cir2 = Circle(centre, red_radius)
    cir2.draw(win)
    cir2.fill_colour = "red"
    
    cir3 = Circle(centre, yellow_radius)
    cir3.draw(win)
    cir3.fill_colour = "yellow"
    
    win.get_mouse()
    win.close()


def draw_rectangle():
    height = float(input("Enter height of rectangle: "))
    width = float(input("Enter width of rectangle: "))
    
    win = Window("New Window", 400, 400)
    centre_x = 400 // 2
    centre_y = 400 // 2
    
    x1 = int(centre_x - width // 2)
    y1 = int(centre_y - height // 2)
    x2 = int(centre_x + width // 2)
    y2 = int(centre_y + height // 2)
    
    rec = Rectangle(Point(x1, y1), Point(x2,y2))
    rec.draw(win)
    
    win.get_mouse()
    win.close()
    
    
def blue_circle():
    MAX = 600
    win = Window("New Window", MAX, MAX)
    
    centre = win.get_mouse()
    radius = 100
    
    cir = Circle(centre, radius)
    cir.draw(win)
    cir.fill_colour = "blue"
    
    win.get_mouse()
    win.close()


def ten_lines():
    win = Window()
    for _ in range(10):
        message = Text(Point(200, 50), "click on first point")
        message.draw(win)
        p1 = win.get_mouse()
        message.text = "click on second point"
        p2 = win.get_mouse()
        line = Line(p1, p2)
        line.draw(win)
        message.text = ""
    message.text = "click anywhere to quit"
    
    win.get_mouse()
    win.close()
    

def ten_strings():
    win = Window("New Window", 500, 500)
    text_box = Entry(Point(250, 20), 30)
    text_box.draw(win)

    instructions = Text(Point(250, 50), "Type the string you want outputted")
    instructions.draw(win)
    
    for _ in range(10):
        click = win.get_mouse()
        text = text_box.text.strip()
        
        string = Text(click, text)
        string.draw(win)
        
        text_box.text = ""
    instructions.text = ("You have entered all 10 strings,"
                            "click again to exit")
    win.get_mouse()
    win.close()
    

def ten_coloured_rectangles():
    MAX = 500
    win = Window("New Window", MAX, MAX)
    
    text_box = Entry(Point(250, 20), 30)
    text_box.text = ("blue")
    text_box.draw(win)
    
    instructions = Text(Point(250, 50), "Enter the colour of the next rectangle")
    instructions.draw(win)
    
    for _ in range(10):
        top_left = win.get_mouse()
        bottom_right = win.get_mouse()
    
        text = text_box.text.strip()
        
        rec = Rectangle(top_left, bottom_right)
        rec.draw(win)
        rec.fill_colour = text
        
    win.get_mouse()
    win.close()
    

def five_click_stick_figure():
    MAX = 500
    win = Window("New Window", MAX, MAX)
    
    centre = win.get_mouse()
    edge = win.get_mouse()
    
    dx = edge.x - centre.x
    dy = edge.y - centre.y
    radius = int((dx**2 + dy**2)**0.5)
    
    cir = Circle(centre, radius)
    cir.draw(win)
    
    p3 = win.get_mouse()
    body = Line(centre, p3)
    body.draw(win)
  
  
    mid_y = (centre.y + p3.y) // 2
    mid_x = (centre.x + p3.x) // 2
    arm_middle = Point(mid_x, mid_y)
    p4 = win.get_mouse()
    
    mirror_x = 2 * mid_x - p4.x
    mirror_y = p4.y
    replicate_arm = Point(mirror_x, mirror_y)
    
    
    arm1 = Line(arm_middle, p4)
    arm1.draw(win)
    
    arm2 = Line(arm_middle, replicate_arm)
    arm2.draw(win)
    
    p5 = win.get_mouse()
    leg_x = 2 * p3.x - p5.x
    leg_y = p5.y
    replicate_leg = Point(leg_x, leg_y)

    leg1 = Line(p3, p5)
    leg1.draw(win)
    
    leg2 = Line(p3, replicate_leg)
    leg2.draw(win) 
       
    win.get_mouse()
    win.close()



five_click_stick_figure()
    
    
    