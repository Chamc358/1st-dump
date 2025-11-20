from graphix import Window, Circle, Rectangle

def main():
    win = Window("oo! a window!", 500, 500)
    
    for _ in range(10):
        p = win.get_mouse()
        #x = p.x
        #y = p.y
        #print("x: ",x,"y: ",y)
        #p.draw(win)
        radius = 50
        cir = Circle(p, radius)
        cir.draw(win)
        cir.fill_colour = "blue"
        
        p2 = win.get_mouse()
        
        rec = Rectangle(p, p2)
        rec.draw(win)
        rec.fill_colour = "red"
        
    win.get_mouse()
    win.close()
    
    
    
    
    
    

main()