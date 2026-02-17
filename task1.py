import os

def total_salary(path):
    with open(path, 'r') as file:
        count = 0
        total_salary = 0

        while True:
            line = file.readline().strip()
            if not line:
                break
            total_salary = total_salary + float(line[line.index(',') + 1::])
            count = count + 1
        if (count != 0):
            result = (total_salary, total_salary/count)
            return result
        else:
            print("Number of developers is 0")
            return (0, 0)

path = 'salaries.txt'

if os.path.exists(path):
    total, average = total_salary(path)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
else:
    print('File not found or corrupt')