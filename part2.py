# Ocean Part 2
# 11. Write a program to take as input n
# and print all prime numbers upto and including n (1 point).
def Q11():
    def is_prime(n):
        if n==2:
            return True
        for i in range(2,n):
            if n%i ==0:
                return False
        return True
    num = int(input("Input a NUMBER: "))
    for i in range(2,num+1):
        if is_prime(i):
            print(i,"\n")

# 12. Input two different strings and concatenate it (1 point).
def Q12():
    string1 = input("1st String: ")
    string2 = input("1nd String: ")
    print(string1+string2)

# 13. Take two strings of the same length and intersperse the second one into the first one:
# Input: india super
# Output: isnudpiear  (1 point).
def Q13():
    str1 = input("string1:")
    str2 = input("string2:")
    string = ''
    while (str1 != '') and (str2 !=''):
        string += str1[0]+str2[0]
        str1 = str1[1:]
        str2 = str2[1:]
        if (str1 != '' and str2=='') or (str2 != '' and str1==''):
            string += str1+str2
    print(string)



# 14. Given a string, write a program to reverse it (1 point).
def Q14():
    str = input("string:")
    print(str[::-1])

# 15. Given a string, check if it is a palindrome or not (1 point).
def Q15():
    str = input("string:")
    palindrome = True
    while len(str)>1:
        if str[0] != str[-1]:
            palindrome=False
            break
        str = str[1:-1]
    print("palindrome" if palindrome else "not palindrome" )


# 16. Write a program that counts and prints the number of vowels and the number of consonants in the string (1 point).


# 17. List of Squares: Write a program that prints the square of numbers from 1 to n, where n is provided by the user (1 point).

# 18. Fibonacci Sequence : Write a program that prints the first n numbers in Fibonacci numbers (1 point).

# 19. Print Star Pattern: Write a program that takes a number n from the user and prints a right-angled triangle pattern with stars of n rows (1 point) .

# 20. Write a piece of code which does exactly as specified in this video (10 points).

# 21. Factorial: Write a program that calculates the factorial of a number provided by the user (1 point).

# 22. Positive or Negative: Write a program that asks the user for a number and prints whether the number is positive, negative, or zero (1 point).

# 23. Simple Interest Calculation: Write a program that calculates the simple interest for given principal, rate, and time provided by the user (1 point).

# 24. Temperature Converter: Write a program that converts Celsius to Fahrenheit or Fahrenheit to Celsius, depending on user input (1 point).

# 25. Leap Year or Not: Write a program that checks if a given year is a leap year or not. Google for the details on how to figure out if the given number is a leap year or not. It is more complicated than simply checking for a multiple of 4 (1 point).

# 26. Divisible by 7 and 5: Write a program that checks if a number provided by the user is divisible by both 7 and 5. Generalize it to a and b (1 point).

# 27. Create a Python program that prompts the user for their age. If the age is less than 18, print “You are a minor.” If the age is between 18 and 65, print “You are an adult.” Otherwise, print “You are a senior citizen.” (1 point).

# 28. Grading System: Write a program that takes the marks of five subjects from the user and calculates the grade according to the average marks: A if average >= 90 B if average >= 80 and < 90 C if average >= 70 and < 80 D if average >= 60 and < 70 F otherwise (1 point).

# 29. Decimal to Binary Conversion: Write a program that converts a decimal number to its binary representation using loops, without using built-in conversion functions (1 point).

# 30. Write a program that finds the gcd of two numbers using Euclid’s Algrorithm. Given k
# as an input, display those two numbers, both with k digits, such that they take the maximum number of steps to find the GCD, across all the pair of numbers, both of which are of k

# digits (8 points).

# 31. Write a program to populate a list L
# with the first n

# natural numbers (1 point).

# 32. Write a program to populate a list L
# with random numbers in the range 1 to 1000 (1 point).
