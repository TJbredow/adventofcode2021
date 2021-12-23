counter = 0
with open('input_day1','r') as file:
    values = file.readlines()

for i in range(0,len(values)):
    if values[i+1:]:
        if values[i] < values[i+1]:
            counter = counter + 1 
    else:
        if values[i] > values[i-1]:
            counter = counter + 1  
print(counter)