# Get the grade obtained in the school test from the user
grade = int(input("Enter the grade obtained in the school test: "))

# Check the grade and take appropriate actions
if grade == 10:
    print("Congratulations! The student achieved a perfect score of 10. The teacher will praise the student with the parent.")
elif grade == 8 or grade == 9:
    print("The student obtained a grade of", grade, "which is very good. The teacher will give a small note to the parent.")
elif grade == 5:
    print("The student obtained a grade of 5. The teacher will give a note to the parent.")
elif grade < 5:
    print("The student obtained a grade of", grade, "which is insufficient. The teacher will expel the student from the school.")
else:
    print("Invalid grade entered. Please enter a grade between 0 and 10.")