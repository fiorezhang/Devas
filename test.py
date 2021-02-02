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
#playerA = [1,92,3,44,45,46,77,98]
#playerB = [71,2,73,94,35,36,37,38]

print("player A    ", end='')    
print(playerA)
print("player B    ", end='')    
print(playerB)
'''
for i in range(100):
    healthBodyA, healthBodyB, round = combatBody(playerA, playerB)
    print("healthBody A    ", end='')    
    print(healthBodyA)
    print("healthBody B    ", end='')    
    print(healthBodyB)       
    print("round    ", end='')
    print(round)
'''   
countWinnerA, countWinnerB = 0, 0
sumRound = 0
countLoop = 1000
for i in range(countLoop):
    healthBodyA, healthBodyB, healthSoulA, healthSoulB, round = combatBoth(playerA, playerB)

    if healthBodyA == 0 and healthBodyB == 0:
        winner = "D"
    elif healthBodyB == 0:
        winner = "A"
        countWinnerA += 1
    elif healthBodyA == 0:
        winner = "B"
        countWinnerB += 1
    elif healthSoulA == 0 and healthSoulB == 0:
        winner = "D"
    elif healthSoulB == 0:
        winner = "A"
        countWinnerA += 1
    elif healthSoulA == 0:
        winner = "B"
        countWinnerB += 1
        
        
    #print("round    ", end='')
    #print(round, end='')    
    sumRound += round
    #print("winner    ", end='')
    #print(winner)
    
print("countWinnerA    ", end='')
print(countWinnerA)
print("countWinnerB    ", end='')
print(countWinnerB)
avgRound = sumRound // countLoop
print("avgRound    ", end='')
print(avgRound)