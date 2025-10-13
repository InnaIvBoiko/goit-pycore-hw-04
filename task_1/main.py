# Function to calculate total and average salary from a file
def total_salary(path: str) -> tuple:
    # Read the file with salary data
    with open(path, 'r') as file:
        lines = file.readlines()
    total = sum(int(line.split(',')[1]) for line in lines) # Calculate total salary
    average = int(total / len(lines) if lines else 0) # Calculate average salary

    return total, average

# Example usage:

total, average = total_salary("path/to/salary_file.txt")
print(f"Total salary amount: {total}, Average salary: {average}")