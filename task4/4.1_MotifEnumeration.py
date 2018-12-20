import itertools

    
def eachPattern(k):
    patterns = [] 
    each = itertools.product('ATGC', repeat=k)
    for i in each:
        tmp = ''.join(i)
        patterns.append(tmp)
    return patterns

def differing(pat1, pat2):    
    if(pat1 == pat2):
       return 0
    tmp = 0
    i = 0
    for j in pat1:
        if j != pat2[i]:
            tmp+=1
        i+=1
    return tmp

def MotifEnumeration(DNA, k, d):
    patterns = []
    out = []
    count = 0
    for st in DNA:
        for i in range(len(st) - k + 1):
            eachpatterns = eachPattern(k)
            for tmp in eachpatterns:
                diff = differing(st[i:i+k], tmp)
                if diff <= d:
                    count = 0
                    for st1 in DNA:
                        for j in range(len(st1) - k + 1):
                            if differing(tmp, st1[j:j+k]) <= d:
                                count += 1
                                break
                    if count == len(DNA):
                        patterns.append(tmp)
    patterns.sort()
    for x in patterns:
        if (not x in out):
            out.append(x)
    out = ' '.join(out)
    return out

t = input()
t = t.split()
k = int(t[0])
d = int(t[1])
DNA = []
for i in range(k):
    DNA.append(input())

print(MotifEnumeration(DNA, k, d))