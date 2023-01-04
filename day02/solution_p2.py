count = 0
buf = 0

# A = 1, B = 2, C = 3
# X = 0, choose -1, Y = 3, choose same, Z = 6, choose +1
dict = {'AX': 0+3, "AY": 3+1, "AZ": 6+2,
        'BX': 0+1, "BY": 3+2, "BZ": 6+3,
        'CX': 0+2, "CY": 3+3, "CZ": 6+1, }


with open("input.txt") as f:
    for line in f:
        buf = line.replace(" ", "")
        buf = buf.replace("\n", "")
        count += dict[buf]

f.close()

print(count)
