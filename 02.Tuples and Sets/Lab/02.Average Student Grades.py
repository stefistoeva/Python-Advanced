def students(list_of_students):
    student_grades = {}

    for student in list_of_students:
        (student_name, student_grade) = student.split(" ")
        if student_name not in student_grades:
            student_grades[student_name] = []
        student_grades[student_name].append(float(student_grade))

    return student_grades


def print_result(all_grades):
    for (student, grades) in all_grades.items():
        average = sum(grades) / len(grades)
        print(f"{student} -> {' '.join([f'{grade:.2f}' for grade in grades])} (avg: {average:.2f})")


count_of_student = [input() for _ in range(int(input()))]
print_result(students(count_of_student))
