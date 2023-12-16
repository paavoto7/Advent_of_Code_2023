

def main():
    points = 0
    with open("day4.txt", "r") as f:
        for line in f:
            key = line[0:6]
            part_points = 0.5

            parts = line.replace(":", "||").strip("\n").split("|")

            win = set(parts[2].split(" "))
            if "" in win: win.remove("")
            
            for num in parts[3].split(" "):
                if num in win:
                    part_points *= 2
            
            if part_points > 0.5:
                points += int(part_points)

    print(points)        
    

if __name__ == "__main__":
    main()