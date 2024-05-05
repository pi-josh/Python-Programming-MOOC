# Write your solution here
while True:
    editor = input("Editor: ").lower()
    
    if editor == "visual studio code":
        print("an excellent choice!")
        break
    elif editor == 'word' or editor == 'notepad':
        print("awful")
        continue
    else:
        print("not good")