#Exercises: Day 11
from statistics import *



#Exercises: Level 1

#1.

def add_two_numbers(num_1,num_2):
    sum =  num_1 + num_2
    return sum

print(add_two_numbers(7,7))

#2.

def area_of_circle(r1,r2):
    pi = 3.14
    area = pi*r1*r2
    return round(area,2)

print("Area of circle is:",area_of_circle(5,6))

#3. 

def add_all_nums(*num):
    #check if the arguments provided are all digits or not
    return sum(num)

print(add_all_nums(1,1,1,1))

#4.

def convert_celsius_to_fahrenheit(c):
    converted_c = (c*9/5)+32
    return round(converted_c,2)


print(f"Celsius to Fahrenheit:{convert_celsius_to_fahrenheit(33)} F")

#5.

def check_season(month):
    autumn = [1,2,3]
    winter = [4,5,6]
    spring = [7,8,9]
    summer = [10,11,12]

    if month in range(1,13):
        for i in autumn:
            if i == month:
                return "The season is Autumn"
            
        for i in winter:
            if i == month:
                return "The season is Winter"
            
        
            for i in spring:
                if i == month:
                    return "The season is Spring"
                    
        
            for i in summer:
                if i == month:
                    return "The season is Summer"
        else:
            print("That's not a valid month number.")
print(check_season(3))
        
#6.

#not farmiliar with how to do it

#7.

def solve_quadratic_eqn(a,b,c):
    ...
    
#8.

def print_list(list):
    for value in list:
        print(f"\n{value}")
    
print_list(["Amahle","Cele","2001","24"])

#9.

def reverse_list(list):
    rev_list = []
    for i in range(len(list)-1,-1,-1):
        rev_list.append(list[i])

    return rev_list

print(reverse_list([1,2,3,4,5]))

#10.

def capitalize_list_items(list):
    capitalized = []
    for i in list:
        capitalized.append(i.upper())
    return capitalized


print(capitalize_list_items(["amahle","visionary","cool nigga"]))

#11.

def add_item(the_list,item_to_add):
    the_list.append(item_to_add)
    return the_list

print(add_item(["Amahle","Cele",24],"Software Engineer, Writer-Director, Artist"))

#12.

def remove_item(the_list,item_to_remove):
    the_list.remove(item_to_remove)
    return the_list

print(remove_item(['Amahle', 'Cele', 24, 'Software Engineer, Writer-Director, Artist','Freelancer'],'Freelancer'))

#13.

def sum_of_numbers(n):
    sum = 0
    for i in range(n+1):
        sum= sum+i
    return sum

print(sum_of_numbers(100))

#14.
#I've done these ones before and I know how to do them though fr.

def sum_of_odds(n):
    sum = 0
    for i in range(n+1):
        if i%2 !=0:
            sum= sum+i
        else:
            continue
    return sum

 #15.

def sum_of_even(n):
    sum = 0
    for i in range(n+1):
        if i%2 ==0:
            sum= sum+i
        else:
            continue
    return sum

print(f"Sum of odds: {sum_of_odds(100)}\n")
print(f"Sum of even: {sum_of_even(100)}\n")


#Exercises: Level 2

#1. 

def evens_and_odds(num):
    sum_odd = 0
    sum_even = 0
    for i in range(num+1):
        if i%2 !=0:
            sum_odd= sum_odd +1
        else:
            sum_even = sum_even +1

    return f"The number of odds are {sum_odd}.\nThe number of evens are {sum_even}."
 


print(evens_and_odds(100))

#2.

def factorial(n):
    factorial = 1
    for number in range(1,n+1):
        factorial = factorial * number
    return factorial

print(factorial(26))

#3. 
def is_empty(para = None):
    if para is not None:
        return "Not empty."
    else:
        return "Empty."

print(is_empty())

#4.

#mean

def calculate_mean(list):
    mean = 0
    mean = sum(list)//len(list)
    return mean
print("mean:",calculate_mean([5,6,43,673234,56531,134,9877,6,25,19,77,100]))

#median

def calculate_median(list):
    median_is = 0.0 
    list = sorted(list)
    print("sorted",list)
    if len(list)%2 == 0:
        median_is = (list[int((len(list)/2)-1)]+list[int((len(list)/2))])/2
        print(list[int((len(list)/2)-1)])
        print(list[int((len(list)/2))])
        return median_is
    else:
        median_is = list[len(list)//2]
        return median_is

print("median:",calculate_median([10,2,8,4]))

def calculate_mode(list):
    most_freq = {}
    list = sorted(list)
    print("sorted list",list)
    for i in (list):
        count = list.count(i)
        most_freq[i] = count
    print(most_freq)
    max_value = max(most_freq.values())
    return max_value
    

print("The most frequent number in the mode is:",calculate_mode([20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]))

def calculate_range(list):
    range = 0.0
    list = sorted(list)
    range =list[-1] - list[0] 
    return range

print("Range:", calculate_range([10,2,8,4,55,2,2,34]))
# def calculate_variance(list):
#     ...
def calculate_std(list):
    return round(stdev(list),1)

print(calculate_std([20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]))