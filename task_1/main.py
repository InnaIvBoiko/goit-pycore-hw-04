# Function to calculate total and average salary from a file
def total_salary(path: str) -> tuple:
    try:
        total = 0
        count = 0
        
        # Use context manager with encoding specification
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()  # Remove whitespace and newlines
                
                if not line:  # Skip empty lines
                    continue
                
                try:
                    # Split by comma and extract salary
                    parts = line.split(',')
                    
                    # Ensure there are exactly two parts (name and salary)
                    if len(parts) != 2: 
                        raise ValueError(f"Invalid salary line format: {line}") 

                    salary = parts[1]
                    total += float(salary)
                    count += 1
                    
                except ValueError as e:
                    print(f"Warning: Skipping invalid salary line '{line}': {e}")
                    continue # Skip lines with invalid salary data
        
        if count == 0:
            print("Warning: No valid salary data found in the file")
            return 0, 0 # Avoid division by zero

        average = total / count
        return total, average
        
    except FileNotFoundError:
        print(f"Error: File '{path}' not found")
        return 0, 0 # Handle file not found errors
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{path}'")
        return 0, 0 # Handle permission errors
    except Exception as e:
        print(f"Error reading file '{path}': {e}")
        return 0, 0 # General exception handling for unexpected errors 

# Example usage:

total, average = total_salary("path/to/salary_file.txt")
print(f"Total salary amount: {total:.2f}, Average salary: {average:.2f}")

total, average = total_salary("path/to/salary_file_1.txt") # Example with invalid data
print(f"Total salary amount: {total:.2f}, Average salary: {average:.2f}") # Error: File 'path/to/salary_file_1.txt' not found