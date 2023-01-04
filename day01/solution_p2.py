list = []
sum = 0

with open("input.txt") as f:
    for line in f:
        if (line == "\n"):
            list.append(sum)
            sum = 0
        else:
            sum += int(line)

f.close()

list.sort(reverse=True)
# print(list)
print(list[0]+list[1]+list[2])

# Space: O(n), Time: O(n.logn)
