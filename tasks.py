from Tools.Scripts.treesync import raw_input
#2
from itertools import takewhile
print(sum(takewhile(lambda x : x<10, [0,1,2,3,4,5,6,7,8,9] )))

#5
a = [1,3,0,5,0,0,2]
max_index = a.index(max(a))
res = a[:max_index+1]+list(filter(lambda x:x !=0, a[max_index+1:]))
print(res)

#10
import distance

distance.levenshtein("lenvestein", "levenshtein")
distance.hamming("hamming", "hamning")
print(distance.hamming("GATGGAACTTGACTACGTAAATT","GAUGGAACUUGACUACGUAAAUU"))

#12

s = "srdgttrgbtr,gersg"
print(s.replace(',', ''))

# или

s = "sr,rt.ytu:dsg;?"
out = "".join(c for c in s if c not in ('!','.',':',';','?',','))
print(out)

#1
import sys

def flip_str1(s):
    for i in range(len(s)):
        sys.stdout.write(s[-i - 1])
    sys.stdout.write('\n')

s = raw_input('Enter string:')
flip_str1(s)




