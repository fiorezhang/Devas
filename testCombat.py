#coding: utf-8

#测试战斗平衡性

from combat import *

sumAvgRound = 0
sumCountWinnerBodyA, sumCountWinnerBodyB = 0, 0
sumCountWinnerSoulA, sumCountWinnerSoulB = 0, 0
countSample = 100
for j in range(countSample):
    playerA = [random.randint(0,69) for i in range(8)]
    playerB = [random.randint(0,69) for i in range(8)]
    #playerA = [1,92,3,44,45,46,77,98]
    #playerB = [71,2,73,94,35,36,37,38]

    #print("player A    ", end='')    
    #print(playerA)
    #print("player B    ", end='')    
    #print(playerB)
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
    countWinnerBodyA, countWinnerBodyB = 0, 0
    countWinnerSoulA, countWinnerSoulB = 0, 0
    sumRound = 0
    countLoop = 400
    for i in range(countLoop):
        healthBodyA, healthBodyB, healthSoulA, healthSoulB, round = combatBoth(playerA, playerB)

        if healthBodyA == 0 and healthBodyB == 0:
            winner = "D"
        elif healthBodyB == 0:
            winner = "A"
            countWinnerBodyA += 1
        elif healthBodyA == 0:
            winner = "B"
            countWinnerBodyB += 1
        elif healthSoulA == 0 and healthSoulB == 0:
            winner = "D"
        elif healthSoulB == 0:
            winner = "A"
            countWinnerSoulA += 1
        elif healthSoulA == 0:
            winner = "B"
            countWinnerSoulB += 1  
            
        sumRound += round
        #print("round    ", end='')
        #print(round, end='')    
        #print("winner    ", end='')
        #print(winner)
        
    avgRound = sumRound // countLoop
    #print("countWinnerBodyA    ", end='')
    #print(countWinnerBodyA)
    #print("countWinnerBodyB    ", end='')
    #print(countWinnerBodyB)
    #print("countWinnerSoulA    ", end='')
    #print(countWinnerSoulA)
    #print("countWinnerSoulB    ", end='')
    #print(countWinnerSoulB)
    #print("avgRound    ", end='')
    #print(avgRound)
    
    sumCountWinnerBodyA += countWinnerBodyA
    sumCountWinnerBodyB += countWinnerBodyB
    sumCountWinnerSoulA += countWinnerSoulA
    sumCountWinnerSoulB += countWinnerSoulB
    sumAvgRound += avgRound

avgCountWinnerBodyA = sumCountWinnerBodyA // countSample
avgCountWinnerBodyB = sumCountWinnerBodyB // countSample
avgCountWinnerSoulA = sumCountWinnerSoulA // countSample
avgCountWinnerSoulB = sumCountWinnerSoulB // countSample
avgAvgRound = sumAvgRound // countSample    

print("avgCountWinnerBodyA    ", end='')
print(avgCountWinnerBodyA)
print("avgCountWinnerBodyB    ", end='')
print(avgCountWinnerBodyB)
print("avgCountWinnerSoulA    ", end='')
print(avgCountWinnerSoulA)
print("avgCountWinnerSoulB    ", end='')
print(avgCountWinnerSoulB)
print("avgAvgRound    ", end='')
print(avgAvgRound)
    
    