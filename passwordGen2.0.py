import random

Chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
         '0','1','2','3','4','5','6','7','8','9']

print("How many characters should the new password have?")
i = int(input())

def getNewPassword(lst, i):
    x = random.sample(lst,i)
    password = ''.join(x)
    return password

myNewPassword = getNewPassword(Chars, i)
print("Your generated Password is: | {} |".format(myNewPassword))
