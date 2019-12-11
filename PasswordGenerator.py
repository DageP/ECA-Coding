Numbers = [0,1,2,3,4,5,6,7,8,9]
Letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Symbols = ["!","@","#","%","$","^","&","*","(",")","_","-"]

import random
limit = 10
password = []
while len(password) < limit:
    password.append(Numbers[random.randrange(10)])
    if len(password) != limit:
        password.append(Letters[random.randrange(26)])
        if len(password) < limit:
            password.append(Symbols[random.randrange(12)])
Up = Letters[random.randrange(26)]
password[0] = Up.upper()
Upp = Letters[random.randrange(26)]
password[9] = Upp.upper()
a = "".join(map(str, password)) #The "" part is to add symbols in between the elements
print("Voila! Your password is : ", a)

