from graphix import Window, Text, Point, Rectangle

def personal_greeting():
    name = input("Enter your name: ")
    print("Hello " + name + ", nice to see you!")
    

def formal_name():
    first_name = input("Enter first name: ")
    surname = input("Enter surname: ")
    print(first_name[0:1] + "." + surname)



    

def generate_email():
    first = input("Enter first name: ")
    surname = input("Enter second name: ")
    year = input("Enter year of entry: ")
    
    first = first.lower()
    surname = surname.lower()
    
    print(surname[0:3]+"."+first[0]+"."+year[2:]+"@myport.ac.uk")
    

def grade_test():
    grades = "FFFFCCBBAAA"
    score = int(input("Enter score: "))
    print("Your grade is: "+(grades[score]))
    

def graphic_letters():
    MAX = 600
    word = input("Enter a word: ")
    win = Window("New Window", MAX, MAX)
    
    instructions = Text(Point(250, 20), "Click to add each letter")
    instructions.draw(win)
    
    for character in word:
        click_point = win.get_mouse()
        text = Text(click_point, character)
        text.size = 30
        text.draw(win)
        
        
    win.get_mouse()
    win.close()


def sing_a_song():
    word = input("Enter a word: ")
    lines = int(input("Enter number of lines: "))
    repeat = int(input("Enter number of repeats: "))
    
    for i in range(lines):
        print((word + "  ") * repeat)
            
            
def exchange_table():
    euros_to_pounds = 1/1.17
    for i in range(0, 21):
        conversion = round(euros_to_pounds*i, 2)
        print(conversion, i)
        

def make_initialism():
    phrase = input("Enter a phrase: ")
    split = phrase.split()
    final = []
    for words in split:
        letter = words[0]
        final.append(letter)
        
    letters = ("".join(final))
    print(letters.upper())
    

def file_in_caps():
    file_name = input("Enter file name: ")
    inside = open(file_name, "r")
    contents = inside.read()
    print(contents.upper())
    

def total_spending():
    inside = open("spending.txt", "r")
    total = 0
    for line in inside:
        total += float(line.strip())
    print("Total spent:",total)


def name_to_number():
    name = input("Enter your name: ")
    name = name.lower()
    letters = "abcdefghijklmnopqrstuvwxyz"
    total = 0
    for char in name:
        total += letters.index(char) + 1
        
    print(total)    
    
  
def rainfall_chart():
    MAX = 600
    win = Window("New Window", 1300, MAX)
    
    names_x = 100
    names_y = 100
    
    top_left_x = 150
    top_left_y = 75
    bottom_right_x = 175
    bottom_right_y = 125
    
    inside = open("rainfall.txt", "r")
    for line in inside:
        group = line.split()
        city = group[0]
        rainfall = int(group[1])
        
        names = Text(Point(names_x, names_y), city)
        names.draw(win)
        names_y += 50
        
        start_left_x = top_left_x
        start_right_x = bottom_right_x
        for i in range(rainfall):
            numbers = Rectangle(Point(top_left_x, top_left_y), Point(bottom_right_x, bottom_right_y))
            numbers.draw(win)
            numbers.fill_colour = "light blue"
            
            top_left_x += 25
            bottom_right_x += 25
            
        top_left_y += 50
        bottom_right_y += 50
        print(city, ("*") * rainfall)
        
        top_left_x = start_left_x
        bottom_right_x = start_right_x
        
    win.get_mouse()
    win.close()


def rainfall_in_inches():
    file = open("rainfall.txt", "r")
    new_file = open("rainfallInches.txt", "w")

    for line in file:
        parts = line.split()
        city = parts[0]
        mm = float(parts[1])
        inch = mm / 25.4
        result = city + " " + str(round(inch, 2))
        print(result)
        new_file.write(result + "\n")

    file.close()
    new_file.close()


def wc():
    filename = input("Enter filename: ")
    file = open(filename, "r")
    
    lines = 0
    words = 0
    characters = 0
    
    for line in file:
        text = line.split()
        
        lines += 1
        words += len(text)
        characters += len(line)
        
    print(lines)
    print(words)
    print(characters)
    
    
        
        
        
        
        
        
        

