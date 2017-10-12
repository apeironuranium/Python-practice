import timeit
from email.policy import default


def average(people):
    if len(people) == 1:
        return people[0]
    else:
        pairs = []
        for x in range(len(people)//2):
            pairs.append((people[2*x]+people[2*x+1])/2)
        return average(pairs)
people = [1, 2, 3, 4, 5, 6, 7, 8]
print(average(people))

