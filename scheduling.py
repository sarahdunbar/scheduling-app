def makeList(phrase, rank):
    num = int(input(phrase))
    if num > 0:
        print ("Please rank the tasks in order of " + rank + ": ")
    if num == 0:
        print ("")
    nameList = ["0"]*num
    timeList = [0]*num
    for i in range (0, num):
        entre = input(str(i + 1) + ": ")
        nameList[i] = entre
        time = int(input("Time (in minutes): "))
        timeList[i] = time
        print ("")
    return nameList, timeList

def formatZeroes(number):
    if number < 10:
        numberString = ("0" + str(number))
    else:
        numberString = str(number)
    return numberString

def timeAdd(oldHour, oldMinute, finalHour, finalMinute, test, index, nameList, timeList):
    activity = nameList[index]
    time = timeList[index]
    antiqueHour = oldHour
    antiqueMinute = oldMinute
    minTemp = oldMinute + time
    if minTemp >= 60:
        amount = minTemp%60
        minRound = minTemp - amount
        hours = minRound/60
        minTemp = int(minTemp - 60*hours)
        hour = int(oldHour + hours)
    else:
        hour = oldHour
    minute = minTemp
    if hour > finalHour:
        minute = finalMinute
        hour = finalHour
        test = False
    if hour == finalHour and minute >= finalMinute:
        minute = finalMinute
        hour = finalHour
        test = False
    oldMinuteString = formatZeroes(antiqueMinute)
    newMinuteString = formatZeroes(minute)
    print (activity + ": " + str(antiqueHour) + ":" + oldMinuteString + " - " + str(hour) + ":" + newMinuteString)
    return test, hour, minute
    
def extraTasks():
    print ("1. At home in the day")
    print ("2. At home at night")
    print ("3. At school, with free time")
    print ("4. At school, in class")
    print ("5. At the library")
    print ("6. Other")
    jaws = True
    while jaws == True:
        where = input ("Which of the following best describes your location? (other assumes you have no objects) ")
        if where == "1":
            otherList = ["deviantArt", "Doodles", "Just Dance", "Speedpaint", "Mindfulness"]
            otherTime = [10, 15, 30, 30, 10]
            jaws = False
        elif where == "2":
            otherList = ["deviantArt", "Doodles", "Stretching", "Speedpaint", "Mindfulness"]
            otherTime = [10, 15, 15, 30, 10]
            jaws = False
        elif where == "3":
            otherList = ["deviantArt", "Buy something from caf", "Doodles", "Yearbook page", "Math team worksheet"]
            otherTime = [10, 10, 5, 10, 15]
            jaws = False
        elif where == "4":
            otherList = ["deviantArt", "Stretching", "Facebook"]
            otherTime = [10, 5, 10]
            jaws = False
        elif where == "5":
            otherList = ["deviantArt", "Get hot chocolate", "Doodles", "Yearbook page", "Onion"]
            otherTime = [10, 15, 10, 10, 5]
            jaws = False
        elif where == "6":
            otherList = ["deviantArt", "Speed poetry", "Facebook", "Onion", "Flower rxn"]
            otherTime = [10, 15, 10, 5, 10]
            jaws = False
        else:
            print ("Invalid command")
    print (" ")
    return otherList, otherTime
            
hourTime = int(input("Hour of the day (military time): "))
minuteTime = int(input("Minute of the day: "))
print ("")
endHourTime = int(input("End hour of session (military time): "))
endMinuteTime = int(input("End minute of session: "))
print("")
otherList, otherTime = extraTasks()
mandNameList, mandTimeList = makeList("How many tasks do you need to do? ", "importance")
funNameList, funTimeList = makeList("How many diversionary tasks would you like to do? ", "enjoyment")
stillScheduling = True
print ("SCHEDULE")
if len(mandNameList) > len(funNameList):
    tot = len(mandNameList)
    bigList = 0
else:
    tot = len(funNameList)
    bigList = 1
for i in range (0, tot):
    if i < len(mandNameList) and stillScheduling == True:
        stillScheduling, hourTime, minuteTime = timeAdd(hourTime, minuteTime, endHourTime, endMinuteTime, stillScheduling, i, mandNameList, mandTimeList)
    if i < len(funNameList) and stillScheduling == True:
        stillScheduling, hourTime, minuteTime = timeAdd(hourTime, minuteTime, endHourTime, endMinuteTime, stillScheduling, i, funNameList, funTimeList)
    if i >= len(mandNameList) or i >= len(funNameList) and stillScheduling == True:
        index = i%4
        stillScheduling, hourTime, minuteTime = timeAdd(hourTime, minuteTime, endHourTime, endMinuteTime, stillScheduling, index, otherList, otherTime)
while stillScheduling == True:
    for i in range (0, 4):
        stillScheduling, hourTime, minuteTime = timeAdd(hourTime, minuteTime, endHourTime, endMinuteTime, stillScheduling, i, otherList, otherTime)
