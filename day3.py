import re

def solution():
    with open("day3.txt", "r") as source:
        data = []
        syms = []
        syms.append([])
        sum = 0
        sum_parts = set()
        
        for line in source:
            level = []
            sym_level = []
            for any in re.finditer("[0-9]+|[^\.]",line.strip("\n")):
                #print(any[0])
                if any[0].isnumeric():
                    level.append((int(any[0]),any.span()[0],any.span()[1]))
                else:
                    sym_level.append((any[0], any.span()[0]))
            data.append(level)
            syms.append(sym_level)
        #print(data)
        #print(syms)
        syms.append([])
       
        for i in range(0, len(data)):
            for j in range(0, len(data[i])):
                num = data[i][j]
                for k in range(0, len(syms[i+1])):
                    symbol = syms[i+1][k]
                    
                    if symbol[1] in range(num[1]-1,num[2]+1):
                        #print(num)
                        sum += num[0]

                for k in range(0, len(syms[i+2])):
                    symbol = syms[i+2][k]
                    
                    if symbol[1] in range(num[1]-1,num[2]+1):
                        #print(num)
                        sum += num[0]

                for k in range(0, len(syms[i])):
                    symbol = syms[i][k]
                    
                    if symbol[1] in range(num[1]-1,num[2]+1):
                        #print(num)
                        sum += num[0]
        print(sum)


if __name__ == "__main__":
    solution()
