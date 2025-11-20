def painted_wall():
    L = float(input("What is the length of the rectangular wall in cm: "))
    H = float(input("What is the height of the rectangular wall in cm: "))
    W = float(input("What is the width of the rectangular window in cm: "))
    Y = float(input("What is the height of the rectangular window in cm: "))
    
    wall_area = L * H
    window_area = W * Y
    paintable = wall_area - window_area
    
    number_cans = int((paintable + 2000 - 1 / 2000))
    price = number_cans * 12
    
    print("The total wall area is ", wall_area, "cm^2")
    print("The total window area is ", window_area, "cm^2")
    print("The paintable wall area is ", paintable, "cm^2")
    print("Tahe number of tins required is", (round(number_cans)))
    print("The total cost of paint is £", round(price,2))