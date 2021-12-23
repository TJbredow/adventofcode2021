from pprint import pprint
with open('input_day8','r') as file:
    fileflow = tuple(file.read().split('\n'))

digits = [x.split('|')[1].strip(' ').split(' ') for x in fileflow]
cipherdigits = [x.split('|')[0].strip(' ').split(' ') for x in fileflow]
# print(cipherdigits)
total = 0
cipher= {}
values = []
# print(cipherdigits)
for k, line in enumerate(cipherdigits):

    for i, digit in enumerate(line):
        print(line)
        if len(digit) == 2:
            cipher['1'] = digit
        if len(digit) == 3:
            cipher['7'] = digit
        if len(digit) == 4:
            cipher['4'] = digit
        if len(digit) == 7:
            cipher['8'] = digit
    pointa = str(filter(lambda x: x not in cipher['1'],cipher['7']))
    for i, digit in enumerate(line):
        if len(digit) == 6:
            if len(list(filter(lambda x: x not in digit,cipher['4']))) == 0:
                cipher['9'] = digit
            elif all(map(lambda x: x in digit, cipher['7'])):
                cipher['0'] = digit
            else:
                cipher['6'] = digit
        if len(digit) == 5:
            if all(map(lambda x: x in digit, cipher['7'])):
                cipher['3'] = digit
            elif len(list(filter(lambda x: x not in digit, cipher['4']))) == 1:
                cipher['5'] = digit
            else:
                cipher['2'] = digit
            
            
    # print(cipher)

    def findnumber(number):
        for key, value in cipher.items():
            if set(number) == set(value):
                return key
        else:
            return 'w'
        
    fourdigit = ''
    for digit in digits[k]:
        print(digit)
        fourdigit += findnumber(digit)

    values.append(int(fourdigit))
print(values)
print(sum(values))

        
    
            
            
            
            
        
                
        
        


    