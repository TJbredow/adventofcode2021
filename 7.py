from statistics import fmean
from math import floor, ceil
def triangle_sum(foo):
    val = 0
    for i in range(foo+1):
        val += i
    return val
with open('input_day7','r') as file:
    data = [int(x) for x in file.read().split(',')]
# print(data)

dfloor = floor(fmean(data))
dceil = ceil(fmean(data))

print(f"(floor - 1) {dfloor - 1} : {sum(map(lambda x: triangle_sum(abs(dfloor - 1 - x )), data))}")
print(f"floor {dfloor} : {sum(map(lambda x: triangle_sum(abs(dfloor-x)), data))}")
print(f"ceiling {dceil} : {sum(map(lambda x: triangle_sum(abs(dceil-x)), data))}")  
print(print(f"(ceiling + 1) {dceil+1} : {sum(map(lambda x: triangle_sum(abs(dceil + 1 - x)), data))}")) 