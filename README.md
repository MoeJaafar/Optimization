# Transportation Problem Solver by Mohammad Jaafar

This Python script provides a solution to the transportation problem using three different methods: North-West Corner, Vogel's Approximation, and Russell's Approximation. It determines the initial basic feasible solution for a given transportation problem.

## Features

- Checks if the input transportation problem is applicable and balanced.
- Constructs and displays the input parameter table.
- Computes initial basic feasible solutions using three different methods.

## Functions

- `is_applicable(C, sources, destinations)`: Checks if all cost coefficients are strictly positive.
- `transportation_problem_is_balanced(S, D)`: Checks if the sum of supplies equals the sum of demands.
- `tabbed(s)`: Formats strings for tabulated display.
- `construct_input_table(S, D, C, sources, destinations)`: Constructs and displays the input parameters table.
- `print_supply_and_demand(a, b)`: Prints the supply and demand calculations.
- `delete_element_from_list(lst, x)`: Removes an element from a list.
- `delete_row_from_matrix(mat, n)`: Removes a row from a matrix.
- `delete_column_from_matrix(mat, m)`: Removes a column from a matrix.
- `run_north_west(supply, demand, C, sources, destinations)`: Solves the problem using the North-West Corner method.
- `run_vogel(supply, demand, C)`: Solves the problem using Vogel's Approximation method.
- `run_russel(supply, demand, C)`: Solves the problem using Russell's Approximation method.
- User input functions for vector and matrix data.

## How to Use

1. Run the script in a Python environment.
2. Input the number of sources and destinations when prompted.
3. Enter the supply vector, cost matrix, and demand vector as instructed.
4. The script will output the solutions using the three methods.

## Input Format

- A vector of coefficients of supply (`S`).
- A matrix of coefficients of costs (`C`).
- A vector of coefficients of demand (`D`).

## Output Format

1. Applicability and balance check results.
2. The input parameters table.
3. Initial basic feasible solutions using the three methods.

## Example

To use the script, follow the input prompts in the terminal. Here's an example of the input and part of the expected output:

```plaintext
Enter the vector of supply coefficients (space-separated, 3 elements): 7 9 18
Enter the matrix of cost coefficients (each row space-separated, 3 rows each with 4 elements):
19 30 50 10
70 30 40 60
40 8 70 20
Enter the vector of demand coefficients (space-separated, 4 elements): 5 8 7 14
```

After entering the data, the script will check for the applicability and balance of the transportation problem, construct and display the input table, and calculate the solutions using the three methods. The output will include the constructed table and the initial basic feasible solutions for each method.

## Requirements

- Python 3.x
- Basic understanding of the transportation problem in operations research.

## Contributing

Feel free to fork this repository and contribute by adding new features or improving the existing code. If you encounter any issues or have suggestions, please open an issue or submit a pull request.

---

