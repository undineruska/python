print('Body Mass Index calculator!')

# Prompt the user for weight and height
weight_str = input("Please write weight in kilograms: ")
height_str = input("Please write height in meters: ")

# Convert input strings to floats
weight = float(weight_str)
height = float(height_str)

# Calculate BMI
bmi = weight / (height ** 2)
print("Your BMI is:", bmi)
