import csv

def saveGradeToCsv(fileName, records):
    with open(fileName, 'w', newline='') as csvFile:
        fieldNames = ['firstname', 'lastname', 'exam1grade', 'exam2grade', 'exam3grade']
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
        
        writer.writeheader()
        for record in records:
            writer.writerow(record)

def main():
    records = []

    print("Enter student information and exam grades. Type 'done' for first name to exit.")

    while True:
        firstName = input("First Name: ")
        if firstName.lower() == 'done':
            break

        lastName = input("Last Name: ")
        exam1Grade = int(input("Exam 1 Grade: "))
        exam2Grade = int(input("Exam 2 Grade: "))
        exam3Grade = int(input("Exam 3 Grade: "))

        record = {
            'firstname': firstName,
            'lastname': lastName,
            'exam1grade': exam1Grade,
            'exam2grade': exam2Grade,
            'exam3grade': exam3Grade
        }

        records.append(record)

    fileName = 'grades.csv'
    saveGradeToCsv(fileName, records)
    print(f"Grades saved to {fileName}.")

if __name__ == "__main__":
    main()
