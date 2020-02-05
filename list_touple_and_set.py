# list

sub=['bangla', 'english']
sub_1=['math','biology']


print(sub)


sub.append(sub_1)
print(sub)



sub.extend(sub_1)
print(sub)

popped = sub.pop()

print(popped)
print(sub)

sub.reverse()
print(sub)

courses= ['EEE','CSE','MATH']
course_str= ' - '.join(courses)
nums = [1,3,2]

print(course_str)
sorted_courses = sorted(courses)
for course in courses:
    print(course)

for index, course in enumerate (courses, start=1):
    print(index, course)

print(sorted_courses)
print(min(nums))

# tuples
#NB: tuples does not support item assignment
tuple_1=('history','EEE','CSE','MATH')
print(tuple_1[1])

# set are values that are non-duplicate and unorder
cs_courses= {'EEE','CSE','MATH'}
art_courses = {'EEE','CSE','bangla'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))








