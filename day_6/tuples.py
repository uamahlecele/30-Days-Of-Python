#Exercises: Day 6

#Exercises: Level 1

#1.
my_tuple = ()

#2.
family_brothers = ("Mpilo","Andile","Sihle")
family_sisters = ("Zoë","Lisa","Sne")

#3.
siblings = family_brothers + family_sisters

#4.
print("Number of siblings:",len(siblings))

#5.
family_members = list(siblings)
family_members.append("Sipho")
family_members.append("Thandazile")
family_members = tuple(family_members)
print(family_members)

#Exercises: Level 2

#1.

#2.

fruits = ("Apple","Mango","Banana","Orange","Peach")
vegitables = ("Carrot","Broccoli","Potatoes","Onions","Beetroot")
animals = ("Beef","Chicken","Pork","Lamb","Fish")
food_stuff_tp = fruits + vegitables + animals

#3.
food_stuff_li = list(food_stuff_tp)

#4.
print("Middle Item:",food_stuff_li[len(food_stuff_li)//2])

#5.
print("First 3:",food_stuff_li[:3])
print("Last 3:",food_stuff_li[-4:-1])

#6.

del food_stuff_tp

#7.

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("Estonia" in nordic_countries)

print("Iceland" in nordic_countries)

