import json
import pandas as pd

def cleanText(text):
    return text.replace('\xa0', ' ')

def readFile(fileName):
    return tuple(open(fileName, 'r'))

def findById(id, array):
    for i in range(0, len(array)):
        if array[i]["id"] == id:
            return i
    return -1

def loadTruthFile(fileName):
    truth = []
    truthLines = readFile(fileName)
    for line in truthLines:
        lineJson = json.loads(line)
        id = lineJson["id"]
        result = lineJson["truthClass"]
        truth.append({"id": id, "result": result})
    return truth

def loadInstances(fileName, truth):
    allData = []
    instanceLines = readFile(fileName)
    for line in instanceLines:
        lineJson = json.loads(line)
        id = lineJson["id"]
        truthId = findById(id, truth)
        if truthId == -1:
            print("id not found")
            continue
        result = truth[truthId]["result"]
        title = cleanText(lineJson["targetTitle"])
        keywords = cleanText(lineJson["targetKeywords"])
        description = cleanText(lineJson["targetDescription"])
        text = ""
        for par in lineJson["targetParagraphs"]:
            text = text + (cleanText(par)+"\n")
        text = text[:-1]
        allData.append({"id": id, "result": result, "title": title, "keywords": keywords, "description": description, "text": text})
    return allData


truth = loadTruthFile("truth.jsonl")
news = loadInstances("instances.jsonl", truth)
pd.DataFrame(news).to_csv('trainingDataSet.csv', index=False, header=False)

