class Car():
    def __init__(self, m, c, y, s):
        self.model = m
        self.color = c
        self.year = y
        self.size = s
    def display(self):
        print(self.model, self.color,  self.year, self.size )
Ford = Car("Ford", "blue", 2018, "large")
Ford.display()
Tesla = Car ("Tesla", "black", 2023, "medium")
Tesla.display()