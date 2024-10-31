#-------------------------------------------------------------------------
# Application used for assignment follows - code is provided to students
#--------------------------------------------------------------------------
# IT-209 Assignment #8 (A8) Application Code
#
# This code is provided to students as part of A8.
#
# 'imports' module contains functions and classes provided
# 'newClasses' module contains the classes students are to provide
#              code for the indicated methods
# 'DataSetUp' module contains a function that creates data for
#          Departments, Students, Faculty, University, and Catalog
# Course objects are not pre-loaded by DataSetUp, but rather are created
#          by users of this application code.
#--------------------------------------------------------------------------

from imports import selectMenu, Department, Person, Student, Faculty
from newClasses import University, Catalog, Course  
from DataSetUp import DataSetUp
import os

GMU, S2024 = DataSetUp()   # run the data load function

Menu = """

        1. Create Course
        2. Add Students to Course (Spring 2024)
        3. Print Students in Course
        4. Print Courses in Catalog
        5. Print All Students - summary list
        6. Print All Students - detailed list
        Q. Quit

"""

while True:
    os.system('cls')
    print (Menu)
    menu_pic = input('Select one of the above and hit "Enter": ')
    
    if menu_pic == '1':   # Create Course -----------------------------
        d_list = GMU.listDepts( )
        item_pic, ret_name, ret_object = selectMenu('Create course, select Dept.', d_list)
        if item_pic != 'x':
            number = input ('Enter course number, 000 to 999: ')
            title = input ('Enter course title: ')
            # Select the instructor for the course --------------
            f_list = ret_object.listFaculty( )
            faculty_pic, faculty_name, faculty_object = selectMenu ('Pick instructor', f_list)
            if faculty_pic != 'x':   # create the course and add to the Catalog
                newCourse = Course(ret_object.d_code, number, title, faculty_object.getName() )        
                if newCourse not in S2024:
                    S2024.addCourse(newCourse)
                    input('\n' + newCourse.getName() + ' added to ' + S2024.getName( ) +
                          '"Enter" to continue') 
                else:
                    print('Course already in catalog ', S2024.getName( ))
                
    if menu_pic == '2':   # Add students to course -----------------------
        course_pic = ' '
        while course_pic != 'x':  # allow for multiple students to be added at once
            c_list = S2024.listCourses( )  # Select course ------------------
            course_pic, course_name, course_object = selectMenu('Add students for...', c_list)
            if course_pic == 'x': break
            # Select the student to be added --------------
            s_list = GMU.listStudents( )
            student_pic, student_name, student_object = selectMenu ('Select student', s_list)
            if student_pic != 'x':
                if course_object.addStudent(student_object):
                    input(student_object.getName() + ' added to course ' + course_object.getName())
                else:
                    input(student_object.getName() + ' is already registered for the course')
                
    if menu_pic == '3':    # print students in course --------------------
        c_list = S2024.listCourses()   # Select course ------------------
        course_pic, course_name, course_object = selectMenu('Courses', c_list)
        if course_pic != 'x': 
            course_object.printStudents()
            input('\nHit "Enter" to continue ')
        
    if menu_pic == '4':    # print courses in catalog
        S2024.printCatalog()
        input ('\nHit "Enter" to continue ')

    if menu_pic == '5':    # list students in department - summary
        print ('\nList of Students at ', GMU.getName() )
        for s in GMU.listStudents():
            print(s.getName() )
        input ('\nHit "Enter" to continue ')
        
    if menu_pic == '6':    # list students in department - detailed
        print ('\nList of Students at ', GMU.getName() )
        for s in GMU.listStudents():
            print(s)
        input ('\nHit "Enter" to continue ')
              
    if menu_pic in 'Qq' and menu_pic != '': break                     
                     
input('\n\n\n***** End of A8 Application Code - Hit "Enter" to end **********')

    
