# read file, split into lines
nums_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
inputArr = open("day1input.txt").readlines()
totalnums = 0

def check_spelled(string, front_index):
    end_index = front_index + 1
    while end_index < len(string) + 1:
        if end_index - front_index > 5:
            return -1
        if string[front_index:end_index] in nums_list:
            return convert_num(string[front_index:end_index])
        end_index = end_index + 1
    return -1
        
def convert_num(string):
    for i in range(len(nums_list)):
        if string == nums_list[i]:
            return i + 1
    return -1

for line in inputArr:
    #track first and last number occurences
    firstFound = False
    firstNum = 0
    lastFound = False
    lastNum = 0
    for i in range(len(line)):
        #move forward in line to find first num
        try_front_spelling = check_spelled(line, i)
        try_end_spelling = check_spelled(line, len(line) - 1 - i)
        if line[i].isnumeric() and firstFound == False:
            firstFound = True
            firstNum = line[i]
        elif try_front_spelling > 0 and firstFound == False:
            firstFound = True
            firstNum = try_front_spelling
        #move backward in line to find last num
        if line[len(line) - 1 - i].isnumeric() and lastFound == False:
            lastFound = True
            lastNum = line[len(line) - 1 - i]
        elif try_end_spelling > 0 and lastFound == False:
            lastFound = True
            lastNum = try_end_spelling
    totalnums = totalnums + int(str(firstNum) + str(lastNum))

print(totalnums)

