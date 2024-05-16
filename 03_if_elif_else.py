import random

# Generate a list of 10 random numbers
numbers = [random.randint(1, 10) for _ in range(10)]

# Iterate through the list and analyze each number
for number in numbers:
    if number > 5:
        print(f"{number} is higher than 5")
    elif number < 5:
        print(f"{number} is lower than 5")
    else:
        print(f"{number} is equal to 5")
