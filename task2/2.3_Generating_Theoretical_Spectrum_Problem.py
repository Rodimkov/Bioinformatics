mas = {
	'A' : 71, 'R' : 156, 'N' : 114, 'D' : 115, 'C' : 103, 'E' : 129, 'Q' : 128, 'G' : 57, 'H' : 137,  'I' : 113, 'L' : 113, 
    'K' : 128, 'M' : 131, 'F' : 147, 'P' : 97, 'S' : 87, 'T' : 101, 'W' : 186, 'Y' : 163, 'V' : 99 
}

string = input()
arr = [0]

for i in range(1, len(string)):
    for j in range(len(string)):
        subpep = ""
        tmp = 0
        if i > len(string) - j: 
            tail = len(string) - j
            stump = i - tail
        else:
            tail = i 
            stump = i - tail
        subpep += string[j:j+tail] + string[0:stump]
        for k in subpep:
            tmp += mas.get(k)
        arr.append(tmp)

arr.sort()
tmp = 0
for k in string:
    tmp += mas.get(k)
arr.append(tmp)
for i in arr:
    print(i, end=" ")