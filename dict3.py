# student = {
#     "name": "Rushaid",
#     "age": 24,
#     "course": "Full Stack Development",
#     "marks": {
#         "math": 88,
#         "english": 75
#     }
# }


# Add a new key called "phone_number" and set its value to "9876543210".

# Update the "age" to 25.

# Print the entire dictionary after these changes.


student = {
    "name": "Rushaid",
    "age": 24,
    "course": "Full Stack Development",
    "marks": {
        "math": 88,
        "english": 75
    }
}

student.update({"phone_number":"9876543210","age":25})
print(student)