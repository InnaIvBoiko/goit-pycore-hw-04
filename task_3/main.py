import sys
from pathlib import Path
from colorama import Fore, Style, init

# Initialize colorama for cross-platform colored output
init(autoreset=True)

def display_directory_structure(directory_path, indent_level=0):
    try:
        # Create indentation string
        indent = "    " * indent_level
        
        # Get all items in the directory and sort them
        items = sorted(directory_path.iterdir())
        
        for item in items:
            if item.is_dir():
                # Display directory in blue color
                print(f"{indent}{Fore.BLUE}{item.name}/{Style.RESET_ALL}")
                # Recursively display subdirectory contents
                display_directory_structure(item, indent_level + 1)
            else:
                # Display file in green color
                print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")
                
    except PermissionError:
        print(f"{indent}{Fore.RED}[Permission Denied]{Style.RESET_ALL}")
    except Exception as e:
        print(f"{indent}{Fore.RED}[Error: {str(e)}]{Style.RESET_ALL}")

def main():
    """
    Main function to handle command line arguments and display directory structure.
    """
    # Check if directory path is provided as command line argument
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Usage: python {sys.argv[0]} <directory_path>{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Example: python {sys.argv[0]} /path/to/your/directory{Style.RESET_ALL}")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    
    # Convert to Path object
    path = Path(directory_path)
    
    # Check if path exists
    if not path.exists():
        print(f"{Fore.RED}Error: The path '{directory_path}' does not exist.{Style.RESET_ALL}")
        sys.exit(1)
    
    # Check if path is a directory
    if not path.is_dir():
        print(f"{Fore.RED}Error: The path '{directory_path}' is not a directory.{Style.RESET_ALL}")
        sys.exit(1)
    
    # Display the root directory name
    print(f"{Fore.BLUE}{path.name}/{Style.RESET_ALL}")
    
    # Display the directory structure
    display_directory_structure(path, 1)

if __name__ == "__main__":
    main()

# Example usage:
# Display structure of the picture directory
# /Users/inna/Documents/GitHub/goit-pycore-hw-04/.venv/bin/python task_3/main.py task_3/picture