# Functions Basics
# Ayesha Mumtaz - Python Learning

# Simple function
def greet():
    print("Hello! Welcome!")

greet()

# Function with parameter
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Ayesha")

# Function with return value
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print("Sum:", result)

# Function with default value
def introduce(name, city="Faisalabad"):
    print(f"I am {name} from {city}")

introduce("Ayesha")
introduce("Sara", "Lahore")

