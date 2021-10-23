import csv

input_path = "C:/Users/Mansour/Desktop/python-challenge/tank_data.csv"


output_path = "C:/Users/Mansour/Desktop/python-challenge/PyBank_results.txt"

thermal_rows = []
input_rows = []


with open(input_path) as csv_file:
    read_file = csv.reader(csv_file , delimiter = ",")
    header_file = next(read_file)
    for row in read_file:
        input_rows.append(row[0])
        thermal_rows.append(int(row[1]))
