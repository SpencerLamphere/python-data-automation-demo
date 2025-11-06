import csv

with open('data/sample.csv' , 'r') as file:
    reader = csv.DictReader(file)
    employees = [row for row in reader]

print("Employee records loaded:")
for e in employees:
    print(f"{e['Name']} - {e['Department']} - ${e['Salary']}")