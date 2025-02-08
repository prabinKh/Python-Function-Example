'''
1. Add students to the system.

2. Add courses to the system.

3. Enroll students in courses.

4. Record grades for students in courses.

5. Calculate the average grade for a student.

6. Calculate the average grade for a course.

7. View all students and their grades.

8. View all courses and their enrolled students.

'''



# Global variables to store student and course data
students = {}  # Dictionary to store students and their grades
courses = {}  # Dictionary to store courses and their enrolled students

# Function to add a student
def add_student(student_id, name):
    if student_id in students:
        print(f"Student with ID {student_id} already exists.")
    else:
        students[student_id] = {
            "name": name,
            "courses": {}  # Dictionary to store courses and grades
        }
        print(f"Student {name} with ID {student_id} added to the system.")

# Function to add a course
def add_course(course_id, course_name):
    if course_id in courses:
        print(f"Course with ID {course_id} already exists.")
    else:
        courses[course_id] = {
            "name": course_name,
            "students": []  # List to store enrolled students
        }
        print(f"Course {course_name} with ID {course_id} added to the system.")

# Function to enroll a student in a course
def enroll_student(student_id, course_id):
    if student_id not in students:
        print(f"Student with ID {student_id} does not exist.")
        return
    if course_id not in courses:
        print(f"Course with ID {course_id} does not exist.")
        return
    if student_id in courses[course_id]["students"]:
        print(f"Student {students[student_id]['name']} is already enrolled in course {courses[course_id]['name']}.")
        return
    courses[course_id]["students"].append(student_id)
    students[student_id]["courses"][course_id] = None  # Initialize grade as None
    print(f"Student {students[student_id]['name']} enrolled in course {courses[course_id]['name']}.")

# Function to record a grade for a student in a course
def record_grade(student_id, course_id, grade):
    if student_id not in students:
        print(f"Student with ID {student_id} does not exist.")
        return
    if course_id not in courses:
        print(f"Course with ID {course_id} does not exist.")
        return
    if course_id not in students[student_id]["courses"]:
        print(f"Student {students[student_id]['name']} is not enrolled in course {courses[course_id]['name']}.")
        return
    students[student_id]["courses"][course_id] = grade
    print(f"Grade {grade} recorded for student {students[student_id]['name']} in course {courses[course_id]['name']}.")

# Function to calculate the average grade for a student
def calculate_student_average(student_id):
    if student_id not in students:
        print(f"Student with ID {student_id} does not exist.")
        return
    grades = [grade for grade in students[student_id]["courses"].values() if grade is not None]
    if not grades:
        print(f"Student {students[student_id]['name']} has no recorded grades.")
        return
    average = sum(grades) / len(grades)
    print(f"Average grade for student {students[student_id]['name']}: {average:.2f}")

# Function to calculate the average grade for a course
def calculate_course_average(course_id):
    if course_id not in courses:
        print(f"Course with ID {course_id} does not exist.")
        return
    grades = []
    for student_id in courses[course_id]["students"]:
        grade = students[student_id]["courses"][course_id]
        if grade is not None:
            grades.append(grade)
    if not grades:
        print(f"Course {courses[course_id]['name']} has no recorded grades.")
        return
    average = sum(grades) / len(grades)
    print(f"Average grade for course {courses[course_id]['name']}: {average:.2f}")

# Function to view all students and their grades
def view_all_students():
    if not students:
        print("No students in the system.")
    else:
        print("\nAll Students and Their Grades:")
        for student_id, student in students.items():
            print(f"Student ID: {student_id}, Name: {student['name']}")
            for course_id, grade in student["courses"].items():
                print(f"  Course: {courses[course_id]['name']}, Grade: {grade if grade is not None else 'Not recorded'}")

# Function to view all courses and their enrolled students
def view_all_courses():
    if not courses:
        print("No courses in the system.")
    else:
        print("\nAll Courses and Their Enrolled Students:")
        for course_id, course in courses.items():
            print(f"Course ID: {course_id}, Name: {course['name']}")
            for student_id in course["students"]:
                print(f"  Student: {students[student_id]['name']}")

# Main function to interact with the user
def __main__():
    while True:
        print("\nWelcome to the Student Grading System!")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enroll Student in Course")
        print("4. Record Grade")
        print("5. Calculate Student Average")
        print("6. Calculate Course Average")
        print("7. View All Students")
        print("8. View All Courses")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            add_student(student_id, name)

        elif choice == "2":
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            add_course(course_id, course_name)

        elif choice == "3":
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            enroll_student(student_id, course_id)

        elif choice == "4":
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            grade = float(input("Enter grade: "))
            record_grade(student_id, course_id, grade)

        elif choice == "5":
            student_id = input("Enter student ID: ")
            calculate_student_average(student_id)

        elif choice == "6":
            course_id = input("Enter course ID: ")
            calculate_course_average(course_id)

        elif choice == "7":
            view_all_students()

        elif choice == "8":
            view_all_courses()

        elif choice == "9":
            print("Thank you for using the Student Grading System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Example usage
if __name__ == "__main__":
    __main__()