## Imports exit function for scrubbing bad inputs
from sys import exit

## Defines X and Y using the numbers input by user as a string
## then attempts to turn the string into a number, if it cant it ends the program
## Will Loop later!
x = str(input("Gimme a number: "))
try:
    int(x)
except:
       print("Sorry, that was not a number")
       exit()

y = str(input ("Give me another number: "))
try:
    int(y)
except:
       print("Sorry, that was not a number")
       exit()

## Prevents dividing by Zero
if x == y == 0:
   print ("Sorry Sonny, we don't like your kind round 'ere")
   exit()

## Allows the user to choose between formula
choice = str(input("What do you want to do? say add, sub, div or mult: "))
choices = ["add", "sub", "mult", "div"]

if choice== choices[0]:
         print (x + y)

if choice== choices[1]:
         print (x - y)

if choice== choices[2]:
         print (x * y)

if choice== choices[3]:
         print (x / y)

## if no good input was recieved, exits the program.
elif choice not in choices:
   print ("You fucked up")
   exit()

