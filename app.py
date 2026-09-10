import datetime

print("--- Welcome to your WSL Python App ---")

# Get user input
name = input(f"What is your name? ")
birth_year = input(f"What year were you born? ")

# Calculate age dynamically
current_year = datetime.datetime.now().year
age = current_year - int(birth_year)

# Print the result
print(f"Hello {name}! You are turning {age} years old this year.")

print(f"The current year is {current_year} and you were born on {birth_year} so that makes you {age} years old")