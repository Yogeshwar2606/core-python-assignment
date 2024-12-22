def calculate_average_marks(students):
    average_marks = {}
    for student, marks in students.items():
        average_marks[student] = sum(marks) / len(marks)
    return average_marks
def find_top_performer(average_marks):
    top_student = max(average_marks, key=average_marks.get)
    return top_student
students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}
average_marks = calculate_average_marks(students)
top_performer = find_top_performer(average_marks)
print("Average Marks:", {student: round(avg, 2) for student, avg in average_marks.items()})
print("Top Performer:", top_performer)
