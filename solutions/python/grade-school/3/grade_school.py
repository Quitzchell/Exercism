class School:
    def __init__(self):
        self.students: dict[int, list[str]] = {}
        self.enrolled: set[str] = set()
        self.additions: list[bool]  = []

    def add_student(self, name, grade):
        self.students.setdefault(grade, [])
        if name not in self.enrolled:
            self.students[grade].append(name)
            self.enrolled.add(name)
            self.additions.append(True)
        else: 
            self.additions.append(False)
        
    def roster(self):
        return [name for grade in sorted(self.students) for name in sorted(self.students[grade])]

    def grade(self, grade_number):
        result = sorted(self.students.get(grade_number, []))
        return result

    def added(self):
        return self.additions
