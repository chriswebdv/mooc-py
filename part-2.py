# Age of maturity

# Write your solution here

age = int(input("How old are you? "))

if age >= 18:
    print("You are of age!")
else:
    print("You are not of age!")

# Compare 2 ints using conditionals
num1 = int(input("Please type in the first number: "))
num2 = int(input("Please type in another number: "))

if num1 > num2:
    print(f"The greater number was: {num1}")
elif num2 > num1:
    print(f"The greater number was: {num2}")
else:
    print("The numbers are equal!")

# Alphabetically last
str1 = input("Please type in the 1st word: ")
str2 = input("Please type in the 2nd word: ")

if str1 > str2:
    print(f"{str1} comes alphabetically last.")
elif str2 > str1:
    print(f"{str2} comes alphabetically last.")
else:
    print("You gave the same word twice.")
