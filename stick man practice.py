from graphix import Window, Point, Line, Circle, Rectangle, Text

def draw_stick_figure():
    win = Window("Stick Figure", 320, 240)

    head = Circle(Point(100, 60), 20)
    head.draw(win)

    body = Line(Point(100, 80), Point(100, 130))
    body.draw(win)

    arm_l = Line(Point(100, 90), Point(70, 100))
    arm_l.draw(win)

    arm_r = Line(Point(100, 90), Point(135, 95))
    arm_r.draw(win)

    leg_l = Line(Point(100, 130), Point(80, 180))
    leg_l.draw(win)

    leg_r = Line(Point(100, 130), Point(120, 180))
    leg_r.draw(win)

    string = Line(Point(135, 95), Point(150, 50))
    string.draw(win)
    
    lin1 = Line(Point(150, 50), Point(130, 30))
    lin2 = Line(Point(150, 10), Point(130, 30))
    lin3 = Line(Point(170, 30), Point(150, 10))
    lin4 = Line(Point(170, 30), Point(150, 50))
    
    lin1.draw(win)
    lin2.draw(win)
    lin3.draw(win)
    lin4.draw(win)
    
    for i in range(3):
        win.get_mouse()
        string.move(10, -15)
        lin1.move(10, -15)
        lin2.move(10, -15)
        lin3.move(10, -15)
        lin4.move(10, -15)
    
    win.get_mouse()
    word = Text(Point(50, 60), "Whee!")
    word.draw(win)
    
    win.get_mouse()
    string.undraw()
    lin1.undraw()
    lin2.undraw()
    lin3.undraw()
    lin4.undraw()

    win.get_mouse()
    win.close()

draw_stick_figure()



from graphix import Window, Point, Line, Circle, Rectangle, Text

def draw_stick_figure():
    win = Window("Stick Figure", 320, 240)

    head = Circle(Point(100, 60), 20)
    head.draw(win)

    body = Line(Point(100, 80), Point(100, 130))
    body.draw(win)

    arm_l = Line(Point(100, 90), Point(70, 100))
    arm_l.draw(win)

    arm_r = Line(Point(100, 90), Point(135, 95))
    arm_r.draw(win)

    leg_l = Line(Point(100, 130), Point(80, 180))
    leg_l.draw(win)

    leg_r = Line(Point(100, 130), Point(120, 180))
    leg_r.draw(win)

    string = Line(Point(135, 95), Point(135, 35))
    string.draw(win)
    
    balloon = Circle(Point(135, 20), 15)
    balloon.draw(win)
    balloon.fill_colour = "red"
    
    basket = Rectangle(Point(140, 150), Point(225, 180))
    basket.draw(win)
    basket.fill_colour = "brown"
    
    for i in range(4):
        win.get_mouse()
        string.move(0, -20)
        balloon.move(0, -20)
        
    word = Text(Point(200, 20),"Bye!")
    word.draw(win)
    
    win.get_mouse
    balloon.undraw()
    string.undraw()
    
    win.get_mouse()
    win.close()

draw_stick_figure()





