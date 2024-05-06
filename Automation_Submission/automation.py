import csv
import subprocess

def execute_command(command):
    """Execute a given command in the shell."""
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Executed: {command}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def write_answer_to_file(answer, file_path):
    """
    Write the answer to the specified Python file between the markers.
    '# @lc code=begin' and '# @lc code=end'.

    Args:
    answer (str): The answer text to insert.
    file_path (str): Path to the Python file.
    """
    # Read the existing content of the file
    with open(file_path, 'r') as file:
        content = file.readlines()

    # Initialize indices for the start and end markers
    begin_index = end_index = None

    # Locate the markers in the file
    for i, line in enumerate(content):
        if '# @lc code=begin' in line:
            begin_index = i + 1  # Insert after this line
        elif '# @lc code=end' in line:
            end_index = i  # Insert before this line
            break

    if begin_index is not None and end_index is not None and begin_index < end_index:
        # Replace existing content between the markers
        content = content[:begin_index] + [answer + '\n'] + content[end_index:]

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.writelines(content)
    else:
        print("Error: The markers were not found or are incorrectly placed in the file.")


def get_python_file_path(id, slug):
    id = int(id)
    new_id = f"{id:04d}"
    return "python/" + new_id + "." + slug + "/solution.py"

def process_csv_row(csv_file_path):
    """Process each row in the given CSV file."""
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            id_value = row['id']
            answer = row['Answer']
            slug = row['slug']
            
            if id_value == '':
                break

            # Execute the leetgo pick command
            pick_command = f"leetgo pick {id_value}"
            execute_command(pick_command)

            python_file_path = get_python_file_path(id_value, slug)
            # Write the answer to the Python file
            write_answer_to_file(answer, python_file_path)

            # Execute the test and submit commands
            # execute_command("leetgo test last -L")
            # execute_command("leetgo submit last")




def main():
    csv_file_path = 'first20.csv'
    # python_file_path = 'python/your_python_file.py'

    process_csv_row(csv_file_path)

if __name__ == "__main__":
    main()

