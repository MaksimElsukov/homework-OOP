from logging.handlers import RotatingFileHandler
from pydoc import stripid


#Объявление классов
lc__list = []
st__list = []
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []
        self.avg_gr = 0
        st__list.append(self)

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.rating:
                lecturer.rating[course] += grade
            else:
                lecturer.rating[course] = grade
        else:
            return 'Ошибка'

    def avg_grades(self):
        summa = 0
        for key in self.grades.keys():
            summa = summa + self.grades [key]
            avg = summa / len(self.grades)
            self.avg_gr = avg

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    
    def __str__(self):
        self.avg_grades()
        courses = ""
        for cours in self.courses_in_progress:
            if courses == "": 
                courses += cours 
            else : 
                courses +=","+ cours

        end_courses = ""
        for end_cours in self.finished_courses:
            if end_courses == "": 
                end_courses += end_cours
            else: 
                 end_courses += ","+end_cours     
        st_name = f'Имя:  {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнюю работу: {self.avg_gr} \nКурсы в процессе изучения: {courses.strip()} \nЗавершённые курсы: {end_courses.strip()}'
        return st_name
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Не Студент")
            return 
        if self.avg_gr < other.avg_gr:
            print(f'Лучший студент: {other.name} {other.surname}. Средняя оценка: {other.avg_gr}') 
        else:
            print(f'Лучший студент: {self.name} {self.surname}. Средняя оценка: {self.avg_gr}')        
        return (self.avg_gr < other.avg_gr)

def avg_rating_lc(lecturers = [],cours = ""):
    sum_rating = 0
    for lec in lecturers:
        if isinstance(lec, Lecturer):
            sum_rating = sum_rating + lec.rating[cours]
            avg = sum_rating/len(lecturers)
    print(f'Средняя оценка лекторов за курс: {cours} = {avg}')  

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
       

class Lecturer(Mentor):

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.rating = {}
        self.avg_rt = 0
        lc__list.append(self)
    def avg_rating(self):
        summa = 0
        for key in self.rating.keys():
            summa = summa + self.rating[key]
            avg = summa / len(self.rating)
            self.avg_rt = avg
            

    def __str__(self):
        self.avg_rating()
        lc_name = f'Имя:  {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avg_rt}'
        return lc_name

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Не Лектор")
            return 
        if self.avg_rt < other.avg_rt:
            print(f'Лучший лектор: {other.name} {other.surname}') 
        else:
            print(f'Лучший лектор: {self.name} {self.surname}')        
        return (self.avg_rt < other.avg_rt)
        
    
class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += grade
            else:
                student.grades[course] = grade
        else:
            return 'Ошибка'

    def __str__(self):
        rev_name = f'Имя:  {self.name} \nФамилия: {self.surname}'
        return rev_name
def avg_grade_st(students = [],cours = ""):
    sum_grades = 0
    for stud in students:
        if isinstance(stud, Student):
            sum_grades = sum_grades + stud.grades[cours]
            avg = sum_grades/len(students)
    print(f'Средняя оценка студентов за курс: {cours} = {avg}')

#Основной код     
rev = Reviewer("Some","Rev")
#print(rev)
rev.courses_attached.append('Eng')
rev.courses_attached.append("Math")

lc = Lecturer("Some","Lec")
lc.courses_attached = {"Math", "Eng"}
#print(lc)

st1 = Student("Some","Stud1","Man")
# st.grades = {'Math': 2, 'Eng': 5}
st1.courses_in_progress = "Math", "Eng"
# st.finished_courses = "Програм", "Био"
#print(st)

st2 = Student("Some","Stud2","Man")
st2.courses_in_progress = "Math", "Eng"
rev.rate_hw(st1, 'Eng', 8)
rev.rate_hw(st2, 'Eng', 2)
rev.rate_hw(st1, 'Math', 10)
rev.rate_hw(st2, 'Math', 7)

avg_grade_st(st__list,"Eng")

lc1 = Lecturer("Some","Lect1")
lc2 = Lecturer("Some","Lect2")
lc.courses_attached = {"Math", "Eng"}
lc1.courses_attached = {"Math", "Eng"}
lc2.courses_attached = {"Math", "Eng"}
st1.rate_lc(lc,"Eng", 10)
st1.rate_lc(lc1, 'Eng', 3)
st2.rate_lc(lc2, 'Eng', 8)
lc.avg_rating()
lc1.avg_rating()
lc < lc1
avg_rating_lc(lc__list,"Eng")

st1.avg_grades()
st2.avg_grades()
st1 < st2
avg_grade_st(st__list,"Eng")

# rev.rate_hw(st,'Eng',10)
# rev.rate_hw(st,"Math",5)
# st.rate_lc(lc,"Math",150)
# st.rate_lc(lc,"Eng",200)

# print("Студент:")
# print(st)
# print('\n')
# print("Лектор:")
# print(lc)



# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']

# cool_lecturer = Lecturer('Some', 'Buddy')
# cool_lecturer.courses_attached += ['Python']

# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)

# print(best_student.grades)