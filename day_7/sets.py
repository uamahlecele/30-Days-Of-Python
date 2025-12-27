# Exercises: Day 7

#Exercises: Level 1

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1.

print("Length of IT Companies:",len(it_companies))

#2.

it_companies.add("Twitter")

print("Updated",it_companies)

#3.
new_companies = {"OpenAI","Deepseek","Takealot"}
it_companies.update(new_companies)
print("Added Multiple Co.'s:",it_companies)

#4.

box = it_companies.pop()

print("Removed:",box)

#5.

"""remove() method raises errors when it cannot find the item it is looking for.
    discard() doesn't raise that error."""

#Exercises: Level 2

#1.

C = A.union(B)
print(f"A and B joined: {C}")

#2.

print(f"Intersection: {A.intersection(B)}")

#3.

print(f"Is subset: {A.issubset(B)}")

#4.

print(f"Is disjoint: {A.isdisjoint(B)}")

#5.

print(f"Join A with B: {A.update(B)}")
print(f"Join B with A: {B.update(A)}")

#6.

print(f"Symmetric Difference: {A.symmetric_difference(B)}")

#7.

del A
del B
del it_companies
# del age

#Exercises: Level 3

#1. 
set_age = set(age)

print(set_age)

#2.

#the first 3 are ordered, the last, the set, is not.

#3.

sentence = "I am a teacher and I love to inspire and teach people."
sentence = sentence.split()

print(f"Unique words: {set(sentence)}")
