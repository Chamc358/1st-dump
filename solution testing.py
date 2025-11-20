from graphix import Window, Point, Line, Circle, Rectangle, Text

def the_painter():
    win = Window("The Painter (small)", 320, 240)

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

    # Brush (short line at right hand)
    brush = Line(Point(135, 95), Point(155, 90))
    brush.outline_width = 3
    brush.outline_colour = "brown"   # corrected colour to match task
    brush.draw(win)

    # Paint tin on floor -- repositioned under the brush tip
    tin = Rectangle(Point(130, 160), Point(180, 190))
    tin.fill_colour = "light grey"
    tin.outline_colour = "black"
    tin.draw(win)

    # Paint drop near brush tip (still aligned horizontally)
    drop = Circle(Point(155, 95), 4)
    drop.fill_colour = "blue"
    drop.outline_colour = "blue"
    drop.draw(win)

    # Text builds up on each click
    line = "Drip!"
    text = Text(Point(200, 40), "")
    text.size = 20
    text.draw(win)

    # One click per character; drop falls ~12 px per click
    for i in range(len(line)):
        win.get_mouse()
        text.text = line[:i+1]
        drop.move(0, 12)

    # Final click, then undraw the drop (lands in tin)
    win.get_mouse()
    drop.undraw()
    # Close window
    win.get_mouse()
    win.close()

the_painter()

