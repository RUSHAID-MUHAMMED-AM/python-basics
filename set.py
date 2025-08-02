# python_students = {"Ali", "Ravi", "Neha", "Sara", "John"}
# django_students = {"Neha", "John", "Meena", "Ravi", "Kiran"}
# Now do the following:

# 🔸 1. Find all students who enrolled in either Python or Django. (Hint: union)
# 🔸 2. Find students who enrolled in both Python and Django. (Hint: intersection)
# 🔸 3. Find students who enrolled in only Python but not Django. (Hint: difference)
# 🔸 4. Find students who enrolled in only one of the two courses. (Hint: symmetric difference)


python_students = {"Ali", "Ravi", "Neha", "Sara", "John"}
django_students = {"Neha", "John", "Meena", "Ravi", "Kiran"}

print(python_students|django_students)
print(python_students&django_students)
print(python_students-django_students)
print(python_students^django_students)