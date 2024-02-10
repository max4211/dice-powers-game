from prettytable import PrettyTable # might need to install this
import numpy as np
import sys

def print_matrix_as_table(matrix):
    table = PrettyTable()

    # Add column headers
    table.field_names = [''] + [f'{i+1}' for i in range(len(matrix[0]))]

    # Add rows with row headers
    for i, row in enumerate(matrix):
        table.add_row([f'{i+1}'] + row)

    print(table.get_string(markdown=True))

def create_matrix(rows=6, cols=6):
    matrix = [[pow(i+1,j+1) for j in range(rows)] for i in range(cols)]
    return matrix

def calculate_mean_and_std(data, round=3):
    mean_value = float(np.mean(data))
    std_deviation = float(np.std(data))

    return np.round(mean_value, round), np.round(std_deviation, round)

def summarize_results(matrix):
    flat_list = [item for sublist in matrix for item in sublist]
    mean, std_dev = calculate_mean_and_std(flat_list)
    n, m = len(matrix), len(matrix[0])
    print(f"{n} by {m} matrix results:")
    print(f"Mean:\t{mean}\nStdev:\t{std_dev}")
    print_matrix_as_table(matrix)


def run(rows, cols):
    # Create the matrix and compute results
    matrix = create_matrix(rows, cols)

    # Summarize results
    summarize_results(matrix)

def main():
    # Check if exactly two command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python run.py <rows> <columns>")
        sys.exit(1)

    try:
        # Convert command-line arguments to integers
        rows = int(sys.argv[1])
        columns = int(sys.argv[2])

        # Call the main function with the provided arguments
        run(rows, columns)
    except ValueError:
        print("Error: Rows and columns must be integers.")
        sys.exit(1)

# CR masmith: accept arguments
if __name__ == "__main__":
    main()

