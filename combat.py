#coding: utf-8

#引用
import random

#常量定义
BODY_PWR = 0
BODY_SPD = 1
BODY_STM = 2

SOUL_FRE = 0
SOUL_WTR = 1
SOUL_ETH = 2
SOUL_WOD = 3
SOUL_MTL = 4

HEALTH_BODY = 10
HEALTH_SOUL = 10

#输入待判定的两个点数，加上属性克制修正，以及随机性修正，返回正数，0，或负数
def judge(valueA, valueB, correctParam=0, correctRand=0):
    return valueA - valueB + correctParam + correctRand
    
#掷n面骰子，默认六面骰子，返回0~n-1
def dice(count=6):
    return (random.randint(0,count-1))
    
#修正身体参数，返回正数，0，或负数
def correctBody(paramA, paramB):
    d = (paramA - paramB)%3
    if d == 0:
        return 0
    elif d == 1:
        return 1
    elif d == 2:
        return -1
    else:
        assert()
        
#修正元神参数，返回正数，0，或负数
def correctSoul(paramA, paramB):
    d = (paramA - paramB)%5
    if d == 0:
        return 0
    elif d == 1 or d == 2:
        return 1
    elif d == 3 or d == 4:
        return -1
    else:
        assert()

#修正随机骰子，例如：0表示减益，5表示增益，返回正数，0，或负数
def correctRandom():
    d = dice(6)
    if d == 0:
        return -1
    elif d == 5:
        return 1
    else:
        return 0
        
def getValue(num):
    assert(num>=0)
    if num >= 0 and num < 40:
        return 0
    elif num >= 40 and num < 70:
        return 1
    elif num >= 70 and num < 90:
        return 2
    else:
        return 3
        
#战斗过程，每次判定失败者扣除一点生命，到0结束        
def combatBody(playerA, playerB):
    healthBodyA, healthBodyB = HEALTH_BODY, HEALTH_BODY
    playerBodyA, playerBodyB = playerA[:3], playerB[:3]
    diceListBodyA, diceListBodyB = setDiceListBody(playerA), setDiceListBody(playerB)
    round = 0
    while True:
        round += 1
        diceBodyA, diceBodyB = dice(6), dice(6)   
        paramBodyA, paramBodyB = diceListBodyA[diceBodyA], diceListBodyB[diceBodyB]
        valueBodyA, valueBodyB = getValue(playerBodyA[paramBodyA]), getValue(playerBodyB[paramBodyB])
        correctRand = correctRandom()
        result = judge(valueBodyA, valueBodyB, correctBody(paramBodyA, paramBodyB), correctRand)
        if result < 0:
            healthBodyA -= 1
        elif result > 0:
            healthBodyB -= 1
        if healthBodyA == 0 or healthBodyB == 0:
            break
    return healthBodyA, healthBodyB, round
 
#战斗过程，每次判定失败者扣除一点生命，到0结束        
def combatSoul(playerA, playerB):
    healthSoulA, healthSoulB = HEALTH_SOUL, HEALTH_SOUL
    playerSoulA, playerSoulB = playerA[-5:], playerB[-5:]
    diceListSoulA, diceListSoulB = setDiceListSoul(playerA), setDiceListSoul(playerB)
    round = 0
    while True:
        round += 1
        diceSoulA, diceSoulB = dice(6), dice(6)   
        paramSoulA, paramSoulB = diceListSoulA[diceSoulA], diceListSoulB[diceSoulB]
        valueSoulA, valueSoulB = getValue(playerSoulA[paramSoulA]), getValue(playerSoulB[paramSoulB])
        correctRand = correctRandom()
        result = judge(valueSoulA, valueSoulB, correctSoul(paramSoulA, paramSoulB), correctRand)
        if result < 0:
            healthSoulA -= 1
        elif result > 0:
            healthSoulB -= 1
        if healthSoulA == 0 or healthSoulB == 0:
            break
    return healthSoulA, healthSoulB, round

#战斗过程，每次判定失败者扣除一点生命，到0结束        
def combatBoth(playerA, playerB):
    healthBodyA, healthBodyB = HEALTH_BODY, HEALTH_BODY
    playerBodyA, playerBodyB = playerA[:3], playerB[:3]
    diceListBodyA, diceListBodyB = setDiceListBody(playerA), setDiceListBody(playerB)
    healthSoulA, healthSoulB = HEALTH_SOUL, HEALTH_SOUL
    playerSoulA, playerSoulB = playerA[-5:], playerB[-5:]
    diceListSoulA, diceListSoulB = setDiceListSoul(playerA), setDiceListSoul(playerB)
    round = 0
    while True:
        round += 1
        diceBodyA, diceBodyB = dice(6), dice(6)   
        paramBodyA, paramBodyB = diceListBodyA[diceBodyA], diceListBodyB[diceBodyB]
        valueBodyA, valueBodyB = getValue(playerBodyA[paramBodyA]), getValue(playerBodyB[paramBodyB])
        correctRand = correctRandom()
        result = judge(valueBodyA, valueBodyB, correctBody(paramBodyA, paramBodyB), correctRand)
        if result < 0:
            healthBodyA -= 1
        elif result > 0:
            healthBodyB -= 1
        if healthBodyA == 0 or healthBodyB == 0:
            break
        diceSoulA, diceSoulB = dice(6), dice(6)   
        paramSoulA, paramSoulB = diceListSoulA[diceSoulA], diceListSoulB[diceSoulB]
        valueSoulA, valueSoulB = getValue(playerSoulA[paramSoulA]), getValue(playerSoulB[paramSoulB])
        correctRand = correctRandom()
        result = judge(valueSoulA, valueSoulB, correctSoul(paramSoulA, paramSoulB), correctRand)
        if result < 0:
            healthSoulA -= 1
        elif result > 0:
            healthSoulB -= 1
        if healthSoulA == 0 or healthSoulB == 0:
            break
    return healthBodyA, healthBodyB, healthSoulA, healthSoulB, round
 
#自定义骰子，例如3-2-1，3-1-1-1
def setDiceListBody(player):
    playerBody = player[:3]
    indexPlayerBody = [i for i,v in sorted(enumerate(playerBody), key=lambda x:x[1], reverse=True)]
    return [indexPlayerBody[0], indexPlayerBody[0], indexPlayerBody[0], indexPlayerBody[1], indexPlayerBody[1], indexPlayerBody[2]]

#自定义骰子，例如3-2-1，3-1-1-1
def setDiceListSoul(player):
    playerSoul = player[-5:]
    indexPlayerSoul = [i for i,v in sorted(enumerate(playerSoul), key=lambda x:x[1], reverse=True)]
    return [indexPlayerSoul[0], indexPlayerSoul[0], indexPlayerSoul[0], indexPlayerSoul[1], indexPlayerSoul[2], indexPlayerSoul[3]]    