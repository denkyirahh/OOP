# Author - Michael Asomani        Date - 11/15/21
# Purpose - From the person class derive a student class 
# which has student id and an indicator for in-state or out-of-state residence
# then derive a class called undergrad which has class numbers, gpa,
# and indicator for graduated students, also have a method for advancing
# students to the next class

''' Student class(es) and inheritance '''
class Person(object):
    def __init__(self, first_name = '', last_name = ''):
        ''' Create a person: first_name, last_name, Defaults are nulls.'''
        self.__last_name = last_name
        self.__first_name = first_name
    def __str__(self):
        result_str = "Name: {}".format(self.__last_name + ', ' + \
                                        self.__first_name)
        return result_str
        
    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name
    
    def set_first_name(self, first_name):
        self.__first_name = first_name
    def set_last_name(self, last_name):
        self.__last_name = last_name
        
class Student(Person):
    def __init__(self, first_name = '', last_name = '', stu_id = 0, \
                 in_state = True):
        ''' Create a student and add student id to Person.'''
        Person.__init__(self, first_name, last_name)
        self.__stu_id = stu_id
        self.__in_state = in_state
        
    def __str__(self):
        if self.__in_state == True:
            result_str = Person.__str__(self)
            result_str = result_str + "; ID: {}".format(self.__stu_id) + \
                "; In-State"
        else:
            result_str = Person.__str__(self)
            result_str = result_str + "; ID: {}".format(self.__stu_id) + \
                "; Out-Of-State"
        return result_str
        
    def get_stu_id(self):
        return self.__stu_id
    
    def set_stu_id(self, stu_id):
        self.__stu_id = stu_id
        
    def get_in_state(self):
        return self.__in_state
    
    def set_in_state(self, in_state):
        self.__in_state = in_state
        
class Undergrad(Student):
    def __init__(self, first_name = '', last_name = '', stu_id = 0, \
                 in_state = True, class_number = 0, gpa = 0.0, grad = False):
        ''' Create an undergrad student and add class number, gpa, 
            and graduated to Student.'''
        Student.__init__(self, first_name, last_name, stu_id, in_state)
        self.__class_number = class_number
        self.__gpa = gpa
        self.__grad = grad
        
    def __str__(self):
        if self.__grad == True: 
            '''Graduates a student'''
            result_str = Student.__str__(self)
            result_str = result_str + \
                "; Graduated with {}".format(self.__gpa) + " GPA"
        elif self.__class_number < 1 and self.__gpa < 0.0:
            result_str = "Class number and GPA is incorrect," + \
            " classes are 1, 2, 3, 4 and GPA has to be in-between 0.0 and 4.0"
        elif self.__class_number > 4 and self.__gpa < 0.0:
            result_str = "Class number and GPA is incorrect," + \
            " classes are 1, 2, 3, 4 and GPA has to be in-between 0.0 and 4.0"
        elif self.__class_number > 4 and self.__gpa > 4.0:
            result_str = "Class number and GPA is incorrect," + \
            " classes are 1, 2, 3, 4 and GPA has to be in-between 0.0 and 4.0"
        elif self.__class_number < 1 and self.__gpa > 4.0:
            result_str = "Class number and GPA is incorrect," + \
            " classes are 1, 2, 3, 4 and GPA has to be in-between 0.0 and 4.0"
        elif self.__class_number < 1 or self.__class_number > 4:
            result_str = ("Class number is incorrect, classes are 1, 2, 3, 4")
        elif self.__gpa < 0.0 or self.__gpa > 4.0:
            result_str = ("GPA is incorrect, has to be in-between 0.0 and 4.0")
        else:
            result_str = Student.__str__(self)
            result_str = result_str + \
                "; Class Number: {}".format(self.__class_number) + \
                "; GPA: {}".format(self.__gpa) + "; Not Graduated"
        return result_str
        
    def get_class_number(self):
        return self.__class_number
    
    def set_class_number(self, class_number):
        self.__class_number = class_number
        
    def get_gpa(self):
        return self.__gpa
    
    def set_gpa(self, gpa):
        self.__gpa = gpa
        if self.__class_number < 1 or self.__class_number > 4 or self.__gpa < 0.0 or self.__gpa > 4.0:
            pass
        elif self.__class_number < 4 and self.__gpa >= 3.0:
            '''Advances student to next class if GPA is 3.0 or greater'''
            self.__class_number=self.__class_number+1
        elif self.__class_number == 4 and self.__gpa >= 3.0:
            '''Graduates student if they're in class 4 and their GPA is 3.0 or greater'''
            Undergrad.set_grad(self, True)
        else:
            pass
        
    def get_grad(self):
        return self.__grad
    
    def set_grad(self, grad):
        self.__grad = grad

# ================================ main starts here
# ---------------------------------- Tests for Person
p1 = Person("Mickey", "Mouse")
#print(p1)
assert p1.__str__() == "Name: Mouse, Mickey"
assert p1.get_first_name() == "Mickey"
assert p1.get_last_name()  == "Mouse"
p1.set_last_name("Duck")
assert p1.__str__() == "Name: Duck, Mickey"
p1.set_first_name("Daffy")
assert p1.__str__() == "Name: Duck, Daffy"

# ---------------------------------- Tests for Student
s1 = Student("Michael", "Asomani", 514617, True)
#print(s1)
assert s1.__str__() == "Name: Asomani, Michael; ID: 514617; In-State"
assert s1.get_stu_id() == 514617
assert s1.get_in_state() == True
s1.set_stu_id(123456)
assert s1.__str__() == "Name: Asomani, Michael; ID: 123456; In-State"
s1.set_in_state(False)
assert s1.__str__() == "Name: Asomani, Michael; ID: 123456; Out-Of-State"

# ---------------------------------- Tests for Undergrad
ug1 = Undergrad("Tony", "Stark", 1001, True, 1)
"""
print(ug1)
ug1.set_gpa(3.0)
print(ug1)
ug1.set_gpa(4.0)
print(ug1)
ug1.set_gpa(3.0)
print(ug1)
ug1.set_gpa(4.0)
print(ug1)
"""
assert ug1.__str__() == "Name: Asomani, Michael; ID: 514617; In-State; Class Number: 1; GPA: 0.0; Not Graduated"
assert ug1.get_class_number() == 1
assert ug1.get_gpa() == 0.0
assert ug1.get_grad() == False
ug1.set_class_number(4)
assert ug1.__str__() == "Name: Asomani, Michael; ID: 514617; In-State; Class Number: 4; GPA: 0.0; Not Graduated"
ug1.set_gpa(3.5)
assert ug1.__str__() == "Name: Asomani, Michael; ID: 514617; In-State; Graduated with 3.5 GPA"
ug1.set_grad(False)
assert ug1.__str__() == "Name: Asomani, Michael; ID: 514617; In-State; Class Number: 4; GPA: 3.5; Not Graduated"
