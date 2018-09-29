# game to guess a random number 
import random

def make_bett():
    msg = '---There is an integer between 0 and 100, make a guess on it---\n: '
    warning = 'Invalid input, only integer between 0 and 100 accepted!'
    
    while True:
        try:
            bett = int(raw_input(msg))
            if bett >= 0 and bett <= 100:
                return bett
            else:
                print(warning)
                continue
        except ValueError:
            print(warning)
            continue


    
def make_ran():
    ran = random.randint(0,100)
    return ran

def validate(ran):
    count = 0
    while count < 10:
        count += 1
        bett = make_bett()
      
        if bett == ran:
            print('Congraduation! You win! The answer is: ' + str(ran))
            break
        
        elif bett > ran:
            print('\nOops! Your guess %s is too large.' % str(bett))
            print('\nOnly %s times left' % str(10-count))
            continue
        
        else:
            print('\nOops! Your guess %s is too small.' % str(bett))
            print('\nOnly %s times left' % str(10-count))
            continue
    if count == 10:
            print("Sorry, you lose! The answer is : " + str(ran))

def start(max_round=10):
    print('-----Welcome to the Guess Number Game!-----\n')
    print('-----You have 10 times to guess, no time limit-----\n')
    ran = make_ran() 
    validate(ran)


# start
start()
        
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    