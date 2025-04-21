# Print 1 to 10
for i in range(1, 11):
    print(i)

# Print even numbers from 2 to 10
for i in range(2, 11, 2):
    print(i)

# First 5 Fibonacci numbers
a, b = 0, 1
count = 0
while count < 5:
    print(a)
    a, b = b, a + b
    count += 1
