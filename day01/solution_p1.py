max = 0
cur = 0

with open("input.txt") as f:
    for line in f:
        if (line == "\n"):
            max = cur if (cur > max) else max
            # print("max is now: " + str(max))
            cur = 0
        else:
            cur += int(line)
            # print("cur is now: " + str(cur))

f.close()

print(max)

# Space: O(1), Time O(n)
