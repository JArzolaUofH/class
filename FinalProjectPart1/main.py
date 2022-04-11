# Justine Arzola 1804667
import csv
from datetime import datetime
# create class for all outputs
class OutputStudents:

    def __init__(self, studentid_list):

        self.studentid_list = studentid_list

    def roster(self):
         #creates the full roster
        with open('FullRoster.csv', 'w') as file:
            students = self.studentid_list
            # get order of keys to write to file based on last name
            keys = sorted(students.keys(), key=lambda x: students[x]['last name'])
            for student in keys:
                id = student
                major = students[student]['major']
                first_name = students[student]['first name']
                last_name = students[student]['last name']
                gpa = students[student]['GPA']
                #grad_date = students[student]['graduation date']
                bad = students[student]['disciplinary action']
                file.write('{},{},{},{},{},{},{}\n'.format(id, major, first_name, last_name, gpa, grad_date, bad))

    def by_major(self): #sort students by major
        students = self.studentid_list
        majors = []
        keys = sorted(students.keys())
        for student in students:
            major = students[student]['major']
            if major not in majors:
                majors.append(major)
        for bymajor in majors:
            file_name = bymajor.capitalize() + 'Students.csv'
            with open(file_name, 'w') as file:
                for student in keys:
                    id = student
                    last_name = students[student]['last name']
                    first_name = students[student]['first name']
                    grad_date = students[student]['graduation date']
                    bad = students[student]['disciplinary action']
                    major = students[student]['major']

                    if bymajor == major:
                        file.write('{},{},{},{},{}\n'.format(id, last_name, first_name, grad_date, bad))

    # scholarship candidates
    def scholars(self):

        students = self.studentid_list
        keys = sorted(students.keys(),key=lambda x: students[x]['GPA'], reverse=True)
        with open('ScholarshipCandidates.csv', 'w') as file:
            for student in keys:
                id = student
                last_name = students[student]['last name']
                first_name = students[student]['first name']
                major = students[student]['major']
                gpa = students[student]['GPA']
                if float(gpa) > 3.8: #only students with higher gpa than 3.8 are qualified
                    file.write('{},{},{},{}\n'.format(id, last_name, first_name, major, gpa))

    def bad(self): # creates disciplined students file
        students = self.studentid_list
        keys = sorted(students.keys(), key=lambda x: students[x]['graduation date'], reverse=True)
        with open('DisciplinedStudents.csv', 'w') as file:
            for student in keys:
                id = student
                last_name = students[student]['last name']
                first_name = students[student]['first name']
                grad_date = students[student]['graduation date']
                bad = students[student]['disciplinary action']
                if bad:
                    file.write('{},{},{},{}\n'.format(id, last_name, first_name, grad_date))


if __name__ == '__main__': #take csv files and read then write to files
    students = {}
    files = ['StudentsMajorsList.csv', 'GPAList.csv', 'GraduationDatesList.csv']
    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                student_id = line[0]
                if file == files[0]:
                    students[student_id] = {}
                    last_name = line[1]
                    first_name = line[2]
                    major = line[3]
                    bad = line[4]
                    #gpa = line[5]
                    #grad_date = line[6]
                    students[student_id]['last name'] = last_name.strip()
                    students[student_id]['first name'] = first_name.strip()
                    students[student_id]['major'] = major.strip()
                    #students[student_id]['gpa'] = gpa.strip()
                    students[student_id]['graduation date'] = bad.strip()
                    students[student_id]['disciplinary action'] = bad
                elif file == files[1]:
                    gpa = line[1]
                    students[student_id]['GPA'] = gpa
                elif file == files[2]:
                    grad_date = line[1]
                    students[student_id]['grad_date'] = grad_date

    output = OutputStudents(students)
# Create all the output files
    output.roster()
    output.by_major()
    output.scholars()
    output.bad()













