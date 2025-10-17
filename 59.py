#  59.	Write a program to calculate final exam marks using weighted average of assignments, midterm, and final exam.

assignments = float(input("Enter marks for assignments: "))
midterm = float(input("Enter marks for midterm: "))
final_exam = float(input("Enter marks for final exam: "))

w_assignments = float(input("Enter weight for assignments (as decimal): "))
w_midterm = float(input("Enter weight for midterm (as decimal): "))
w_final = float(input("Enter weight for final exam (as decimal): "))

final_marks = (assignments * w_assignments +
               midterm * w_midterm +
               final_exam * w_final)

print(f"Final exam marks = {final_marks}")
