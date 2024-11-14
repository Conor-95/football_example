#! /usr/bin/python3

if __name__ == '__main__':
    matches = []
    line = ""
    try:
        f = open("matches.txt")
    except FileNotFoundError:
        print("File not found")
        exit(-1)
    print("reading file")
    for line in f:
        split_list = line.split(" ")    # split into 4 element list
        if len(split_list) != 4:
            print("error within match data :", line, end="")
            continue
        try:
            split_list[2] = int(split_list[2])
            split_list[3] = int(split_list[3])
        except ValueError:
            print("invalid score :", line, end="")
            continue

        matches.append(split_list)
    print("R E S U L T S")
    for match in matches:
        home_team = match[0].strip()
        away_team = match[1].strip()
        home_score = match[2]
        away_score = match[3]
        print(home_team, " ", home_score, " : ", away_score, " ", away_team)
