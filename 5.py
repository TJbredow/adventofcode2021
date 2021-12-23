from pprint import pprint
with open('input_day5','r') as file:
    data = file.read().split('\n')

cleaner = list(map(lambda x: x.split(' -> '), data))
    
class coordinate:
    def __init__(self, line):
        self.start = [int(x) for x in line[0].split(',')]
        self.end = [int(x) for x in line[1].split(',')]
    def coordlist(self):
        xvector = self.end[0] - self.start[0]
        yvector = self.end[1] - self.start[1]
        coordlist = []  
        if any([xvector == 0, yvector == 0]):
            if xvector:
                for i in range(self.start[0], self.end[0], round(xvector/abs(xvector))):
                    coordlist.append([i,self.start[1]])
            else:
                for i in range(self.start[1], self.end[1], round(yvector/abs(yvector))):
                    coordlist.append([self.start[0],i])
            if [self.end[0],self.end[1]] not in coordlist:
                coordlist.append([self.end[0],self.end[1]])
            else:
                coordlist.append([self.start[0],self.start[1]])
        elif abs(xvector) == abs(yvector):
            ys = [y for y in range(self.start[1],self.end[1],round(yvector/abs(yvector)))]
            xs = [x for x in range(self.start[0],self.end[0],round(xvector/abs(xvector)))]
            for x, y in zip(xs, ys):
                coordlist.append([x,y])
                
            if [self.end[0],self.end[1]] not in coordlist:
                coordlist.append([self.end[0],self.end[1]])
            else:
                coordlist.append([self.start[0],self.start[1]])                                         
        return coordlist                         
                    
                 
coordinate_plane = [[0 for x in range(0,1000)] for x in range(0,1000)]
# print(coordinate_plane)       
        
for line in cleaner:
    for coord in coordinate(line).coordlist():
        # print(coord[1])
        coordinate_plane[coord[1]][coord[0]] = coordinate_plane[coord[1]][coord[0]] + 1
# for line in coordinate_plane:
#     print(line)

total = 0
for i, y in enumerate(coordinate_plane):
    for k, x in enumerate(y):
        if x > 1:
            print(f"{i},{k}")
            total += 1
            print(total)
    


