'''
import math
def calculate_area(radius):
    area=round(math.pi,3)*radius**2
    return area
print(calculate_area(5))

my_list = ['apple', 'banana', 'cherry']

# Using enumerate in a for loop
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

# Using enumerate with a custom start index
for index, value in enumerate(my_list, start=1):
    print(f"Index: {index}, Value: {value}")

# Converting the enumerate object to a list of tuples
enumerated_list = list(enumerate(my_list))
print(enumerated_list)

def find_largest(numbers):
    Max=0
    for i in range(len(numbers)-1):
        for j in range(1,len(numbers)):
            if numbers[i]>numbers[j]:
                Max=numbers[i]
            else:
                Max=numbers[j]
    return Max
print(find_largest([2,4,7,1]))

s = "popopoppoppop"
sub="pop"
count=0
#a=s.split("op")
#print(a)
for i in range(len(s)):
    if s[i:len(s):3]==sub:
        count+=1
print(count)

def is_prime(n):
    for i in range(2,n-1):
        if n%i==0:
            return "False"
            break
        else:
            return "True"
print(is_prime(10))


my_list = [1,2,3,4,5]

print([x*2 for x in my_list if x%2==0])


l=[[1,2,3], [4,5,6], [7,8,9]]
out=[]
#for i in l:
 #   for j in i:
  #      out.append(j)
#print(out)

print([j for i in l for j in i ])

def sum_last_ele(l):
    Sum=0
    for i in l:
            Sum+=i[-1]
    return Sum
print(sum_last_ele([[8, 14, -6], [12,7,4], [-11,3,21]]))

flat_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

nested_list = []
chunk_size = 3

for i in range(0, len(flat_list), chunk_size):
    nested_list.append(flat_list[i:i + chunk_size])

print(nested_list)
'''
# Joining a list of strings with a space as a separator
words = ["Hello", "world", "from", "Python"]
sentence = " ".join(words)
print(sentence)

# Joining a tuple of strings with a comma and space
items = ("apple", "banana", "orange")
fruit_list = ", ".join(items)
print(fruit_list)

# Joining a list with an empty string (concatenates without a separator)
characters = ["P", "y", "t", "h", "o", "n"]
joined_chars = "".join(characters)
print(joined_chars)