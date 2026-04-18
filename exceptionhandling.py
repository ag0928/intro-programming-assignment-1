try:
    x=10/0
except ZeroDivisionError: print("You cannot divide by zero!")
else: print ("Divison successful")
finally: print ("This is always excuted")