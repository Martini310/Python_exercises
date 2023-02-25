"""Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)"""

while True:
    s = input("Enter a word to check if it's palindrome: ")
    print("It's a palindrome!" if s.lower() == s.lower()[::-1] else "It's not a palindrome!")
    