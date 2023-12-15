import re

def solution():
    with open("day3.txt", "r") as source:
        data = []
        syms = []
        syms.append([])
        sum = 0
        
        for line in source:
            level = []
            sym_level = []
            for char in re.finditer("[0-9]+|[^\.]",line.strip("\n")):                
                if char[0].isnumeric():
                    level.append((int(char[0]),char.span()[0],char.span()[1]))
                else:
                    sym_level.append((char[0], char.span()[0]))
            data.append(level)
            syms.append(sym_level)

        syms.append([])
       
        for i in range(0, len(data)):
            for j in range(0, len(data[i])):
                num = data[i][j]                
                
                for k in range(0, len(max(syms, key=len))):

                    get_symbol = lambda syms, i, k: syms[i][k] if len(syms[i]) >= k+1 else (0, -10)

                    symbols = [get_symbol(syms, i+x, k)[1] for x in range(3)]

                    if any(num[1]-1 <= sym <= num[2] for sym in symbols):                    
                        sum += num[0]
        print(sum)


if __name__ == "__main__":
    solution()
