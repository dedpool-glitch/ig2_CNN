import csv

lst_filepath = 'label.lst'
csv_filepath = 'labels.csv' 

with open(lst_filepath, 'r') as lst_file:
    lines = lst_file.readlines()

with open(csv_filepath, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    for line in lines:
        row = line.strip().split(' ')
        writer.writerow(row)

print(f"Conversion complete! CSV saved as: {csv_file}")
