#Peter Answers
#To use cheat write your answer in petition starting and ending with .(dot)
#Without .(dot) peter will give random answers

import random
from msvcrt import getch
print('Enter Petition:')
x = getch()
cheat = False
if x.decode()=='.':  #In case of dot you will see noting on the screen and your answer will be stored in list
    cheat = True
    ans=[]
    while True:
        x = getch()
        if x.decode() == '.':  #dot in the end will mark the end of the answer anddisplay default petition on the screen
            break
        else:
            ans.append(x.decode())
    print('Peter, please answer the following question')
else:
    print(x.decode(),end='') 
    input()             #In case of not using cheat you have to write the petition 

input('Enter Question:\n')
print('Answer:')
if cheat:
    for x in ans:
        print(x,end='')
else:
    random_answers = ['If you go on being rude to me, I will never answer','You are wasting my time.','We\'ll leave this question for later.','I can\'t quite tell at the moment.',
    'Why you don\'t let another person ask me? Maybe I\'ll answer.']
    print(random.choice(random_answers))