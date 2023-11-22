# Helper functions and methods
def is_applicable(C, sources, destinations):
    for i in range(sources):
        for j in range(destinations):
            if C[i][j] <= 0:
                return False
    return True

def transportation_problem_is_balanced(S, D):
    return sum(S) == sum(D)

def tabbed(s):
    return s + ' ' * (10 - len(s))

def construct_input_table(S, D, C, sources, destinations):
    headers = ['D' + str(i+1) for i in range(destinations)] + ['Supply']
    print(tabbed(''), *map(tabbed, headers))
    for i in range(sources):
        row = ['S' + str(i+1)] + [C[i][j] for j in range(destinations)] + [S[i]]
        print(*map(tabbed, map(str, row)))
    demand_row = ['Demand'] + D
    print(*map(tabbed, map(str, demand_row)))

def print_supply_and_demand(a, b):
    min_val = min(a, b)
    print(f"Supply: {a} - {min_val} = {a - min_val}")
    print(f"Demand: {b} - {min_val} = {b - min_val}")

def delete_element_from_list(lst, x):
    return [lst[i] for i in range(len(lst)) if i != x]

def delete_row_from_matrix(mat, n):
    return [mat[i] for i in range(len(mat)) if i != n]

def delete_column_from_matrix(mat, m):
    return [[mat[i][j] for j in range(len(mat[0])) if j != m] for i in range(len(mat))]

def run_north_west(supply, demand, C, sources, destinations):
    north_west_x, north_west_y = 0, 0
    res = 0

    while north_west_x != sources - 1 or north_west_y != destinations - 1:
        print(f"Current north-west corner: ({north_west_x+1}, {north_west_y+1})")

        amount = min(supply[north_west_x], demand[north_west_y])
        print(f"We add {C[north_west_x][north_west_y]} * min({supply[north_west_x]}, {demand[north_west_y]})")
        res += C[north_west_x][north_west_y] * amount

        print_supply_and_demand(supply[north_west_x], demand[north_west_y])
        supply[north_west_x] -= amount
        demand[north_west_y] -= amount

        if supply[north_west_x] == 0:
            north_west_x += 1
        elif demand[north_west_y] == 0:
            north_west_y += 1

    # Final step
    print(f"Final north-west corner: ({north_west_x+1}, {north_west_y+1})")
    amount = min(supply[north_west_x], demand[north_west_y])
    print(f"We add {C[north_west_x][north_west_y]} * min({supply[north_west_x]}, {demand[north_west_y]})")
    res += C[north_west_x][north_west_y] * amount

    print(f"Initial basic feasible solution: {res}\n")

def run_vogel(supply, demand, C):
    res = 0

    while len(C) > 1 or len(C[0]) > 1:
        n = len(C)
        m = len(C[0])

        # Calculating penalties
        supply_penalty = [0 for _ in range(n)]
        demand_penalty = [0 for _ in range(m)]

        for i in range(n):
            sorted_row = sorted(C[i])
            supply_penalty[i] = sorted_row[1] - sorted_row[0] if len(sorted_row) > 1 else 0

        for j in range(m):
            sorted_column = sorted([C[i][j] for i in range(n)])
            demand_penalty[j] = sorted_column[1] - sorted_column[0] if len(sorted_column) > 1 else 0

        # Finding max penalty
        max_supply_penalty = max(supply_penalty)
        max_demand_penalty = max(demand_penalty)

        if max_supply_penalty >= max_demand_penalty:
            i = supply_penalty.index(max_supply_penalty)
            costs = [(C[i][j], j) for j in range(m)]
        else:
            j = demand_penalty.index(max_demand_penalty)
            costs = [(C[i][j], i) for i in range(n)]

        mini_cost, mini_index = min(costs)

        if max_supply_penalty >= max_demand_penalty:
            j = mini_index
        else:
            i = mini_index

        amount = min(supply[i], demand[j])
        print(f"We add {C[i][j]} * min({supply[i]}, {demand[j]})")
        res += C[i][j] * amount
        print_supply_and_demand(supply[i], demand[j])

        supply[i] -= amount
        demand[j] -= amount

        # Removing exhausted rows or columns
        if supply[i] == 0:
            C = delete_row_from_matrix(C, i)
            supply = delete_element_from_list(supply, i)
        elif demand[j] == 0:
            C = delete_column_from_matrix(C, j)
            demand = delete_element_from_list(demand, j)

    # Final addition
    print("Final addition:")
    print(f"We add {C[0][0]} * min({supply[0]}, {demand[0]})")
    res += C[0][0] * min(supply[0], demand[0])

    print(f"Initial basic feasible solution: {res}\n")


def run_russel(supply, demand, C):
    res = 0

    while len(C) > 1 or len(C[0]) > 1:
        n = len(C)
        m = len(C[0])

        U = [max(C[i]) for i in range(n)]  # Largest cost in supply (row)
        V = [max(C[i][j] for i in range(n)) for j in range(m)]  # Largest cost in demand (column)

        # Calculating delta values
        delta = [[C[i][j] - (U[i] + V[j]) for j in range(m)] for i in range(n)]

        # Finding the most negative delta
        min_delta = min(min(row) for row in delta)
        for i in range(n):
            for j in range(m):
                if delta[i][j] == min_delta:
                    min_i, min_j = i, j
                    break

        amount = min(supply[min_i], demand[min_j])
        print(f"We add {C[min_i][min_j]} * min({supply[min_i]}, {demand[min_j]})")
        res += C[min_i][min_j] * amount
        print_supply_and_demand(supply[min_i], demand[min_j])

        supply[min_i] -= amount
        demand[min_j] -= amount

        # Removing exhausted rows or columns
        if supply[min_i] == 0:
            C = delete_row_from_matrix(C, min_i)
            supply = delete_element_from_list(supply, min_i)
        elif demand[min_j] == 0:
            C = delete_column_from_matrix(C, min_j)
            demand = delete_element_from_list(demand, min_j)

    # Final addition
    print("Final addition:")
    print(f"We add {C[0][0]} * min({supply[0]}, {demand[0]})")
    res += C[0][0] * min(supply[0], demand[0])

    print(f"Initial basic feasible solution: {res}\n")


# Function to read a vector from user input
def read_vector(prompt, size):
    return [int(x) for x in input(f"{prompt} (space-separated, {size} elements): ").split()]

# Function to read a matrix from user input
def read_matrix(prompt, rows, cols):
    print(f"{prompt} (each row space-separated, {rows} rows each with {cols} elements):")
    return [[int(x) for x in input().split()] for _ in range(rows)]

# Main code
def main():
    sources = 3
    destinations = 4

    # Reading vectors and matrix from user input
    S = read_vector("Enter the vector of supply coefficients", sources)
    C = read_matrix("Enter the matrix of cost coefficients", sources, destinations)
    D = read_vector("Enter the vector of demand coefficients", destinations)

    # Checking applicability and balance
    if not is_applicable(C, sources, destinations):
        print("The method is not applicable!")
        return

    if not transportation_problem_is_balanced(S, D):
        print("The problem is not balanced!")
        return

    # Constructing and displaying input table
    construct_input_table(S, D, C, sources, destinations)

    # Solving using different methods and printing solutions
    print("\nNorth-West Corner Method Solution:")
    run_north_west(S.copy(), D.copy(), C, sources, destinations)
    
    print("\nVogel's Approximation Method Solution:")
    run_vogel(S.copy(), D.copy(), C.copy())
    
    print("\nRussel's Approximation Method Solution:")
    run_russel(S.copy(), D.copy(), C.copy())

# Run the main function
if __name__ == "__main__":
    main()
