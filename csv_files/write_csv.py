import csv

with open('to_save_file.csv', 'w', encoding='utf-8', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(['num 1', 'num 2', 'num 3'])
    csv_writer.writerows([['1', '2', '3'], ['4', '5', '6']])


# Appending to the same file
with open('to_save_file.csv', 'a', encoding='utf-8', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(['7', '8', '9'])
    csv_writer.writerows([['10', '11', '12'], ['13', '14', '15']])
