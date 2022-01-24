import logging
import math


class LineComparison:

    logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.DEBUG)

    @staticmethod
    def line_inputs(x):
        """
        Get's the user input
        :param x: point to get
        :return: point value
        """
        try:
            x = int(input(f"Enter {x} value "))
            return x
        except Exception:
            logging.exception(msg="Error while getting input")
            print("Enter integer values")
            return LineComparison.line_inputs(x)

    @staticmethod
    def line_length_calculator(point1, point2):
        """
        Calculates line length based on two given points
        :param point1:
        :param point2:
        :return: line length
        """
        try:
            return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
        except Exception:
            logging.exception(msg="Error while getting input")
            print("Math error")

    def line_comparator(self):
        """
        Compares line lengths
        :return: prints the comparison
        """
        line1 = self.line_length_calculator([self.line_inputs("x1"), self.line_inputs("y1")],
                                            [self.line_inputs("x2"), self.line_inputs("y2")])
        line2 = self.line_length_calculator([self.line_inputs("x3"), self.line_inputs("y3")],
                                            [self.line_inputs("x4"), self.line_inputs("y4")])
        print(f"Line1 length is {line1}")
        print(f"Line2 length is {line2}")
        try:
            if line1 == line2:
                print("Lines are equal")
            elif line1 > line2:
                print("Line1 is greater than line2")
            else:
                print("Line2 is greater than line1")

        except Exception:
            logging.exception(msg="Error at line comparison")
            print("Values cannot be compared")


if __name__ == "__main__":
    LineComparison().line_comparator()
