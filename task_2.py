import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(filename, file1) -> None:
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)

        a = [row for row in reader]

    with open(file1, 'w') as file2:
        json.dump(a, file2, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
