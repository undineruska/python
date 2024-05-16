#Define a list of numbers [10, 20, 30, 40, 50]
numbers=[10, 20, 30, 40, 50]

#Print the length of the list.
print(len(numbers))

#Print the first element of the list.
print(numbers[0])

#Print the last element of the list.
print(numbers[4])

#Append a new number (e.g., 60) to the list.
numbers.append(60)

#Print the updated list.
print(numbers)

#Remove the second element from the list.
numbers.pop(1)

#Print the list after removal.
print(numbers)

#Check if a specific number (e.g., 30) exists in the list and print the result.
if 30 in numbers:
    print("30 exists in the list.")
else:
    print("30 does not exist in the list.")
