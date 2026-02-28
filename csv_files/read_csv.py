import csv

with open('example.csv', 'r', encoding='utf-8') as csv_file:
    print('=== file type:', type(csv_file))
    csv_data = csv.reader(csv_file)
    data_lines = list(csv_data)
    print(data_lines)

    for row in data_lines[: 5]:
        print(row)

    all_emails = [row[3] for row in data_lines[1 : 5]]
    print(all_emails)
    full_names = [f'{row[1]} {row[2]}' for row in data_lines[1 : 5]]
    print(full_names)
