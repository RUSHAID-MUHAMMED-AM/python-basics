# student = {
#     "name": "Rushaid",
#     "age": 24,
#     "course": "Full Stack Development",
#     "marks": {
#         "math": 88,
#         "english": 75
#     }
# }

# Use .setdefault() to add a key called "email" with value "rushaid@example.com".

# Then, try using .setdefault() again on the same key with a different value like "test@example.com".

# Print the value of "email" after both operations to see what happens.




student = {
    "name": "Rushaid",
    "age": 24,
    "course": "Full Stack Development",
    "marks": {
        "math": 88,
        "english": 75
    }
}

student.setdefault("email","rushaid@example.com")
student.setdefault("email","test@example.com")
print(student.get("email"))