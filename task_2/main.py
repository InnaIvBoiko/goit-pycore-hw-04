# Function to read cat information from a file and return it as a list of dictionaries
def get_cats_info(path: str) -> list[dict[str, str]]:
    cats_list = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()  # Remove whitespace and newlines
                
                if not line:  # Skip empty lines
                    continue
                
                try:
                    # Split by comma and extract cat id, name and age
                    parts = line.split(',')

                    # Ensure there are exactly three parts (id, name, age)
                    if len(parts) != 3: 
                        raise ValueError(f"Invalid cat line format: {line}") 

                    # Create dictionary with the cat information
                    cat_info = {"id": parts[0].strip(), "name": parts[1].strip(), "age": parts[2].strip()}
                    cats_list.append(cat_info)

                except ValueError as e:
                    print(f"Warning: Skipping invalid cat line '{line}': {e}")
                    continue # Skip lines with invalid cat data
        
        if not cats_list:
            print("Warning: No valid cat data found in the file")

        return cats_list

    except FileNotFoundError:
        print(f"Error: File '{path}' not found")
        return []
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{path}'")
        return []
    except Exception as e:
        print(f"Error reading file '{path}': {e}")
        return []

# Example usage:

cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)

cats_info_error = get_cats_info("path/to/cats_file_1.txt") # Example with invalid data
print(cats_info_error) # Error: File 'path/to/cats_file_1.txt' not found
