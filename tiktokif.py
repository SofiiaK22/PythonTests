dictionary = {'x': [], 'o': []}
a = dictionary['x']
b = dictionary['o']
k = 0
comb = [[0, 1, 2],[0, 4, 8],[0, 3, 6],[1, 4, 7],[2, 4, 6],[2, 5, 8],[3, 4, 5],[6, 7, 8]]
def wonlost():
    for m in dictionary:
        s = dictionary[m]
        for f in comb:
                if f[0] in s and f[1] in s and f[2] in s:
                    print("won!")
                    break
from appearanceAB import appearance
appearance(a, b)
while k < 4:
    for m in dictionary:
        s = dictionary[m]
        n1 = int(input()) - 1
        if n1 in a or n1 in b or n1 > 8 or n1 < -1:
            print("Use another number:")
            break
            n1 = int(input()) - 1
            continue
        else:
            s.append(n1)
            appearance(a, b)
            wonlost()
k += 1
print(a, b, "draw")
