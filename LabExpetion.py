"""# LAB_EXCEPTIONS


## Below you have a code that raises an exception , using what you learned do the following:
- Find what type of exception is raised.
- Hanlde the exception in try..except 
- If operation successful , print "the operation is successful"
- if operation fails, handle the specific exception that is raised , and print a relevant message.
```
def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)


additoin(10, 20)
```


"""
def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

try:
    additoin(10, 20)
except NameError as e:
    print('the variable is not defined ')
except Exception as e :
    print("Opraion failed ")
    print(e.__class__,e)
else:
    print('Opration is done with no errors')