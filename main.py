def solve():
    print()


def print_state(state):
    for row in state:
        print(row)


if __name__ == '__main__':
    file = open("input.txt")
    starting_state = [0]*3
    counter = 0
    for line in file:
        # per each line, split into values we need
        splitLine = line.replace("\n", "").split(' ')  # should hold 3 values
        pos1, pos2, pos3 = splitLine
        temp = [pos1,pos2,pos3]
        # add to starting_state
        starting_state[counter] = (temp)
        counter += 1

    print_state(starting_state)



