# List of string values
words = ["Anna", "Oskars", "Toms", "Janis", "Peteris"]

# Prompt the user to enter a string value
user_input = input("Enter a the name: ")

# Standardize the user input using string methods
user_input = user_input.lower().strip()  # Convert to lowercase and remove leading/trailing whitespace

# Check if the standardized user input is in the list
found = False
for word in words:
    if user_input == word:
        found = True
        break

# Print the result
if found:
    print(f"The word '{user_input}' is in the list.")
else:
    print(f"The word '{user_input}' is not in the list.")
