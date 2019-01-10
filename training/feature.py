import sys
import csv


import TFIDFCalculator as tfidfCalculator
from ContentCalculator import ContentCalculator

def booleanToInt(value):
    if value:
        return 1
    return 0

def dataToFeatureRow(data):
    idValue = data[1]
    result = data[3]
    if result == "no-clickbait":
        result = False
    else:
        result = True
    tfidfs = tfidfCalculator.TFIDFCalculator()
    sims = tfidfs.calculateTFIDFofNew(data[0], data[4])
    if len(sims) < 1:
        return []
    top1Sim = sims[0]
    top2Sim = sims[1]
    top3Sim = sims[2]
    top4Sim = sims[3]
    top5Sim = sims[4]
    content = ContentCalculator(data[0], data[4])
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
    row = [idValue, booleanToInt(result), top1Sim, top2Sim, top3Sim, top4Sim, top5Sim, numberOfTitle, numberOfBody, numberOfCap, numberOfAcronym, booleanToInt(isExclm), numberOfExclm, booleanToInt(isQues), numberOfQues, booleanToInt(isStartNum), booleanToInt(hasNumber),
           booleanToInt(isSuperlative), booleanToInt(isQuote), numberOfQuote, booleanToInt(isStart5W1H), booleanToInt(isNeg), numberOfNeg, booleanToInt(isPos), numberOfPos, booleanToInt(isBaity), numberOfBaity, booleanToInt(hasParenthesis), booleanToInt(hasMoney), avgWordSent, booleanToInt(isForwardReference),
           numberOfForwardReference, CLScore, rixScore, lixScore, formalityMeasure]
    return row

def getHeaders():
    return ["id", "result", "top1Sim","top2Sim","top3Sim","top4Sim","top5Sim","numberOfTitle","numberOfBody","numberOfCap","numberOfAcronym","isExclm","numberOfExclm","isQues","numberOfQues","isStartNum","hasNumber",
           "isSuperlative","isQuote","numberOfQuote","isStart5W1H","isNeg","numberOfNeg","isPos","numberOfPos","isBaity","numberOfBaity","hasParenthesis","hasMoney","avgWordSent","isForwardReference",
           "numberOfForwardReference","CLScore","rixScore","lixScore","formalityMeasure"]


def readCsv():
    with open('trainingDataSet.csv', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        writer = csv.writer(open("nonbooleanfeatures.csv", 'w', newline=''))
        writer.writerow(getHeaders())
        i = 0
        for row in csv_reader:
            feature = dataToFeatureRow(row)
            if len(feature) > 1:
                writer.writerow(feature)
                print(i)
                i += 1

csv.field_size_limit(sys.maxsize)
readCsv()

