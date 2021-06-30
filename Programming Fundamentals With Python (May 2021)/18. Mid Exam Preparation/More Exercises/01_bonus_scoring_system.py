"""
Create a program that calculates bonus points for each student, for a certain course.
On the first line, you are going to receive the count of the students for this course.
On the second line, you will receive the count of the lectures in the course.
Every course has an additional bonus. You are going to receive it on the third line.
On the next lines, you will be receiving the count of attendances for each student.

The bonus is calculated with the following formula:
    {total bonus} = {student attendances} / {course lectures} * (5 + {additional bonus})

Find the student with the maximum bonus and print him/her, along with his attendances in the following format:
"Max Bonus: {maxBonusPoints}."
"The student has attended {studentAttendances} lectures."
Round the bonus points at the end to the nearest bigger number.

Print the maximum bonus points along with the attendances of the given student,
rounded to the nearest bigger number, scored by a student in this course in the format described above.
"""
import math

students_cnt = int(input())
lectures_cnt = int(input())
initial_bonus = int(input())


max_bonus, max_bonus_attendances = 0, 0


for students_cnt in range(1, students_cnt + 1):
    attendances = int(input())
    total_bonus = attendances / lectures_cnt * (5 + initial_bonus)
    if total_bonus >= max_bonus:
        max_bonus = total_bonus
        max_bonus_attendances = attendances


print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {max_bonus_attendances} lectures.")
