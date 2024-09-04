student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 22,
    'marital_status': 'Single',
    'skills': ['Python', 'Java'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}

length_student_dict = len(student)
print("Length of the student dictionary:", length_student_dict)

skills_value = student['skills']
print("Skills:", skills_value)
print("Data type of skills:", type(skills_value))

student['skills'].extend(['JavaScript', 'SQL'])
print("Updated skills:", student['skills'])

keys_list = list(student.keys())
print("Dictionary keys:", keys_list)

values_list = list(student.values())
print("Dictionary values:", values_list)

student_tuples = list(student.items())
print("Dictionary as list of tuples:", student_tuples)

student.pop('marital_status')
print("Dictionary after deleting 'marital_status':", student)

del student
