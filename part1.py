# 1. Write a program that prints “Namasthey India” to the screen (1 point).
print("Namasthey India")
print()
# 2. Take as input a number n
# and print the square, cube and 2n
# of the number (1 point).
n1 = input("n: ")
print(n1**2,"\n",n1**3,"\n",2*n1)
print()
# 3. Print the following using four print statements:
# *
# **
# ***
# ****
# (1 point) .
print("*")
print("**")
print("***")
print("****")
print()
# 4. Write an interactive python program which does the following:
# What's your name? John
# How old are you? 25
# What's your favorite color? Blue
# What's your favorite hobby? Reading
# (1 point).
name = input("What's your name? ")
age = input("How old are you? ")
color = input("What's your favorite color? ")
hobby = input("What's your favorite hobby? ")
print()
# 5. Understand how to use a if conditional in python. 
# Ask the user to enter a number and check if the number is even or odd (1 point).
num = input("number: ")
if num%2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
print()
# 6. Write a program to take as input a number n
# and display the first n
# natural numbers (1 point).
n2 = input("number: ")
for i in range(1,n2+1):
    print(i)
print()
# 7. Print a sequence of numbers starting from the number a with common difference d.
# Go on till you reach the number b.
# Enter a value for a: 10
# Enter a value for d: 3
# Enter a value for b: 20
# Output: 10 13 16 19
# (1 point).
a = input("Enter a value for a: ")
d = input("Enter a value for d(diff): ")
b = input("Enter a value for b: ")
if a<b:
    while a<=b:
        print(a)
        a+=d
else:
    while b<=a:
        print(a)
        a-=d
print()
# 8. Write a program that calculates and prints the sum of all numbers from 1 to n, where n is provided by the user (1 point).
n3=input("number: ")
v=0
for i in range(1,n3+1):
    v=v+i
print(v)
print()
# 9. Write a program that takes a number n from the user and prints the multiplication table for that number from 1 to 10.
# Generalize it from i to j.
# 2X1=2
# 2X2=4 and so on... (1 point).
n4= input("number to create table for: ")
for i in (1,11):
    print(f"{n4}x{i}={n4*i}\n")
print()
# 10. Write a program to find out if the given number is prime or not (1 point).
n5 = input("number: ")
PRIME=True
for i in range(2,n5):
    if n5%i ==0:
        PRIME = False
        break
if PRIME:
    print("Prime")
else:
    print("not Prime")