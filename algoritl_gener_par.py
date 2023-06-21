import random
import requests
import jupyter

import string
copy=''
email='semenenko0688289809@gmail.com'
chet1=0
done_work=False
password=input()
zn=8
false_password=['']
f=open('logins.txt', 'r+')
l=f.read().split('\n')


def binary_search(list, item):
    low=0
    high=len(list)-1

    while low < high:
        mid=(low+high)
        guess = list[mid]   
        if guess == item:
            return mid
        if guess > item:
            high=mid - 1
        else:
            low = mid+1
    return None

def proverka(copy):
    #2

    if binary_search(false_password, copy) == None:
        pass
    else:
        copy=randomStringDigits()
        
def randomStringDigits():
    """Generate a random string of letters and digits """
    copy=''
    # lettersAndDigits = string.ascii_lowercase
    lettersAndDigits = string.ascii_lowercase + string.digits
    # lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(zn))
#1
while done_work != True:
    if chet1==218340105584896 or chet1==218340105584897 :
        print("finished(218340105584896)")
        done_work=True
    copy=randomStringDigits()
    proverka(copy)
    print(copy, end=', ')
    #3
    if(password == copy):
        done_work=True
        print('\n====================================================\n',
            '...........\n...........\n........... Poputok => {0}\n........... PAROL => {1}\n...........\n...........\n...........'.format(chet1+1, copy))
            
    else:
        chet1 += 1
        false_password.append(copy)

