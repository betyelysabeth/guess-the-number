from random import randint

value = randint(0,101) #this function will give a number randomly and save it to variable value
print('Welcome to my game. Try guessing my number')

#we need the loop, so when our number wasn't match, it still give us the chance until matching with what stored in value
while value:
    n = int(input())
    if n>value:
        print('your number is bigger')
    elif n<value:
        print('your number is smaller')
    else:
        print('you got it')
        break
