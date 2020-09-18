print("1. Personal Information")
print()
Name = "Danielle Corbee"
Adress = "Cantatestraat 89 Nijmegen Gelderland 6455 VV"
Phone_number = "0639533461"
College_major = "bioinformatics"

print(Name)
print(Adress)
print(Phone_number)
print(College_major)

#Hier wordt mijn persoonlijke informatie geprint

print()
print("2. Sales prediction")
print()

sales = int(input("How many sales have been made?"))
annual_profit = float(sales * 0.23)
print("The annual profit is:")
print(annual_profit)

#Hiermee word gevraagd wat de sales waren en de profit mee uitgerekend

print()
print("Total purchase")
print()

item_1 = int(input("what is the price of the first item?"))
item_2 = int(input("What is the price of the second item?"))
item_3 = int(input("What is the price of the third item?"))
item_4 = int(input("What is the price of the fourth item?"))
item_5 = int(input("what is the price of the fifth item?"))

#Er word gevraagd naar de prijzen om later mee verder te rekenen

price_no_tax = float(item_4 + item_5 + item_3 + item_2 + item_1)
price_of_tax = float(price_no_tax * 0.23)
price_total = float(price_no_tax + price_of_tax)

#Hier worden de berekeningen berekend

print("The price without tax:")
print(price_no_tax)
print("price of the tax:")
print(price_of_tax)
print("total price:")
print(price_total)

#Hiermee worden de waarde's ge-displayed

print()
print("5. Distance traveled")
print()

speed = (70)
time_1 = (6)
time_2 = (10)
time_3 = (15)

#Dit zijn de gegeven waarde's

print("this is the distance traveled in 6 hours:")
print(speed * time_1)
print("this is the distance traveled in 10 hours:")
print(speed * time_2)
print("this is the distance traveled in 15 hours:")
print(speed * time_3)

#Hier worden de afstanden berekend

print()
print("7. Miles per gallon")
print()

miles = float(input("how many miles have been driven?"))
gallons = float(input("how many gallons have been used?"))

#Er word gevraagd hoeveel miles en gallons er zijn

MPG = float(miles / gallons)
print("mpg is:")
print(MPG)

#Hiermee word de MPG berekend

print()
print("10. Ingredient adjuster")
print()

cookies = int(input("How many cookies do you want to make?"))
sugar = float((1.5 / 48) * cookies)
butter = float((1 / 48) * cookies)
flour = float((2.75 / 48) * cookies)

#Hier worden de ingredïenten berkend

print("This is how much sugar:")
print(sugar)
print("This is how much butter:")
print(butter)
print("This is how much flour:")
print(flour)

#Dit zijn de hoeveelheden die nodig zijn voor x cookies