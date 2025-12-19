# fruit = "Banana".  Bydefult Input 
# color = "yellow".  Bydefult Input
fruit = input("Enter Your Fruit: ").capitalize()     #User Input
color = input("Enter Your Fruit Color: ").lower()    #User Input

if fruit == "Banana":
    if color == "green":
        print("Unripe")
    elif color == "yellow":
        print("Ripe")
    elif color == "brown":
        print("Overripe")
    else:
        print("Fruit is available, but the entered color is invalid.")
else:
    print("Fruit not available.")

