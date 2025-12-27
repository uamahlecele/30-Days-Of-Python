#Exercises: Day 8

#1. and #2.
dog_dict = {"name":"Zoe","colour":"brown", "breed":"Africunus","legs":4}

#3. 

student_dict= {"first_name":"Amahle","last_name":"Cele","gender":"male","age":24,"marital_status":"single","skills":["Dope shit","Art","Writing","Music"],"country":"mzansi","city":"pinetown","address":"236 mfeme road"}

#4.

print("length of student dictionary:",len(student_dict))

#5.

print(type(student_dict["skills"]))

#6.

print(student_dict["skills"])
add_more = ["Funny","Prolific","Visionary"]
student_dict["skills"] =  student_dict["skills"] + add_more

print(student_dict["skills"])

#7.

print(student_dict.keys())

#8.

print(student_dict.values())

#9.

print("List of items\n",student_dict.items())

#10.

del student_dict["address"]
print(student_dict)

#11.

del dog_dict

