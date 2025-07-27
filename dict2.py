# student = {
#     "name": "Rushaid",
#     "age": 24,
#     "course": "Full Stack Development",
#     "marks": {
#         "math": 88,
#         "english": 75
#     }
# }
# Print the student’s name using key access

# Try to print the student’s phone number using .get() method, with a default value "Not provided" if phone number is not present.



student = {
    "name": "Rushaid",
    "age": 24,
    "course": "Full Stack Development",
    "marks": {
        "math": 88,
        "english": 75
    }
}


print(student["name"]);
print(student.get("phone_number"));