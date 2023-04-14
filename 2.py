# #1///
# def get_middle(s):
#     return s[len(s)//2] if len(s) % 2 != 0 else s[len(s)//2-1:len(s)//2+1]
# s = "kuka"
# print(get_middle(s))
# #2///
# def accum(s):
#     return "-".join([s[i].upper() + (s[i].lower() * i) for i in range(len(s))])
# s = str(input())
# print(accum())
# #3///
# import math
# def sqrt(n):
#     return False if n == -1 and math.sqrt(n)  else True
#4///
# def find_short(s):
#     return len(s) if len(l) > len(s) else len(l)

# l = "Kuka"
# s = "L;JSLK"
# print(find_short(s))

#5///
# def keep_order(ary, val):
#     return sorted(ary + [val]).index(val)

# ary = [1,2,3,4]
# val = 1
# print(keep_order(ary,val))
#6///

# def xo(s):
#     return (s.lower().count("x") == s.lower().count("o"))
# s = "OOXX"
# print(xo(s))

import math 
def heron(a, b, c):
    return (math.sqrt(s * ((s - a) * (s - b) * (s - c))))

s = int(input())
print(heron(3,4,5))