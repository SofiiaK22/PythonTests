import random

def myCalc():
    a = "Text"
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    x = a + b
    y = a * b
    return x,y

c,m = myCalc()
print(c,m)
