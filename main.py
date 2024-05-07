"""List comprehension"""

#new_list = [new_item for item in list]

# Go from this:
numbers = [1,2,3]
new_list = []

for n in numbers:
    add_1 = n+1
    new_list.append(add_1)

#to this:
new_list = [n + 1 for n in numbers]

name = "Angela"
new_list = [letter for letter in name]
# print(new_list)

doubled = [num*2 for num in range(1,5)]
# print(doubled)

names = ['Alex', 'Beth', 'Caroline']

short_names = [item for item in names if len(item) < 5]

# print(short_names)

numbers = [1, 1 ,2 ,3, 5, 8, 13, 21, 34, 55]

squared = [num**2 for num in numbers]
# print(squared)

list_of_strings = input().split(',')

list_int = [int(num) for num in list_of_strings]
print(list_int)

result = [num for num in list_int if (num%2) == 0]

print(result)

"""Dictionary Comprehension"""

# new_dict = {new_key:new_value for item in list}

# new_dict = {new_key:new_value for (key,value) in dict.items() if test}