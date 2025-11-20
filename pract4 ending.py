
def rainfall_in_inches():
    file = open("rainfall.txt", "r")
    new_file = open("rainfallInches.txt", "w")

    for line in file:
        line = line.strip()
        new_file.write(line + "\n")
        mm = float(line[1])
        inch = mm / 25.4
        print(inch)
        
        print(line)

    file.close()
    new_file.close()

rainfall_in_inches()
"""
def rainfall_in_inches():
    file = open("rainfall.txt", "r")
    new_file = open("rainfallInches.txt", "w")

    for line in file:
        line = line.strip()
        if line:
            parts = line.split()
            city = parts[0]
            mm = float(parts[1])
            inch = mm / 25.4
            result = city + " " + str(round(inch, 2))
            print(result)
            new_file.write(result + "\n")

    file.close()
    new_file.close()

rainfall_in_inches()
"""