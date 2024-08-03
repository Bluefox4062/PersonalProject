pointcard = True
point = 4
age = 40

if (age >= 60) or (pointcard == True and point==5):
    print('ticket=200')
elif (59 > age > 18):
    print('ticket=400')
else:
    print("don't sold")