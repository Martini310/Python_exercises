'''The exercise comes first (with a few extras if you want the extra challenge or want to spend more time), followed by a discussion. Enjoy!

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:
    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (chec).
    If check divides evenly into num, tell that to the user. If not, print a different appropriate
    message.'''
    
def number(num, check):
    if num % 4 == 0:
        print(f"{num} is multiple of 4", end='')
    elif num % 2 == 0:
        print(f"{num} is an even number", end='')
    else:
        print(f"{num} is an odd number", end='')
    if num % check == 0:
        print(f" and is divisible by {check}.")
    else:
        print(f" and is not divisible by {check}.")

while True:
    num = int(input("Tell me some number: "))
    check = int(input("What number do You want to divide it: "))
    number(num, check)