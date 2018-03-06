#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class Lotto:
    countDraw = 0
    userNumber = []
    randNumber = []

    def draw(self,x):
        for i in range(x):
            tempNumber = []

            oneNumber = input("Podaj pierwszą liczbę (przedział od 1 do 49): ")
            tempNumber.append(self.checkNumber(oneNumber, tempNumber, 'user'))

            twoNumber = input("Podaj drugą liczbę (przedział od 1 do 49): ")
            tempNumber.append(self.checkNumber(twoNumber,tempNumber, 'user'))

            threeNumber = input("Podaj trzecią liczbę (przedział od 1 do 49): ")
            tempNumber.append(self.checkNumber(threeNumber, tempNumber, 'user'))

            fourNumber = input("Podaj czwartą liczbę (przedział od 1 do 49): ")
            tempNumber.append(self.checkNumber(fourNumber, tempNumber, 'user'))

            fiveNumber = input("Podaj piątą liczbę (przedział od 1 do 49): ")
            tempNumber.append(self.checkNumber(fiveNumber, tempNumber, 'user'))

            sixNumber = input("Podaj szóstą liczbę (przedział od 1 do 49): ")
            tempNumber.append(self.checkNumber(sixNumber, tempNumber, 'user'))

            tempNumber.sort()

            self.userNumber.append(tempNumber)

    def randNumber(self):
        tempNumber = []

        oneNumber = random.randint(1, 49)
        tempNumber.append(self.checkNumber(oneNumber, tempNumber, 'auto'))

        twoNumber = random.randint(1, 49)
        tempNumber.append(self.checkNumber(twoNumber, tempNumber, 'auto'))

        threeNumber = random.randint(1, 49)
        tempNumber.append(self.checkNumber(threeNumber, tempNumber, 'auto'))

        fourNumber = random.randint(1, 49)
        tempNumber.append(self.checkNumber(fourNumber, tempNumber, 'auto'))

        fiveNumber = random.randint(1, 49)
        tempNumber.append(self.checkNumber(fiveNumber, tempNumber, 'auto'))

        sixNumber = random.randint(1, 49)
        tempNumber.append(self.checkNumber(sixNumber, tempNumber, 'auto'))

        tempNumber.sort()
        self.randNumber = tempNumber

    def checkNumber(self, number, list, created, returnData=None, brokeData=False):
        while True:

            try:
                int(number)
                brokeData = False
            except ValueError:
                brokeData = True

            if (brokeData == False) and (number not in list) and (int(number) > 0 and int(number) <50):
                returnData = int(number)
                break
            else:
                if created == 'user':
                    number = input("Podaj prawidłową wartość, liczbę wcześniej nie użytą, z przedziału od 1 do 49: ")
                else:
                    number = random.randint(1,49)

        return returnData

    def checkReward(self,randNumbers,userNumbers):
        count = 0
        while count < len(userNumbers):
            print('sprawdzam'+str(count))
            i=0

            if userNumbers[count]==randNumbers:
                return True

            count = count + 1

program = Lotto()

program.randNumber()

userCountDraw = ''

print(program.randNumber)

while True:
    try:
        int(userCountDraw)
        break
    except ValueError:
        userCountDraw = input("Podaj ilość kuponów jaką chcesz wysłać w lotto: ")

program.draw(int(userCountDraw))

print('Wydałeś łącznie '+str(int(userCountDraw)*3)+'zł')

if(program.checkReward(program.randNumber,program.userNumber)):
    print('Wygrałeś, liczby wylosowane przez system to: '+str(program.randNumber))
else:
    print('Nie wygrałeś, liczby wylosowane przez system to: '+str(program.randNumber))

input('Enter zakończy program...');