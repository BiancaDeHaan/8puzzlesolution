import copy


def solve(state):

    # Stores potential moves
    # Stores g(n), h(n), state
    fringe = [[0, calc_number_of_displaced_tiles(state), state]]
    closed_list = []
    explored_state_node = [0, calc_number_of_displaced_tiles(state), state]
    while True:
        if check_if_goal_state(explored_state_node[2]):
            return explored_state_node[0] + explored_state_node[1]

        # explore the lowest cost on the fringe
        # remove from fringe, add to closed list

        explored_state_node = find_lowest_cost_in_fringe(fringe)
        fringe.remove(explored_state_node)
        closed_list.append(explored_state_node[2])

        explored_state = explored_state_node[2]
        explored_cost = explored_state_node[0]
        explored_heuristic = explored_state_node[1]
        i, j = find_blank_space(explored_state)

        # Try 4 moves, up, left, down, right and compare their g(n) + h(n)
        # Add onto the fringe, and take the least costly move
        # Move up check
        if i != 0:
            temp_state = state_swap(explored_state, i-1, j)
            g_n = temp_state[i][j] + explored_cost  # cost
            h_n = calc_number_of_displaced_tiles(temp_state)  # heuristic
            temp_node = [g_n, h_n, temp_state]

            if temp_state not in closed_list:
                fringe.append([g_n, h_n, temp_state])
        # Move down check
        if i != 2:
            temp_state = state_swap(explored_state, i + 1, j)
            g_n = temp_state[i][j] + explored_cost  # cost
            h_n = calc_number_of_displaced_tiles(temp_state)  # heuristic
            temp_node = [g_n, h_n, temp_state]
            if temp_state not in closed_list:
                fringe.append([g_n, h_n, temp_state])
        # Move left check
        if j != 0:
            temp_state = state_swap(explored_state, i, j - 1)
            g_n = temp_state[i][j] + explored_cost  # cost
            h_n = calc_number_of_displaced_tiles(temp_state)  # heuristic
            temp_node = [g_n, h_n, temp_state]
            if temp_state not in closed_list:
                fringe.append([g_n, h_n, temp_state])
        # Move right check
        if j != 2:
            temp_state = state_swap(explored_state, i, j + 1)
            g_n = temp_state   [i][j] + explored_cost  # cost
            h_n = calc_number_of_displaced_tiles(temp_state)  # heuristic
            temp_node = [g_n, h_n, temp_state]
            if temp_state not in closed_list:
                fringe.append([g_n, h_n, temp_state])



def find_lowest_cost_in_fringe(fringe):
    min_cost = 99999999
    lowest_cost_node = None
    for node in fringe:
        cost = node[0] + node[1]
        if cost < min_cost:
            lowest_cost_node = node
            min_cost = cost
    return lowest_cost_node


def state_swap(state, x, y):
    x_0, y_0 = find_blank_space(state)
    value = state[x][y]
    temp_state = copy.deepcopy(state)
    temp_state[x_0][y_0] = value
    temp_state[x][y] = 0
    return temp_state


def print_state(state):
    for row in state:
        print(row)


def check_if_goal_state(state):
    if calc_number_of_displaced_tiles(state) == 0:
        return True
    else:
        return False


# This function returns the number of displaced tiles compared to the goal state
def calc_number_of_displaced_tiles(state):
    global goal_state
    count_of_displaced_tiles = 0
    for i in range (0, 3):
        for j in range(0, 3):
            if goal_state[i][j] != state[i][j]:
                count_of_displaced_tiles += 1
    return count_of_displaced_tiles


def find_blank_space(state):
    for i in range(0, 3):
        for j in range(0, 3):
            if state[i][j] == 0:
                return [i, j]


if __name__ == '__main__':
    file = open("input.txt")
    starting_state = [0]*3
    goal_state = [0]*3

    # Initializing the goal state ( per instructions )
    goal_state[0] = [1, 2, 3]
    goal_state[1] = [8, 0, 4]
    goal_state[2] = [7, 6, 5]

    # Initializing the start state from a file formatted as
    # x x x
    # x x x
    # x x x
    counter = 0
    for line in file:
        # per each line, split into values we need
        splitLine = line.replace("\n", "").split(' ')  # should hold 3 values
        pos1, pos2, pos3 = splitLine
        temp = [int(pos1), int(pos2), int(pos3)]
        # add to starting_state
        starting_state[counter] = temp
        counter += 1

    # Call the solve function, handles solving the problem
    cost_of_solution = solve(starting_state)
    print("The shortest path is: " , cost_of_solution)


