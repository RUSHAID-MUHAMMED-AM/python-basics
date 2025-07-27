# Student's name

# Course name

# Science marks

#  Update and Add data to the dictionary

# Loop through marks and print only subjects with marks above 80


student = {
    "name": "Rushaid",
    "age": 24,
    "course": "Full Stack Development",
    "marks": {
        "math": 85,
        "english": 78,
        "science": 92
    }
}

print(student["name"]);
print(student["course"]);
print(student["marks"]["science"]);
student["age"]=25;
student["place"]="Kozhikode";
print(student["age"])
print(student["place"])

for subject,mark in student["marks"].items():
    if mark>80:
        print(f"{subject} : {mark}")