score = input('Score: (should be between 0.0 and 1.0) \n')
msg = ''
grade = ''

try :
    score_int = float(score)
    if score_int < 0.0 or score_int > 1.0 :
        msg = score_int
    elif score_int <= 0.6 :
        grade = 'F' 
    elif score_int <= 0.7 :
        grade = 'D' 
    elif score_int <= 0.8 :
        grade = 'C' 
    elif score_int <= 0.9 :
        grade = 'B' 
    else :
        grade = 'Amazing'
except :
    print(msg)

if msg != '' :
    print(str(msg) + ' was out of range!')

if grade != '' :
    print('The grade was this: {grade}!'.format(grade = grade))