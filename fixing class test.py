from graphix import Window, Point, Line, Circle, Rectangle, Text

def the_teacher():
    win = Window("Stick figure", 500, 300)
    head = Circle(Point(330, 90), 30)
    head.draw(win)
    body = Line(Point(330, 120), Point(330, 180))
    body.draw(win)
    arm1 = Line(Point(330, 140), Point(270, 120))
    arm1.draw(win)
    arm2 = Line(Point(330, 140), Point(390, 120))
    arm2.draw(win)
    leg1 = Line(Point(330, 180), Point(280, 260))
    leg1.draw(win)
    leg2 = Line(Point(330, 180), Point(380, 260))
    leg2.draw(win)
    
    # board and marker
    board = Rectangle(Point(50, 50), Point(250, 250))
    board.draw(win)
    
    marker = Rectangle(Point(280, 110), Point(300, 140))
    marker.draw(win)
    marker.fill_colour = "blue"
    
    tip = Rectangle(Point(285, 95), Point(295, 110))
    tip.draw(win)
    tip.fill_colour = "blue"
    
    letters = "ABCDEF"
    
    # Create one text object and draw it initially (empty)
    display = Text(Point(150, 150), "")
    display.size = 36
    display.fill_colour = "blue"
    display.draw(win)
    
    for i in range(6):
        win.get_mouse()  # wait for click
        display.undraw()  # remove old letter
        display = Text(Point(150, 150), letters[i])  # new letter
        display.size = 36
        display.fill_colour = "blue"
        display.draw(win)  # draw new letter instantly
          
    win.get_mouse()
    tip.fill_colour = "white"
    win.get_mouse()
    win.close()

the_teacher()