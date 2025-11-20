#Know how to position objects on stick figures
#String display
import time

def str_basics():
    
    word = "This is a sentence"
    word2 = ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 's', 'e', 'n', 't', 'e', 'n', 'c', 'e']
    
    for i in range(len(word)):
        win.get_mouse()
        print(word[0:i])
    
    
#str_basics()

def str_advanced():
    
    word = "This is a sentence"
    
    print(word.upper())
    print(word.count("i"))
    print(word.split("s"))
    
str_advanced()