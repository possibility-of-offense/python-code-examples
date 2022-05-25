answer = input('What I am learning now? \n 1) Python \n 2) Java \n 3) C## \n')

try :
    answer_casting = int(answer)
except: 
    answer_casting = 'Not a number'

match answer_casting :
    case 1 :
        print('Correct')
    case 2 :
        print('Not correct')
    case 3 :
        print('Not correct')
    case _ :
        if type(answer_casting) == str :
            print(answer_casting)
        elif type(answer_casting) == int:
            print('Larger number')