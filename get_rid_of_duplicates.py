# dictionary of students
student_data = {
    "id1": {"name": "MJ", "class": "V", "Subject_integration": "Math, English, Science"},
    "id2": {"name": "Mahek", "class": "V", "Subject_integration": "Math, English, Science"},
    "id3": {"name": "Loki", "class": "V", "Subject_integration": "Math, English, Science"},
    "id4": {"name": "Avenger", "class": "V", "Subject_integration": "Math, English, Science"}
}
result = {}
seen_keys = [] # using a list instead of set

for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["Subject_integration"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id]= details

# print output by output
for k, v in result.items():
    print(k, ":",v)
