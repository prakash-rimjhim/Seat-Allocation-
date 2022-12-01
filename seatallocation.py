#Write a program that helps seat audiences in a flight based on the following input and rules.

from array import *
seatDimensions = [[3,2],[4,3],[2,3],[3,4]]
passengerCount = 30

resultArray = []

maxRowCount = 0

allocatedCount = 0

def fillResultArray(resultArray):
    maxRowCount = 0
    for seatDimension in seatDimensions:
        if(maxRowCount < seatDimension[1]):
            maxRowCount = seatDimension[1]
        resultArray.append([[0 for _ in range(seatDimension[0])] for _ in range(seatDimension[1])])
    #print(resultArray)
    return resultArray, maxRowCount
    
resultArray, maxRowCount = fillResultArray(resultArray)

print(maxRowCount)

def fillAsileSeats(resultArray, allocatedCount):
    seatGroupCount = len(resultArray)
    
    if(seatGroupCount > 1):
        for i in range(maxRowCount):
            if(allocatedCount >= passengerCount):
                break
            
            for j in range(seatGroupCount):
                if(allocatedCount >= passengerCount):
                    break
                
                seatGroup = resultArray[j]
                if(i < len(seatGroup)):
                    row = seatGroup[i]
                    #print(row)
                    if(j == 0):
                        rightColumnINdex = len(seatGroup[0]) - 1
                        if(rightColumnINdex > 0):
                            allocatedCount = allocatedCount + 1
                            row[rightColumnINdex] = allocatedCount
                    elif(j == seatGroupCount-1):
                        rightColumnINdex = len(seatGroup[0]) - 1
                        if(rightColumnINdex > 0):
                            allocatedCount = allocatedCount + 1
                            row[0] = allocatedCount
                    else:
                        seatCount = len(row)
                        if(seatCount == 1):
                            allocatedCount = allocatedCount + 1
                            row[0] = allocatedCount
                        else:
                            allocatedCount = allocatedCount + 1
                            row[0] = allocatedCount
                            allocatedCount = allocatedCount + 1
                            row[seatCount - 1] = allocatedCount
                        
    return resultArray, allocatedCount

def fillWindowSeats(resultArray, allocatedCount):
    seatGroupCount = len(resultArray)
    
    if(seatGroupCount > 1):
        for i in range(maxRowCount):
            if(allocatedCount >= passengerCount):
                break
            
            for j in range(seatGroupCount):
                if(allocatedCount >= passengerCount):
                    break
                
                seatGroup = resultArray[j]
                if(i < len(seatGroup)):
                    row = seatGroup[i]
                    if(j == 0):
                        allocatedCount = allocatedCount + 1
                        row[0] = allocatedCount
                    elif(j == seatGroupCount-1):
                        allocatedCount = allocatedCount + 1
                        row[-1] = allocatedCount
                    
                        
    return resultArray, allocatedCount     
    
def fillMiddleSeats(resultArray, allocatedCount):
    seatGroupCount = len(resultArray)
    
    if(seatGroupCount > 1):
        for i in range(maxRowCount):
            if(allocatedCount >= passengerCount):
                break

            for j in range(seatGroupCount):
                if(allocatedCount >= passengerCount):
                    break
                
                seatGroup = resultArray[j]
                if(i < len(seatGroup)):
                    row = seatGroup[i]
                    seatCount = len(row)
                    for seatIndex in range(seatCount):
                        if(allocatedCount >= passengerCount):
                            break
                        if(row[seatIndex] == 0):
                            allocatedCount = allocatedCount + 1
                            row[seatIndex] = allocatedCount
                        
    return resultArray, allocatedCount
resultArray, allocatedCount = fillAsileSeats(resultArray, allocatedCount)
resultArray, allocatedCount = fillWindowSeats(resultArray, allocatedCount)
resultArray, allocatedCount = fillMiddleSeats(resultArray, allocatedCount)


print(resultArray)
