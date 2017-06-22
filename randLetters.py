import random
from string import punctuation

def randomize(s):
    l_s = len(s)
    if (l_s > 2) and (s[-1] not in list (punctuation)):
        res = s[0] + "".join(random.sample(s[1:-1], l_s - 2)) + s[-1]
    elif (l_s > 2) and (s[-1] in list (punctuation)):
        res = s[0] + "".join(random.sample(s[1:-2], l_s - 3)) + s[-2:]
    else:
        res = s
    return res

s = input("Введите предложение:")
s_words = s.split()
print(" ".join(([randomize(x) for x in s_words])))

