count = 0
buf = 0

dict = {'AX': 1+3, "AY": 2+6, "AZ": 3+0,
        'BX': 1+0, "BY": 2+3, "BZ": 3+6,
        'CX': 1+6, "CY": 2+0, "CZ": 3+3, }


with open("input.txt") as f:
    for line in f:
        buf = line.replace(" ", "")
        buf = buf.replace("\n", "")
        count += dict[buf]

f.close()

print(count)
