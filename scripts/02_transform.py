import csv, json

with open('data/sample.csv', 'r') as infile:
    reader = csv.DictReader(infile)
    employees = list(reader)

for emp in employees:
    
    emp['Salary'] = int(emp['Salary'])
    
    emp['NewSalary'] = round(emp['Salary'] * 1.05, 2)


with open('data/updated_employees.json', 'w') as outfile:
    json.dump(employees, outfile, indent=2)

print("✅ Updated file saved as data/updated_employees.json")
