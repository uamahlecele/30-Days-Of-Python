#Exercises: Day 12

#Exercises: Level 1

#1.

import random
import string
def random_user_id(length=6):
    generated_user_id = ""
    strings = string.ascii_letters + string.digits
    user_id =  random.choices(strings,k = length)

    return "".join(user_id)

print(random_user_id())

#2.

def user_id_gen_by_user(length,how_many_ids):
    generated_ids = ""
    
    for i in range(how_many_ids+1):
        strings = string.ascii_letters + string.digits
        user_id =  random.choices(strings,k = length)
        user_id ="".join(user_id)
        # generated_ids= "#"+ user_id+"\n"+generated_ids
        generated_ids+= user_id+"\n"
    return generated_ids

print(user_id_gen_by_user(16,5))

#3.

def rgb_colour_gen():
    rgb= ""
    r= str(random.randint(0,255))
    g= str(random.randint(0,255))
    b= str(random.randint(0,255))
    # rgb = r+","+g+","+b
    return f"rgb({r},{g},{b})"

print(rgb_colour_gen())

#Exercises: Level 2

