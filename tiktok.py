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
board = ['1', '|', '2', '|', '3', '\n', '4', '|', '5', '|', '6', '\n', '7', '|', '8', '|', '9']
print(''.join(board))
while k < 4:
    n1 = int(input())
    a.append(n1)
    board[(n1-1)*2]= 'x'
    wonlost()
    print(''.join(board))
    n2 = int(input())
    b.append(n2)
    wonlost()
    board[(n2-1)*2]= 'o'
    print(''.join(board))
    k += 1
n3 = int(input())
a.append(n3)
wonlost()
print(a, b, "draw")
