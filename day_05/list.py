#Day 5 of 30 Days Python

#Exercises: Day 5

#1.

empty_list = []

#2.

list_five = ["Amahlemandosi", "Cele", "Creative Director", 24, "Single"]

#3.
print(list_five)
print(len(list_five))

#4.

# *rest unpacks whatever might be outstanding in a list

print(list_five[0],list_five[2], list_five[-1])

#5.

mixed_data_types = ["Amahlemandosi Thabo",24,"1.76 Meters", "Single", "236 Mfeme Road"]

#6.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7.

print(f"IT Companies:",it_companies)

#8.

print("No. of companies:", len(it_companies))

#9.

print("First, Middle, Last:", it_companies[0],it_companies[4],it_companies[-1])

#10.

it_companies[0] = "Khumbuza"
print(it_companies)

#11.

it_companies.append("Velaphi")
print(it_companies)

#12.

it_companies.insert(4,"A24")
print(it_companies)

#13.

print(it_companies[-1].upper())

#14.

print("#".join(it_companies))

#15.


for i in it_companies:
    company = "Velaphi"
    if i == company:
        print("Exists")
        break
    else:
        continue

#16.

print(sorted(it_companies))

#17.

print(*reversed(it_companies))

#18.

print(it_companies[0:3])

#19.

print(it_companies[-4:-1])

#20.

print(it_companies[4:7])

#21.
it_companies.pop(0)
print(it_companies)

#22.

it_companies.pop(5)
print(it_companies)

#23.

it_companies.pop(-1)
print(it_companies)

#24.
it_companies.clear()
print(it_companies)

#25.
del it_companies

#26.

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined_list= front_end+back_end
print(joined_list)

#27.

full_stack = joined_list.copy()
full_stack.insert(5,"Python")
full_stack.insert(6,"SQL")

print("Fullstack:",full_stack)

#Exercises: Level 2.
 
