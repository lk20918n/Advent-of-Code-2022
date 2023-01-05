import re
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.intersection(y)

# print(z)

def parse_Contains(buffer):
    pair = buffer.split(',')
    e1 = pair[0].split('-')
    e2 = pair[1].split('-')
    for i in range(2):
        e1[i] = int(e1[i])
        e2[i] = int(e2[i])
    if((e1[0] >= e2[0]) and (e1[1] <= e2[1])):
        return True
    elif(e1[0] <= e2[0] and e1[1] >= e2[1]):
        return True

    return False

def parse_Overlaps(buffer):
    pair = buffer.split(',')
    e1 = pair[0].split('-')
    e2 = pair[1].split('-')
    for i in range(2):
        e1[i] = int(e1[i])
        e2[i] = int(e2[i])
    if((e1[0] <= e2[1]) and (e2[0] <= e1[1])):
        return True
    return False


# f = open('test.txt','r')
# buf = f.read().split('\n')
# # buf = parse(buf)
# print(buf)

count1 = 0
count2 = 0

with open('input.txt') as f:
    for line in f:
        if(parse_Contains(line.replace('\n','')) == True):
            count1 += 1
        if(parse_Overlaps(line.replace('\n','')) == True):
            count2 += 1


print(count1)
print(count2)
