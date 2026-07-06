class Student(object):
    def __init__(self, name, marks=None):
        """
        marks is a list
        """
        self.name = name
        self.marks = marks if marks is not None else []
    
    # Add marks method

    def add_mark(self, mark):
        """
        input: int(mark),
        appends mark to the list
        of marks
        """
        self.marks.append(mark)
        return self.marks
    
    # Find the average

    def average(self):
        """
        no args,
        returns the avg of the student
        marks
        """
        # avg = sum of all / length
        return sum(self.marks) / len(self.marks)
    
    # Find the highest mark

    def highest_mark(self):
        """
        returns the highest mark
        """
        return max(self.marks)

# examples
s = Student("Mike")

s.add_mark(80)
s.add_mark(90)
s.add_mark(70)

print(s.average())

print(s.highest_mark())
