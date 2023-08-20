import pandas

student_dict = {
    "students": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(value)


students_data_frame = pandas.DataFrame(student_dict)
# print(students_data_frame)

# for (key, value) in students_data_frame.items():
#     print(key)
#     print(value)

for (index, row) in students_data_frame.iterrows():
    if row.students == "Angela":
        print(row.score)