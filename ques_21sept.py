# ============================================================
# 1. Write a program to print "Hello, World!".
# ============================================================

print("Hello, World!")


# ============================================================
# 2. Write a program that takes a name and prints a greeting.
# ============================================================

name = input("Enter your name: ")
print("Hello,", name)


# ============================================================
# 3. Write a program to add two numbers.
# ============================================================

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum = num1 + num2

print("Sum =", sum)


# ============================================================
# 4. Write a program to find the square of a number.
# ============================================================

num = float(input("Enter a number: "))

square = num * num

print("Square =", square)


# ============================================================
# 5. Write a program to check whether a number is even or odd.
# ============================================================

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# ============================================================
# 6. Write a program to find the maximum of two numbers.
# ============================================================

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print("Maximum =", num1)
else:
    print("Maximum =", num2)


# ============================================================
# 7. Write a program to convert Celsius to Fahrenheit.
# ============================================================

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit =", fahrenheit)


# ============================================================
# 8. Write a program to calculate the area of a circle.
# ============================================================

radius = float(input("Enter radius of the circle: "))

area = 3.14 * radius * radius

print("Area of circle =", area)


# ============================================================
# 9. Write a program to calculate the factorial of a number.
# ============================================================

num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial =", factorial)


# ============================================================
# 10. Write a program to check whether a number is
#     positive, negative, or zero.
# ============================================================

num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# ============================================================
# 11. Write a program to find the maximum of three numbers.
# ============================================================

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    maximum = num1
elif num2 >= num1 and num2 >= num3:
    maximum = num2
else:
    maximum = num3

print("Maximum =", maximum)


# ============================================================
# 12. Write a program to count vowels in a string.
# ============================================================

text = input("Enter a string: ")

count = 0

for char in text:
    if char.lower() in "aeiou":
        count += 1

print("Number of vowels =", count)


# ============================================================
# 13. Write a program to reverse a string.
# ============================================================

text = input("Enter a string: ")

reverse = text[::-1]

print("Reversed string =", reverse)


# ============================================================
# 14. Write a program to check whether a string is a palindrome.
# ============================================================

text = input("Enter a string: ")

reverse = text[::-1]

if text == reverse:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# ============================================================
# 15. Write a program to find the sum of all elements in a list.
# ============================================================

numbers = list(map(int, input("Enter numbers separated by spaces: "
).split()))

total = 0

for num in numbers:
    total += num

print("Sum of list elements =", total)


# ============================================================
# 16. Write a program to find the largest element in a list.
# ============================================================

numbers = list(map(int, input(
    "Enter numbers separated by spaces: "
).split()))

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest element =", largest)


# ============================================================
# 17. Write a program to remove duplicate elements from a list.
# ============================================================

numbers = list(map(int, input(
    "Enter numbers separated by spaces: "
).split()))

un = []

for num in numbers:
    if num not in un:
        un.append(num)

print("List after removing duplicates =", un)


# ============================================================
# 18. Write a program to count how many times an element
#     appears in a list.
# ============================================================

numbers = list(map(int, input(
    "Enter numbers separated by spaces: "
).split()))

element = int(input("Enter the element to count: "))

count = 0

for num in numbers:
    if num == element:
        count += 1

print("Element appears", count, "times.")


# ============================================================
# 19. Write a program to check whether a number is prime.
# ============================================================

num = int(input("Enter a number: "))

if num < 2:
    print("The number is not prime.")
else:
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("The number is prime.")
    else:
        print("The number is not prime.")


# ============================================================
# 20. Write a program to return all prime numbers between
#     two numbers.
# ============================================================

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Prime numbers:")

for num in range(start, end + 1):

    if num < 2:
        continue

    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")


# ============================================================
# 21. Write a program to calculate Fibonacci numbers.
# ============================================================

n = int(input("\nEnter the number of Fibonacci terms: "))

a = 0
b = 1

print("Fibonacci series:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# ============================================================
# 22. Write a program to find the second-largest number
#     in a list.
# ============================================================

numbers = list(map(int, input(
    "\nEnter numbers separated by spaces: "
).split()))

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

if len(unique_numbers) < 2:
    print("There is no second-largest number.")
else:
    largest = unique_numbers[0]
    second_largest = unique_numbers[0]

    for num in unique_numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    print("Second-largest number =", second_largest)


# ============================================================
# 23. Write a program to sort a list without using sort().
# ============================================================

numbers = list(map(int, input(
    "Enter numbers separated by spaces: "
).split()))

# Bubble Sort
for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):

        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list =", numbers)


# ============================================================
# 24. Write a program to merge two lists and remove duplicates.
# ============================================================

list1 = list(map(int, input(
    "Enter first list elements: "
).split()))

list2 = list(map(int, input(
    "Enter second list elements: "
).split()))

merged_list = list1 + list2

unique_list = []

for num in merged_list:
    if num not in unique_list:
        unique_list.append(num)

print("Merged list without duplicates =", unique_list)
