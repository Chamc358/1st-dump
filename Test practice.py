from graphix import Window, Point, Line, Circle

def draw_stick_figure():
    win = Window("Stick Figure", 320, 240)

    # Stick figure
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



    #insert code here

    win.get_mouse()
    win.close()

draw_stick_figure()
