import random

class Letters(object):

    def randomin(self,s):
        if len(s)>2:
            return s[0] + "".join(random.sample(s[1:-1], len(s) - 2)) + s[-1]
        else:
            return s

    def out(self, s):
        s_words = s.split()
        print(" ".join([self.randomin(x) for x in s_words]))


class Example():

    field = 0

    def __init__(self, field):
        print(self.field)
        self.field = field
        print(self.field)

    def field_increment(self):
        self.field += 1
        return self.field

example = Example(1)
print(example.field_increment())
print(example.field_increment())
print(example.field_increment())

text = input("Введите предложение:")
Letters().out(text)
