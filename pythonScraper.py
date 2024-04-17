import csv
import subprocess

def execute_command(command):
    """Execute a given command in the shell."""
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Executed: {command}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


def run_pick(csv_file_path):
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            id_value = row['id']

            if id_value == '':
                break

            id_value = int(id_value)
            pick_command = f"leetgo pick {id_value}"
            execute_command(pick_command)

def main():
    csv_file_path = 'answers_python2024.csv'
    # python_file_path = 'python/your_python_file.py'

    run_pick(csv_file_path)


if __name__ == "__main__":
    main()
