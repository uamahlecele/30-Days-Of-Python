#Exercises: Level 1

#Day 2: 30 Days of python programming

first_name = "Amahle"
last_name = "Cele"
full_name = "Amahlemandosi"
country = "The Republic of South Africa"
city = "Pinetown"
age = 24
year = 2025
is_married = False
is_true = False
is_light_on = False

favourite_food, industry ="Miltart", "Technology, Creative"

#Exercises: Level 2

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(favourite_food))
print(type(industry))

print("Length of my first name:",len(first_name))
print(f"first name length: {len(first_name)} vs last name length: {len(last_name)}")

num_one,num_two = 5,4
total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

#A= Pi x r square 2

radius = 30
area_of_circle = 3.14159*(radius)**2

#C=2 x Pi x r
circum_of_circle = 2*3.14159*radius
# print("Area:",round(area_of_circle,2))
# print("Circum:",round(circum_of_circle,2))

#user input is the radius

user_radius= float(input("Enter your radius value: "))
area_of_circle = 3.14159*(user_radius)**2
print("Area:",round(area_of_circle,2))

#user input and assign to corresponding variables

first_name = input("Name: ")
last_name = input("Surname: ")
country = input("Country: ")
age = int(input("Age: "))

print("")

print(f"Hi there {first_name}! I see you're from {country}. Interesting place! Mr/Mrs. {last_name} you are {age} years old.")


help('keywords')

