#!/bin/python3


n = int(input("Enter a number: "))
if (n % 2) == 0:
     if ( 2 <= n <= 5 ): 
        print ("Not Weird")
     elif ( 6 <= n <= 20 ):
        print("Weird")
     else:
        print("Not Weird")
else:
    print("Weird")
