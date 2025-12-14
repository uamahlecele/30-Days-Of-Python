"""This is my day one submission of the exercises demanded of me for the 30 Day Challenge.
I am proud ukuthi I made it this far and solved all of the questions"""

print("Exercise Level 2:")
print("")
print("addition:",3+4)
print("subtraction:",3-4)
print("multiplication:",3*4)
print("modulus:",3%4)
print("division:",3/4)
print("exponential:",3**4)
print("floor division:",3//4)

print("")
name,family_name,country="Amahle", "Cele", "South Africa"
print("Name:",name)
print("Family Name:",family_name)
print("Country:",country)
print("I am enjoying 30 days of python")

print("Check the data types of the following data\n")

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type(name))
print(type(family_name))
print(type(country))

print("Exercise Level 3:")
print("")
print(type(True))
print(type(False))
print(type((4,7,65,9.75)))

print("")

print("Calculate the Euclidian Distance between (2,3) and (10,8)\n")

x1,y1=2,3
x2,y2= 10,8

E_Distance = ((x2-x1)**2)+((y2-y1)**2)

print("Answer:",round(E_Distance**0.5,2))


"""Notes:
I learnt that I can find the square of a number in python by raising it to the power (**) of 1/2"""