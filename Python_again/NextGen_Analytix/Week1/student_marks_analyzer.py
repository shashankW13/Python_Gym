marks = {}
SUBJECTS = 3

enter_choice = 'y'
print("Student Marks Analyzer")
while enter_choice.lower() == 'y':
    subject = []
    
    try:
        name = input("\nEnter students name: ").strip().title()
        for subject_count in range(SUBJECTS):
            subject_marks = int(input(f"Enter subject {subject_count + 1} marks: "))
            subject.append(subject_marks)

        marks[name] = subject
    except ValueError:
        print("Invalid marks!")

    enter_choice = input("Do you want to add more students (y/n)?: ")

students_count = len(marks)

def avg_marks():
    if students_count > 0:
        print("\nAverage marks of each students: ")
        for name, scores_list in marks.items():
            avg = sum(scores_list)/3
            print(f"{name} => Average: {avg:.2f}")
    else:
        return "No students exist!"

def topper():
    if students_count > 0:
        topper_marks = 0
        topper = ''
        for name, mark_list in marks.items():
            mark_list_sum = sum(mark_list)
            if topper_marks < mark_list_sum:
                topper_marks = mark_list_sum
                topper = name
        print(f"\nTopper: {topper} with {topper_marks} marks\n")
    else:
        return "No students exist!"

def subject_wise_avg():
    maths_sum = 0
    science_sum = 0
    commerce_sum = 0

    total_students = len(marks)
    if total_students > 0:
        for marks_list in marks.values(): 
            maths_sum += marks_list[0]
            science_sum += marks_list[1]
            commerce_sum += marks_list[2]

        print("Subject wise average:")
        print(f"Maths = {(maths_sum/total_students):.2f}")
        print(f"Science = {(science_sum/total_students):.2f}")
        print(f"Commerce = {(commerce_sum/total_students):.2f}\n")
    else:
        return "No students exist!"


avg_marks()
topper()
subject_wise_avg()