#!/usr/bin/env python
# coding: utf-8

# In[ ]:



print("Enter marks between 0 to 100")

maths = input("Enter marks for Maths: ")
chemistry = input("Enter marks for Chemistry: ")
physics = input("Enter marks for Physics: ")
english = input("Enter marks for English: ")
computer = input("Enter marks for Computer: ")

total_marks = int(maths) + int(chemistry) + int(physics) + int(english) + int(computer)

percentage = ( total_marks / 500 ) * 100

if percentage <= 100 and percentage >= 80:
    print("A+ ", percentage)
elif percentage < 80 and percentage >= 70:
    print("A ", percentage)
elif percentage < 70 and percentage >= 60:
    print("B ", percentage)
elif percentage < 60 and percentage >= 50:
    print("C ", percentage)
elif percentage < 50 and percentage >= 40:
    print("D ", percentage)
else:
    print("F ", percentage)

