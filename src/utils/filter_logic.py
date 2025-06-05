def sort_students_by_name(students):
    return sorted(students, key=lambda s: s.name)

def filter_by_subject(students, subject):
    return [s for s in students if s.favorite_subject == subject]

def filter_by_age(students, age):
    return [s for s in students if s.age == age]