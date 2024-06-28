import pandas as pd
import sys

data = pd.read_csv('cleaned_dataset.csv')

# Age at enrollment group by students codition
age_status_counts = data.groupby(['Age at enrollment', 'Target']).size().unstack(fill_value=0)
print(age_status_counts)

# Gender distribution group by students codition
gender_status_counts = data.groupby(['Gender', 'Target']).size().unstack(fill_value=0)
print(gender_status_counts)

# Nacionality distribution group by students codition
nacionality_status_counts = data.groupby(['Nacionality', 'Target']).size().unstack(fill_value=0)
print(nacionality_status_counts)

# Admission grade distribution group by students codition
data['Admission grade'] = data['Admission grade'].round()
admission_status_counts = data.groupby(['Admission grade', 'Target']).size().unstack(fill_value=0)
print(admission_status_counts)

# Curricular Units Enrolled vs. Approved 1st sem
enrolled_approved_counts = data.groupby(['Curricular units 1st sem (enrolled)','Curricular units 1st sem (approved)', 'Target']).size().unstack(fill_value=0)
print(enrolled_approved_counts)

# Curricular Units Enrolled vs. Approved 2nd sem
enrolled_approved_counts_2nd = data.groupby(['Curricular units 2nd sem (enrolled)','Curricular units 2nd sem (approved)', 'Target']).size().unstack(fill_value=0)
print(enrolled_approved_counts)

# 1st Semester Grades
data['Curricular units 1st sem (grade)'] = data['Curricular units 1st sem (grade)'].round()
grades_1st = data.groupby(['Curricular units 1st sem (grade)', 'Target']).size().unstack(fill_value=0)
print(grades_1st)

# 2nd Semester Grades
data['Curricular units 2nd sem (grade)'] = data['Curricular units 2nd sem (grade)'].round()
grades_2nd = data.groupby(['Curricular units 2nd sem (grade)', 'Target']).size().unstack(fill_value=0)
print(grades_2nd)

# Previous qualification
previous_qualification = data.groupby(['Previous qualification', 'Target']).size().unstack(fill_value=0)
print(previous_qualification)

# Father's qualification
fathers_qualification = data.groupby(['Father\'s qualification', 'Target']).size().unstack(fill_value=0)
print(fathers_qualification)

# Mother's qualification
mothers_qualification = data.groupby(['Mother\'s qualification', 'Target']).size().unstack(fill_value=0)
print(mothers_qualification)

# Father's occupation
fathers_occupation = data.groupby(['Father\'s occupation', 'Target']).size().unstack(fill_value=0)
print(fathers_occupation)

# Mother's occupation
mothers_occupation = data.groupby(['Mother\'s occupation', 'Target']).size().unstack(fill_value=0)
print(mothers_occupation)

# Scholarship holder
scholarship_holder = data.groupby(['Scholarship holder', 'Target']).size().unstack(fill_value=0)
print(scholarship_holder)

# Debtor status
debtor_status = data.groupby(['Debtor', 'Target']).size().unstack(fill_value=0)
print(debtor_status)

# Educational special needs
educational_special_needs = data.groupby(['Educational special needs', 'Target']).size().unstack(fill_value=0)
print(educational_special_needs)

# Tuition fees up to date
tuition_fees_up_to_date = data.groupby(['Tuition fees up to date', 'Target']).size().unstack(fill_value=0)
print(tuition_fees_up_to_date)

# Daytime/evening attendance
daytime_evening_attendance = data.groupby(['Daytime/evening attendance	', 'Target']).size().unstack(fill_value=0)
print(daytime_evening_attendance)

# Application mode
application_mode = data.groupby(['Application mode', 'Target']).size().unstack(fill_value=0)
print(application_mode)

# Admission Grade vs. Age at Enrollment 
data['Admission grade'] = data['Admission grade'].round()
admission_grade_counts = data.groupby(['Admission grade', 'Age at enrollment', 'Target']).size().unstack(fill_value=0)
print(admission_grade_counts)

# Curricular units' grades by Course
course_mean_grades = data.groupby(['Course', 'Target'])['Curricular units 1st sem (grade)'].mean().unstack(fill_value=0)
print(course_mean_grades)

# Financial metrics
finacial_metrics = data.groupby(['GDP', 'Unemployment rate','Inflation rate', 'Target']).size().unstack(fill_value=0)
print(finacial_metrics)

