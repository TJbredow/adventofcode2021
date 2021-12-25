from pprint import pprint
from statistics import median
with open('input_day10','r') as file:
    data = file.read().split('\n')
testdata = [
    '[({(<(())[]>[[{[]{<()<>>',
    '[(()[<>])]({[<{<<[]>>(',
    '{([(<{}[<>[]}>{[]{[(<()>',
    '(((({<>}<{<{<>}{[]{[]{}',
    '[[<[([]))<([[{}[[()]]]',
    '[{[{({}]{}}([{[{{{}}([]',
    '{<[[]]>}<{[{[{[]{()[[[]',
    '[<(<(<(<{}))><([]([]()',
    '<{([([[(<>()){}]>(<<{{',
    '<{([{{}}[<[[[<>{}]]]>[]]'
]

bracketlist = []
matchchars = {
    '{':'}',
    '[':']',
    '(':')',
    '<':'>'
}
# sums = {
#     ')':3,
#     ']':57, ######## for part one
#     '}':1197,
#     '>':25137
# }
completesums = {
    ')':1,
    ']':2,
    '}':3,
    '>':4
}
# part one, remove corrupted lines
corruptedlines = []
completedlines = []
for line in data:
    bracketlist = []
    for i, char in enumerate(line):
        if char in matchchars:
            bracketlist.insert(0,matchchars[char])
        else:
            if char == bracketlist[0]:
                bracketlist.pop(0)
            else:
                corruptedlines.append(line)
                break
    else:
        if bracketlist:
            completion = 0
            for charcomplete in bracketlist:
                completion = completion * 5
                completion += completesums[charcomplete]
            completedlines.append(completion)
    
            
# testdata = list(filter(lambda x: x not in corruptedlines,testdata))
print(median(completedlines))
# print(sum(map(lambda x: sums.get(x),corruptedlines)))

