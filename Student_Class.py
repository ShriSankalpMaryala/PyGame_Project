class Student():
    def __init__(self, n, a, g, f):
        self.name = n
        self.age = a
        self.grade = g
        self.favourite_color = f
    def display(self):
        print(self.name, self.age, self.grade, self.favourite_color)
adam = Student("adam", 12, 8, "blue")
adam.display()