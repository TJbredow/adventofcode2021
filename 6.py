# testdata = [3,4,3,1,2]
with open('input_day6','r') as file:
    testdata = list(map(lambda x: int(x),file.read().split(',')))

# initial values
fishcycle = [0,0,0,0,0,0,0]
newbuffer2 = 0
newbuffer1 = 0
temp = 0
for item in testdata:
    fishcycle[item] += 1
    
for day in range(256):
    print(day)
    temp = newbuffer2 * 1
    newbuffer2 = fishcycle[day % 7]
    fishcycle[day % 7] += newbuffer1
    newbuffer1 = temp

    # print(testdata)
    # for i, fish in enumerate(testdata):
    #     if fish == 0:
    #         testdata[i] = 7
    #         testdata.append(9)

print(sum(fishcycle)+newbuffer2+newbuffer1)