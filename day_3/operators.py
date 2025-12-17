#Exercises - Day 3:

age = 24
height = 1.76
complex_num = 2+7j

b = int(input("Enter base: "))
h = int(input("Enter height: "))
area = 0.5 * b * h
print(f"The area of the triangle is {int(area)}")

#perimeter:

side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print(f"The perimeter of the triangle is {perimeter}")

#area of rectangle:

length = int(input("Length: "))
width = int(input("Width: "))
rect_area = length * width
rect_perimeter = 2 * (length + width)
print("")
print(f"Rectangle Area {rect_area}")
print(f"Rectangle Perimeter {rect_perimeter}\n")

#Circle radius:

radius = float(input("Radius: "))
area_of_circle = 3.14 * radius**2
circum_of_circle = 2 * 3.14 * radius
print(f"Area of circle: {round(area_of_circle,2)}")
print(f"Circum of circle: {round(circum_of_circle,2)}")


#Calculating the slope:

# y = 2j-2

#skipping 8,9,10,11

#12. 

if len("python") == len("dragon"):
    print(f"The words are exactly the same length {len("python")}")

#13.

if "on" in "dragon" and "python":
    print("True!")
else:
    print("False!")

#14. 

if "jargon" in "I hope this course is not full of jargon":
    print("True! There's jargon.")
else:
    print("False! No jargon.")

#15.

if not("on" in "dragon" and "python"):
    print("False.")
else:
    print("True.")

#16.

print(str(float(len("python"))))

#17. 

user_num = int(input("Find out if your number is even: "))

if user_num % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")

#18.

if 7//3 == int(2.7):
    print("Equal")
else:
    print("Not equal")

#19.

if '10' == 10:
    print("True, they are the same")
else:
    print("False, they are not")

#20.
if int('9.8') == 10:
    print("Equal")
else:
    print("Not Equal")

21.

u_hours =int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
earnings = u_hours *rate
print(f"Your weekly earning is {earnings}")

#22.

years = int(input("Enter number of years you have lived: "))
seconds_lived = years * 31536000
print(f"You have lived for {seconds_lived} seconds.")

#23.

print("1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125")
