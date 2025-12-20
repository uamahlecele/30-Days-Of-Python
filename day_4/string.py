# Day 4 of 30 Days of Python:

#Exercises - Day 4

#1.

print("Thirty "+"Days " +"Of "+ "Python")

#2.

one_string="Coding "+"For "+"All "
print(one_string)

# #3.
company= "Coding For All"

#4.
print(company)

#5.
print(len(company))

#6. 
print(company.upper())

#7.
print(company.lower())

#8.

print(company.title())
print(company.capitalize())
print(company.swapcase())

#9.

print(company[7:])

#10.

print(company.find("Coding"))

#11.

new_string = company.replace("Coding","Python")
print(new_string)

#12.

print(new_string.replace("for Everyone","Python for All"))

#13.
print(company.split(" "))

#14.

tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_companies.split(","))

#15.
print(company[0])

#16.
print(company[-1])

#17.

print(company[10])

#18.

p = 'Python For Everyone'
print(p[0],p[7],p[11])

#19.

p2= 'Coding For All'
print(p2[0],p2[7],p2[11])

#20.

print(company.index("C"))

#21.
print(company.index("F"))

#22.
phrase = "Coding For All People"
print(phrase.rindex("i"))

#23.

sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.rindex("because"))

#24.
print(sentence.replace("because",""))

#25.

print(sentence.index("because"))

#28.

print(company.startswith("Coding"))

#29.
print(company.endswith("coding"))

#30.

print('   Coding For All      '  .strip())

#31.

print("30DaysOfPython".isidentifier())

#32.

the_list =['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

print(" # ".join(the_list))

#33.

print("I am enjoying this challenge.\tI just wonder what is next.")

#34.

print("Name\tAge\tCountry\t\tCity\nAmahle\t24\tSouth Africa\tPinetown")

#35. 
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square".format(radius,area)) #this is kinda sexy

#36.
a=8
b=6
print(f"{a+b}\n{a-b}\n{a*b}\n{round(a/b,2)}\n{a%b}\n{a//b}\n{a**b}")
