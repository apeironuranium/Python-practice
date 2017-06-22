import random
from string import punctuation

class Letters(object):

    def randomin(self,s):
        if len(s)>2 and (s[-1] not in list(punctuation)):
            return s[0] + "".join(random.sample(s[1:-1], len(s) - 2)) + s[-1]
        elif len(s) > 2 and (s[-1] in list(punctuation)):
            return s[0] + "".join(random.sample(s[1:-2], len(s) - 3)) + s[-2:]
        else:
            return s

    def out(self, s):
        s_words = s.split()
        print(" ".join([self.randomin(x) for x in s_words]))

text = input("Введите предложение:")
Letters().out(text)
