#----------------------------------------------------------------------
# Program: newClasses .py module...Instructions to Students working on A8
#
# Purpose: To complete the methods in the classes below to make the
# University course creation application work correctly.
#
# Author: Thalia Edwards
#
# Date:12/03/2023
#---------------------------------------------------------------------

#--------------------------------------------------------------------
# University - University class - container for Department objects
#                                 and Catalog objects 
# Only one object for A8, but could hold other university objects
#---------------------------------------------------------------------

from imports import Department, Person, Student, Faculty

class University():
    """ University class - creates University objects, one for A8. 
        Container for Department, catalog, and student objects
        ---------------------------------------------------------- """
    
    def __init__(self, name = 'GMU'):
        self.__name = name
        self.__departments = [ ]   # container for Department objects
        self.__catalogs = [ ]      # container for catalogs
        self.__students = [ ]      # roster of all univ. student objects
 
    def __str__(self):
        return('University name: ' + self.__name + ', contains ' + 
               str(len(self.__departments))+ ' departments ')

    def getName(self):          # U1. provide code for this method.
        """Return name of University object. """
        return self.__name                    # code goes here
    
    def addDept(self, d_obj):   # U2. provide code for this method.
        """Add Department object to the 'departments' container list. """
        return self.__departments.append(d_obj)                    # code goes here
    
    def addCat(self, c_obj):   # U3. provide code for this method
        """Add the input Catalog object to the 'catalogs' cntainer list. """
        return self.__catalogs.append(c_obj)                   # code goes here

    def addStudent (self, s_obj):  # U4. provide code for this method
        """Add the input Student object to the 'students' cotainer list. """
        return self.__students.append(s_obj)                   # code goes here

    def __len__(self):
        return len(self.__departments)

    def __contains__(self, u_obj):
        if isinstance(u_obj, Department):
            for d in self.__departments:
                if d.d_code == u_obj.d_code:
                    return True
            return False
        if isinstance(u_obj, Catalog):
            for c in self.__catalogs:
                if c.__name == u_obj.__name:
                    return True
            return False
        
    def listDepts(self):    # U5. provide code for this method
        """Return a list of all Department objects in container. """
        return self.__departments                # code goes here

    def listStudents(self): # U6. provide code for this method
        """Return a list of all Student objects in container. """
        return self.__students               # code goes here

    def printDepts(self):
        for d in self.__departments:
            print(d)

#--------------------------------------------------------------------
# Course - Course class - course objects
#---------------------------------------------------------------------
class Course():
    """ Course class - creates Course objects - created by A8 appl.
                     - container for students registered for course
        Attributes:  d_code from Department object + number + title
                     name of Faculty object instructor
                     container list of assigned Student objects
                     in course.
        ---------------------------------------------------------- """
    
    def __init__(self, d_code, number, title, instructor):
        self.__d_code = d_code
        self.__number = number
        self.__section = '001'  # Only one section per course (KISS)
        self.__title = title    # descriptive course title
        self.__instructor = instructor
        self.__students = [ ]   # container for Student objects
 
    def __str__(self):  # Co1: provide code for this method
        """Return a string that is a good print/display representation
           of the course object.  Include the code, number, section,
           instructor, and number of students.  Example:
           Course: ENGR-101.001 - Introduction to Engineering
                                  Instructor: A. Einstein
                                  11 students registered          """
        return f'Course:  {str(self.__d_code) + "-" + str(self.__number) + "." + str(self.__section) + " - " + self.__title } , \
               \nInstructor:  {str(self.__instructor)}, \
               \nStudents registered: {len(self.__students)}'


# code goes here

    def addFaculty (self, f_obj):  # Co2. provide code for this method
        """Assign name of faculty belonging to the input object. """
        return self.__instructor == f_obj # code goes here

    def addStudent (self, s_obj):  # Co3. provide code for this method
        """Add input Student object to the course student container. """
        return self.__students.append(s_obj)             # code goes here

    def getName (self): # Co4. provide code for this method
        """Return course dept code + number (e.g. ENGR-101) as string. """
        return str(self.__d_code + self.__number)            # code goes here

    def __len__(self):
        return len(self.__students)

    def __eq__(self, c_obj):
        if self.__d_code == c_obj.__d_code and \
            self.__number == c_obj.__number: 
            return True                                                                                                                                               
        return False

    def printStudents(self):  # Co5. provide code for this course
        """Print/display the students in the course. Use the Student
           '__str__' method that works with the Python 'print' function. """
        for students in self.__students:
            print(students.__str__()) # code goes here
    
#--------------------------------------------------------------------
# Course - Catalog - Catalog object - contains Course objects
#                    Only one needed for A8
#---------------------------------------------------------------------
class Catalog():
    """ Catalog class - creates Catalog object - created by A8 appl.
                     - container for courses for a given semester+year
        Attributes:  name - e.g. S2021 is Spring 2021 semester
                     course list - object refs. of all courses in 
                     catalog.
        ---------------------------------------------------------- """
    
    def __init__(self, name):
        
        self.__name = name
        self.__courses = [ ]   # container for Course objects
        
 
    def __str__(self):
        return('Catalog: ' + self.__name + ' - ' + 
               str(len(self.__courses)) + ' courses' )

    def getName (self):    # Ct1. provide code for this method
        """Return name of Catalog. """
        return self.__name               # code goes here
    
    def addCourse (self, c_obj):  # Ct2. provide code for this method
        """Add the input Course object to the catalog 'courses'
           container list. """
        return self.__courses.append(c_obj)               # code goes here
               
    def __len__(self):
        return len(self.__courses)

    def __contains__(self, c_obj):   # Ct3. provide code for this method
        """This 'dunder' method uses 'Duck typing' to provide functionality
           for the application code to use the 'in' keyword to ask whether
           a course object is in the catalog.                         """
        return c_obj in self.__courses # code goes here

    def printCatalog(self): # Ct4. provide code for this method
        """Print a list of all Course objects in the catalog 'courses'
           container list.  Use the Course class '__str__' method that
           works with the Python 'print' function.                """
        for courses in self.__courses:
            print(courses.__str__()) # code goes here

    def listCourses(self):  # Ct5. provide code for this method
        """Return a list of all course objects in the catalogs 'courses'
           container list.                                        """
        return self.__courses                # code goes here


    
