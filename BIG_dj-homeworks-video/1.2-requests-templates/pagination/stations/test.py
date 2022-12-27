import csv

list_data = []
with open("data-398-2018-08-30.csv",  encoding='utf-8') as file:
    reader = csv.reader(file)
    line_count = 0
    for row in reader:
        dict_data = {}
        if line_count == 0:
            print(f'Имена столбцов {", ".join(row)}')
            line_count += 1
        dict_data['Name'] = row[1]
        dict_data['Street'] = row[4]
        dict_data['District'] = row[6]
        list_data.append(dict_data)

