#array = ['где', 'гуляет', 'пёс']
#for i in array:
#    print(list(reversed(array)))

def reverse(s):
    l = s.split(" ")
    l.reverse()
    return " ".join(l)
print(reverse(input()))


