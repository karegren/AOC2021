def task_1(values):


    prev = None
    count = 0
    for value in values:
        value = int(value)
        if prev == None:
            prev = value
            continue
        if value > prev:
            count += 1
        prev = value
            
    print(count)

def task_2(values):
    
    count = 0
    sums = []
    for i in range(0, len(values)-2):
        
        value = int(values[i])+int(values[i+1])+int(values[i+2])
        sums.append(value)
    
    prev = sums[0]
    for sum in sums[1:]:
        if sum > prev:
            count += 1
        prev = sum
    print(count)


input = open('01.txt', "r")
values = input.readlines()
task_1(values)
task_2(values)