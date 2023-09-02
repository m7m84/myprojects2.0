import random
secret_number = random.randint(1, 100)
attempts = 10
no_more_attempts = False
print('hello there')
print('im thinking about a number between 1 to 100')
while True :
    if attempts > 0 :
        guess = int(input('what is the number'))
        attempts -= 1
        if guess < secret_number :
            print('try a bigger number')
        elif guess > secret_number :
            print('try a smaller number')
        else:
            print('good job')
            break
    else:
        print('You lost. The secret number was', secret_number)
        break


