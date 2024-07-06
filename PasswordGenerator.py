import random
passLength = int(input('What is your desired password length? (numbers only): '))
letters = 0
password = ""
while letters < passLength:
    randomLowerLetter = chr(random.randint(ord('a'), ord('z')))
    randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
    randomNumber = str(random.randint(0,9))
    randomSymbol = random.randint(0,9)
    characterType = random.randint(1,4)
    if characterType == 1:
        password = password + randomLowerLetter
    elif characterType == 2:
        password = password + randomUpperLetter
    elif characterType == 3:
        password = password + randomNumber
    elif characterType == 4:
        if randomSymbol == 1:
            password = password + '!'
        elif randomSymbol == 2 or randomSymbol == 9 or randomSymbol == 0:
            password = password + '@'
        elif randomSymbol == 3:
            password = password + '#'
        elif randomSymbol == 4:
            password = password + '$'
        elif randomSymbol == 5:
            password = password + '%'
        elif randomSymbol == 6:
            password = password + '^'
        elif randomSymbol == 7:
            password = password + '&'
        elif randomSymbol == 8:
            password = password + '*'
    letters = letters + 1
print()
print(password)
print()
print('Your password is secure and unique. ' 
    + 'Not even the creator of this program knows it.')
