# Functions

"""
 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function. """

"""hrs = float(input("Enter hours? "))
rt = float(input("Enter rate per hour? "))
def computepay(h,r):
    if h>40:
      pay=h*r
      ot=(h-40)*(r*0.5)
      grasspay=pay+ot
      print("Pay : ",grasspay)
    else:
      pay=h*r
      print("Pay : ",pay)
    print("Done !!!")
    return 'pay'

p = computepay(hrs, rt)
print("Pay",p)
"""
hour=float(input("Enter the Number of Hours ?:"))
rate=float(input('Enter the rate per Hour?:'))

def Grass_pay(h,r):
  if hour>40:
    print("Grass_pay=",rate*40+(hour-40)*rate*1.5)
  else:
    print("Grass_pay=",hour*rate)
Grass_pay(hour,rate)