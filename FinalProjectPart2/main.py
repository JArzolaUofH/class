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
            keys = sorted(students.keys(), key= lambda x: students[x]['last name'])
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
                    #grad_date = students[student]['graduation date']
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
                    file.write('{},{},{},{},{}\n'.format(id, last_name, first_name, major, gpa))

    def bad(self): # creates disciplined students file
        students = self.studentid_list
        keys = sorted(students.keys(), key=lambda x: students[x]['graduation date'], reverse=True)
        with open('DisciplinedStudents.csv', 'w') as file:
            for student in keys:
                id = student
                last_name = students[student]['last name']
                first_name = students[student]['first name']
                #grad_date = students[student]['graduation date']
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

    majors = []
    gpas = []
    for student in students:
        checked_gpa = students[student]['GPA']
        checked_major = students[student]['major']
        if checked_gpa not in majors:
            gpas.append(checked_gpa)
        if checked_major not in majors:
            majors.append(checked_major)

    query_user = None
    while query_user != 'q':
        query_user = input("\nEnter student gpa and major or enter 'q' to quit:\n")
        if query_user == 'q':
            break
        else:
            selected_gpa = None
            selected_major = None
            query_user = query_user.split()
            invalid_input = False
            for word in query_user:
                if word in gpas:
                    if selected_gpa:
                        # should only have one submitted gpa
                        invalid_input = True
                    else:
                        selected_gpa = word
                elif word in majors:
                    if selected_major:
                        # should only have one submitted major
                        invalid_input = True
                    else:
                        selected_major = word
            if not selected_gpa or not selected_major or invalid_input:
                print("No such student")
            else:
                # ordered list of keys to iterate through based on majors

                keys = sorted(students.keys(), key=lambda x: students[x]['major'])

                # get matching list of students based on user input
                matching_students = []

                similar_students = {}
                for student in keys:
                    if students[student]['major'] == selected_major:
                        # don't add disciplined or graduated to lists
                        today = datetime.now().date()
                        grad_date = students[student]['grad_date']
                        graduation = datetime.strptime(grad_date, "%m/%d/%Y").date()
                        graduated = graduation < today
                        if students[student]['GPA'] == selected_gpa:
                            if not graduated and not students[student]['bad']:
                                matching_students.append((student, students[student]))
                        else:
                            if not graduated and not students[student]['bad']:
                                similar_students[student] = students[student]

                # output student if matched
                if matching_students:
                    student = matching_students[0]
                    id = student[0]
                    first_name = student[1]['first name']
                    last_name = student[1]['last name']
                    gpa = student[1]['GPA']
                    print("Your student(s): {}, {}, {}, {}\n".format(id, first_name, last_name, gpa))

                    if similar_students:
                        matched_gpa = gpa

                        close_student = None
                        closest_gpa = None
                        for student in similar_students:
                            if closest_gpa is None:
                                close_student = similar_students[student]
                                closest_gpa = abs(int(matched_gpa) - int(similar_students[student]['gpa']))
                                id = student
                                first_name = similar_students[student]['first name']
                                last_name = similar_students[student]['last name']
                                gpa = similar_students[student]['GPA']
                                continue
                            gpa_diff = abs(int(matched_gpa) +-.25 int(similar_students[student]['GPA']))
                            if gpa_diff < closest_gpa:
                                close_student = student
                                closest_gpa = gpa_diff
                                id = student
                                first_name = similar_students[student]['first name']
                                last_name = similar_students[student]['last name']
                                gpa = similar_students[student]['GPA']
                        print("You may, also, consider: {}, {}, {}, {}\n".format(id, first_name, last_name, gpa))
                    else:
                        print("done")






























