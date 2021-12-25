from pprint import pprint
with open('input_day9','r') as file:
    data = file.read().split('\n')

testdata = ['2199943210',
'3987894921',
'9856789892',
'8767896789',
'9899965678'] 
    
# pprint(data)
# lowpoints = []
# for i, line in enumerate(data):
#     for k, val in enumerate(line):
#         adjacentsx = list(line)[k-1:k+2]
#         adjacentsy = [x[k] for x in data[i-1:i+2]]
#         if k == 0:
#             adjacentsx = list(line)[k:k+2]
#         if i == 0:
#             adjacentsy = [x[k] for x in data[i:i+2]]
#         print(adjacentsy)
#         if val == min(adjacentsx + adjacentsy) and len(list(filter(lambda x: x == min(adjacentsx + adjacentsy),adjacentsx + adjacentsy))) == 2:
#             lowpoints.append(int(val)+1)
# print(lowpoints)
# print(sum(lowpoints))

basins = {}
basincount = 0
tempset = dict()
for i, line in enumerate(data):
    for k, val in enumerate(line):
        if i == 0:
            if val != '9':
                coords = tuple([k,i])
                tempset[coords] = int(val)
            else:
                if tempset:
                    basins[basincount] = tempset
                    basincount += 1
                    tempset = {}
        if val != '9':
            coords = tuple([k,i])
            tempset[coords] = int(val)
        else:
            if tempset:
                for coord in tempset:
                    for basin in basins:
                        if tuple([coord[0],coord[1]-1]) in basins[basin]:
                            tempset = basins[basin] | tempset
                basins[basincount] = tempset
                basincount += 1
                tempset = {}                                       
    else:
        if tempset:
            for coord in tempset:
                for basin in basins:
                    if tuple([coord[0],coord[1]-1]) in basins[basin]:
                        tempset = basins[basin] | tempset
            basins[basincount] = tempset
            basincount += 1
            tempset = {}
    
basinsfiltered = []
for basin in basins.values():
    if len(list(filter(lambda x: set(basin.keys()).issubset(set(x.keys())), basins.values()))) == 1:
        basinsfiltered.append(basin)

basinwtf = []
for basin in basinsfiltered:
    basinwtf.append(len(basin))
print(sorted(basinwtf)[::-1][0:3])

# top3 = list(map(lambda x: len(x),basins.values())).sort(reverse=True)[0:3]

