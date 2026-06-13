d = {}

# -------- Reading the file ----------
with open("student_marks.csv", "r") as f:

    # Read header
    keys = f.readline().strip().split(',')

    # Create dictionary
    for key in keys:
        d[key] = []

    # Read remaining lines
    for line in f:
        data = line.strip().split(',')

        for i, key in enumerate(d):
            d[key].append(data[i])

# -------- Display dictionary ----------
import pprint
pprint.pprint(d)

print("Keys:", d.keys())
print("Values:", d.values())

# -------- Add total marks ----------
num_students = len(d[keys[0]])

d['total_marks'] = [0] * num_students

all_subjects = [
    'Maths','Physics','Chemistry','English',
    'Biology','Economics','History','Civics'
]

for i in range(num_students):
    total = 0
    count = 0

    for subject in all_subjects:
        mark = d[subject][i]

        if mark != "":
            total += int(mark)
            count += 1

    d['total_marks'][i] = total

# -------- Calculate Average ----------
d['Average'] = [0] * num_students

for i in range(num_students):
    count = 0

    for subject in all_subjects:
        if d[subject][i] != "":
            count += 1

    if count > 0:
        d['Average'][i] = round(d['total_marks'][i] / count, 2)

print("\nTotal Marks:", d['total_marks'])
print("Average:", d['Average'])