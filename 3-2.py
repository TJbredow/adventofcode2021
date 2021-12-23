

from copy import deepcopy
# with open('input_day3.txt','r') as file:
#     data = file.read().split('\n')
data = ['00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010'
    ]

datao2 = deepcopy(data)
for i in range(0,len(data[0])):
    ones = sum([int(x[i]) for x in datao2])
    print(datao2)
    if len(datao2) == 1:
        break
    if ones <= (len(datao2)/2):
        datao2 = list(filter(lambda x: x[i] == '1',datao2))
    else:
        datao2 = list(filter(lambda x: x[i] == '0',datao2))
       
o2 = int(datao2[0],2)            
print(o2)
for i in range(0,len(data[0])):
    ones = sum([int(x[i]) for x in datao2])
    print(data)
    if len(data) == 1:
        break
    if ones >= (len(data)/2):
        data = list(filter(lambda x: x[i] == '0',data))
    else:
        data = list(filter(lambda x: x[i] == '1',data)) 
co2 = int(data[0],2) 
print(co2) 
print(co2*o2)