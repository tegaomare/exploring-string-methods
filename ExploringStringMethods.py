# Author: Tega Omarejedje
# Assignment: Exploring String Methods
# Date: 05/27/2025

# Task 1 - String Slicing and Indexing
wordplay = "Python is amazing!"

# The first 6 characters ("Python")
print("First word: " + wordplay[0:6])

# The word "amazing"
print("Amazing part: " + wordplay[10:17])

# The entire string in reverse order
print("Reversed string: " + wordplay[::-1])

# Task 2 - String Methods
wordplay = " hello, python world! "

# strip() to remove extra spaces
print("Stripped:", wordplay.strip())

# capitalize() to capitalize the first letter
print("Capitalized:", wordplay.strip().capitalize())

# replace() to replace "world" with "universe"
print("Replaced:", wordplay.replace("world", "universe"))

# upper() to convert the string to uppercase
print("Uppercase:", wordplay.upper())

# Task 3 - Check for Palindromes
wordplay = input("Enter a word: ").lower()

# Check if it's a palindrome
if wordplay == wordplay[::-1]:
    print(f"Yes, '{wordplay}' is a palindrome! ")
else:
    print(f"No, '{wordplay}' is not a palindrome! ")
