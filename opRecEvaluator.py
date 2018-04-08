import matplotlib.pyplot as plt
import pprint as pp
import xlrd
import math

workbook = xlrd.open_workbook("Dataset.xlsx")
dataset = workbook.sheet_by_index(0)
testData = []

#thresshold

high = 70
mid  = 50
low  = 25
interval = 5


def sigmoidUp (x, a, b, c):
    if (x <= a):
        return 0
    elif (x <= b):
        return 2 * math.pow((x - a) / (c-a), 2)
    elif (x < c):
        return 1 - (2 * math.pow((c - x) / (c - a)))
    else
        return 1

def sigmoiDown (x, a, b, c):
    if (x <= a):
        return 1
    elif (x <= b):
        return 1 - (2 * math.pow((c - x) / (c - a)))
    elif (x < c):
        return 2 * math.pow((x - a) / (c-a), 2)
    else:
        return 0



def rendah (x):
    pass

def sedang (x):
    pass

def tinggi (x):
    pass


if __name__ == '__main__':
    
    # initialize control dataset
    for i in range (0, 18):
        testData.append ({
            'id': i,
            'writtenScore': dataset.cell (i + 2, 2).value,
            'InterviewScore': dataset.cell (i + 2, 3).value,
            'result': True if (dataset.cell (i + 2, 4).value) else False
        })

    print ('control dataset : ')
    pp.pprint (testData)
    
    # initialize teset dataset
    for i in range (0, 18):
        testData.append ({
            'id': i,
            'writtenScore': dataset.cell (i + 2, 2).value,
            'InterviewScore': dataset.cell (i + 2, 3).value,
            'result': None
        })

    print ('\ntest dateset : ')
    pp.pprint (testData)


