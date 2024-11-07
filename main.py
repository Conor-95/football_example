if __name__ == '__main__':
    matches = []
    line = ""
    f = open("matches.txt")
    print("reading file")
    for line in f:
        split_list = line.split(" ")    # split into 4 element list
        matches.append(split_list)
    print("R E S U L T S")
    for match in matches:
        home_team = match[0].strip()
        away_team = match[1].strip()
        home_score = match[2].strip()
        away_score = match[3].strip()
        print(home_team, " ", home_score, " : ", away_score, " ", away_team)
