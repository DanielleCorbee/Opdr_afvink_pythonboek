print("1. Number Analyser")
print()
number = int(input("Give me a number: "))
total = 0
if number > total:
    print("Positive")
elif number < total:
    print("Negative")
elif number == total:
    print("Zero")
else:
    print("Error")
remainder = number % 2
if remainder == 0:
    print("Even")
else:
    print("Odd")
print()
print("2. Areas of Rectangles")
print()
length1 = int(input("How long is the first rectangle? "))
width1 = int(input("How wide is the first rectangle? "))
length2 = int(input("How long is the second rectangle? "))
width2 = int(input("How wide is the second rectangle? "))
area1 = length1 * width1
area2 = length2 * width2
if area1 > area2:
    print("The first rectangle is bigger")
elif area1 < area2:
    print("the second rectangle is bigger")
elif area1 == area2:
    print("The rectangles are the same size")
else:
    print("Something went wrong...")
print()
print("9. Roulette Wheel Colours")
print()
pocket_number = int(input("Give me a number between 0 and 36: "))
if pocket_number == 0:
    print("Green")
elif pocket_number <= 11:
    if pocket_number % 2 == 0:
        print("Black")
    else:
        print("Red")
elif pocket_number <= 18:
    if pocket_number % 2 == 0:
        print("Red")
    else:
        print("Black")
elif pocket_number <= 28:
    if pocket_number % 2 == 0:
        print("Black")
    else:
        print("Red")
elif pocket_number <= 36:
    if pocket_number % 2 == 0:
        print("Red")
    else:
        print("Black")
else:
    print("I said a number between 0 and 36... smh")
print()
print("17. Wi-Fi Diagnostic Tree")
print()
yes = "yes"
no = "no"
WiFi = input("Is the Wi-Fi working? (yes/no)")
if WiFi == no:
    print("Reboot the computer and try to connect")
    WiFi2 = input("I the Wi-Fi working now? (yes/no)")
    if WiFi2 == no:
        print("Reboot the router and try again")
        WiFi3 = input("Is it working now? (yes/no)")
        if WiFi3 == no:
            print("Make sure the cables inbetween the router and modum are plugged in firmly")
            Wifi4 = input("Is it working now mr. Krabs??? (yes/no)")
            if Wifi4 == no:
                print("Move the router to a new location")
                Wifi5 = input("Pleade tell me, is it working? (yes/no)")
                if Wifi5 == no:
                    print("Get a new router")
                else:
                    print("Trust me you don't want to know the next step")
            else:
                print("Look at you fixing the Wi-Fi... I'm so proud of you")
        else:
            print("Damn that was one hell of a journey")
    else:
        print("She's working now")
else:
    print("Then why are you here???")

print()
print("18. Restaurant Selector")
print()
vegan = input("Is anyone in your party a vegan? (yes/no)")
gluten = input("Is anyone in your party gluten free? (yes/no)")
vegetarian = input("Is anyone in your party vegetarian? (yes/no)")
yes = "yes"
no = "no"
if vegan == gluten == vegetarian == no:
    print("Your options are: ")
    print("Joe's Gourmet Burgers")
    print("Main Street Pizza")
    print("Corner Café")
    print("Mama's Fine Italian")
    print("The Chef's Kitchen")
elif vegan == gluten == vegetarian == yes:
    print("These are your options: ")
    print("Corner Café")
    print("The Chef's Kitchen")
elif vegan == yes:
    print("These are your options: ")
    print("Corner Café")
    print("The Chef's Kitchen")
elif gluten == vegan == yes:
    print("These are your options: ")
    print("Corner Café")
    print("The Chef's Kitchen")
elif gluten == yes:
    print("These are your options: ")
    print("Main Street Pizza")
    print("Corner Café")
    print("The Chef's Kitchen")
elif vegetarian == yes:
    print("These are your options: ")
    print("Main Street Pizza")
    print("Corner Café")
    print("The Chef's Kitchen")
    print("Mama's Fine Italian")
else:
    print("Cook at home then damn")


