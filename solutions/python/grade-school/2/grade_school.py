class School:
    def __init__(self):
        self.students = {}
        self.result = []

    def add_student(self, name, grade):
        self.students.setdefault(grade, [])
        if name not in self.roster():
            self.students[grade].append(name)
            self.result.append(True)
        else: 
            self.result.append(False)
        
    def roster(self):
        return [name for grade in sorted(self.students) for name in sorted(self.students[grade])]

    def grade(self, grade_number):
        return sorted(self.students.get(grade_number, []))

    def added(self):
        return self.result
