# Initialize an empty set to store the numeric inputs
numeric_set = set()

# Keep accepting inputs until the user decides to stop
while True:
    user_input = input("Enter a numeric value (or type 'done' to finish): ")

    if user_input.lower() == 'done':
        break

    try:
        numeric_value = float(user_input)
        numeric_set.add(numeric_value)
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

print("Numeric inputs added to the set:", numeric_set)
