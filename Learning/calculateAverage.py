def calculateAverage():
    vals = int(input("Enter the number of values to be evaluated: "))
    valList = []

    for i in range(0, vals):
        nums = int(input("Enter a number: "))
        valList.append(nums)
    avg = sum(valList) / vals
    print("Average of values entered", round(avg, 2))

calculateAverage()