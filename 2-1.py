x = 0 
y = 0

with open('input_day2','r') as file:
    lines = file.readlines()
for line in lines:
    l = line.strip('\n').split(' ')
    if l[0] == "forward":
        x = x + int(l[1])
    elif l[0] == "down":
        y = y + int(l[1])
    elif l[0] == "up":
        y = y - int(l[1])

print(x * y)
