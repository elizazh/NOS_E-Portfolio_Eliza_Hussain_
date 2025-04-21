# Check if number is positive, negative, or zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# Check if string starts with vowel or consonant
text = input("Enter a word: ")
if text[0].lower() in "aeiou":
    print("Starts with a vowel")
else:
    print("Starts with a consonant")

# Check if two numbers are equal
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
if x == y:
    print("The numbers are equal")
else:
    print("The numbers are not equal")
