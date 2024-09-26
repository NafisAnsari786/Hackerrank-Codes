'''Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
 

Solution:'''

if __name__ == '__main__':
    students=[]
    # Input the no. of students, their names and grade
    for _ in range(int(input())):
        name = input()
        grade = float(input())
        students.append([name, grade])
        
    # find the lowest grade
    lowest_grade=min(students, key=lambda x: x[1])[1]
        
    # find the second lowest grade by excluding the lowest grade
        
    second_lowest_grade=min([grade for name, grade in students if
    grade>lowest_grade])
        
    # Collect names of students with the second lowest grade
    second_lowest_students=[name for name, grade in students if
    grade==second_lowest_grade]
        
        
    # Sort the names alphabetically and print them
    for name in sorted(second_lowest_students):
        print(name)
            
