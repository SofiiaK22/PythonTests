comb = [[0, 1, 2],[0, 4, 8],[0, 3, 6],[1, 4, 7],[2, 4, 6],[2, 5, 8],[3, 4, 5],[6, 7, 8]]
def wonlost(dictionary):
    result = 0
    for m in dictionary:
        s = dictionary[m]
        for f in comb:
            if f[0] in s and f[1] in s and f[2] in s:
                result = 2
                break
            elif 5 == len(dictionary[m]):
                result = 1
    return result
'''   
def checkWin(comb):
    for f in comb:
        if f in comb:
            return f
    return []
    
def judge(comb):
    result = 0
    if len(comb) >= 3:
        if len(checkWin(comb)):
            result = 2
        else:
            if 5 == len(comb):
                result = 1
    return result'''