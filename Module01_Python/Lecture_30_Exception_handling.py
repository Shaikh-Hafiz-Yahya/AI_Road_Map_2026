x = 10
y = 2

quotient = x/y
print(quotient)
print('This is next code line')

# suppose input from user most probably error mily ga 
num1 = int(input('Enter num1:'))
num2 = int(input('Enter num2:'))

quotient = num1/num2  #NUMBER/0 = ERROR (ZeroDivisionError)
print(quotient)
print('This is next code line') #Ab ye next line of code nahi chala means system crash 

# Now Above Problem solution below.

num1 = int(input('Enter num1:'))
num2 = int(input('Enter num2:'))

try:

    quotient = num1/num2
    print(quotient)

except Exception:
    print('There is something wronge..')  #NUMBER/0 = ERROR (ZeroDivisionError)

print('This is next code line')  #ab ye next line of code run hoga    

# -------------------------------------------------------------------
num1 = int(input('Enter num1:'))
num2 = int(input('Enter num2:'))

try:
    print('Open DataBase')
    quotient = num1/num2
    print(quotient)
    print('Close DataBase') #ye print nahi hoga means DataBase connection close nahi hoga

except Exception as e:
    print('There is somethong wronge' , e)

print('This is next code line')        

# Above Problem Solution Below

num1 = int(input('Enter number1:'))
num2 = int(input('Enter number2:'))

try:
    
    print('Open DataBase')
    quotient = num1/num2
    print(quotient)

except Exception as e:
    print('There is something wronge',e)
    print('Close DataBase')  #ab ye print hoga means dabase connection close hogya

print('This is next code line')    

# but above problem ka solution tou milgya but agr zerodivsionerrorhi na mila
#  phir problem means k DataBase again close nahi hoga 

num1 = int(input('Enter number1:'))
num2 = int(input('Enter number2:'))

try:

    print('Open DataBase Connection')
    quotient = num1/num2
    print(quotient)
    
except Exception as e:
    print('There is somethong wronge',e)

finally:
    print('Close DataBase Connection')

print('This is next code line')         

# ---------------------------------------------------------------
num1 = int(input('Enter number1:'))
num2 = int(input('Enter number2:'))

try:

    print('Open DataBase Connection')
    quotient = num1/num2
    p = int(input('Enter a number:'))
    print(quotient)
    print(p)

except Exception as e:
    print('There is something wronge',e)

finally:
    print('Close DataBase Connection')

print('This is next code line')            


num1 = int(input('Enter number1:'))
num2 = int(input('Enter number2:'))

try:

    print('Open DataBase Connection')
    quotient = num1/num2
    p = int(input('Enter a number:'))
    print(quotient)
    print(p)

except ZeroDivisionError as e:
    print('You cannot divide a number by zero',e)

except ValueError as e:
    print('There is something wronge',e)    

finally:
    print('Close DataBase Connection')

print('This is next code line')  


num1 = int(input('Enter number1:'))
num2 = int(input('Enter number2:'))

try:

    print('Open DataBase Connection')
    quotient = num1/num2
    p = int(input('Enter a number:'))
    print(quotient)
    print(p)

except ZeroDivisionError as e:
    print('You cannot divide a number by zero',e)

except ValueError as e:
    print('There is something wronge',e)   

except Exception as e:
    print('Any Types Of Errors')     

finally:
    print('Close DataBase Connection')

print('This is next code line')  


int1 = int(input('Enter num1:'))
int2 = int(input('Enter num2:'))

try:
    
    print('Open DataBase Connection:')
    result = int1/int2
    password = int(input('Enter numeric base password..'))
    your_password = password
    print(result)
    print(your_password)
 
except ZeroDivisionError as e:    
    print('You cannot divide a number by zero',e)

except ValueError as e:    
    print('There is something wronge',e)

except Exception as e:    
    print('Any Types Of Error',e)    

finally:
    print('Close DataBase Connection:')

print('This is next line of code.')

# ---------------PRACTICE TIME-------------
x = 10
y = 20

result = x/y
print(result)
print('This is next code of line..')

# input FROM USERS
int1 = int(input('Enter number1:'))
int2 = int(input('Enter number2:'))

result = int1/int2
print(result)
print('This is next code of line..')


int1 = int(input('Enter number1:'))
int2 = int(input('Enter number2:'))

try: 
    print('Open DataBase Connection')
    result = int1/int2
    p = int(input('Enter your password(Password must integers):'))
    print(result)
    print(p)
    
except ZeroDivisionError as e:
    print('You cannot divide a number by zero' , e)

except ValueError as e:
        print('This is something wronge' , e)

except Exception as e:
        print('Any types of error' , e)        

finally:    
    print('Close DataBase Connection')

print('This is next line of code..')





