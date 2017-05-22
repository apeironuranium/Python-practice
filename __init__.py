import sys


class FrogPelophylaxRidibundus:
    def __init__(self, l, w):
        self.long = l
        self.weight = w


    def outing(self):
        print(self.long, self.weight)


def self(args):
    pass


class  Amphibia(FrogPelophylaxRidibundus):
    def Frog(self, n):

        n = int(input('Enter length of frog: '))
        print(n)
        if n < 6:
            print("It is not a Frog Pelophylax Ridibundus")
        else:
            print("It's Ok")
    print (Frog(self,n=int()))



t_parametres = Amphibia(6, 200)
t_parametres.outing()


class Chordata(Amphibia, FrogPelophylaxRidibundus):
    def __init__(self):
        # something
        super().__init__()

print(issubclass(Amphibia, FrogPelophylaxRidibundus))
print(issubclass(Chordata, Amphibia))