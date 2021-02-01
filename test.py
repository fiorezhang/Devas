#coding: utf-8

from combat import *

valueA = random.randint(0, 3)
valueB = random.randint(0, 3)
paramA = random.randint(0, 2)
paramB = random.randint(0, 2)
correctRand = correctRandom()

'''
print(valueA)
print(valueB)
print(paramA)
print(paramB)
print(correctRand)
print(judge(valueA, valueB, correctBody(paramA, paramB), correctRand))


playerA = [random.randint(0,99) for i in range(8)]
print(playerA)
print(setDiceBody(playerA))
print(setDiceSoul(playerA))
'''

playerA = [random.randint(0,99) for i in range(8)]
playerB = [random.randint(0,99) for i in range(8)]
combatBody(playerA, playerB)