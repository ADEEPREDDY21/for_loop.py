#for loop in Python is used to iterate over a sequence (e.g., a list, tuple, dictionary, set, or string) or other iterable objects.
# It allows you to execute a block of code multiple times, once for each item in the sequence.
print("FOR LOOP SEQUENCE")
print("Example for for_loop")
l1=[12,34,56,76,45]#Here l1 is a list
for each_in_list1 in l1:#we are initiating a new variable each_in_list1 to print each element in the list
    print(each_in_list1)
    
print("Example for for_loop")
l1=[12,34,56,76,45]
for each_in_list1 in l1:
    print(each_in_list1*3)#by using for loop we can print each element in the list and also we can perform any operation on each
    
    
print("Example for for_loop")
l1=[12,34,56,76,45]
for each_in_list1 in l1:
    print(each_in_list1)
    if each_in_list1==76:#Here we are checking each element in the list with 76
        break #When the execution reach 76 it will break the loop and will not print the rest of the elements in the list
    
print("Example for for_loop with break")
l1=[12,34,56,76,45]
for each_in_list1 in l1:
    print(each_in_list1)
    if each_in_list1==76:
        break     
else:
    print("No longer 76 is found in the list")#When the loop is not breaked it will print this message
    
print("Example for for_loop with skip")
l1=[12,34,56,76,45]
for each_in_list1 in l1:
    print(each_in_list1)
    if each_in_list1==76:
        continue#In this case when the execution reach 76 it will skip 76 and will print the rest of the elements in the l1
else:
    print("No longer 76 is found in the list")#When the loop is not breaked it will print this message
    
print("example 1 Iterating Over a List of Names using for loop")    
names = ["Adeep", "Likitha", "Geetha", "Suresh"]
for name in names:
    print(f"Hello Mr/MRs {name}")#Here we are printing each name in the list with a greeting message



print("Example 2 Calculating the Sum of Numbers in a List using for loop")
#List of numbers
num=[1,4,5,65,34,34]
#Variable store in the sum of the numbers in the list
total_sum=0
for numbers in num:
   total_sum += numbers
print(f"total sum is {total_sum}")#Here we are printing the sum of the numbers in the list

print("Example 3 Finding Even Numbers and Odd Numbers in a Range using for loop")
for i in range(1, 101):
    if i % 2 == 0:
        print(f"{i} is an even number") #Here we are printing all the even numbers in the range from 1 to 100
    else:
        print(f"{i} is an odd number") # Here we are printing all the odd numbers in the range from 1 to 100
        
print("Example 4  Printing Each Character in a String usng for loop")        
char="Hello World..!"
for each_Character in char:
    print(each_Character) #Here we are printing each character in the string "Hello World..!"
    
print("Example 5  Iterating Over a Dictionary using for loop")    
#Dictionary of Names and their ages
dict={"Adeep":21,"Likitha":21,"Suresh":22,"Geetha":34}
for name,age in dict.items():
    print(f"{name}:{age}")