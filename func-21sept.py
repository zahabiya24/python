# 1. Write a function to print "Hello, World!"
def hello():
    print("Hello, World!")

hello()


# 2. Write a function that takes a name and prints a greeting.
def greet():
    name = input("Enter your name: ")
    print("Hello", name)

greet()


# 3. Write a function to add two numbers.
def add():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum =", a + b)

add()


# 4. Write a function to find the square of a number.
def square():
    n = int(input("Enter a number: "))
    print("Square =", n * n)

square()


# 5. Write a function to check whether a number is even or odd.
def even_odd():
    n = int(input("Enter a number: "))

    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_odd()


# 6. Write a function to find the maximum of two numbers.
def maximum():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if a > b:
        print("Maximum =", a)
    else:
        print("Maximum =", b)

maximum()


# 7. Write a function to convert Celsius to Fahrenheit.
def celsius_to_fahrenheit():
    c = float(input("Enter Celsius: "))
    f = (c * 9 / 5) + 32
    print("Fahrenheit =", f)

celsius_to_fahrenheit()


# 8. Write a function to calculate the area of a circle.
def circle_area():
    r = float(input("Enter radius: "))
    area = 3.14 * r * r
    print("Area =", area)

circle_area()


# 9. Write a function to calculate the factorial of a number.
def factorial():
    n = int(input("Enter a number: "))
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    print("Factorial =", fact)

factorial()


# 10. Write a function to check whether a number is positive, negative, or zero.
def check_number():
    n = int(input("Enter a number: "))

    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")

check_number()


# 11. Write a function to find the maximum of three numbers.
def maximum_three():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    if a >= b and a >= c:
        print("Maximum =", a)
    elif b >= a and b >= c:
        print("Maximum =", b)
    else:
        print("Maximum =", c)

maximum_three()


# 12. Write a function to count vowels in a string.
def count_vowels():
    text = input("Enter a string: ")
    count = 0

    for ch in text:
        if ch.lower() in "aeiou":
            count = count + 1

    print("Number of vowels =", count)

count_vowels()


# 13. Write a function to reverse a string.
def reverse_string():
    text = input("Enter a string: ")
    print("Reverse =", text[::-1])

reverse_string()


# 14. Write a function to check whether a string is a palindrome.
def palindrome():
    text = input("Enter a string: ")

    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

palindrome()


# 15. Write a function to find the sum of all elements in a list.
def list_sum():
    numbers = [1, 2, 3, 4, 5]
    total = 0

    for n in numbers:
        total = total + n

    print("Sum =", total)

list_sum()


# 16. Write a function to find the largest element in a list.
def largest():
    numbers = [10, 20, 5, 30, 15]
    big = numbers[0]

    for n in numbers:
        if n > big:
            big = n

    print("Largest =", big)

largest()


# 17. Write a function to remove duplicate elements from a list.
def remove_duplicates():
    numbers = [1, 2, 2, 3, 3, 4, 5]
    new_list = []

    for n in numbers:
        if n not in new_list:
            new_list.append(n)

    print("New list =", new_list)

remove_duplicates()


# 18. Write a function to count how many times an element appears in a list.
def count_element():
    numbers = [1, 2, 2, 3, 2, 4]
    element = int(input("Enter element to count: "))
    count = 0

    for n in numbers:
        if n == element:
            count = count + 1

    print("Count =", count)

count_element()


# 19. Write a function to check whether a number is prime.
def prime():
    n = int(input("Enter a number: "))
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1

    if count == 2:
        print("Prime")
    else:
        print("Not Prime")

prime()


# 20. Write a function to return all prime numbers between two numbers.
def primes_between():
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))

    for n in range(start, end + 1):
        count = 0

        for i in range(1, n + 1):
            if n % i == 0:
                count = count + 1

        if count == 2:
            print(n, end=" ")

    print()

primes_between()


# 21. Write a function to calculate Fibonacci numbers.
def fibonacci():
    n = int(input("Enter number of terms: "))

    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

    print()

fibonacci()


# 22. Write a function to find the second-largest number in a list.
def second_largest():
    numbers = [10, 20, 5, 30, 25]

    largest = numbers[0]
    second = numbers[0]

    for n in numbers:
        if n > largest:
            second = largest
            largest = n
        elif n > second and n != largest:
            second = n

    print("Second largest =", second)

second_largest()


# 23. Write a function to sort a list without using sort().
def my_sort():
    numbers = [5, 2, 8, 1, 3]

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    print("Sorted list =", numbers)

my_sort()


# 24. Write a function to merge two lists and remove duplicates.
def merge_lists():
    list1 = [1, 2, 3]
    list2 = [3, 4, 5]

    new_list = list1.copy()

    for n in list2:
        if n not in new_list:
            new_list.append(n)

    print("Merged list =", new_list)

merge_lists()
