# Sum of two numbers
def add(a, b):
    return a + b


print("Sum:", add(5, 7))


# Largest number in a list
def find_max(numbers):
    return max(numbers)


print("Max:", find_max([3, 8, 2, 10, 6]))


# Count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


print("Vowel count:", count_vowels("Hello World"))
