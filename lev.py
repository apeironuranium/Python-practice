import timeit
import distance

def lev(f_string, s_string):
    len_f_string = len(f_string)+1
    len_s_string = len(s_string)+1
    matr = [[0 for x in range(len_f_string)] for y in range(len(s_string) + 1)]

    del_cost = 1
    add_cost = 1
    rep_cost = lambda x, y: 1 if x != y else 0

    for j in range(1, len_f_string):
        matr[0][j] = matr[0][j - 1] + add_cost
    for i in range(1, len_s_string):
        matr[i][0] = matr[i - 1][0] + del_cost
        for j in range(1, len_f_string):
            matr[i][j] = min([
                matr [i-1][j]+del_cost,
                matr [i][j-1]+add_cost,
                matr [i-1][j-1]+rep_cost(f_string[j-1], s_string[i-1]),
            ])
    # for x in matr:
        # print(x)
    return matr[len_s_string-1][len_f_string-1]

f_string = "everybody"
s_string = "sleep"

assert lev(f_string, s_string) == distance.levenshtein(f_string, s_string)

print(timeit.timeit('lev("everybody", "sleep")', setup="from __main__ import lev", number=1000))
print(timeit.timeit('distance.levenshtein("everybody", "sleep")', setup="import distance", number=1000))

