from pprint import pprint
with open('input_day9','r') as file:
    data = file.read().split('\n')

testdata = ['2199943210',
'3987894921',
'9856789892',
'8767896789',
'9899965678'] 
    
pprint(data)
lowpoints = []
for i, line in enumerate(data):
    for k, val in enumerate(line):
        adjacentsx = list(line)[k-1:k+2]
        adjacentsy = [x[k] for x in data[i-1:i+2]]
        if k == 0:
            adjacentsx = list(line)[k:k+2]
        if i == 0:
            adjacentsy = [x[k] for x in data[i:i+2]]
        print(adjacentsy)
        if val == min(adjacentsx + adjacentsy) and len(list(filter(lambda x: x == min(adjacentsx + adjacentsy),adjacentsx + adjacentsy))) == 2:
            lowpoints.append(int(val)+1)
print(lowpoints)
print(sum(lowpoints))