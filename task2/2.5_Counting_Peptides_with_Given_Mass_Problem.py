Masses = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]
k = int(input())
tmp = []
tmp.append(1)
for i in range(k+1):
    tmp.append(0)
    for j in range(len(Masses)):
        if (i >= Masses[j]):
            tmp[i] += tmp[i - Masses[j]]

print(tmp[k])