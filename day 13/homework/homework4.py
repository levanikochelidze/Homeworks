# Get the person's age from the user
age = int(input("Enter your age: "))

# Check if the age falls into different categories
if age < 13:
    print("You are a child")
elif 13 <= age <= 19:
    print("You are a teenager")
else:
    print("You are of legal age")
