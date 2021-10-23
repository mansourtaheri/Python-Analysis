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


number_of_month = len(input_rows)

sum_of_temps = sum(thermal_rows)

average_change = round((thermal_rows[-1]-thermal_rows[0])/(number_of_month-1),2)

fifferent_temps = [j - i for i, j in zip(thermal_rows[: -1], thermal_rows[1 :])] 

greatest_increase = max(fifferent_temps)
ind_increase = fifferent_temps.index(greatest_increase)+1
date_increase = input_rows[ind_increase]

greatest_decrease= min(fifferent_temps)
ind_decrease = fifferent_temps.index(greatest_decrease)+ 1
date_decrease = input_rows[ind_decrease]


with open(output_path,'w') as output:
   output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format("Thermal Analysis","----------------------------",f"Total Months: {number_of_month}",
   f"Total: ${sum_of_temps}",f"Average  Change: ${average_change}",f"Greatest Increase in thermal: {date_increase} (${greatest_increase})",
   f"Greatest Decrease in thermal: {date_decrease} (${greatest_decrease})","----------------------------"))
 
    
    
    
