def main():
    colours = ["red", "blue", "green"]
    sizes = [2, 3, 4]
    
    colours2 = []
    
    while True:
        colour = input("colour please: ")
        
        if colour in colours:
            colours2.append(colour)
            break
    
    
    while True:
        size = int(input("size please: "))
        
        if size in sizes:
            screen_size = size
            break
        
    
    
    
    print(colours2)
    print(screen_size)
    
    
    
main()