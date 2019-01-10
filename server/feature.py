
import TFIDFCalculator as tfidfCalculator
from ContentCalculator import ContentCalculator

def booleanToInt(value):
    if value:
        return 1
    return 0

def dataToFeatureRow(title, body):
    idValue = -1
    result = -1
    if result == "no-clickbait":
        result = False
    else:
        result = True
    tfidfs = tfidfCalculator.TFIDFCalculator()
    sims = tfidfs.calculateTFIDFofNew(title, body)
    if len(sims) < 1:
        return []
    top1Sim = sims[0]
    top2Sim = sims[1]
    top3Sim = sims[2]
    top4Sim = sims[3]
    top5Sim = sims[4]
    content = ContentCalculator(title, body)
    numberOfTitle, numberOfBody = content.numWords()
    if numberOfTitle == 0 or numberOfBody < 1:
        return []
    numberOfCap = content.numCap()
    numberOfAcronym = content.numAcronym()
    isExclm, numberOfExclm = content.exclm()
    isQues, numberOfQues = content.ques()
    isStartNum = content.isStartNum()
    hasNumber = content.hasNumber()
    isSuperlative = content.isSuperlative()
    isQuote, numberOfQuote = content.quoteCounter()
    isStart5W1H = content.isStart5W1H()
    isNeg, numberOfNeg = content.neg()
    isPos, numberOfPos = content.pos()
    isBaity, numberOfBaity = content.baity()
    hasParenthesis = content.hasParenthesis()
    hasMoney = content.hasMoney()
    avgWordSent = content.avgWordSent()
    isForwardReference, numberOfForwardReference = content.forwardReference()
    CLScore = content.CLScore()
    rixScore, lixScore = content.RIXandLIXIndices()
    formalityMeasure = content.formalityMeasure()
    row = [top1Sim, top2Sim, top3Sim, top4Sim, top5Sim, numberOfTitle, numberOfBody, numberOfCap, numberOfAcronym, booleanToInt(isExclm), numberOfExclm, booleanToInt(isQues), numberOfQues, booleanToInt(isStartNum), booleanToInt(hasNumber),
           booleanToInt(isSuperlative), booleanToInt(isQuote), numberOfQuote, booleanToInt(isStart5W1H), booleanToInt(isNeg), numberOfNeg, booleanToInt(isPos), numberOfPos, booleanToInt(isBaity), numberOfBaity, booleanToInt(hasParenthesis), booleanToInt(hasMoney), avgWordSent, booleanToInt(isForwardReference),
           numberOfForwardReference, CLScore, rixScore, lixScore, formalityMeasure]
    return row


def getFeatures(title, body):
    return dataToFeatureRow(title, body)


