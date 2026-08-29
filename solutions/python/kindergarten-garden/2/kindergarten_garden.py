class Garden:
    students = [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve",
        "Fred",
        "Ginny",
        "Harriet",
        "Ileana",
        "Joseph",
        "Kincaid",
        "Larry"
    ]

    
    def __init__(self, diagram, students=None):
        self.diagram = diagram
        if students:
            self.students = sorted(students)


    def plants(self, student):
        positions = self.student_positions(student)
        rows = self.diagram_rows()

        plants = []
        for row in rows:
            for position in positions:
                plant = self.decode_plant(row[position])
                plants.append(plant)

        return plants

    
    def student_positions(self, student):
        position = self.students.index(student)
        return position * 2, position * 2 + 1


    def diagram_rows(self):
        return self.diagram.split("\n")

    @staticmethod
    def decode_plant(plant):
        if plant == "G":
            return "Grass"
        if plant == "C":
            return "Clover"
        if plant == "R":
            return "Radishes"
        if plant == "V":
            return "Violets"

        return None