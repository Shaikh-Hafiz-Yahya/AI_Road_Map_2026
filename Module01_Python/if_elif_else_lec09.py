# # if condition 
#       # Do Some Action 
# # elif Other condition
#       # Do some other action
# # elif
#      # Do some other action

passingmarks = 70
score = int(input('Enter your score:'))

if score >= passingmarks:
    print('Congratulations---You are passed.')
else:
    print('You need to take exam again.')    

passingmarks = 33
score = int(input('Enter your score:'))    

if score == 50:
    print('Congratulations--BETTER RESULT--You are passed')
elif (score < 50) and (score > passingmarks):
    print('Passed But you really need to focus study.')
elif (score > 50) and (score < 100):  
    print('best performance')  
else:
    print('You need to take exam again.')    

# Exam grade system
passingmarks = 40.1
score = float(input('Enter score:'))

if score == passingmarks:
    print('Your --Result-- Passed but more than need to focus study.')
elif score >= 50 and score <= 59.99: 
    print('Grade is C')
elif score >= 60 and score <= 69.99: 
    print('Grade is B')    
elif score >= 70 and score <= 79.99: 
    print('Grade is A-')    
elif score >= 80 and score <= 89.99: 
    print('Grade is A')
elif score >= 90 and score <= 99.99: 
    print('Mind Beloing Performance')
    print('Grade is A+')   
else:
    print('You need to take exam again.')     

# conceptual 
employee = True  
if employee: # ye condition true hona lazmi ha 
    print('Have Fun..')    

employee = False
if employee:  
    print('No Display..')    

employee1 = False
employee2 = True
if employee1:  
    print('No Display..') 
elif employee2:
    print('Display')       

adult = 'Yes'
if adult == 'Yes':
    print('you are adult.')

adult = 'No'
if adult == 'Yes':
    print('You are adult.')    

score = 80
match score:
    case 70:
        print('You are passed')
    case 75:
        print('A')
    case 80:
        print('A-')
    case 90:    
        print('A+')
    case 60:
        print('Fail')    
    