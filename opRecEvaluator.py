import matplotlib.pyplot as plt
import pprint as pp
import xlrd
import math

workbook = xlrd.open_workbook("Dataset.xlsx")
dataset = workbook.sheet_by_index(0)
controlData = []
testData = []


#thresshold

mid  = 70
low  = 30

interval = 5

def dist (a, b):
    return b - a

def sigmoidUp (x, a, b):
    if x <= a:
        return 0
    elif x <= a + dist(a, b) / 2:
        return 2 * math.pow((x - a) / (b-a), 2)
    elif x < b:
        return 1 - (2 * math.pow((b - x) / (b - a), 2))
    else:
        return 1

def sigmoidDown (x, a, b):
    if x <= a:
        return 1
    elif x <= a + dist(a, b) / 2:
        return 1 - (2 * math.pow((x - a) / (b - a), 2))
    elif x < b:
        return 2 * math.pow((b - x) / (b - a), 2)
    else:
        return 0

def sigmoid (x, min, max):
    return sigmoidUp(x, min, min + (dist(min, max) / 2)) if (x < min + dist(min, max) / 2) else sigmoidDown(x, min + (dist(min, max) / 2), max) 

def rendah (x):
    return sigmoidDown (x, 0, low + interval)

def sedang (x):
    return sigmoid (x, low - interval, mid + interval)

def tinggi (x):
    return sigmoidUp (x, mid - interval, 100)

def Fuzzification (crispData):
    return {
        "low"  : rendah (crispData),
        "mid"  : sedang (crispData),
        "high" : tinggi (crispData)
    }

def Inteference (fuzzyData):
    return {
        "Y":   (fuzzyData[0]["low"] and fuzzyData[1]["high"]) 
            or (fuzzyData[0]["high"] and fuzzyData[1]["low"])
            or (fuzzyData[0]["mid"] and fuzzyData[1]["mid"])
            or (fuzzyData[0]["high"] and fuzzyData[1]["mid"])
            or (fuzzyData[0]["high"] and fuzzyData[1]["high"]),
        "T":   (fuzzyData[0]["low"] and fuzzyData[1]["low"]) 
            or (fuzzyData[0]["low"] and fuzzyData[1]["mid"])
            or (fuzzyData[0]["mid"] and fuzzyData[1]["low"])
            or (fuzzyData[0]["mid"] and fuzzyData[1]["heigh"])
    }

def Defuzzification (fuzzyData):
    pass

if __name__ == '__main__':
    
    # initialize control dataset
    for i in range (0, 18):
        controlData.append ({
            'id': i,
            'writtenScore': dataset.cell (i + 2, 2).value,
            'InterviewScore': dataset.cell (i + 2, 3).value,
            'result': True if (dataset.cell (i + 2, 4).value) else False
        })

    print ('control dataset : ')
    pp.pprint (controlData)
    
    # initialize teset dataset
    for i in range (0, 10):
        testData.append ({
            'id': i,
            'writtenScore': dataset.cell (i + 2, 7).value,
            'InterviewScore': dataset.cell (i + 2, 8).value,
            'result': None
        })

    print ('\ntest dateset : ')

    pp.pprint (testData)

    plt.plot([x for x in range (0, low + interval)], [sigmoidDown (x, 0, low + interval) for x in range (0, low + interval)])
    plt.plot([x for x in range (low - interval, mid + interval)], [sigmoid (x, low - interval, mid + interval) for x in range (low - interval, mid + interval)])
    plt.plot([x for x in range (mid - interval, 100)], [sigmoidUp(x, mid - interval, 100) for x in range(mid - interval, 100)])
    plt.show()
