from graphix import Window, Point, Line, Circle, Rectangle, Text

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

    tl_tin = Point(130, 160)
    br_tin = Point(180, 190)
    tin = Rectangle(tl_tin, br_tin)
    tin.draw(win)
    tin.fill_colour = "light grey"
    tin.outline_colour = "black"

    paint_brush = Line(Point(135, 95), Point(155, 90))
    paint_brush.draw(win)
    paint_brush.fill_colour = "brown"
    paint_brush.outline_width = 3
    
    paint_drop = Circle(Point(155, 94), 3)
    paint_drop.draw(win)
    paint_drop.fill_colour = "blue"
    
    line = "Drip!"
    word_on_screen = Text(Point(200, 40), "")
    word_on_screen.size = 20
    word_on_screen.draw(win)
    for i in range(6):
        win.get_mouse()
        word_on_screen.text = line[:i+1]
        paint_drop.move(0,12)
    paint_drop.undraw()
        
        
        

    win.get_mouse()
    win.close()

draw_stick_figure()
