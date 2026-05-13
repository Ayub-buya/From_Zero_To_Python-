#Exeptions  =   An event that interupts the flow of program
#                (ZeroDivisionError, TypeError, ValueError)
#               try, 2.exept, 3.finally

#ZeroDivisionError
try:
    x= 1/0
except ZeroDivisionError:
    print ("You can't divide by Zero")

#ValueError
value = int (input("please enter a value: "))
try:
    y=10/value
except ValueError:
    print("That is not a valid number")
except ZeroDivisionError:
    print ("You can't divide by Zero ")
except Exception as e:
    print("Something wenr wrong {e}")
finally:
    print ("Do some clean up here!")