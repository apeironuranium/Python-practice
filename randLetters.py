import random

def randomize(s):
    l_s = len(s)
    if l_s > 2:
        res = s[0] + "".join(random.sample(s[1:-1], l_s - 2)) + s[-1]
    else:
        res = s
    return res

s = input("Введите предложение:")
s_words = s.split()
print(" ".join(([randomize(x) for x in s_words])))

