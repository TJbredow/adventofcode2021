count = 0
with open('input_day1','r') as file:
    valuespre = file.readlines()
values = [int(x.strip('\n')) for x in valuespre]
for i in range(0,len(values)):
    if len(values[i:i+3]) == 3:
        if sum(values[i:i+3]) < sum(values[i+1:i+4]):
            count = count + 1

print(count)
    
