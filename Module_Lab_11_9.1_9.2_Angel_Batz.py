def storeGrades(fileName, grades):
    with open(fileName, 'w') as file:
        for grade in grades:
            file.write(str(grade) + '\n')

def main():
    grades = []

    print("Enter grades (type 'done' when finished):")
    while True:
        inputedGrades = input("Grade: ")
        if inputedGrades.lower() == 'done':
            break
        try:
            grade = float(inputedGrades)
            grades.append(grade)
        except ValueError:
            print("Invalid input. Please enter a valid grade or 'done' to finish.")

    fileName = 'grades.txt'
    storeGrades(fileName, grades)
    print(f"Grades saved to {fileName}.")
    calculateStats(grades)

def calculateStats(grades):
    total = sum(grades)
    count = len(grades)
    average = total / count if count > 0 else 0

    print('Each Grades:')
    for i, grade in enumerate(grades, start=1):
        print(f'Grade {i}: {grade}')
        
    print(f'\nTotal: {total}')
    print(f'Count: {count}')
    print(f'Average: {average:.2f}')

if __name__ == "__main__":
    main()

