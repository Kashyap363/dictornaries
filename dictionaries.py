# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'browney'
dog['color'] = 'White'
dog['breed'] = 'shitzu'
dog['legs'] = 4
dog['age'] = 7
print(dog)

# Create a student dictionary
student = {
    'first_name': 'Kashyap',
    'last_name': 'Vyas',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Gaming', 'Travelling'],
    'country': 'India',
    'city': 'Ahemadabad',
    'address': 'Maninagar'
}
print(student)

# Get the length of the student dictionary
student_length = len(student)
print("Length of student",student_length)

# Get the value of skills and check the data type, it should be a list
skills_value = student['skills']
skills_type = type(skills_value)

# Modify the skills values by adding one or two skills
student['skills'].extend(['Learning'])
print("After adding skills",student)

# Get the dictionary keys as a list
keys_list = list(student.keys())

# Get the dictionary values as a list
values_list = list(student.values())

# Change the dictionary to a list of tuples using items() method
items_list = list(student.items())

# Delete one of the items in the dictionary
del student['marital_status']
print("After delete martial status",student)

# Delete one of the dictionaries
del dog