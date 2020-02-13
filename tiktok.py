a = []
b = []
k = 0
comb = [[0, 1, 2],[0, 4, 8],[0, 3, 6],[1, 4, 7],[2, 4, 6],[2, 5, 8],[3, 4, 5],[6, 7, 8]]
def wonlost():
    for f in comb:
                if f[0] in a and f[1] in a and f[2] in a:
                        print("won A")
                        break
                elif f[0] in b and f[1] in b and f[2] in b:
                        print("won B")
                        break
from appearanceAB import appearance
appearance(a, b)
while k < 4:
    n1 = int(input()) - 1
    a.append(n1)
    appearance(a, b)
    wonlost()
    n2 = int(input()) - 1
    b.append(n2)
    appearance(a, b)
    wonlost()
k += 1
n3 = int(input())
a.append(n3)
wonlost()
print(a, b, "draw")
