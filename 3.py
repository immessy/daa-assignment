import csv

with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    for row_index, row in enumerate(reader, start=1):
        for col_index, cell in enumerate(row, start=1):
            if 'ai' in cell.lower():
                print(f"Match at Row {row_index} Column {col_index}: {cell}")

