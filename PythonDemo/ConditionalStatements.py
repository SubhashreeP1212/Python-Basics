#conditional stements
#if , if--else, elif

age=15
if age>=18:
    print("You are eligible to vote")#if print is written from the starting point then print will not be considered part of if
else:
    print("You are not eligible to vote")

#USING BOOLEAN VALUE
if True:
    print("You are True")
else:
    print("you are False")
#using 1 or 0
if 1:
    print("you are True")

if 0:
    print("you are True")
else:
    print("you are False")
#printing in single line
num=int(input("Enter a number: "))
print("Even number") if num%2==0 else print("Odd number")
#if multiple statements to be printed  in a single line use {} and multiple print statements
{print("Even number"),print(num)} if num%2==0 else {print("Odd number"),print(num)}

#mulitple conditions using elif,it act as else if in java
weekDay=1
if weekDay==1:
    print("Sunday")
elif weekDay==2:
    print("Monday")
elif weekDay==3:
    print("Tuesday")
else:
    print("invalid week number")





