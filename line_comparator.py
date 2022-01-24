import math


class LineComparison:

    @staticmethod
    def line_inputs(x, y):
        x = int(input(f"Enter {x} value "))
        y = int(input(f"Enter {y} value "))
        return [x, y]

    @staticmethod
    def line_length_calculator(line1, line2):
        return math.sqrt((line2[0] - line1[0])**2 + (line2[1] - line1[1])**2)

    def line_comparator(self):
        length = self.line_length_calculator(self.line_inputs("x1", "y1"), self.line_inputs("x2", "y2"))
        print(length)


if __name__ == "__main__":
    LineComparison().line_comparator()
