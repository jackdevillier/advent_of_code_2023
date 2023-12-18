# read file, split into lines
inputArr = open("day1input.txt").readlines()
totalnums = 0
for line in inputArr:
    #track first and last number occurences
    firstFound = False
    firstNum = 0
    lastFound = False
    lastNum = 0
    for i in range(len(line)):
        #move forward in line to find first num
        if line[i].isnumeric() and firstFound == False:
            firstFound = True
            firstNum = line[i]
        #move backward in line to find last num
        if line[len(line) - 1 - i].isnumeric() and lastFound == False:
            lastFound = True
            lastNum = line[len(line) - 1 - i]
    totalnums = totalnums + int(str(firstNum) + str(lastNum))
print(totalnums)

